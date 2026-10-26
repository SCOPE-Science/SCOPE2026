# Boundary-twist cancellation for exact-two public-goods equilibria on Möbius ladders

## Finding
For each integer \(n\ge3\), compare the prism \(C_n\square K_2\) with the Möbius ladder obtained by crossing the two horizontal closing edges of the same two-row strip. At each vertex, the sole best response is to produce, denoted by \(1\), exactly when **two** of its **three open neighbors** produce. Count labeled pure Nash equilibria by their total number of producers, with \(P_n^{\mathrm{pr}}(z)\) and \(P_n^{\mathrm{Mo}}(z)\) denoting the respective producer-count polynomials. Put
\[
Q_n(z)=\sum_{j=0}^{\lfloor n/4\rfloor}\frac{n}{n-3j}\binom{n-3j}{j}z^{4j}.
\]
Then the two exact distributions are
\[
P_n^{\mathrm{pr}}(z)=Q_n(z)+2z^n+4\mathbf1_{4\mid n}z^{3n/2},
\qquad P_n^{\mathrm{Mo}}(z)=Q_n(z)+4\mathbf1_{n\equiv2\pmod4}z^{3n/2}.
\]
In particular, the **boundary-twist defect identity** is
\[
\boxed{P_n^{\mathrm{Mo}}(z)-P_n^{\mathrm{pr}}(z)
=-2z^n+4\bigl(\mathbf1_{n\equiv2\pmod4}-\mathbf1_{4\mid n}\bigr)z^{3n/2}.}
\]
Indicator-controlled terms are absent whenever their indicator vanishes (in particular, fractional exponents in the displayed shorthand are never used for odd \(n\)). Thus the complete producer-count distributions differ only at the two specified degrees, with all other coefficients exactly identical. The difference in total equilibrium counts is \(-2\) for odd \(n\), \(-6\) for \(n\equiv0\pmod4\), and \(+2\) for \(n\equiv2\pmod4\). These are differences of counts, **not** a claimed bijection or overlap of individual labeled strategy profiles. Both total counts grow as \(\alpha^n(1+o(1))\), where \(\alpha\approx1.380277569\) is the dominant root of \(\lambda^4-\lambda^3-1=0\); consequently the relative count defect vanishes exponentially.

## Assumptions and scope
A row-pair column is \(v_j=(a_j,b_j)\in\{0,1\}^2\), for \(j=0,\ldots,n-1\). There are vertical edges \(a_jb_j\) and horizontal edges between successive columns. The prism identifies \(a_{n}=a_0,b_n=b_0\); the Möbius ladder identifies \(a_n=b_0,b_n=a_0\), together with the corresponding predecessor identifications. Each is an undirected simple cubic graph for \(n\ge3\). The best response to \(k\in\{0,1,2,3\}\) active open neighbors is \(T(k)=\mathbf1_{\{2\}}(k)\); there are no indifferences. Vertices are labeled: no quotient by automorphisms or interchange of rows is taken. Formal polynomial variables record producer number, not payoff.

## Proof
Define a transfer matrix on the sixteen ordered two-column states \((u,v)\in(\{0,1\}^2)^2\). Its entry from \((u,v)\) to \((v,w)\) is \(z^{v_1+v_2}\) if and only if, for both \(h\in\{1,2\}\),
\[
v_h=\mathbf1_{\{2\}}(u_h+w_h+v_{3-h});
\]
all other entries are zero. This equation is exactly the simultaneous best-response condition for the middle column. Every admissible closed walk carries every vertex weight exactly once. Therefore the labeled prism polynomial is \(\operatorname{tr}(T^n)\).

Let \(J\) interchange the two coordinates in *both* columns of a transfer state. The crossed closure requires the terminal state to be the row swap of the initial state. Therefore the Möbius polynomial is \(\operatorname{tr}(JT^n)\). Since \(TJ=JT\), split the sixteen-dimensional transfer space into the \(+1\) and \(-1\) eigenspaces of \(J\), of dimensions ten and six. In the basis of row-swap-fixed states and sums/differences of row-swap-paired states, direct substitution of the entry rule yields these exact characteristic polynomials (with \(t\) the characteristic variable):
\[
\chi_+(t)=t^3(t-z)(t^2-z^3)(t^4-t^3-z^4),
\quad\chi_-(t)=t^3(t-z)(t^2+z^3).
\]
The explicit sixteen-state construction, the invariant-subspace bases, and exact polynomial characteristic-identity checks are supplied in `certify_transfer.py`. The independent direct enumeration is in `verify_twist.py`. In particular, these characteristic identities are exact algebraic identities, not extrapolations from finitely many lengths.

