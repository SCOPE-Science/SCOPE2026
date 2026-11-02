MU={'0':'01','1':'02','2':'0'}
PAIRS=('00','01','02','10','20')

def morph(s):return ''.join(MU[c] for c in s)
def triple_census(C):
 block={c:c for c in '012'}
 k=0
 while min(map(len,block.values()))<C+1:
  block={c:morph(block[c]) for c in '012'};k+=1
 covered=set()
 for a,b in PAIRS:
  t=block[a]+block[b]
  covered.update(t[i:i+C+1] for i in range(len(t)-C))
 MASK=(1<<(C+1))-2
 allowed=[]
 for w in covered:
  m=0
  for d in range(1,C+1):
   if w[d]==w[0]:m|=1<<d
  allowed.append(m)
 # group equal allowed masks, no scientific reliance on count
 allowed=list(set(allowed))
 result=[]
 for a in range(1,C-1):
  for b in range(a+1,C):
   mask=MASK & ~((1<<(b+1))-1)
   for m in allowed:
    if not (m>>a&1 or m>>b&1):
     mask&=m
     if not mask:break
   while mask:
    bit=mask&-mask
    c=bit.bit_length()-1
    result.append((a,b,c))
    mask^=bit
 result.sort()
 return k,block,len(covered),len(allowed),result

if __name__=='__main__':
 import sys
 if len(sys.argv)!=2:
  raise SystemExit('Usage: python3 census.py triples.csv')
 C=1705
 k,blocks,nw,nm,rows=triple_census(C)
 assert k==14 and nw==3413 and nm==3409 and len(rows)==145217
 from pathlib import Path
 Path(sys.argv[1]).write_text('a,b,c\n'+''.join(f'{a},{b},{c}\n' for a,b,c in rows),encoding='ascii')
 print('CENSUS_OK',len(rows))
