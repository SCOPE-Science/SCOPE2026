# Two-stage loss of invertibility in the sine-circle nontwist map

## Finding

The sine-circle nontwist family of Mugnaine, Sales, Szezech and Viana has **two explicit analytic criticality surfaces**. Across those surfaces its degree-one lift passes through regimes with zero, two, and four turning points, with an exceptional simultaneous birth of two pairs and a sharp three-halves-power singularity of the second threshold.

For real \(a>0\), \(b>0\), and \(\Omega\in[-1,1]\), define the smooth circle map using its real lift
\[
F_{a,b,\Omega}(x)=x+a\bigl[1-(\Omega-b\sin(2\pi x))^2\bigr],\qquad F(x+1)=F(x)+1.
\]
Write
\[
r=\frac{|\Omega|}{b},\quad q=\sqrt{r^2+8},\quad u_- =\frac{r-q}{4},\quad u_+=\frac{r+q}{4},\quad H(r)=(r-u_-)\sqrt{1-u_-^2}.
\]
For \(0\le r<1\), put \(h(r)=(u_+-r)\sqrt{1-u_+^2}\), while for \(r\ge1\) put \(h(r)=0\). Define
\[
 a_1=\frac{1}{4\pi b^2 H(r)},\qquad
 a_2=\begin{cases}\dfrac{1}{4\pi b^2 h(r)},&0\le r<1,\\[3pt]+\infty,&r\ge1.\end{cases}
\]
These thresholds are positive and \(a_1\le a_2\), with equality exactly when \(r=0\).

**Sharp invertibility criterion.** The induced circle map is an orientation-preserving homeomorphism exactly for \(0<a\le a_1\). For \(a>a_1\) it is not injective.

