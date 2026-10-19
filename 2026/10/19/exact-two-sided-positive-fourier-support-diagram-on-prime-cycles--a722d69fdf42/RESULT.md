# Exact two-sided positive Fourier-support diagram on prime cycles

## Finding

Let \(p\ge3\) be an odd prime and let \(G=\mathbb Z/p\mathbb Z\). For nonzero functions \(f:G\to[0,\infty)\) whose unnormalized discrete Fourier transforms \(\widehat f\) are also pointwise nonnegative, the attainable pairs
\[
(k,\ell)=\bigl(|\operatorname{supp}f|,|\operatorname{supp}\widehat f|\bigr)
\]
are **exactly**
\[
\boxed{1\le k,\ell\le p,\quad k\equiv\ell\equiv1\pmod2,\quad k+\ell\ge p+1.}
\]
Every such pair has an explicit witness strictly positive at every position and frequency in its respective support. Thus simultaneous pointwise positivity and positive definiteness impose no support-cardinality restrictions beyond oddness and prime-cyclic uncertainty.

## Assumptions and scope

Write \(\zeta=e^{2\pi i/p}\) and use the Fourier convention
\[
\widehat f(j)=\sum_{x\in G}f(x)\zeta^{-jx},\qquad
f(x)=\frac1p\sum_{j\in G}\widehat f(j)\zeta^{jx}.
\]
All inequalities for functions or Fourier transforms are real and pointwise. The condition \(\widehat f\ge0\) is equivalent to positive definiteness of \(f\) in this finite abelian setting. Supports count nonzero group elements, not intervals with multiplicity. The result concerns **cardinalities** of supports; arbitrary prescribed support sets are not asserted to occur. It makes no assertion for composite cyclic orders or even characteristic.

## Proof

**Necessity.** Because \(f\ge0\), \(f\not\equiv0\), its zero-frequency coefficient \(\widehat f(0)=\sum_xf(x)\) is strictly positive. Because \(\widehat f\ge0\) and is not zero, Fourier inversion gives \(f(0)=p^{-1}\sum_j\widehat f(j)>0\). Reality of \(f\) implies \(\widehat f(-j)=\overline{\widehat f(j)}\); since the latter is nonnegative real, the Fourier transform is even. Conversely, reality of \(\widehat f\) implies that \(f\) is even. Both supports are therefore inversion-symmetric and contain zero. As \(p\) is odd, they have odd cardinalities. Finally, Tao's prime-cyclic Fourier uncertainty theorem, valid for every nonzero complex function, gives \(k+\ell\ge p+1\).

**Sufficiency with the smaller support on the spatial side.** Given an admissible pair with \(k\le\ell\), write
\[
p=2m+1,\qquad k=2r+1,\qquad \ell=p-2s.
\]
The cardinality constraints give
\[
0\le s\le r\le m-s,\qquad\text{and hence}\quad 2s\le m.
\]
Set \(c_j=\cos(2\pi j/p)\) for \(0\le j\le m\). The real numbers satisfy \(1=c_0>c_1>\cdots>c_m>-1\). If \(s>0\), every index \(j\in\{m-s+1,\ldots,m\}\) satisfies
\[
4j\ge4(m-s+1)>2m+1=p,
\]
so \(c_j<0\). (When \(s=0\), the indicated index set is empty.) Consider the real polynomial
\[
P_{r,s}(t)=(t+2)^{r-s}\prod_{j=m-s+1}^{m}(t-c_j).
\]
All its linear factors have strictly positive constant and linear coefficients. On the discrete cosine grid \(\{c_0,\ldots,c_m\}\), every value \(P_{r,s}(c_j)\) is nonnegative, and it is zero **if and only if** \(m-s+1\le j\le m\): at any other grid point, each factor is strictly positive. The function \(P_{r,s}(\cos(2\pi j/p))\) on \(G\) therefore vanishes at exactly \(2s\) frequencies and is strictly positive at the other \(p-2s=\ell\).

