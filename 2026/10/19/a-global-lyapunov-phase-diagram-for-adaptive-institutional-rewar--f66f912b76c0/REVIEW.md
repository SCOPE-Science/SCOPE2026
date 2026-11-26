# Independent mathematical audit

## correctness

PASS

Independently reconstructed the factorization x'=P(x)(a-Aδ(x)), a'=(1+u)Q(a)(h-x) and the Lyapunov argument. S_N decreases strictly from N to 1 and 0<h<1, so comparing Aδ at 0,h,1 with the two reward bounds gives the four strictly ordered thresholds and the five displayed choices. For the selected point (xe,ae), differentiating the separable integrals gives V'/(1+u)=−(x−xe)(Aδ(x)−Aδ(xe))+(x−xe)(ae−Aδ(xe))+(a−ae)(h−xe). The first summand is strictly negative for x≠xe; the second is zero except in the two endpoint regimes, where the displacement and selection inequality give opposite signs; the last is zero at xe=h and otherwise nonpositive with equality only at ae. These signs do not require strict threshold inequalities. The integrands have removable singularities at a selected boundary coordinate and logarithmic barriers at every other endpoint; the extended finite sublevels are compact and forward invariant, since selected boundary faces are invariant and V' extends there. At xe=h the only trajectory held on V'=0 has a=Aδ(h), because P(h)>0. Otherwise V'=0 already gives the selected point. LaSalle therefore applies even at the four nonhyperbolic thresholds. The branch is continuous by inversion of S_N, with exactly the stated monotonic pieces. No nonconstant interior cycle can stay in the zero-dissipation set. The frozen wording 'strict decrease ... off the selected point' should not be interpreted as pointwise V'<0 on x=h in the central regime; the invariant-set proof is valid and supplies the conclusion. The recorded finite numerical checks are ancillary; no submitted script was executed.

## originality

PASS

The complete global five-regime selection theorem, including boundary and equality cases at arbitrary positive ε, is distinct from the original model analysis and from the strongest exact-model comparisons. The ODE, central equilibrium, local stability analysis and representative phase portraits are not original to this result.

## value

PASS

It replaces parameter-specific portraits and local stability with a single global prediction at every speed for a published feedback model. In particular, compactness at selected faces and convergence at nonhyperbolic thresholds resolve questions that linearization cannot decide. The continuous monotone response branches are useful consequences within the exact model, not claims about policy or modified feedback.

The dated certificate retains the supplied scientific assessment, sources and limitations.
