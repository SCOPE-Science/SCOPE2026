# Exact two-sided zero-hole entropy and a tail-product law for gap shifts

## Finding

Let \(S\subseteq\mathbb N_0\) be infinite and contain \(0\). For integers \(r,s\ge1\), remove from its two-sided \(S\)-gap shift \(X_S\) every configuration containing the word \(w_{r,s}=0^r10^s\). Put
\[
T(z)=\sum_{g\in S}z^{-(g+1)},\qquad A_j(z)=\sum_{\substack{g\in S\\g\ge j}}z^{-(g+1)},\quad z>1.
\]
There is a unique \(\lambda_{r,s}>1\) satisfying
\[
\boxed{(1-T(\lambda_{r,s}))(1+A_{\max(r,s)}(\lambda_{r,s}))
+A_r(\lambda_{r,s})A_s(\lambda_{r,s})=0.}
\]
The perturbed shift has topological entropy \(h(X_S\setminus[w_{r,s}])=\log\lambda_{r,s}\), where the notation means the invariant subshift avoiding that word everywhere. If \(\lambda>1\) is the unique solution of \(T(\lambda)=1\), then \(1<\lambda_{r,s}<\lambda\). Moreover, as \(\min(r,s)\to\infty\), with no condition on the relative rates,
\[
\boxed{\log\lambda-\log\lambda_{r,s}
=\frac{A_r(\lambda)A_s(\lambda)}{\mu}\,(1+o(1)),\qquad
\mu=\sum_{g\in S}(g+1)\lambda^{-(g+1)}.}
\]
This includes nonsofic examples such as \(S=\{0\}\cup\{2^j:j\ge0\}\). In this example the exact perturbed entropy is constant as either threshold varies without crossing an allowed gap, while its deficit obeys the displayed tail-product asymptotic.

## Assumptions and scope

The alphabet is \(\{0,1\}\). The two-sided \(S\)-gap shift \(X_S\) is the closure of bi-infinite concatenations of the blocks \(10^g\), with \(g\in S\). Entropy means the topological entropy of the shift, computed using logarithms to base \(e\). The hole \([w_{r,s}]\) is forbidden at *every* spatial position, not removed at a single time-zero coordinate. Both thresholds are positive integers. The assumption \(0\in S\) supplies a short separator and ensures irreducibility of the induced two-class gap graph; the assumption that \(S\) is infinite guarantees arbitrarily large allowed gaps and makes the hole genuine for all positive thresholds. No arithmetic regularity, eventual periodicity, or bounded-gap hypothesis is imposed on \(S\).

## Proof

**1. Reduction to consecutive gaps.** In a configuration with infinitely many \(1\)'s in both directions, denote by \((g_i)_{i\in\mathbb Z}\) the numbers of \(0\)'s between consecutive \(1\)'s. Each \(g_i\) belongs to \(S\). An occurrence of \(0^r10^s\), centered on a particular \(1\), exists exactly when the gap preceding that \(1\) is at least \(r\) and the gap following it is at least \(s\). Thus the permitted gap transitions \(g\to h\) satisfy
\[
\neg(g\ge r\ \text{and}\ h\ge s).
\]
Words with at most one \(1\) number at most \(n+1\) at length \(n\); words with two or more \(1\) are controlled by their complete internal gaps, as shown in step 3. Thus configurations having finitely many \(1\)'s introduce no additional word-growth mechanism beyond those two classes.

