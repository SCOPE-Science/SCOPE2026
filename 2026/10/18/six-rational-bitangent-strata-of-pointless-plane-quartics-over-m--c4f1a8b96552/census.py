#!/usr/bin/env python3
from bitangent import summarize
from collections import Counter
from pathlib import Path
lines=Path(__file__).with_name('curves_f5.txt').read_text().splitlines()
assert len(lines)==31,len(lines)
counts=[]
for i,L in enumerate(lines,1):
 n,lb=summarize(L)
 counts.append(n)
 print(i,n,flush=True)
print('DISTRIBUTION',dict(sorted(Counter(counts).items())))
print('MAX',max(counts),'AT',[i+1 for i,n in enumerate(counts) if n==max(counts)])
