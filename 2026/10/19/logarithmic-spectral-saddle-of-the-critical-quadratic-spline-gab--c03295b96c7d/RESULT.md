# Logarithmic spectral saddle of the critical quadratic-spline Gabor operator

## Finding
Consider the centered, integral-one cardinal quadratic B-spline
\[
g(t)=\begin{cases}
\frac34-t^2,&|t|\le\frac12,\\
\frac12(\frac32-|t|)^2,&\frac12<|t|\le\frac32,\\
0,&|t|>\frac32.
\end{cases}
\]
Let \(S_g\) be the positive Gabor operator for the unit rectangular lattice: its quadratic form is
\[
\langle S_g f,f\rangle=\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i m(\cdot)}g(\cdot-n)\rangle|^2.
\]
The unitary Zak transform conjugates \(S_g\) to multiplication by a real scalar \(H\) on the unit torus. Its normalized spectral measure \(\mu\) (the distribution of \(H\) under unit torus area) is absolutely continuous, supported on \([0,1]\), has no atoms and satisfies the following *sharp spectral trichotomy*:
\[
\lim_{s\downarrow0}\rho(s)=\frac12,\qquad
\rho(s)=\frac1\pi\log\frac1{|s-1/4|}+O(1)\quad(s\to1/4),\qquad
\rho(s)\sim\frac1{\pi\sqrt{1-s}}\quad(s\uparrow1),
\]
where \(\rho=d\mu/ds\) is the density on \((0,1)\setminus\{1/4\}\). The logarithm has the **exact** coefficient \(1/\pi\), and \(1/4\) is the only interior critical spectral value. In addition, the normalized distribution has an explicit one-dimensional integral, and
\[
\int_0^1 s\,d\mu(s)=\frac{11}{20},\quad
\mu([0,\varepsilon])\sim\frac\varepsilon2,\quad
\mu([1-\varepsilon,1])\sim\frac{2\sqrt\varepsilon}{\pi}.
\]
The operator has spectrum \([0,1]\), has no eigenvalues, and has zero optimal lower frame bound. Its Tikhonov resolvent spectral mean obeys
\[
\int_0^1\frac{d\mu(s)}{s+\eta}=\frac12\log\frac1\eta+O(1)\qquad(\eta\downarrow0).
\]

## Assumptions and scope
The window \(g\) is exactly the unit-integral spline above, **not** an \(L^2\)-normalized spline; its squared norm is \(11/20\). The lattice has translation step and modulation step both exactly one. Define
\[
(Zf)(x,\omega)=\sum_{k\in\mathbb Z}f(x-k)e^{2\pi ik\omega},\qquad(x,\omega)\in[0,1)^2.
\]
The boundary identifications follow the Zak quasiperiodicity; \(Z\) is unitary for Lebesgue measure with total cell area one. For a bounded Borel function \(\Phi\), its **normalized spectral mean** is
\[
\mathcal T(\Phi(S_g)):=\int_{[0,1)^2}\Phi(|Zg(x,\omega)|^2)\,dx\,d\omega
=\int_0^1\Phi(s)\,d\mu(s).
\]
This is the canonical torus-fiber mean, **not** a trace of \(\Phi(S_g)\) as an operator on infinite-dimensional \(L^2(\mathbb R)\). The spectral density assertion is an almost-everywhere density, with its specified continuous choice away from \(1/4\). No claim is made for noncritical lattices or higher spline orders.

## Proof
**1. Exact Zak multiplier and normalization.** At the unit lattice, Zak orthogonality gives \(ZS_gZ^{-1}=M_H\), where \(H=|Zg|^2\). On \(0\le x\le1/2\), the only nonzero Zak coefficients are
\[
Zg(x,\omega)=\frac{(1/2-x)^2}{2}e^{-2\pi i\omega}
+\left(\frac34-x^2\right)
+\frac{(1/2+x)^2}{2}e^{2\pi i\omega}.
\]
Evenness and quasiperiodicity preserve the modulus under \(x\mapsto1-x\). Put \(y=\min\{x,1-x\}\), \(T=1-4y^2\), and \(V=\sin^2(\pi\omega)\). Expanding the two real and imaginary parts of the displayed finite Laurent polynomial yields, identically,
\[
\boxed{H(x,\omega)=1-V+\frac14V^2T^2.}\tag{1}
\]
Here \(0\le V,T\le1\) and \(\partial H/\partial V=-1+VT^2/2\le-1/2\). Thus \(H\) ranges exactly over \([0,1]\), with minimum at \((x,\omega)=(1/2,1/2)\) and maximum on the frequency circle \(\omega=0\). Since a nonconstant polynomial in the variables \(V,T\) has level sets of zero planar measure, the spectral measure has no atoms; the change of variables in Step 2 gives its density explicitly. This establishes the spectrum and absence of eigenvalues (multiplication operator eigenvalues require positive-measure level sets). The zero minimum makes the optimal lower frame bound zero.

