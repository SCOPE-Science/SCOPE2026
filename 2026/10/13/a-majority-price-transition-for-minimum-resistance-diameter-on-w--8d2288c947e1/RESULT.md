# A majority-price transition for minimum resistance diameter on weighted stars

## Finding
For a star with at least two leaves and arbitrary strictly positive conductance prices, a total unit expenditure on edges has a unique optimal allocation minimizing the maximum effective resistance between any two vertices. The allocation is unexpectedly **uniform whenever no single edge costs more than all other edges combined**, regardless of how unequal the individual prices are. When a unique edge has a majority of the total price, the optimizer splits into two conductance levels determined by square roots of the majority price and its complement.

Specifically, for positive prices \(c_1,\ldots,c_m\) put \(C=\sum_{i=1}^{m}c_i\). If \(2\max_i c_i\le C\), the unique minimizer is
\[
w_i^\star=\frac1C\quad(1\le i\le m),\qquad \mathcal D^\star=2C.
\]
If \(2c_j>C\), the index \(j\) is necessarily unique. Put \(a=\sqrt{c_j}\) and \(b=\sqrt{C-c_j}\). Then the unique minimizer is
\[
w_j^\star=\frac{1}{a(a+b)},\qquad
w_i^\star=\frac{1}{b(a+b)}\quad(i\ne j),\qquad
\mathcal D^\star=(a+b)^2.
\]
At the boundary \(2c_j=C\) these formulas agree. In the strict-majority regime the exact improvement over uniform conductances is
\[
2C-\mathcal D^\star=\bigl(\sqrt{c_j}-\sqrt{C-c_j}\bigr)^2>0.
\]

## Assumptions and scope
Let \(m\ge2\) be an integer. The undirected network consists of a hub vertex \(0\), leaf vertices \(1,\ldots,m\), and exactly the edges \(\{0,i\}\). Assign each edge a strictly positive conductance \(w_i\) and a strictly positive cost coefficient \(c_i\). Restrict to \(\sum_i c_iw_i=1\). The effective resistance \(R_{uv}\) is the voltage difference from injecting one unit of current at \(u\) and removing one unit at \(v\). Define the resistance diameter \(\mathcal D(w)=\max_{u\ne v}R_{uv}\). The claim concerns **all vertex pairs**, not just adjacent pairs, and the optimization is over all positive conductance vectors satisfying the budget.

For a star, the unique current path gives \(R_{0i}=1/w_i\) and \(R_{ij}=1/w_i+1/w_j\) for distinct leaves. Because there are at least two leaves and all conductances are positive, every leaf-to-hub resistance is below some leaf-to-leaf resistance, and hence
\[
\mathcal D(w)=\max_{1\le i<j\le m}\left(\frac1{w_i}+\frac1{w_j}\right).
\]

## Proof
Write \(r_i=1/w_i\), \(D=\mathcal D(w)>0\), and \(u_i=r_i/D\). Then all \(u_i>0\), each \(u_i+u_j\le1\), and at least one pair has equality. Using the cost constraint,
\[
1=\sum_i\frac{c_i}{r_i}
=\frac1D\sum_i\frac{c_i}{u_i},
\qquad D=\sum_i\frac{c_i}{u_i}.
\]
Conversely, given any positive \(u_i\) satisfying all pair constraints, let \(F(u)=\sum_i c_i/u_i\), \(w_i=1/(F(u)u_i)\). This allocation has cost one and resistance diameter \(F(u)\max_{i<j}(u_i+u_j)\le F(u)\). If every pair inequality is strict, scaling all \(u_i\) up until one becomes equality reduces \(F\). Consequently minimizing resistance diameter is equivalent to minimizing \(F\) over this pair-constrained region, with a pair inequality active at the minimizer.

**Case 1: no coordinate exceeds one-half.** If \(\max_i u_i\le1/2\), then
\[
F(u)=\sum_i\frac{c_i}{u_i}\ge2C,
\]
with equality if and only if all \(u_i=1/2\). This uniform normalized vector satisfies all pair constraints and corresponds to the uniform conductance vector \(w_i=1/C\), which has diameter \(2C\).

