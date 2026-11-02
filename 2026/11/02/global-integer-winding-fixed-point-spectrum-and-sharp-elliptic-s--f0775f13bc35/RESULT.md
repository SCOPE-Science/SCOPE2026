# Global integer-winding fixed-point spectrum and sharp elliptic staircase of the biquadratic nontwist map

## Finding

For the biquadratic nontwist map on the full open cylinder, there is a globally countable collection of period-one resonances, with an exact winding-by-winding census, a sharp quartic growth law by action height, and an exact finite elliptic staircase. The critical small-perturbation number of elliptic positive-winding resonances grows with exponent \(4/3\) and has an explicit two-term asymptotic.

Define \(B=a(1-\epsilon)^2/(4\epsilon)\), \(D_m=(1-\epsilon)^2+4\epsilon m/a\), and, whenever real, \(z_{m,\pm}=(1+\epsilon\pm\sqrt{D_m})/(2\epsilon)\). All period-one points lie above \(x=0\) or \(x=1/2\); their action coordinates are \(y=\pm\sqrt{z_{m,\pm}}\) for positive roots and integer windings \(m\). For each \(m\ge1\), exactly four points occur, using only \(z_{m,+}\). At winding zero there are eight points, except four when \(\epsilon=1\). At winding \(-k\), \(k\ge1\), there are eight points if \(k<B\), four if \(k=B\), and none if \(k>B\).

For \(Y\ge\max\{1,\epsilon^{-1/2}\}\), the exact count in \(|y|\le Y\) is
\[
 N(Y)=C+4\left\lfloor a(1-Y^2)(1-\epsilon Y^2)\right\rfloor,
\]
where \(C=4\) if \(\epsilon=1\) and \(8\) otherwise, **plus** \(8\max\{0,\lceil B\rceil-1\}+4\mathbf1_{\{B\in\mathbb Z_{>0}\}}\). Thus
\[
 N(Y)=4a\epsilon Y^4-4a(1+\epsilon)Y^2+O_{a,\epsilon}(1).
\]

For \(m\ge1\), set \(d_m=\pi a\sqrt{z_{m,+}D_m}\) and \(b_m=d_m^{-1}\). Exactly two of the four winding-\(m\) fixed points are linearly elliptic for \(0<b<b_m\); they are parabolic of trace \(-2\) at equality and hyperbolic for \(b>b_m\). The other two are always hyperbolic. The thresholds \(b_m\) strictly decrease and
\[
 b_m\sim\frac{m^{-3/4}}{2\pi(a\epsilon)^{1/4}}.
\]

Let \(s_b>0\) be the unique solution of
\[
 s_b^2(s_b+1+\epsilon)=\frac{2\epsilon}{\pi^2a^2b^2},
\qquad m_*(b)=\frac{a}{4\epsilon}\bigl(s_b^2-(1-\epsilon)^2\bigr).
\]
The number of **positive-winding indices** supporting two linearly elliptic fixed points is exactly
\[
 M(b)=\max\{0,\lceil m_*(b)\rceil-1\};
\]
there are \(2M(b)\) such fixed points. As \(b\downarrow0\),
\[
 \boxed{M(b)=\frac{b^{-4/3}}{(2\pi)^{4/3}(a\epsilon)^{1/3}}
 -\frac{(1+\epsilon)a^{1/3}b^{-2/3}}{3(2\pi)^{2/3}\epsilon^{2/3}}
 +O_{a,\epsilon}(1).}
\]
All counts are of *fixed points on the cylinder*, not fixed points of a chosen real lift. The winding is the integer lift displacement in the angle coordinate.

## Assumptions and scope