**2. Exact spectral distribution.** Under unit torus area, the random variables \(T\) and \(V\) are independent and have respective densities
\[
p_T(t)=\frac1{2\sqrt{1-t}},\quad 0<t<1;\qquad
p_V(v)=\frac1{\pi\sqrt{v(1-v)}},\quad0<v<1.
\]
For \(0<s<1\) and \(0\le t\le T_s:=\min\{1,2\sqrt s\}\), let
\[
v_s(t)=\frac{2(1-s)}{1+\sqrt{1-t^2(1-s)}}.
\]
Solving \(s=1-v+t^2v^2/4\) and using the strict negativity of its derivative with respect to \(v\) gives \(H\le s\) exactly when \(V\ge v_s(T)\), and this is possible exactly when \(T\le T_s\). Because \(\Pr(V\ge v)=(2/\pi)\arccos\sqrt v\), the exact cumulative distribution is
\[
\boxed{F(s):=\mu([0,s])=\frac1\pi\int_0^{T_s}
\frac{\arccos\sqrt{v_s(t)}}{\sqrt{1-t}}\,dt.}\tag{2}
\]
Differentiating away from \(s=1/4\) (the boundary integrand vanishes when \(T_s<1\)), and using \(\partial_sv_s(t)=-[1-t^2(1-s)]^{-1/2}\), gives
\[
\boxed{\rho(s)=\frac1{2\pi}\int_0^{T_s}
\frac{dt}{\sqrt{1-t}\sqrt{v_s(t)(1-v_s(t))}\sqrt{1-t^2(1-s)}}.}\tag{3}
\]
Both integrations involve only integrable square-root endpoint singularities for \(s\ne1/4\). In particular, this establishes absolute continuity on \((0,1)\) and no hidden spectral mass at \(1/4\). Formula (1) also gives
\[
\mathbb E H=1-\mathbb E V+\tfrac14\mathbb E V^2\,\mathbb E T^2
=1-\tfrac12+\tfrac14\cdot\tfrac38\cdot\tfrac8{15}=\tfrac{11}{20}.
\]

**3. All critical values and the Morse saddle.** For \(0<V<1\), the strictly negative \(V\)-derivative prevents any stationary point in the frequency direction unless \(\omega=0\) or \(1/2\). At \(\omega=1/2\), the multiplier is \(H=T^2/4\); its only critical spatial points on the torus are \(x=0\) and \(x=1/2\). The latter is the global minimum (value zero); the former has value \(1/4\). At \(\omega=0\) the entire frequency circle is the maximum level one. Thus \(1/4\) is the unique interior critical value. The piecewise spline formula is twice continuously differentiable, and it is real-analytic in a neighborhood of the point \((0,1/2)\) (the change of the explicit formula at \(x=0\) matches to all orders there for \(H\)). In real torus local coordinates \(u=x\), \(w=\omega-1/2\) near this saddle,
\[
H(u,1/2+w)=\tfrac14-2u^2+\tfrac{\pi^2}{2}w^2+O((|u|+|w|)^4).
\]
It has nonzero Hessian determinant and Morse index one. Changing to \(p=\sqrt2u\), \(q=(\pi/\sqrt2)w\) gives local area element \(du\,dw=\pi^{-1}\,dp\,dq\) and quadratic normal form \(H-1/4=q^2-p^2\). The smooth Morse coordinate correction has Jacobian \(1/\pi+O(|p|+|q|)\), and its error contributes only a bounded term to the coarea density. Indeed, under \(r=q+p\), \(h=q-p\), one has \(q^2-p^2=rh\) and \(dp\,dq=\tfrac12dr\,dh\); integrating \(\delta(s-1/4-rh)\) in any fixed small coordinate square produces exactly \(\log(1/|s-1/4|)+O(1)\). The rest of the torus has no critical points at \(1/4\), so contributes a bounded continuous density. Therefore
\[
\rho(s)=\frac1\pi\log\frac1{|s-1/4|}+O(1),\qquad s\to(1/4)^\pm.
\]
The coefficient accounts for the single saddle on the *identified* torus; the boundary point \(x=1\) is the same point as \(x=0\) and is not a second saddle.

