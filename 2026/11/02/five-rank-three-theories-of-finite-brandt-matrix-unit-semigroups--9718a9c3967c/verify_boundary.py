"""Independent explicit-sentence and one-exception case checks for matrix-unit semigroups."""
ZERO=None

def mul(a,b):
 if a is None or b is None:return None
 if a[1]!=b[0]:return None
 return (a[0],b[1])

def atomic(x):
 xs=(None,)+x
 return (tuple(a==b for a in xs for b in xs), tuple(mul(a,b)==c for a in xs for b in xs for c in xs))

def idem(z):return z is not None and mul(z,z)==z

def end(z,x):return mul(z,x)==x or mul(x,z)==x

def cutoff_tests(n):
 S=[None]+[(i,j) for i in range(n) for j in range(n)]
 is_one=not any(x is not None and mul(x,x) is None for x in S)
 at_most_two=any(x is not None and all(not idem(y) or end(y,x) for y in S) for x in S)
 at_most_three=any(x is not None and idem(y) and all(not idem(z) or end(z,x) or z==y for z in S) for x in S for y in S)
 at_most_four=any(x is not None and y is not None and all(not idem(z) or end(z,x) or end(z,y) for z in S) for x in S for y in S)
 return [is_one,at_most_two,at_most_three,at_most_four]

assert atomic(((0,1),(2,3),(4,5)))==atomic(((0,1),(2,3),(0,4)))
for n in range(1,10):
 v=cutoff_tests(n)
 assert v == [n<=k for k in [1,2,3,4]]
 print('n',n,'boundary_formulas',v)
print('EXCEPTIONAL_THIRD_MOVE_ATOMS_MATCH')
print('EXPLICIT_BOUNDARY_CHECKS_PASS')
