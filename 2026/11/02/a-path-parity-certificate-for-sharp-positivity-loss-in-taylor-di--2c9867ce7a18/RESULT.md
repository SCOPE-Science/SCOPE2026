# A path-parity certificate for sharp positivity loss in Taylor diffusion

## Finding

For every integer \(s\geq2\), let \(A\) be a finite square matrix with nonnegative entries, zero diagonal, and the same positive row sum \(d\). Write \(L=dI-A\) and consider the degree-\(s\) exponential Taylor update
\[
T_s(h)=\sum_{k=0}^{s}\frac{(-hL)^k}{k!},\qquad h\geq0.
\]
This is an explicit linear-order-\(s\) time-discretization of the Markov or graph-diffusion equation \(u'=-Lu\). Then \(T_s(h)\) is entrywise nonnegative and row-stochastic whenever \(0\leq h\leq1/d\).

Suppose additionally that some ordered pair \((u,v)\) has the **walk gap**
\[
(A^j)_{uv}=0\ (0\leq j<s-1),\qquad
(A^{s-1})_{uv}>0,\qquad(A^s)_{uv}=0.
\]
Then, for every \(h\geq0\), the exact entry is
\[
[T_s(h)]_{uv}=
\frac{h^{s-1}}{(s-1)!}(A^{s-1})_{uv}(1-dh).
\]
Consequently, the **entire**, not merely initial, interval of entrywise stochasticity is exactly
\[
\boxed{\{h\geq0:T_s(h)\geq0\}=[0,1/d].}
\]
At every larger timestep this same transition entry is strictly negative.

**Graph corollary.** Every finite connected weighted \(d\)-regular undirected bipartite graph of diameter at least \(s-1\) satisfies the walk-gap hypothesis. The same is true of strongly connected, constant-exit-rate directed bipartite networks of directed diameter at least \(s-1\). Thus a whole network family has a sharp positivity timestep equal to the forward-Euler timestep, independent of Taylor order. In particular, this holds for classical fourth-order Runge–Kutta on every such graph of diameter at least three.

## Assumptions and scope

All entries of \(A\) are real and nonnegative, \(A_{ii}=0\), and \(A\mathbf1=d\mathbf1\) with \(d>0\). No reversibility, diagonalizability, spectral assumption, or symmetry is required for the matrix theorem. The walk gap is a sufficient structural hypothesis for sharpness, not a claimed necessary characterization of every possible sharp example. If \(A\) is a weighted undirected adjacency matrix, the row-sum assumption means weighted regularity. A directed bipartite support means every positive arc crosses between the two parts. The graph corollary uses ordinary directed shortest-path length or undirected graph distance, as appropriate.

For \(s>4\), “linear order” does **not** assert the existence of an explicit \(s\)-stage Runge–Kutta method with classical nonlinear order \(s\). The result concerns the stated Taylor stability polynomial on the linear autonomous equation. It establishes one-step positivity for every nonnegative initial vector; it does not give accuracy guarantees at large timesteps.

## Proof

Put \(E_m(-x)=\sum_{r=0}^{m}(-x)^r/r!\) for every nonnegative integer \(m\). Since \(A\) commutes with \(dI\), the binomial theorem gives the exact identity
\[
T_s(h)=\sum_{j=0}^{s}\frac{h^j}{j!}
E_{s-j}(-dh)A^j.\tag{1}
\]
For \(0\leq x\leq1\), every \(E_m(-x)\) is nonnegative: the terms of the alternating exponential series have nonincreasing absolute values, so every even partial sum is positive and every odd partial sum is at least the next paired difference. In particular, \(E_1(-x)=1-x\geq0\). Every coefficient in (1) is therefore nonnegative on \(0\leq h\leq1/d\), and all matrix powers \(A^j\) are entrywise nonnegative. Thus \(T_s(h)\geq0\). Also \(L\mathbf1=0\), hence \(T_s(h)\mathbf1=\mathbf1\); the update is stochastic.

For the asserted witness pair, all summands in (1) vanish except the one indexed by \(j=s-1\): the shorter-walk powers vanish by hypothesis and the only longer allowed power, \(A^s\), also vanishes. Substituting \(E_1(-dh)=1-dh\) proves the exact displayed entry formula. Its coefficient is positive at every \(h>0\), so this entry is strictly negative for every \(h>1/d\), and is zero at equality. Together with the sufficient interval, this proves the precise positivity set.

For the graph corollary, take a shortest path of length \(s-1\), available as an initial segment of a geodesic whenever the (directed) diameter is at least \(s-1\). Its endpoints have at least one positive-weight walk of length \(s-1\) and none of smaller length. Bipartiteness rules out walks of the opposite parity, so there is no walk of length \(s\). This gives the walk gap and completes the proof.

For example, on the unit-weight cycle \(C_8\), \(d=2\), and for vertices at distance three classical RK4 has exactly
\[
[T_4(h)]_{uv}=\frac{h^3}{6}(1-2h).
\]
Its entrywise positivity horizon is therefore \(h=1/2\). For a weighted Boolean hypercube of dimension at least three, with coordinate flip rates \(w_1,\ldots,w_m>0\) and total rate \(d=\sum_i w_i\), the classical RK4 positivity horizon is \(1/d\), even for anisotropic rates.

## Verification

Run `python verify.py` from this package using Python's standard library. The checker constructs exact rational weighted adjacency matrices of even cycles, balanced bicliques, anisotropic hypercubes, and directed even cycles. For all applicable orders it checks the walk gap, the exact witness formula, stochasticity and entrywise nonnegativity at five rational steps in the claimed interval, and strict negativity at three larger steps. A separate two-state example confirms that the diameter hypothesis is not vacuous: fourth-order Taylor diffusion on \(K_2\) can remain positive beyond the forward-Euler threshold. The completed replay reports `VERIFY_OK cases=29 exact_assertion_groups=698`.

These finite checks corroborate, but do not replace, the arbitrary-order proof above. They do not establish graph-wide novelty or characterize graphs that do not have the prescribed walk gap.

## Relationship to prior work

The general theory of positivity radii and strict classwise Runge–Kutta positivity steps appears in Horváth (1998, 2005). Gottlieb, Grant and Higgs (arXiv:1403.6519v1, Section 2) give linear-order-\(s\), \(s\)-stage methods with strong-stability-preserving coefficient one, implying the sufficient forward-Euler-type bound for the broad problem class. This known sufficient bound is **not** claimed as new here. The distinct assertion established above is the fixed-network, all-order **necessity** and exact negative transition entry under a verifiable graph walk-parity certificate. It is not a consequence of a worst-case bound without identifying a witness for each graph.

## Limitations

The sharpness theorem requires a concrete walk gap. It does not classify positivity beyond \(1/d\) on graphs lacking that gap, such as very small-diameter examples or nonregular generators. Finite checker examples are not an infinite classification. Historical general SSP results and graph-specific RK positivity results may contain equivalent corollaries under other terminology; independent bibliographic and mathematical review remains appropriate.

## References

1. S. Gottlieb, Z. Grant, D. Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and Optimal Nonlinear Order*, arXiv:1403.6519v1 (public 2014-03-25), https://arxiv.org/abs/1403.6519.
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, DOI:10.1016/j.apnum.2004.08.026 (available online 2004-10-27).
3. Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI:10.1016/S0168-9274(98)00050-6.
