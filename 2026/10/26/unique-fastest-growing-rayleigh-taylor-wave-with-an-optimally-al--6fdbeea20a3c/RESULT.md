# Unique fastest-growing Rayleigh–Taylor wave with an optimally allocated two-fluid column

## Finding

For two inviscid fluids of unequal densities confined between rigid horizontal walls, fixing the **sum** of their positive depths and allowing the dividing interface to move yields a unique joint maximizer of the linear Rayleigh–Taylor growth rate over both interface placement and horizontal wavenumber. The heavier fluid must occupy strictly more than half of the available height, but less than its square-root-density share. The optimized dispersion relation admits an exact scalar reduction and a globally unique fastest mode.

Precisely, fix densities \(a>b>0\) (heavy upper, light lower), total height \(L>0\), gravitational acceleration \(g>0\), and interfacial tension \(\sigma>0\). Put \(G=(a-b)g\) and \(k_c=\sqrt{G/\sigma}\). For upper depth \(h\in(0,L)\), lower depth \(L-h\), and unstable horizontal wavenumber \(k\in(0,k_c)\), the positive growth exponent \(\Gamma(k,h)\) obeys
\[
\Gamma(k,h)^2=\frac{k(G-\sigma k^2)}{a\coth(kh)+b\coth(k(L-h))}.
\]

**Exact optimal depth allocation at a prescribed wavenumber.** For every \(k>0\), the denominator has the unique minimum
\[
D_*(k)=(a+b)\coth(kL)+2\sqrt{ab}\,\operatorname{csch}(kL),
\]
attained precisely at \(h=h_*(k)\) satisfying
\[
\frac{\sinh(kh_*(k))}{\sinh(k(L-h_*(k)))}=\sqrt{\frac ab}.
\]
Writing \(r=\sqrt{a/b}>1\) and \(S=kL\), the explicit optimal fraction is
\[
\frac{h_*(k)}L=\frac{1}{2S}\log\frac{1+r e^S}{1+r e^{-S}},\qquad
\frac12<\frac{h_*(k)}L<\frac{\sqrt a}{\sqrt a+\sqrt b}.
\]
The fraction decreases strictly as \(S\) increases; its endpoints are sharp as \(S\to\infty\) and \(S\to0\), respectively. For the equal-depth allocation, its denominator differs by the exact positive amount
\[
D_{\mathrm{equal}}(k)-D_*(k)=(\sqrt a-\sqrt b)^2\operatorname{csch}(kL)>0.
\]
Thus the optimized split improves growth strictly at every unstable wavenumber.

**Unique joint optimum.** There is exactly one pair \((k_*,h_*)\in(0,k_c)\times(0,L)\) maximizing the growth rate, with \(h_*=h_*(k_*)\). Define \(c=2\sqrt{ab}/(a+b)\in(0,1)\) and
\[
E(S)=1+\frac{S(1+c\cosh S)}{\sinh S(\cosh S+c)}.
\]
Then \(k_*\) is the unique solution of
\[
\frac{2k_*^2}{k_c^2-k_*^2}=E(k_*L),
\]
and satisfies the sharp universal bounds
\[
\frac{k_c}{\sqrt3}<k_*<\frac{k_c}{\sqrt2}.
\]
As total height \(L\) increases, \(k_*\) decreases strictly while the maximum growth exponent increases strictly.

**Sharp depth limits.** As \(L\downarrow0\),
\[
 k_*\longrightarrow \frac{k_c}{\sqrt2},\quad
 \frac{h_*}{L}\longrightarrow\frac{\sqrt a}{\sqrt a+\sqrt b},\quad
 \frac{\Gamma_{\max}^2}{L}\longrightarrow
 \frac{\sigma k_c^4}{4(\sqrt a+\sqrt b)^2}.
\]
As \(L\to\infty\),
\[
 k_*\longrightarrow\frac{k_c}{\sqrt3},\quad
 \frac{h_*}{L}\longrightarrow\frac12,\quad
 2h_*-L\longrightarrow\frac{1}{2(k_c/\sqrt3)}\log\frac ab,
\]
while
\[
\Gamma_{\max}^2\longrightarrow\frac{2\sigma k_c^3}{3\sqrt3(a+b)}.
\]
These are limits along fixed densities, acceleration, and surface tension.

## Assumptions and scope

Both fluids are homogeneous, immiscible, incompressible and inviscid; the upper fluid is heavier. Their base state is motionless, with a plane internal interface and impermeable rigid walls at the top and bottom. Perturbations are infinitesimal, horizontally sinusoidal, irrotational, and are assessed by their positive linear normal-mode growth rate. The total wall-to-wall distance \(L\), the two densities \(a,b\), \(g\), and \(\sigma\) are fixed. The interface depth \(h\) is freely allocated in the open interval \((0,L)\). Horizontal wavenumbers form a continuum; no finite lateral domain is imposed. All optimization statements concern positive unstable modes \(0<k<k_c\).

## Proof

