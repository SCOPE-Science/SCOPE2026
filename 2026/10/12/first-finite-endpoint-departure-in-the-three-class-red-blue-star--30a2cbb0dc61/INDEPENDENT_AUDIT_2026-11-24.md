# Independent mathematical audit

## correctness

PASS

For center degree d the two red leaves can be chosen in d(d−1) ordered ways and the blue leaf in n−1−d ways, disjoint from both red leaves. Degrees on A,B,C are n−1,a+b−1,a on the nonempty classes, with m=binom(a+b,2)+ac, including the zero-class cases. Independently exhausted (a,h) with 0≤a≤h≤n and (a,b,c)=(a,h−a,n−h). For each order I constructed actual adjacency matrices: a pair u<v is in H iff u<a or v<h, and Q and S use the first and last m pairs in order of increasing v then u, respectively. The first m pairs give exactly the full clique and partial next vertex, including m=0 and complete graphs; the last m are the complement of the first binom(n,2)−m. The exact run covered 1767 triples; none improved on both endpoints through n=19. The complete n=20 output in (a,b,c;m;H,Q,S) order is (6,12,2;165;7308,7860,7344) and (7,11,2;167;6992,7370,7072). Literal ordered four-vertex counts checked all three graphs for each witness and every profile through n=8. The frozen enumeration and recorded log agree; the independent enumeration did not execute the frozen script.

## originality

PASS

The edge family, general counting identity and asymptotic endpoint departure are already known. Credit only the exact finite onset and complete census at the first order in that family. The strongest inspected primary statements and the indexed search did not establish this finite claim.

## value

PASS

This is the least exact order realizing the documented asymptotic failure in its natural witness family. The full first-order classification and fixed edge counts give small reproducible tests for discrete endpoint conjectures or algorithms. The value is the sharp cutoff with all first witnesses, not the small absolute score gains or the reuse of the known construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
