# Cubic permutation isotropy and degree-dependent sign reversal in shuffled Markov kernels

## Finding
For every integer \(d\geq3\), each sequence of deterministic doubly stochastic kernels \(P_1,\ldots,P_L\), and independent uniform permutation matrices \(\Pi_1,\ldots,\Pi_L\), the signed cubic centered dispersion of any initial probability row has an **exact scalar product law**:
\[
\mathbb E\,C_3(\mu\Pi_1P_1\cdots\Pi_LP_L)
=C_3(\mu)\prod_{t=1}^L\kappa(P_t),
\qquad \kappa(P)=\frac{d}{(d-1)(d-2)}\sum_{a,j=1}^d(P_{aj}-1/d)^3.
\]
Here \(C_3(v)=\sum_{j=1}^d(v_j-1/d)^3\), a signed measure of asymmetry of a probability profile about uniformity. Unlike squared distance, \(C_3\) may be negative.

For the transition kernel of an \(r\)-regular directed graph on \(d\) vertices, with \(1\leq r\leq d\),
\[
\kappa(P)=\frac{(d-r)(d-2r)}{r^2(d-1)(d-2)}.
\]
Thus a half-dense regular layer (\(r=d/2\), with \(d\) even) annihilates the expectation, while every layer with \(d/2<r<d\) reverses its sign. The formulas hold for all graph geometries, including disconnected graphs, and all finite depths.

The cubic factorization is not a generic power-moment contraction law. For \(d=4\), the doubly stochastic kernel that averages coordinates 1 and 2 but fixes coordinates 3 and 4 has two zero-sum input rows \(x=(3,-1,-1,-1)\) and \(y=(1,1,-1,-1)\). Under a fresh uniform permutation \(\Pi\),
\[
\frac{\mathbb E\sum_j(x\Pi P)_j^4}{\sum_jx_j^4}=\frac{11}{21},\qquad
\frac{\mathbb E\sum_j(y\Pi P)_j^4}{\sum_jy_j^4}=\frac23.
\]
There is therefore no input-independent scalar multiplying the centered fourth-power sum for this kernel.

## Assumptions and scope
Fix an integer \(d\geq3\) and an integer \(L\geq1\). Every \(P_t\) has nonnegative entries and each of its row sums and column sums equals 1. Each \(\Pi_t\) is uniformly distributed over all \(d!\) permutation matrices and independent of all other permutations. The initial \(\mu\) is deterministic, nonnegative and sums to 1. Let \(u=(1/d,\ldots,1/d)\). Expectation is only with respect to the permutations. The same calculation holds algebraically for any real zero-sum starting row \(x\) in place of \(\mu-u\).

For the regular-graph specialization, \(P_{aj}\) is either 0 or \(1/r\), with exactly \(r\) nonzero entries in each row and column. Loops may be allowed; multiple edges are excluded from this explicit specialization.

## Proof
**One-step permutation cubic identity.** Take any real row \(x=(x_1,\ldots,x_d)\) with \(\sum_a x_a=0\), and any real column \(w=(w_1,\ldots,w_d)\) with \(\sum_a w_a=0\). Write \(S=\sum_a x_a^3\) and \(W=\sum_a w_a^3\). For a uniform permutation \(\pi\), sampling without replacement gives
\[
\mathbb E x_{\pi(a)}^3=S/d,\quad
\mathbb E x_{\pi(a)}^2x_{\pi(b)}=-S/[d(d-1)]\ (a\ne b),
\]
\[
\mathbb E x_{\pi(a)}x_{\pi(b)}x_{\pi(c)}=2S/[d(d-1)(d-2)]\quad(a,b,c\text{ distinct}).
\]
Indeed the zero-sum identity \((\sum_a x_a)^3=0\) and the relation \(\sum_{a\ne b}x_a^2x_b=-S\) imply \(\sum_{a,b,c\text{ distinct}}x_ax_bx_c=2S\). Identical relations apply to \(w\).

