# Asymmetric D-optimality of small-area Gaussian Gabor rectangles

## Finding
Let \(g(t)=2^{1/4}e^{-\pi t^2}\) in \(L^2(\mathbb R)\), and use the Weyl time-frequency shift
\[
(W_{p,q}g)(t)=e^{2\pi i q(t-p/2)}g(t-p).
\]
For \(a,b>0\), let \(G(a,b)\) be the \(4\times4\) Gram matrix of the unit vectors indexed, in order, by the four rectangle corners \((0,0),(a,0),(0,b),(a,b)\). Put \(u=\pi ab\), and let
\[
D_*(u)=\max_{a,b>0:\;\pi ab=u}\det G(a,b).
\]
There is a unique positive maximizer \(x_*\) of
\[
f(x)=\left(\frac{1-e^{-x}}x\right)^2-e^{-x}\quad(x>0),
\]
with \(x_*=2.38266416673503469\ldots\) and \(c_*=f(x_*)=0.05282488254575485\ldots\). As \(u\downarrow0\),
\[
\boxed{D_*(u)=c_*u^4+O(u^6).}
\]
For all sufficiently small positive \(u\), the maximizing ordered pairs \((a,b)\) consist of precisely two partners obtained by swapping their coordinates. In the branch where \(a>b\),
\[
\boxed{\pi a^2=x_*+O(u^2),\qquad b=\frac{u}{\pi a}.}
\]
Thus the longer side tends to the nonzero length \(\sqrt{x_*/\pi}=0.87087631712409\ldots\), while the shorter side tends to zero. In contrast, the balanced rectangle \(a=b=\sqrt{u/\pi}\) has
\[
\det G\bigl(\sqrt{u/\pi},\sqrt{u/\pi}\bigr)=\frac{u^6}{3}+O(u^7),
\]
so the optimized determinant divided by the balanced determinant is asymptotic to \(3c_*/u^2\), which diverges. The determinant is the squared four-dimensional volume of the synthesis vectors, a natural D-optimality measure for finite Gaussian Gabor sampling.

## Assumptions and scope
All four states use exactly the same \(L^2\)-normalized Gaussian and the symmetric Weyl convention above. The constraint fixes the positive symplectic area \(ab\), not the perimeter or Euclidean diameter; only axis-aligned rectangles are optimized. The parameter \(u=\pi ab\) tends to zero through positive real values. The statement concerns the determinant of the four-state Gram matrix, **not** its least eigenvalue or the optimal placement among arbitrary four-point configurations. The two maximizing rectangles are distinguished as ordered time and frequency spacings; their swap gives the second branch.

## Proof
**Step 1: Exact Gram determinant.** Gaussian integration yields, for \(z=(p,q)\), \(w=(r,s)\),
\[
\langle W_zg,W_wg\rangle=e^{-\pi|z-w|^2/2}e^{\pi i(ps-qr)}.
\]
Set \(h=e^{-\pi a^2/2}\), \(k=e^{-\pi b^2/2}\), \(\zeta=e^{i\pi ab}\). With the displayed ordering, the Gram matrix is
\[
\begin{pmatrix}
1&h&k&hk\\
h&1&hk\zeta&k\zeta\\
k&hk\zeta^{-1}&1&h\zeta^{-1}\\
hk&k\zeta^{-1}&h\zeta&1
\end{pmatrix}.
\]
Direct expansion and factorization give
\[
\det G=\bigl((1-h^2)(1-k^2)\bigr)^2
-\bigl(hk(\zeta+\zeta^{-1}-2)\bigr)^2.
\]
Since \(\zeta+\zeta^{-1}-2=-4\sin^2(u/2)\), on putting \(x=\pi a^2\) and \(y=\pi b^2\) (so \(xy=u^2\)) this becomes the exact positive expression
\[
\boxed{\Delta_u(x)=\bigl((1-e^{-x})(1-e^{-u^2/x})\bigr)^2-16e^{-x-u^2/x}\sin^4(u/2).}\tag{1}
\]
It is strictly positive because \(4\sinh(x/2)\sinh(y/2)>xy=u^2\ge4\sin^2(u/2)\). Moreover it tends to zero as \(x\to0\) or \(x\to\infty\) with \(u\) fixed, so the maximum in the theorem is attained.

**Step 2: The normalized singular limit.** Define \(A(s)=(1-e^{-s})/s\) for \(s>0\) and \(A(0)=1\). Dividing (1) by \(u^4\) gives the exact identity
\[
\frac{\Delta_u(x)}{u^4}= A(x)^2 A(u^2/x)^2-e^{-x-u^2/x}\left(\frac{\sin(u/2)}{u/2}\right)^4.\tag{2}
\]
For every fixed \(x>0\), the right side tends to \(f(x)\), locally uniformly together with its derivatives, and has an even analytic expansion in \(u\) near zero. More precisely, uniformly on compact subintervals of \((0,\infty)\),
\[
\frac{\Delta_u(x)}{u^4}=f(x)+u^2\left(\frac{e^{-x}}6-\frac{f(x)}x\right)+O(u^4).\tag{3}
\]
The function \(f\) is strictly positive because \(\sinh(x/2)>x/2\), and tends to zero at both endpoints \(0\) and \(+\infty\).