Now expand the symmetric Laurent polynomial
\[
P_{r,s}\!\left(\frac{z+z^{-1}}2\right)
=\sum_{h=-r}^{r}a_hz^h.
\]
Each of the \(r\) factors has the form \(\frac12(z+z^{-1})+b\) with \(b>0\). For every integer \(h\) between \(-r\) and \(r\), choose \(|h|\) factors contributing \(z^{\operatorname{sgn}(h)}/2\) and the remaining factors contributing their positive constant terms. Hence \(a_h>0\) for **every** \(|h|\le r\); there are no other exponents. If \(r=0\), this assertion is immediate from the empty product. Since \(r\le m\), these \(2r+1\) exponents are distinct modulo \(p\). Define \(f(h)=a_h\) for \(-r\le h\le r\), interpreted modulo \(p\), and \(f=0\) elsewhere. Then \(f\ge0\) has exactly \(k=2r+1\) nonzero values, and direct Fourier evaluation yields
\[
\widehat f(j)=P_{r,s}(\cos(2\pi j/p))\ge0
\]
with exactly \(\ell\) nonzero values. This constructs every admissible pair with \(k\le\ell\).

**Fourier duality.** If instead \(k>\ell\), first construct \(g\ge0\) with \(\widehat g\ge0\) and support sizes \((\ell,k)\), using the previous case. Define \(f=\widehat g\). The unnormalized Fourier involution identity gives
\[
\widehat f(x)=\widehat{\widehat g}(x)=p\,g(-x)\ge0.
\]
Thus \(f\) has support sizes \((k,\ell)\). Both inequalities remain pointwise, and every nonzero value remains strictly positive. The two orientations exhaust all allowed pairs, proving the theorem.

## Verification

The proof for all odd primes is analytic and does not rely on numerical enumeration. An accompanying independent checker, `check_support.py`, constructs Laurent coefficients, evaluates the direct discrete cosine transform, checks Fourier values against the claimed polynomial factorization, and verifies exactly the expected number of zeros using 90-decimal-digit arithmetic. It tests all admissible pairs for the ten odd primes \(3,5,7,11,13,17,19,23,29,31\), totaling 502 cases. It also checks double-transform duality for the reversed orientation. The checker needs Python 3.10+ and `mpmath` 1.3+; see `requirements.txt`. The analytic root-ordering and positive-coefficient arguments, not floating-point thresholds, establish exact zeros and strict signs for arbitrary primes.

## Relationship to prior work

Tao's prime-order uncertainty theorem supplies exactly the lower bound \(k+\ell\ge p+1\), but permits arbitrary complex values and its converse does not preserve either positivity constraint. Work of Kolountzakis and Révész formulates positive-definite Fourier cones and Turán mass optimization on finite abelian groups; those optimization statements do not classify the simultaneous **cardinalities of two strictly supported nonnegative functions**. Wang and Ye's finite-group estimates bound values of positive-definite functions and discuss Fourier-support parameters, rather than constructing every admissible pair. A related positivity-only support classification of functions with \(f\ge0\) does not require \(\widehat f\ge0\); its existential conclusion alone does not give the present two-sided witnesses. The additional ingredient here is a product with positive Laurent coefficients whose roots are the lowest cosine-grid values, together with Fourier duality.

## Limitations

The classification is only by support cardinality. It neither characterizes prescribed spatial and frequency support locations nor optimizes amplitudes or stability within the positive-definite cone. The chosen witnesses depend on cyclotomic cosine values and are not generally rational. Numerical verification is finite and is not claimed as an infinite proof. Although accessible comparable literature does not state this exact two-sided classification, a previously unnoticed equivalent formulation among older positivity or Carathéodory–Fejér results remains possible; no independent mathematical audit has occurred.

## References

1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first publicly submitted 2003-08-29. Full text: https://arxiv.org/html/math/0308286v6 .
2. M. N. Kolountzakis and Sz. G. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first publicly submitted 2003-12-10. Full text: https://arxiv.org/abs/math/0312218 .
3. L. Wang and K. Ye, *An estimate for positive definite functions on finite abelian groups and its applications*, arXiv:2503.06908, first publicly submitted 2025-03-10. Full text: https://arxiv.org/abs/2503.06908 .
