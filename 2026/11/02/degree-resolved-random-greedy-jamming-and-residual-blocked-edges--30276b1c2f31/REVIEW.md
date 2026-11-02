# Scientific review

## Correctness — PASS

The rooted labeled-tree decomposition gives \(T=ze^T\). Arrival-time conditioning derives \(\partial_tF=ze^{T-F}\) and \(F=\log(1+tT)\), hence the exact bivariate degree-resolved accepted-root generating function \(\mathcal A(z,q)=ze^{qT}\int_0^1(1+tT)^{-q}\,dt\). Differentiating in the root-degree variable gives \(H=T\log(1+T)-\tfrac12\log^2(1+T)\). The pathwise independent-set identity \(B_n=n-1-\sum_{v\in I_n}D_v\) then yields its exact expectation. Square-root singularity transfer establishes the order-one finite-size correction, with separately checked derivatives. A fixed-degree coefficient transfer and two-root local convergence establish the limiting empirical joint degree/acceptance profile and residual edge concentration. The separately replayed checker passes 38 exact rational assertions using Prüfer enumeration, first-pick recursion, and permutation enumeration; the all-size claim rests on the analytic steps, not exhaustive finite tests.

## Originality — PASS, with specified priority risk

Krivelevich–Mészáros–Michaeli–Shikhelman (arXiv:1907.07216, first posted July 16, 2019) obtain local-limit random-greedy occupancy and the accepted-density \(1/2\) for Poisson offspring; their two-type ODE plausibly supplies the limiting conditional degree profile by routine extraction, so that profile is not claimed as a separate novel theorem. Contat (arXiv:2103.03800) gives exact *scalar* cardinality and asymptotic fluctuation laws on Cayley trees. Neither inspected full text states the degree-marked *all-finite-order* labeled-Cayley-tree EGF or its residual blocked-edge mean and the order-one term \(-9/16+\log2/8\). Penrose–Sudbury's general forward equations concern deposition on fixed graphs and infinite tree geometry; they provide relevant antecedents without the finite uniform-Cayley-tree joint enumeration. The claim cannot be deduced from the published scalar accepted-cardinality law alone because the degree-weighted accepted count is independent additional information. The exact finite enumerator and its nontrivial coefficient are the contribution. Risks include implicit specialization of broad graph-deposition equations or older marked-tree enumeration not located by the searches. Definitive priority and independent audit remain outstanding.

## Value — PASS

The edge count whose endpoints are both rejected measures geometric jamming beyond cardinality occupancy. Its natural joint degree weighting is invisible to the scalar jamming law. An explicit all-order bivariate identity gives the finite-size expectation and first nonvanishing correction and permits degree-conditioned observables. This gives reproducible structural information in a well-studied random-tree adsorption model, not a change of symbols or an arbitrary enumeration slice.

## Limitations

Only uniform labeled Cayley trees with iid continuous exchangeable arrival priorities are addressed. The known total-occupancy half-density and general local-limit apparatus are credited to earlier authors, and the degree-profile corollary may follow from their framework. The full bivariate finite-order series and correction remain the specifically compared statements. The 38 finite tests do not imply all-order correctness by themselves. Some older primary literature was inspected only at limited depth.

Self-review: passed. Independent audit: not yet performed.