Take \(0<a<1\), \(\epsilon>0\), \(b>0\), and \(D=(\mathbb R/\mathbb Z)\times\mathbb R\). The map is
\[
 y'=y-b\sin(2\pi x),\qquad
 F(x,y)=\bigl(x+\omega(y')\pmod1,\ y'\bigr),
 \quad\omega(y)=a(1-y^2)(1-\epsilon y^2).
\]
A period-one point of winding \(m\in\mathbb Z\) is a cylinder fixed point whose unwrapped angle advances exactly \(m\). A point is *linearly elliptic* if its area-preserving derivative has nonreal conjugate eigenvalues on the unit circle; this does not assert nonlinear/KAM stability. The action height \(Y\) is measured on the full, unbounded mathematical cylinder, not a physically justified radial range of the model's plasma approximation. The auxiliary \(\epsilon=0\) comparison is outside the main theorem's hypotheses.

## Proof

**Complete enumeration.** Since \(b>0\), stationarity of the action means \(\sin(2\pi x)=0\); thus \(x\) is either \(0\) or \(1/2\). Stationarity of the circular angle is equivalent to \(\omega(y)=m\in\mathbb Z\). With \(z=y^2\), this is
\[
 \epsilon z^2-(1+\epsilon)z+1-m/a=0.
\]
Its discriminant is \(D_m\) and its roots are \(z_{m,\pm}\). Because \(0<a<1\), no integer winding equals \(a\), so \(z=0\) is never a root. When \(m\ge1\), \(D_m>(1+\epsilon)^2\), giving one strictly positive root and one negative root, hence four points. At \(m=0\), the roots are \(1\) and \(1/\epsilon\); they coincide exactly when \(\epsilon=1\). For \(m=-k\), the discriminant is positive, zero, or negative as \(k<B\), \(k=B\), or \(k>B\). If it is nonnegative, both roots are strictly positive, including the coincident-root case. This proves all three cases and the finite negative-winding correction \(C\).

**Height growth.** The polynomial \(\omega(y)\) is even and its outer branch is strictly increasing in \(|y|\) for \(|y|>\sqrt{(1+\epsilon)/(2\epsilon)}\). Every zero- or negative-winding fixed point has \(|y|\le\max\{1,\epsilon^{-1/2}\}\), while every positive-winding fixed point is on that outer branch. For the stated \(Y\), exactly the positive integers \(m\le\omega(Y)\) are represented inside \(|y|\le Y\). Every such integer contributes four points. Expanding \(4\omega(Y)\) and using \(-1<\lfloor u\rfloor-u\le0\) gives the exact count and bounded remainder.

**Residue and threshold.** Writing \(c=\cos(2\pi x)\), the derivative at a fixed point is
\[
 DF=\begin{pmatrix}1-2\pi bc\,\omega'(y)&\omega'(y)\\-2\pi bc&1\end{pmatrix},
 \qquad \det DF=1,
\]
and the Greene residue is
\[
 R=\frac{2-\operatorname{tr}DF}{4}=\frac{\pi bc\,\omega'(y)}2.
\]
At the positive-winding action \(y_m=\sqrt{z_{m,+}}\), the derivative \(\omega'(y_m)=2a\sqrt{z_{m,+}D_m}>0\). Hence \(R(0,y_m)=R(1/2,-y_m)=bd_m\), while their symmetric partners have residue \(-bd_m\). The elliptic/parabolic/hyperbolic criterion for determinant-one real two-dimensional matrices yields the stated alternatives. Both \(D_m\) and \(z_{m,+}\) strictly increase, so \(d_m\) increases and \(b_m\) decreases. Since \(D_m\sim4\epsilon m/a\) and \(z_{m,+}\sim\sqrt{m/(a\epsilon)}\), direct substitution yields the asserted \(m^{-3/4}\) threshold law.

**Exact staircase and two-term asymptotic.** Put \(s=\sqrt{D_m}\). Then
\[
 d_m^2=\frac{\pi^2a^2}{2\epsilon}\,s^2(s+1+\epsilon).
\]
The right-hand side is strictly increasing for \(s>0\). The ellipticity condition \(bd_m<1\) is therefore exactly \(m<m_*(b)\). Counting the positive integers with this strict inequality proves the ceiling formula, including at every parabolic threshold. Let
\[
 t=\left(\frac{2\epsilon}{\pi^2a^2b^2}\right)^{1/3}.
\]
The cubic equation gives \(s_b=t-(1+\epsilon)/3+O_{a,\epsilon}(t^{-1})\), so
\[
 m_*(b)=\frac{a}{4\epsilon}t^2-\frac{a(1+\epsilon)}{6\epsilon}t+O_{a,\epsilon}(1).
\]
Substituting \(t\) and noting that ceiling changes the value by less than one yields the displayed two-term \(M(b)\) law.

## Verification

The independent standalone \(verify.py\) evaluates the quadratic identities, symplectic determinant and residue, rational-parameter winding censuses, exact height counts, and numerical checks of the strictly indexed elliptic staircase and its two-term approximation. Run `python verify.py` with SymPy installed. It executes 145 finite checks and reports PASS. All universal statements, sharp thresholds and asymptotic coefficients are proved above; numerical checks are not used as completeness evidence. No external certificate is asserted.

For a reproducible exact example, \(a=1/2\), \(\epsilon=1/4\) gives \(B=9/32\), so there are exactly eight fixed points of nonpositive winding. At \(Y=3\), \(\omega(Y)=5\); the exact count is \(N(3)=8+4\cdot5=28\). An exact fold example is \(a=1/2\), \(\epsilon=5-2\sqrt6\), for which \(B=1\), yielding four coincident-branch negative-one-winding fixed points at \(y=\pm\sqrt{3+\sqrt6}\).

## Relationship to prior work

Grime et al. [1] define precisely this area-preserving cylinder map in their Eq. (10), document its symmetries and give eight distinguished winding-zero fixed points and their residues in their §3. Their focus is the main resonance islands and shearless bifurcation. Their 2023 sequel [2] again gives the winding-zero points in §2 and studies breakup/transport; their 2024 preprint [3] analyzes effective transport barriers on the cylinder. The integer-winding condition is not itself new: Fonseca's 2016 thesis [4, §2.4.1] writes an integer winding equation for a *different* gyro-averaged quartic nontwist map, then specializes to winding zero. The residue criterion is standard [5]. The claim here is the **joint exact global winding census, height growth with bounded remainder, and all-positive-winding ellipticity cutoff with explicit two-term weak-perturbation law** for the BNM. It is not a general theorem for all quartic symplectic maps and is not an assertion that finite literature searches prove priority.

## Limitations

The theorem is a mathematical classification on the full, unbounded cylinder and need not describe physically accessible plasma action heights where the source approximation is valid. Linear ellipticity does not imply nonlinear stability or the persistence of finite-area islands. There may exist earlier calculations of outer resonances or more general counting theorems not found in the inspected literature. The small-\(b\) law holds with fixed strictly positive \(\epsilon\); taking \(\epsilon\to0\) first gives the standard-nontwist twist \(a(1-y^2)\) and **quadratic**, rather than quartic, height growth \(N_0(Y)=4+4\lfloor a(Y^2-1)\rfloor\) for \(Y\ge1\). The theorem does not classify higher-period orbits or their nonlinear stability.

## References

1. G. C. Grime, M. Roberto, R. L. Viana, Y. Elskens, and I. L. Caldas, *Biquadratic Nontwist Map: a model for shearless bifurcations*, arXiv:2209.07408v1, September 15, 2022; *Chaos, Solitons & Fractals* **169** (2023), 113231. https://arxiv.org/abs/2209.07408 ; https://fisica.ufpr.br/viana/artigos/2023/grime2023.pdf
2. G. C. Grime et al., *Shearless curve breakup in the biquadratic nontwist map*, arXiv:2305.17538, 2023. https://portal.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/Grime_CSF2023_0.pdf
3. G. C. Grime et al., *Effective transport barriers in the biquadratic nontwist map*, arXiv:2409.00785, 2024. https://arxiv.org/abs/2409.00785
4. J. D. Fonseca, doctoral thesis, 2016, §2.4.1, *Gyro-averaged quartic nontwist map*. https://teses.usp.br/teses/disponiveis/43/43134/tde-06062016-120807/publico/tesedout.pdf
5. J. D. Meiss, *Symplectic maps, variational principles, and transport*, *Reviews of Modern Physics* **64** (1992), 795–848.
