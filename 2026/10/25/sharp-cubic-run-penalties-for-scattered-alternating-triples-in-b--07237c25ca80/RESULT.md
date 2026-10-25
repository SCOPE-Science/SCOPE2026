# Sharp cubic run penalties for scattered alternating triples in binary words

## Finding

For a binary word \(w\), let \(c_{010}(w)\) count triples of indices \(i<j<k\) with letters \(0,1,0\), and let \(\rho(w)\) be the number of maximal constant-symbol runs. Fix integers \(a,b\geq1\) (numbers of zeros and ones). For every feasible integer \(R\geq2\), the maximum of \(c_{010}(w)\) among words with composition \((a,b)\) and exactly \(R\) runs is given explicitly below, together with the exact number and a structural classification of *all* maximizers.

Put \(F(a)=\lfloor a^2/4\rfloor\). For \(0\leq t\leq a-1\), define the **central-cut penalty**
\[
\Delta_a(t)=\begin{cases}
\dfrac{s(2s^2+1)}3,&a\text{ even},\ t=2s,\\[2pt]
\dfrac{2s(s^2-1)}3,&a\text{ odd},\ t=2s,\\[2pt]
\dfrac{s(s+1)(2s+1)}3,&t=2s+1.
\end{cases}
\]
This penalty depends only on \(t\) and the parity of \(a\), and is a cubic quasi-polynomial in \(t\), independently of the magnitude of \(a\).

**Even run counts.** If \(R=2r\), the class is nonempty exactly when \(a,b\geq r\). Its maximum is \(0\) for \(r=1\), and for \(r\geq2\) it is
\[
M_{a,b}(2r)=(b-1)F(a)-\Delta_a(r-1).
\]

**Odd run counts.** If \(R=2r+1\), with \(r\geq1\), there are two possibilities:

* If \(a\geq r+1\) and \(b\geq r\), then
\[
M_{a,b}(2r+1)=bF(a)-\Delta_a(r).
\]
All maximizing words start and end with \(0\), even when words starting and ending with \(1\) are feasible.
* If \(a=r\) and \(b\geq r+1\), only words starting and ending with \(1\) exist. Their maximum is \(0\) for \(r=1\), and for \(r\geq2\) is
\[
M_{a,b}(2r+1)=(b-2)F(a)-\Delta_a(r-1).
\]

In every nonzero case all maximizers are characterized as follows. Let \(t\) be the number of *productive* one-runs: \(t=r-1\) for even \(R=2r\), \(t=r\) for odd words beginning and ending in zero, and \(t=r-1\) for odd words beginning and ending in one. List the cumulative zero counts immediately preceding the productive one-runs as \(1\leq z_1<\cdots<z_t\leq a-1\). These must be **exactly a choice of the \(t\) integers closest to \(a/2\)**, allowing the two symmetric choices at an equally distant boundary. Every one-run with no zero on one side has length exactly one. Give each productive one-run length at least one and distribute every remaining one only among productive runs at zero cuts where \(z(a-z)=F(a)\). These rules are necessary and sufficient.

For completeness, write \(E=b-t-u\), where \(u\) is the number of unproductive boundary one-runs (\(u=0,1,2\), respectively), and suppose \(t\geq1\). Define
\[
Q(a,t,E)=\begin{cases}
1,&a\text{ even},\ t\text{ odd},\\
2,&a\text{ even},\ t\text{ even},\\
2,&a\text{ odd},\ t=1,\\
E+1,&a\text{ odd},\ t\geq2\text{ even},\\
2(E+1),&a\text{ odd},\ t\geq3\text{ odd}.
\end{cases}
\]
The exact numbers of maximizing words in the three nondegenerate branches above are respectively \(2Q(a,r-1,b-r)\), \(Q(a,r,b-r)\), and \(Q(a,r-1,b-r-1)\). In the degenerate branches \(R=2\) and \((a,R)=(1,3)\), the numbers are \(2\) and \(b-1\), respectively.

## Assumptions and scope

A word is a finite **linear**, ordered binary string. Each occurrence of \(010\) is a *scattered* subsequence: the three selected positions need not be adjacent. All zeros and ones are labeled only by their symbol, not as distinguishable objects. Integers \(a,b\geq1\) and \(R\geq2\) are fixed; when none of the displayed feasibility conditions applies, no word of that composition and run count exists. The expressions count labeled linear strings, not necklaces or equivalence classes under reversal/complementation. Reversal preserves the \(010\) statistic and exchanges the even-run orientations.

## Proof

**1. Counting through zero cuts.** Suppose a word has \(a\) zeros. Every one situated after exactly \(z\) zeros contributes \(z(a-z)\) scattered copies of \(010\), by choosing the first zero to its left and the final zero to its right. Therefore
\[
c_{010}(w)=\sum_{\text{one-runs }J}|J|z_J(a-z_J).
\]
A one-run is productive precisely when \(1\leq z_J\leq a-1\). Productive one-runs occur at distinct, strictly increasing integer cuts in the zero sequence. Conversely, any strictly increasing \(t\)-tuple of such cuts gives positive zero-run lengths between and around them, uniquely. A zero run is therefore determined by the differences of consecutive cuts and the two endpoint gaps.

