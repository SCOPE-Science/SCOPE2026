# Extremality guarantees an ergodic lift, not an ergodic chosen lift
## Finding
Let \(X\) be a compact metric space and let \(S\subset C(\mathbb R,X)\) be compact and invariant under the shift flow \(\sigma_t\). Write \(\pi(\phi)=\phi(0)\), let \(\mathcal M_\sigma(S)\) be the shift-invariant Borel probability measures on \(S\), and let
\[
\mathcal I:=\pi_*\mathcal M_\sigma(S).
\]
These are exactly the invariant measures in the trajectory-space formulation used by Suda.

If \(\mu\in\mathcal I\) is extreme, then there exists an **ergodic** \(\nu_*\in\mathcal M_\sigma(S)\) satisfying \(\pi_*\nu_*=\mu\). Hence, for every \(f\in L^1(\mu)\), for \(\mu\)-almost every \(x\in X\) there exists at least one trajectory \(\phi\in S\) with \(\phi(0)=x\) such that
\[
\lim_{T\to\infty}\frac1T\int_0^T f(\phi(t))\,dt=\int_X f\,d\mu.
\]

This existential statement is sharp. Extremality of \(\mu\) does **not** imply that an arbitrarily specified shift-invariant lift of \(\mu\) is ergodic.

## Assumptions and scope
No switching axiom and no uniqueness-of-orbits axiom are used. Compactness of \(S\) is used to make \(\mathcal M_\sigma(S)\) weak-star compact and to apply the extreme-point theorem. The time-average statement uses the continuous-time Birkhoff theorem on trajectory space and standard disintegration over \(\pi\).

The claim concerns extreme invariant measures, a natural subclass of Suda's ergodic invariant measures. It does not assert that every ergodic invariant measure in Suda's stronger-backward-invariance sense is extreme.

## Proof
Consider the continuous affine map
\[
P:\mathcal M_\sigma(S)\longrightarrow\mathcal I,\qquad P(\nu)=\pi_*\nu.
\]
Fix \(\mu\in\operatorname{ext}(\mathcal I)\) and its nonempty fibre
\[
F_\mu:=\{\nu\in\mathcal M_\sigma(S):P(\nu)=\mu\}.
\]
The fibre is compact and convex. It is also a face of \(\mathcal M_\sigma(S)\): if \(0<a<1\) and
\[
\nu=a\nu_1+(1-a)\nu_2\in F_\mu,
\]
then
\[
\mu=aP(\nu_1)+(1-a)P(\nu_2).
\]
Since \(\mu\) is extreme in \(\mathcal I\), necessarily \(P(\nu_1)=P(\nu_2)=\mu\), so \(\nu_1,\nu_2\in F_\mu\).

By Krein--Milman, \(F_\mu\) has an extreme point \(\nu_*\). Because \(F_\mu\) is a face, an extreme point of \(F_\mu\) is extreme in \(\mathcal M_\sigma(S)\). Extreme invariant measures of the shift flow are exactly its ergodic invariant measures, so \(\nu_*\) is ergodic and \(\pi_*\nu_*=\mu\).

For \(f\in L^1(\mu)\), the function \(f\circ\pi\) lies in \(L^1(\nu_*)\). Birkhoff's theorem gives, for \(\nu_*\)-almost every \(\phi\),
\[
\lim_{T\to\infty}\frac1T\int_0^T f(\pi(\sigma_t\phi))\,dt
=\int_S f\circ\pi\,d\nu_*
=\int_X f\,d\mu.
\]
Since \(\pi(\sigma_t\phi)=\phi(t)\), this is the asserted trajectory average. Disintegrating \(\nu_*\) over \(\pi\) shows that for \(\mu\)-almost every starting point \(x\), the fibre \(\pi^-1(x)\) contains such a Birkhoff-generic trajectory.