**2. Two-class weighted renewal matrix.** Assign to a new gap \(h\) the weight \(z^{-(h+1)}\), the reciprocal exponential of the length from one \(1\) to the next. Classify the preceding gap by the bit \(\mathbf 1_{\{g\ge r\}}\). Write
\[
L(z)=T(z)-A_r(z),\qquad
E(z)=\sum_{\substack{g\in S\\g<\min(r,s)}}z^{-(g+1)},\qquad
D(z)=\sum_{\substack{g\in S\\r\le g<s}}z^{-(g+1)}.
\]
The weighted successor matrix, with rows indexed by the old class and columns by the new class, is
\[
M(z)=\begin{pmatrix}L(z)&A_r(z)\\E(z)&D(z)\end{pmatrix}.
\]
All its entries are finite for \(z>1\). Since \(0\in S\), both \(L(z)\) and \(E(z)\) are positive. Since \(S\) is infinite, \(A_r(z)>0\). Thus \(M(z)\) is irreducible and aperiodic, and its Perron eigenvalue \(R(z)=\rho(M(z))\) is strictly decreasing as \(z\) increases: at least the positive \(0\)-gap edges decrease strictly, and entrywise comparison of primitive nonnegative matrices gives strictness. As \(z\to\infty\), \(R(z)\to0\). As \(z\downarrow1\), \(A_r(z)\to\infty\) while \(E(z)\ge z^{-1}\), so \(R(z)\to\infty\). Consequently \(R(z)=1\) has a unique solution \(\lambda_{r,s}>1\).

Writing \(C=A_{\max(r,s)}\), expansion of the determinant gives the identity
\[
\det(I-M(z))=(1-T(z))(1+C(z))+A_r(z)A_s(z).
\]
The other eigenvalue of \(M(z)\) is nonpositive: \(\det M=A_rA_s-TC\le0\), since \(C\) is the smaller of \(A_r,A_s\) and both are at most \(T\). Hence \(\det(I-M(z))=0\) for \(z>1\) precisely when the Perron eigenvalue equals \(1\). This proves uniqueness of the displayed scalar root.

**3. Entropy identification without finite-state assumptions.** For any sufficiently large finite subset \(S_K\subset S\) containing \(0\) and at least one allowed gap \(g\ge\max(r,s)\), the corresponding constrained gap system is a finite directed graph after each weighted edge of length \(g+1\) is expanded into \(g+1\) unit edges. Its entropy is \(\log\lambda_K\), where \(\rho(M_K(\lambda_K))=1\). Increasing finite sets \(S_K\uparrow S\) gives \(M_K(z)\uparrow M(z)\) entrywise for each \(z>1\), and therefore \(\lambda_K\uparrow\lambda_{r,s}\). This establishes the lower entropy bound.

For the upper bound, a length-\(n\) word containing at least two \(1\)'s has a unique decomposition into an arbitrary initial zero run, a first \(1\), a finite sequence of complete permitted gaps, a last \(1\), and an arbitrary final zero run. Ignoring restrictions at the first and last \(1\) only enlarges the count. For every \(z>\lambda_{r,s}\), the generating weight of all such decompositions is bounded by a finite multiple of
\[
(1-z^{-1})^{-2}\sum_{k\ge0}\mathbf u(z)^{\mathsf T}M(z)^k\mathbf1,
\]
where \(\mathbf u(z)\) is any finite nonnegative vector dominating the weights of the first complete gap; for example, it may be taken to have components \(T(z)-A_r(z)\) and \(A_r(z)\). This series converges because \(\rho(M(z))<1\). Words with at most one \(1\) have polynomial count. Consequently the whole word-count generating series converges for every \(z>\lambda_{r,s}\), proving that the entropy is at most \(\log\lambda_{r,s}\). Thus equality holds.

**4. Strict loss.** Let \(\lambda>1\) be determined by \(T(\lambda)=1\), the standard \(S\)-gap entropy equation. At \(z=\lambda\), the displayed determinant is \(A_r(\lambda)A_s(\lambda)>0\). More directly, the forbidden transition deletes positive weight from the strictly positive rank-one unrestricted weighted renewal matrix, so \(\rho(M(\lambda))<T(\lambda)=1\). The unique crossing therefore lies strictly below \(\lambda\).

