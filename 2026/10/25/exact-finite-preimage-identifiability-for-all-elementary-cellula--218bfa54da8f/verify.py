#!/usr/bin/env python3
"""Exact predecessor-word and boundary-observability classification for ECA.

Usage: python verify.py [classification.csv]
Only Python standard library required. All calculations use exact integers.
"""
import csv
import io
import sys
from collections import Counter, deque
from pathlib import Path


def transitions(rule):
    # State 2*a+b records two consecutive input bits.
    by_label = [[], []]
    for label in (0, 1):
        back = [[] for _ in range(4)]
        for old in range(4):
            for new_bit in (0, 1):
                trip = 2*old + new_bit
                dest = 2*(old % 2) + new_bit
                if (rule >> trip) & 1 == label:
                    back[dest].append(old)
        by_label[label] = back
    return by_label


def count_machine(rule):
    back = transitions(rule)
    def step(state, bit):
        return tuple(min(2, sum(state[old] for old in back[bit][dest]))
                     for dest in range(4))
    return step


def full_preimage_shortest(rule):
    step = count_machine(rule)
    initial = (1, 1, 1, 1)
    pending = deque([(initial, '')])
    visited = {initial}
    first_length = None
    first_word = ''
    # Continue the closure even after finding a singleton-preimage output.
    while pending:
        state, word = pending.popleft()
        if sum(state) == 1 and first_length is None:
            first_length, first_word = len(word), word
        for label in (0, 1):
            nxt = step(state, label)
            if nxt not in visited:
                visited.add(nxt)
                pending.append((nxt, word + str(label)))
    assert len(visited) <= 3**4
    return first_length, first_word, len(visited)


def right_boundary_shortest(rule):
    by_label = transitions(rule)
    masks = []
    for label in (0, 1):
        mask = [0]*4
        for destination in range(4):
            for old in by_label[label][destination]:
                mask[old] |= (1 << destination)
        masks.append(mask)
    pending = deque([(15, '')])
    visited = {15}
    while pending:
        state, word = pending.popleft()
        if state and (state & (state-1)) == 0:
            return len(word), word
        for label in (0, 1):
            nxt = 0
            for old in range(4):
                if state & (1 << old):
                    nxt |= masks[label][old]
            if nxt not in visited:
                visited.add(nxt)
                pending.append((nxt, word + str(label)))
    return None, ''


def direct_unique_words(rule, n):
    # Independent exhaustive finite-word method, not using the count machine.
    counts = [0]*(1 << n)
    endpoints = [0]*(1 << n)
    for inp in range(1 << (n+2)):
        bits = [(inp >> (n+1-i)) & 1 for i in range(n+2)]
        output = 0
        for i in range(n):
            trip = (bits[i] << 2) | (bits[i+1] << 1) | bits[i+2]
            output = (output << 1) | ((rule >> trip) & 1)
        counts[output] += 1
        endpoints[output] |= (1 << ((bits[-2] << 1) | bits[-1]))
    unique = [format(i, '0%db' % n) for i, x in enumerate(counts) if x == 1]
    right_singletons = [format(i, '0%db' % n) for i, mask in enumerate(endpoints)
                       if mask and (mask & (mask-1)) == 0]
    return unique, right_singletons


def rows():
    result = []
    for rule in range(256):
        length, word, states = full_preimage_shortest(rule)
        right_length, right_word = right_boundary_shortest(rule)
        result.append({'rule': str(rule),
                       'unique_length': 'never' if length is None else str(length),
                       'unique_witness': word,
                       'reachable_count_states': str(states),
                       'right_boundary_length': 'never' if right_length is None else str(right_length),
                       'right_boundary_witness': right_word})
    return result


def csv_bytes(result):
    output = io.StringIO(newline='')
    writer = csv.DictWriter(output, fieldnames=['rule','unique_length','unique_witness',
        'reachable_count_states','right_boundary_length','right_boundary_witness'],
        lineterminator='\n')
    writer.writeheader()
    writer.writerows(result)
    return output.getvalue().encode('utf-8')


def verify(filename=None):
    result = rows()
    tally = Counter(row['unique_length'] for row in result)
    assert tally == {'never': 92, '1':16, '2':52, '3':56,
                     '4':28, '5':4, '6':8}, tally
    rtally = Counter(row['right_boundary_length'] for row in result)
    assert rtally == {'never':50,'1':24,'2':90,'3':72,'4':12,'5':4,'6':4}, rtally
    six = [int(row['rule']) for row in result if row['unique_length'] == '6']
    assert six == [37,57,91,99,156,164,198,218], six
    assert [result[r]['unique_witness'] for r in six] == [
        '100101','000100','010010','001000','000100','100101','001000','010010']
    diff = [int(row['rule']) for row in result if row['unique_length'] == 'never'
            and row['right_boundary_length'] != 'never']
    assert len(diff) == 42
    gap = Counter(int(row['unique_length']) - int(row['right_boundary_length'])
                for row in result if row['unique_length'] != 'never')
    assert gap == {0:132, 1:20, 2:8, 3:4}, gap
    assert max(int(row['reachable_count_states']) for row in result) == 66
    # A direct and independent complete enumeration for every output word at
    # all lengths up to six (and hence all claimed shortest lengths).
    checked_words = 0
    for rule in range(256):
        found = None
        found_right = None
        for length in range(1, 7):
            words, right_words = direct_unique_words(rule, length)
            checked_words += (1 << length)
            if words and found is None:
                found = (length, words[0])
            if right_words and found_right is None:
                found_right = (length, right_words[0])
        row = result[rule]
        alleged = None if row['unique_length'] == 'never' else (
            int(row['unique_length']), row['unique_witness'])
        alleged_right = None if row['right_boundary_length'] == 'never' else (
            int(row['right_boundary_length']), row['right_boundary_witness'])
        assert found == alleged, (rule, found, alleged)
        assert found_right == alleged_right, (rule, found_right, alleged_right)
    data = csv_bytes(result)
    if filename is not None:
        assert Path(filename).read_bytes() == data, 'CSV bytes differ'
    print('VERIFY_OK: 256 exhaustive capped-count-automaton closures; '
          '92 rules without finite unique antecedents; 164 with shortest witness <=6; '
          'sharp six-symbol rules=37,57,91,99,156,164,198,218; '
          '42 right-synchronizing rules without full unique preimages; '
          f'{checked_words} independent finite-word preimage-count checks; '
          f'largest reachability closure=66 states; CSV bytes matched={filename is not None}')
    return data

if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise SystemExit('Usage: python verify.py [classification.csv]')
    if len(sys.argv) == 2:
        verify(sys.argv[1])
    else:
        Path(__file__).with_name('classification.csv').write_bytes(verify())
