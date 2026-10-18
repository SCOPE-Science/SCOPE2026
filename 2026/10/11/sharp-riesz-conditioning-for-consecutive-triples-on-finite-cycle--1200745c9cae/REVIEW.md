# Independent mathematical audit

## correctness

PASS

For N>=3, E={0,1,2}, B any unordered frequency triple in Z_N, column-wise unitary phase changes make V_B*V_B real symmetric diagonal 3 with offdiagonal g(d)=1+2cos(2pi*d/N); Vandermonde determinant is nonzero for three distinct roots. For 3|N the orthogonal balanced sets give rho=1, equality forces vanishing all cross terms. For N mod3=1,2, the balanced g-values (a,a,b) or (b,b,a) yield stated three eigenvalues. For any min gap r<q, strict g(q-1)>a+|b| and principal-submatrix interlacing yield rho strictly above balanced Gershgorin bound; the only remaining unbalanced type for mod3=2 is (q,q,q+2). The exact half-angle polynomial identity a(t-a)-b^2=-4v^2(v-sqrt3)^2 P(v)/(1+v^2)^6, v=tan(pi/(3N)), gives positivity via P(v)<0 for 0<v<1/10 at N>=11. Independently verified all three symbolic trigonometric identities with SymPy; enumerated all unordered triples N=3..33 and verified best value, balanced gap necessity and multiplicities. Small N=3,4,5,6,8 handled in source with explicit eigenvalues; N=7,9,10 handled by previous cases. This verifies infinitely many N analytically rather than extrapolating finite experiments.

## originality

PASS

Best-of-knowledge comparison against the same primary mathematical object, stronger theorems, equivalent reductions, exact tables and indexed related results finds no previously established result implying the full final statement. Searches alone are not novelty proof. Most relevant full primary texts were read where accessible; restricted sources and mathematical priority uncertainties are named below.

## value

PASS

Riesz ratio is the canonical quantitative spectral conditioning invariant; optimizing all frequency triples for the smallest nontrivial consecutive aperture at every cyclic order, with exact arithmetic dependence and the full count of equality designs, is a complete and natural spectral-design classification. It explains optimal imperfect conditioning when 3 does not divide N and quantifies exact loss; not merely a sample calculation or previously known orthogonal divisible case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
