# Sharp finite Stieltjes-jet recovery of zero-mean periodic Dirichlet series

## Finding
For every integer \(q\ge2\), real shift \(x>0\), and complex-valued \(q\)-periodic sequence \(f\) satisfying \(\sum_{j=0}^{q-1}f(j)=0\), put
\[
L(s,f,x)=\sum_{n=0}^{\infty}\frac{f(n)}{(n+x)^s},\qquad \operatorname{Re}(s)>0.
\]
The series converges by Dirichlet's test and is analytic on this half-plane. Write its Taylor expansion about \(s=1\) as
\[
L(s,f,x)=\sum_{k\ge0}\frac{(-1)^k\gamma_k(f,x)}{k!}(s-1)^k.
\]
Then the finite vector \(\bigl(\gamma_0(f,x),\ldots,\gamma_{q-2}(f,x)\bigr)\) uniquely determines all \(q\) values of \(f\), and \(q-1\) is the minimum number of arbitrary linear measurements necessary on this \((q-1)\)-dimensional space.

A quantitative certificate of invertibility is the following strict determinant inequality. Let \(\gamma_j(a)\) denote the generalized Hurwitz Stieltjes constant for the shift \(a>0\). Define the \((q-1)\)-square matrix \(G\), with \(0\le k,i\le q-2\), by
\[
G_{ki}=\frac1q\sum_{j=0}^{k}\binom kj(\log q)^{k-j}
\left[\gamma_j\!\left(\frac{x+i}{q}\right)-\gamma_j\!\left(\frac{x+i+1}{q}\right)\right].
\]
Then \(\det G>0\) for every \(q\ge2\) and \(x>0\). Recovery is by solving \(Gr=(\gamma_0(f,x),\ldots,\gamma_{q-2}(f,x))^{\mathsf T}\), then taking \(f(0)=r_0\), \(f(i)=r_i-r_{i-1}\) for \(1\le i\le q-2\), and \(f(q-1)=-r_{q-2}\).

More generally, \(q-1\) distinct positive real values of \(L(s,f,x)\), or its first \(q-1\) derivatives at any fixed positive real \(s\), uniquely determine \(f\). A nonzero series in this family has at most \(q-2\) positive real zeros, counted with multiplicity. This bound is sharp in the strongest possible sense: for every choice of \(q-2\) distinct positive real numbers, exactly one real one-dimensional family of sequences realizes them as its entire positive-real zero set, with all zeros simple.

## Assumptions and scope
The period \(q\ge2\) is specified but need not be the least period. The coefficients may be complex, and the mean-zero condition is exact. The shift \(x\) is positive real. Zero counts refer only to the open real interval \((0,\infty)\) in the \(s\)-variable; multiplicities are analytic multiplicities. For the sharpness realization, take real coefficients.

## Proof
**1. A positive integral kernel.** Form \(P(z)=\sum_{j=0}^{q-1}f(j)z^j\). The mean-zero assumption gives \(P(1)=0\), so uniquely
\[
P(z)=(1-z)R(z),\qquad R(z)=\sum_{i=0}^{q-2}r_i z^i.
\]
The transformation between the \(q-1\) values \(r_i\) and the mean-zero \(q\)-tuple \(f\) is bijective, with the recovery formulas stated above. For \(\operatorname{Re}(s)>1\), the gamma integral and the geometric series give
\[
L(s,f,x)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}
\frac{e^{-xt}P(e^{-t})}{1-e^{-qt}}\,dt
=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}
\frac{e^{-xt}R(e^{-t})}{D_q(t)}\,dt,
\quad D_q(t)=\sum_{a=0}^{q-1}e^{-at}>0.
\]
The latter integral converges locally uniformly for \(\operatorname{Re}(s)>0\): at zero its integrand is \(O(t^{\operatorname{Re}(s)-1})\), up to logarithmic factors after differentiating in \(s\), and at infinity it decays exponentially because \(x>0\). This agrees with the Dirichlet series by analytic continuation. Define positive real functions
\[
H_i(s)=\frac1{\Gamma(s)}\int_0^\infty
\frac{t^{s-1}e^{-(x+i)t}}{D_q(t)}\,dt,
\qquad 0\le i\le q-2,\quad s>0.
\]
Thus \(L(s,f,x)=\sum_i r_i H_i(s)\). Equivalently,
\[
H_i(s)=q^{-s}\left[\zeta\!\left(s,\frac{x+i}{q}\right)-
\zeta\!\left(s,\frac{x+i+1}{q}\right)\right],
\]
with the removable singularity at \(s=1\) understood.

