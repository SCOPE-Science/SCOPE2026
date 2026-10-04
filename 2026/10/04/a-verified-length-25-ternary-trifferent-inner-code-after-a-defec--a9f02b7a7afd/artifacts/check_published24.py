#!/usr/bin/env python3
ROWS = [
'101111101000011011111111',
'012200000101120112210201',
'121212202202012220112100',
'110110100011120021110011',
'220002101012122202102210',
'010002111020111202200000',
]
G=[[int(c) for c in row] for row in ROWS]
def codeword(u):
    return tuple(sum(u[i]*G[i][j] for i in range(6))%3 for j in range(24))
u=(0,1,1,0,0,0)  # row 2 + row 3
v=(1,0,0,1,0,0)  # row 1 + row 4
cu,cv=codeword(u),codeword(v)
su={i for i,x in enumerate(cu) if x}
sv={i for i,x in enumerate(cv) if x}
assert su < sv
print('u=(0,1,1,0,0,0), weight='+str(len(su)))
print('v=(1,0,0,1,0,0), weight='+str(len(sv)))
print('support(u)='+repr(sorted(su)))
print('support(v)='+repr(sorted(sv)))
print('strict_containment=yes')
print('PUBLISHED24_CHECK_OK')
