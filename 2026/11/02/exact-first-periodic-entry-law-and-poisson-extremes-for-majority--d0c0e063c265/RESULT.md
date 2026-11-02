# Exact first-periodic-entry law and Poisson extremes for majority-three rings

## Finding

For the synchronous binary majority-of-three automaton on the labelled cyclic ring of size \(n\ge3\), the first periodic-entry time is determined *exactly* by the longest initially alternating edge run, apart from the two entirely alternating even-ring states, which are periodic from time zero. The finite-size entry-time distribution is given by a parity-projected transfer-matrix trace. For independent fair initial bits, the convergence time is asymptotic to half the binary logarithm of the ring size, with a Poisson extreme-value window and bounded error in its mean.

More precisely, let \(T_n\) be first periodic-entry time and let \(M_q(z)\) be the \((q+1)\)-square matrix indexed by \(0,\ldots,q\) with \((M_q(z))_{j,0}=1\) for all \(j\), \((M_q(z))_{j,j+1}=z\) for \(j<q\), and other entries zero. For every \(n\ge3\) and integer \(t\ge0\),
\[
2^n\Pr(T_n\le t)=\operatorname{tr}(M_{2t+1}(1)^n)+\operatorname{tr}(M_{2t+1}(-1)^n)+2\mathbf 1_{\{2\mid n\}}.
\]
For integer sequences \(t_n\ge0\) satisfying \(n2^{-(2t_n+3)}\to\lambda\) with \(0<\lambda<\infty\),
\[
\Pr(T_n\le t_n)\longrightarrow e^{-\lambda}.
\]
Furthermore, as \(n\to\infty\),
\[
\frac{T_n}{\log_2 n}\xrightarrow{\mathsf P}\frac12,
\qquad \mathbb E T_n=\frac12\log_2 n+O(1).
\]
The extreme-value assertion is intentionally lattice-valued: it describes every subsequence with the displayed intensity limit; it does not assert an unqualified continuously shifted Gumbel limit.

## Assumptions and scope

There are \(n\ge3\) labelled sites \(i\in\mathbb Z/n\mathbb Z\) with spins \(x_i\in\{0,1\}\). One simultaneous update is
\[
F(x)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1}),
\]
where \(\operatorname{maj}\) is the Boolean majority of three inputs and indices are cyclic. The first periodic-entry time is
\[
T_n(x)=\min\{t\ge0:\ F^{t+p}(x)=F^t(x)\text{ for some }p\ge1\}.
\]
Set \(y_i=x_i\oplus x_{i+1}\), using addition modulo two. If at least one \(y_i\) is zero, let \(L(x)\) be the greatest number of consecutive ones between cyclic zeros; take \(L=0\) when every \(y_i\) is zero. If no \(y_i\) is zero, the initial state is an alternating checkerboard, possible exactly when \(n\) is even. Probability statements below use \(n\) independent fair initial spins, and make no claim about noisy or asynchronous majority rules.

## Proof

**1. Exact erosion identity.** A majority update changes site \(i\) precisely when its two neighbors agree with each other and disagree with it; equivalently both incident edge disagreements equal one. Thus, with arithmetic over \(\mathbb F_2\),
\[
F(x)_i=x_i\oplus (y_{i-1}y_i),\qquad
(F(x))_i\oplus(F(x))_{i+1}=y_i(1\oplus y_{i-1}\oplus y_{i+1}).
\]
Every zero edge therefore remains zero. For each maximal run of consecutive one-edges bounded by zeros, a run of length at least two loses exactly its two end edges in one update, while a run of length one remains unchanged. Consequently, for a state with at least one zero edge, after exactly \(\lfloor L/2\rfloor\) steps all runs have length at most one, and the spin state is fixed thereafter. Before that time some run contains two consecutive one-edges and at least one spin changes. Because every edge-zero set can only expand until this time, no earlier state can lie on any temporal cycle unless all runs have length at most one; indeed the last nonzero erosion implies the next edge word differs. This proves
\[
T_n(x)=\lfloor L(x)/2\rfloor
\]
for all states with a zero edge. If no edge is zero, each site changes, yielding the two alternating configurations as one primitive two-cycle from the initial time: \(T_n(x)=0\). Thus all other trajectories ultimately reach fixed points.

