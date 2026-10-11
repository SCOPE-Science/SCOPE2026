from itertools import combinations
from collections import Counter

RAW = """1256 12512 12612 1378 13711 13811 1456 14516
14612 141013 141016 141213 151213 151316 1789 17911
18914 181014 181015 181115 191115 191415 1101314 1101516
1131416 1141516 23413 23415 231315 2478 24715 24816
241013 241016 25614 251214 26812 26816 26914 26916
2789 27910 271013 271315 28914 281214 291016 341213
341215 3567 35614 3578 35811 351114 36716 36914
36916 371114 371416 391213 391216 391315 391415 3121516
3141516 4567 4578 45816 46715 461215 581113 581316
5111213 5111214 671315 671316 681215 681315 681316 791012
791112 7101214 7101314 7111214 7131416 8101214 8101215 8111315
9101216 9111213 9111315 10121516""".split()

SOURCE_BOUNDARY = {
 (2,5,6),(2,5,12),(2,6,12),(3,7,8),(3,7,11),(3,8,11),
 (4,5,6),(4,5,16),(4,6,12),(4,10,13),(4,10,16),(4,12,13),
 (5,12,13),(5,13,16),(7,8,9),(7,9,11),(8,9,14),(8,10,14),
 (8,10,15),(8,11,15),(9,11,15),(9,14,15),(10,13,14),
 (10,15,16),(13,14,16),(14,15,16)
}

def parse_token(s):
    ans=[]
    def rec(pos,last,a):
        if len(a)==4:
            if pos==len(s): ans.append(tuple(a))
            return
        for width in (1,2):
            if pos+width<=len(s) and s[pos] != '0':
                v=int(s[pos:pos+width])
                if last < v <= 16:
                    rec(pos+width,v,a+[v])
    rec(0,0,[])
    assert len(ans)==1,(s,ans)
    return ans[0]

sphere=[parse_token(s) for s in RAW]
assert len(sphere)==92 and len(set(sphere))==92
ball=[f for f in sphere if 1 not in f]
assert len(ball)==66
vertices=set().union(*map(set,ball))
assert vertices==set(range(2,17))

faces=[]
for k in range(1,5):
    q=set()
    for tet in ball: q.update(combinations(tet,k))
    faces.append(q)
assert tuple(map(len,faces))==(15,93,145,66)

tri_inc=Counter()
for tet in ball:
    tri_inc.update(combinations(tet,3))
boundary_triangles={t for t,c in tri_inc.items() if c==1}
assert boundary_triangles==SOURCE_BOUNDARY
boundary_edges=set()
for tri in boundary_triangles: boundary_edges.update(combinations(tri,2))
assert len(boundary_edges)==39
all_edges=faces[1]
interior_edges=all_edges-boundary_edges
assert len(interior_edges)==54

degree=Counter()
for tet in ball:
    degree.update(combinations(tet,2))
hist=Counter(degree[e] for e in interior_edges)
assert hist==Counter({3:1,4:14,5:21,6:13,7:5}),hist
mins=sorted(e for e in interior_edges if degree[e]==3)
assert mins==[(2,3)]
incident=sorted(t for t in ball if {2,3}.issubset(t))
assert incident==[(2,3,4,13),(2,3,4,15),(2,3,13,15)]
link_edges=set()
for tet in incident:
    link_edges.add(tuple(sorted(set(tet)-{2,3})))
assert link_edges=={(4,13),(4,15),(13,15)}
print('VERIFY_OK sphere_facets=92 ball_f=15,93,145,66 boundary_triangles=26 boundary_edges=39 interior_edges=54 degree_hist=3:1,4:14,5:21,6:13,7:5 unique_degree3=2-3 link=4-13-15')
