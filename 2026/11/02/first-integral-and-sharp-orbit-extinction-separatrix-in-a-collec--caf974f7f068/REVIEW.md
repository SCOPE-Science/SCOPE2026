# Independent mathematical audit

## correctness

PASS

PASS. For N>=3, 2<=M<N, alpha=M-1>0, beta=N-M>0, 0<c<h(p), eps,b>0 and critical u=alpha/beta, direct differentiation of I=((1-r)/r)^(beta*c/eps), h(x), and the stated H yields H_x*x_dot+H_r*r_dot=0 identically (independently checked in a nontrivial exact SymPy model N=6,M=3). h(x) is strictly unimodal; G(r)=H(p,r) has unique minimum r*=c/h(p), G->+infty as r->0 and finite H_sep as r->1. For Hmin<E<Hsep, the two x branches glue into a regular compact oval with nonvanishing flow and hence a periodic orbit. At Hsep the boundary asymptotic gives h(x)->c, connecting (x2,1) backward to (x1,1) forward; above it branches approach x=1 and x=0, forward flow entering the x=0 branch and r->1. Logistic factors ensure no finite-time boundary crossing. The limit E=Hmin is exactly the center. It rules out an attracting isolated cycle at this exact critical u, not in nearby off-critical systems.

## originality

PASS

PASS best-of-knowledge. The complete same-model eLife 2023 article and Appendix 1 explicitly identify critical u and a numerical negative first Lyapunov coefficient, interpreting a stable emerging limit cycle; they do not exhibit an exact first integral or the Hmin/Hsep trichotomy. Their reported numerical coefficient (~ -1.4e-8) cannot overturn an exact conserved quantity. Weitz 2016 obtains neutral cycles in a distinct factorable matrix-payoff environment system, not this binomial group-payoff risk ODE. Possible later re-derivation remains a risk.

## value

PASS

PASS. A global first integral and sharp energy separatrix rigorously resolve an apparent nearly-degenerate numerical Hopf conclusion in a natural nonlinear collective-risk game. The result distinguishes neutral coexistence oscillations from maximal-risk extinction throughout the interior and has a substantive bifurcation interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
