# Independent mathematical audit

## correctness

PASS

Any symmetric S⊂K with center c obeys S⊂M(c)=K∩(2c−K), which is itself convex and centrally symmetric; hence optimization reduces exactly to the centers. For c=(s,z), at axial coordinate x, the transverse section is the overlap of two Euclidean (n−1)-balls of radii sqrt(1−x²), sqrt(1−(2s−x)²). Displacing z≠0 strictly decreases the section area on a positive-measure neighborhood of x=s whenever the core is positive-volume, so the optimum lies on the cut axis. For axial centers the formula is F(s)=2κ_{n−1}∫₀^{min(s−a,1−|s|)}(1−(|s|+u)²)^{(n−1)/2}du. Negative s is strictly inferior to s=0. On 0≤s≤(1+a)/2 the derivative has sign 2 f(2s−a)−f(s) and the ratio f(2s−a)/f(s) strictly decreases; beyond the midpoint F strictly decreases. Thus s=0 is optimal exactly for a≤−sqrt(1−q), q=2^{−2/(n−1)}, else the unique positive quadratic root s=[2a+sqrt(q a²+(4−q)(1−q))]/(4−q). Integrating f_3 gives β_3(0)=2/sqrt(7). Thin cap a=1−h expansion gives ratio (2−q)^{−(n−1)/2}, tending to 1/2 as n→∞. Independent SciPy quadrature/one-dimensional optimization for 81 n,a configurations agreed with the analytic center core value within 8.5×10⁻13; no finite search replaces the proof of transverse optimality or all-dimensional monotonicity.

## originality

PASS

Classical Macbeath reflected intersections supply the right optimization reduction but not the one-cut ball’s exact moving center and dimensions-dependent threshold. The Meyer–Schütt–Werner paper introduces affine-covariant-point measures, not the volume-maximizing symmetric core; directly relevant 2015 harmonic-mean article full text inaccessible, with only abstract compared and specific residual risk. Resultary Reuleaux-gon symmetric area and parallel-plank ball-volume results concern different bodies/functionals. The multi-dimensional phase law survives as best-of-knowledge new.

## value

PASS

Kovner–Besicovitch maximal centrally symmetric subset is a classical natural measure, and a unit ball clipped by one plane is a simplest continuous family breaking central symmetry. The sharp locked/unlocked center transition, unique global optimizer over ALL symmetric subsets, hemisphere constant and thin-cap limit are explicit structural information not supplied by general symmetry lower bounds or unrelated clipped-body area calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
