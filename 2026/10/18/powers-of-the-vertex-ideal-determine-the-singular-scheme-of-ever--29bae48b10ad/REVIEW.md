# Independent mathematical audit

## correctness

PASS

PASS: For k algebraically closed of characteristic zero and a,b>=2 the dimension d=a+b-1, codimension c=(a-1)(b-1) rank-one determinantal presentation supplies a c-minor Jacobian Fitting ideal. Each Jacobian entry is linear, giving Fitt_d(Omega_A) subset m^c. The c anchored quadrics z11*zij-zi1*z1j have the interior-column Jacobian matrix z11 I_c; its determinant z11^c is a nonzero class in A. The intrinsic Fitting ideal is GL_a x GL_b stable; its degree-c piece is a nonzero submodule of Sym^c(k^a) tensor Sym^c(k^b), which is an irreducible product-group representation in char0. Thus the entire A_c occurs and m^c subset Fitt; equality follows. This representation-theoretic step, rather than any finite calculation, covers all a,b. Counting degree t monomials u^alpha v^beta yields length L=sum_{t<c}binom(a+t-1,t)binom(b+t-1,t). On each projective chart z_B !=0 of Delta(r,n), all ratios are products of single-exchange t_j/t_i; the row/column toric relations are 2x2 minors (contingency 2x2 swaps), so the local ring is A_{r,n-r}. Its only singular point is the rank-zero origin. Disjoint local lengths yield total binom(n,r)L. Independent symbolic derivative checks of rectangles (2,2),(2,3),(2,4),(3,3),(3,4) confirmed the distinguished diagonal pivot and exact lengths 1,7,39,146,1974; these sample checks are not an infinite proof. Scope 2<=r<=n-2; r=1,n-1 smooth. Does not claim a characteristic-p version or Hilbert-Samuel multiplicity.

## originality

PASS

PASS (qualified): the uniform identification of the differential Fitting ideal with the cth maximal-ideal power and consequent nonreduced scheme colength is more specific than the classical rank-one Segre charts, toric equations, and hypersimplex secant/symbolic-square ideals. Full arXiv HTML of Sullivant 0804.2897v2 concerns Groebner bases for secant and symbolic-square ideals of the second hypersimplex, not Fitt_d(Omega) of the unsecanted toric variety. Results for reduced singular supports or Hilbert-Samuel multiplicities do not imply the nonreduced Fitting length. This is best-of-knowledge only: a general determinantal Jacobian/Fitting-ideal theorem, possibly in Bruns-Vetter, could implicitly yield the result and was not fully checked.

## value

PASS

PASS: The intrinsic nonreduced singular scheme distinguishes a toric singular support of binom(n,r) isolated reduced points from its infinitesimal structure; the uniform nilpotence exponent and scheme lengths (e.g. n=6,r=3 gives 20 points of length 146, degree 2920) are natural numerical singularity invariants. A chart-wise representation-theoretic identity across all rectangular ranks is more than merely observing the already known reduced torus fixed points. It does not assert a new toric chart description alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
