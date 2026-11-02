#!/usr/bin/env python3
"""Generate adaptive comparison-shattering witnesses; self-contained."""
import json
from verify_even_orders import EXPECTED, exact_search

def generate(n):
    words, domain, qmasks, sigs, full, wins = exact_search(n)
    def rec(mask, depth):
        if depth==0:
            ix = (mask & -mask).bit_length()-1
            return {'witness':list(words[ix])}
        choices = []
        for i,q in enumerate(qmasks):
            yes = mask&q
            no = mask^yes
            if yes.bit_count() < 1 << (depth-1) or no.bit_count() < 1 << (depth-1):continue
            choices.append((abs(yes.bit_count()-no.bit_count()),i,yes,no))
        for _,i,yes,no in sorted(choices):
            if wins(yes,depth-1) and wins(no,depth-1):
                return {'query':list(domain[i]), '0':rec(no,depth-1), '1':rec(yes,depth-1)}
        raise AssertionError((n,depth))
    return rec(full, EXPECTED[n])

if __name__ == '__main__':
    trees = {str(n):generate(n) for n in EXPECTED if EXPECTED[n]>0}
    with open('trees.json','w',encoding='utf8') as f:
        json.dump(trees,f,ensure_ascii=False,separators=(',',':'))
        f.write('\n')
    print('generated', len(trees),'trees')
