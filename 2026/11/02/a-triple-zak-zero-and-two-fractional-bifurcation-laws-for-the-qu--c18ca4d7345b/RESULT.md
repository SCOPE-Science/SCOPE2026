# A triple Zak zero and two fractional bifurcation laws for the quadratic B-spline

## Finding

For \(B_1=\mathbf 1_{[-1/2,1/2]}\), let \(B_3=B_1*B_1*B_1\). Define
\[
Z_{1/b}B_3(x,\nu)=b^{-1/2}\sum_{k\in\mathbb Z}B_3((x-k)/b)e^{2\pi i k\nu}.
\]
Set \(\beta=(99+2\sqrt{42})/39\approx2.87080721530\). For every real \(8/3<b<3\), the complete set of zeros of \(Z_{1/b}B_3(1/2,\nu)\) with \(0\leq\nu<1\) is:

- \(\{1/2\}\), a simple zero, if \(8/3<b<\beta\);
- \(\{1/2\}\), a zero of multiplicity three as a function of the real frequency, if \(b=\beta\);
- \(\{\nu_b,1/2,1-\nu_b\}\), three simple zeros, if \(\beta<b<3\), where \(1/3<\nu_b<1/2\).

In the last case the exact parameter \(\nu_b=\pi^{-1}\arccos\sqrt{y_b}\) is defined by the unique real root \(y_b\in(0,1/4)\) of the cubic below. Furthermore,
\[
\frac12-\nu_b=\frac1\pi\sqrt{\frac{33\sqrt{42}-28}{76}}\,(b-\beta)^{1/2}+O((b-\beta)^{3/2})\quad(b\downarrow\beta),
\]
and
\[
\nu_b-\frac13=\frac{2}{\pi\sqrt3}\left(\frac3{128}\right)^{1/3}(3-b)^{2/3}+O(3-b)\quad(b\uparrow3).
\]

## Assumptions and scope

The real scaling parameter belongs to the **open** interval \(8/3<b<3\), and the spatial coordinate is fixed to \(x=1/2\). Frequency is taken modulo one. Multiplicity means the order of vanishing of the analytic trigonometric polynomial in the real frequency variable. No claim is made at \(b=3\) or for other spatial coordinates. The normalization of the Zak transform is the same as in [1, Eq. (1.1)].

The centered order-three spline has the elementary piecewise form
\[
B_3(t)=\begin{cases}3/4-t^2,&|t|\leq1/2,\\(3/2-|t|)^2/2,&1/2\leq|t|\leq3/2,\\0,&|t|\geq3/2.\end{cases}
\]
(The values agree at the piece boundaries.)

## Proof

**Exact finite polynomial reduction.** For \(8/3<b<3\), only the eight terms with indices \(-3,-2,-1,0,1,2,3,4\) contribute when \(x=1/2\). Pair the indices \(-j\) and \(j+1\) for \(j=0,1,2,3\), and put
\[
a_0=\frac{3b^2-1}{4b^2},\quad a_1=\frac{9(b-1)^2}{8b^2},\quad a_2=\frac{(3b-5)^2}{8b^2},\quad a_3=\frac{(3b-7)^2}{8b^2}.
\]
With \(y=\cos^2(\pi\nu)\), the pair identity and odd Chebyshev polynomials give
\[
Z_{1/b}B_3(1/2,\nu)=\frac2{\sqrt b}\,e^{\pi i\nu}\cos(\pi\nu)H_b(y),
\]
where
\[
H_b(y)=a_0+a_1(4y-3)+a_2(16y^2-20y+5)+a_3(64y^3-112y^2+56y-7).
\]
Equivalently, this is the explicit cubic
\[
H_b(y)=\frac{(576b^2-2688b+3136)y^3+(-864b^2+4224b-5088)y^2+(360b^2-1824b+2280)y-39b^2+198b-247}{8b^2}.
\]
Its leading coefficient is \(8(3b-7)^2/b^2>0\).

