# Two elliptic diagonals and two exact minus-one resonances in the eye-shaped billiard

## Finding

For the strictly convex planar billiard with boundary
\[
 r_\varepsilon(\theta)=(\cos\theta,\;\varepsilon\sin\theta(1+\sin^2\theta)), \qquad \varepsilon>0,
\]
consider primitive two-collision trajectories. For every \(1/(2\sqrt2)<\varepsilon<1\), there are exactly four distinct unoriented normal diameters: two axial and two nonaxial. The axial diameters are hyperbolic. **Both nonaxial diameters are linearly elliptic throughout the open interval apart from exactly two isolated minus-one multiplier resonances**, where their complete two-step linearization is \(-I\).

Specifically, put
\[
 u=u(\varepsilon)=\frac{\sqrt{1+3/\varepsilon^2}-2}{3}, \qquad
 K(u)=\frac{2(1+u)(1-3u+6u^2)}{(1+3u)(1+3u-2u^2)}.
\]
For either diagonal, in any canonical local billiard coordinates,
\[
 \det DT^2=1,\qquad \operatorname{tr}DT^2=4(1-K(u))^2-2,\qquad 0<K(u)<2.
\]
Hence \(-2\le\operatorname{tr}DT^2<2\), with equality on the left precisely when
\[
 f(u)=18u^3-u^2-10u+1=0.
\]
There are exactly two such roots in \((0,1)\), characterized by
\[
 u_-\in(1/10,11/100),\quad u_+\in(7/10,3/4),\qquad
 \varepsilon_-=\frac{1}{\sqrt{(1+u_+)(1+3u_+)}}\approx0.4289370102697598,
\]
\[
 \varepsilon_+=\frac{1}{\sqrt{(1+u_-)(1+3u_-)}}\approx0.8351293352358268.
\]
At both resonance values \(DT^2=-I\) in canonical optical coordinates (and therefore in any coordinate chart). Other rational-angle resonances, which may have trace strictly between \(-2\) and \(2\), are not excluded by this statement. The parameter interval is maximal for existence of the nonaxial orbits; the endpoints are mergers with axial orbits.

## Assumptions and scope

The boundary is the exact smooth strictly convex curve above, with specular reflection and the usual billiard collision map \(T\). "Linearly elliptic" means that the real area-preserving two-step derivative has trace strictly between \(-2\) and \(2\); this does not assert Lyapunov stability. A two-collision geometric orbit is identified with its reversed orientation and the choice of starting impact. Only non-grazing, genuinely two-point trajectories are considered.

## Proof