**5. Sharp two-threshold limit.** As \(\min(r,s)\to\infty\), the three tails \(A_r,A_s,A_{\max(r,s)}\) and their first derivatives tend to zero uniformly on any compact subinterval of \((1,\infty)\). The unique perturbed root tends to \(\lambda\) by monotone convergence of weighted matrices. Denote the determinant in step 2 by \(F_{r,s}(z)\). We have \(F_{r,s}(\lambda)=A_r(\lambda)A_s(\lambda)\), while
\[
F_{r,s}'(z)\longrightarrow -T'(z)
\]
locally uniformly near \(\lambda\). Since \(-\lambda T'(\lambda)=\mu>0\), the mean-value theorem between the two roots gives
\[
\lambda-\lambda_{r,s}
=\frac{\lambda A_r(\lambda)A_s(\lambda)}{\mu}(1+o(1)).
\]
Dividing by \(\lambda\) and using the expansion of the logarithm gives the stated entropy-deficit asymptotic, uniform with respect to how the two thresholds tend to infinity.

## Verification

The accompanying standalone `verify.py` uses only Python standard-library arithmetic. It constructs finite gap-state automata independently of the two-class matrix and compares (i) exact rational determinant identities at three test arguments, (ii) Perron roots of the expanded automata and two-tail scalar equations, and (iii) exact traces of powers of the expanded adjacency matrices against brute-force enumeration of cyclic binary words. It checks three finite gap alphabets, six ordered threshold pairs, and cyclic periods from \(1\) through \(12\): 288 assertions pass. The finite tests confirm the algebraic reduction in accessible cases but do not prove the infinite-\(S\) theorem or its asymptotic; those are proved above.

## Relationship to prior work

Haritha Cheriyath, *A note on the perturbations of subshifts*, arXiv:2506.20750v1 (first public June 25, 2025), Theorem 4.1, treats holes whose forbidden words begin or end with zero, but not both; the introduction explicitly singles out the zero-at-both-ends case as unresolved in general. Its Section 4.1 treats the special sofic \(d\)-gap systems, including zero-ended holes. The present result treats the specific one-central-\(1\) family for all infinite \(S\) containing \(0\), including non-eventually-periodic, nonsofic gap systems; it does not claim novelty for the known \(d\)-gap special cases. The classical unperturbed \(S\)-gap entropy formula and finite-state Perron theory are used as established ingredients, not asserted as new. Henning de Jong, *On sets of periodic orbit lengths in finitely presented dynamical systems* (2026), Section 3.3, studies possible orbit periods of gap shifts and supplies the standard soficity criterion but does not give the specific perturbed entropy formula.

## Limitations

The result addresses a forbidden word with exactly one central \(1\), not arbitrary forbidden words that begin and end in \(0\) and may contain many \(1\)'s. For finite \(S\), the proof can be adapted in nondegenerate cases, but finite \(S\) is deliberately outside the claim because zero-entropy exceptional components require separate hypotheses. The entropy formula does not establish conjugacy, mixing, or unique equilibrium states of the perturbed systems. Previous formulas for sofic and finite-type examples remain prior knowledge. Historical priority in a different renewal or constrained-gap formalism cannot be excluded by the searches undertaken.

## References

1. H. Cheriyath, *A note on the perturbations of subshifts*, arXiv:2506.20750v1, June 25, 2025; Section 4, Theorems 1.3 and 4.1, and Section 4.1. https://arxiv.org/html/2506.20750v1
2. H. de Jong, *On sets of periodic orbit lengths in finitely presented dynamical systems*, *Ergodic Theory and Dynamical Systems* (2026), Section 3.3, DOI:10.1017/etds.2026.10313.
3. D. A. Dastjerdi and S. Jangjoo, *Dynamics and topology of S-gap shifts*, *Topology and its Applications* 159 (2012), 2654–2661 (standard S-gap structure and entropy references).
4. D. A. Lind, *Perturbations of shifts of finite type*, *SIAM Journal on Discrete Mathematics* 2 (1989), 350–365 (finite-type hole theory).
