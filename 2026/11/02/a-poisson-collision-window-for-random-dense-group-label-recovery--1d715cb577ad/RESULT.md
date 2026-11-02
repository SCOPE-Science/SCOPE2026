# A Poisson collision window for random dense-group label recovery

## Finding

Consider repeatedly sampling an unordered, uniformly chosen set of exactly \(k_n\) distinct coupons from \(n\) coupon types. Along with each sampled coupon set, one observes the corresponding *unordered* set of distinct labels, but not the coupon-to-label matches. There is a fixed unknown bijection between coupons and labels. Let \(Q_{\mathrm I}\) be the number of draws to recover it when the label alphabet is known, and \(Q_{\mathrm {II}}\) the number when that alphabet is initially unknown.

**Theorem (dense-group recovery window).** Suppose \(k_n/n\to p\in(0,1)\). Write
\[
q_n=\frac{k_n(k_n-1)+(n-k_n)(n-k_n-1)}{n(n-1)},\qquad
M_n=\binom n2,\qquad
b_n=\frac{\log M_n}{-\log q_n}.
\]
For a nonnegative integer \(t\), let \(X_n(t)\) count unordered pairs of coupons whose \(t\)-draw binary incidence signatures are identical. If integer \(t_n\) satisfies \(M_nq_n^{t_n}\to\lambda\in(0,\infty)\), then
\[
X_n(t_n)\ \Rightarrow\ \operatorname{Poisson}(\lambda),\qquad
\Pr(Q_{\mathrm I}\le t_n)\to e^{-\lambda},\qquad
\Pr(Q_{\mathrm {II}}\le t_n)\to e^{-\lambda}.
\]
More precisely, for every fixed \(C>0\), uniformly over integers \(t\ge0\) with \(|t-b_n|\le C\),
\[
\Pr(Q_{\mathrm I}\le t)
=\Pr(Q_{\mathrm {II}}\le t)+o(1)
=\exp(-M_nq_n^t)+o(1).
\]
The actual recovery time has lattice-scale fluctuations (a discretized, phase-dependent Gumbel profile), rather than an unqualified continuous Gumbel limit. The corresponding means and the Type-I/Type-II coupling satisfy
\[
\mathbb E Q_{\mathrm I}=b_n+O(1),\qquad
\mathbb E(Q_{\mathrm {II}}-Q_{\mathrm I})=o(1),\qquad
\Pr(Q_{\mathrm {II}}=Q_{\mathrm I})\to1.
\]
In particular, for \(n=2^d\) and \(k_n=n/2\), deterministic Type-I recovery is possible in exactly \(d\) planned draws, whereas independent uniform random draws require \(\mathbb E Q_{\mathrm I}=2d+O(1)\).

There is also an exact finite-size formula. Let \(\Pi_n\) denote the set of partitions of \([n]\), and for \(\pi\in\Pi_n\) put
\[
\mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!,\qquad
h_k(\pi)=[z^k]\prod_{B\in\pi}(1+z^{|B|}).
\]
Then, for every \(n\ge2\), \(1\le k<n\), and integer \(t\ge0\),
\[
\Pr(Q_{\mathrm I}\le t)=
\sum_{\pi\in\Pi_n}\mu(\pi)
\left(\frac{h_k(\pi)}{\binom nk}\right)^t,
\]
where a zero power, including a zero-base zero power, is interpreted as one when \(t=0\).

## Assumptions and scope

Each draw is independent, uniformly distributed over the \(\binom n{k_n}\) subsets of cardinality \(k_n\). The order of elements inside a draw is discarded, but coupon identities and the unordered label set are visible. No sampling noise or repeated coupon within one draw is permitted. The asymptotic assertions require a **fixed positive limiting sampling fraction** \(p\in(0,1)\); the results are not claimed uniformly as \(p\to0\) or \(p\to1\). All logarithms are natural. The \(O(1)\) constants may depend on the limiting fraction and the sequence; the difference of expectations is taken on the natural coupling using the same successive draws.

