# A generalized Kanter inequality for the modified-Bessel family \(\Phi_\nu\)

**Publication date:** 2026-09-21 (UTC)

## Statement

For \(\nu\ge -\tfrac12\) and \(x>0\), define
\[
\Phi_\nu(x)=e^{-x}x^{-\nu}\bigl(I_\nu(x)+I_{\nu+1}(x)\bigr),
\]
where \(I_\nu\) is the modified Bessel function of the first kind.

Then for every \(r\ge0\),
\[
\boxed{
\Phi_\nu(2r)\ge
\frac{\Gamma(r+\tfrac12)}
{\sqrt{\pi}\,2^\nu\,\Gamma(r+\nu+1)}.
}
\]

The equality cases are sharp:

- if \(r=0\), equality holds for every \(\nu\ge-\tfrac12\);
- if \(\nu=-\tfrac12\), equality holds for every \(r\ge0\);
- if \(r>0\) and \(\nu>-\tfrac12\), the inequality is strict.

At \(\nu=0\), the duplication formula turns the right-hand side into
\[
\frac{\Gamma(2r+1)}{\Gamma(r+1)^2}2^{-2r},
\]
so the theorem reduces exactly to the real-variable extension of Kanter's inequality.

Equivalently,
\[
e^{-2r}\bigl(I_\nu(2r)+I_{\nu+1}(2r)\bigr)
\ge
\frac{r^\nu\Gamma(r+\tfrac12)}
{\sqrt{\pi}\,\Gamma(r+\nu+1)}.
\]

Using
\[
\Phi_\nu(y)=\frac{2^{-\nu}}{\Gamma(\nu+1)}
\,{}_1F_1\!\left(\nu+\tfrac12;2\nu+2;-2y\right),
\]
one also obtains the Kummer-function form
\[
{}_1F_1\!\left(\nu+\tfrac12;2\nu+2;-4r\right)
\ge
\frac{\Gamma(\nu+1)\Gamma(r+\tfrac12)}
{\sqrt{\pi}\,\Gamma(r+\nu+1)}.
\]

## Context

Baricz and Pogány introduced \(\Phi_\nu\) as an order-parameter extension of the function
\[
\Phi(x)=e^{-x}(I_0(x)+I_1(x))
\]
appearing in Kanter's concentration inequality. Their 2014 paper proves several monotonicity, convexity, Turán-type and two-sided estimates for \(\Phi_\nu\), proves Kanter's inequality for all real \(r\ge0\) in the case \(\nu=0\), and ends with the explicit open problem of finding a generalization of Kanter's inequality for \(\Phi_\nu\).

The bound above supplies such a generalization with the same gamma-ratio structure, exact recovery of \(\nu=0\), equality at the full boundary order \(\nu=-\tfrac12\), and asymptotic sharpness as \(r\to\infty\).

## Proof

The endpoint \(\nu=-\tfrac12\) is immediate from
\[
I_{-1/2}(x)=\sqrt{\frac{2}{\pi x}}\cosh x,
\qquad
I_{1/2}(x)=\sqrt{\frac{2}{\pi x}}\sinh x,
\]
which give
\[
\Phi_{-1/2}(x)=\sqrt{\frac2\pi}.
\]
This is exactly the proposed right-hand side at \(\nu=-\tfrac12\).

Now assume \(\nu>-\tfrac12\), and set
\[
a=\nu+\frac12>0.
\]
Baricz and Pogány's integral representation is
\[
\sqrt{\pi}\,2^\nu\Gamma(a)\Phi_\nu(x)
=
\int_{-1}^1
(1-t)(1-t^2)^{a-1}e^{-x(1+t)}\,dt.
\]
At \(x=2r\), multiplication of the desired inequality by
\(\sqrt{\pi}\,2^\nu\Gamma(a)\) shows that it is equivalent to
\[
\int_{-1}^1
(1-t)(1-t^2)^{a-1}e^{-2r(1+t)}\,dt
\ge
B\!\left(a,r+\frac12\right).
\]
The beta term has the matching integral representation
\[
B\!\left(a,r+\frac12\right)
=
\int_{-1}^1
(1-t)(1-t^2)^{a-1}|t|^{2r}\,dt,
\]
because the odd part integrates to zero.

