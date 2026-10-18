# Sharp global invertibility threshold and basin geometry of a cosine normal-return map

## Finding

Fix an inner unit disk and the smooth outer polar curve
\[
 X_{\varepsilon}(\theta)=(3+\varepsilon\cos(2\theta))(\cos\theta,\sin\theta),
 \qquad 0<\varepsilon<2/5.
\]
For each input angle \(\theta\), travel radially from the unit circle to \(X_{\varepsilon}(\theta)\), then follow the inward outer normal to its **first** encounter with the inner unit circle. Denote the output angle by \(F_{\varepsilon}(\theta)\). This defines a real-analytic circle map throughout the indicated range. Define
\[
 \varepsilon_{\mathrm c}=\frac{\sqrt{97}-7}{8}=0.3561072252245\ldots.
\]
**Sharp trichotomy:** For \(0<\varepsilon<\varepsilon_{\mathrm c}\), the return map is an orientation-preserving real-analytic circle diffeomorphism. At \(\varepsilon=\varepsilon_{\mathrm c}\), it is an orientation-preserving real-analytic circle homeomorphism but not a \(C^1\) diffeomorphism: its derivative vanishes precisely at the two radial thickness maxima. For \(\varepsilon_{\mathrm c}<\varepsilon<2/5\), the map is noninjective even though those same two maxima remain linearly attracting, with multipliers strictly between \(-1\) and \(0\).

In the homeomorphism range, there are exactly four fixed points, at angles \(0,\pi/2,\pi,3\pi/2\). The two maxima \(0,\pi\) attract every orbit other than the two fixed repellers \(\pi/2,3\pi/2\). More precisely, every nonfixed initial angle in \((-\pi/2,\pi/2)\) converges to \(0\) modulo \(2\pi\), and every nonfixed initial angle in \((\pi/2,3\pi/2)\) converges to \(\pi\). The corresponding basins are exactly these open semicircles.

## Assumptions and scope

