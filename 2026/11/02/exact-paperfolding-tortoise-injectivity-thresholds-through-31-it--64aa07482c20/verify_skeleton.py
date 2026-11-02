#!/usr/bin/env python3
"""Exhaustive factor-skeleton check for paperfolding tortoise injectivity.
No external packages or network access are required.
"""
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import csv

TARGETS = [8,13,14,25,26,28,29,49,50,52,53,56,57,58,61,
           97,98,100,101,104,105,106,109,112,113,114,116,117,121,122,125]


def paperfolding(index):
    assert index >= 1
    while index % 2 == 0:
        index //= 2
    return 0 if index % 4 == 1 else 1


def factors(n):
    # Because n < 2^h, a length-n window has at most one index
    # divisible by 2^h. All its other letters are P=2^(h+1)-periodic.
    h = n.bit_length()
    assert n < (1 << h)
    period = 1 << (h+1)
    result = set()
    for start in range(1, period + 1):
        word = [None if (start+j) % (1 << h) == 0
                else paperfolding(start+j) for j in range(n)]
        holes = [j for j,a in enumerate(word) if a is None]
        assert len(holes) <= 1
        if not holes:
            result.add(bytes(word))
        else:
            q = holes[0]
            for b in (0,1):
                word[q] = b
                result.add(bytes(word))
    return result


def kth_tortoise(word, k):
    # Exact identity: T^k deletes the first min(k, number of ones)
    # occurrences of 1 and appends that many ones.
    ans = bytearray()
    removed = 0
    for x in word:
        if x == 1 and removed < k:
            removed += 1
        else:
            ans.append(x)
    ans.extend([1]*removed)
    return bytes(ans)


def collision(words,k):
    seen={}
    for word in sorted(words):
        image=kth_tortoise(word,k)
        other=seen.get(image)
        if other is not None and other!=word:
            return other,word,image
        seen[image]=word
    return None


def bitstr(b):
    return ''.join(map(str,b))


def main():
    out=[]
    for k,threshold in enumerate(TARGETS,1):
        prev=factors(threshold-1)
        at=factors(threshold)
        assert len(prev)==4*(threshold-1), (k,threshold,'previous factor count')
        assert len(at)==4*threshold, (k,threshold,'factor count')
        c=collision(prev,k)
        assert c is not None, (k,threshold,'missing previous collision')
        assert collision(at,k) is None, (k,threshold,'threshold collision')
        minones=min(w.count(1) for w in at)
        assert minones>=k, (k,threshold,minones)
        a,b,img=c
        assert a!=b and kth_tortoise(a,k)==kth_tortoise(b,k)
        out.append({'k':k,'threshold':threshold,
          'factors_previous':len(prev),'factors_at_threshold':len(at),
          'minimum_ones_at_threshold':minones,
          'collision_predecessor_first':bitstr(a),
          'collision_predecessor_second':bitstr(b)})
    with open('threshold_table.csv','w',newline='',encoding='utf-8') as file:
        wr=csv.DictWriter(file,fieldnames=list(out[0]));wr.writeheader();wr.writerows(out)
    digest=sha256(Path('threshold_table.csv').read_bytes()).hexdigest()
    print('SKELETON_OK depths=1..31, all 31 thresholds proved; table_sha256='+digest)
    print('thresholds='+','.join(str(x) for x in TARGETS))

if __name__=='__main__':main()
