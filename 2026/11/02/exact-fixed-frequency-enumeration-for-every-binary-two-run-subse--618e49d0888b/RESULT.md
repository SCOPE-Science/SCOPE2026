# Exact fixed-frequency enumeration for every binary two-run subsequence pattern

## Finding

Let \(a,b,k\ge 1\) be integers, let \(p=0^a1^b\), and let \(B_{a,b}(n,k)\) count length-\(n\) binary words in which \(p\) occurs as a scattered subsequence exactly \(k\) times, with occurrences distinguished by their increasing tuples of positions.

Define the finite set of *constrained profiles*
\[
\mathcal P_{a,b}(k)=\left\{(q;t_1,\ldots,t_r):\ q\ge b,\ r=q-b+1,\ a\le t_1\le\cdots\le t_r,\ \sum_{i=1}^{r}\binom{q-i}{b-1}\binom{t_i}{a}=k\right\}.
\]
For a profile \(\pi=(q;t_1,\ldots,t_r)\), put \(h(\pi)=q+t_r\). Then, as an identity of formal power series,
\[
\boxed{\sum_{n\ge0}B_{a,b}(n,k)z^n=\frac{\sum_{\pi\in\mathcal P_{a,b}(k)}z^{h(\pi)}}{(1-z)^{a+b}}.}
\]
Equivalently, with \(\binom{x}{d}=0\) whenever \(x<d\) for nonnegative integer \(d\),
\[
B_{a,b}(n,k)=\sum_{\pi\in\mathcal P_{a,b}(k)}\binom{n-h(\pi)+a+b-1}{a+b-1}.
\]
The set \(\mathcal P_{a,b}(k)\) is explicitly finite: every profile satisfies \(\binom qb\le k\) and \(\binom{t_r}{a}\le k\). Consequently **exactly one** of the following happens: either \(k\) is unattainable as a number of scattered occurrences of \(p\), in which case \(B_{a,b}(n,k)=0\) for every \(n\); or \(k\) is attainable, in which case \(B_{a,b}(n,k)\) is eventually a polynomial of *exact* degree \(a+b-1\), with leading coefficient
\[
\frac{|\mathcal P_{a,b}(k)|}{(a+b-1)!}>0.
\]
For example, with \(a=b=2\) and \(k=5\), the unique constrained profile is \((3;2,3)\). Thus
\[
\sum_{n\ge0}B_{2,2}(n,5)z^n=\frac{z^6}{(1-z)^4},\qquad B_{2,2}(n,5)=\binom{n-3}{3}\quad(n\ge6),
\]
and the count is zero for \(n<6\). By reversal and binary complementation, the same enumerations apply to every binary pattern with precisely two constant runs.

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\); patterns have exactly two nonempty constant runs. A scattered occurrence is a choice of increasing positions, not merely a distinct output word. The multiplicity \(k\) is positive and fixed, and \(n\) is any nonnegative integer. The conventions about binomial coefficients include \(\binom{t}{a}=0\) for \(t<a\); all parameters appearing in profiles are nonnegative integers unless specified.

## Proof

**1. Canonical early-one profile.** Fix a word \(w\) with \(k>0\) occurrences of \(0^a1^b\). There are at least \(a\) zeros. Locate the \(a\)-th zero, and label, in increasing order, the \(q\) ones occurring strictly after that zero. Necessarily \(q\ge b\). Let \(t_i\) be the number of zeros before the \(i\)-th labeled one. Then \(a\le t_1\le\cdots\le t_q\). If an occurrence uses the \(i\)-th labeled one as its earliest one, then the other \(b-1\) ones can be selected in \(\binom{q-i}{b-1}\) ways and the preceding \(a\) zeros in \(\binom{t_i}{a}\) ways. Every occurrence has exactly one earliest one. Therefore
\[
 k=\sum_{i=1}^{q-b+1}\binom{q-i}{b-1}\binom{t_i}{a}.
\]
Only the first \(r=q-b+1\) values of \(t_i\) enter this equation. They form the constrained profile \(\pi\) in the statement.

**2. Finite profile bounds.** Since \(t_i\ge a\), every \(\binom{t_i}{a}\ge1\). The hockey-stick identity gives
\[
k\ge\sum_{i=1}^{q-b+1}\binom{q-i}{b-1}=\binom qb.
\]
Moreover, the last summand is \(\binom{b-1}{b-1}\binom{t_r}{a}=\binom{t_r}{a}\), so \(\binom{t_r}{a}\le k\). Each binomial grows without bound as its upper argument grows with its positive lower argument fixed. Hence only finitely many profiles are possible and the displayed bounds provide an exact terminating enumeration.

**3. Unique factorization and free slots.** For fixed \(\pi=(q;t_1,\ldots,t_r)\), every corresponding word has precisely the form
\[
 1^{x_1}0\,1^{x_2}0\cdots1^{x_a}0\;
 0^{t_1-a}1\,0^{t_2-t_1}1\cdots0^{t_r-t_{r-1}}1\;
 0^{y_1}1\cdots0^{y_{b-1}}1\,0^{y_b},
\]
where \(x_1,\ldots,x_a,y_1,\ldots,y_b\) are arbitrary nonnegative integers. For \(r=1\), the constrained middle block consists only of \(0^{t_1-a}1\). For \(b=1\), the final block consists only of \(0^{y_1}\). These formulas are interpreted accordingly without introducing empty-index ambiguities.

