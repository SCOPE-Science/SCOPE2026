# Sharp small-cell shape asymmetry for four Gaussian Gabor atoms

## Finding

Let \(g(t)=2^{1/4}e^{-\pi t^2}\) in \(L^2(\mathbb R)\), and use the Weyl time-frequency shift
\[
(\rho(x,\omega)g)(t)=e^{2\pi i\omega(t-x/2)}g(t-x).
\]
For \(a,b>0\), let \(G(a,b)\) be the Gram matrix, in the stated order, of the four unit vectors
\[
g,\quad\rho(a,0)g,\quad\rho(0,b)g,\quad\rho(a,b)g.
\]
The determinant is exactly
\[
D(a,b):=\det G(a,b)
=\big[(1-e^{-\pi a^2})(1-e^{-\pi b^2})\big]^2
-16e^{-\pi(a^2+b^2)}\sin^4(\pi ab/2).
\tag{1}
\]
For \(h>0\) define \(\mathcal D(h)=\sup_{a,b>0,\,ab=h}D(a,b)\). Define
\[
F(y)=\frac{(1-e^{-y})^2}{y^2}-e^{-y}\qquad(y>0).
\]
There is a *unique* \(y_*>0\) maximizing \(F\). It is the unique positive solution of
\[
y^3+2y+4-2e^y-2(y+1)e^{-y}=0.
\tag{2}
\]
Then the sharp fixed-area small-cell law is
\[
\boxed{\lim_{h\downarrow0}\frac{\mathcal D(h)}{h^4}=\pi^4F(y_*)=5.1456237927599207988\ldots.}
\tag{3}
\]
Moreover, for **every** choice of maximizing rectangles, relabel the sides so that \(a_h\ge b_h\). Then
\[
\boxed{a_h\longrightarrow \sqrt{y_*/\pi}=0.8708763171240938803\ldots,\qquad
b_h/h\longrightarrow\sqrt{\pi/y_*}.}
\tag{4}
\]
The square, by contrast, has
\[
D(\sqrt h,\sqrt h)=\frac{\pi^6}{3}h^6+O(h^7).
\tag{5}
\]
Thus every sufficiently small fixed-area optimum is non-square, and the optimal squared four-vector volume is of order \(h^4\) rather than \(h^6\). The theorem concerns Gram determinants (product of four Gram eigenvalues), not the optimal smallest eigenvalue or the condition number.

## Assumptions and scope

All parameters \(a,b,h\) are strictly positive and real. The window is the specified unit \(L^2\)-Gaussian, the time-frequency shifts use the displayed Weyl normalization, the design region consists of *exactly the four rectangle corners*, and the constrained quantity is the Euclidean phase-space cell area \(ab=h\). No result is asserted for general four-point configurations, different windows, sheared cells, or infinite Gabor lattices. The limit \(h\downarrow0\) allows arbitrarily anisotropic rectangles. The Gaussian four-vector Gram determinant is invariant under rephasing of the individual vectors.

## Proof

**Step 1: exact Gram determinant.** Under the Gaussian Bargmann correspondence, the above vectors are coherent kernels at \(0,\sqrt\pi a,i\sqrt\pi b,\sqrt\pi(a+ib)\), modulo individual unit phases. Normalized coherent kernels satisfy
\[
\langle k_u,k_v\rangle
=\exp\big[-(|u|^2+|v|^2)/2+\bar u v\big].
\]
Set \(x=e^{-\pi a^2/2}\), \(y=e^{-\pi b^2/2}\), and \(z=e^{i\pi ab}\). Up to conjugating every matrix entry, the Gram matrix equals
\[
\begin{pmatrix}
1&x&y&xy\\
x&1&xyz&yz\\
y&xy/z&1&x/z\\
xy&y/z&xz&1
\end{pmatrix}.
\]
Its algebraic determinant is
\[
\big[(1-x^2)(1-y^2)\big]^2-x^2y^2(2-z-z^{-1})^2.
\]
Since \(2-z-z^{-1}=4\sin^2(\pi ab/2)\), this gives (1). This symbolic identity is also independently checked by the included executable.

**Step 2: a useful nonnegative form.** Put \(A=\pi a^2/2\), \(B=\pi b^2/2\), and \(c=\pi ab/2=\sqrt{AB}\). Identity (1) is equivalent to
\[
D(a,b)=16e^{-2(A+B)}\big[\sinh^2 A\,\sinh^2 B-\sin^4c\big].
\tag{6}
\]
The bracket is nonnegative because \(\sinh A\,\sinh B\ge AB=c^2\ge\sin^2 c\). In particular \(D\ge0\). For any fixed \(h>0\), \(D(a,h/a)\to0\) as \(a\to0\) or \(a\to\infty\), since it is at most \([(1-e^{-\pi a^2})(1-e^{-\pi h^2/a^2})]^2\). A maximizer at area \(h\) therefore exists.

**Step 3: all possible shrinking-area regimes.** Take any \(h_j\downarrow0\) and \(a_j\ge b_j>0\) with \(a_jb_j=h_j\). Passing to a subsequence, the larger side has a limit in \([0,\infty]\). If \(a_j\to a_0\in(0,\infty)\), then \(b_j=h_j/a_j\to0\), and Taylor expansion directly in (1) yields
\[
\frac{D(a_j,b_j)}{h_j^4}\longrightarrow
\pi^4F(\pi a_0^2).
\tag{7}
\]
If \(a_j\to\infty\), then \(D(a_j,b_j)\le(1-e^{-\pi b_j^2})^2\le\pi^2b_j^4\), whence \(D/h_j^4\le\pi^2/a_j^4\to0\).

