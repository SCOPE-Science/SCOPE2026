# Independent audit — SCOPE-20260914-015

Date: 2026-09-28 (UTC)  

## Disposition: REPAIRED

### Correctness
The finite train-track computation survives, but the proof needed a theorem-attribution repair. Independently recomputed data give det M=-1, characteristic polynomial x^4-x-1, strictly positive M^10, seven gates with unique illegal turn {A,B}, a 13-turn Df-closed taken set avoiding that illegal turn, connected local Whitehead graph, and stable graph K_{4,3}. Absence of taken illegal turns rules out PNPs. Full irreducibility should then be concluded from Pfaff's Full Irreducibility Criterion—PNP-free train track plus Perron-Frobenius transition matrix plus connected local Whitehead graphs—not from irreducibility and Whitehead connectivity alone. With that correction, ageometric full irreducibility, atoroidality, IW=K_{4,3}, index [-5/2], and the rotationless power f^12 all follow.

### Originality
Moderate as an explicit rank-4 example/invariant computation. Pfaff already proves the general full-irreducibility criterion and constructs broad ideal-Whitehead-graph families, including complete (2r-1)-vertex graphs; no retrieved source contained this exact substitution or its K_{4,3} graph.

### Scientific value
Moderate-to-high for geometric-group-theory examples: it packages a short substitution with a complete finite turn certificate and nontrivial ideal Whitehead graph.

### Repair
Replace RESULT.md and METADATA.json so the proof invokes Pfaff's Full Irreducibility Criterion only after establishing PNP-freeness, corrects the reproducibility path, and distinguishes exact algebra from NumPy sanity checks.

### Sources checked
- Pfaff, Ideal Whitehead Graphs in Out(F_r) II: The Complete Graph in Each Rank: https://catherinepfaff.com/CompleteGraphs.pdf — Contains the Full Irreducibility Criterion used in the repaired proof and prior ideal-Whitehead-graph constructions.
- Train-track/ideal-Whitehead-graph background in IMRN: https://academic.oup.com/imrn/article/2019/14/4549/4791942 — Definitions and modern context for train-track representatives and ideal Whitehead graphs.
- Brinkmann, Hyperbolic automorphisms of free groups: https://arxiv.org/abs/math/9906008 — Hyperbolicity/atoroidality background for mapping tori of free-group automorphisms.

### Limitations
- The repository script's NumPy determinant/characteristic-polynomial lines are floating sanity checks; the exact values were independently verified by integer algebra.
- Atoroidality and rotationless-index deductions use standard train-track theorems rather than being re-proved from first principles.
