# Review: Equilibrium-axis barycenter rigidity in the cubic Clapp oscillator

## Correctness
**PASS.** The four invariant-measure identities are obtained by integrating the coordinate derivatives, and every division uses a parameter assumed strictly positive. The strict one-sided conclusion uses strict convexity and an invariant-support argument; it does not infer recurrence from a finite trajectory.

## Originality
**PASS.** The same-system 2022 primary article was inspected through the model, equilibrium, numerical-analysis, circuit-realization, and discussion sections. It gives the equilibrium line but not the barycenter identity, cubic stationary moment, or threshold-crossing result. Targeted same-system searches under mean, stationary moment, invariant measure, barycenter, and third-moment aliases found no covering statement. A related 2019 Clapp-based snap-circuit paper concerns a different vector field and does not imply this claim. General stationarity of invariant measures is standard and is not claimed as new.

## Value
**PASS.** The source highlights coexistence and multistability as a structural open direction. The result constrains every compact recurrent statistical state without numerical trajectory fitting, and the one-sided theorem forces symmetry-broken recurrent states to cross the voltage of the outer equilibrium. This is a meaningful geometric restriction on the coexisting regimes studied in the source.

## Closest literature and limitations
The closest primary source is Petržela (2022), which introduces the exact polynomial Clapp model and reports chaotic/hyperchaotic coexistence. The closest earlier circuit literature inspected is Srisuchinwong et al. (2019), but it uses a different Clapp-based snap flow. The theorem assumes compact invariant support; the strict crossing statement additionally assumes ergodicity and one-sided support, and it does not prove existence of such a state.

Same-model review: passed. Independent audit: not yet performed.