For \(r>0\), pair the contributions at \(t=x\) and \(t=-x\), \(0<x<1\), and define
\[
b_r(x)
=
(1+x)e^{-2r(1-x)}
+(1-x)e^{-2r(1+x)}
-2x^{2r}.
\]
The required difference is therefore
\[
D_a(r)=\int_0^1(1-x^2)^{a-1}b_r(x)\,dx.
\]

### A single sign change

Put \(k=2r\) and
\[
H_r(x)=
e^{-k}\frac{\cosh(kx)+x\sinh(kx)}{x^k}.
\]
Then
\[
b_r(x)=2x^k\bigl(H_r(x)-1\bigr).
\]
A direct differentiation gives
\[
\operatorname{sgn} H_r'(x)
=
\operatorname{sgn}
\left[x\tanh(kx)-k(1-x^2)\right].
\]
The expression in brackets is strictly increasing, since its derivative is
\[
\tanh(kx)+kx\,\operatorname{sech}^2(kx)+2kx>0.
\]
It is negative at \(x=0\) and positive at \(x=1\). Hence \(H_r\) first decreases and then increases. Moreover,
\[
H_r(x)\to\infty\quad(x\downarrow0),
\qquad
H_r(1)=1.
\]
Consequently there is a unique \(c_r\in(0,1)\) such that
\[
b_r(x)>0\quad(0<x<c_r),
\qquad
b_r(x)<0\quad(c_r<x<1).
\]

### The boundary-weight integral is positive

The integral
\[
D_0(r):=\int_0^1\frac{b_r(x)}{1-x^2}\,dx
\]
converges. Splitting the two denominators gives
\[
D_0(r)
=
\int_0^1
\frac{e^{-k(1-x)}-x^k}{1-x}\,dx
+
\int_0^1
\frac{e^{-k(1+x)}-x^k}{1+x}\,dx.
\]
Using the standard integral identities for the digamma function and the exponential integral, followed by the digamma duplication formula, this simplifies to
\[
D_0(r)
=
F(r):=
\psi\!\left(r+\frac12\right)-\log r+\operatorname{Ei}(-4r).
\]

We show \(F(r)>0\) for every \(r>0\). Differentiating and using the Laplace representation of the trigamma function,
\[
F'(r)
=
\psi_1\!\left(r+\frac12\right)
-\frac{1-e^{-4r}}r
=
\int_0^\infty e^{-rt}q(t)\,dt,
\]
where
\[
q(t)=
\begin{cases}
\dfrac{t}{2\sinh(t/2)}-1,&0<t<4,\\[2mm]
\dfrac{t}{2\sinh(t/2)},&t>4.
\end{cases}
\]
Thus \(q<0\) on \((0,4)\) and \(q>0\) on \((4,\infty)\).

This one-sign-change structure implies that \(F'\) can change sign at most once, from positive to negative. Indeed, if \(F'(s)\le0\) and \(r>s\), multiply the integrand defining \(F'(s)\) by the strictly decreasing factor \(e^{-(r-s)t}\). On the negative part \(t<4\) this factor is at least its value at \(4\), while on the positive part \(t>4\) it is at most that value; hence \(F'(r)<0\).

At the left endpoint,
\[
F(0+)=0,
\qquad
F'(0+)=\frac{\pi^2}{2}-4>0.
\]
At infinity, the standard asymptotics of \(\psi\) and \(\operatorname{Ei}\) give
\[
F(r)\to0.
\]
Therefore \(F\) initially increases, can turn only once, and after turning decreases to \(0\). Hence
\[
D_0(r)=F(r)>0
\qquad(r>0).
\]

### All orders \(\nu>-\tfrac12\)