All angles lie in \(\mathbb R/2\pi\mathbb Z\). The core has radius one; the outer polar radius is \(R(\theta)=3+\varepsilon\cos(2\theta)\), and \(p(\theta)=R'(\theta)=-2\varepsilon\sin(2\theta)\). The outer domain is strictly convex: its polar curvature numerator satisfies
\[
 R^2+2p^2-RR''\ge(13/5)^2-(17/5)(8/5)>0
\]
throughout \(0<\varepsilon<2/5\). Also \(R>13/5\) and \(|p|<4/5\). In particular, each inward normal ray from the outer boundary intersects the unit disk transversely at two points, and its first entry point defines the smooth return map; no dynamical assertion relies on sufficient small-slope hypotheses from the literature.

## Proof

**1. Exact normal geometry.** In the polar frame \((e_r,e_\theta)\) at \(\theta\), the outward normal to the outer curve is \((R e_r-p e_\theta)/\sqrt{R^2+p^2}\). The signed distance from the origin to its normal line is \(Rp/\sqrt{R^2+p^2}\), of absolute value less than one because \(|p|<1\). Elementary intersection geometry gives the unique degree-one continuous angular lift
\[
 f(\theta)=\theta-\arctan\frac pR+
 \arcsin\frac{Rp}{\sqrt{R^2+p^2}},
 \qquad f(\theta+2\pi)=f(\theta)+2\pi.
\]
The arguments of both inverse trigonometric functions stay strictly inside their analytic domains. Define
\[
 W=\sqrt{R^2-(R^2-1)p^2}>0.
\]
Differentiation, then rationalization of the coefficient of \(R''\), gives the **exact derivative**
\[
 f'=1+R''\frac{R(R^2-1)}{W(R^2+W)}
 +\frac{p^2(W+p^2)}{W(R^2+p^2)}.\tag{1}
\]
The final term is nonnegative and is positive whenever \(p\ne0\).

**2. A global inequality with the sharp equality case.** Set \(u=\cos(2\theta)\). If \(u\le0\), then \(R''=-4\varepsilon u\ge0\), and both nonconstant terms in (1) are nonnegative. Hence \(f'>0\) in this region. For \(0\le u\le1\), put \(v=4\varepsilon^2(1-u^2)=p^2\) and
\[
 K=R^2-(R^2-1)4\varepsilon^2,\qquad c=\frac{R}{R+2},
 \qquad Z=Ru+c(1-u).
\]
Because \(R\in[3,17/5)\), the elementary uniform inequality
\[
 4\varepsilon^2<\frac{16}{25}<\frac{R^2}{(R-1)(R+2)}
\]
holds. To check the second comparison without decimals, the right-hand rational function decreases on \([3,17/5]\) and at its right endpoint equals \(289/324>16/25\). Thus \(K/R\ge c\). Furthermore,
\[
 W^2=R^2u^2+K(1-u^2),\qquad W\le R,
\]
so by difference of squares
\[
 W-Ru=\frac{K(1-u^2)}{W+Ru}
 \ge\frac KR(1-u)\ge c(1-u).
\]
Consequently \(W\ge Z\). Direct expansion yields the exact factorization
\[
 Z(R^2+Z)-uR^2(R+1)=(R-c)^2(1-u)^2\ge0.
\]
It follows that
\[
 u\frac{R(R^2-1)}{W(R^2+W)}\le\frac{R-1}{R}
 \le\frac{2+\varepsilon}{3+\varepsilon}.
\]
Since \(R''=-4\varepsilon u\), (1) therefore gives a **uniformly sharp** lower bound
\[
 f'(\theta)\ge1-\frac{4\varepsilon(2+\varepsilon)}{3+\varepsilon}.\tag{2}
\]
Equality in (2) is possible exactly when \(u=1\), i.e. \(\theta=0,\pi\), where \(p=0\); there (1) indeed gives equality. For \(u<1\), the bound is strict (because the positive last term, or the strict difference-of-squares bound).

**3. Exact global transition.** The right side of (2) is zero precisely when \(4\varepsilon^2+7\varepsilon-3=0\), giving the stated \(\varepsilon_{\mathrm c}\). Below it, the lift derivative is strictly positive, hence the degree-one lift is a real-analytic circle diffeomorphism. At equality it is nonnegative and vanishes only at two isolated angles, so it remains strictly increasing and defines a homeomorphism, while its inverse cannot be \(C^1\) at the corresponding critical values. Above the threshold the derivative is negative at \(\theta=0,\pi\) but positive at \(\theta=\pi/2,3\pi/2\). A degree-one circle map with this sign change is noninjective. The multipliers at maxima and minima are respectively
\[
 \Lambda_+=1-\frac{4\varepsilon(2+\varepsilon)}{3+\varepsilon},
 \qquad
 \Lambda_-=1+\frac{4\varepsilon(2-\varepsilon)}{3-\varepsilon}.
\]
For \(\varepsilon_{\mathrm c}<\varepsilon<2/5\), the first lies in \((-1,0)\) (indeed the subtracted fraction is \(<\frac85\cdot\frac{12}{5}\cdot\frac13=\frac{32}{25}<2\)); the second is greater than one.

**4. Fixed points and basins.** When \(p>0\), one has
\[
 \arcsin\frac{Rp}{\sqrt{R^2+p^2}}>
 \arctan\frac pR>0
\]
because \(R>1\), and both inverse sines lie in their principal branch. The inequalities reverse when \(p<0\). Hence \(\operatorname{sgn}(f(\theta)-\theta)=\operatorname{sgn}(p(\theta))\), so exactly the four angles \(\sin2\theta=0\) are fixed. For \(\varepsilon\le\varepsilon_{\mathrm c}\), monotonicity of the lift makes each interval between successive fixed points invariant; on each such interval the displacement has a fixed sign. Iteration thus converges monotonically to the adjacent maximum, except at the repelling minimum itself. This proves the asserted exact basin partition even at the homeomorphism endpoint.

## Verification

The accompanying standard-library `verify.py` checks the rational factorization and sufficient inequalities at numerous exact-rational parameter points; compares (1) to independent finite differences of the explicit angular lift; tests geometric transversality and positive curvature; and checks finite-grid signs, sample convergence, and multiplier signs on both sides of the threshold. Running the actual script returned **18,228 finite diagnostics passed** and the critical numerical value \(0.356107225224513\). Exact real-parameter claims are established by the preceding inequalities and topology, not by the finite tests.

## Relationship to prior work

Barkatou and El Morsalani, arXiv:2603.30010v2, Section 9.1, give the cosine thickness model and **local** fixed-point multipliers and explicitly distinguish these from independent global geometric hypotheses. Their companion arXiv:2603.28453v4, Sections 9.1–9.4, writes an exact angular return formula, gives sufficient global ascent criteria, and reports **numerical** regimes; arXiv:2603.28445 establishes general fixed-point and linearization identities. These known formulas are acknowledged. The additional conclusion here is the sharp **global injectivity/homeomorphism threshold** for a fully specified strictly convex cosine family, including a proof that no derivative zero occurs away from the extrema, its sharp endpoint classification, and its full subcritical basin structure. The result is not a new general local-multiplier identity. An earlier equivalent special calculation outside the inspected literature remains possible.

## Limitations

This is a theorem about one explicit planar unit-core, frequency-two, radial-baseline-two family with \(0<\varepsilon<2/5\); it does not establish sharp thresholds for general baseline thickness, harmonic frequencies, other convex cores, or parameter amplitudes beyond the stated range. In the noninjective region only the folding and local hyperbolicity conclusions are asserted; there is no global chaos or basin classification there. The strict-convexity and first-intersection geometry are verified directly; membership in any more restrictive externally defined domain class is not required. Finite diagnostic checks are not a computer-assisted proof. Bibliographic priority has not been independently audited.

## References

1. M. El Morsalani and M. Barkatou, *Geometry, Dynamics, and Topology of the Thickness Landscape: A Morse-Theoretic Analysis of the Return Map in the Class O_C*, arXiv:2603.30010, first submitted 31 March 2026; version 2, 8 October 2026. https://arxiv.org/abs/2603.30010
2. M. El Morsalani and M. Barkatou, *Global Convergence Regimes of the Return Dynamics in the Class O_C*, arXiv:2603.28453, particularly Sections 9.1–9.4. https://arxiv.org/abs/2603.28453
3. M. El Morsalani and M. Barkatou, *The Return Map in the Class O_C: Geometry, Dynamics, and Thickness Regularity*, arXiv:2603.28445, Sections 6–7. https://arxiv.org/abs/2603.28445