To show sharpness, take \(X=\mathbb R/\mathbb Z\). For \(\varepsilon\in\{+1,-1}\) and \(\theta\in X\), define
\[
\phi_{\varepsilon,\theta}(t)=\theta+\varepsilon t\pmod 1,
\]
and let \(S\) be the union of these two families. It is a compact shift-invariant subset of \(C(\mathbb R,X)\). Each component \(S_+\) and \(S_-\) is a single periodic shift orbit and has a unique ergodic invariant probability \(\nu_+\) and \(\nu_-\), respectively. Both project under \(\pi\) to Haar measure \(m\) on the circle. Every shift-invariant probability on \(S\) is
\[
\lambda\nu_+ +(1-\lambda)\nu_-\qquad(0\le\lambda\le1),
\]
so every one projects to \(m\). Thus \(\mathcal I=\{m}\), making \(m\) extreme, while
\[
\nu=\tfrac12(\nu_++\nu_-)
\]
is not ergodic because the invariant set \(S_+\) has \(\nu\)-measure \(1/2\). Therefore an extreme base measure can have a nonergodic specified lift.

## Verification
The face argument was checked in both directions: extremality is used only after pushing a convex decomposition of a lift down to \(\mathcal I\), and the face property then promotes an extreme point of the fibre to an extreme point of the whole shift-invariant-measure simplex. No injectivity of \(\pi_*\) is assumed.

The counterexample was checked at the level of the complete invariant-measure sets. Each sign component is conjugate to the unit-speed rotation flow on the circle and therefore uniquely ergodic. Since the two components are disjoint invariant sets, every invariant measure on their union is a convex combination of their Haar measures. Both one-time marginals are the same Haar measure \(m\), so the base invariant-measure set is exactly the singleton \(\{m}\).

## Relationship to prior work
Suda defines a measure \(\mu=\pi_*\nu\) to be finely ergodic when the displayed lift \(\nu\) is ergodic, and Theorem 3.7 states that extremal invariant measures are finely ergodic. Its proof attempts to infer extremality of \(\nu\) from extremality of \(\pi_*\nu\). That inference is not valid when \(\pi_*\) is noninjective: extremality of the image only forces the components of a decomposition of \(\nu\) to have the same image. The circle example above realizes this obstruction exactly.

The corrected existential statement follows from the standard fact that extreme points of a compact convex affine image have extreme preimages. In ordinary factor-map dynamics, existence of an ergodic invariant lift of an ergodic factor measure is standard; Downarowicz and Weiss explicitly recall this fact before studying the substantially harder problem of lifting individual generic points. The present point is that Suda's evaluation map is not a factor map to a deterministic base flow, so the appropriate object is the affine image \(\mathcal I\); extremality in that image still gives an ergodic lift, but does not make every lift ergodic.

The time-average consequence gives a concrete partial answer to Suda's concluding question: for every extreme invariant measure, the specific value \(\int_X f\,d\mu\) is realizable by at least one trajectory from almost every starting point.

## Limitations
The result does not characterize all almost-everywhere realizable time-average values, and it does not show that every Suda-ergodic invariant measure is extreme. The circle example does not satisfy the switching axiom; that axiom is not assumed in Suda's Theorem 3.7 or in the corrected extremal-lift statement. The positive existence theorem is an application of standard compact-convex geometry; the new content here is the sharp distinction between existence of an ergodic lift and ergodicity of a specified lift in this generalized trajectory-space setting, together with the explicit counterexample and time-average consequence.

## References
1. T. Suda, *Ergodicity of dynamical systems without uniqueness of orbits*, arXiv:2609.11087, first posted 10 September 2026. In particular Definition 3.2, Theorem 3.7, Theorem 4.1, Corollary 4.3, and the concluding question.
2. T. Downarowicz and B. Weiss, *Lifting generic points*, Ergodic Theory and Dynamical Systems 44 (2024), 2565--2580, doi:10.1017/etds.2023.119.
3. Krein--Milman theorem and the standard characterization of ergodic invariant measures as extreme invariant measures.
