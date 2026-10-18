# Frobenius-sharp \(q\)-numerical radii of three-site nilpotent shifts

## Finding
For complex numbers \(a,b\), put
\[
T_{a,b}=\begin{pmatrix}0&a&0\\0&0&b\\0&0&0\end{pmatrix}
\quad\text{on }\mathbb C^3,
\qquad |a|^2+|b|^2=1.
\]
For \(0\le q\le1\), its \(q\)-numerical radius is
\[
w_q(T)=\max\left\{|\langle Tx,y\rangle|:\|x\|_2=\|y\|_2=1,\ \langle x,y\rangle=q\right\}.
\]
The Hermitian inner product is taken linear in the first variable; changing the convention makes no difference here. For \(0\le q<1\), the following sharp, simultaneously attained bounds hold:
\[
\boxed{\quad L(q)\le w_q(T_{a,b})\le U(q):=\frac{1+\sqrt{1-q^2}}2.\quad}
\]
The **upper bound** is attained exactly when one weight vanishes. The **lower bound** is attained exactly when \(|a|=|b|=1/\sqrt2\). More strongly, at every fixed \(q<1\), \(w_q(T_{a,b})\) is a strictly decreasing function of the invariant \(\pi=|ab|^2\) on \([0,1/4]\). All phases of the nonzero weights are immaterial.

