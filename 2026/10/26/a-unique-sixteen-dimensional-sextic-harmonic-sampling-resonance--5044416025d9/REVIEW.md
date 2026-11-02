# Independent mathematical audit

## correctness

PASS

With normalized Gegenbauer P_6(t), compute u=P_6(1/2)=(n^3-42n^2+224n+672)/(64(n-1)(n+1)(n+3)), v=P_6(0)=-15/((n-1)(n+1)(n+3)). Sign-difference edge vectors have eigenvalue 1-v. Sign-symmetric sector is (1+v)I+2u A_J+2v B_J on Johnson J(n,2), whose A_J eigenvalues 2(n-2),n-4,-2 and complementary B_J eigenvalues (n-2)(n-3)/2,-(n-3),1. This proves all four branches and multiplicities, not a fit to numerical eigenvalues. Symbolic substitution and factorization independently checked in SymPy, and remaining B cubic q(n) has q(5)=939>0 and q'(n)=3(n-6)^2+452>0, while all other positive factors are manifest. Thus A=(n-16)^2(n-2)(n+6)/(16(n-1)(n+1)(n+3)) alone vanishes at n16. Direct Gram numerics are supporting tests only. Exact normalization is probability surface L2 and f(x)/sqrt(h_n,6); dimensions n>=5.

## originality

PASS

Bannai–Okuda–Tagami arXiv:1308.5101 defines harmonic-index designs and Gegenbauer kernels; Zhu et al arXiv:1507.05373 studies tight degree-six designs and Gegenbauer formulas. These establish the language and techniques, not visibly the four specific D_n half-root eigenvalue branches or sole n=16 constant-zero sector. Johnson scheme spectral decomposition is standard and explicitly not new. A prior all-degree association-scheme eigenmatrix or root-system moment classification could imply the full answer even without the same wording; this is a real residual risk despite searching.

## value

PASS

Full harmonic sampling spectrum of a canonical family of D_n root shells is a natural analytic/combinatorial invariant. It yields an isolated rank obstruction in dimension sixteen and exact conditioning for all n>=5, more than an arbitrary finite computation or renaming of a known design. Clarifies harmonic-index 6 versus ordinary spherical 6-design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