**2. Strict sign-regularity and Wronskians.** Fix \(1\le m\le q-1\). For any \(0<s_1<\cdots<s_m\), Andréief's continuous Cauchy–Binet identity, applied with the positive weight \(D_q(t)^{-1}\), gives
\[
\det[\Gamma(s_a)H_{i_b}(s_a)]_{a,b=1}^{m}
=\int_{0<t_1<\cdots<t_m}
\det[t_\ell^{s_a-1}]_{a,\ell=1}^{m}
\det[e^{-(x+i_b)t_\ell}]_{\ell,b=1}^{m}
\prod_{\ell=1}^m\frac{dt_\ell}{D_q(t_\ell)},
\]
where \(0\le i_1<\cdots<i_m\le q-2\). The first determinant is strictly positive: setting \(u_\ell=\log t_\ell\) makes it the generalized exponential Vandermonde determinant \(\det[e^{(s_a-1)u_\ell}]\). The second has sign \((-1)^{m(m-1)/2}\) and never vanishes, by the same exponential Vandermonde property with negative, strictly ordered exponents. For completeness, nonvanishing of an exponential Vandermonde follows by induction from Rolle's theorem applied after dividing a nonzero exponential combination by its lowest exponential; its sign is fixed by the ordinary Vandermonde in a confluent limit. The integrand has constant strict sign on the entire ordered simplex, and integrability follows from \(s_a>0\), \(x>0\). Hence
\[
(-1)^{m(m-1)/2}\det[H_{i_b}(s_a)]_{a,b=1}^{m}>0.
\]
For derivatives at a common point \(s>0\), differentiate \(\Gamma(s)H_i(s)\) under the integral. Its order-\(k\) derivative replaces \(t^{s-1}\) by \(t^{s-1}(\log t)^k\). Andréief then gives a determinant with first factor
\[
\det[t_\ell^{s-1}(\log t_\ell)^k]_{0\le k<m,1\le\ell\le m}
=\left(\prod_{\ell=1}^m t_\ell^{s-1}\right)
\prod_{1\le a<b\le m}(\log t_b-\log t_a)>0.
\]
Multiplication of all the functions by the same positive \(\Gamma(s)\) changes each Wronskian by \(\Gamma(s)^m\), using a triangular derivative row transformation. Therefore every Wronskian of the first \(m\) functions \(H_0,\ldots,H_{m-1}\) is nonzero on \((0,\infty)\), with sign \((-1)^{m(m-1)/2}\).