**4. Sharp lower and upper edges.** Near \((x,\omega)=(1/2,1/2)\), set \(u=x-1/2\), \(w=\omega-1/2\). The exact formula (1) yields
\[
H=4u^2+\pi^2w^2+o(u^2+w^2).
\]
The area of \(4u^2+\pi^2w^2\le s\) is \(s/2\), giving \(F(s)\sim s/2\); differentiating (3) after the natural square-root endpoint rescaling yields \(\rho(s)\to1/2\). Near \(\omega=0\) (the top circle), uniformly in \(x\),
\[
1-H=\pi^2\omega^2+O(\omega^4),
\]
so \(1-F(1-\varepsilon)=2\sqrt\varepsilon/\pi+o(\sqrt\varepsilon)\). Rescaling (3) gives \(\rho(s)\sim1/(\pi\sqrt{1-s})\). No other extremal points contribute.

**5. Sharp regularized inverse mean.** The lower-edge density satisfies \(\rho(s)=1/2+O(\sqrt s)\), as follows from the piecewise-polynomial local expansion and the rescaled integral (3). Splitting \(\int_0^1\rho(s)/(s+\eta)\,ds\) at a fixed small positive level and integrating its constant lower-edge term yields \((1/2)\log(1/\eta)+O(1)\); the logarithmic saddle at \(s=1/4\) is integrable and does not affect this limit.

## Verification
The standalone Python program `verify_b3.py` checks the exact Zak polynomial and identity (1) against the direct finite spline sum on 600,000 deterministic pseudorandom fibers, evaluates the independently derived one-dimensional density formula at interior points, compares it with random-sampling estimates, and checks the predicted saddle and upper-edge asymptotic coefficients. Run `python3 verify_b3.py` with NumPy and SciPy installed; `verification_output.txt` contains its actual output. These finite computations are supplementary: the unconditional statements are proved in Steps 1–5, and no finite sampling is invoked as a completeness argument.

## Relationship to prior work
Kloos and Stöckler's 2013 paper establishes the Zak-zero and Gabor-frame framework for exponential B-splines, and explicitly discusses polynomial spline Zak transforms. Kloos (2014) develops zero uniqueness for totally positive windows. Their established Zak theory explains the critical non-frame endpoint; neither inspected analysis calculates the pushforward spectral measure or the interior logarithmic singularity and coefficient for the *quadratic cardinal spline*. Earlier B-spline frame results concern threshold frame membership or optimal frame bounds at **different lattice densities** or for the order-two tent spline, not this order-three critical spectral density. The present work does not claim Zak fiberization or spline polynomial identities themselves as novel.

## Limitations
The law applies only to the centered quadratic cardinal spline and the lattice with both steps exactly one, with the specific (unit-integral) window normalization. The normalized spectral measure is a torus-fiber average and is not an ordinary trace on \(L^2(\mathbb R)\). The density is unbounded but locally integrable at the saddle level; the operator is not an invertible frame operator. Related recent B-spline Zak-zero research had accessible abstracts but unavailable full text, creating a residual literature-priority risk; mathematically equivalent older density-of-states calculations cannot be ruled out by search absence. No independent mathematical audit has been performed.

## References
1. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (first public 2013-11-28), https://arxiv.org/pdf/1311.7359.
2. T. Kloos, *Zeros of the Zak transform of totally positive functions*, arXiv:1411.1539v1 (2014-11-06), https://arxiv.org/pdf/1411.1539.
3. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116v1 (2026-09-11), https://arxiv.org/abs/2609.13116 (abstract available).
4. A. Stangl and C. Frederick, *The frameset of the second-order B-spline along \(ab=1/q\)*, arXiv:2609.00481v1 (first public 2026-08-31), https://arxiv.org/abs/2609.00481.
5. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Applied and Computational Harmonic Analysis 4 (1997), 188–221.
