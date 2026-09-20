# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The argument uses only Proposition 23 and Lemma 20 of Swanepoel--Villa (2013), plus an elementary reciprocal inequality.

The lower bound is forced by condition (12):
\[
s:=1/k_1+1/k_2<4-2^p=2a_p.
\]
Since \((k_1+k_2)s\ge4\), every admissible pair has
\[
2(k_1+k_2)>4/a_p.
\]

For the upper bound, \(x_p=1/a_p\to\infty\). Lemma 20 gives a Hadamard order in
\[
(x_p,(1+\varepsilon)x_p)
\]
for \(p\) sufficiently close to \(2\). With \(k_1=k_2=k\), condition (12) is exactly \(x_p<k<2x_p\). Conditions (13) and (14) both simplify to \(k<2x_p\), because
\[
1+(1-2^{1-p})=2(1-2^{-p}).
\]
Thus the symmetric pair is genuinely admissible, not merely admissible for condition (12). The resulting size is \(4k<(1+\varepsilon)4/a_p\), matching the universal lower bound asymptotically.

The Taylor expansion
\[
2-2^{p-1}=2(2-p)\ln2+O((2-p)^2)
\]
then gives the stated coefficient \(2/\ln2\).

No numerical or computational assumption is used.

## Originality — PASS (to the best of our knowledge)

The primary source was checked at the theorem, Proposition 23, Lemma 20, and proof-of-Theorem-6 level. It explicitly records the weaker displayed estimate
\[
4k<16/(4-2^p)\sim4/((2-p)\ln2).
\]
The present result instead identifies the asymptotically optimal size attainable by the entire Proposition 23 two-Hadamard family.

Searches covered the exact formulas \(4/(2-2^{p-1})\) and \(2/((2-p)\ln2)\), the phrases “maximal equilateral sets” and “Hadamard”, Proposition 23 with Swanepoel--Villa, and later work on equilateral sets in Banach spaces. No exact or stronger coverage was located. Later accessible papers found in these searches concern equilateral dimension, large equilateral sets, or other Banach-space settings rather than this asymptotic optimization.

Residual risk remains from literature that is unindexed, inaccessible, or expressed in substantially different terminology.

## Value — PASS

The result gives a quantitative sharpening of the principal Hadamard construction near the Hilbert-space endpoint \(p=2\):

- it halves the leading constant explicitly displayed in the 2013 proof;
- it proves that the new leading constant is best possible within the full two-Hadamard Proposition 23 framework, including asymmetric choices \(k_1\ne k_2\);
- it sharpens both the set-size parameter \(C(p)\) and the dimension threshold \(d_0(p)\) produced by that construction.

The result does not claim global optimality for \(m(\ell_p^d)\), and the existing logarithmic asymptotic gap remains.

## Scientific limitations

1. Construction-optimality is not global optimality for maximal equilateral sets.
2. The conclusion is asymptotic as \(p\uparrow2\); it does not optimize the best discrete Hadamard pair for each fixed \(p\).
3. The originality assessment is necessarily “to the best of our knowledge.”
