# Scientific review: period-two census of a fixed-point-free planar map

## Correctness

**PASS.** The map and the four strictly positive parameters are stated explicitly. Every period-two orbit necessarily alternates its second coordinate and lies away from the nonsmooth line. The sum-and-difference computation fixes both first coordinates and reduces existence to one scalar quadratic; substitution proves sufficiency, avoiding a candidate-only computation. Quadratic signs cover all parameter boundary cases. Direct matrix multiplication produces exact return trace, determinant, and the \(+1\)-multiplier identity. Standard Schur inequalities identify the hyperbolically attracting case. A symbolic checker and rational zero-, double-, and two-root examples passed. Limits: no classification of nonlinear behavior on unit-multiplier boundaries or higher periods.

## Originality

**PASS, with residual priority uncertainty.** The founding paper (Huynh et al., *Entropy* 2019, DOI 10.3390/e21030279) contains the same map, no-fixed-point argument, numerical period-two branch, and period-doubling diagram. Inspection of its complete public PDF, especially equation (1), Section 2.1, Figure 2, and Sections 3–5, found no exact four-parameter period-two root census, positive-branch multiplicity, fold threshold, large-branch escape asymptotic, or Schur boundary expressions. The similarly titled García Grimaldo et al. (*Electronics* 2023, DOI 10.3390/electronics12020444) concerns a one-dimensional piecewise-linear system and does not imply this theorem. Published mathematical-record searches and available related prior claims did not identify covering statements. Independent priority verification remains outstanding; standard algebra and stability tests as methods are not claimed to be novel.

## Value

**PASS.** The exact map was introduced specifically because it has no fixed points, and the first periodic regime was numerically reported to be period two. A complete global four-parameter classification of that first natural periodic object resolves a concrete question about where these cycles exist, including two previously unquantified phenomena: coexistence of distinct cycles and loss of one cycle at infinity. The exact attracting-versus-unstable multiplier tests and an explicitly certified attracting example make the census dynamically meaningful rather than a mere algebraic root table. This does not establish global attraction or chaos.

Self-review: passed. Independent audit: not yet performed.
