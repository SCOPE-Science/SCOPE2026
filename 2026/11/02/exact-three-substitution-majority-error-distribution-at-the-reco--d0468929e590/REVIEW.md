# Independent mathematical audit

## correctness

PASS

Translate the sent binary word to zero. The N distinct three-substitution outputs are a simple 3-uniform hypergraph on k labeled vertices; coordinate majority error is exactly degree >=H=b+1 for b=binom(k-2,2), N=2b+1. A one-vertex degree hypergeometric choice gives T1. Four edge classes relative to two vertices give T2 by selecting x common-pair edges and omitting i,j single-vertex edges. The maximum total incidences across any three vertices is N+3k-7 and is less than 3H for k>=9, bounding bad coordinates by two. For k=8 and 7, direct incident-edge maxima bound them by three and four. Exact coefficient extraction yields F3(7)=951125,F4(7)=4531,F3(8)=16003008. Binomial inversion of incidence counts I_j=binom(k,j)F_j yields every E_r. Independently recalculated T1,T2 for k=7..10, all E_r for k=7,8, the three exception counts using complementary omitted-edge dynamic programming, and three exact failure totals. The logarithmic asymptotic uses a sharp one-vertex tail and union bounds, not an independence assumption. Distinct unordered outputs, exact three different flips, k>=7 and threshold N are essential.

## originality

PASS

The 2026 Papadopoulou–Yehezkeally–Rameshwar–Wachter-Zeh article supplies the worst-case N and already tabulates the total k=7,t=3 majority failure count. It primarily obtains t=2 counts and labels t>2 counting open; its inspected Section III-C and tables do not give the all-k full coordinate-error distribution, the k=8/9 exact values or the large-k probability exponent. The known k=7 total is acknowledged prior, not presented as new.

## value

PASS

A pointwise decoding-performance distribution at the exact optimal reconstruction threshold is an independently useful finite and asymptotic coding invariant: it identifies how many coordinates fail, sharp error cutoffs and a super-exponentially rare failure event. That is materially more informative than existence of optimal decoding or a single short-block count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
