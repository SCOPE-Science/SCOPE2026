# Independent mathematical audit

## correctness

PASS

For the published active-sector thermodynamic flux, the positive root parametrization rho=s(1+qs)/(1+2s+qs^2) is strictly increasing 0 to1. Direct symbolic differentiation of j=q s^2(s+2+qs)/[(1+s)(1+qs)(1+2s+qs^2)] equals -q s P_q(s) over a positive squared denominator. The quintic P has signs (+,+,-,-,-,-) for all q>0 and P(0)=-4, so exactly one positive root gives the unique global maximum; q=1 gives s=2,rho=2/3,j=8/27. Singular substitutions s=u/q at q->0 and s=q^(-1/3)u at q->infty give limiting root factors u^3(u^2-2) and u^2(u^3-2), respectively; positive root uniqueness and bracketing prove limit constants. The q(1-rho)->xi boundary layer follows by solving a limiting quadratic, with xi=0 treated separately. An independently written SymPy checker re-derived derivative, benchmark factorization, density monotonicity and both asymptotic polynomial identities. No finite computation substitutes for Descartes/root limits.

## originality

PASS

Ngoc–Nhung–Thi 2026 Theorem 4 provides the exact density-current relation and exhibits maximum density above 1/2, plus pointwise q->infinity behavior. It does not establish the unique global maximizer at every q through a sign-regular quintic, sharp cube-root constants, or a distinct q^-1 boundary layer. The contribution is calculus on an already-known physical observable; Gibbs measure and current formula are prior work.

## value

PASS

The current-maximizing density and maximal throughput are natural operational observables of the model. Unique optimum at every rate and sharp singular scaling resolve nonuniformity concealed by the source paper pointwise q->infinity limit; the distinct q^-1 and q^-1/3 density scales have mathematical and modeling significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
