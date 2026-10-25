# Reentrant zero-free phase for doubly jet-penalized Bergman kernels

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and let \(\sigma,\tau\ge0\) be finite. The analytic Bergman space equipped with the norm
\[
\|f\|_{\sigma,\tau}^{2}=\frac1\pi\int_{\mathbb D}|f(z)|^2\,dA(z)+\sigma|f(0)|^2+\tau|f'(0)|^2
\]
has reproducing kernel
\[
K_{\sigma,\tau}(z,w)=\frac1{(1-z\overline w)^2}-a-bz\overline w,\qquad a=\frac{\sigma}{1+\sigma},\quad b=\frac{4\tau}{1+2\tau}.
\]
Write \(A=1-4a+4b\) and \(E=1-a-2b\). For every \(0\le a<1\), \(0\le b<2\), the exact number \(N(a,b)\) of scalar zeros in \(|t|<1\), counted with multiplicity, is
\[
N(a,b)=\begin{cases}
1,&A<0,\\
0,&A=0,\ a\le\tfrac12,\\
1,&A=0,\ a>\tfrac12,\\
0,&A>0,\ E\ge0,\\
2,&A>0,\ E<0.
\end{cases}
\]
Every \(|t|<1\) is realized by some \(t=z\overline w\) with \(z,w\in\mathbb D\). Thus zero-freeness on \(\mathbb D\times\mathbb D\) is equivalent to \(N=0\).

In particular, for each \(\tfrac14<a<\tfrac12\), the family exhibits a *reentrant zero-free interval*: initially one zero for \(0\le b<a-\tfrac14\), none for \(a-\tfrac14\le b\le(1-a)/2\), and two for \(b>(1-a)/2\). The endpoints are included in the zero-free interval, because their zeros lie on \(|t|=1\), not inside.

## Assumptions and scope
All parameters are real, finite, and nonnegative in the displayed norm. Monomials are orthogonal because the extra functionals select the constant and linear Taylor coefficients. The count concerns zeros in the scalar product \(t=z\overline w\), not their continuously many representations as pairs of disk points. Multiplicities are counted in this scalar variable; the zero-free statement requires no multiplicity convention.

## Proof
For \(f(z)=\sum_{n\ge0}c_nz^n\), the exact norm is
\[
\|f\|_{\sigma,\tau}^2=(1+\sigma)|c_0|^2+(\tfrac12+\tau)|c_1|^2+\sum_{n\ge2}\frac{|c_n|^2}{n+1}.
\]
Thus the monomial reproducing series has coefficients \((1+\sigma)^{-1}\), \((\tfrac12+\tau)^{-1}\), and \(n+1\) for \(n\ge2\), giving the stated kernel. Since \(|t|<1\), multiplication by \((1-t)^2\) does not introduce or remove zeros. Its numerator is
\[
P(t)=1-(a+bt)(1-t)^2
=1-a+(2a-b)t+(2b-a)t^2-bt^3.
\]
Use the Möbius transformation \(w=(1-t)/(1+t)\), which maps \(|t|<1\) conformally onto \(\operatorname{Re}w>0\). After clearing denominators,
\[
Q(w)=(1+w)^3P\!\left(\frac{1-w}{1+w}\right)
=Aw^3+Bw^2+3w+1,
\quad A=1-4a+4b,\quad B=3-4a-4b.
\]
Zeros of \(P\) inside the disk correspond bijectively, with multiplicity, to finite zeros of \(Q\) in the right half-plane. (When \(b=0\), the reduction also has an extraneous root at \(w=-1\), safely in the *left* half-plane.)

For a real cubic \(Aw^3+Bw^2+3w+1\) with \(A B\ne0\), and no imaginary-axis roots, the Routh array has first column
\[
A,\qquad B,\qquad \frac{3B-A}{B}=\frac{8E}{B},\qquad1.
\]
The number of right-half-plane zeros is the number of sign changes. If \(A<0\), then \(B>0\) forces \(E>0\), producing signs \((- + + +)\); if \(B<0\), either sign of \(E\) produces exactly one change in \((- - \operatorname{sgn}(E)+)\). Hence \(N=1\) whenever \(A<0\) away from zero-array entries. If \(A>0\) and \(E>0\), then \(B>0\): indeed, from \(a<b+\tfrac14\) and \(a+2b<1\), one obtains \(a+b<\tfrac34\) by considering \(b\le\tfrac14\) and \(b>\tfrac14\) separately. Thus all signs are positive and \(N=0\). If \(A>0\) and \(E<0\), either sign of \(B\) yields two changes, so \(N=2\).

