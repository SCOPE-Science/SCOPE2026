# Last-observation delay invariance for record values under exchangeability

## Finding
Let \(X=(X_1,\ldots,X_n)\) be an **exchangeable** real vector. Let \(V(X)\) denote the ordered list of *values* of its strict upper records, beginning with \(X_1\). For a nonempty ordered set of indices \(S\), let \(Q_S(X)\) denote the number of strict upper records in the corresponding retained subsequence.

**Theorem (last retained observation can be delayed).** For \(n\ge2\), any nonempty \(T\subseteq\{1,\ldots,n-1\}\), and any \(s,t\) in \(\{\max T+1,\ldots,n\}\),
\[
 (V(X),Q_{T\cup\{s\}}(X))\ \stackrel{d}{=}\ (V(X),Q_{T\cup\{t\}}(X)).
\]
The equality remains valid when the entire unordered multiset \(\{\!\{X_1,\ldots,X_n\}\!\}\) is included as an additional joint coordinate. In particular, given the ordered record heights (and even the unordered full sample), the conditional distribution of the retained record count cannot distinguish which allowed final sampling time was chosen. Neither independence of observations nor continuity of their marginal law is required.

**Sharp location-sensitive covariance.** If the observations are iid from an atomless law, put \(R_n=|V(X)|\) and \(S=\{k,t\}\), where \(1\le k<t\le n\). Then
\[
 \operatorname{Cov}(R_n,Q_S)=\frac{1}{2k(k+1)},\qquad
 \operatorname{Corr}(R_n,Q_S)=\frac{1}{k(k+1)\sqrt{H_n-H_n^{(2)}}},
\]
where \(H_n=\sum_{j=1}^{n}j^{-1}\) and \(H_n^{(2)}=\sum_{j=1}^{n}j^{-2}\). Thus the covariance is independent of the second time, but depends nontrivially on the first time. At sample size three it equals \(1/4\) for first time one and \(1/12\) for first time two.

## Assumptions and scope
Exchangeability means that the joint distribution of \(X\) is invariant under every permutation of the coordinates. A strict upper record occurs at position one and at each later position strictly exceeding all earlier values in the sequence being considered. Tied observations never create another strict record. All assertions hold for finite \(n\); no asymptotic or independence assumption is used in the main theorem. The extra covariance formulas, by contrast, require iid observations without atoms.

The word *values* is essential: the ordered list of record times need not be preserved by the coupling. The multiset is an unordered collection counting multiplicity, not a set discarding duplicates.

## Proof
It suffices to move the final retained time from \(t\) to \(t+1\), with \(t>\max T\) and \(t<n\). Fix a deterministic data vector \(x\), set \(M=\max_{i\in T}x_i\), and define \(F_t(x)\) by exchanging entries \(x_t,x_{t+1}\) if and only if exactly one exceeds \(M\); otherwise leave all entries unchanged.

**Measure preservation.** Because every member of \(T\) precedes \(t\), the threshold \(M\) is unchanged by the exchange. The condition for exchanging is symmetric in the two entries, so \(F_t\) is an involution. On each ordinary coordinate-transposition orbit, it either exchanges both points or fixes both. Exchangeability therefore implies \(F_t(X)\stackrel d=X\), even with atoms and arbitrary dependence.

**Preservation of the full record heights.** In the nontrivial exchange case, one of \(x_t,x_{t+1}\) is at most \(M\), while the other exceeds \(M\). Since \(M\) is bounded above by the maximum of the full prefix ending at \(t-1\), the lower entry cannot be a full record at either of the two positions. The higher entry becomes a full record exactly when it exceeds that earlier full-prefix maximum, independently of which of the two positions contains it. Accordingly the ordered record-height list is unchanged through the pair. The maximum after the pair is also unchanged, so every later full record height is identical. If no exchange occurs, the assertion is immediate. A coordinate exchange also preserves the unordered multiset.

