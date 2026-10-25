# Sharp split stability and unbounded stage transients for three-node FIMEX-Radau

## Finding

For the uniterated three-node FIMEX-Radau propagator [1], the entire nonnegative real split-stability region is an explicit sharp strip. With normalized implicit and explicit damping \(s=ra\) and \(t=rb\), its complete block matrix is power bounded **if and only if**
\[
0\le t\le T(s),\qquad T(s)=s+\frac72-\frac12\sqrt{24s+37},\qquad s\ge0.
\]
Except at the zero split, strict spectral contraction holds precisely when \(t<T(s)\); at the upper edge a simple eigenvalue is \(-1\). The stiff-implicit upper edge has a nonconstant square-root deficit,
\[
T(s)=s-\sqrt{6s}+\frac72+O(s^{-1/2}).
\]
Even well inside this spectral-stability region, the active block stages need not contract in Euclidean norm. At any fixed ratio \(t=cs\) with \(0<c<1\), the large-\(s\) matrix becomes a defective scalar multiple of a Jordan block. Its exact limiting peak amplification satisfies
\[
\lim_{c\uparrow1}(1-c)\sup_{n\ge0}\|(cJ)^n\|_2=\frac3e.
\]
Consequently, **no finite common bound** exists on the Euclidean power norms over all strictly spectrally stable finite nonnegative splits. This concerns perturbations of the method's two-component stage vector, not a worst-case estimate for the scalar endpoint output under specially consistent initialization.

## Assumptions and scope

Fix physical step \(h=2r>0\), and the scalar split initial-value problem
\[
y'=f^{\mathrm{imp}}(y)+f^{\mathrm{exp}}(y),\qquad
f^{\mathrm{imp}}(y)=-ay,\quad f^{\mathrm{exp}}(y)=-by,\quad a,b\ge0.
\]
Use precisely the three-node FIMEX-Radau propagator with no additional iterator, as defined in [1, equation (45)]; **not** FIMEX-Radau* or the composite method with positive iterator count. Its three values are associated with nodes \(-1,-1/3,1\); the first output repeats the previous third input. All matrix norms here are ordinary Euclidean operator norms of the indicated vector of **block stage values**, and all conclusions concern exact-arithmetic constant scalar coefficients.

Write \(s=ra\), \(t=rb\) and \(d(s)=2s^2+4s+3>0\). Because the first previous-stage coordinate is unused, the active two-coordinate block update is
\[
\begin{pmatrix}y_2^{[n+1]}\\y_3^{[n+1]}\end{pmatrix}
=B(s,t)\begin{pmatrix}y_2^{[n]}\\y_3^{[n]}\end{pmatrix},
\quad B(s,t)=\frac1{2d(s)}\begin{pmatrix}
t(2s+1)&-6st+4s-5t+6\\
3t(2s+3)&-10st-4s-21t+6
\end{pmatrix}.
\]
The complete three-stage matrix has its first row \((0,0,1)\) and its last two rows equal to the last two rows of \(B\) with an initial zero; thus its eigenvalues are \(0\) together with those of \(B\). Power boundedness at possible unit-modulus eigenvalues is addressed explicitly below.

## Proof

**1. Exact reduction from the defining method.** In [1, equation (45)], put the scaled implicit component at an output equal to \(-s\) times that output and the scaled explicit component at an input equal to \(-t\) times that input. Writing \(x=y_2^{[n]}\), \(y=y_3^{[n]}\), the last two outputs \(X,Y\) solve the uniquely invertible system
\[
\begin{pmatrix}1+5s/6&-s/6\\3s/2&1+s/2\end{pmatrix}
\begin{pmatrix}X\\Y\end{pmatrix}
=\begin{pmatrix}y+t(x-5y)/6\\y+t(3x-7y)/2\end{pmatrix}.
\]
The determinant is \(d(s)/3>0\). Direct inversion produces the displayed \(B(s,t)\). In particular its characteristic polynomial is \(\lambda^2-\tau\lambda+\Delta\), with
\[
\tau=\operatorname{tr}B=-\frac{4st+2s+10t-3}{d(s)},\qquad
\Delta=\det B=\frac{2t(t-2)}{d(s)}.
\]

**2. Complete sharp stability classification.** For a real monic quadratic, both roots lie in the open unit disk precisely when \(1-\tau+\Delta>0\), \(1+\tau+\Delta>0\), and \(1-\Delta>0\) (the degree-two Jury criterion). Here exact algebra gives
\[
\begin{aligned}
1-\tau+\Delta&=\frac{2(s+t)(s+t+3)}{d(s)},\\
1+\tau+\Delta&=\frac{2((s-t)^2+s-7t+3)}{d(s)},\\
1-\Delta&=\frac{2s^2+4s+3-2t^2+4t}{d(s)}.
\end{aligned}
\]
The middle numerator, regarded as a quadratic in \(t\), has the two roots
\[
T(s)=s+\frac72-\frac12\sqrt{24s+37},\quad
U(s)=s+\frac72+\frac12\sqrt{24s+37}.
\]
The determinant condition is equivalent, for \(t\ge0\), to \(t<P(s)\), where
\[
P(s)=1+\sqrt{s^2+2s+\frac52}.
\]
For every \(s\ge0\),
\[
0<T(s)<P(s)<U(s).
\]
Indeed, \((2s+7)^2-(24s+37)=4(s^2+s+3)>0\) proves positivity. Since \(\sqrt{24s+37}\ge\sqrt{37}>6\), one has \(T(s)<s+1/2\), whereas \(P(s)>s+2\) and \(U(s)>s+13/2\); also \(P(s)<s+7/2\) since \(\sqrt{(s+1)^2+3/2}<s+5/2\). Thus all the strict Jury inequalities hold exactly for \(0\le t<T(s)\) except at \((s,t)=(0,0)\), where the first expression vanishes. For \(T(s)<t<P(s)\) the middle expression is negative, and for \(t\ge P(s)\) the determinant condition fails (and the preceding middle condition is negative at equality); hence the spectral radius exceeds one whenever \(t>T(s)\).

