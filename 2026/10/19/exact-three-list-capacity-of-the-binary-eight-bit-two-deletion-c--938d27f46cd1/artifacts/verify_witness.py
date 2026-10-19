from itertools import combinations
wordlist='''00000000 00000001 00000111 00001000 00010111 00011111 00110001 00111101 01001010 01101010 01110000 01111111 10001100 10010011 10110101 10111100 11000010 11001110 11010011 11100000 11101111 11110100 11111111'''.split()
W=[99,36,4,36,16,0,0,63,16,0,0,0,4,17,32,36,4,0,0,17,0,5,18,0,0,30,18,0,32,0,10,36,36,10,0,32,0,18,30,0,0,18,5,0,17,0,0,4,36,32,17,4,0,0,0,16,63,0,0,16,36,4,36,99]
assert len(wordlist)==23 and len(set(wordlist))==23 and all(len(t)==8 for t in wordlist)
assert len(W)==64
# explicit position-set deletion, independent of greedy subsequence membership
D=lambda x:{''.join(x[i] for i in keep) for keep in combinations(range(8),6)}
occ={format(i,'06b'):0 for i in range(64)}
for x in wordlist:
 for y in D(x):occ[y]+=1
assert max(occ.values())<=3
print('WITNESS_OK n=8 words=23 max_list=',max(occ.values()), 'occupied=',sum(bool(i) for i in occ.values()))
assert 3*sum(W)+72==3246
sl=[]
for i in range(256):
 s=format(i,'08b')
 paths=D(s)
 v=sum(W[int(t,2)] for t in paths)+(36 if i in (0,255) else 0)-135
 assert v>=0,(i,v)
 sl.append(v)
print('DUAL_OK objective=3246/135=',3246/135,'zeros=',sum(v==0 for v in sl),'small=',sum(0<v<=6 for v in sl),'min_nonzero=',min(v for v in sl if v>0))
print('small positive values',{i:sum(v==i for v in sl) for i in range(1,7)})

# Independent exact rational feasible point of the 256-variable LP relaxation.
primal_denominator = 35865
primal_numerators = {0: 35865, 1: 5973, 7: 35865, 8: 31830, 14: 15236, 16: 14249, 23: 5163, 31: 35865, 49: 30065, 52: 4438, 54: 15236, 61: 35865, 67: 35692, 74: 15286, 82: 18719, 84: 8294, 86: 9122, 105: 797, 106: 4122, 108: 16064, 112: 15355, 115: 31339, 127: 4526, 128: 19678, 140: 33498, 143: 15466, 147: 15639, 149: 2036, 150: 797, 169: 7036, 173: 19955, 181: 15517, 188: 27186, 194: 26524, 201: 20668, 203: 3950, 206: 26901, 211: 517, 213: 6711, 224: 27895, 231: 1870, 239: 29471, 240: 17153, 241: 11327, 247: 18220, 248: 35865, 254: 17643, 255: 35865}
assert len(primal_numerators) == 48
assert sum(primal_numerators.values()) == 862354
assert all(0 <= u <= primal_denominator for u in primal_numerators.values())
for sixbits in range(64):
    yy = format(sixbits, "06b")
    load = sum(u for x,u in primal_numerators.items() if yy in D(format(x,"08b")))
    assert load <= 3 * primal_denominator, (sixbits, load)
assert 862354*45 == 1082*35865
print("LP_PRIMAL_OK 48 nonzeros exact optimum=1082/45")