Write
\[
f_r(x)=\frac{b_r(x)}{1-x^2},
\qquad
w_a(x)=(1-x^2)^a.
\]
Then
\[
D_a(r)=\int_0^1 f_r(x)w_a(x)\,dx.
\]
The function \(f_r\) has the same single sign change as \(b_r\): positive before \(c_r\), negative after \(c_r\). Since \(w_a\) is strictly decreasing,
\[
\begin{aligned}
D_a(r)
&=
\int_0^{c_r}f_r(x)w_a(x)\,dx
+\int_{c_r}^1f_r(x)w_a(x)\,dx\\
&\ge
w_a(c_r)\int_0^1 f_r(x)\,dx\\
&=
w_a(c_r)D_0(r)>0.
\end{aligned}
\]
Thus the desired inequality is strict whenever \(r>0\) and \(a>0\), i.e. whenever \(r>0\) and \(\nu>-\tfrac12\).

Finally, when \(r=0\),
\[
\Phi_\nu(0+)=\frac1{2^\nu\Gamma(\nu+1)},
\]
which equals the proposed right-hand side. This completes the proof and the equality classification.

## Sharpness

The right-hand side is sharp at both natural boundaries. Besides the exact equality cases above, the standard large-\(x\) asymptotic for \(I_\nu\) and the gamma-ratio asymptotic give
\[
\Phi_\nu(2r)
\sim
\frac{1}{\sqrt{\pi}\,2^\nu}\,r^{-\nu-1/2}
\sim
\frac{\Gamma(r+\tfrac12)}
{\sqrt{\pi}\,2^\nu\,\Gamma(r+\nu+1)}
\qquad(r\to\infty).
\]
Thus the multiplicative constant cannot be improved.

## Literature status and originality

The 2014 Baricz–Pogány paper explicitly asks for a generalization of Kanter's inequality for \(\Phi_\nu\). Targeted searches were made for the exact \(\Phi_\nu\) family, the source title and DOI, "generalization of Kanter's inequality", the Bessel form above, the gamma ratio
\(\Gamma(r+\tfrac12)/\Gamma(r+\nu+1)\), and the equivalent Kummer-function form.

A 2026 paper by Veestraeten revisits sums of \(I_\nu\), explicitly cites Baricz–Pogány, and rewrites \(\Phi_\nu\) in confluent-hypergeometric form. Its accessible text was also checked as a current-status source. No statement equivalent to the gamma-ratio lower bound above was located in those searches.

Accordingly, originality is claimed only **to the best of our knowledge**. The main residual risk is that an equivalent inequality may occur in the extensive literature on Kummer functions, beta-integral inequalities, or modified-Bessel bounds under different notation.

## Reproducibility

`artifacts/verify_numeric.py` numerically checks the inequality on representative values of \((\nu,r)\) and independently checks the identity
\[
\int_0^1\frac{b_r(x)}{1-x^2}\,dx
=
\psi\!\left(r+\frac12\right)-\log r+\operatorname{Ei}(-4r).
\]
The numerical checks are supplementary and are not used in place of the analytic proof.

## Limitations

- The theorem gives a sharp Kanter-type lower bound for this specific \(\Phi_\nu\) family; it does not classify all sharp lower bounds for \(I_\nu+I_{\nu+1}\).
- The single-crossing and digamma/exponential-integral ingredients are analytic tools, not independent claims of novelty.
- The originality search is targeted rather than exhaustive; equivalent prior coverage under substantially different special-function notation remains possible.


## References

1. Á. Baricz and T. K. Pogány, *On a sum of modified Bessel functions*, Mediterranean Journal of Mathematics **11** (2014), 349–360. https://doi.org/10.1007/s00009-013-0365-y ; https://arxiv.org/abs/1301.5429
2. L. Mattner and B. Roos, *A shorter proof of Kanter's Bessel function concentration bound*, Probability Theory and Related Fields **139** (2007), 191–205. https://doi.org/10.1007/s00440-006-0043-0 ; https://arxiv.org/abs/math/0603522
3. M. Kanter, *Probability inequalities for convex sets and multidimensional concentration functions*, Journal of Multivariate Analysis **6** (1976), 222–236. https://www.sciencedirect.com/science/article/pii/0047259X76900324
4. D. Veestraeten, *On Finite and Infinite Sums of the Modified Bessel Function of the First Kind*, Mediterranean Journal of Mathematics **23** (2026). https://doi.org/10.1007/s00009-026-03050-1
5. NIST Digital Library of Mathematical Functions, chapters on gamma/polygamma, exponential integrals, and modified Bessel functions. https://dlmf.nist.gov/
