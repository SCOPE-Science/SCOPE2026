# Exact recurrence crossing and mean-elevation law in a fear-controlled food chain

## Finding
For the three-species food-chain model introduced by Kumar and Kumari, the top-predator equation is
\[
\dot u_3=u_3\left(-c_3+\frac{w_3u_2}{d_3+u_2}\right).
\]
Let \(\mu\) be any compactly supported invariant Borel probability measure whose support is contained in \((0,\infty)^3\), and put
\[
m_2=\int u_2\,d\mu.
\]
Then
\[
\int\frac{u_2}{d_3+u_2}\,d\mu=\frac{c_3}{w_3}.
\]
Thus such a recurrent positive state requires \(w_3>c_3\). Define the positive-equilibrium middle-predator coordinate
\[
u_{2*}=\frac{c_3d_3}{w_3-c_3}.
\]
The following exact finite-amplitude identity holds:
\[
m_2-u_{2*}=
\frac{d_3+u_{2*}}{d_3+m_2}
\int\frac{(u_2-m_2)^2}{d_3+u_2}\,d\mu.
\]
In particular, \(m_2\ge u_{2*}\). If \(\mu\) is ergodic and is not an equilibrium point mass, then
\[
m_2>u_{2*},
\]
and its support meets both open half-spaces \(u_2<u_{2*}\) and \(u_2>u_{2*}\). Every strictly positive nonconstant periodic orbit therefore crosses \(u_2=u_{2*}\) and has period mean \(\bar u_2>u_{2*}\).

For the numerical parameter values used repeatedly in the source, \(c_3=0.7\), \(w_3=2\), and \(d_3=20\),
\[
u_{2*}=\frac{140}{13}\approx10.7692307692.
\]
Hence every strictly positive nonconstant periodic orbit at those parameter values must pass both below and above \(140/13\), while its arithmetic mean lies strictly above \(140/13\).

## Assumptions and scope
The source model is
\[
\dot u_1=\frac{a_0u_1}{1+f_1u_2}-b_0u_1^2-\frac{w_0u_1u_2}{d_0+u_1},
\]
\[
\dot u_2=\frac{w_1u_1u_2}{(d_1+u_1)(1+f_2u_3)}-\frac{w_2u_2u_3}{d_2+u_2}-a_1u_2,
\]
\[
\dot u_3=-c_3u_3+\frac{w_3u_2u_3}{d_3+u_2}.
\]
All demographic, mortality, saturation, and conversion parameters used in the proof are positive; \(f_1,f_2\ge0\). The invariant-measure statement assumes compact support contained in the strict positive octant. This guarantees that \(\log u_3\) is a legitimate smooth observable on a neighborhood of the support. The periodic-orbit consequence requires a classical strictly positive nonconstant periodic solution.

The identity is independent of the two fear parameters because the top-predator per-capita equation contains only \(u_2\). Fear still changes which recurrent states exist and their geometry through the other two equations.

## Proof
On the strict positive octant,
\[
\frac{d}{dt}\log u_3=-c_3+w_3\frac{u_2}{d_3+u_2}.
\]
For an invariant probability measure with compact positive support, the integral of a flow derivative of a smooth observable is zero. Therefore
\[
0=-c_3+w_3\int\frac{u_2}{d_3+u_2}\,d\mu,
\]
which proves the trophic balance. Since \(0<u_2/(d_3+u_2)<1\), this also forces \(0<c_3/w_3<1\), hence \(w_3>c_3\).

Let
\[
h(x)=\frac{x}{d_3+x}.
\]
The positive-equilibrium coordinate satisfies \(h(u_{2*})=c_3/w_3\), so the trophic balance is \(\int h(u_2)\,d\mu=h(u_{2*})\). For every \(x>0\) and every \(m>0\), the pointwise identity
\[
\frac{m}{d_3+m}-\frac{x}{d_3+x}
=-\frac{d_3(x-m)}{(d_3+m)^2}
+\frac{d_3(x-m)^2}{(d_3+m)^2(d_3+x)}
\]
holds. Set \(m=m_2\) and integrate. The linear term vanishes because \(\int(u_2-m_2)\,d\mu=0\), giving
\[
h(m_2)-\int h(u_2)\,d\mu
=\frac{d_3}{(d_3+m_2)^2}
\int\frac{(u_2-m_2)^2}{d_3+u_2}\,d\mu.
\]
Also
\[
h(m_2)-h(u_{2*})=
\frac{d_3(m_2-u_{2*})}{(d_3+m_2)(d_3+u_{2*})}.
\]
Equating these two expressions proves the displayed defect law. Its right-hand side is nonnegative, and it is zero exactly when \(u_2=m_2\) almost surely.

