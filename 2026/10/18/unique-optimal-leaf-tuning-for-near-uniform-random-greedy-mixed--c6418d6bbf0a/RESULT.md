# Unique optimal leaf tuning for near-uniform random greedy mixed spiders

## Finding
Let \(T_{k,\ell}\) have one centre, \(k\) vertex-disjoint length-two arms incident with the centre, and \(\ell\ge1\) additional leaves adjacent directly to it. Given a uniform random permutation of its vertices, greedily accept each vertex unless an accepted neighbour already exists. Let \(b(k,\ell)\) be the total-variation distance of the resulting law on maximal independent sets from the uniform law on those sets.

**Theorem.** For every integer \(k\ge0\), the function \(\ell\mapsto b(k,\ell)\) on positive integers has a **unique** minimizer:
\[
\ell_k^*=\begin{cases}
1,&k=0,\\
2,&k=1\text{ or }2,\\
6,&k=3,\\
2^k-k,&k\ge4.
\end{cases}
\]
For \(k\ge4\), the exact optimal bias is
\[
b(k,2^k-k)=\frac{1}{2(2^k+1)}\,\mathbb E\left[\frac{|2J-k|}{2^k+1-|2J-k|}\right],
\qquad J\sim\operatorname{Bin}(k,\tfrac12).
\]
In particular the previously known near-uniform upper order is sharp for this tuned family, with the exact leading constant
\[
\min_{\ell\ge1}b(k,\ell)\sim\sqrt{\frac1{2\pi}}\frac{\sqrt{k}}{4^k}\quad(k\longrightarrow\infty).
\]
These conclusions optimize the number of direct leaves **within** this fixed mixed-spider family; they say nothing about all trees of a prescribed order.

## Assumptions and scope
Graphs are finite, simple and undirected; \(k\) is a nonnegative integer and \(\ell\) a positive integer. The graph has \(2k+\ell+1\) vertices. There are exactly \(N+1\) maximal independent sets, where \(N=2^k\): one contains the centre, while each of the other \(N\) includes every direct leaf and makes one choice from each length-two arm. The target uniform distribution gives probability \(1/(N+1)\) to each.

## Proof
**1. Independent derivation of the output law.** Give every vertex an independent uniform arrival time on \([0,1]\). Fix a non-centre maximal independent set that chooses the inner vertex from exactly \(j\) of the \(k\) arms. Each prescribed arm-pair priority occurs with probability \(2^{-k}=1/N\). Conditional on this, an inner vertex's time is the minimum of its two arm times; its probability of being later than \(t\) is \((1-t)^2\). To avoid accepting the centre, at least one direct leaf or selected inner vertex must arrive before the centre. The probability that none does is
\[
\int_0^1(1-t)^{\ell+2j}\,dt=\frac1{\ell+2j+1}.
\]
Thus the probability of that particular non-centre maximal set is
\[
q_j=\frac{\ell+2j}{N(\ell+2j+1)},\qquad\text{with multiplicity }\binom kj.
\]
The remaining probability belongs to the centre-containing set. This also independently recovers the probability formula in the initiating paper.

**2. Deviation and monotonicity.** Subtracting \(1/(N+1)\) gives
\[
q_j-\frac1{N+1}=\frac{\ell+2j-N}{N(N+1)(\ell+2j+1)}.
\]
Define
\[
P_k(\ell)=\sum_{\ell+2j>N}\binom kj\frac{\ell+2j-N}{\ell+2j+1},\qquad
M_k(\ell)=\sum_{\ell+2j<N}\binom kj\frac{N-\ell-2j}{\ell+2j+1}.
\]
Because the deviation of the centre-containing set is the negative of the sum of all non-centre deviations,
\[
b(k,\ell)=\frac{\max\{P_k(\ell),M_k(\ell)\}}{N(N+1)}.
\]
Every summand contributing to \(P_k\) is nondecreasing (strictly increasing once positive) as \(\ell\) grows, and every summand contributing to \(M_k\) is nonincreasing (strictly decreasing while positive). These statements follow directly by rewriting the summand as \(1-(N+1)/(\ell+2j+1)\) and its negative, respectively.

**3. The minimizer lies at one of two consecutive integers.** Assume \(k\ge1\) and put \(\ell_0=N-k\), \(A=N+1\), and \(W=2J-k\). Symmetric pairing of \(W=w\) with \(W=-w\) gives
\[
P_k(\ell_0)-M_k(\ell_0)
=\sum_{j=0}^k\binom kj\frac{2j-k}{A+2j-k}<0,
\]
since each nonzero pair contributes \(-2\binom kj w^2/(A^2-w^2)\). At \(\ell_0+1\), with \(B=N+2\), each pair contributes
\[
\binom kj\left(\frac{1+w}{B+w}+\frac{1-w}{B-w}\right)
=\frac{2\binom kj(B-w^2)}{B^2-w^2}>0,
\]
and the central \(w=0\) term, if present, is positive. The inequality uses \(2^k+2>k^2\ge w^2\), valid for all \(k\ge1\). Therefore \(b(k,\ell_0)=M_k(\ell_0)/(NA)\) and \(b(k,\ell_0+1)=P_k(\ell_0+1)/(NA)\). Strict monotonicity of the respective active summands shows that every \(\ell<\ell_0\) is worse than \(\ell_0\), and every \(\ell>\ell_0+1\) is worse than \(\ell_0+1\). Thus the unique optimum is whichever of these two has smaller bias.

