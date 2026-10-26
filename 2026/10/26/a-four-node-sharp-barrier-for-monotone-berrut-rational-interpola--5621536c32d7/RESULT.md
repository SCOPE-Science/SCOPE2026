# A four-node sharp barrier for monotone Berrut rational interpolation

## Finding

Let \(n\ge1\) be any integer and let \(0\le y_0\le\cdots\le y_n\le1\). At the equidistant nodes \(x_j=j/n\), define Berrut's alternating-weight rational interpolant
\[
 R_{n,y}(x)=\frac{\sum_{j=0}^n(-1)^j y_j/(x-x_j)}{\sum_{j=0}^n(-1)^j/(x-x_j)}\quad(x\ne x_j),\qquad R_{n,y}(x_j)=y_j.
\]
For every \(x\in[0,1]\) and every \(n\),
\[
 \boxed{-\delta_*\le R_{n,y}(x)\le1+\delta_*},\qquad
 12\delta_*^4+24\delta_*^3+32\delta_*^2-6\delta_*-1=0,
\]
where \(\delta_*=0.255032152490845\ldots\) is the **unique positive root**. Both endpoints of this universal range are attained already for \(n=3\) (four equally spaced nodes). Thus the worst bounded-monotone range defect is independent of the number of nodes and is completely realized by four-node step data.

For arbitrary \(L\le y_j\le U\) with nondecreasing samples, affine rescaling gives the sharp range \([L-\delta_*(U-L),\ U+\delta_*(U-L)]\).

## Assumptions and scope

Only the original weights \((-1)^j\), equal spacing, pointwise interpolation and nondecreasing real data are assumed. No regularity of an underlying function is required. The result is a sharp **range** bound, not a monotonicity-preservation theorem and not an unrestricted Lebesgue-norm estimate. For decreasing data, replace \(y_j\) with \(-y_j\) and transform the interval appropriately. All formulae at interpolation nodes mean continuous limits.

## Proof

**1. A denominator with two alternating tails.** Fix an open node interval, write \(nx=m+t\), \(0\le m\le n-1\), \(0<t<1\), and put \(r=n-m-1\). Multiplying all barycentric numerator/denominator terms by the common sign \((-1)^m\), define
\[
 w_j=\frac{(-1)^{j-m}}{m+t-j},\quad
 a=\sum_{\ell=1}^{m}\frac{(-1)^{\ell+1}}{t+\ell},\quad
 b=\sum_{\ell=1}^{r}\frac{(-1)^{\ell+1}}{1-t+\ell},\quad
 u=\frac1t+\frac1{1-t}.
\]
Empty sums are zero. The signed tail to the left of index \(m\) is \(-a\), and the signed tail to the right of index \(m+1\) is \(-b\). The two central weights are \(1/t\) and \(1/(1-t)\). Consequently
\[
 D=\sum_{j=0}^{n}w_j=u-a-b.
\]
Alternating-series estimates give \(0\le a\le\alpha=1/(1+t)\) and \(0\le b\le\beta=1/(2-t)\). Equality \(a=\alpha>0\) requires \(m=1\), and equality \(b=\beta>0\) requires \(r=1\). As \(u\ge4\) and \(\alpha+\beta=3/((1+t)(2-t))\le3/2\), we have \(D>5/2\), so there is no real pole in any open node interval.

**2. Sharp control over step data.** Define the suffix (step-data) response
\[
 H_k=\frac{\sum_{j=k}^{n}w_j}{D},\qquad 1\le k\le n.
\]
We claim
\[
 -\frac bD\le H_k\le1+\frac aD.\tag{1}
\]
Here are the alternating-sign details. On the left, \(w_0,\ldots,w_{m-1}\) alternate and their magnitudes strictly increase toward the central cell; any initial partial sum whose last term is negative lies between \(-a\) and zero, because its omitted final pairs have strictly negative sum, whereas a positive initial partial sum has magnitude at most its last term, hence at most \(\alpha<1<D\). For \(k\le m\), write \(H_k=1-(\sum_{j<k}w_j)/D\), giving (1). At \(k=m+1\),
\[
 H_{m+1}=\frac{1/(1-t)-b}{D}=1+\frac{a-1/t}{D}\in(0,1).
\]
On the right, the suffix beginning at \(m+2\) has alternating signs and strictly decreasing magnitudes; every negative suffix is at least the full right-tail sum \(-b\), by pairing the omitted initial terms, and every positive suffix is smaller than its leading term, at most \(1/(3-t)<D\). This proves (1) for \(k\ge m+2\). When \(m\ge1\), equality at the upper local endpoint occurs for \(H_m=1+a/D\); when \(r\ge1\), equality at the lower local endpoint occurs for \(H_{m+2}=-b/D\).

Decompose monotone data into nonnegative jumps:
\[
 y_j=y_0+\sum_{k=1}^{n}(y_k-y_{k-1})\mathbf1_{\{j\ge k\}},\qquad
 R_{n,y}(x)=y_0+\sum_{k=1}^n(y_k-y_{k-1})H_k.
\]
Because the jump sum is \(y_n-y_0\le1-y_0\), (1) yields \(-b/D\le R_{n,y}(x)\le1+a/D\). Hence the largest possible violation at this cell position is exactly
\[
 \Delta_{n,m}(t)=\frac{\max\{a,b\}}{u-a-b},\tag{2}
\]
with the convention that zero tails contribute no defect. The local extrema are realized by step data at \(k=m\) or \(k=m+2\), as applicable.

