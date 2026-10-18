# Cyclotomic zero-line rigidity for rational finite-parabola Fourier data

## Finding

For every odd prime \(p\ge5\), write \(\zeta=\exp(2\pi i/p)\) and, for a nonzero rational-valued sequence \(f:\mathbb F_p\to\mathbb Q\), define the quadratic Fourier transform
\[
F_f(a,b)=\sum_{t\in\mathbb F_p} f(t)\zeta^{at^2+bt},\qquad (a,b)\in\mathbb F_p^2.
\]
There are exactly four possible zero-set shapes, with the stated necessary and sufficient conditions:

1. **Empty:** \(f\) is not constant, has nonzero sum, and is not odd under any reflection.
2. **One point:** \(Z(F_f)=\{(0,0)\}\) precisely when \(f\) is nonconstant, has zero sum, and is not odd under any reflection.
3. **Punctured frequency axis:** \(Z(F_f)=\{(0,b):b\ne0\}\), of size \(p-1\), precisely when \(f\) is a nonzero constant.
4. **A complete line:** for exactly one \(s\in\mathbb F_p\), \(Z(F_f)=\{(a,-as):a\in\mathbb F_p\}\), of size \(p\), precisely when \(f(t)=-f(s-t)\) for every \(t\).

All four shapes occur for every prime \(p\ge5\). In particular, for any even exact support \(k\) with \(2\le k\le p-1\), the largest possible rational-data zero count is \(p\); the known unrestricted complex-data sharp count is \(p+k-2\). The gap is therefore exactly \(k-2\), strictly positive from four support points onward.

There is also a complete one-bit-amplitude census. Among sign sequences \(f:\mathbb F_p\to\{-1,0,1\}\) with exactly \(2r\) nonzero entries, \(1\le r\le(p-1)/2\), the counts of sequences having respectively \(p\), \(1\), and \(0\) quadratic Fourier zeros are
\[
N_p=p\binom{(p-1)/2}{r}2^r,
\quad N_1=\binom p{2r}\binom{2r}r-N_p,
\quad N_0=\binom p{2r}\left(2^{2r}-\binom{2r}r\right).
\]
For odd exact support smaller than \(p\), every sign sequence has no zeros. For full support \(p\), exactly the two constant sign sequences have \(p-1\) zeros; all other sign sequences have none. The zero vector is excluded.

## Assumptions and scope

The coefficient field is \(\mathbb Q\), embedded in \(\mathbb C\). The prime is at least five. No Fourier normalization factor is included (multiplying the transform by a nonzero scalar leaves zeros unchanged). Reflection parameters are elements of \(\mathbb F_p\), and \(f\) is extended by zero to the entire field when its support is proper. Sign-sequence counts distinguish labeled sequences, not equivalence classes under translations or global sign.

## Proof

**Cyclotomic coefficient lemma.** Given rational numbers \(d_0,\dots,d_{p-1}\), the identity \(\sum_{j=0}^{p-1}d_j\zeta^j=0\) holds if and only if all \(d_j\) are equal. Indeed, the coefficient polynomial is divisible in \(\mathbb Q[X]\) by the minimal polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\). Since its degree is at most \(p-1\), it must be a scalar multiple of \(\Phi_p\). This also proves the converse.

If \(a=0\) and \(b\ne0\), the exponent map \(t\mapsto bt\) is bijective. Applying the lemma shows that \(F_f(0,b)=0\) if and only if \(f\) is constant. At \((0,0)\), the transform equals \(\sum_t f(t)\).

Now fix \(a\ne0\). For each \(j\in\mathbb F_p\) let \(d_j=\sum_{at^2+bt=j}f(t)\). The quadratic exponent takes only \((p+1)/2<p\) distinct values; at least one \(d_j\) is therefore zero. If \(F_f(a,b)=0\), the coefficient lemma forces all \(d_j=0\). Write \(s=-b/a\). Equality \(at^2+bt=a(s-t)^2+b(s-t)\) holds, and each fiber is a pair \(\{t,s-t\}\), except the one fixed point \(s/2\). Thus \(d_j=0\) for all \(j\) is equivalent to
\[
f(t)=-f(s-t)\quad\text{for every }t\in\mathbb F_p.
\]
Conversely, that reflection-odd identity cancels the two members of every fiber, including the fixed point, and hence forces \(F_f(a,-as)=0\) for every \(a\ne0\); it also forces \(\sum_tf(t)=0\), giving the origin as a zero.