**4. Exact two-point comparison.** At \(\ell_0\), the negative mass is
\[
M_0=\sum_{w>0}\binom{k}{(k-w)/2}\frac{w}{A-w},
\]
where \(w\) ranges over positive integers with the parity of \(k\), at most \(k\). At \(\ell_0+1\), the positive mass is
\[
P_1=\sum_{w>0}\binom{k}{(k-w)/2}\frac{w+1}{A+w+1}
+\boldsymbol1_{2\mid k}\frac{\binom{k}{k/2}}{A+1}.
\]
Their paired difference has the exact identity
\[
\frac{w+1}{A+w+1}-\frac{w}{A-w}
=\frac{A-2w(w+1)}{(A+w+1)(A-w)}.
\]
For \(k\ge7\), \(A=2^k+1>2k(k+1)\), so every paired difference is positive and hence \(P_1>M_0\). The remaining small values are checked by exact rational arithmetic:

| \(k\) | \(M_0\) | \(P_1\) | Winning direct-leaf count |
|---:|---:|---:|---:|
| 1 | \(1/2\) | \(2/5\) | \(2\) |
| 2 | \(2/3\) | \(17/24\) | \(2\) |
| 3 | \(7/8\) | \(122/143\) | \(6\) |
| 4 | \(164/195\) | \(383/330\) | \(12\) |
| 5 | \(111/112\) | \(4262/3367\) | \(27\) |
| 6 | \(73412/75579\) | \(140485/94248\) | \(58\) |

For \(k=0\), the graph is the star \(K_{1,\ell}\): its two maximal independent sets have greedy probabilities \(1/(\ell+1)\) and \(\ell/(\ell+1)\), equal only at \(\ell=1\).

**5. Exact optimum and leading constant.** For \(k\ge4\), \(\ell^*_k=\ell_0\), and symmetry of the binomial law gives
\[
M_0=\frac N2\mathbb E\left[\frac{|W|}{A-|W|}\right].
\]
The formula in the Finding follows. Since \(|W|\le k\) and \(k/A\to0\), uniformly
\[
\mathbb E\left[\frac{|W|}{A-|W|}\right]
=\frac{\mathbb E|W|}{A}\left(1+O(k/A)\right).
\]
The central-binomial estimate (or the central limit theorem with uniform integrability) gives \(\mathbb E|W|\sim\sqrt{2k/\pi}\). Substitution yields the asserted \(\sqrt{1/(2\pi)}\) leading constant.

## Verification
The independent Python script `verify.py` reconstructs greedy output probabilities from the graph through the first-arrival recurrence for twelve parameter cases (including \(k=3\) and both competing leaf counts); checks them against the analytic probability formula using exact fractions; and checks deviation identities and the two-point optimizer comparison for \(0\le k\le10\). It completes with `VERIFICATION_OK`. The unrestricted optimizer and asymptotic statements are established by the written proof, not by those finite tests.

## Relationship to prior work
Fairfax-Ball (2026, arXiv:2610.02276v1) proved the exact distribution \(q_j\) for mixed spiders and established an \(O(\sqrt{k}/4^k)\) bound under the choice \(\ell=2^k-k\); that work explicitly did **not** claim tuning optimality or a matching asymptotic lower bound. The new theorem optimizes \(\ell\) over **all positive integers**, discovers the small exceptional choices \(k=1,3\), and identifies the exact leading constant. These conclusions follow from a new monotone positive/negative deviation comparison rather than merely reproducing the published counting law. Other literature on random-priority greedy independent sets, including Krivelevich–Mészáros–Michaeli–Shikhelman (2024), concerns general processes, densities or limits and does not imply this two-parameter exact optimization.

## Limitations
The optimizer is only for the specified two-parameter family, not for all trees with the same vertex count; the number of vertices changes when \(\ell\) changes. The starting probability formula is already known and explicitly credited. The theorem does not assert exact uniformity for nontrivial spiders (it never occurs here except \(k=0,\ell=1\)). Literature-search incompleteness remains a bibliographic risk. Neither finite checks nor the asymptotic estimate alone prove the exact minimizer; that assertion depends on the monotonicity and the exact finite exceptions in the proof.

## References
1. J. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, arXiv:2610.02276v1, first posted 2026-10-01. https://arxiv.org/abs/2610.02276
2. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015. https://doi.org/10.1002/rsa.21200
3. I. Kryven, R. Versendaal and M. de Vries, *Unified framework for asymptotically uniform iterative construction of generalised random graphs with local constraints*, arXiv:2608.07239v1 (2026). https://arxiv.org/abs/2608.07239
