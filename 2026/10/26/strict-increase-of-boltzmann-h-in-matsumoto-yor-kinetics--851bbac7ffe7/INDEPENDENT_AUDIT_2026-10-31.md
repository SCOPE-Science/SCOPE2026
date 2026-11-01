# Independent mathematical audit

## correctness

PASS

PASS: Direct differentiation verifies ψ(x,y)=(1/(x+y),y/[x(x+y)]) is involutive with signed determinant -1/[x²(x+y)²], so the gain-map Jacobian is its absolute j=1/[x²(x+y)²]. The energy x+y+1/x and ratio y/x invariants and monomial Jacobian show GIG(p,c)⊗Gamma(p,c) product q is exactly invariant under density pushforward K. The loss/gain marginal equations yield F'=∫(Kg-g)log(g/q)=-KL(g||Kg) and H'=F'-E_g log j. At perturbed product gε=q(1+εh(x)), h(x)=x/(1+x)-E_qX[x/(1+x)] is bounded smooth increasing; m(x)=E_qY log j(x,Y) is strictly decreasing since m'=-2/x-2E(1/(x+Y))<0. Thus B=-Cov_qX(h,m)>0. The KL defect ≤4ε²/(1-ε); for sufficiently small ε>0, H'(0)=εB-KL>0 for every p,c>0. Independent symbolic involution, Jacobian, invariance checks verify the algebra; sign proof is analytic, not numerical. Relative-entropy identity is not a convergence-rate theorem.

## originality

PASS

PASS, qualified: The October 9 2026 same mathematical model Itoh arXiv primary manuscript was read in complete HTML, including its equation (7)-(8) identical coupled kinetic gain-minus-loss model, and Section 3.3 equation (10) explicitly defines unweighted Lebesgue H=∫fX log fX+∫fY log fY and asserts H' is nonpositive symmetrized production. The present proof identifies the omitted nonzero logarithmic-Jacobian expectation and constructs positive H'(0) arbitrarily near every balanced equilibrium. This precisely contradicts Eq (10) for its stated H (not a guessed alternative measure), while explaining why the corresponding relative entropy has its claimed dissipation. Itoh's conic invariant measure and the GIG/Gamma law are prior mathematics. Standard data-processing alone does not exhibit the positive-H counterexample. A future corrigendum/earlier refutation remains a priority risk.

## value

PASS

PASS: A concrete, sign-definite counterexample to using unweighted entropy as a Lyapunov function for a named non-volume-preserving kinetic involution is mathematically and physically consequential. The exact corrective KL dissipation law identifies the appropriate stationary reference and Jacobian term, providing a reusable distinction between Lebesgue entropy and invariant-measure entropy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
