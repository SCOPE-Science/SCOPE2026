# Exact classification of infinitary harmonic numbers with four I-components

## Statement

Let
\[
I=\{p^{2^a}: p\text{ prime},\ a\ge 0\}.
\]
Every integer \(N>1\) is uniquely a product of distinct elements of \(I\); these factors are its **I-components**, and \(J(N)\) denotes their number. If the I-components are \(x_1,\dots,x_J\), then the infinitary harmonic mean is
\[
H_\infty(N)=2^J\prod_{i=1}^J\frac{x_i}{x_i+1}.
\]
An infinitary harmonic number (IHN) is an \(N\) for which \(H_\infty(N)\) is an integer.

**Theorem.** The infinitary harmonic numbers with exactly four I-components are precisely
\[
\boxed{270,\ 420,\ 630,\ 9100,\ 46494,\ 646425}.
\]
Their ordered I-components and infinitary harmonic means are:

| \(N\) | ordered I-components | \(H_\infty(N)\) |
|---:|:---|---:|
| 270 | \((2,3,5,9)\) | 6 |
| 420 | \((3,4,5,7)\) | 7 |
| 630 | \((2,5,7,9)\) | 7 |
| 9100 | \((4,7,13,25)\) | 10 |
| 46494 | \((2,7,41,81)\) | 9 |
| 646425 | \((9,17,25,169)\) | 13 |

Combining this theorem with Hasanalizade's 2026 classification for \(J\le 3\) gives the immediate corollary
\[
J(N)\le4\quad\Longleftrightarrow\quad
N\in\{1,6,45,60,90,270,420,630,9100,15925,46494,646425\}
\]
for infinitary harmonic \(N\).

## Proof

Put \(\rho(x)=x/(x+1)\), which is strictly increasing for positive \(x\). Suppose that \(N\) is an IHN with four I-components, ordered as
\[
2\le x_1<x_2<x_3<x_4,
\]
where each \(x_i\in I\). Write \(c=H_\infty(N)\). Hagis and Cohen proved that an IHN with \(J\) I-components satisfies
\[
\frac{2^{J+1}}{J+2}\le H_\infty(N)<2^J.
\]
For \(J=4\), integrality therefore forces
\[
c\in\{6,7,8,9,10,11,12,13,14,15\}.
\]
For each such \(c\), set \(t_0=c/16\). The defining equation is
\[
\rho(x_1)\rho(x_2)\rho(x_3)\rho(x_4)=t_0. \tag{1}
\]

The key observation makes the search finite at every stage. Suppose \(x_1,\ldots,x_k\) have been fixed and \(m=4-k\) components remain. Define
\[
t_k=\frac{t_0}{\rho(x_1)\cdots\rho(x_k)}.
\]
If a completion exists and \(y=x_{k+1}\), then every remaining component is at least \(y\). Hence monotonicity of \(\rho\) gives
\[
t_k=\prod_{j=k+1}^{4}\rho(x_j)\ge \rho(y)^m. \tag{2}
\]
Since a feasible residual product is strictly below 1, inequality (2) gives a finite upper bound for \(y\): it is at most the largest integer satisfying
\[
\left(\frac{y}{y+1}\right)^m\le t_k. \tag{3}
\]
Thus one may enumerate only I-components above the preceding component and within the exact bound (3).

Applying (3) successively with exact rational arithmetic gives universal bounds
\[
x_1\le61,\qquad x_2\le765,\qquad x_3\le131070.
\]
After choosing \(x_1,x_2,x_3\), equation (1) leaves no search for the fourth component. The residual \(t_3\) must satisfy
\[
\rho(x_4)=t_3,
\]
so necessarily
\[
x_4=\frac{t_3}{1-t_3}. \tag{4}
\]
The finite exact enumeration therefore consists only of testing whether the rational number in (4) is an integer, is larger than \(x_3\), and belongs to \(I\).

The supplied verifier performs precisely this exhaustive enumeration using integer and `Fraction` arithmetic. It examines 48,733 admissible three-component branches. Equation (4) is integral for 289 of them; the largest such integer candidate is \(2^{32}-1\). Exactly six candidates are I-components larger than \(x_3\), giving the six rows in the table above. A separate direct exact evaluation of \(16\prod_i x_i/(x_i+1)\) verifies the displayed harmonic mean for every surviving row. This proves both completeness and the converse.

## Context and prior literature

Hagis and Cohen introduced infinitary harmonic numbers and proved that only finitely many IHNs can have any specified number of I-components. Their 1990 paper also reported a computer search up to \(10^6\); all six numbers in the theorem occur in that historical table, but the bounded table does not establish completeness for \(J=4\).

Hasanalizade (2026) made the small-component boundary explicit: Lemma 2.3(a) states that the IHNs with \(J\le3\) are exactly \(\{1,6,45,60,90,15925\}\), and the subsequent argument treats \(J\ge4\) without classifying the \(J=4\) case. The theorem above advances that exact boundary by one I-component.

OEIS A063947 records known infinitary harmonic numbers, while A361385 records the number of I-components of those terms. These data independently agree with the six classified values, but are used only as corroboration, not as the completeness argument.

## Reproducibility

Run

```text
python artifacts/verify.py
```

with Python 3. The script uses only the standard library, exact rational arithmetic, a sieve for bounded I-components, and deterministic 64-bit primality testing for the uniquely determined final candidates. The expected deterministic output is stored in `artifacts/verification.txt`.

## Limitations

The result classifies only the case \(J=4\); it does not address the open question of whether infinitely many infinitary harmonic numbers exist. The proof is computer-assisted in its finite enumeration, although the finiteness and completeness bounds are proved explicitly and every arithmetic test is exact. No formal proof-assistant verification is claimed.

Originality is asserted only to the best of our knowledge. Searches covered the foundational 1990 paper, the 2026 small-component result, exact and synonymous web queries, OEIS component-count data, and the current SCOPE archive. No earlier proof classifying all \(J=4\) IHNs was located. A residual risk remains that an equivalent classification appears under different terminology or in literature not indexed by the searches consulted.

## References

1. P. Hagis Jr. and G. L. Cohen, “Infinitary harmonic numbers,” *Bulletin of the Australian Mathematical Society* **41** (1990), 151–158. DOI: https://doi.org/10.1017/S0004972700017949
2. E. Hasanalizade, “Upper bounds for infinitary harmonic numbers and infinitary harmonious tuples,” *Bulletin of the Australian Mathematical Society* (published online 17 June 2026). DOI: https://doi.org/10.1017/S0004972726101324
3. G. L. Cohen, “On an integer's infinitary divisors,” *Mathematics of Computation* **54** (1990), 395–411. DOI: https://doi.org/10.1090/S0025-5718-1990-0993927-5
4. OEIS A063947, “Infinitary harmonic numbers”: https://oeis.org/A063947
5. OEIS A361385, “Number of I-components of the n-th infinitary harmonic number”: https://oeis.org/A361385