The exact lower profile is
\[
\boxed{\quad L(q)=\frac1{\sqrt2}\quad(0\le q\le\tfrac12),\quad}
\]
and for \(\tfrac12<q<1\), \(L(q)=s(t_q)-qt_q\), where \(s(t)=\sqrt{z_+(t)}\), \(z_+(t)\) is the **largest real root** of
\[
z^3-(3t^2+1)z^2+(3t^4+t^2+\tfrac14)z-t^6=0,
\]
and \(t_q>0\) is the **unique** solution of \(s'(t_q)=q\). These statements give a finite algebraic/one-dimensional characterization rather than merely numerical estimates. At the endpoint \(q=1\), the inequalities coalesce:
\[
\boxed{\ w_1(T_{a,b})=\frac12\ \text{for every admissible }(a,b).\ }
\]
In particular, the balanced minimizer has a genuine \(q\)-plateau through \(1/2\), whereas each unbalanced profile begins decreasing immediately above \(q=0\). As a concrete instance,
\[
L(0.8)=0.6733109129\ldots <U(0.8)=0.8.
\]

## Assumptions and scope
All spaces, matrices, and inner products are complex Hilbertian. The energy constraint is the Frobenius normalization \(\operatorname{tr}(T^*T)=1\). The weights may be zero or non-real. The constrained overlap \(q\) is real in \([0,1]\); complex overlaps have the same radius after replacing \(q\) by its modulus. The assertion concerns **all** such three-coordinate one-step nilpotent shifts, not arbitrary nilpotent matrices. The published motivating operator-theoretic parameter is the scaled \(q\)-numerical range \(W_q(T)/q\) for \(q>0\); the sharp disk radii for this normalized class are obtained by dividing the displayed constants by \(q\).

## Proof
**1. Circularity and a norm-envelope identity.** By a diagonal unitary change of basis, suppose \(a,b\ge0\). The diagonal unitary \(D_\theta=\operatorname{diag}(1,e^{i\theta},e^{2i\theta})\) satisfies \(D_\theta^*TD_\theta=e^{i\theta}T\). Consequently the constrained numerical range is invariant under rotation. Its maximal real part therefore equals the maximal absolute value.

Put \(F(t)=\|T+tI\|\) for \(t\ge0\). For any admissible \(x,y\),
\[
\operatorname{Re}\langle Tx,y\rangle
=\operatorname{Re}\langle(T+tI)x,y\rangle-tq\le F(t)-tq.
\]
We prove this upper envelope is exact:
\[
\boxed{\qquad w_q(T)=\min_{t\ge0}\{F(t)-qt\}\quad(0\le q<1).\qquad}\tag{1}
\]
Indeed, \(F(t)\ge t\), so \(F(t)-qt\to\infty\) as \(t\to\infty\) when \(q<1\); a minimizer exists. The function \(F\) is **strictly convex**: otherwise equality in its operator-norm convexity inequality at two distinct scalar shifts would produce a common norming unit vector \(v\) for both shifts whose images \((T+t_1I)v\) and \((T+t_2I)v\) are positively collinear. Their difference is a nonzero multiple of \(v\), so \(Tv\) would be a scalar multiple of \(v\). Nilpotency forces \(Tv=0\), contradicting \(F(t_i)>t_i\). The latter strict inequality holds because the numerical range of \(T\) is a centered disk of radius \(1/2\), and hence \(F(t)\ge w_1(T+tI)=t+1/2\).

For \(t>0\), the top singular value \(F(t)\) of the nonnegative upper-bidiagonal matrix \(T+tI\) is simple, including if one edge vanishes. Choose real, nonnegative top right and left singular vectors \(v,u\) with \((T+tI)v=F(t)u\). Standard singular-value differentiation gives
\[
F'(t)=\langle v,u\rangle\in(0,1).
\]
As \(t\to\infty\), \(F'(t)\to1\): for instance \(F(t)=t+1/2+O(t^{-1})\), and convexity gives the derivative limit. At the origin, if \(a\ne b\), the top singular value of \(T\) is simple, with mutually orthogonal top left and right singular vectors, so \(F'(0+)=0\). If \(a=b=1/\sqrt2\), the top singular value is double and its largest first-order splitting coefficient is \(1/2\): top right singular vectors are \((0,c,s)\), top left singular vectors are \((c,s,0)\), and their maximal overlap is \(cs=1/2\). Equivalently \(F'(0+)=1/2\).

For \(q>F'(0+)\), strict convexity and the derivative limit give a unique minimizing \(t_q>0\) with \(F'(t_q)=q\). Its top singular vectors satisfy \(\langle v,u\rangle=q\) and
\[
\langle Tv,u\rangle=F(t_q)-qt_q,
\]
so they realize the upper bound in (1). For \(0\le q\le F'(0+)\), the minimum is at \(t=0\). When \(a=b\), its top singular pairs \(v=(0,\cos\phi,\sin\phi)\), \(u=(\cos\phi,\sin\phi,0)\) give every overlap \(q=\sin\phi\cos\phi\in[0,1/2]\) and attain \(F(0)\). When \(a\ne b\), the only such overlap is \(q=0\), attained by the top singular pair of \(T\). This proves (1) in all cases.

**2. A single energy-allocation invariant.** Set \(\pi=a^2b^2\) and let \(z\) denote squared singular value. Direct determinant expansion gives the exact characteristic polynomial
\[
P_{t,\pi}(z)
=\det\!\left(zI-(T+tI)^*(T+tI)\right)
=z^3-(3t^2+1)z^2+(3t^4+t^2+\pi)z-t^6.
\tag{2}
\]
Thus \(F_\pi(t)\) depends on the weights only through \(\pi\). For \(t>0\) the largest root \(z_+(t,\pi)>0\) is simple, and at that root \(\partial_zP_{t,\pi}(z_+)>0\). Therefore, whenever \(0<\pi<1/4\),
\[
\frac{\partial z_+}{\partial\pi}
=-\frac{z_+}{\partial_zP_{t,\pi}(z_+)}<0.
\tag{3}
\]
Continuity treats both boundary values of \(\pi\). At \(t=0\),
\[
F_\pi(0)=\max(a,b)
=\sqrt{\frac{1+\sqrt{1-4\pi}}2},
\]
which is also strictly decreasing on \([0,1/4]\). Therefore \(F_{\pi_1}(t)>F_{\pi_2}(t)\) for every finite \(t\ge0\) whenever \(\pi_1<\pi_2\).

To transfer the strict inequality through the infimum, let \(t_1\) be a minimizer in (1) for \(\pi_1\), which is finite for \(q<1\). Then
\[
w_q(\pi_2)
\le F_{\pi_2}(t_1)-qt_1
< F_{\pi_1}(t_1)-qt_1=w_q(\pi_1).
\]
This proves strict monotonicity at every \(q<1\). Since \(\pi\in[0,1/4]\), the maximum is exactly the rank-one endpoint \(\pi=0\), and the minimum is exactly \(\pi=1/4\), or \(a=b=1/\sqrt2\), with the equality cases stated in the theorem.

**3. The two sharp profiles and the plateau.** At \(\pi=0\), \(T\) is a two-dimensional square-zero rank-one operator plus a zero block. Its shifted norm is exactly
\[
F_0(t)=\frac{1+\sqrt{1+4t^2}}2.
\]
Minimizing \(F_0(t)-qt\) gives \(U(q)=(1+\sqrt{1-q^2})/2\) for \(0\le q<1\).

At \(\pi=1/4\), formula (2) gives the cubic in the Finding. The first-order splitting calculation in Step 1 yields \(F_{1/4}'(0+)=1/2\). Hence its norm envelope remains constant at \(F_{1/4}(0)=1/\sqrt2\) precisely for \(0\le q\le1/2\). For each \(q\in(1/2,1)\), the strict convexity and smoothness of \(F_{1/4}\) on \((0,\infty)\) give a unique positive \(t_q\) with \(F_{1/4}'(t_q)=q\). This establishes the stated exact lower profile. The derivative can be evaluated without numerical differentiation using
\[
F_{1/4}'(t)
=\frac{6tz_+^2-(12t^3+2t)z_++6t^5}
{2\sqrt{z_+}\bigl(3z_+^2-2(3t^2+1)z_++3t^4+t^2+1/4\bigr)},\qquad t>0.
\]

**4. Hilbert endpoint.** The Hermitian part \((T+T^*)/2\) has spectrum \(\{-1/2,0,1/2\}\) under the energy constraint. The circularity of \(T\) makes its ordinary numerical radius \(w_1(T)=1/2\), independent of \(\pi\). This is why strict allocation rigidity ceases exactly at \(q=1\).

## Verification
The companion standalone `CHECK.py` performs exact integer-arithmetic checks of (2), independently evaluates singular-value envelopes, tests the two extrema across sampled energy allocations, checks the phase boundary and endpoint, and constructs finite singular-vector witnesses for interior parameters. It reports 1,645 passed diagnostic assertions in the included run. These finite tests are reproducibility diagnostics, **not** an exhaustive or independent proof of the universal theorem; all quantifiers above are discharged by Steps 1–4.

## Relationship to prior work
Kaunisto, O'Loughlin, and Virtanen (arXiv:2610.00443, first public September 30, 2026) prove a general dilation and complete-spectral-set theorem for **scaled** \(q\)-numerical ranges. Their Remark 2.4 explicitly computes the rank-one nilpotent radius \(U(q)\), which is used here as an endpoint; the new claim is **not** ownership of that previously known formula. Their proof does not address sharp two-edge energy-allocation extremizers.

The 2008 full-text study of Koide and Nakazato determines boundaries for a specific upper-triangular matrix with a nonzero second-superdiagonal term, distinct from the one-step nilpotent shifts here. The 2010 work of Chien and Nakazato studies a particular **two-sided** three-by-three tridiagonal family; its abstract does not state a Frobenius-normalized two-edge minimax theorem, but its entire text was not retrieved and remains a priority risk. Chien and Nakazato's 2013 cubic-surface study supplies broad algebraic geometry of \(q\)-numerical ranges; the full text was likewise unavailable in the checks performed. Independently known unscaled/spatial \(\ell_p\) weighted-shift radii and unweighted-Jordan \(q\)-radius results do not by their displayed statements imply the strict **two-parameter allocation monotonicity** asserted here. Any older equivalent extremization theorem under algebraic-pencil terminology would supersede this originality assessment.

## Limitations
The results are confined to three-by-three **one-step nilpotent** shifts and a fixed Frobenius normalization. The claim does not extend the ordering to larger shifts, general three-by-three nilpotents with a second-superdiagonal entry, or arbitrary nonnilpotent operators. The root/derivative prescription is an exact implicit characterization, not an elementary closed radical for the entire lower profile. No independent expert audit or independent priority search was performed. Inaccessible complete texts of plausible older general \(q\)-numerical-range papers leave publication-priority risk.

## References
1. M. Kaunisto, R. O'Loughlin, J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, arXiv:2610.00443 (v1 September 30, 2026), https://arxiv.org/html/2610.00443v2.
2. R. Koide, H. Nakazato, *The \(q\)-Numerical Range of a Certain \(3\times3\) Matrix*, International Mathematical Forum **3** (2008), 1001–1010, https://www.m-hikari.com/imf-password2008/21-24-2008/nakazatoIMF21-24-2008.pdf.
3. M.-T. Chien, H. Nakazato, *The \(q\)-numerical range of \(3\times3\) tridiagonal matrices*, Electronic Journal of Linear Algebra **20** (2010), 376–390, https://doi.org/10.13001/1081-3810.1382.
4. M.-T. Chien, H. Nakazato, *Cubic surfaces and \(q\)-numerical ranges*, Mathematical Communications **18** (2013), 133–141, https://hrcak.srce.hr/101406.
5. D. Denčić, H. Stanković, M. Krstić, I. Damnjanović, *\(q\)-numerical radius of rank-one operators and the generalized Buzano inequality*, arXiv:2503.05036 (2025), https://arxiv.org/abs/2503.05036.