If \(a_j\to0\), then both sides tend to zero. Divide (6) by \(h_j^4\) to get the exact expression
\[
\frac{D}{h^4}=\pi^4e^{-2(A+B)}
\left[\left(\frac{\sinh A}{A}\right)^2
\left(\frac{\sinh B}{B}\right)^2-
\left(\frac{\sin c}{c}\right)^4\right].
\tag{8}
\]
As \(A,B,c\to0\), its bracket tends to zero. Thus the normalized determinant tends to zero also in this regime. These three cases exhaust *all* eccentricity scales, without assuming bounded aspect ratio.

**Step 4: scalar optimization and uniqueness.** The function \(F\) is positive for \(y>0\), since
\[
F(y)=e^{-y}\left[\left(\frac{\sinh(y/2)}{y/2}\right)^2-1\right]>0.
\]
It tends to zero at both \(0\) and \(+\infty\), so it has a positive interior maximum. Differentiation gives
\[
F'(y)=e^{-y}Q(y)/y^3,
\quad Q(y)=y^3+2y+4-2e^y-2(y+1)e^{-y}.
\]
Here \(Q(0)=Q'(0)=Q''(0)=Q'''(0)=0\), while \(Q''''(0)=4\) and
\[
Q'''''(y)=-2e^{-y}(e^{2y}-y+4)<0\qquad(y\ge0).
\]
Consequently \(Q''''\) decreases through zero exactly once; successively integrating, each of \(Q'''\), \(Q''\), \(Q'\), and \(Q\) first increases and then decreases past zero exactly once on \((0,\infty)\). (For each derivative the starting value is zero, and its limit at \(+\infty\) is negative.) Hence \(Q\) has exactly one positive zero \(y_*\), and \(F\) increases before and decreases after it.

**Step 5: sharpness and rigidity of the asymptotic shape.** For a lower bound, fix \(a=\sqrt{y_*/\pi}\) and \(b=h/a\). Equation (7) yields \(\liminf\mathcal D(h)/h^4\ge\pi^4F(y_*)\). For an upper bound, choose maximizing rectangles, sort their sides, and apply the exhaustive subsequential analysis in Step 3. Any subsequential limit is either zero or \(\pi^4F(\pi a_0^2)\le\pi^4F(y_*)\), proving (3). Because the lower bound is positive and the scalar maximizer unique, every maximizing larger side converges to \(\sqrt{y_*/\pi}\). Since \(b=h/a\), (4) follows.

**Step 6: square benchmark.** In (8), set \(A=B=c=\pi h/2\). Expanding \((\sinh c/c)^4-(\sin c/c)^4=4c^2/3+O(c^4)\) gives (5), with error \(O(h^7)\) from the exponential prefactor. Since the optimum has strictly positive \(h^4\) coefficient, the square is not maximizing for all sufficiently small \(h\). This completes the proof.

## Verification

Running `python verify.py` with SymPy and mpmath checks the exact symbolic determinant against the coherent-kernel Gram matrix, seven independent high-precision Gram determinants, the scalar stationary point, several asymptotic scaling ratios, and small-area asymmetric advantages. The program is a finite supplementary check; the all-parameter determinant and asymptotic maximum are proved by Steps 1–6. Approximate constants are displayed only to aid identification of the uniquely defined exact root.

## Relationship to prior work

The original Gaussian coherent-kernel inner product and the link between Gram eigenvalues and Riesz stability are standard. Faulhuber's 2017 work optimizes *infinite Gaussian Gabor lattice frame bounds* at specified density, including a square-lattice comparison within rectangular infinite lattices; its optimization functional and admissible object are different from the finite four-vector Gram determinant here. Oussa's August 2026 result exhibits a four-point time-frequency dependence with a specially constructed non-Gaussian window in the endpoint Gelfand–Shilov class; it neither implies nor excludes this quantitative four-Gaussian rectangular determinant asymptotic. The new question is the optimal *finite four-atom volume* when the four points enclose a prescribed small area, and the answer has a strong anisotropic shape transition. These precedents are not claimed as supporting the new formula.

## Limitations

This is an exact small-area *asymptotic* of the optimal Gram determinant, not an all-area classification of optimal rectangles. It does not optimize the smallest Gram eigenvalue, spectral condition number, infinite-frame bounds, arbitrary quadrilateral geometries, or non-Gaussian windows. The cited primary literature and mathematical-record searches found no dominating theorem, but absence from indexed searches does not establish historical priority. Independent external review has not been performed.

## References

1. V. Oussa, *A minimal HRT counterexample at the sharp Gelfand–Shilov threshold*, arXiv:2609.27774, first posted 17 August 2026, https://arxiv.org/abs/2609.27774. Read original HTML manuscript, especially the four-point theorem and marked-configuration sections.
2. M. Faulhuber, *Minimal Frame Operator Norms Via Minimal Theta Functions*, Journal of Fourier Analysis and Applications, online 11 February 2017, https://doi.org/10.1007/s00041-017-9526-x. Read original full-text introduction, Theorem 1.1, and Gaussian-frame optimization sections.
3. E. A. Kiselev, L. A. Minin, I. Ya. Novikov, S. N. Ushakov, *Localization of the window functions of dual and tight Gabor frames generated by the Gaussian function*, Sbornik: Mathematics 215 (2024), 364–382, https://doi.org/10.4213/sm9957e. Relevant accessible description of finite Gram eigenvalues and Riesz stability; the full text was not systematically inspected.