**1. Dispersion law and cutoff.** With the interface at vertical coordinate zero, each velocity potential solves the separated Laplace equation with horizontal wavenumber \(k\) and zero normal derivative at its rigid wall. Hence the vertical dependence is a scaled hyperbolic cosine in each fluid. The linearized kinematic condition sets the common interface normal velocity to \(\partial_t\eta\); the linearized pressure-jump condition sets its difference to \(G\eta-\sigma k^2\eta\), with the signs corresponding to a heavy-over-light configuration. Eliminating potential amplitudes yields
\[
\Gamma^2\big[a\coth(kh)+b\coth(k(L-h))\big]=k(G-\sigma k^2).
\]
The bracket is positive. Thus exponentially growing modes exist exactly for \(0<k<k_c\); the stated expression is their positive squared growth rate. This forward dispersion relation is classical and is not claimed as new.

**2. Exact depth optimization.** Set \(x=kh\), \(y=k(L-h)\), and \(S=x+y=kL\). Using the addition formula for \(\coth\),
\[
\coth x=\coth S+\frac{\sinh y}{\sinh x\,\sinh S},\qquad
\coth y=\coth S+\frac{\sinh x}{\sinh y\,\sinh S}.
\]
Consequently, for \(t=\sinh y/\sinh x>0\),
\[
 D(k,h)=(a+b)\coth S+\frac{at+b/t}{\sinh S}
 \ge(a+b)\coth S+2\sqrt{ab}\,\operatorname{csch} S.
\]
The inequality is the arithmetic–geometric mean inequality, with equality precisely when \(t=\sqrt{b/a}\). As \(h\) rises from zero to \(L\), \(t\) decreases continuously and strictly from infinity to zero, so equality occurs at one and only one \(h=h_*(k)\). Rearranging the equality equation gives
\[
 e^{2kh_*}=\frac{1+r e^{kL}}{1+r e^{-kL}},\quad r=\sqrt{a/b},
\]
which proves the closed allocation formula. Since \(r>1\), the ratio of hyperbolic sines forces \(kh_*>k(L-h_*)\), hence \(h_*/L>1/2\).

To prove the upper fraction bound and strict scale monotonicity, put \(p=h_*/L\in(1/2,1)\). The equality condition becomes
\[
 F(p,S)=\log\sinh(pS)-\log\sinh((1-p)S)=\log r.
\]
Here \(F_p=S[\coth(pS)+\coth((1-p)S)]>0\). Also
\[
 SF_S=(pS)\coth(pS)-((1-p)S)\coth((1-p)S)>0
\]
because \(z\mapsto z\coth z\) is strictly increasing on \((0,\infty)\), as \(\sinh z\cosh z>z\). The implicit derivative \(dp/dS=-F_S/F_p\) is strictly negative. Since the small-\(S\) equality becomes \(p/(1-p)=r\) and the large-\(S\) equality gives \((2p-1)S\to\log r\), its two limits are \(r/(1+r)\) and \(1/2\). The exact equal-depth deficit follows from \(\coth(S/2)=\coth S+\operatorname{csch}S\) and \((a+b)-2\sqrt{ab}=(\sqrt a-\sqrt b)^2\).

**3. Strict monotonicity of the spectral elasticity.** Let positive coefficients \(\alpha_j\) and depths \(d_j\) define \(D(k)=\sum_j\alpha_j\coth(kd_j)\). Put
\[
 w_j=\frac{\alpha_j\coth(kd_j)}{D(k)},\qquad
 q_j=\frac{2kd_j}{\sinh(2kd_j)}.
\]
Then \(w_j>0\), \(\sum_jw_j=1\), \(0<q_j<1\), and
\[
 E_D(k):=\frac{d}{d\log k}\log\frac{k}{D(k)}=1+\sum_jw_jq_j.
\]
Each \(q(z)=2z/\sinh(2z)\) strictly decreases for \(z>0\), since \(\tanh(2z)<2z\). Differentiating with respect to \(\log k\) gives the exact identity
\[
\frac{d}{d\log k}(E_D-1)
=\sum_j w_j\frac{dq_j}{d\log k}
 -\sum_jw_j\left(q_j-\sum_mw_mq_m\right)^2<0.
\]
The second term is a nonnegative variance and the first is strictly negative, proving \(1<E_D(k)<2\), strict decrease, and limits \(E_D\to2\) as \(k\to0\), \(E_D\to1\) as \(k\to\infty\).

In particular, with \(c=2\sqrt{ab}/(a+b)\), the optimal denominator has the positive-mixture representation
\[
D_*(k)=(a+b)[(1-c)\coth(kL)+c\coth(kL/2)].
\]
Applying the preceding lemma yields a strictly decreasing \(E_D(k)=E(kL)\) and elementary differentiation of \(D_*\) gives exactly the displayed formula for \(E(S)\).