**Complete critical-point census.** A critical point means a distinct solution of \(F'(x)=0\) modulo one. If \(r>0\), the census is
\[
\begin{array}{c|c}
\text{parameter regime}&\#\{x\bmod1:F'(x)=0\}\\\hline
0<a<a_1&0\\
a=a_1&1\\
a_1<a<a_2&2\\
a=a_2<\infty&3\\
a>a_2,\ a_2<\infty&4.
\end{array}
\]
The rows involving the finite secondary threshold require \(0<r<1\); for \(r\ge1\), \(a_2=\infty\), and exactly two simple critical points persist for every \(a>a_1\). At \(a=a_1\) the unique critical zero has multiplicity two in \(F'\), and when \(a=a_2<\infty\) the third point likewise has multiplicity two while the other two are simple.

At the symmetric parameter \(r=0\), both thresholds coincide at \(a_1=a_2=1/(2\pi b^2)\). The count is zero below, **two distinct double critical zeros** at equality, and **four simple critical zeros** above. Thus the two-turning-point interval disappears exactly at \(\Omega=0\).

**Sharp edge law.** With \(b>0\) fixed, as \(r\uparrow1\),
\[
h(r)=\frac{2\sqrt6}{9}(1-r)^{3/2}\bigl(1+O(1-r)\bigr),\qquad
 a_2=\frac{3\sqrt6}{16\pi b^2}(1-r)^{-3/2}\bigl(1+O(1-r)\bigr).
\]
In particular the secondary fold threshold diverges and disappears for \(r\ge1\). At \(r=1\), \(a_1=1/(3\sqrt3\pi b^2)\).

For fixed \(0<r<1\), each of the two births obeys an explicit square-root splitting. With \(a=a_j(1+\varepsilon)\) and \(\varepsilon\downarrow0\), the coordinate separation of the newly created critical-point pair is
\[
\Delta x_1=\frac{1}{\pi}\sqrt{\frac{2(r-u_-)}q}\,\sqrt\varepsilon+O(\varepsilon),\qquad
\Delta x_2=\frac{1}{\pi}\sqrt{\frac{2(u_+-r)}q}\,\sqrt\varepsilon+O(\varepsilon),
\]
respectively, when each threshold is crossed while other parameters are fixed. The distance here is measured in a sufficiently small circle-coordinate neighborhood of the corresponding critical phase.

## Assumptions and scope

All quantities are real. The circle is \(\mathbb R/\mathbb Z\), and differentiability is that of the degree-one lift. We assume \(a>0\), \(b>0\), and \(|\Omega|\le1\); the same proof applies to any real \(\Omega\). The originating physical paper primarily uses \(0\le a\le1\). The formulas here define analytic threshold surfaces even where a threshold lies above one; for that original domain the census is simply intersected with \(0<a\le1\). The case \(b=0\) is excluded because the lift then is a rigid translation and has no zero derivative. The case \(a=0\) is the identity map and also has no critical points.

A *turning point* is a simple zero of \(F'\), across which the derivative changes sign. A double zero of \(F'\) is instead a cubic stationary inflection of \(F\): at the threshold itself it is critical but not a turning point. The census counts distinct critical points, not multiplicity or critical values. These thresholds describe loss of invertibility, **not** onset of positive Lyapunov exponent or chaos.

## Proof

**1. Sign reduction and derivative.** If \(\Omega<0\), the translation \(x\mapsto x+1/2\) conjugates the map with parameter \(\Omega\) to the map with parameter \(|\Omega|\), because the sine reverses sign. It suffices to take \(\Omega=br\ge0\). With \(t=2\pi x\), \(K=4\pi a b^2>0\), and \(g_r(t)=\cos t\,(r-\sin t)\), differentiation gives
\[
F'(x)=1+K g_r(2\pi x),\qquad
 g_r'(t)=2\sin^2t-r\sin t-1.
\]
Thus the stationary values of \(g_r\) can occur only at \(\sin t=u_-\) and, when \(r\le1\), at \(\sin t=u_+\), where \(u_\pm\) are the two roots of \(2u^2-ru-1=0\). For \(r>0\), \(-1<u_-<0\); \(0<u_+<1\) holds exactly for \(0<r<1\). For \(r=1\), \(u_+=1\), while for \(r>1\) it lies outside the sine range.

**2. Identify the two negative wells.** For \(u_-\), choose the phase whose cosine is negative. Its value is \(-H(r)\). When \(0\le r<1\), choose the phase for \(u_+\) whose cosine is positive. Its value is \(-h(r)\). The other phases at the same sine values give the corresponding positive maxima. The stationarity relation implies
\[
r-u=-\frac{1-u^2}{u},\qquad
|g_r|_{\text{stationary with sine }u}=\frac{(1-u^2)^{3/2}}{|u|}.
\]
For \(0<r<1\), the sum \(u_-+u_+=r/2>0\) shows \(|u_-|<u_+\). The function \(v\mapsto (1-v^2)^{3/2}/v\) decreases strictly on \((0,1)\), so \(0<h(r)<H(r)\). At \(r=0\) the two depths coincide and equal \(1/2\). For \(r\ge1\), there is no secondary negative well: at \(r=1\) the extra stationary phase has \(g_r=0\), never meeting the negative level needed for \(F'=0\).

**3. Count intersections.** The equation \(F'=0\) is exactly \(g_r=-1/K\). As \(a\) increases, the negative level rises from minus infinity toward zero. It first touches \(-H(r)\) at \(K=1/H(r)\), namely \(a=a_1\). Crossing it produces two simple roots. If \(0<r<1\), the level next touches \(-h(r)\) at \(a=a_2\), producing two more; for \(r=0\), the wells have equal depth so both pairs emerge simultaneously. For \(r\ge1\) only the first well occurs. Between extrema the derivative \(g_r'\) has strict sign; therefore there are no additional solutions beyond those counted. At each negative minimum \(g_r''>0\), making each tangency a double zero of \(F'\). More explicitly, with \(q=\sqrt{r^2+8}\),
\[
g_r''=\cos t\,(4\sin t-r),\quad
 g_r''(t_-)=q\sqrt{1-u_-^2},\quad
 g_r''(t_+)=q\sqrt{1-u_+^2}.
\]
The asserted counts and multiplicities follow.

**4. Homeomorphism boundary.** If \(a\le a_1\), then \(F'\ge0\) everywhere and its zeros are isolated, so the lift is strictly increasing. The relation \(F(x+1)=F(x)+1\) makes its circle projection an orientation-preserving homeomorphism. For \(a>a_1\), \(F'\) is negative on a nonempty open arc and positive elsewhere (its mean over one circle period is one). A degree-one circle homeomorphism must have a strictly increasing lift, so this map is not injective. The endpoint \(a=a_1\) is included on the homeomorphism side, despite the derivative-zero inflection.

**5. Edge and local birth.** Set \(\delta=1-r\downarrow0\). A Taylor expansion of the positive stationary sine yields
\[
u_+=1-\frac\delta3+O(\delta^2),\quad
u_+-r=\frac{2\delta}{3}+O(\delta^2),\quad
\sqrt{1-u_+^2}=\sqrt{\frac{2\delta}{3}}\,[1+O(\delta)].
\]
Multiplication gives the stated \(3/2\)-power law for \(h\), and reciprocal inversion gives the law for \(a_2\). At \(r=1\), direct substitution gives \(H(1)=3\sqrt3/4\). Finally, in a nondegenerate well of depth \(m_j\), at \(K=K_j(1+\varepsilon)\) the critical equation becomes \(g_r=-m_j/(1+\varepsilon)\). Taylor expansion about the unique minimizer gives two phase offsets of size \(\sqrt{2m_j\varepsilon/g_r''}+O(\varepsilon)\). Their angular separation divided by \(2\pi\), with \(m_1=H\) and \(m_2=h\), yields the displayed \(\Delta x_j\) formulas. This completes the proof.

## Verification

Run `python3 check_fold_boundaries.py` using the Python 3 standard library. The script reports **144 finite consistency checks**, including derivative finite differences, exact algebraic identities evaluated at parameter samples, numerical simple-root censuses away from thresholds, derivative and stationarity checks at the thresholds, and the \(3/2\)-power coefficient. These tests provide useful regression coverage but are not an exhaustive parameter search or an infinite proof. The argument above supplies the latter.

## Relationship to prior work

Mugnaine, Sales, Szezech and Viana (2022), equations (4), (5), and (7), introduce this same map and its double-harmonic form. Their section II states that an explicit criticality boundary is not straightforward; section III and its appendix derive instead two *fixed-point saddle-node* curves \(b\pm\Omega=1\) by imposing derivative equal to **one** at a fixed point. The present criterion imposes derivative equal to **zero** anywhere on the circle and classifies *global injectivity* and all turning points, including non-fixed phases. Neither set of conditions implies the other.

The classic Arnold circle map has one-harmonic invertibility threshold; even its exact threshold does not determine the two competing harmonic wells here. Derks, Glendinning and Skeldon (2021) study creation of discontinuities and nonmonotonicity for threshold/Cherry-flow circle maps rather than this smooth three-parameter trigonometric lift. Estevez and Guarino (2022) address rigidity of bicritical circle homeomorphisms under rotation-number hypotheses, not the analytic parameter location of their critical points. A 2025 nontwist-circle study by Simile Baroni and coauthors addresses numerical global organization in a related two-parameter reduction, not an identified covering classification in its publicly accessible material.

## Limitations

This is a theorem about derivative zeros, turning points, injectivity, and precise local onset scales. It does not prove that noninjective parameter choices are chaotic, or classify attracting periodic orbits, entropy, rotation numbers, or crises. Thresholds can exceed the originating \(a\le1\) range; those surfaces still describe the mathematically extended family but the corresponding transitions are not reached in a restricted slice. Known general fold theory explains square-root splitting but does not automatically supply these parameter formulas. Exhaustive priority across unindexed and unavailable literature is not claimed; notably, the full 2025 related article was not obtained.

## References

1. M. Mugnaine, M. R. Sales, J. D. Szezech Jr., R. L. Viana, *Dynamics, multistability, and crisis analysis of a sine-circle nontwist map*, Physical Review E **106** (2022), 034203. DOI: https://doi.org/10.1103/PhysRevE.106.034203 . Public author-copy full text: https://fisica.ufpr.br/viana/artigos/2022/PhysRevE.106.034203.pdf .
2. G. Derks, P. A. Glendinning, A. C. Skeldon, *Creation of discontinuities in circle maps*, Proceedings of the Royal Society A **477** (2021), 20200872. DOI: https://doi.org/10.1098/rspa.2020.0872 .
3. G. Estevez, P. Guarino, *Renormalization of bicritical circle maps*, arXiv:2202.03128 (2022). https://arxiv.org/abs/2202.03128 .
4. R. Simile Baroni, R. Egydio de Carvalho, C. E. P. Abreu, R. O. Medrano-T, *Global dynamics and asymmetric fractal dimension in a nontwist circle map*, Chaos **35** (2025), 023122. DOI: https://doi.org/10.1063/5.0238699 .