**3. Uniform all-grid reduction.** The function \(\max(a,b)/(u-a-b)\) is nondecreasing separately in \(a\) and \(b\) for \(0\le a+b<u\). Replacing the alternating tails by their first-term upper bounds in (2) gives
\[
 \Delta_{n,m}(t)\le F(t):=\frac{\max\{(1+t)^{-1},(2-t)^{-1}\}}{t^{-1}+(1-t)^{-1}-(1+t)^{-1}-(2-t)^{-1}}.
\]
By reflection \(F(1-t)=F(t)\). On \(0<t\le1/2\), this simplifies to
\[
 F(t)=\frac{t(t-1)(t-2)}{2(t^2-t+1)},\qquad
 F'(t)=\frac{p(t)}{2(t^2-t+1)^2},\quad
 p(t)=t^4-2t^3+4t^2-6t+2.
\]
The derivative \(p'(t)=4t^3-6t^2+8t-6<0\) on \([0,1/2]\), while \(p(0)=2>0\) and \(p(1/2)=-3/16<0\). Thus there is a unique maximizer \(t_*=0.440458513317765\ldots\) and \(\delta_*=F(t_*)\). Eliminating \(t\) from \(p(t)=0\) and \(z=F(t)\) gives
\[
 \operatorname{Res}_t\bigl(p(t),2z(t^2-t+1)-t(t-1)(t-2)\bigr)
 =12\bigl(12z^4+24z^3+32z^2-6z-1\bigr).
\]
The polynomial inside parentheses has exactly one positive root by Descartes' rule of signs, and it changes sign between zero and one; this is \(\delta_*\).

**4. Equality.** In the middle cell of four nodes, \(n=3\), \(m=r=1\), so the two alternating tails each consist of their first term: \(a=\alpha\), \(b=\beta\). For \(t=t_*\), the step array \((0,1,1,1)\) at \(x=(1+t_*)/3\) produces \(R=1+\delta_*\). Reflection and complementation give the step array \((0,0,0,1)\) at \(x=(2-t_*)/3\) with value \(-\delta_*\). As at the nodes \(R(x_j)=y_j\in[0,1]\), these witnesses complete the global proof.

## Verification

The accompanying `verify.py` uses exact rational arithmetic for all step tails and all open cells for \(1\le n\le30\), at 34 rational positions per cell. It independently checks denominator identities, (1), local attainment, and the uniform envelope. Symbolic algebra checks the derivative and elimination identity; a separate floating-point check evaluates the two four-node extremizers and the positive algebraic root. **These finite checks are supplementary; the proof above covers every integer \(n\) and every real point.** Run `python verify.py` with Python 3.10 or later and SymPy installed.

## Relationship to prior work

Berrut's original 1988 scheme supplies the alternating barycentric weights. Baltensperger–Berrut–Noël (electronically published 19 February 1999) investigate convergence for specially arranged nodes, not this monotone range extremum. Bos–De Marchi–Hormann (2011) establish logarithmic growth of the **unrestricted** Lebesgue constant for the identical equispaced Berrut operator; their proof and formulas do not provide the present sharp monotone-restricted constant or four-node realization. Shape-preserving rational interpolation with deliberately selected weights and pole-free higher-order Floater–Hormann interpolation concern different operators or conditions. The denominator/tail method uses classical alternating-series estimates, but the all-grid sharp monotone envelope is a different optimization.

## Limitations

This does not assert that the rational interpolant itself is monotone. Equal spacing and unmodified Berrut weights are essential to the stated sharp constant; other nodal arrays/weights need separate analysis. The complete original 1988 source and a potentially relevant 2011 comonotone interpolation article were not available for exhaustive full-text comparison, so independently published equivalent bounds cannot be categorically excluded. A first-public date is recorded for the earliest examined source with explicit day-level public evidence (19 February 1999); the original scheme is known to date from 1988, but its exact earliest public day has not been established here.

## References

1. J.-P. Berrut, *Rational functions for guaranteed and experimentally well-conditioned global interpolation*, Computers & Mathematics with Applications 15 (1988), 1–16, DOI:10.1016/0898-1221(88)90067-3.
2. R. Baltensperger, J.-P. Berrut, and B. Noël, *Exponential convergence of a linear rational interpolant between transformed Chebyshev points*, Mathematics of Computation 68 (1999), 1109–1120; electronically published 19 February 1999, DOI:10.1090/S0025-5718-99-01070-4.
3. L. Bos, S. De Marchi, and K. Hormann, *On the Lebesgue constant of Berrut's rational interpolant at equidistant nodes*, Journal of Computational and Applied Mathematics 236 (2011), 504–510. Accessible author manuscript: https://www.inf.usi.ch/hormann/papers/Bos.2011.OTL.pdf.
4. T. N. T. Nguyen, A. Cuyt, and O. Salazar Celis, *Comonotone and cocovex rational interpolation and approximation*, Numerical Algorithms 58 (2011), 1–21, DOI:10.1007/s11075-010-9445-2.
5. M. S. Floater and K. Hormann, *Barycentric rational interpolation with no poles and high rates of approximation*, Numerische Mathematik 107 (2007), 315–331, DOI:10.1007/s00211-007-0093-y.