**4. Global uniqueness, bounds, and height dependence.** Because
\[
\Gamma_*(k)^2=\frac{\sigma k(k_c^2-k^2)}{D_*(k)},
\]
its logarithmic derivative with respect to \(\log k\) is
\[
 E(kL)-\frac{2k^2}{k_c^2-k^2}.
\]
The first term strictly decreases, whereas the second strictly increases from zero to infinity on \((0,k_c)\). The derivative is therefore positive before exactly one crossing and negative after it. Moreover \(\Gamma_*(k)^2\) tends to zero at both endpoints, so the crossing is the unique global peak. Step 2 supplies the unique interface position for every \(k\), establishing uniqueness of the **joint** optimum. At the crossing, \(1<E<2\) implies \(1/3<k_*^2/k_c^2<1/2\), proving the strict, sharp wavenumber bounds.

For fixed \(k\), the formula for \(D_*(k)\) is strictly decreasing in \(L\); thus the optimized growth at every \(k\), and in particular its global maximum, strictly increases with \(L\). The stationarity equation depends on \(k,L\) through \(E(kL)\). The implicit derivative has negative numerator (\(E'<0\)) and strictly negative denominator (\(LE'(kL)-d[2k^2/(k_c^2-k^2)]/dk<0\)), so \(dk_*/dL<0\).

**5. Sharp shallow and deep limits.** The strictly bounded sequence \(k_*(L)\in(k_c/\sqrt3,k_c/\sqrt2)\) and the monotonic elasticity limits imply \(k_*\to k_c/\sqrt2\) as \(L\downarrow0\), and \(k_*\to k_c/\sqrt3\) as \(L\to\infty\). The allocation-fraction limits in Step 2 then apply at \(S=k_*(L)L\); the large-depth difference follows from \(k_*(2h_*-L)=2kh_*-kL\to\log r=\frac12\log(a/b)\). Finally, uniformly for \(k\) bounded away from zero,
\[
D_*(k)\sim\frac{(\sqrt a+\sqrt b)^2}{kL}\quad(L\downarrow0),\qquad
D_*(k)\longrightarrow a+b\quad(L\to\infty).
\]
Inserting the respective limiting maximizing wavenumbers into \(\Gamma_*^2\) yields both asserted maximum-growth limits. Strict inequalities and the two attainability limits make the wavenumber bounds sharp.

## Verification

The accompanying standalone `verify.py` independently minimizes the unoptimized denominator over interface position, compares the exact optimized denominator and split against numerical optimization, checks the unique wavenumber via a separate bounded scalar maximization, tests strict improvements over equal-depth placements, and checks both asymptotic regimes for positive parameter samples. Its printed assertions are finite numerical checks, not the proof of the continuum-wide and strict inequalities above. Run with `python verify.py` using Python 3, NumPy, and SciPy.

## Relationship to prior work

Mikaelian's 1990 paper derives the general multi-fluid capillary Rayleigh–Taylor eigenvalue problem and the fixed-wall two-fluid case; its existing dispersion relation contains the forward formula used here. The author's accessible 1996 full-text paper reproduces that inviscid two-depth relation explicitly as equation (2), and studies finite-depth and viscous growth-rate curves. Neither the dispersion relation itself nor the familiar infinite-depth fastest wavenumber is claimed as new. The result assessed here instead optimizes the *placement of the internal interface at fixed total depth* simultaneously with the wavelength: the exact square-root-weighted split, positive-cotangent reduction, strict uniqueness in two control variables, improvement over equal placement, and sharp limits constitute the asserted contribution.

The 1990 paper's full text was not accessible in the available sources; only the publisher's detailed abstract could be examined, so specialized previously published optimization statements cannot be completely excluded. The 1996 author's full-text version was examined through its linear-dispersion section, approximate-dispersion section, figure discussion, and references, without finding the fixed-total-depth allocation classification.

## Limitations

This is an exact **linear** instability result for inviscid, incompressible fluid layers between impermeable flat rigid walls. Altering the allocation while keeping total height fixed also changes the total mass per horizontal area; no separate mass or volume constraints are imposed. No claim is made about viscous/no-slip behavior, diffusion, nonlinear plume dynamics, capillary contact-angle effects, finite horizontal domains with discrete wavenumbers, or robustness to parameter uncertainty. The historical-priority comparison is not exhaustive because the highly relevant 1990 paper's complete text could not be read.

## References

1. K. O. Mikaelian, “Rayleigh–Taylor and Richtmyer–Meshkov instabilities in multilayer fluids with surface tension,” *Physical Review A* **42**, 7211–7225 (1990), DOI: 10.1103/PhysRevA.42.7211; first verified public date 1990-12-01.
2. K. O. Mikaelian, “Rayleigh–Taylor instability in finite-thickness fluids with viscosity and surface tension,” *Physical Review E* **54**, 3676–3680 (1996), DOI: 10.1103/PhysRevE.54.3676; available author-uploaded full text, specifically equation (2), Sections I–III, and references.
3. S. Chandrasekhar, *Hydrodynamic and Hydromagnetic Stability* (Clarendon, 1961), chapter X, for the classical inviscid gravity-interface instability framework.
