# Exact dyadic Stern-zero counts modulo seven and a sharp square-root discrepancy

## Finding

Let \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\) for integers \(n\geq1\) where appropriate. For each integer \(r\geq0\), set
\[
T_r=\#\{0\leq n<2^r: s(n)\equiv0\pmod7\}.
\]
The ordinary generating function, as a formal power series over \(\mathbb Q\), is
\[
\boxed{\sum_{r\geq0} T_r z^r=
\frac{1-z-2z^2+2z^3-4z^5}
{(1-2z)(1-z)(1+z+2z^3+4z^4)}.}
\]
Consequently \(T_0,T_1,\ldots,T_5=(1,1,1,1,1,5)\), and for every integer \(r\geq0\),
\[
\boxed{T_{r+6}=2T_{r+5}+T_{r+4}-4T_{r+3}+2T_{r+2}+8T_{r+1}-8T_r.}
\]
This is a minimal-order constant-coefficient homogeneous recurrence over \(\mathbb Q\). Further, with \(E_r=T_r-2^r/8-1/2\),
\[
\boxed{E_r=O(2^{r/2})\quad\text{and}\quad
\limsup_{r\to\infty}\frac{|E_r|}{2^{r/2}}>0.}
\]
Thus the square-root scale cannot be replaced by any smaller exponential growth factor. The density \(1/8\) itself is established prior work, not claimed as new.

## Assumptions and scope

The index \(r\) is a nonnegative integer and the modulus is exactly seven. An initial index \(n=0\) contributes to \(T_r\) for every \(r\), since \(s(0)=0\). Only the classical Stern diatomic sequence is considered. The arithmetic classification is primary MSC2020 11B75.

## Proof

**1. Eight projective states.** Consecutive Stern values are coprime: this follows inductively from the two child maps
\[
(a,b)\longmapsto(a,a+b),\qquad (a,b)\longmapsto(a+b,b)
\]
and the initial pair \((0,1)\). Therefore reduction modulo seven never yields \((0,0)\). Write \(t=a/b\) as an element of \(\mathbb P^1(\mathbb F_7)=\{0,1,\ldots,6,\infty\}\). The two child maps become
\[
L(t)=\frac{t}{t+1},\qquad R(t)=t+1
\]
with the usual projective conventions \(L(6)=\infty\), \(L(\infty)=1\), \(R(\infty)=\infty\). The complete transition table is