**3. Strict recovery and zero counting.** Nonzero Wronskians of every initial segment imply the extended complete Chebyshev property. Here is a direct Rolle argument. Because \(H_0>0\), divide any nonzero combination \(F\) by \(H_0\). The derivative belongs to the span of the \(m-1\) functions \((H_i/H_0)'\), \(1\le i<m\). Their prefix Wronskians equal the corresponding Wronskians of \(H_0,\ldots,H_k\), divided by positive powers of \(H_0\), and hence are nonzero. Induction and Rolle's theorem (including multiplicities) show that a nonzero combination of \(m\) basis functions has at most \(m-1\) positive real zeros, counted with multiplicity. For complex coefficients, apply the same real-valued argument to a nonzero real or imaginary part of the coefficient vector: every real zero of the original series, with its full analytic multiplicity, is a zero of that real combination of at least the same multiplicity. Taking \(m=q-1\) gives the claimed \(q-2\) zero bound and proves that a nonzero coefficient vector cannot vanish at \(q-1\) distinct positive real samples. The nonzero Wronskian at any \(s_0>0\) also proves injectivity from the first \(q-1\) derivatives there.

At \(s_0=1\), the coefficients satisfy \(\gamma_k(f,x)=(-1)^k L^{(k)}(1,f,x)\). For the difference basis, the standard Laurent expansion \(\zeta(s,a)=1/(s-1)+\sum_{j\ge0}(-1)^j\gamma_j(a)(s-1)^j/j!\) and the Leibniz rule applied to \(q^{-s}\) yield precisely the displayed matrix \(G\). Its determinant is the Wronskian determinant at \(1\), times \(\prod_{k=0}^{q-2}(-1)^k\). Since both factors have sign \((-1)^{(q-1)(q-2)/2}\), \(\det G>0\), proving recovery.

There are \(q-1\) complex degrees of freedom, so any \(q-2\) linear observations necessarily have a nontrivial kernel, proving the minimality of the Stieltjes-jet length. For any prescribed \(q-2\) distinct positive real nodes, the \((q-2)\times(q-1)\) evaluation matrix has rank \(q-2\), since any ordered \((q-2)\)-column minor is nonzero by the same integral determinant argument. Its real nullspace is one-dimensional; the resulting nonzero real series has the prescribed zeros. The zero bound forces these zeros to be simple and prohibits any others on \((0,\infty)\). For \(q=2\), the prescribed set is empty and the assertion reduces to \(H_0>0\).

## Verification
Run `python verify.py` with `mpmath` installed. The code independently builds the matrix from generalized Stieltjes constants, checks its positive determinant for \(q=2,3,4,5\) at two positive shifts, verifies the orientation of sample-value determinants and exact-data coefficient recovery at elevated precision, and constructs a nonzero period-five sequence with three prescribed positive real zeros. The included \(`verification_output.txt`\) is the resulting record. These finite calculations are not a proof of the universal assertions, which follow from the positive integral and determinant argument above.

## Relationship to prior work
Bayad and Rihane (2026, first posted October 9) introduce these generalized Stieltjes coefficients for periodic Hurwitz-type series and express them linearly in the periodic data; their formulas and derivative identities supply a natural basis for this inverse question. Their main results address continuation, functional equations, evaluation and examples, not the strictly positive finite determinant, minimal recovery count or complete positive-real zero bound proved here. Chatterjee and Murty (2014) study vanishing at \(s=1\) for algebraically constrained periodic data; a single nonvanishing criterion does not entail reconstruction of arbitrary complex mean-zero sequences from a sharp number of derivatives. The argument employs the classical strict sign-regularity of exponential kernels and the standard Chebyshev-system principle, specialized to a new arithmetic determinant and recovery question. An implicit formulation in the older total-positivity literature cannot be ruled out by the searches performed.

## Limitations
The shift must be positive real and the period must be known. No uniform stability or numerical condition-number bound as \(q\) or \(x\) varies is established. The zero bound concerns the positive real \(s\)-axis and says nothing about zeros in the complex plane or on the negative real axis. Nonzero-mean series have a pole at \(s=1\), and the theorem does not extend to them without changing the data model. The sharp real-zero constructions generally require freely chosen real coefficients, not fixed arithmetic characters. Numerical checks are finite; this is not independent validation.

## References
1. A. Bayad and S. E. Rihane, *Stieltjes constants for Hurwitz-type L-series attached to periodic arithmetic functions*, arXiv:2610.13136v1 (first public version, 2026-10-09), especially equations (2.1), (3.7), (3.10).
2. T. Chatterjee and M. R. Murty, *Non-vanishing of Dirichlet series with periodic coefficients*, arXiv:1405.6982 (2014); Journal of Number Theory 145 (2014), 1–21.
3. S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience, 1966 (classical general background).