For coupon \(i\), its incidence signature after \(t\) draws is the binary vector \(\eta_i(t)\in\{0,1\}^t\) recording which draws contained coupon \(i\). The known-alphabet problem completes exactly when all \(\eta_i(t)\) are distinct; the unknown-alphabet problem additionally requires every signature to be nonzero. These equivalences are the separating/covering characterization in the cited labeled-coupon literature.

## Proof

**1. Pair collisions.** For any specified pair of coupons, the probability that a single draw includes both or neither is exactly \(q_n\). Independence across draws gives
\[
\mathbb E X_n(t)=M_nq_n^t=:\Lambda_n(t).
\]
For any fixed integer \(s\ge2\), put \(r_s=p^s+(1-p)^s\). Given a fixed graph \(H\) on \(v\) marked coupon vertices, having no isolated vertices, let its connected component sizes be \(s_1,\ldots,s_j\). The collision events on all its edges require that the coupons in each component have one common incidence signature. For a *single* draw, with \(p_n=k_n/n\), the probability of this condition is
\[
\prod_{i=1}^j[p_n^{s_i}+(1-p_n)^{s_i}]+O_H(n^{-1}).
\]
Indeed, for any prescribed membership pattern on \(v\) fixed coupons, its probability under sampling without replacement differs from that of independent Bernoulli-\(p_n\) membership bits by \(O_H(n^{-1})\). The expression tends to \(\prod_i r_{s_i}\), but no convergence rate for \(p_n\to p\) is assumed. The bounded-away-from-zero component probabilities make the relative error uniform. Over \(t=O(\log n)\) independent draws, the resulting probability is
\[
\left(\prod_i[p_n^{s_i}+(1-p_n)^{s_i}]\right)^t(1+O_H(t/n)).
\]

**2. Poisson factorial moments.** Expand \(\mathbb E(X_n(t))_r\) over ordered \(r\)-tuples of distinct coupon-pairs, for fixed \(r\). Their edge-union graph has no isolated vertices. The disjoint-edge configurations number \((n)_{2r}/2^r\); their contribution tends to \(\lambda^r\) if \(\Lambda_n(t)\to\lambda\). Every nonmatching configuration has a connected component of size \(s\ge3\). Strict monotonicity of the \(\ell^s\) norms of the positive two-vector \((p,1-p)\) gives
\[
r_s<(p^2+(1-p)^2)^{s/2},\qquad s\ge3.
\]
Since \(t=2\log n/[-\log(p^2+(1-p)^2)]+o(\log n)\), it follows that \(n^s[p_n^s+(1-p_n)^s]^t=o(1)\) for each fixed \(s\ge3\), while \(n^2q_n^t=O(1)\). There are only finitely many graph shapes at each fixed \(r\), so every nonmatching contribution vanishes. Consequently every fixed factorial moment tends to \(\lambda^r\), proving \(X_n(t)\Rightarrow\operatorname{Poisson}(\lambda)\). By subsequential compactness, this also proves the asserted uniform zero-collision probability over bounded \(t-b_n\).

**3. Unknown alphabet.** Let \(U_n(t)\) be the count of coupons never sampled. Then
\[
\mathbb E U_n(t)=n(1-p_n)^t.
\]
At \(t=b_n+O(1)\), the power of \(n\) is \(1+2\log(1-p)/[-\log(p^2+(1-p)^2)]<0\), since \(p^2+(1-p)^2>(1-p)^2\). Therefore \(\Pr(U_n(t)>0)=o(1)\) by Markov's inequality. The Type-I and Type-II completion probabilities are asymptotically equal throughout the window.