Let \(Q_n(z)\) be the sum of the \(n\)-th powers of the four roots of \(t^4-t^3-z^4\), counted with multiplicity. Taking the sum and difference of the two eigenspace power traces gives
\[
\operatorname{tr}(T^n)=Q_n(z)+2z^n+4\mathbf1_{4\mid n}z^{3n/2},
\quad\operatorname{tr}(JT^n)=Q_n(z)+4\mathbf1_{n\equiv2\pmod4}z^{3n/2}.
\]
Indeed the quadratic factors contribute \(2z^{3n/2}\) for even \(n\) from \(t^2-z^3\), and \(2(-1)^{n/2}z^{3n/2}\) from \(t^2+z^3\); both vanish for odd \(n\). The common eigenvalue \(z\) contributes twice to the sum but cancels in the difference.

Finally, the formal logarithmic identity
\[
-t\frac{\partial}{\partial t}\log(1-t-z^4t^4)
=\sum_{n\ge1}Q_n(z)t^n
\]
shows that the coefficient of \(z^{4j}t^n\) is \(\frac{n}{n-3j}\binom{n-3j}{j}\): expand \(-\log(1-u)=\sum_{m\ge1}u^m/m\), set \(m=n-3j\), and differentiate with respect to \(t\). This proves both formulas for every \(n\ge3\). At \(z=1\), the quartic power sum has leading term \(\alpha^n\), because its other three roots have smaller modulus; the correction remains bounded. This proves the asymptotic assertion.

## Verification
`certify_transfer.py` reconstructs the sixteen-state transfer matrix and the row-interchange operator, verifies their commutation, exactly reduces the transfer to the ten- and six-dimensional subspaces, and checks the two characteristic polynomials in symbolic integer polynomial arithmetic using SymPy. It also verifies both traces symbolically for \(3\le n\le9\). `verify_twist.py` independently enumerates all binary profiles of both graph families for \(3\le n\le9\), checks every agent's exact best response, and compares the resulting producer-count histograms. This amounts to \(699008\) labeled profiles across fourteen graph instances. Neither finite enumeration nor computational logs alone is used as a proof for arbitrary \(n\); the general proof is the invariant-subspace characteristic-polynomial argument above.

## Relationship to prior work
Gilboa and Nisan (2022) formulate strict binary public-goods best-response patterns and complexity questions. Klimm and Stahlberg (2023) prove complexity classifications including nonmonotonic patterns; their inspected manuscript is not an all-length producer-count census for these two cubic strip families. The untwisted prism counting polynomial can be established independently by the plus/minus *sum* trace above, so that polynomial alone does not imply the Möbius result: crossing the seam requires the *difference* trace. The new statement is the Möbius polynomial and the exact finite-support topological correction, not general equilibrium complexity or the previously available untwisted polynomial. Nearby literature on cellular-automaton fixed points on random regular graphs concerns different graph ensembles and does not directly produce these finite-size formulas.

## Limitations
The result concerns only cubic prisms and Möbius ladders, strict deterministic response to **exactly** two productive neighbors, and **pure** equilibria. It does not assert convergence of best-response dynamics, equilibrium welfare, individual-profile preservation under rewiring, or formulas for arbitrary graph families. The originality assessment cannot rule out an equivalent result hidden in older fixed-point or transfer-matrix literature. The asymptotic is for counting equilibria as strip length tends to infinity, not a stochastic dynamic.

## References
- M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs* (first public preprint 2022-07-09), arXiv:2207.04238, https://arxiv.org/abs/2207.04238.
- M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs* (first public preprint 2023-01-27), arXiv:2301.11849, https://arxiv.org/abs/2301.11849.
- C. Koller, F. Behrens and L. Zdeborová, *Counting and Hardness-of-Finding Fixed Points in Cellular Automata on Random Graphs* (2024), arXiv:2406.01710, https://arxiv.org/abs/2406.01710; background abstract consulted only.