Now suppose \(\mu\) is ergodic and not an equilibrium point mass. If \(u_2\) were almost surely constant, the trophic balance would force that constant to equal \(u_{2*}\). Along every trajectory in the support, the top-predator equation would then give \(\dot u_3=0\), so \(u_3\) would be constant. With positive constant \(u_2\) and \(u_3\), the equation \(\dot u_2=0\) makes
\[
\frac{w_1u_1}{(d_1+u_1)(1+f_2u_3)}
\]
constant. This expression is strictly increasing in \(u_1>0\), so \(u_1\) is constant as well. Every trajectory in the support would therefore be an equilibrium; ergodicity would force \(\mu\) to be an equilibrium point mass, a contradiction. Thus the defect integral is positive and \(m_2>u_{2*}\).

Finally, because \(h\) is strictly increasing and \(\int h(u_2)\,d\mu=h(u_{2*})\), a non-equilibrium ergodic measure cannot be supported entirely in either \(u_2\le u_{2*}\) or \(u_2\ge u_{2*}\). It therefore assigns positive mass to both strict sides. The invariant probability measure uniformly distributed along a nonconstant periodic orbit is ergodic for the orbit flow, so the periodic statement follows.

## Verification
The bundled checker `verify_identity.py` verifies the rational pointwise decomposition, the conversion from the defect in \(h\) to the exact formula for \(m_2-u_{2*}\), and the source-parameter value \(u_{2*}=140/13\). The proof of the invariant-measure identity is analytic and does not infer an infinite-time statement from finite simulation.

The same source reports limit-cycle and chaotic regimes as fear parameters and prey growth are varied. The present result is a necessary constraint on any strictly positive recurrent state of the printed model and is valid at arbitrary amplitude.

## Relationship to prior work
Kumar and Kumari introduced the model, derived its equilibria and local stability conditions, and numerically exhibited stable-focus, limit-cycle, period-doubling, and chaotic regimes. The positive equilibrium already contains the coordinate \(u_{2*}=c_3d_3/(w_3-c_3)\). The inspected source does not state the invariant-measure balance, the exact mean-elevation defect, or the global support-crossing consequence.

A closely related later three-species fear model with a generalist top predator has a different top-predator growth law, including alternative-food terms, so its recurrence equations do not specialize to the balance above. The earlier fear-chain literature cited by the source is relevant background for the model class, but the accessible material inspected did not supply an equivalent all-amplitude mean-defect statement for this exact model.

## Limitations
This result supplies necessary conditions only. It does not prove that a positive periodic orbit, chaotic invariant set, or other recurrent state exists, nor does it establish uniqueness, stability, bifurcation direction, basin geometry, or persistence. The strict conclusion for general invariant measures requires ergodicity; a non-ergodic mixture of equilibrium measures can satisfy equality without representing a nonconstant orbit. The originality search is necessarily non-exhaustive, and an equivalent identity could exist in literature not indexed or not fully accessible in the sources inspected.

## References
1. V. Kumar and N. Kumari, “Controlling chaos in three species food chain model with fear effect,” *AIMS Mathematics* 5(2), 828–842 (2020), published 31 December 2019, DOI: 10.3934/math.2020056.
2. S. Pal, S. Tiwari, O. P. Misra, and X. Wang, “Fear effect in a three-species food chain model with generalist predator,” *Mathematical Biosciences and Engineering* 21(1), 1–28 (2024), DOI: 10.3934/mbe.2024001.
3. P. Panday, N. Pal, S. Samanta, et al., “Stability and bifurcation analysis of a three-species food chain model with fear,” *International Journal of Bifurcation and Chaos* 28 (2018), 1850009, DOI: 10.1142/S0218127418500098.
