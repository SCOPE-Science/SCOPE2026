# Independent audit — 2026-09-30

**Record:** `2026/09/21/shimizu-morioka-stationary-height-defect-and-joint-excursion--a57215009954`  
**Repository:** `SCOPE-Science/SCOPE2026` at `253a0fe5d0217455660a277f9adb940030e567ad`  
**Audited tree:** `177c976b8521083ee276a2343833602dc2ceb3d1`  
**Disposition:** **PASSED**

## Correctness

**PASS.** For a compactly supported invariant measure, applying the generator to H(z) with H'=h gives integral h(z)(x^2-bz)=0 for every continuous h, hence E[x^2|z]=bz. Direct differentiation of W=xy-z+z^2/2+(a/2)x^2 independently gives LW=y^2-bz(z-1). These identities imply the stated defect formula. Equality forces y=0 on the invariant support; the only complete bounded orbits in that set are O and E_±. If the measure is not such an equilibrium mixture, positive mass above z=1 follows, and conditioning on that set forces positive mass with x^2>b simultaneously. The periodic-orbit corollary is then immediate.

## Originality

**PASS (literature-bounded).** The model, its equilibria, bifurcations, Lorenz attractors and general invariant-measure generator identity are prior work. Searches across Shimizu-Morioka and equivalent Rucklidge terminology did not locate the exact conditional law, square height defect, equality simplex, or simultaneous z>1 and |x|>sqrt(b) stationary barrier. The originality verdict is therefore literature-bounded rather than absolute; older Russian bifurcation literature and some complete historical sources were not exhaustively inspected.

## Scientific value

**PASS.** The result gives parameter-uniform exact stationary constraints for every compact invariant measure, not merely a particular attractor. The equality classification and simultaneous excursion threshold supply a sharp analytic diagnostic for genuinely nonequilibrium recurrent dynamics.

## Literature and evidence

- Shimizu and Morioka, On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model: https://doi.org/10.1016/0375-9601(80)90466-1
- Messias, Gouveia and Pessoa, Dynamics at infinity and other global dynamical aspects of Shimizu-Morioka equations: https://doi.org/10.1007/s11071-011-0288-8
- Llibre and Pessoa, The Hopf bifurcation in the Shimizu-Morioka system: https://doi.org/10.1007/s11071-014-1805-3

## Limitations

- The theorem assumes a,b>0 and compact support of the invariant probability measure.
- It does not prove existence, uniqueness or ergodicity of attractors or invariant measures.
- Historical-equivalence risk remains in older Shimizu-Morioka/Rucklidge literature.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