**Step 3: Uniqueness of the limiting maximizer.** Differentiating exactly, let
\[
H(x)=x^3 e^{2x}f'(x)=(x^3+2x+4)e^x-2e^{2x}-2x-2.
\]
The Taylor coefficients of \(H\) at orders \(0,1,2,3\) vanish. For every integer \(n\ge4\), the coefficient of \(x^n\) is
\[
\frac{n(n-1)(n-2)+2n+4-2^{n+1}}{n!}.
\]
These coefficients are positive for \(n=4,5,6\) and negative for every \(n\ge7\): the latter follows from the strict inequality \(2^{8}>7\cdot6\cdot5+14+4\) and the induction inequality
\[
2P(n)-P(n+1)=(n-2)(n^2-4n-1)>0\quad(n\ge7),
\]
where \(P(n)=n(n-1)(n-2)+2n+4\). Therefore \(H(x)/x^6\) is strictly decreasing on \((0,\infty)\): it is a sum of positive multiples of \(x^{-2}\), \(x^{-1}\), and \(1\), followed by strictly negative multiples of positive powers of \(x\). It tends to \(+\infty\) at zero and \(-\infty\) at infinity, hence has precisely one positive zero, \(x_*\). The sign change is strict, so \(f\) increases before \(x_*\), decreases afterward, and \(f''(x_*)<0\).

**Step 4: No maximizing mass escapes.** By swapping \(a,b\) if needed, any maximizer can be parameterized by \(x\ge u\), \(y=u^2/x\le x\). Fix a sequence \(u_j\downarrow0\) and let \(x_j\ge u_j\) be such maximizers. Evaluating (2) at the fixed \(x_*\) shows
\[
\liminf_{j\to\infty}\Delta_{u_j}(x_j)/u_j^4\ge c_*>0.
\]
If \(x_j\to\infty\), the right side of (2) is at most \(A(x_j)^2\to0\). If \(x_j\to0\), then \(0<y_j\le x_j\to0\), and both terms in (2) tend to one, so their difference tends to zero. Consequently \(x_j\) stays in a compact subset of \((0,\infty)\). Every convergent subsequence has limit \(x_0\) with \(f(x_0)\ge c_*\), hence \(x_0=x_*\) by Step 3. It follows that all maximizing representatives satisfy \(x_j\to x_*\).

**Step 5: Exactly two optimal branches and the sharp asymptotic.** The stationary equation obtained by differentiating (2) is real-analytic in \((x,u^2)\) near \((x_*,0)\), with nonzero derivative in \(x\) because \(f''(x_*)<0\). The implicit-function theorem therefore gives exactly one stationary branch there, \(x(u)=x_*+O(u^2)\). The compactness argument forces every global maximizing representative \(x\ge u\) onto that branch for all sufficiently small \(u\). The coordinate-swap symmetry gives its sole other ordered maximizing rectangle. Evaluating (3) along the branch yields \(D_*(u)=c_*u^4+O(u^6)\). Finally, a direct Taylor expansion of (1) at \(x=y=u\) gives \(u^6/3+O(u^7)\), proving the balanced comparison and the divergent determinant advantage.

## Verification
The standalone `checker.py` confirms the \(4\times4\) determinant factorization exactly using symbolic algebra, checks the coefficient signs and polynomial induction identity, and compares fifteen high-precision complex Gram determinants with (2). It numerically locates the nondegenerate positive solution \(x_*\) and checks the small-\(u\) expansions along the stationary and balanced branches. `checker_output.txt` contains the actual run results. None of these finite computations substitutes for the uniform compactness and uniqueness arguments above.

## Relationship to prior work
The qualitative independence of finite Gaussian time-frequency shifts is classical. Benedetto and Bourouihiya (2012) study HRT independence under decay assumptions; Gröchenig (2014) studies quantitative Riesz-bound deterioration for large finite Gabor sections; Gröchenig, Ortega-Cerdà, and Romero (2013) prove deformation stability of Gabor systems. These results explain why quantitative finite-set geometry is natural, but the inspected relevant portions do not state or imply the **fixed-area four-corner Gram-determinant maximum**, its singularly anisotropic limiting optimizer, or the \(u^4\)-versus-\(u^6\) sharp comparison. The statement can also be expressed as a normalized Bargmann–Fock kernel determinant problem; routine kernel equivalence by itself does not provide the extremal assertion. Related kernel-interpolation literature concerns numerical stabilization of Gaussian radial basis functions with different, real symmetric kernels and constraints. No publication-priority guarantee is claimed.

## Limitations
The classification of global maximizers is proved only for all sufficiently small positive area; no exact transition area or all-area phase diagram is asserted. The determinant is not equivalent to an optimized minimum singular value. The four corners and Gaussian width are fixed in the stated convention. The numerical values are approximations to uniquely defined analytic quantities. Older or unindexed coherent-state determinant design results may contain equivalent formulations, and independent assessment of originality has not been performed.

## References
1. J. J. Benedetto and A. Bourouihiya, *Linear Independence of Finite Gabor Systems Determined by Behavior at Infinity*, arXiv:1211.0337v1, publicly posted 2012-11-02.
2. K. Gröchenig, J. Ortega-Cerdà, and J. L. Romero, *Deformation of Gabor Systems*, arXiv:1311.3861v1, publicly posted 2013-11-15.
3. K. Gröchenig, *Linear Independence of Time-Frequency Shifts?*, arXiv:1401.1353v1, publicly posted 2014-01-07.
4. K. Gröchenig, A. Haimi, and J. L. Romero, *Completeness of Gabor Systems*, arXiv:1507.02124v1, publicly posted 2015-07-08.
