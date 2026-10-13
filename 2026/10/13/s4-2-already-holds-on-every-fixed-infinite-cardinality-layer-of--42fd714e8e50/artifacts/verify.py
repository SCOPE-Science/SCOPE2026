from itertools import product
checks=0
for n in range(4):
  for m in range(4):
    states=[(b,s) for b in range(1<<n) for s in range(1<<m)]
    def le(x,y): return (x[0] & ~y[0])==0
    for x in states:
      assert le(x,x); checks+=1
    for x in states:
      for y in states:
        if not le(x,y): continue
        for z in states:
          if le(y,z): assert le(x,z); checks+=1
    for x in states:
      for y in states:
        z=(x[0]|y[0],0)
        assert le(x,z) and le(y,z); checks+=2
    arrows=sum(le(x,y) for x in states for y in states)
    assert arrows==(3**n)*(4**m); checks+=1
    for x in states:
      for c in range(1<<n):
        if x[0] & ~c: continue
        for t in range(1<<m):
          assert le(x,(c,t)); checks+=1
print(f"VERIFY_OK {checks} exact assertions")