Boundary values follow from exact factorization rather than a generic-position argument. If \(A=0\), then \(b=a-\tfrac14\) and
\[
Q(w)=(4-8a)w^2+3w+1.
\]
For \(a<\tfrac12\), both roots have negative real part; at \(a=\tfrac12\), this becomes \(3w+1\); for \(a>\tfrac12\), its roots have opposite real signs. Thus the three \(A=0\) cases have counts zero, zero, and one. If \(E=0\), so \(a=1-2b\), there is the identity
\[
Q(w)=(3w+1)\bigl((4b-1)w^2+1\bigr).
\]
For \(A>0\), necessarily \(b>\tfrac14\), and the quadratic roots are purely imaginary, giving \(N=0\). For \(A<0\), the roots of the quadratic are one positive and one negative real, leaving \(N=1\). At \(A=E=0\) the numerator factors as \(P(t)=-(t-2)(t+1)^2/4\), so both boundary zeros are excluded. At \(B=0\), the expression \(E=-A/8\) holds; there are no imaginary-axis zeros, and the asserted counts follow continuously from adjacent \(B\ne0\) parameters. This covers every parameter including \(b=0\).

For reentrance, fix \(\tfrac14<a<\tfrac12\). Then \(A=0\) occurs at \(b=a-\tfrac14\), whereas \(E=0\) occurs at \(b=(1-a)/2\), and the first threshold is strictly smaller. Applying the verified count in the resulting three regions gives the exact progression \(1\to0\to2\). These intervals lie inside \(0\le b<2\), so both threshold phenomena are realized by finite physical penalties.

## Verification
The attached `verify.py` independently expands the Cayley-transformed numerator and transition factorizations in exact symbolic algebra, then checks the formula against deterministic numerical cubic-root counts for 12,000 parameter pairs and designated endpoint cases. All tests passed. The numerical census does not establish the universal result; the analytic Routh count and separate boundary factorizations do.

## Relationship to prior work
Zeytuncu, arXiv:1009.2806v1 (2010), establishes that changing a *radial area weight* can create Bergman-kernel zeros and discusses the classical Lu Qi-Keng question. Jacobson, arXiv:1309.4800v1 (2013), gives weighted Bergman formulas for weights arising from squared meromorphic functions and examines zeros. Neither changes the Hilbert norm by two independently tunable point-supported Taylor-jet penalties, and neither contains the above two-dimensional phase diagram.

The published first-order Bergman **jet Gram kernel** result concerns kernels of the functionals \(f\mapsto c_0f(z)+c_1f'(z)\) *at varying points*. This is not the reproducing kernel of the **new Hilbert norm** that penalizes \(f(0)\) and \(f'(0)\); its zero-free dichotomy does not imply this theorem. The single-derivative-norm perturbation is a one-parameter section \(a=0\) of this problem and cannot determine the reentrant regime with \(a>\tfrac14\).

## Limitations
Only the unit disk, the classical area Bergman norm, two jets at the origin, and finite nonnegative penalties are covered. The result neither identifies zeros explicitly nor asserts a corresponding classification for general radial weights, off-origin jets, higher-order penalties, or other domains. Some complex roots may coalesce; the count is with multiplicity. This is an analytic same-source classification, not independent verification or evidence of absolute priority over unindexed literature.

## References
1. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806v1 (2010), Sections 1–2. https://arxiv.org/abs/1009.2806
2. R. Jacobson, *Weighted Bergman Kernel Functions Associated to Meromorphic Functions*, arXiv:1309.4800v1 (2013), Sections 1, 2, and 4. https://arxiv.org/abs/1309.4800
3. N. Aronszajn, *Theory of Reproducing Kernels*, Trans. Amer. Math. Soc. 68 (1950), 337–404, for the RKHS framework.