A nonzero \(f\) cannot be odd about two different reflection parameters. Indeed, if \(f(t)=-f(s-t)\) and \(f(t)=-f(s'-t)\), composition gives invariance under translation by \(s-s'\). If the parameters differ, that translation generates all of \(\mathbb F_p\), making \(f\) constant; oddness then makes this constant zero, a contradiction. Thus the reflection center is unique, and the four cases above exhaust all possibilities. Explicit examples are a point mass (no zero), a three-point zero-sum vector with nonzero entries \(1,1,-2\) (only the origin), a nonzero constant (punctured axis), and \(\delta_0-\delta_1\) (a complete line).

For any even support \(k=2r\le p-1\), choose a nonzero center \(s\), choose \(r\) distinct two-point reflection orbits, and place opposite nonzero rational weights on each pair; the support is exactly \(k\) and the zero count is \(p\). The upper bound follows from the four-shape classification. The complex-data optimum \(p+k-2\) is the sharp even-support statement of Li (2026); its claim concerns unrestricted complex coefficients and is not being reproved here.

For the sign census, choose the unique reflection parameter (\(p\) choices), then select \(r\) among the \((p-1)/2\) two-point orbits and select one of two opposite-sign orientations on each orbit. This yields \(N_p\), without overcounting because uniqueness was just proved. Exactly balanced sign sequences of support \(2r\) number \(B=\binom p{2r}\binom{2r}r\); they and only they have the origin as a zero. Every line case is balanced, so \(N_1=B-N_p\). Subtracting the balanced class from all \(\binom p{2r}2^{2r}\) sequences yields \(N_0\). Odd support cannot have equal positive and negative sign counts, so no zero is possible. At full support, oddness is impossible due to the reflection fixed point, while among sign sequences the only nonzero constants are the two all-sign vectors. This proves every asserted formula.

## Verification

An exact-integer diagnostic, `checker.py`, computes Fourier zeros using the cyclotomic coefficient criterion, not floating-point root evaluations. It exhausts every nonzero ternary sequence in dimensions five and seven and checks 10,000 reproducibly seeded rational-integer sequences in dimension eleven against the four-shape classification. Its checks are finite diagnostics; the proof above establishes the result for every prime \(p\ge5\). The exact combinatorial formulas follow algebraically from reflection-orbit counting, independent of any computer enumeration.

## Relationship to prior work

Dongwei Li's 2026 finite-parabola zero theorem gives sharp general-complex upper bounds \(p+k-2\) for even support \(k\), and develops reflection rigidity for extremizers of the complete mutually unbiased basis support problem. It does not state this coefficient-field-sensitive, all-support classification of exact zero-set shapes for rational data or the enumeration by sign support. Here cyclotomic irreducibility gives a stronger equality test only under the essential rationality hypothesis; the unrestricted complex bounds do not imply this test. Earlier work by Casazza and Fickus treats transforms of finite chirps and Gauss-sum behavior rather than the zero sets of arbitrary rational superpositions. Classical minimal-polynomial and quadratic-fiber identities are acknowledged as ingredients.

## Limitations

The rationality assumption is indispensable: complex coefficients may exhibit additional parabolic Fourier zeros, and no comparable four-shape theorem is claimed for arbitrary complex data. The word "sharp" concerns exact zero counts, not stability or near-zero amplitudes. The result does not classify complex extremizers, prove a new bound for general complex coefficients, or provide a robustness statement under coefficient perturbations. Historical priority for this arithmetic subcase is not independently certified.

## References

1. Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030 (first public version September 11, 2026); current related manuscript *Sharp Total-Support Uncertainty for the Standard Complete Set of Mutually Unbiased Bases*, arXiv:2609.16030v2, October 3, 2026. https://arxiv.org/abs/2609.16030
2. Peter G. Casazza and Matthew Fickus, *Fourier Transforms of Finite Chirps*, EURASIP Journal on Applied Signal Processing 2006, article 70204. https://doi.org/10.1155/ASP/2006/70204
3. Classical irreducibility of the prime cyclotomic polynomial \(\Phi_p\) over \(\mathbb Q\) and the quadratic Gauss-sum identity, standard prerequisites.
