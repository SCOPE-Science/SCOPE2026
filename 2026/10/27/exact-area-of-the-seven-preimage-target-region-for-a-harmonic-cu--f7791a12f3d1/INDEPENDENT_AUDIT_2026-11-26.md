# Independent mathematical audit

## correctness

PASS

The frozen finding is false as a topological statement: the critical value 0 is deleted, making the set non-star-shaped about any point and adding an isolated boundary point. The frozen proof also wrongly says the near-zero split has opposite signs; the two inner preimages both have negative Jacobian. The full corrected result in repairs/4/RESULT.md proves the punctured radial domain and preserves the exact area. Independently checked: the lifted caustic angle decreases by 4π, so a ray gives two radii; signed crossings give wind -2 precisely below both, and degree three plus negative disk degree gives seven preimages. Choosing h in (0,π/2] for a double point reduces its equation to |4 cos²h-1|=3 cos h; the only allowable solution cos h=1/4 gives five images and two explicitly nonparallel derivatives at each. Checking C(0) and C(π) selects the inner arc, with rotation giving all five. Green's theorem on the filled domain then gives the stated formula, and F_b(bu)=b³F(u) proves the scaling. Independent polar inversion by bisection and a periodic 4,000-ray midpoint grid yielded 0.0803254871 versus the closed form 0.0803255144; this numerical check is not the proof. Replay: repaired RESULT.md Proof and Reproducibility; frozen verify_area.py and VERIFICATION.md were inspected, not executed, and their finite checks do not establish the topology. Applies only to regular targets of this map and its positive rescalings.

## originality

PASS

For the repaired claim, the distinct result supported by the inspected evidence is the exact unweighted target-plane area and its specific smaller radial envelope, not the use of harmonic degree or the existence of seven roots. The strongest available close comparisons concern zeros in other parameter spaces or harmonic interpolants and do not fix the selected arcs of this caustic. This is a bounded judgment, not a historical-priority assertion.

## value

PASS

The maximum-regular-valence cell of a natural harmonic binomial is singled out by the map, not by arbitrary parameter sampling. Its unweighted area quantifies how large the seven-preimage ambiguity region is, which counts or signed total caustic area cannot supply. The exact double-point and envelope calculation explains the area and supplies a reproducible benchmark; the puncture correction makes the geometric claim precise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
