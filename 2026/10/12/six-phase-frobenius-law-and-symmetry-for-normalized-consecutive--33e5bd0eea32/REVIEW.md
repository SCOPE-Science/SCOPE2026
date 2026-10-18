# Independent mathematical audit

## correctness

PASS

For n=6k+r with n>=2 the given six factorizations of normalized (T_n,T_{n+1},T_{n+2}) correctly exhibit U=hu, V=hv and W in <u,v>, with gcd(u,v)=gcd(h,W)=1. The Apéry set with modulus hu is the rectangle {i hv+j W:0<=i<u,0<=j<h}: reduction absorbs hW into h<u,v>, and residue distinctness holds successively modulo h and u. Its maximum minus hu gives F=huv-hu-hv+(h-1)W; complementary indices certify symmetry and genus (F+1)/2. Substitution yields six cubics with leading coefficients 96,162,96,30,432,30 in k, and asymptotic n^-3 values 4/9,3/4,4/9,5/36,2,5/36. For n=2,3 the triples (2,5,10),(2,4,7) are 2-generated; for n>=7 increasing a<b<c<2a prevents redundancy, while n=4..6 checked separately. Independent exact Dijkstra shortest-residue Apéry computation for all n=2..35 matched six formulas (34 checks), with exact gcd normalization. This is bounded corroboration, not the reason the all-n result holds.

## originality

PASS

Robles-Pérez/Rosales arXiv:1706.04378, primary full PDF §3, explicitly computes four consecutive tetrahedral numbers, with same gcd/gluing toolkit; §2 computes three consecutive triangular numbers. This work instead normalizes the gcd of exactly three consecutive tetrahedral numbers and classifies all six congruence classes and semigroup symmetry. OEIS A069761 similarly addresses four tetrahedral terms. The general Apéry/gluing lemma and gcd techniques are classical, but the complete natural triple-family application does not follow directly from the four-generator formula.

## value

PASS

A complete exact Frobenius number, genus/symmetry and embedding-dimension classification for a natural missing three-term tetrahedral numerical-semigroup family. Six residue laws and four asymptotic phases are useful invariants beyond a small table; no downstream theorem requirement is imposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
