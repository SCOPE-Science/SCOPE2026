# Uniformisation Obstruction for Fibrewise Trilinear Bogolyubov

## Context

The trilinear Bogolyubov problem asks for a structured subset (a trilinear Bohr
variety with polylogarithmic bounds) inside iterated directional differences of
a dense set A in a product G_1 x G_2 x G_3 of finite abelian groups. A natural
attack is fibrewise: apply the linear Bogolyubov-Ruzsa theorem
(Sanders/Schoen-Sisask) inside each x-fibre, then pigeonhole or intersect the
resulting Bohr sets to obtain one fixed x-uniform Bohr set of rank depending
only on the density delta. The following lemma shows this uniformisation step
is impossible in general: per-fibre spectra can vary over the whole dual, and
any fixed Bohr set covering many fibres must pay ambient-dimension rank.

## Definitions

Let n >= 1, G_1 = G_2 = F_2^n, G_3 = F_2, with standard dot product
<x,y> mod 2. Define

  A_n = {(x,y,z) in G_1 x G_2 x G_3 : <x,y> = 0}.

For (y,z) write A_{y,z} = {x : (x,y,z) in A_n} for the x-fibre and
H_y = {x : <x,y> = 0}. Characters of F_2^n take values +/-1, so for a Bohr
set B(Gamma;rho) in G_1: if rho >= 1/2 then B = G_1; if rho < 1/2 then
B(Gamma;rho) = intersection_{a in Gamma} ker(chi_a), the annihilator subspace.

## Result

Lemma (Fibrewise uniformisation obstruction). For A_n above:

1. Density d(A_n) = 1/2 + 2^{-(n+1)} >= 1/2, uniformly bounded away from 0.
2. Every x-fibre equals H_y independent of z: H_0 = G_1 and H_y = ker(chi_y),
   an index-2 subgroup, for y != 0; each satisfies H_y - H_y = H_y.
3. Intersection over y != 0 of H_y is {0}.
4. Let B(Gamma;rho) be any Bohr set in G_1. If rho >= 1/2, B = G_1 lies in no
   proper H_y. If rho < 1/2, B is the annihilator above and B subset H_y iff
   chi_y in span(Gamma). Hence (a) no fixed B with |Gamma| <= n-1 lies in all
   H_y, y != 0; (b) a fixed B lies in H_y for at least a fraction c > 0 of
   y in G_2 only if |Gamma| >= n + log_2(c).

Consequence: at fixed density >= 1/2, any fixed x-uniform Bohr set covering a
positive fraction of fibrewise difference sets needs rank linear in n; no
delta-only (let alone absolute) rank bound is possible at this stage. Any
trilinear Bogolyubov proof must use genuinely (y,z)-varying Freiman-linear
frequencies M_k(y,z), as in the admitted target, and the cost of correlating
them is the remaining quantitative inverse gap.

## Proof / Evidence

Density: for y = 0 all x qualify; for y != 0 exactly half do; doubling over
z in G_3 gives 1/2 + 2^{-(n+1)}. Fibre identity is by definition; subgroups
satisfy H - H = H. Trivial intersection follows from nondegeneracy of the dot
product. Bohr dichotomy follows from character values {0,1/2} in torus
distance. Containment-iff-span is standard linear duality: if
chi_y not in span(Gamma), extend to a dual vector vanishing on Gamma but not
on y. Quantitation: |span(Gamma)| <= 2^{|Gamma|} versus |G_2| = 2^n, so
covering fraction c needs 2^{|Gamma|}/2^n >= c. The y = 0 fibre (whole group)
is included: rho >= 1/2 gives B = G_1 in no proper fibre; rho < 1/2 gives the
annihilator, contained in H_0 automatically, not affecting the count over
y != 0.

Machine verification: output/artifacts/obstruction_verify.py brute-forces
n = 2,3,4 (density, fibre identity, difference identity, trivial intersection)
and 344 + 533 random annihilator duality checks for n = 2,3; results stored in
output/artifacts/obstruction_verify_result.json; rank table n + log_2(c)
printed for n <= 20.

## Limitations

The lemma obstructs only the fixed x-uniform fibrewise strategy; it does not
refute the full trilinear Bogolyubov target (which permits varying M_k(y,z))
nor proves any positive trilinear containment. Brute-force verification covers
n = 2,3,4; general n rests on the exact duality proof.

## Reproducibility

Run `python3 output/artifacts/obstruction_verify.py`; exit 0 and densities
0.625, 0.5625, 0.53125 with trivial intersections reproduce the JSON record.

## References

- Sanders, Bogolyubov-Ruzsa lemma (linear, polylog bounds).
- Schoen-Sisask, robust linear Bogolyubov-Ruzsa.
- Hosseini-Lovett, bilinear Bogolyubov-Ruzsa with polylog bounds (2019).
- Milicevic, bilinear Bogolyubov argument in abelian groups (2024).
