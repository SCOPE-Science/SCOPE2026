# Exact three-sparse Fourier support spectra on elementary Abelian odd-prime groups
## Finding
Let \(p\) be an odd prime, \(d\ge2\), and \(G=\mathbb F_p^d\). If a function \(f:G\to\mathbb C\) has exactly three nonzero values, let \(S=\operatorname{supp}f\) and let \(r\) be the affine dimension of \(S\). Then \(r\in\{1,2\}\), and for every fixed support \(S\) the attainable values of \(|\operatorname{supp}\widehat f|\) depend only on \(r\):
\[
\{(p-j)p^{d-1}:j=0,1,2\}\qquad (r=1),
\]
\[
\{(p^2-j)p^{d-2}:j=0,1,2\}\qquad (r=2).
\]
Every listed value occurs on every support of the corresponding affine type. Equivalently, if \(H=\langle S-S\rangle\), then the zero set of \(\widehat f\) is a union of exactly \(j\in\{0,1,2\}\) cosets of \(H^\perp\). Consequently the exact global spectrum is
\[
\{p^d,(p-1)p^{d-1},(p-2)p^{d-1},p^d-p^{d-2},p^d-2p^{d-2}\}.
\]

## Assumptions and scope
The Fourier transform is
\[
\widehat f(\xi)=\sum_{x\in G}f(x)\exp\!\left(-\frac{2\pi i}p\langle \xi,x\rangle\right).
\]
All three values of \(f\) on \(S\) are required to be nonzero. The theorem covers every odd prime \(p\) and every dimension \(d\ge2\). The affine dimension of a three-point set is either one (collinear) or two (noncollinear).

## Proof
Translate the support so that one point is zero. Translation multiplies \(\widehat f\) by a character and therefore does not alter its zero set. Put \(H=\langle S-S\rangle\). Since \(f\) is supported on one affine coset of \(H\), the value of \(\widehat f(\xi)\) depends only on the restriction of \(\xi\) to \(H\). Thus each local Fourier value on \(H\) is repeated on one coset of \(H^\perp\), of size \(p^{d-r}\). It remains to classify the number of zeros in the local transform on \(H\).

If \(r=1\), choose a coordinate on \(H\cong\mathbb F_p\) so that the support is \(\{0,u,v\}\) with \(u,v\ne0\) and \(u\ne v\). Writing \(\zeta=e^{2\pi i/p}\), the local transform is
\[
F(t)=a+b\zeta^{ut}+c\zeta^{vt},\qquad t\in\mathbb F_p,
\]
with \(abc\ne0\). The prime-order Fourier-minor theorem implies that a three-term polynomial on the \(p\)-th roots of unity has at most two zeros. Hence \(F\) has at most two zeros. All zero counts occur on every fixed support. For zero zeros take \((a,b,c)=(3,1,1)\). For exactly one zero take \((a,b,c)=(-2,1,1)\): equality \(-2+\zeta^{ut}+\zeta^{vt}=0\) forces both unit summands to equal \(1\), hence \(t=0\). For exactly two zeros, prescribe zeros at \(t=0\) and \(t=1\); one explicit nonzero coefficient triple is
\[
(a,b,c)=(\zeta^u-\zeta^v,\ \zeta^v-1,\ -(\zeta^u-1)).
\]
The prime Fourier-minor theorem excludes a third zero.

If \(r=2\), an invertible affine-linear change of coordinates reduces the support to \(\{0,e_1,e_2\}\). The local transform is
\[
F(x,y)=a+b\zeta^x+c\zeta^y,\qquad (x,y)\in\mathbb F_p^2,
\]
with \(abc\ne0\). If \(F(x,y)=0\), then
\[
|a+b\zeta^x|=|c|.
\]
After squaring, this is one real affine-line condition on the unit-circle point \(\zeta^x\):
\[
\operatorname{Re}(a\overline b\,\zeta^{-x})=\frac{|c|^2-|a|^2-|b|^2}2.
\]
Because \(a\overline b\ne0\), a line meets the unit circle in at most two points, so there are at most two possible values of \(x\). For each such \(x\), the equation determines \(\zeta^y\), and hence \(y\), uniquely. Thus there are at most two local zeros.

Again all three counts occur. The triples \((3,1,1)\) and \((-2,1,1)\) give respectively zero zeros and the unique zero \((0,0)\). For two zeros, take
\[
(a,b,c)=(\zeta,-(1+\zeta),1).
\]
It vanishes at \((0,0)\) and \((1,2)\). Since \(p\) is odd, \(1+\zeta\ne0\), so all coefficients are nonzero; the preceding bound shows these are the only zeros.

Multiplying the local nonzero counts by \(|H^\perp|=p^{d-r}\) proves the two fixed-support formulas and the five-value global spectrum.

## Verification
The proof is analytic and covers all odd primes and all \(d\ge2\). The accompanying `verify.py` uses exact cyclotomic arithmetic for the normalized local transforms. It checks all collinear support shapes for \(p\in\{3,5,7,11\}\), verifies the three explicit witness families, exhaustively tests a finite integer coefficient box for the two-zero upper bound, and checks the noncollinear witnesses and upper bound on the same primes. No floating-point tolerance is used.

## Relationship to prior work
Bonami and Ghobber determine the minimum support size of the Fourier transform and classify equality cases for \(\mathbb Z_p^2\). In particular, for support size three their results identify the collinear supports as the minimizers, with minimum \(p(p-2)\). Their theorem does not list all exact Fourier-support sizes on a fixed three-point support, nor the noncollinear exact values \(p^2\), \(p^2-1\), and \(p^2-2\), and it does not state the all-dimensional affine-span reduction above.

Biró and Lev later obtain stronger structure-sensitive uncertainty inequalities in finite planes. Their results give broad lower bounds according to the geometry of the supports, but the inspected statements do not provide the complete exact three-sparse spectrum or the every-support realizability classification stated here. The collinear upper bound uses the prime cyclic Fourier-minor theorem, while the noncollinear bound follows from the elementary unit-circle intersection argument above.

## Limitations
The theorem is specific to exactly three nonzero time-domain coefficients over elementary Abelian groups of odd prime exponent. It does not classify support size four or larger, groups of composite exponent, or the characteristic-two three-point case. The finite verifier is corroborative only; the infinite quantifiers rest on the analytic proof.

## References
A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first posted 2010-03-26; Acta Sci. Math. (Szeged) 79 (2013), 507-528.

T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286; Math. Res. Lett. 12 (2005), 121-127.

A. Biró and V. F. Lev, *Uncertainty in finite planes*, arXiv:1808.07424; J. Funct. Anal. 281 (2021), 109026.
