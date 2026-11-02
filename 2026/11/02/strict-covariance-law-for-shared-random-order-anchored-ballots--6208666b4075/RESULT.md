# Strict covariance law for shared random-order anchored ballots

## Finding

Let \(m\ge 2\) and let \(p,q\) be strict rankings of the same \(m\) alternatives. Under a uniformly random **common** presentation order \(\sigma\), each voter retains an alternative precisely when it is better in her fixed ranking than every alternative previously displayed. Write \(L_p(\sigma)\) and \(L_q(\sigma)\) for the respective numbers of retained alternatives. All alternatives are acceptable to both voters.

Suppose that \(q\) ranks \(a\) immediately above \(b\), and that \(p\) also ranks \(a\) above \(b\). Let \(q'\) exchange those adjacent positions. Put
\[
S=\{z:z\succ_q a\},\quad A=\{z:z\succ_p a\},\quad r=1+|S\cup A|.
\]
Then the covariance responds to this one preference inversion by the **exact, strictly positive** increment
\[
\boxed{\operatorname{Cov}(L_p,L_q)-\operatorname{Cov}(L_p,L_{q'})=\frac{1}{r(r+1)}.}
\]
In particular, for every \(p,q\),
\[
\boxed{1-H_m^{(2)}\ \le\ \operatorname{Cov}(L_p,L_q)\ \le\ H_m-H_m^{(2)}},
\]
where \(H_m=\sum_{i=1}^{m}1/i\) and \(H_m^{(2)}=\sum_{i=1}^{m}1/i^2\). Equality on the right occurs **only when \(q=p\)** and equality on the left **only when \(q\) is the reverse of \(p\)**. Thus the covariance is strictly decreasing along any adjacent inversion of \(q\) away from agreement with \(p\). For four alternatives the sharp interval is \([-61/144,95/144]\).

## Assumptions and scope

The universe of alternatives is any fixed set of size \(m\ge2\). Every alternative is acceptable and every intrinsic ranking is strict and deterministic. Both voters face the **same** uniform random permutation of all alternatives; the experiment is repeated with the same fixed preferences, and covariance refers only to randomness in presentation. The retained ballot is the restriction of a voter's intrinsic ranking to the displayed left-to-right preference records. The result is about retained ballot **length**, not the election winner or strategic choice of an interface order. A full-acceptability threshold is essential to the stated formula; no formula for smaller acceptability sets is asserted.

## Proof

**1. Record representation.** Draw independent continuous clocks \((U_x)\), each uniform on \((0,1)\), and display alternatives in increasing clock order. For any strict ranking \(v\), an alternative \(x\) is retained precisely if \(U_x\) is the smallest clock among \(\{x\}\cup\{z:z\succ_v x\}\). In a uniformly random presentation the item at position \(i\) is a new preference record with probability \(1/i\). Hence \(\mathbb E L_v=H_m\) for every \(v\), and \(\mathbb E L_q=\mathbb E L_{q'}\).

**2. Which record counts change?** Write \(S=\{z:z\succ_q a\}\). For adjacent \(a\succ_q b\), the only record indicators affected on exchanging their ranks are those of \(a\) and \(b\), yielding the pointwise identity
\[
L_q-L_{q'}=\mathbf1_{\{U_b<U_a<\min_{z\in S}U_z\}}-\mathbf1_{\{U_a<U_b<\min_{z\in S}U_z\}}.
\]
When \(S\) is empty, the displayed minimum is interpreted as \(+\infty\). By the expectation equality above, the desired covariance decrement is the expectation of \(L_p\) times this signed indicator. Exchanging the two clock labels is measure-preserving and exchanges the two events. Therefore the decrement is
\[
\mathbb E\left[(L_p(U)-L_p(U^{a\leftrightarrow b}))\,\mathbf1_{\{U_b<U_a<\min_{z\in S}U_z\}}\right].
\]
Here \(U^{a\leftrightarrow b}\) denotes the clock assignment with the values of \(a,b\) exchanged, while the ranking \(p\) is held fixed.

**3. Exact integration.** Since \(a\succ_p b\), partition the other alternatives into the \(p\)-better-than-\(a\) set \(A\), the strictly-between-\(a,b\) set \(B\), and the \(p\)-worse-than-\(b\) set. Define
\[
j=1+|S|,\qquad k=|A\setminus S|,\qquad \ell=|B\setminus S|.
\]
On the event in step 2 put \(t=U_b<s=U_a\). After integrating out clocks in \(S\), the measure on \(0<t<s<1\) is \((1-s)^{j-1}\,dt\,ds\). The record indicators from alternatives \(p\)-better than \(a\) or \(p\)-worse than \(b\) are unchanged by the clock exchange. The alternatives in \(B\cap S\) cannot be records under either clock assignment on this event. Conditional on \(t,s\) and all \(S\)-clocks being later than \(s\), the expected change in \(p\)'s record count is
\[
(1-t)^{k+\ell}-(1-t)^k+(1-s)^k
+\sum_{h=0}^{\ell-1}\int_t^s(1-u)^{k+h}\,du.
\]
The first three terms come from the record indicators of \(b\) and \(a\). In the sum, enumerate the \(\ell\) elements of \(B\setminus S\) in \(p\)-preference order: the term indexed by \(h\) counts configurations where that intermediate element appears between the clocks \(t,s\) and is preferred to all earlier displayed \(p\)-better elements.

Direct integration of the first three terms against \((1-s)^{j-1}\,dt\,ds\), over \(0<t<s<1\), gives
\[
\frac1{j(k+\ell+j+1)}-\frac1{j(k+j+1)}+\frac1{(k+j)(k+j+1)}.
\]
Each term of the sum integrates to
\[
\frac1{j(k+h+j+1)(k+h+j+2)},
\]
and the sum telescopes to
\[
\frac1j\left(\frac1{k+j+1}-\frac1{k+\ell+j+1}\right).
\]
The two terms involving \(\ell\) cancel the corresponding first two contributions. What remains is \(1/((k+j)(k+j+1))\). Since \(k+j=1+|S\cup A|=r\), the asserted decrement follows, and it is strictly positive for all admissible ranks and all \(m\).

**4. Sharp global extrema.** Fix \(p\). Any nonidentical ranking \(q\) admits an adjacent inversion relative to \(p\) that can be removed; step 3 strictly increases covariance on removal. Iterating yields the unique maximizer \(q=p\). Conversely, by adding adjacent inversions until \(q\) reverses \(p\), covariance strictly decreases, giving the unique minimizer at reversal. For \(q=p\) the covariance is the variance of the lower-record count of a uniform permutation, which is \(H_m-H_m^{(2)}\): the record indicators at successive positions are independent Bernoulli variables with parameters \(1/i\). For reverse \(q\), the two counts are the lower- and upper-record counts of one uniform permutation. At positions \(i\ge2\), a new lower and new upper record cannot occur simultaneously; their indicator covariance is \(-1/i^2\). Indicators from different positions are independent because successive insertion ranks are independent. At position \(i=1\), both indicators are deterministic. The covariance is therefore \(-\sum_{i=2}^{m}1/i^2=1-H_m^{(2)}\). This completes the proof.

## Verification

Run `python3 verify.py` from the extracted package. The code uses only the Python standard library and exact rational arithmetic. It independently enumerates complete uniform presentation orders for all relative ranking pairs through five alternatives; compares these values to the record-indicator probability calculation; checks all 872 relative ranking cases through six alternatives; checks 2,283 adjacent-inversion examples (including randomized relabelings with seven alternatives); and checks the sharp endpoints and uniqueness in all enumerated sizes. The verifier completed successfully. These finite checks illustrate and stress-test the proof, rather than proving its infinite scope.

## Relationship to prior work

Fioravanti and Terzopoulou (2026) define the sequential anchoring/retention model and show that voting rules invariant under *arbitrary individual* presentation orders must be tops-only. They do not analyze the **joint** distribution of retained-ballot lengths under one shared uniform order; their proof of winner invariance does not imply the stated exact covariance sensitivity. Gnedin (2006) studies uniform and biased upper/lower record counts; that work supplies classical record-statistic context for the **two endpoint configurations**, but not the general dependence on two fixed rankings or the strict adjacent preference-inversion decrement. Johnson, Leader and Long (2020) study correlation of permutation up-set events in Bruhat orders, which is a different observable and supplies no quantitative adjacent-swap identity for these two record counts. The record-indicator, adjacent-swap proof here establishes the precise statement beyond those ingredients. An equivalent result in unindexed permutation-statistics literature remains possible.

## Limitations

The result assumes full acceptability, strict fixed preferences, a common uniform permutation of all alternatives and exactly two measured voters. It does not infer fairness of an election winner, nor handle voter-specific presentation orders, nonuniform presentation, random preferences, different acceptability thresholds or dependence across repeated elections. The endpoint lower/upper record covariance is classical rather than a separate novelty claim. Literature comparisons are self-review, not independent priority certification.

## References

1. Federico Fioravanti and Zoi Terzopoulou, *Anchor-proofness in Voting with Ranked Ballots*, arXiv:2610.10316, first posted 7 October 2026. https://arxiv.org/abs/2610.10316
2. Alexander Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first posted 17 November 2006, especially §§2–3. https://arxiv.org/abs/math/0611538
3. J. Robert Johnson, Imre Leader and Eoin Long, *Correlation for permutations*, arXiv:1909.03770, especially Theorems 1–3. https://arxiv.org/abs/1909.03770