**Case 2: one coordinate exceeds one-half.** If \(t=\max_i u_i>1/2\), its maximizing index \(j\) is unique, and all other coordinates satisfy \(u_i\le1-t\). Hence
\[
F(u)\ge f_j(t):=\frac{c_j}{t}+\frac{C-c_j}{1-t},\qquad \frac12<t<1.
\]
Because every coefficient is strictly positive, equality holds precisely when \(u_i=1-t\) for every \(i\ne j\). The function \(f_j\) is strictly convex on \((0,1)\), with derivative
\[
f_j'(t)=-\frac{c_j}{t^2}+\frac{C-c_j}{(1-t)^2}.
\]
Its unique unconstrained minimizer occurs at
\[
t_j=\frac{\sqrt{c_j}}{\sqrt{c_j}+\sqrt{C-c_j}},
\qquad f_j(t_j)=\left(\sqrt{c_j}+\sqrt{C-c_j}\right)^2.
\]
If \(2c_j\le C\), then \(t_j\le1/2\). Strict convexity makes \(f_j(t)>f_j(1/2)=2C\) for every \(t>1/2\). In particular, if **every** price is at most \(C/2\), the uniform allocation of Case 1 is the unique global minimizer.

If instead \(2c_j>C\), then \(j\) is the only such index and \(t_j>1/2\). The construction \(u_j=t_j\), \(u_i=1-t_j\) for \(i\ne j\) is feasible: its cross pairs sum to one, while its other pairs sum to \(2(1-t_j)<1\). It attains \(F(u)=f_j(t_j)<2C\). For any index \(k\ne j\), the strict inequality \(2c_k<C\) implies that Case 2 with maximum at \(k\) has value greater than \(2C\). Case 1 has value at least \(2C\). Thus this construction is the unique optimizer, including equality conditions. Recovering the conductances via \(w_i=1/(F(u)u_i)\) gives the displayed formulas. The equality and strict-improvement statements follow by substitution. This completes the proof for every integer \(m\ge2\) and every positive price vector.

## Verification
A standalone Python 3 standard-library checker, `verify_star.py`, evaluates the closed forms and expenditure constraints at 259 representative positive-integer price vectors, checks 1225 exact rational grounded-Laplacian effective-resistance computations against the series law, and checks 20277 feasible exact rational grid points against the derived global lower bound. The checker also verifies the explicit price vector \((16,4,4,1)\): uniform conductances give diameter \(50\), whereas the optimal conductances \((1/28,1/21,1/21,1/21)\) give diameter \(49\). Every infinite-parameter assertion and uniqueness conclusion follows from the analytical proof, **not** from finite computational tests.

To reproduce, save the accompanying standalone script and run `python3 verify_star.py`; the expected ending starts with `VERIFY_OK`.

## Relationship to prior work
Ghosh, Boyd, and Saberi introduced convex edge-conductance allocation for **total** effective resistance and explicitly named **maximum pairwise** effective resistance as another convex problem, reducible to a semidefinite program. Their 2006 proceedings version and 2008 full treatment do not give the arbitrary-positive-price closed-form star classification or its majority-price transition. The present theorem concerns this exact all-pairs minimax objective on stars, not the established general SDP formulation or total-resistance optimization. Suliman and Weinstein study a related but distinct maximum taken over **existing edges**, and compare its optimizing Lewis weights with total effective resistance; on a star this edge-only maximum differs from the all-vertex-pairs resistance diameter used here. The statement is a closed-form specialization beyond the general numerical formulation, not a claim that the graph-design convexity itself is new.

## Limitations
The result assumes a star, fixed topology, strictly positive conductances and prices, linear edge expenditure, and at least two leaves. It does not classify general trees or arbitrary graphs, nonlinear prices, edge removals, or other spectral objectives. A full historical uniqueness assertion is not possible: equivalent specialized formulations in hard-to-index network-design or minmax allocation literature cannot be excluded. The 2006 proceedings predate the day-verified 2008 electronic release; the precise first public availability day of that proceedings version was not established, so the day-verified date used for bibliographic eligibility is not a claim that the mathematical topic first appeared in 2008.

## References
1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems (Kyoto, July 24–28, 2006), pp. 1185–1196. Author-hosted full text: https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1) (2008), 37–66; electronically public February 1, 2008. DOI: 10.1137/050645452. Author-hosted full text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf.
3. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1, February 12, 2023, Sections 1 and 4; https://arxiv.org/abs/2302.05966.
