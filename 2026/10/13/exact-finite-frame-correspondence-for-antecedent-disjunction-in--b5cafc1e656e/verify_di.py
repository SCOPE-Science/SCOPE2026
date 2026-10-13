#!/usr/bin/env python3
"""Independent finite-frame checks for distributivity of flat strict implication.

No external packages or input files are required.
"""

def subsets(mask):
    a = mask
    while True:
        yield a
        if a == 0:
            return
        a = (a - 1) & mask


def bits(mask, n):
    return (i for i in range(n) if mask & (1 << i))


def proper_preorders(n):
    diag = sum(1 << (i*n+i) for i in range(n))
    for matrix in range(1 << (n*n)):
        if matrix & diag != diag:
            continue
        after = [sum((1 << j) for j in range(n)
                     if matrix & (1 << (i*n+j))) for i in range(n)]
        if all((after[i] | after[j]) == after[i]
               for i in range(n) for j in bits(after[i], n)):
            yield after


def ups_and_closure(after, n):
    whole = (1 << n) - 1
    upsets = [a for a in range(whole + 1)
              if all((after[i] & a) == after[i] for i in bits(a, n))]
    closure = [0] * (whole + 1)
    for a in range(whole + 1):
        for i in bits(a, n):
            closure[a] |= after[i]
    return upsets, closure


def compare_frame(n, after, relation, upsets, closure):
    h = [closure[z] for z in relation]
    iw = {}
    for w in range(n):
        upper = list(bits(after[w], n))
        iw[w] = {a: 0 for a in upsets}
        for a in upsets:
            for x in upper:
                if h[x] & ~a == 0:
                    iw[w][a] |= h[x]
    # Original modal clause, with all propositional valuations A,B,C.
    semantic = True
    for w in range(n):
        t = iw[w]
        for a in upsets:
            for b in upsets:
                for c in upsets:
                    if (t[a] & ~c == 0 and t[b] & ~c == 0
                            and t[a | b] & ~c != 0):
                        semantic = False
                        break
                if not semantic:
                    break
            if not semantic:
                break
        if not semantic:
            break
    # The proposed first-order cover property.
    structural = True
    for w in range(n):
        for x in bits(after[w], n):
            for u in bits(h[x], n):
                if not any((h[y] & (1 << u)) and not (h[y] & ~after[v])
                           for v in bits(h[x], n)
                           for y in bits(after[w], n)):
                    structural = False
                    break
            if not structural:
                break
        if not structural:
            break
    # Alternative Boolean-distributivity proof step.
    joined = all(iw[w][a | b] == (iw[w][a] | iw[w][b])
                 for w in range(n) for a in upsets for b in upsets)
    assert semantic == structural == joined, (n, after, relation, semantic, structural, joined)
    return semantic


def main():
    total = 0
    success = 0
    for n in (1, 2, 3):
        order_count = 0
        frame_count = 0
        for after in proper_preorders(n):
            order_count += 1
            upsets, closure = ups_and_closure(after, n)
            for z in range(1 << (n*n)):
                relation = [(z >> (i*n)) & ((1 << n)-1) for i in range(n)]
                success += compare_frame(n, after, relation, upsets, closure)
                total += 1
                frame_count += 1
        print('n=%d: preorders=%d, frames=%d' % (n, order_count, frame_count))
    # Three-point fork: w<a,w<b, H_w={a,b}, H_a={a}, H_b={b}.
    fork = [7,2,4]
    relation = [6,2,4]
    upsets, closure = ups_and_closure(fork, 3)
    assert compare_frame(3, fork, relation, upsets, closure)
    assert not any((fork[v] & relation[0]) and (fork[v] & relation[0]) == relation[0]
                   for v in bits(relation[0],3))
    print('fork: distributivity valid, R[w] not downward directed')
    print('VERIFY_OK: frames=%d; valid=%d; invalid=%d' % (total,success,total-success))

if __name__ == '__main__':
    main()
