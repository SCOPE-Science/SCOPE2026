# Leaf-sibling Palm dominance in uniform labeled trees

## Finding
For each integer \(n\ge4\), sample uniformly from the \(n^{n-2}\) unrooted trees on vertex set \([n]\). Let \(L\) be the number of degree-one vertices. For every vertex \(v\), let \(\ell_v\) count its degree-one neighbors, and let
\[
 C=\sum_{v=1}^n\binom{\ell_v}{2}
\]
count unordered *leaf-sibling pairs* (pairs of leaves with a common neighbor). Define the \(C\)-size-biased leaf law by \(\Pr^*(L=t)=\mathbb E[C\mathbf1_{\{L=t\}}]/\mathbb E C\).

**Exact Palm law.** If \(Z\) is the number of empty boxes among a designated set of \(n-3\) boxes after \(n-4\) independent uniform allocations to \(n-2\) boxes, then
\[
 L\ \text{under }\Pr^*\ \stackrel{d}=2+Z.
\]
In particular its probability generating function, including all boundary cases, is
\[
 \mathbb E^*z^L=z^2\sum_{j=0}^{n-3}\binom{n-3}{j}(z-1)^j
 \left(1-\frac{j}{n-2}\right)^{n-4},\quad z\in\mathbb R.
\]
Its falling-factorial moments satisfy \(\mathbb E^*[(L-2)_{\underline r}]=(n-3)_{\underline r}\left(1-r/(n-2)\right)^{n-4}\) for every integer \(0\le r\le n-3\).

**Strict stochastic enhancement of leaves.** For every real \(t\),
\[
 \Pr^*(L\ge t)\ge\Pr(L\ge t),
\]
and for each \(n\ge4\) there is at least one integer threshold with strict inequality. Consequently \(\operatorname{Cov}(C,L)>0\) for every \(n\ge4\). Its exact value is
\[
 \operatorname{Cov}(C,L)=\frac{n-1}{2}\left(1-\frac2n\right)^{n-3}
 \left[2+(n-3)\left(1-\frac1{n-2}\right)^{n-4}
 -n\left(1-\frac1n\right)^{n-2}\right].
\]
The normalized covariance converges to a strictly positive constant:
\[
 \lim_{n\to\infty}\frac{\operatorname{Cov}(C,L)}{n}
 =\frac{2-3/e}{2e^2}=0.0606546806848\ldots.
\]

## Assumptions and scope
Trees are uniformly sampled **labeled unrooted** Cayley trees; \(n\ge4\) is integral. A leaf has degree exactly one. Pairs counted by \(C\) share one neighbor, with **no degree-three requirement** on that neighbor; a vertex incident to three leaves contributes three distinct pairs. The Palm distribution is size bias by this precise count, *not* the law conditioned merely on \(C>0\). Empty-box and factorial-moment formulas use the convention \(0^0=1\) in the finite boundary case, consistently with an empty sequence of draws. No distributional independence between \(L\) and \(C\) is asserted.

## Proof
**1. Palm deletion bijection.** Fix pairwise distinct labels \(a,b,w\), and let \(E_{a,b,w}\) be the event that \(a,b\) are leaves both adjacent to \(w\). Deleting \(a,b\) gives an arbitrary labeled tree on the remaining \(N=n-2\) vertices, and adding those two leaf edges is the inverse map. The event therefore has exactly \(N^{N-2}\) trees, and its conditional contracted tree is uniform among all \(N^{N-2}\) trees. By exchangeability, \(C=\sum_{a<b}\sum_{w\notin\{a,b\}}\mathbf1_{E_{a,b,w}}\), so the \(C\)-size-biased law of \(L\) equals its law conditional on any one \(E_{a,b,w}\). Vertices \(a,b\) are new leaves, \(w\) is not a leaf after attachment, and the remaining \(N-1=n-3\) vertices retain their leaf status. Thus
\[
 L\mid E_{a,b,w}=2+\#\{u\notin\{a,b,w\}:u\text{ is a leaf in the contracted tree}\}.
\]

**2. Prüfer occupancy.** A uniform labeled \(N\)-vertex tree has a uniform Prüfer sequence of length \(N-2=n-4\) on \(N\) symbols. A vertex is a leaf exactly when its label is absent from that sequence. The displayed identity is precisely \(2+Z\), and inclusion--exclusion gives the generating polynomial. For any \(r\) designated eligible vertices, the probability that all are absent is \(((N-r)/N)^{N-2}\), which proves every stated factorial moment.

