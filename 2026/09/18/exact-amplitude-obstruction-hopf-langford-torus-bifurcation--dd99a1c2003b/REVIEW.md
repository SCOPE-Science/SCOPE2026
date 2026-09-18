# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

For the source system, the polar variables \(s=x^2+y^2\), \(\theta=\arg(x+iy)\) give the exact autonomous quotient
\[
\dot s=2s(\mu-\alpha+z),\qquad
\dot z=\mu z-\gamma(s+z^2),\qquad
\dot\theta=\beta.
\]
The positive quotient equilibrium corresponds to the circular periodic orbit and has Jacobian trace
\[
D=(1+2\gamma)\mu-2\gamma\alpha
\]
and determinant \(2\gamma s_*\). Thus a complex transverse pair can have unit-modulus Floquet multipliers only at \(D=0\).

The stronger obstruction follows from the positive Dulac density \(B=s^{\gamma-1}\), for which \(\operatorname{div}(BF)=DB\). Weighted area under the quotient flow scales exactly by \(e^{Dt}\). A local torus transverse to the nonzero angular flow would intersect a global angular section in an invariant Jordan curve of the quotient time map; the bounded interior of that curve would have to map to itself, which contradicts strict weighted-area expansion or contraction when \(D\neq0\).

At \(D=0\), with \(\gamma>0\), the displayed first integral in RESULT.md differentiates to zero identically. Its Hessian at the positive equilibrium is positive definite, proving that the quotient equilibrium is a center and is surrounded by a continuum of closed orbits. Their lifts are a continuum of invariant tori. Hence the critical surface is degenerate and integrable, not a generic Neimark-Sacker surface with a unique torus on one side.

The perturbative comparison was checked independently from the exact trace condition. For \(\alpha_1=\gamma_0=\omega=1\) and \(\alpha_2=\gamma_1=\mu_2=0\), the source's strict assumptions (4) evaluate to \(1/9>0\) and \(-8/9<0\). The exact neutral curve has first correction zero, while the source's Eq. (7) gives \((8\pi^2-2)/27\). This is an analytic contradiction inside the stated theorem hypotheses.

The source's Example 2 was also checked. It uses \(\gamma_0=-1\), violating the theorem assumption \(\gamma_0>0\); at \(\varepsilon=10^{-3}\) the circular orbit has negative transverse determinant and is saddle-type. This example is supporting evidence, not needed for the main contradiction.

## Originality

PASS, to the best of our knowledge, with a deliberately narrow claim.

The dimensional reduction and first-integral phenomenon are prior art. Vassilev--Nikolov (Axioms 14(1):8) explicitly reduce a seven-parameter Hopf-Langford-type system to a planar amplitude system and derive first integrals. Under the parameter identification for the 2026 source, their first-integral condition becomes the same neutral relation \(D=0\); their equal-coefficient special case covers the remaining \(\gamma=1\) branch. Earlier Hopf-Langford integrability work was also located. None of these tools or the existence of an integrable Hopf-Langford subfamily is claimed as new.

The primary source arXiv:2609.18010v1 was inspected in full-text HTML. Its Theorem 2 explicitly asserts a smooth curve producing a unique invariant torus by Neimark-Sacker bifurcation, with a nonzero positive first Lyapunov coefficient, and its Eq. (7) gives the first correction to that curve. The exact source-specific reduction above contradicts those claims. Searches by exact title, arXiv identifier, `correction`, `torus`, `Neimark-Sacker`, and equivalent Hopf-Langford integrability terminology did not locate a later correction or an existing note making this specific contradiction.

The originality claim is therefore only the source-specific correction: applying the exact amplitude geometry to arXiv:2609.18010v1 to prove the no-torus/center-foliation alternative, derive the exact Floquet-neutral surface, and exhibit an admissible coefficient choice where the source's perturbative bifurcation curve disagrees at first correction order.

The main residual risk is temporal: the source was submitted on 16 September 2026 and currently has only v1 on arXiv, so an unindexed author communication or a later revision could independently identify and correct the issue. That possibility is not evidence of current prior coverage.

## Value

PASS.

The result changes the qualitative interpretation of the source's main theorem. It shows that the particular SO(2)-symmetric system cannot undergo the generic secondary Hopf scenario asserted there: the exact angular decoupling leaves a planar autonomous amplitude flow whose weighted area either contracts/expands monotonically or, on the neutral surface, becomes integrable and center-like. This replaces an approximate torus-bifurcation picture with an exact structural classification near the circular periodic orbit.

The explicit discrepancy between the exact neutral curve and the published Eq. (7) gives a reproducible diagnostic for correcting the perturbative calculation. The observation that Example 2 violates the theorem's sign hypothesis is an additional concrete consistency check.

## Sources checked

- G. Domingues, *Torus Bifurcation in the Hopf-Langford type system through Averaging Theory*, arXiv:2609.18010v1 (submitted 16 September 2026). Full-text HTML, theorem statements, perturbation formulas, proof section, and numerical examples were inspected:
  https://arxiv.org/abs/2609.18010
- V. M. Vassilev and S. G. Nikolov, *First and Second Integrals of Hopf-Langford-Type Systems*, Axioms 14(1):8. The open full text, dimensional reduction, and first-integral conditions were inspected:
  https://doi.org/10.3390/axioms14010008
- S. G. Nikolov and V. M. Vassilev, *Completely integrable dynamical systems of Hopf-Langford type*, Communications in Nonlinear Science and Numerical Simulation 92 (2021), 105464. Abstract/indexed description was inspected; the full article was not independently inspected:
  https://doi.org/10.1016/j.cnsns.2020.105464
- M. R. Cândido and D. D. Novaes, *On the torus bifurcation in averaging theory*, Journal of Differential Equations 268 (2020), 4555--4576. This is the general theorem invoked by the source; no defect in that general theorem is claimed here:
  https://doi.org/10.1016/j.jde.2019.11.046

## Limitations retained

The theorem recorded here addresses the exact SO(2)-symmetric system in arXiv:2609.18010v1 and local surrounding tori contained in \(s>0\). It does not rule out torus bifurcations in generalized Hopf-Langford systems with symmetry-breaking terms, nor does it classify invariant sets meeting the rotation axis or the case \(\beta=0\). The first-integral mechanism itself is prior literature. A later source revision may alter the theorem being corrected.