**Exactly one real cubic root.** The cubic discriminant is exactly
\[
\operatorname{disc}_y(H_b)=\frac{81(b-3)^4}{b^8}\,Q(b),\qquad Q(b)=2349b^4-20844b^3+67662b^2-95084b+48621.
\]
For \(t=3b-8\in(0,1)\), direct polynomial expansion yields
\[
-Q((8+t)/3)=\frac{793}{3}(1-t)^4+1296t(1-t)^3+2176t^2(1-t)^2+\frac{4096}{3}t^3(1-t)+192t^4>0.
\]
Therefore the discriminant is strictly negative. Since the coefficients are real and the leading term is positive, \(H_b\) has exactly one distinct real root, and that root is simple. The exact endpoint values are
\[
H_b(0)=-\frac{39b^2-198b+247}{8b^2},\quad H_b(1/4)=\frac{3(b-3)^2}{4b^2}>0,\quad H_b(1)=\frac{3(11b^2-30b+27)}{8b^2}>0.
\]
The quadratic \(39b^2-198b+247\) has precisely one root in \((8/3,3)\), namely \(\beta\). Hence for \(b<\beta\) the unique real cubic root is negative, for \(b=\beta\) it is zero, and for \(b>\beta\) it belongs to \((0,1/4)\). Because \(y=\cos^2(\pi\nu)\in[0,1]\) for real frequency, the claimed zero counts follow. The factor \(\cos(\pi\nu)\) is simple at \(\nu=1/2\); its square \(y\) vanishes to order two there. At \(b=\beta\), simplicity of the cubic root at \(y=0\) makes the product vanish to order three. Otherwise the three zeros are all simple.

**First square-root law.** At \((b,y)=(\beta,0)\), the derivative \(\partial_yH_\beta(0)>0\); direct differentiation gives
\[
-\frac{\partial_bH_\beta(0)}{\partial_yH_\beta(0)}=K=\frac{33\sqrt{42}-28}{76}>0.
\]
The implicit-function theorem yields \(y_b=K(b-\beta)+O((b-\beta)^2)\). Using the Taylor expansion of \(\arccos\sqrt y\) at \(y=0\) gives the asserted square-root law, including its remainder.

**Second fractional law.** Write \(\delta=3-b>0\), \(h=y-1/4\). An exact expansion (not an asymptotic guess) is
\[
4(3-\delta)^2 H_{3-\delta}(1/4+h)=128h^3-384\delta h^3+192\delta h^2+288\delta^2h^3-216\delta^2h^2+18\delta^2h+3\delta^2.
\]
The unique real root tends to \(1/4\), since \(H_3(y)=(4y-1)^3/18\). Put \(\delta=s^3\) and \(h=s^2 q\) in the exact expansion and divide by \(s^6\). Its limit is \(128q^3+3\), which has a simple real root \(q_0=-(3/128)^{1/3}\). The implicit-function theorem at \((s,q)=(0,q_0)\) gives \(h=q_0\delta^{2/3}+O(\delta)\); the uniqueness of the real cubic root identifies that branch. Finally, \((d/dy)[\pi^{-1}\arccos\sqrt y]_{y=1/4}=-2/(\pi\sqrt3)\), proving the \(2/3\)-power law.

## Verification

The standalone script `check.py` recomputes the cubic discriminant and sign certificate, the three endpoint identities, the exact critical derivative, the degenerate limit, and the expanded cusp polynomial in exact SymPy arithmetic. It additionally compares the eight-term spline Zak sum directly with the cubic factor at 35 real parameter pairs. Run `python check.py` with SymPy installed; the expected final message begins `EXACT_ZAK_CUBIC_OK`. This is an auxiliary algebraic check, not a substitute for the infinite-parameter sign/implicit-function arguments above.

## Relationship to prior work

Hasannasab and Lemvig [1] introduce the precise Zak normalization, examine palindromic polynomial zeros on the vertical symmetry line in Section 6, and give a special order-three calculation in a different parameter regime. Their full-text discussion does not supply the odd nearest-integer \(R=3\), \(8/3<b<3\) vertical-slice zero classification, the discriminant threshold, or either fractional bifurcation law proved here. The earlier obstruction literature [2,3] treats Gabor frame-set slits or root grids rather than these multiplicities and local singular asymptotics; [4] concerns the second-order hat spline. Previous related calculations at the spatial slice \(x=0\) and \(2<b<8/3\) concern different Zak polynomials and do not imply this result. This is a best-knowledge distinction, not a claim of exhaustive worldwide uniqueness.

## Limitations

This gives a complete frequency-zero classification for exactly one natural vertical slice and parameter interval. It does **not** classify zeros at general \(x\), characterize the full Gabor frame set, determine higher-order splines, or establish behavior at the excluded endpoint \(b=3\). Computational sampling alone would not establish the result; the sign certificate and analytic argument are essential. Earlier or unindexed equivalent formulations may exist.

## References

[1] M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116, first publicly posted September 11, 2026. https://arxiv.org/abs/2609.13116 (especially Sections 1 and 6).

[2] J. Lemvig, *A new family of hyperbolic slits in the Gabor frame set of B-spline generators*, arXiv:2601.07642 (2026). https://arxiv.org/abs/2601.07642.

[3] J. Lemvig and K. H. Nielsen, *Counterexamples to the B-spline conjecture for Gabor frames*, arXiv:1507.03982 (2015), later J. Fourier Anal. Appl. 22 (2016). https://arxiv.org/abs/1507.03982.

[4] A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (2026). https://arxiv.org/abs/2609.00481.
