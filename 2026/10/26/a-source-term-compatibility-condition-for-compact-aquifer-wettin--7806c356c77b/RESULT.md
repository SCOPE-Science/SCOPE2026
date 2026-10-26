# A source-term compatibility condition for compact aquifer wetting fronts

## Finding

On any time interval \(I\) for which the zero-extended aquifer profile is identically dry on a fixed open spatial interval \(U\), a distributional solution of the printed full-line Boussinesq equation \(h_t=k\partial_x(h\partial_x h)+v_s\partial_x h-\phi h+N(t)/n\) must satisfy \(N(t)=0\) almost everywhere on \(I\). Therefore a compactly supported zero extension is incompatible with a spatially uniform additive source/sink whenever \(N\) is nonzero on a positive-measure subset of \(I\), unless the equation is restricted to the wet region or the source is explicitly localized there.

## Assumptions and scope

Let \(k>0\), \(n>0\), \(\phi\geq0\), and let \(v_s\) be constant. The equation is interpreted as a distributional PDE on the full spatial line, with \(N\) locally integrable in time. On a time interval \(I\), assume the zero extension has a fixed nonempty open dry interval \(U\), so \(h=0\) almost everywhere on \(U\times I\). This statement is a compatibility condition, not an existence or uniqueness theorem for the wet-region problem.

## Proof

On \(U\times I\), the function \(h\) is identically zero. Hence its time derivative and spatial derivative vanish there as distributions; also \(h\partial_xh=0\) and \(\phi h=0\). Testing the equation against any smooth compactly supported test function in \(U\times I\) therefore leaves only the source term, giving \(N(t)/n=0\) in distributions on \(I\). Since \(n>0\) and \(N\) is locally integrable, \(N(t)=0\) almost everywhere on \(I\). The contrapositive proves the incompatibility for any interval on which \(N\) is nonzero on a set of positive measure. No numerical approximation or finite experiment is used.

## Verification

The source article prints the equation with source term \(\Lambda(h,t)=-\phi n h+N(t)\), and then states that its parabolic profile is zero outside the finite wetting fronts. Substitution of \(\Lambda/n=-\phi h+N(t)/n\) yields the equation used above. The proof checks the weak equation on a dry open set, away from the moving interface; it does not rely on an unverified interface jump condition.

## Relationship to prior work

Bartlett and Porporato derive an exact parabolic-profile formula for sloping and horizontal aquifers with a time-only additive term, and explicitly extend the profile by zero beyond the wetting fronts. The general groundwater review by Troch and coauthors discusses the history and limitations of exact Boussinesq solutions, including the distinction between drainage and recharge settings. The present statement is not a new general theorem about porous-medium equations: it records the necessary compatibility condition for this particular printed equation and its advertised zero extension. General finite-propagation results for unforced equations, or equations whose source vanishes with \(h\), do not by themselves establish compatibility for the additive term \(N(t)\).

## Limitations

The conclusion is conditional on interpreting the printed PDE distributionally on the full line, including dry locations. If the intended physical equation is defined only on \(h>0\), or if recharge is applied only on the saturated region, then the model must state that domain/source convention explicitly; the result does not rule out a valid interior wet-region solution under that different formulation. No claim is made about the model's uniqueness, quantitative hydrologic accuracy, or the behavior after the entire domain becomes wet.

## References

1. M. S. Bartlett and A. Porporato, “A class of exact solutions of the Boussinesq equation for horizontal and sloping aquifers,” *Water Resources Research* 54 (2018), 767–778. First published 11 January 2018. https://doi.org/10.1002/2017WR022056
2. P. A. Troch et al., “The importance of hydraulic groundwater theory in catchment hydrology: The legacy of Wilfried Brutsaert and Jean-Yves Parlange,” *Water Resources Research* (2013). https://doi.org/10.1002/wrcr.20407