**Exhaustion of two-bounce trajectories.** A trajectory that retraces the same chord after two specular impacts must meet the boundary normally at both endpoints, because the outgoing velocity is the negative of the incoming velocity. The outward normals at the two impacts are opposite. Strict positive curvature makes the Gauss normal map injective, while central symmetry sends a normal to its opposite under \(r\mapsto-r\). Thus the two endpoints are necessarily antipodal. The normal-diameter condition \(r\cdot r'=0\) reduces to
\[
 \sin\theta\cos\theta\,[-1+\varepsilon^2(1+\sin^2\theta)(1+3\sin^2\theta)]=0.
\]
The axial solutions always exist; the nonaxial equation is \(\varepsilon^2(1+u)(1+3u)=1\), yielding the stated unique \(u\in(0,1)\) and exactly two diagonal diameter lines, when and only when \(1/(2\sqrt2)<\varepsilon<1\). This enumeration and the axial trace formulas were previously obtained in the motivating study; they are included to state the complete classification and are not claimed as new.

**Geometry at a diagonal impact.** Set \(H(u)=1+3u-2u^2\) and \(Q(u)=1-3u+6u^2\). Direct differentiation and use of \(\varepsilon^2(1+u)(1+3u)=1\) give
\[
 |r|^2=\frac{H(u)}{1+3u},\qquad |r'|^2=\frac{H(u)}{1+u},\qquad
 \det(r',r'')=\varepsilon Q(u).
\]
Here \(H(u)>0\), \(Q(u)>0\), since \(0<u<1\) and the discriminant of \(Q\) is negative. The flight distance is \(L=2|r|\) and the positive curvature is \(\kappa=\det(r',r'')/|r'|^3\). Therefore
\[
 L\kappa=\frac{2(1+u)Q(u)}{(1+3u)H(u)}=K(u).
\]

**Two-collision monodromy.** In local transverse displacement/slope coordinates for a ray, a free flight of length \(L\) is \(F_L=\begin{pmatrix}1&L\\0&1\end{pmatrix}\), and specular reflection at positive curvature \(\kappa\) is \(R_\kappa=\begin{pmatrix}1&0\\-2\kappa&1\end{pmatrix}\). This follows from the first-order reflection law: changing the impact point by transverse distance \(\delta x\) rotates its inward normal by \(\kappa\delta x\), hence changes the outgoing slope by \(-2\kappa\delta x\). Opposite impacts have equal curvature and flight length, so the two-step derivative is conjugate to \((R_\kappa F_L)^2\) (a possible orientation sign in the one-step basis cancels on squaring). Since \(\det(R_\kappa F_L)=1\) and \(\operatorname{tr}(R_\kappa F_L)=2(1-L\kappa)\), the Cayley–Hamilton identity gives
\[
 \operatorname{tr}DT^2=4(1-L\kappa)^2-2.
\]
The formula reproduces the source's axial trace expressions when the appropriate axial curvature and chord lengths are substituted, providing an independent normalization check.

**Sharp elliptic interval and exceptional values.** The decisive factorization is
\[
 (1+3u)H(u)-(1+u)Q(u)=4u(1-u)(3u+2)>0
 \quad (0<u<1).
\]
Therefore \(0<K(u)<2\), and the trace is strictly below \(2\) and at least \(-2\). The trace equals \(-2\) precisely when \(K=1\), equivalent to \(f(u)=18u^3-u^2-10u+1=0\). The derivative \(f'(u)=54u^2-2u-10\) has exactly one zero in \((0,1)\), namely \((1+\sqrt{541})/54\). Moreover, \(f(0)=1\), \(f(1/2)=-2\), and \(f(1)=8\). Thus \(f\) has exactly two roots in \((0,1)\); rational sign tests place them in the intervals stated above. Since \(K=1\) gives \(\operatorname{tr}(R_\kappa F_L)=0\), Cayley–Hamilton yields \((R_\kappa F_L)^2=-I\), not just trace \(-2\). The map \(u\mapsto\varepsilon=((1+u)(1+3u))^{-1/2}\) is strictly decreasing, giving the stated parameter order.

Finally, the source's exact axial trace formulas are \(4(1-16\varepsilon^2)^2-2\) (vertical) and \(4(2/\varepsilon^2-1)^2-2\) (horizontal). Both exceed \(2\) throughout the open diagonal-existence interval, proving the two hyperbolic/two elliptic-or-exceptional census.

## Verification

Run `python verify.py` with Python 3 and SymPy. The standalone script checks the normal-diameter and curvature identities, the optical monodromy trace and \(-I\) resonance, the exact positivity factorization and polynomial reduction, rational isolating brackets, and a finite rational parameter sample. It reports approximations to both resonance parameters. A finite sample is supplementary and not a proof of an interval-wide inequality; that inequality follows from the displayed strictly positive factorization.

## Relationship to prior work

Fonseca, Leonel, and Oliveira, *Geometry-induced chaos and scaling near two singular limits of an eye-shaped billiard*, arXiv:2610.29128v1 (first made public 2026-10-21), derives the normal-diameter existence interval and both **axial** monodromy traces. At the end of its Section III.1 it explicitly leaves the **diagonal** two-collision monodromy to a separate examination. The new contribution is the exact diagonal trace, universal ellipticity throughout its existence interval except for the two explicit \(-I\) resonances, and the resulting complete two-bounce spectral census. Standard optical linearization supplies the general framework but does not by itself evaluate the nontrivial rational curvature expression or its global factorization for this particular boundary. General work on central-symmetric billiard rigidity and shortest billiard orbits treats different questions.

## Limitations

Elliptic linearization does not guarantee nonlinear stability, a positive-area island, invariant KAM curves around each orbit, or global dynamical regularity. The two exceptional values are the \(-1\) two-step multipliers only; no claim excludes higher-order resonances elsewhere. At the boundary parameters the diagonal orbits merge with axial ones and the strict interior classification does not apply. Historical priority beyond the inspected primary text and indexed literature remains provisional.

## References

1. A. K. P. da Fonseca, E. D. Leonel, D. F. M. Oliveira, *Geometry-induced chaos and scaling near two singular limits of an eye-shaped billiard*, arXiv:2610.29128v1, 21 October 2026. https://arxiv.org/html/2610.29128v1
2. M. Bialy and A. E. Mironov, *The Birkhoff–Poritsky conjecture for centrally-symmetric billiard tables*, Ann. of Math. 196 (2022), 389–413. https://annals.math.princeton.edu/2022/196-1/p02
3. N. Alkoumi and F. Schlenk, *Shortest closed billiard orbits on convex tables*, arXiv:1408.5255 (2014). https://arxiv.org/abs/1408.5255