**3. A finite monotone coupling.** The unconditioned \(n\)-vertex Prüfer code has \(n-2\) independent uniform entries from \(n\) symbols. The first symbol is necessarily occupied, so write \(L=n-1-K\), where \(K\) counts distinct symbols *other than the first* seen during the remaining \(n-3\) draws. At state \(K=k\), its upward-transition probability is
\[
 p_n(k)=\frac{n-1-k}{n}.
\]
Likewise \(2+Z=n-1-J\), where \(J\) counts distinct labels among the \(n-3\) eligible contracted-tree labels visited by \(n-4\) draws from \(n-2\) labels (the center label is an ineligible extra symbol). At \(J=k\), its upward-transition probability is
\[
 q_n(k)=\frac{n-3-k}{n-2}.
\]
For every state \(0\le k\le n-3\),
\[
 p_n(k)-q_n(k)=\frac{2(k+1)}{n(n-2)}>0.
\]
Start the chains together at zero, use common uniform random variables for the first \(n-4\) updates, and give \(K\) its additional \((n-3)\)-rd update. If the states are equal, the larger upward probability forces \(K\) to stay at least \(J\); if they differ, their one-step changes cannot reverse their order. Hence \(K\ge J\) almost surely and \(n-1-J\ge n-1-K\) almost surely. Their laws are not equal: there is positive probability of an earlier birth in \(K\) but not \(J\), followed by no births that erase the difference. This establishes the asserted strict stochastic order without assuming independent occupancy indicators.

**4. Covariance and asymptotics.** Counting the \(\binom n2(n-2)\) potential triples in Step 1 gives the classical mean
\[
 \mathbb EC=\binom n2(n-2)\frac{(n-2)^{n-4}}{n^{n-2}}=
 \frac{n-1}{2}\left(1-\frac2n\right)^{n-3}.
\]
By the two Prüfer occupancy laws,
\[
 \mathbb E^*L=2+(n-3)\left(1-\frac1{n-2}\right)^{n-4},
 \qquad \mathbb EL=n\left(1-\frac1n\right)^{n-2}.
\]
The identity \(\operatorname{Cov}(C,L)=\mathbb EC(\mathbb E^*L-\mathbb EL)\) proves the exact formula and strict positivity. Taylor expansion of \(\log(1-x)\) at zero yields \(\mathbb E^*L-\mathbb EL\to2-3/e>0\) and \(\mathbb EC/n\to e^{-2}/2\), giving the claimed limit. No unproved large-size step relies on enumeration.

## Verification
The included `verify.py` decodes *every* Prüfer word for \(n=4,5,6,7,8\) (\(280388\) trees in total), independently computes leaf and sibling-pair counts from adjacency lists, and checks exact rational factorial probabilities, the complete size-biased leaf distribution, the covariance identity, and stochastic tails. It also checks the transition inequality for \(4\le n\le500\). Run with Python 3 standard library: `python verify.py`. Finite tests supplement, rather than establish, the analytic proof.

## Relationship to prior work
Erdős and Rényi, *Asymmetric graphs* (1963), pp. 312–313, define a cherry exactly as two degree-one vertices adjacent to a common vertex and compute its one-triple probability and count asymptotics. The present mean \(\mathbb EC\) therefore reuses established enumeration; the distinguishing claim is the **full \(C\)-Palm law of total leaf count**, its stochastic dominance over the unweighted tree law, and its resulting mixed covariance and exact limit.

Junk, Schmidt, and Weber (2020), §3, impose an additional degree-three condition on the cherry center and study occurrence and symmetry; their definition and conclusions do not give the claimed Palm leaf distribution. Choi, Kaur, and Wu (2021), §§1–2, study cherry/pitchfork counts in binary phylogenetic YHK and PDA models in which the number of leaves is fixed by construction, a different probability space. The Prüfer-code method is classical and appears in Seo and Shin's earlier arXiv account (2005). These comparisons do not establish global historical uniqueness of the new joint law.

## Limitations
The stochastic ordering is for **count-size-biased** selection, not the ordinary event \(C>0\), and only for uniform labeled nonbinary trees. The covariance result does not imply positive association of all tree statistics. The exact mean \(\mathbb EC\) itself is prior work. Historical priority remains subject to older unindexed joint tree-statistic results; independent mathematical audit has not been performed.

## References
- P. Erdős and A. Rényi, *Asymmetric graphs*, Acta Mathematica Academiae Scientiarum Hungaricae **14** (1963), 295–315, esp. pp. 312–313. DOI: `10.1007/BF01895716`; openly available at `https://static.renyi.hu/~p_erdos/1963-04.pdf`.
- L. Junk, S. Schmidt, and M. Weber, *Almost all trees have quantum symmetry*, Archiv der Mathematik **115** (2020), 367–378, §3. DOI: `10.1007/s00013-020-01476-x`.
- K. P. Choi, G. Kaur, and T. Wu, *On asymptotic joint distributions of cherries and pitchforks for random phylogenetic trees*, Journal of Mathematical Biology **83** (2021), 40. DOI: `10.1007/s00285-021-01667-2`.
- S. Seo and H. Shin, *A Generalized Enumeration of Labeled Trees and Reverse Prüfer Algorithm*, arXiv:`math/0601009` (first arXiv version December 31, 2005).
