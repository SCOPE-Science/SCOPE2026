# Review of the all-stage Gauss–Legendre complete-multipartite positivity theorem

## Correctness

**PASS.** The stability polynomial has exact factorial coefficients. Odd/even coefficient ratios increase strictly, making the rational deficit quotient strictly decreasing for all integer stage counts. An integral representation proves strict scalar positivity for every even stage. Spectral projectors yield explicit positive off-diagonal entries for every unit-edge complete multipartite graph, and positive definiteness supplies the diagonals. The odd-stage large-step matrix limit is \(2J/n-I\); the even-stage \(P_4\) obstruction follows from the positive endpoint-neighbor entry \((L_{P_4}^\dagger)_{1,2}=1/8\). The packaged rational checker reconstructed 1,938 coefficient pairs, 4,656 strictly positive matrix entries, 3,904 exact projector identities, and 16 negative witnesses. These checks supplement rather than replace the proof.

## Originality

**PASS, with limited historical confidence.** Published general Runge–Kutta positivity-radius theory does not itself assert unconditional positivity on this fixed graph family. Earlier spectral multiplier criteria already explain how scalar monotonicity relates to graph positivity; that general criterion and the two-stage instance are not credited to this theorem. The new substantive step is a uniform, exact coefficient-ratio argument for every diagonal Padé approximant of the exponential, yielding the even/odd stage law. Searches of mathematical research records, related formula terminology, and primary full texts did not find an equivalent all-stage scalar result. This negative search is not proof of priority. Further specialist comparison remains desirable.

## Value

**PASS.** General Runge–Kutta positivity order barriers might suggest that arbitrarily high-order classical implicit schemes cannot remain positive for all timesteps. On the natural complete-multipartite network class, every even-stage Gauss method of order \(2s\) does so for its completed step. The parity obstruction and the \(P_4\) witness delimit the result. The all-order rational monotonicity lemma is useful as a scalable analytic sufficient condition, not merely a finite table entry.

## Scope and related literature

Horváth (1998), Lóczi–Ketcheson (arXiv:1303.6651v1), and Fekete–Ketcheson–Lóczi (arXiv:1610.00228v1) were compared with their actual investigated systems, algorithms, and conclusions. Existing general complete-multipartite multiplier formulas and the known two-stage positivity example limit the originality claim to the all-stage scalar lemma and parity consequences. The theorem does not address stagewise positivity, weighted or directed graphs, nonlinear dynamics, or arbitrary connected networks. An equivalent all-stage result elsewhere cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