**2. Exact finite-size census.** A cyclic edge-word \(y\) is realized by a spin configuration precisely when it has even total parity; it then has exactly two spin preimages. If a cyclic edge-word contains a zero, its runs of ones all have length at most \(q\) precisely when it labels a unique closed length-\(n\) walk of the automaton with states \(0,1,\ldots,q\), where a zero resets the run counter to zero and a one advances it by one (forbidden from state \(q\)). Consequently
\[
\operatorname{tr}(M_q(z)^n)=\sum_{\substack{y:\ \text{at least one zero}\\\text{all one-runs have length at most }q}}z^{\#\{i:y_i=1\}}.
\]
The sum of traces at \(z=1\) and \(z=-1\) equals twice the number of even-parity admissible words, which equals the number of corresponding labelled spin configurations. A first-entry time at most \(t\) is equivalent to \(L\le2t+1\). For even \(n\), add the two entirely alternating initial states not represented by closed walks. This proves the stated formula for every \(n,t\), including \(t=0\) and caps exceeding the ring size.

**3. Poisson extreme-value window.** Let \(k_n=2t_n+2\), and define \(I_i\) to be the event
\[
y_i=0,\qquad y_{i+1}=\cdots=y_{i+k_n}=1.
\]
For \(k_n+1<n\), any proper subset of the edge variables has the distribution of independent fair bits: the map from spins to edges is uniform on the even-parity subspace, and every assignment to fewer than all \(n\) edges has the same number of completions. Thus \(\Pr(I_i)=2^{-(k_n+1)}\), and
\[
\mathbb E X_n=\mathbb E\sum_i\mathbf1_{I_i}=n2^{-(2t_n+3)}=: \lambda_n.
\]
Starts at cyclic distance at most \(k_n\) are mutually incompatible; events supported on disjoint sets of edges are independent whenever their union is a proper subset of the ring. For each fixed positive integer \(r\), the number of ordered \(r\)-tuples of starts with pairwise disjoint blocks is \(n^r(1+O_r(k_n/n))\). Since \(k_n=O(\log n)\), their union occupies fewer than \(n\) edges for all sufficiently large \(n\). The factorial moments therefore satisfy
\[
\mathbb E(X_n)_r=\lambda_n^r(1+O_r(k_n/n))\longrightarrow\lambda^r.
\]
The factorial-moment characterization of the Poisson law gives \(X_n\Rightarrow\mathrm{Poisson}(\lambda)\). Each maximal one-run of length at least \(k_n\) begins immediately after a zero, so (except for the two already-periodic checkerboards) \(T_n>t_n\) iff \(X_n>0\). As the checkerboards also have \(X_n=0\), \(\Pr(T_n\le t_n)=\Pr(X_n=0)\). The claimed limit follows.

**4. Logarithmic concentration and expectation.** The preceding indicator construction yields \(\Pr(T_n>t)\le n2^{-(2t+3)}\) for nonnegative integers \(t\) whenever the corresponding prohibited run fits in the ring; when it does not, the left side vanishes. If \(2(2t+3)<n\), distinct indicator blocks are either disjoint and independent or overlap incompatibly. Therefore \(\operatorname{Var}(X_n)\le\mathbb E X_n\), and Chebyshev yields
\[
\Pr(T_n\le t)=\Pr(X_n=0)\le\frac{2^{2t+3}}{n}.
\]
For the lower-tail estimate use \(t\le\lfloor(\log_2 n-3)/2\rfloor\), when this disjoint-block condition holds for sufficiently large \(n\). For the upper tail use the first inequality. Both tails are bounded by geometric series in steps away from the center \((\log_2 n-3)/2\). They imply \(T_n/\log_2n\to1/2\) in probability and, by the tail-sum identity and geometrically bounded two-sided deviations, \(\mathbb E T_n=(\log_2 n)/2+O(1)\).

## Verification

Run the accompanying `verify.py` with Python 3.9 or later. It computes first-periodic-entry times and eventual periods directly from microscopic updates, independently computes longest-run predictions, and evaluates the integer transfer-matrix traces. For every labelled binary initial state on rings of sizes \(3\) through \(15\), it checks both the microscopic return time and the complete finite-size cumulative counts, covering \(65{,}528\) configurations. It also evaluates finite-size transfer traces at ring sizes \(256,512,1024,2048\). The recorded run terminated with `MAJORITY232_TRANSIENT_VERIFY_OK`. Those finite computations are corroboration only; the infinite claims follow from the proof above.

## Relationship to prior work

Tosic and Agha (2004) studied configuration-space and stability properties of one-dimensional threshold cellular automata. Tosic and Raju (2011) investigated convergence of majority cellular automata experimentally, including the dependence of parallel convergence rates on ring size. Lemoy, Mozeika and Seki (arXiv:1311.4388v1, publicly posted November 18, 2013) applied a transfer-matrix approach to the *thermal-noise* majority cellular automaton. Nakar and Ron (arXiv:2205.08972) established broader structural properties of one-dimensional majority automata, including periodic configurations for more general neighborhood radii. Their reported theorems and models do not directly give this explicit parity-projected entry-time census or the Poisson extreme-value limit for independent binary starts with synchronous radius-one majority. These comparisons are statements about specific inspected claims, not a declaration of exhaustive priority.

## Limitations

The theorem applies to deterministic, fully synchronous majority of the nearest three sites on a finite ring, not general graph majority, arbitrary update schedules or noisy dynamics. The Poisson limit is restricted to integer threshold sequences whose intensity has a positive finite limit; due to the lattice spacing there is no asserted full-sequence centered continuous Gumbel law. The finite verification is not a replacement for the proof. A historical unindexed equivalent of the precise entry-time formula or asymptotic law remains possible.

## References

1. P. Tosic and G. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata* (2004), https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf .
2. P. Tosic and S. N. V. Raju, *On Convergence Properties of One-Dimensional Cellular Automata with Majority Cell Update Rule*, CSC (2011), https://www.researchgate.net/publication/258511570_On_Convergence_Properties_of_One-Dimensional_Cellular_Automata_with_Majority_Cell_Update_Rule .
3. R. Lemoy, A. Mozeika and S. Seki, *Transfer matrix analysis of one-dimensional majority cellular automata with thermal noise*, arXiv:1311.4388v1 (November 18, 2013), https://arxiv.org/abs/1311.4388 .
4. E. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:2205.08972 (2022), https://arxiv.org/abs/2205.08972 .