To compare their actual stopping times, take \(t^-_n=\lfloor b_n-L\rfloor\) with fixed \(L>0\). The Poisson zero-collision formula bounds \(\Pr(Q_{\mathrm I}<t^-_n)\) by a quantity tending to zero as \(L\to\infty\), while \(\Pr(U_n(t^-_n)>0)=o(1)\) for each fixed \(L\). It follows that the probability of an unseen coupon at time \(Q_{\mathrm I}\) tends to zero. Since distinct signatures permit at most one unseen coupon, a Type-II delay, if any, is exactly the waiting time for that coupon to be sampled on a later draw. Conditional on the past, that waiting time is geometric with success probability \(p_n\). Thus
\[
\mathbb E(Q_{\mathrm {II}}-Q_{\mathrm I})
=\frac{\Pr(U_n(Q_{\mathrm I})>0)}{p_n}=o(1).
\]
The same argument gives equality of stopping times with probability tending to one.

**4. Expected Type-I completion time.** The first-moment bound \(\Pr(Q_{\mathrm I}>t)\le M_nq_n^t\) sums to \(O(1)\) above \(b_n\). For the lower tail, write \(R_{3,n}=((k_n)_3+(n-k_n)_3)/(n)_3\) and
\[
D_{4,n}=\frac{(k_n)_4+(n-k_n)_4+2(k_n)_2(n-k_n)_2}{(n)_4},
\]
where \((a)_s=a(a-1)\cdots(a-s+1)\) denotes a falling factorial. Counting pairs of collision indicators with zero, one, or two common coupon vertices yields the exact variance
\[
\operatorname{Var}(X_n(t))=
\Lambda_n(t)(1-q_n^t)
+6\binom n3(R_{3,n}^t-q_n^{2t})
+6\binom n4(D_{4,n}^t-q_n^{2t}).
\]
For \(0\le t\le b_n+O(1)\), \(D_{4,n}/q_n^2=1+O(n^{-1})\), while the strict \(r_3<q^{3/2}\) inequality supplies a \(\delta(p)>0\) with
\[
\frac{\operatorname{Var}(X_n(t))}{\Lambda_n(t)^2}
\le\Lambda_n(t)^{-1}+O(n^{-\delta(p)}+\log n/n).
\]
Chebyshev's inequality bounds \(\Pr(Q_{\mathrm I}\le t)=\Pr(X_n(t)=0)\) by the right side. Summing over integer \(t<b_n\) contributes \(O(1)\), because \(\Lambda_n(t)^{-1}=\exp[-(-\log q_n)(b_n-t)]\) is geometrically summable and the uniform error is \(o(1/\log n)\). Together with the upper-tail sum this proves \(\mathbb E Q_{\mathrm I}=b_n+O(1)\).

**5. Exact finite-size identity and sampling overhead.** The event that all columns of the incidence matrix are distinct has the Möbius-inversion expansion on the set-partition lattice of \([n]\). For a partition \(\pi\), requiring all coupons in every block to share a signature restricts a single row to selecting whole blocks. The number of permitted size-\(k\) rows is \(h_k(\pi)\). Raising the per-row probability to the \(t\)-th power and using the partition-lattice Möbius coefficient \(\mu(\pi)\) gives the displayed exact formula.

For \(n=2^d\) and \(k=n/2\), a Type-I separating incidence matrix must have at least \(d\) rows because its \(n\) columns must be distinct binary words. Taking all \(2^d\) binary \(d\)-words as its columns achieves \(d\) rows, each with exactly \(n/2\) ones. Conversely \(q_n=1/2+O(1/n)\), so \(b_n=2d+O(1)\), yielding the stated factor-of-two average overhead for independent random sampling.

## Verification

The standalone `checker.py` computes exact finite CDFs using the partition formula and independently enumerates all sequences of small fixed-size draws. It also compares exact variance formulas against complete enumeration and tests numerical critical-window probabilities by seeded simulation. Its saved output is `checks.txt`. The verified exact examples include
\[
\Pr(Q_{\mathrm I}\le3\mid n=4,k=2)=8/9,\qquad
\Pr(Q_{\mathrm I}\le4\mid n=5,k=2)=96/125.
\]
These finite calculations are checks on the identities, not proofs of asymptotic Poisson convergence or novelty. The latter rests on the factorial-moment argument and the primary-literature comparisons above.

