# Independent mathematical audit

## correctness

PASS

For s=min_i n_i=2, choose one 2-part with 3,2 and one vertex in another part with 2, giving feasible weight 7; published Propositions 11/12 exclude minima 5 and 6 and standard total lower bound excludes smaller. For s>=3, a 4-4 pair across distinct parts gives 8. Put q=#positive, E=sum_P(f-1), E_i in part i. For every zero in part i, cancellation converts required f(N[v])>=|AN(v)|+3 to E-E_i>=3; for supported f(x)<3, f(x)+E-E_i>=3. A fully positive part forces weight>=8 after the case split; otherwise for two supported parts E_i,E_j>=3 gives q+E>=8, and for at least three parts sum of three zero inequalities gives E>=5 and q>=3. Independently exhaustive definition-level search of bounded labelings confirmed minima 7 for (2,2),(2,3),(2,2,2),(2,3,3) and 8 for (3,3),(3,3,3); 10,988 candidate labelings through first solution in (3,3,3). The proof is universal, not finite extrapolation.

## originality

PASS

Structured searches compared exact claims and implications; see named checks and inspection evidence. Best-of-knowledge only; residual literature-priority risks remain.

## value

PASS

Complete connected multipartite family (without singleton parts) has an exact sharp one-unit structural threshold at smallest part size 2, refining initiating total-triple Roman invariants. It is a natural infinite graph class and motivated domination invariant; the excess argument and boundary distinction are not just a reparametrized known total Roman formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
