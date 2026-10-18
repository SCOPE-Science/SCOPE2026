# Independent mathematical audit

## correctness

PASS

The cube support function gives W=Σ|Ui|. Each orthant is a spherical cap around v=(1,…,1)/√d, and the cap stays inside the orthant iff its angular radius ≤arcsin(1/√d), i.e. s≥√(d−1); the sphere cap fraction is I_beta/2, multiplied by 2^d orthants. If two different coordinates leave their orthant, ΣUi≤√(d−2), so below the first threshold but above √(d−2) one subtracts d disjoint one-face spherical segments exactly. Parameterizing a face by x<0 and the residual sphere gives aperture²≈2(ε+x)/√(d−1), segment area proportional to ε^(d/2) and coefficient −2^d/π(2/q)^((d−2)/2). In d=3 a spherical cap cut by a great-circle gives explicit segment angles α=acos(s/√(2(3−s²))) and γ=acos(1/√(3−s²)); subtraction yields the stated H3(s); differentiation gives lower density 4/√3(1−3α/π) and upper density 4/√3. My independent conditional-azimuth integral over x=|U1|, split at exact algebraic event thresholds to avoid quadrature endpoint bias, matched H3(s) within 3×10⁻¹⁴ over s=1.001,1.05,1.2,1.4,√2±.001,1.6,1.72. The d=3 normalized near-threshold correction/ε^(3/2) tends numerically 3.0282910514, matching the analytic constant; this tests but does not replace the all-d argument.

## originality

PASS

Best-of-knowledge explicit elementary cube distribution and all-dimensional first spherical-cap transition. Higher-moment formulas and asymptotics do not by themselves display the claimed piecewise d=3 density and first face-crossing exponent/coefficient, though they determine the distribution implicitly on compact support. A 2026 broadly relevant 3D polytope coarea preprint could encompass the cube by specialization, but its abstract only was accessible; this material coverage risk is explicitly retained.

## value

PASS

Directional width is a canonical convex-geometric random invariant. A fully elementary density in dimension three, with an exactly uniform upper-tail interval, and a sharp dimension-parameterized first nonanalytic cap-overlap transition are meaningful exact distributions, not merely re-computations of existing mean/moment tables. The first-transition exponent and coefficient also quantify singularity introduced by crossing coordinate faces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