**Retained record counts.** The retained prefix \(T\) is fixed. The final selected entry adds one to its record count precisely when its value exceeds \(M\). If exactly one of the two potential final entries exceeds \(M\), the involution transfers this indicator from time \(t+1\) to time \(t\). If neither or both exceeds \(M\), the indicators are already equal. Hence, pointwise for every \(x\),
\[
 Q_{T\cup\{t+1\}}(x)=Q_{T\cup\{t\}}(F_t x),
 \quad V(x)=V(F_t x).
\]
Combined with measure preservation this proves the claimed equality in law for adjacent times, and iteration proves it for any \(s,t>\max T\).

**Two-position covariance.** Now suppose iid atomless data. By invariance it is enough to take \(t=k+1\). Let \(I_j\) be the full-sample record indicator at time \(j\), and \(J=\mathbf 1\{X_{k+1}>X_k\}\), so \(Q_{\{k,k+1\}}=1+J\). The relative ranks in each prefix are independent insertion ranks; consequently future full-record indicators are independent of \(J\), and full-record indicators before time \(k\) are also independent of \(J\). Exchangeable ordering of the first \(k+1\) observations gives
\[
 \mathbb E(I_kJ)=\frac{1}{k(k+1)},\qquad
 \mathbb E(I_{k+1}J)=\frac1{k+1},
 \quad\mathbb E J=\frac12,
 \quad\mathbb E I_j=\frac1j.
\]
It follows that
\[
 \operatorname{Cov}(R_n,J)
 =\left(\frac1{k(k+1)}-\frac1{2k}\right)
 +\left(\frac1{k+1}-\frac1{2(k+1)}\right)
 =\frac1{2k(k+1)}.
\]
Finally, the independence of full-record indicators yields \(\operatorname{Var}(R_n)=H_n-H_n^{(2)}\), while \(\operatorname{Var}(J)=1/4\). Dividing the covariance by the product of standard deviations gives the stated correlation.

## Verification
The self-contained `verify.py` exhaustively tests every word over a ternary ordered alphabet at lengths two through seven (including tied observations) and every permutation of distinct ranks at lengths two through eight. It verifies the pointwise involution, preservation of full record heights and of the unordered multiset, and the retained-record count identity for every eligible nonempty prefix \(T\) and adjacent pair of final times. It additionally checks the claimed equality of joint finite distributions for permutations through length seven and the exact covariance formula at every eligible pair of indices through length eight using rational arithmetic. Successful execution prints `VERIFY_OK 49508 full words; 21170019 exact identity checks; ties and distinct ranks`.

These finite checks test implementation and edge cases. The theorem for all sizes and all exchangeable laws is proved by the involution, not by enumeration.

## Relationship to prior work
Falk, Khorrami Chokami, and Padoan (2017) analyze simultaneous record events at prescribed observation times and joint record-value distributions under iid continuity. Their full manuscript develops conditioning on two or three full-sequence record events; the presently stated law instead concerns the record *count of a selected subsequence* jointly with the *entire full-sequence record-value list*, is insensitive to the final retained time, and allows arbitrary exchangeable dependence and ties. Li (2022) studies recent-window records and Poisson approximation under discreteness rather than selected-subsequence record counts. Classical insertion-rank independence explains the iid covariance consequence but is not used for the main exchangeable-law invariance.

## Limitations
The first \(m-1\) selected positions must be fixed: moving one of these may change the joint law. The final selected position must remain strictly later than them. The coupling preserves record *heights*, not record *timestamps*. The covariance specialization assumes iid atomless data; without it, the same simple covariance formula need not hold. The result gives a joint-law equality, not a claim of statistical independence, and does not identify arbitrary hidden sampling designs. Earlier equivalent permutation arguments may exist despite the distinctions from the inspected literature.

## References
1. M. Falk, A. Khorrami Chokami, and S. A. Padoan, *Some Results on Joint Record Events*, arXiv:1707.06254 (first posted 19 July 2017), https://arxiv.org/abs/1707.06254.
2. A. Li, *On the recent-k-record of discrete random variables*, arXiv:2208.06791v1 (first posted 14 August 2022), https://arxiv.org/abs/2208.06791.