At \(t=T(s)\), the characteristic polynomial has root \(-1\). The first and third Jury expressions are strictly positive there, so the other eigenvalue lies strictly between \(-1\) and \(1\); hence \(-1\) is simple and the matrix remains power bounded. At the sole zero split, \(B(0,0)=\begin{psmallmatrix}0&1\\0&1\end{psmallmatrix}\), whose eigenvalues \(0,1\) are simple. The full three-stage matrix introduces only a zero eigenvalue and one dependent first coordinate, so it also stays power bounded at all these endpoints. This proves the claimed weak and strict regions, including all boundary cases.

**3. Stiff edge and defective limit.** The explicit expression yields
\[
T(s)=s+\frac72-\sqrt{6s+\frac{37}4}
=s-\sqrt{6s}+\frac72+O(s^{-1/2}).
\]
Fix \(0<c<1\). Because \(T(s)/s\to1\), all sufficiently large finite splits \((s,cs)\) lie strictly within the stable region. Entrywise division of \(B(s,cs)\) by its leading denominator shows
\[
B(s,cs)\longrightarrow cJ,\quad
J=\begin{pmatrix}1/2&-3/2\\3/2&-5/2\end{pmatrix}
=-I+N,\quad
N=\frac32\begin{pmatrix}1&-1\\1&-1\end{pmatrix}.
\]
Direct multiplication gives \(N^2=0\), and the rank-one outer-product representation shows \(\|N\|_2=3\). Hence for every integer \(n\ge0\),
\[
(cJ)^n=(-c)^n(I-nN),\qquad
3n-1\le\|I-nN\|_2\le3n+1.
\]
Let \(M(c)=\sup_{n\ge0}\|(cJ)^n\|_2\). The preceding two-sided bounds imply
\[
\big|M(c)-3\sup_{n\ge0}nc^n\big|\le1.
\]
Elementary maximization on the integers, comparing with the continuous maximum of \(x\mapsto xc^x\), gives \((1-c)\sup_{n\ge0}nc^n\to e^{-1}\) as \(c\uparrow1\). Thus \((1-c)M(c)\to3/e\).

For each arbitrarily large prescribed norm bound, choose \(c<1\) and a **finite** integer \(n\) for which \(\|(cJ)^n\|_2\) exceeds twice that bound. Then select a sufficiently large but finite \(s\) so that \(cs<T(s)\) and \(B(s,cs)^n\) is close enough to \((cJ)^n\) to retain the bound. Therefore no uniform Euclidean power bound exists over the strictly stable finite splits. This argument makes no claim that a single fixed finite split has unbounded powers.

## Verification

The standalone file `fimex_radau3_verifier.py` independently evaluates the published stage equations with exact rational arithmetic and compares them against the closed-form \(B(s,t)\); it checks the trace, determinant, and all three stability polynomials over a rational grid. It also checks representative endpoint ordering, the stiff matrix limit, the nilpotent identity, and numerical convergence toward \(3/e\). To reproduce, run `python3 fimex_radau3_verifier.py` with the Python standard library. Every infinite and uniform assertion above follows from the algebraic proof, not from the finite grid or floating-point experiments.

## Relationship to prior work

Buvoli and Southworth [1] introduced the FIMEX-Radau methods, published the defining coefficients in equation (45), and characterized general split stability by a spectral-radius region in section 5.3; their displayed experiments emphasize larger composite variants. The stability-matrix reduction uses their method and the standard quadratic Jury criterion, neither claimed new here. What is established here is the **explicit necessary-and-sufficient three-node real damping frontier including power-bounded edges**, together with its stiff square-root penalty and the separate nonnormal, unbounded stage-transient phenomenon. Cardone, Jackiewicz, Sandu and Zhang [2] give a general extrapolation-based IMEX general-linear-method stability framework, but their inspected methods and stability formulas do not specialize to the coefficients of [1, equation (45)] or state this frontier and transient law. Generic facts about Jordan blocks are also not novel; the nonstandard claim is that this particular published FIMEX propagator approaches the exhibited defective block *inside its scalar spectral-stability region*.

## Limitations

The classification applies to the uniterated three-node FIMEX-Radau propagator and nonnegative **real** damping splits only. It does not describe complex split spectra, nonlinear systems, noncommuting matrices, other node counts, or compositional iterators. The Euclidean transient is a block-stage perturbation effect, not a claim of physical scalar-solution growth under consistently initialized stages. The limiting \(cJ\) matrices are reached only as the implicit damping parameter tends to infinity; the proof separately constructs large **finite** stable splits with arbitrarily large finite transient. Related unindexed exact calculations may exist; publication priority is not independently established.

## References

[1] T. Buvoli and B. S. Southworth, *Additive Polynomial Time Integrators, Part I: Framework and Fully-Implicit-Explicit (FIMEX) Collocation Methods*, arXiv:2109.03317, first public version 2021-09-07, equation (45) and section 5.3. https://arxiv.org/abs/2109.03317 ; published DOI: https://doi.org/10.1137/21M1446988 .

[2] A. Cardone, Z. Jackiewicz, H. Zhang and A. Sandu, *Extrapolation-based implicit-explicit general linear methods*, arXiv:1304.2276, section 4 (2013). https://arxiv.org/abs/1304.2276 .