Indeed, the first \(a\) zeros delimit exactly \(a\) slots for ones, and the total number of zeros before each of the first \(r\) post-boundary ones fixes all intermediate zero gaps. The remaining \(b-1\) ones have arbitrary preceding zero gaps, followed by an arbitrary final zero gap. Conversely, every choice of these \(a+b\) integers yields a word with precisely the specified constrained profile and exactly \(k\) occurrences, by step 1. The factorization is unique: the first \(a\) zeros, the following \(q\) ones, and the recorded preceding-zero counts recover every slot length. It follows that profiles and slot vectors do not double-count words.

**4. Enumeration and exact degree.** The length of a word with this profile is
\[
 |w|=q+t_r+\sum_{j=1}^{a}x_j+\sum_{j=1}^{b}y_j.
\]
The \(a+b\) independent nonnegative slot variables contribute \((1-z)^{-(a+b)}\), while the constrained baseline contributes \(z^{q+t_r}\). Summation over all profiles proves the formal power-series identity and its coefficient formula. The numerator is a polynomial with nonnegative integer coefficients. It vanishes identically if and only if there is no admissible profile, equivalently no word with exactly \(k\) occurrences. Otherwise its value at \(z=1\) is the positive integer \(|\mathcal P_{a,b}(k)|\). Expanding the binomial coefficients in the coefficient formula for all sufficiently large \(n\) gives a polynomial of exact degree \(a+b-1\) and leading coefficient \(|\mathcal P_{a,b}(k)|/(a+b-1)!\). No finite experiment is used to justify this all-parameter conclusion.

**5. The first two-run exceptional frequency.** For \(a=b=2\) and \(k=5\), the bound \(\binom q2\le5\) restricts \(q\) to \(2\) or \(3\). For \(q=2\), the equation \(\binom{t_1}{2}=5\) has no integer solution. For \(q=3\), it is \(2\binom{t_1}{2}+\binom{t_2}{2}=5\) with \(2\le t_1\le t_2\), whose unique solution is \((t_1,t_2)=(2,3)\). The resulting words have the unique form \(1^{x_1}0\,1^{x_2}0\,1\,0\,1\,0^{y_1}1\,0^{y_2}\), with \(x_1+x_2+y_1+y_2=n-6\). This yields exactly \(\binom{n-3}{3}\) words for \(n\ge6\).

## Verification

The independent executable `check.py` computes scattered occurrence multiplicities by standard right-to-left subsequence dynamic programming on every binary word of length at most 15, and compares aggregate counts with the constrained-profile formula. It verifies 3,168 exact parameter-and-length cells for \(1\le a,b\le4\), \(a+b\le n\le15\), and \(1\le k\le18\). It separately checks the unique \((3;2,3)\) profile and its binomial coefficient formula through \(n=39\). All comparisons passed (see `check_output.txt`). The proof, not the finite tests, establishes the identities for all allowed parameters.

To reproduce from the containing folder: `python3 check.py`.

## Relationship to prior work

Menon and Singh (2023/2024) give explicit formulas for frequencies through four and analyze maximum occurrence counts. Tian (2025) supplies a general occurrence formula and algorithms involving primitive words, but the inspected results do not state this unique two-run profile decomposition or the resulting closed coefficient formula. Bruda (first public June 30, 2026) proves eventual polynomiality of degree at most \(\ell-r+1\) for general binary patterns with \(r\ge2\) runs. For the two-run pattern of length \(\ell=a+b\), that upper bound is \(a+b-1\); the paper identifies \(0^21^2\) at frequency five as an example outside its sufficient sharpness conditions and explicitly leaves a full characterization of sharpness open. The finding here gives an exact positive-coefficient numerator and an if-and-only-if sharpness criterion throughout the two-run class. The paper's upper bound alone does not imply this sharpness or exact enumeration. The present contribution does not claim discovery of the \(0^21^2,k=5\) exception itself.

## Limitations

This result does not treat zero occurrences, patterns with three or more runs, or nonbinary alphabets. The profile enumerator is finite for fixed parameters but may have substantial cost when \(k\) grows; no polynomial-time complexity bound in the binary encoding of \(k\) is asserted. No claim is made about closed arithmetic descriptions of all attainable \(k\) without evaluating the finite profile criterion. Publication priority beyond the inspected sources is not independently certified.

## References

1. G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578v1, first public June 30, 2026. https://arxiv.org/abs/2607.02578
2. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870v1, June 13, 2023; *Discrete Mathematics* 347 (2024), 113928. https://arxiv.org/abs/2306.07870
3. R. Tian, *Counting occurrences of a pattern in a binary word*, arXiv:2507.03205v1, July 3, 2025. https://arxiv.org/abs/2507.03205