## Relationship to prior work

The separating/covering characterization and the deterministic minimal-row problem belong to the earlier labeled-coupon and separating-system literature. Rényi (1961, Theorem 1 and its corollary) already proved the complete birthday-window profile and a factor-of-two random-vs-designed sample overhead when each random query independently includes each element with probability one half (unrestricted row cardinalities). That classical result is explicitly prior; the fixed-positive-fraction, **exact-cardinality** model here has dependent incidence columns and does not follow from Rényi's product formula. The balanced-case factor of two is an analogue of Rényi's already-known phenomenon, not claimed as a newly discovered contrast. The 2025 work of Berrebi, Yaakobi, Yakhini, and Bar-Lev studies random sample sizes and partial recovery; Tan and collaborators' 2025 paper provides a Markov-chain computation of expectations, notably for two-coupon draws; Barak-Pelleg and Berend establish asymptotic expectations for groups of size two; Berend and Sher (2026) establish dense-group expected collection times when the objective is merely to have seen every coupon, not to infer an unknown label-to-coupon correspondence; Tan and collaborators' October 2026 paper develops deterministic minimal constructions. The present result concerns a different, fixed **positive-density** random-draw regime: a sharp Poisson obstruction profile for random full recovery, a lattice-scale stopping-time approximation, asymptotic equality of the two informational variants, and the random-versus-designed sampling overhead. It is an application of the birthday-collision mechanism, with a nontrivial fixed-row-cardinality dependence handled by its factorial-moment proof.

## Limitations

Only fixed positive limiting sampling fractions are treated. The theorem does not cover sparse-group critical windows, density tending to one, noise in observed labels, heterogeneous group-size mixtures, or full finite-\(n\) Type-II distributions. The exact integer-time profile has lattice oscillations, so it must not be stated as an unrestricted continuous Gumbel law. General prior collision-limit theorems for dependent random codes could potentially imply parts of this result under a stronger available formulation; historical priority has not been independently certified.

## References

1. S. S. Berrebi, E. Yaakobi, Z. Yakhini, D. Bar-Lev, *The Labeled Coupon Collector Problem with Random Sample Sizes and Partial Recovery*, arXiv:2502.02968v1, first posted 2025-02-05. https://arxiv.org/abs/2502.02968
2. A. Tan, O. Limor, D. Bar-Lev, R. Gabrys, Z. Yakhini, P. H. Siegel, *The Labeled Coupon Collector Problem*, arXiv:2507.15231v1, first posted 2025-07-21. https://arxiv.org/abs/2507.15231
3. D. Barak-Pelleg, D. Berend, *On Conjectures concerning the Labeled Coupon Collector Problem*, arXiv:2510.23249v1, first posted 2025-10-27. https://arxiv.org/abs/2510.23249
4. A. Tan, D. Bar-Lev, R. Gabrys, Z. Yakhini, P. H. Siegel, *The Minimum Number of Samples in the Labeled Coupon Collector Problem*, arXiv:2610.32251v1, first posted 2026-10-23. https://arxiv.org/abs/2610.32251
5. G. Katona, *On separating systems of a finite set*, Journal of Combinatorial Theory 1 (1966), 174–194.
6. A. Rényi, *On random generating elements of a finite Boolean algebra*, Acta Sci. Math. (Szeged) **22** (1961), 75–81, Theorem 1 and corollary (unrestricted independent fair-bit rows). https://acta.bibl.u-szeged.hu/13920/1/math_022_fasc_001_002_075-081.pdf
7. D. Berend and T. Sher, *Asymptotic Results for Uniform Group Drawing in the Coupon Collector's Problem*, arXiv:2605.06953v1, first posted 2026-05-07, Theorem 2.2 (ordinary dense group collection). https://arxiv.org/abs/2605.06953
