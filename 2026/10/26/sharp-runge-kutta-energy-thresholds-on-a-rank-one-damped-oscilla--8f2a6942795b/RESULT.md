# Sharp Runge–Kutta energy thresholds on a rank-one damped oscillator

## Finding

For the canonical two-coordinate hypocoercive system \(u'(t)=Lu(t)\),
\[
L=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
\qquad R_p(h)=\sum_{j=0}^p\frac{(hL)^j}{j!},\quad p\in\{2,3,4\},
\]
the exact one-step Euclidean energy-safe step intervals are
\[
\boxed{\|R_2(h)\|_2\le1\iff 0\le h\le2,\qquad
\|R_3(h)\|_2\le1\iff 0\le h\le\alpha,\qquad
\|R_4(h)\|_2\le1\iff0\le h\le2.}
\]
Here \(\alpha=2.375701168186\ldots\) is the **unique positive real zero** of
\[
E(h)=h^5-3h^4+3h^3-6h^2+36h-72.
\]
Thus the third-order, three-stage truncation permits a strictly larger energy-safe step than both the second- and fourth-order methods, although the fourth-order truncation uses more stages. This is a sharp statement about Euclidean *one-step norm* contraction, not a claim that a lower-order method is uniformly more accurate.

A rational witness is \(h=9/4\). At this step \(R_3\) is strictly contractive, whereas \(R_4\) has a singular value greater than one, even though \(\rho(R_4)^2=1949353/4194304<1\). Hence asymptotic spectral stability does not guarantee monotone discrete energy on the same problem.

## Assumptions and scope

All matrices and steps are real and exact. The matrices \(R_p\) are precisely the stability-polynomial propagators of the \(p\)-stage explicit methods of order \(p\) on **linear autonomous** systems; in particular \(R_3\) is the SSPRK(3,3) polynomial and \(R_4\) is classical RK4. The assertion quantifies over every initial vector \(v\in\mathbb R^2\) and every real \(h\ge0\); nonexpansivity refers to \(\|R_p(h)v\|_2\le\|v\|_2\) for all such vectors.

The Hermitian part is \((L+L^{\mathsf T})/2=\operatorname{diag}(-1,0)\), and \(L\) has eigenvalues \((-1\pm i\sqrt3)/2\). The exact continuous energy derivative equals \(-2u_1(t)^2\le0\). Equality of energy at two distinct times would imply \(u_1\) vanishes throughout that interval, and then \(u'_1=-u_2\) forces \(u_2=0\). Hence \(\|e^{tL}\|_2<1\) for every \(t>0\). Since \(LL^{\mathsf T}\ne L^{\mathsf T}L\), scalar eigenvalue stability is not sufficient for the requested one-step Euclidean bound.

## Proof

Put \(B_p(h)=R_p(h)^{\mathsf T}R_p(h)-I\). For a real symmetric \(2\times2\) matrix, \(B_p\preceq0\) is equivalent to a nonpositive diagonal entry together with nonnegative determinant (with the degenerate case explicitly checked). Direct polynomial multiplication yields:

For \(p=2\),
\[
(B_2)_{22}=\frac{h^3(h-2)}2,\quad
(B_2)_{11}=\frac{h(h-2)(h^2-2h+4)}4,\quad
\det B_2=\frac{h^4(h-2)^2(h^2+4)}{16}.
\]
Both diagonal entries are negative and the determinant positive when \(0<h<2\). At \(h=2\), \(R_2=-I\), and for \(h>2\), \((B_2)_{22}>0\).

For \(p=3\), define
\[
C(h)=(h-1)^3-5,\qquad
G(h)=h^3-6h^2+18h-24,
\]
\[
F_3(h)=h^5-3h^3-24h^2+72h-72.
\]
The exact entries needed are
\[
(B_3)_{22}=\frac{h^3G(h)}{36},\qquad
(B_3)_{11}=\frac{hF_3(h)}{36},\qquad
\det B_3=\frac{h^4 C(h)E(h)}{1296}.
\]
First, for \(0\le h\le2\),
\[
E'(h)=h^2(5h^2-12h+9)+36-12h>0,
\]
where the quadratic is positive for all real \(h\); also \(E(2)=-16\). For \(h=2+t\), \(t\ge0\),
\[
E(2+t)=t^5+7t^4+19t^3+20t^2+32t-16.
\]
This is strictly increasing on \([0,\infty)\), from \(-16\) to infinity, so \(E\) has exactly one positive zero \(\alpha\). Since \(E(5/2)=251/32>0\), \(2<\alpha<5/2\). The unique zero of \(C\) is \(c=1+\sqrt[3]{5}>5/2\), and \(C<0\) below \(c\). Finally, \(G'(h)=3(h-2)^2+6>0\), while \(G(5/2)=-7/8\); hence \((B_3)_{22}<0\) on \((0,\alpha]\). The determinant is positive for \(0<h<\alpha\) and zero at \(h=\alpha\); thus \(B_3\preceq0\) precisely there. When \(\alpha<h<c\), \(\det B_3<0\), ruling out contraction. When \(h\ge c\), put \(t=h-2>1/2\):
\[
F_3(2+t)=t^5+10t^4+37t^3+38t^2+20t-16.
\]
It is strictly increasing for \(t\ge0\) and equals \(281/32>0\) at \(t=1/2\), so \((B_3)_{11}>0\) for all \(h\ge c\). This excludes all remaining steps.

For \(p=4\), define
\[
Q(h)=h^4-2h^3+48,
\qquad F_4(h)=h^7-4h^6+4h^5-96h^2+576h-1152,
\]
\[
P(h)=h^5-8h^3-48h^2+288h-384.
\]
Direct multiplication gives
\[
(B_4)_{22}=\frac{h^3P(h)}{576},\qquad
\det B_4=\frac{h^4(h-2)Q(h)F_4(h)}{331776}.
\]
The factor \(Q\) is positive: on \([0,2]\), \(Q(h)\ge48-2h^3\ge32\), while on \([2,\infty)\) it is at least \(48\). The other factor is
\[
F_4(h)=h^5(h-2)^2-96\bigl((h-3)^2+3\bigr).
\]
For \(0\le h\le2\), its first term is at most \(128\) while the subtracted term is at least \(384\). For \(2\le h\le3\), those bounds are \(243\) and \(288\), respectively. Therefore \(F_4(h)<0\) throughout \([0,3]\). With \(t=h-3\ge0\),
\[
F_4(3+t)=t^7+17t^6+121t^5+465t^4+1035t^3+1227t^2+891t-45,
\]
which increases strictly from \(-45\) to infinity and has a unique zero \(r>3\). For \(0<h\le2\), the identity
\[
P(h)=h^3(h^2-8)+48\bigl(1-(h-3)^2\bigr)<0
\]
holds (strictly, also at endpoints), so \((B_4)_{22}<0\) and \(\det B_4\ge0\), proving contraction. For \(2<h<r\), \(\det B_4<0\), proving noncontractivity. For \(h\ge r>3\),
\[
P(3+t)=t^5+15t^4+82t^3+150t^2+189t+75>0,
\]
so \((B_4)_{22}>0\), excluding all remaining steps. At \(h=2\), direct substitution gives \(R_4=\frac13\begin{pmatrix}-1&-2\\2&1\end{pmatrix}\) with singular values \(1\) and \(1/3\).

For the rational witness \(h=9/4\), exact arithmetic gives \((B_3)_{22}=-12879/16384\) and \(\det B_3=103915305/268435456>0\), whereas \(\det B_4=-5845760259183/17592186044416<0\). Also \(\operatorname{tr}R_4=-107/2048\) and \(\det R_4=1949353/4194304\), so its two eigenvalues are conjugate and have modulus \(\sqrt{1949353/4194304}<1\). This establishes both strict one-step contraction for the third-order method and nonnormal transient amplification for RK4 at the same step.

## Verification

The standalone `verify.py` performs exact symbolic checks of the three propagation matrices, their energy-matrix factors, the polynomial shift identities and endpoint computations. It also checks exact-rational steps on both sides of the energy boundaries. Run `python verify.py` with SymPy installed. The full proof of the infinite step intervals is the sign and uniqueness argument above, not the finite test grid.

## Relationship to prior work

Sun and Shu (2018) developed the general energy approach and established general strong-stability conclusions for third-order Runge–Kutta and counterexamples for classical fourth-order Runge–Kutta; their exhibited fourth-order counterexample uses a three-dimensional matrix and concerns sufficiently small steps. Achleitner, Arnold and Jüngel (2023) connected hypocoercivity indices to local strong stability, and their later note explicitly uses the tridiagonal rank-one-damped generator family containing the present two-coordinate matrix (up to an orthogonal change of coordinates). These results motivate the chosen benchmark but do not supply the exact **global-in-step** nonexpansivity intervals \([0,2]\), \([0,\alpha]\), \([0,2]\), or the rational same-matrix spectral-versus-norm witness. The general two-by-two energy test is elementary; the contribution is the exact classification and order reversal for this natural benchmark, not a new abstract contractivity criterion.

## Limitations

The result concerns Euclidean one-step contractivity on one fixed two-dimensional linear generator in exact arithmetic. It makes no general statement about nonlinear convergence, arbitrary inner-product norms, global error, larger dimensions, other damped-oscillator ratios, or floating-point implementations. Larger allowed energy-safe steps do not alone imply superior accuracy. Equivalence to a specialized previously published calculation cannot be ruled out without an independent literature audit.

## References

- Z. Sun and C.-W. Shu, *Strong stability of explicit Runge–Kutta time discretizations*, arXiv:1811.10680 (first posted 2018-11-26), especially introduction and Section 3.2. https://arxiv.org/abs/1811.10680
- F. Achleitner, A. Arnold and A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge–Kutta methods*, arXiv:2308.05689v1 (posted 2023-08-10), especially Theorem 2 and examples. https://arxiv.org/abs/2308.05689
- F. Achleitner, A. Arnold and A. Jüngel, *Hypocoercivity for Linear ODEs and Strong Stability for Runge–Kutta Methods*, arXiv:2310.19758 (first posted 2023-10-30), especially the canonical generator (2) and Proposition 3. https://arxiv.org/abs/2310.19758
