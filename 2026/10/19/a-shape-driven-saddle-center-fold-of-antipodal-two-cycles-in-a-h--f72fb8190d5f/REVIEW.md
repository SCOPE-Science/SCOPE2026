# Review of the antipodal two-cycle fold theorem

## Correctness — PASS

The orbit equation is established directly from the stated area-preserving map rather than a numerical plot. A positive-radius antipodal primitive cycle exists if and only if \(R_p(s)=4(1+p)/t\) with \(0<s<\operatorname{arsinh}\sqrt p\). The nonstandard global step is a strictly increasing ratio of two positive hyperbolic power series, with coefficient ratios \((4^n-1)/2\). That produces one nondegenerate maximum only for \(p>3/2\) and proves each threshold/equality case. Direct differentiation of the map identifies the hyperbolic inner orbit and the linearly elliptic companion near the fold. Taylor analysis produces the fourth-root onset and quadratic fold width. The included standalone finite checker passed 687 assertions; numerical evidence is not used as an infinite proof. The result deliberately excludes nonsymmetric cycles and nonlinear stability of the elliptic cycle.

## Originality — PASS, with a priority caveat

Dikandé's 2021 originating preprint (arXiv:2103.07727v1) and its full 2022 journal version (DOI:10.5506/APhysPolB.53.3-A1) give the planar hyperbolic potential map, analyze the first flip at \(t=4(1+p)\), and numerically trace antipodal period-two points. Their inspected text does not classify the exact number of these cycles at arbitrary positive shape, the new fold threshold, or the singular fourth-root scaling. The earlier related map analysis (arXiv:nlin/0008011v1) provides fixed-point and numerical bifurcation information but no such global census. Search comparisons with a published polynomial Duffing-map two-cycle classification concern different equations and do not subsume the theorem. Unindexed or incompletely accessible older literature could still contain an equivalent antecedent; the priority assessment is not exhaustive.

## Mathematical value — PASS

The question is inherent to the published family: deforming a bistable potential changes the onset and multiplicity of its symmetry-defined two-site spatial patterns. A sharp deformation threshold separates an everywhere single-branch regime from a wedge of two branches born in a saddle-center fold. The exact width and fourth-root critical scaling provide structural information unavailable from single-branch continuation. These claims do not require a broader chaotic-attractor theorem.

Self-review: passed. Independent audit: not yet performed.