**2. Optimization for a prescribed orientation.** Suppose the number of productive one-runs is \(t\geq1\), and there are \(u\) forced one-runs at word boundaries (where their contribution is zero). All \(t+u\) one-runs must have positive lengths. Write \(E=b-t-u\geq0\). For a fixed cut set \(Z\) of size \(t\), the contribution is at most
\[
\sum_{z\in Z}z(a-z)+E\max_{z\in Z}z(a-z).
\]
Equality holds exactly when the \(u\) unproductive runs have length one and all \(E\) extra ones lie in productive runs with maximal cut weight. Because \(z(a-z)=F(a)-(z-a/2)^2+\text{constant}\) is strictly decreasing with distance from the center, its \(t\) largest values occur at the \(t\) cuts nearest \(a/2\). Such a set contains a cut realizing \(F(a)\). Thus the optimum in the fixed orientation is
\[
S(a,t)+E F(a)=(b-u)F(a)-\Delta_a(t),
\]
where \(S(a,t)\) is the sum of the \(t\) largest cut weights. Every equality condition listed in the finding is forced by the two maximizations.

**3. Exact central-cut loss.** If \(a=2h\), the losses \(F(a)-z(a-z)\), arranged by increasing distance from the center, are
\[
0,1,1,4,4,9,9,\ldots.
\]
If \(a=2h+1\), they are
\[
0,0,2,2,6,6,12,12,\ldots.
\]
The first \(t\leq a-1\) losses sum to the displayed \(\Delta_a(t)\), using the usual sums of squares and consecutive products. In particular, the loss is independent of \(a\) except for parity, provided the specified cuts exist.

**4. Run orientation and feasibility.** If \(R=2r\), either orientation has exactly \(r\) zero-runs and \(r\) one-runs. Exactly one one-run is unproductive, so \(t=r-1\), \(u=1\); either orientation is possible iff \(a,b\geq r\). If \(R=2\), both words have zero \(010\) occurrences. If \(R=2r+1\) begins and ends in zero, there are \(r+1\) zero-runs and \(r\) productive one-runs, so \(t=r\), \(u=0\), and feasibility is \(a\geq r+1,b\geq r\). If it begins and ends in one, there are \(r\) zero-runs and \(r+1\) one-runs of which two are unproductive, so \(t=r-1\), \(u=2\); feasibility is \(a\geq r,b\geq r+1\). With \(r=1\) the latter orientation contains no \(010\). When both odd-run orientations are available, the zero-ended orientation wins strictly: for \(r\geq2\) its optimum exceeds the other by
\[
\bigl(S(a,r)-S(a,r-1)\bigr)+F(a)>0,
\]
and for \(r=1\) it is positive while the one-ended orientation has value zero. The stated cases exhaust all feasible words.

**5. Enumeration of equality cases.** For even \(a\), the set of \(t\) nearest cuts is unique if \(t\) is odd and has two choices if \(t\) is even; it always contains the unique central maximum cut. For odd \(a\), there are two cut sets for odd \(t\), one for even \(t\); when \(t\geq2\), both central maximal cuts are included. Distributing \(E\) identical extra ones among those two productive central runs gives \(E+1\) possibilities. At \(t=1\), the single chosen central cut gives one allocation. This proves the formula for \(Q\). Each even-run orientation provides the same number of distinct words; odd-run maximizers have the unique winning orientation from step 4. The zero-occurrence cases are exactly the two words with two runs and the \(b-1\) words \(1^i0 1^{b-i}\) with \(1\leq i<b\), respectively.

## Verification

`verify.py` is a standalone Python 3 verifier with no dependencies beyond the standard library. Run `python3 verify.py`. It computes \(c_{010}\) independently by scanning each word, enumerates every fixed-composition word through length \(18\), groups words by their exact number of runs, and checks **both** the claimed optimum and exact maximizing-word multiplicity for all \(1041\) nonempty parameter classes. It separately enumerates cut sets for \(126\) small parameter cases to verify the cubic penalty. The expected final line is `VERIFY_OK`.

The computation checks finite instances; the proof above is what establishes the theorem for all parameters.

## Relationship to prior work

Menon and Singh (2023, Section 4, especially Proposition 4.1) study unrestricted maxima of occurrences for binary patterns with up to three runs. In particular, their approach implies the classical unrestricted upper bound \(bF(a)\) for the pattern \(010\). It does not give the sharp decrease enforced by an **exact prescribed number of runs** or classify the run-constrained maximizers.

Bruda (first posted June 30, 2026, Theorem 1.8 and Section 4.4) proves a general upper bound using run data and explicitly highlights sharper estimates for constrained classes of words as a direction for improvement. The present result gives exact values and all equality cases for a basic three-letter alternating pattern when the complete Parikh vector and run count are fixed; no claim is made for general patterns. Fang (2024, Sections 3–4) studies a different global subword-entropy extremal objective, not this fixed-pattern, fixed-run optimization.

## Limitations

This theorem applies only to \(010\) (equivalently \(101\) after exchanging zero and one) and linear binary words. It does not solve the general constrained extremal problem for longer patterns, arbitrary alphabets, or simultaneous optimization of several patterns. Its novelty is assessed against the cited accessible literature and mathematical-record searches; an equivalent result outside those sources remains possible. The finite checker is not an exhaustive proof for arbitrary length.

## References

1. G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578v1 (first public posting June 30, 2026). https://arxiv.org/abs/2607.02578
2. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870v1 (June 13, 2023). https://arxiv.org/abs/2306.07870
3. W. Fang, *Maximal number of subword occurrences in a word*, arXiv:2406.02971v1 (June 5, 2024). https://arxiv.org/abs/2406.02971