| \(t\) | \(0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) | \(\infty\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(L(t)\) | 0 | 4 | 3 | 6 | 5 | 2 | \(\infty\) | 1 |
| \(R(t)\) | 1 | 2 | 3 | 4 | 5 | 6 | 0 | \(\infty\) |

Every binary word of length \(r\), with leading zeroes allowed, represents one index in \([0,2^r)\), and its successive child maps take \((s(0),s(1))\) to the corresponding reduced pair. Thus \(T_r\) counts length-\(r\) paths starting at projective state zero and finishing at zero.

**2. Polynomial certificate.** For each possible starting state \(t\), let \(g_t(z)\) enumerate paths ending at zero: the coefficient of \(z^r\) is their number at length \(r\). The exact formal equations are
\[
g_t(z)={\bf1}_{t=0}+z\bigl(g_{L(t)}(z)+g_{R(t)}(z)\bigr).
\]
Set \(D(z)=(1-2z)(1-z)(1+z+2z^3+4z^4)\). The following eight **numerator polynomials** \(h_t(z)=D(z)g_t(z)\) give an explicit exact certificate:

| \(t\) | \(h_t(z)\) |
|---|---|
| 0 | \(1-z-2z^2+2z^3-4z^5\) |
| 1 | \(4z^4(1-z)\) |
| 2 | \(2z^3(1-z)\) |
| 3 | \(z^2(1-z)\) |
| 4 | \(2z^3(1-z)\) |
| 5 | \(z^2(1-z)\) |
| 6 | \(z(z-1)(2z^2-1)\) |
| \(\infty\) | \(4z^5\) |

Direct polynomial substitution verifies, for every state \(t\),
\[
h_t(z)=D(z){\bf1}_{t=0}+z\bigl(h_{L(t)}(z)+h_{R(t)}(z)\bigr).
\]
Because the system's matrix has constant term the identity, its formal-power-series solution is unique. Thus \(g_0(z)=h_0(z)/D(z)\), proving the claimed generating function. Multiplying by its denominator gives the displayed recurrence and initial values.

**3. Minimality.** The rational polynomials \(h_0(z)\) and \(D(z)\) are coprime (an exact rational Euclidean-algorithm check is included in `verify.py`). The reduced denominator therefore has degree six. Any eventually valid homogeneous linear recurrence with constant rational coefficients would give a denominator whose degree is at least six. Hence six is the minimal order.

**4. Leading term and sharp error.** Exact partial fractions yield
\[
g_0(z)=\frac{1}{8(1-2z)}+\frac{1}{2(1-z)}+
\frac{3+5z+2z^2+2z^3}{8(1+z+2z^3+4z^4)}.
\]
The reciprocal polynomial of the remaining quartic is
\[
Q(X)=X^4+X^3+2X+4
=(X^2+\alpha X+2)(X^2+\beta X+2),
\]
where \(\alpha=(1+\sqrt{17})/2\), \(\beta=(1-\sqrt{17})/2\). Both satisfy \(|\alpha|,|\beta|<2\sqrt2\), since \(17<49\). Each quadratic therefore has two distinct nonreal conjugate roots of modulus \(\sqrt2\). The four roots of \(Q\) are distinct because \(\alpha\ne\beta\). A partial-fraction expansion gives
\[
E_r=\sum_{j=1}^{4} c_j\lambda_j^r,
\qquad |\lambda_j|=\sqrt2.
\]
All four constants \(c_j\) are nonzero because the reduced numerator and denominator have no common root. This proves the upper bound. Moreover, for pairwise distinct unit complex numbers \(\omega_j=\lambda_j/\sqrt2\), Cesàro orthogonality yields
\[
\lim_{N\to\infty}\frac1N\sum_{r=0}^{N-1}
\left|\frac{E_r}{2^{r/2}}\right|^2
=\sum_{j=1}^{4}|c_j|^2>0.
\]
Consequently the normalized discrepancy has strictly positive limsup, establishing sharpness.

## Verification

Run `python3 verify.py` using only the Python standard library. The checker verifies all eight polynomial-state identities, coprimality of the numerator and denominator over \(\mathbb Q[z]\), exact dyadic counts by independently computing the classical Stern sequence for every \(0\le n<2^{18}\), and agreement of the recurrence with the eight-state transfer for \(0\le r\le300\). These finite checks test the explicit certificate; the formal uniqueness and spectral arguments above prove the all-index statements.

## Relationship to prior work

Reznick, *Regularity Properties of the Stern Enumeration of the Rationals*, arXiv:math/0610601 (first publicly posted 2006-10-19), proves limiting density \(1/(p+1)\) at every prime \(p\), develops finite-state distribution machinery, and calculates a detailed exact formula and sharp square-root error for modulus three. It also announces other modular coincidences for moduli 4, 5, 6, 9, and 11. Thus the general mechanism, the limiting \(1/8\) density at seven, and the possibility of a finite-order recurrence are **prior work**. The claims assessed here are the explicitly reduced modulus-seven generating function, the proven minimal sixth-order recurrence, and the sharp \(\sqrt{2}\)-scale discrepancy for this modulus. The projective eight-state numerator certificate makes the difference explicit. Dilcher and Stolarsky (2009) study a different Stern-polynomial/continued-fraction family; Coons and Shallit (2011) develop a binary-pattern expansion, not these modulus-seven counts.

## Limitations

This work does not supply formulas for all nonzero residue classes modulo seven, non-dyadic intervals, or other primes. The general finite-state method is not new. A manuscript cited by Reznick as *A Stern Introduction to Combinatorial Number Theory*, later referenced as 2012 course notes, was not available for full inspection; it might contain an equivalent computation, so historical priority is not fully resolved. No independent mathematical audit has been performed.

## References

1. B. Reznick, *Regularity Properties of the Stern Enumeration of the Rationals*, arXiv:math/0610601 (2006 preprint; *Journal of Integer Sequences* 11 (2008), Article 08.4.1), https://arxiv.org/abs/math/0610601 and https://cs.uwaterloo.ca/journals/JIS/VOL11/Reznick/reznick4.pdf.
2. K. Dilcher and K. B. Stolarsky, *Stern Polynomials and Double-Limit Continued Fractions*, *Acta Arithmetica* 140 (2009), 119–134, https://doi.org/10.4064/aa140-2-2.
3. M. Coons and J. Shallit, *A Pattern Sequence Approach to Stern's Sequence*, arXiv:1105.0086 (2011), https://arxiv.org/abs/1105.0086.
4. B. Reznick, *A Stern Introduction to Combinatorial Number Theory*, University of Illinois course notes (2012), cited in K. Anders, *Counting Non-Standard Binary Representations*, *Journal of Integer Sequences* 19 (2016). Not fully accessible in this investigation.