Expanding the cube into all-equal, exactly-two-equal, and all-distinct index patterns gives
\[
\begin{aligned}
\mathbb E\left(\sum_a x_{\pi(a)}w_a\right)^3
&=SW\left(\frac1d+\frac{3}{d(d-1)}+\frac4{d(d-1)(d-2)}\right)\\
&=\frac{d}{(d-1)(d-2)}SW.
\end{aligned}
\]
For any doubly stochastic \(P\), each column of \(P-J\) has zero sum, where \(J\) is the all-\(1/d\) matrix. Because \(x\Pi P=x\Pi(P-J)\), use each centered column as \(w\), sum the one-step identity over output columns, and obtain
\[
\mathbb E\sum_j(x\Pi P)_j^3
=\kappa(P)\sum_a x_a^3.
\]

**Iteration.** Set \(x_0=\mu-u\) and \(x_t=x_{t-1}\Pi_tP_t\). Doubly stochasticity ensures \(\sum_j(x_t)_j=0\) and \(\mu\Pi_1P_1\cdots\Pi_tP_t-u=x_t\). Conditional independence of \(\Pi_t\) yields
\[
\mathbb E[\sum_j(x_t)_j^3\mid x_{t-1}]
=\kappa(P_t)\sum_j(x_{t-1})_j^3.
\]
Repeated conditional expectation proves the displayed finite-depth identity, including when any factor is zero.

**Regular-degree formula.** In an \(r\)-regular zero-one adjacency kernel there are \(dr\) entries equal to \(1/r\) and \(d(d-r)\) entries equal to 0. Therefore
\[
\sum_{a,j}(P_{aj}-1/d)^3
=dr(1/r-1/d)^3+d(d-r)(-1/d)^3
=\frac{(d-r)(d-2r)}{d\,r^2}.
\]
Multiplication by \(d/[(d-1)(d-2)]\) gives the claimed \(\kappa\). The sign assertions follow from the two factors \(d-r\) and \(d-2r\). At \(r=d\), \(P=J\) and \(\kappa=0\), not a sign reversal.

**Failure of fourth-order scalar closure.** Let \(P\) have its upper-left \(2\times2\) block filled with \(1/2\), and its remaining diagonal entries equal 1. For the stated \(x,y\), averaging over all 24 permutations gives the two rational ratios \(11/21\) and \(2/3\), respectively. Since these are unequal, no scalar depending only on \(P\) can govern the fourth-power sum for every zero-sum input.

## Verification
Run `python3 verify_cubic.py` using only the Python standard library. The checker uses exact rational arithmetic; it verifies 96 assertions including full enumeration of uniform permutations at dimensions 3 through 6 for one-step identities, all permutation paths for selected two- and three-step products, the regular-degree formula, and the fourth-order obstruction. The proof above, not these bounded finite tests, establishes the theorem for all allowed dimensions and depths.

## Relationship to prior work
Chiclana [1, Theorem 1.6 and Corollary 1.7] established an exact **quadratic** isotropy and chi-square contraction law for the same independent-permutation/doubly-stochastic model. The present identity describes the **signed cubic** centered moment and distinguishes sparse, half-dense, and dense regular layers by a degree-driven sign transition. The quadratic law alone cannot give these signed effects: its factors are nonnegative squared Frobenius norms. The proof uses elementary without-replacement third moments rather than the covariance identity of [1].

Loizou and Richtárik [2] investigate convergence and mean-square contraction in randomized gossip frameworks; their stochastic updates and analytical targets differ from the exact third-order symmetric functional here. The cubic moment identity can be understood through elementary permutation-invariant tensor algebra. Earlier general representation-theoretic results may subsume its special case; the present literature comparison does not establish exhaustive priority.

## Limitations
The signed cubic sum is **not** a distance to equilibrium and need not contract on each sample path. The theorem provides expectations, not concentration, mixing-time bounds, or a complete distribution. The regular-degree simplification requires simple zero-one adjacency divided by the degree, not arbitrary weighted regular multigraphs. The fourth-order example rules out only a universal scalar fourth-power-sum factor; it does not rule out higher-dimensional invariant systems. Full independent priority assessment and independent proof audit have not been performed.

## References
[1] Rafael Chiclana, *Poisson occupancy of paths on permuted regular graphs*, arXiv:2610.14724v1, publicly submitted October 10, 2026. https://arxiv.org/html/2610.14724v1

[2] Nicolas Loizou and Peter Richtárik, *Revisiting Randomized Gossip Algorithms: General Framework, Convergence Rates and Novel Block and Accelerated Protocols*, arXiv:1905.08645v2, 2019. https://arxiv.org/html/1905.08645v2
