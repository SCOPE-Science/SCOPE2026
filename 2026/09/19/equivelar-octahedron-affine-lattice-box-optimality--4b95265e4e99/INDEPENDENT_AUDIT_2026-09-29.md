# Independent Audit — 2026/09/19/equivelar-octahedron-affine-lattice-box-optimality--4b95265e4e99

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `904fd248ff4c3e1701bf8820692d1d706e7ff4e6`
- Disposition: **PASSED**

## Correctness

**PASS** — The affine-lattice argument is exact. Recomputing from the 24 normalized coordinates gives coordinate ranges x,y in [-100,100] and z in [-78,78], hence spans (200,200,156). The two submitted difference-lattice minors evaluate exactly to -8 and 1325; their gcd is one, so the Z-span of all vertex differences has index one and equals Z^3. Therefore any affine map F(x)=Ax+b taking every vertex to Z^3 must have A Z^3 subset Z^3, so A has integer entries. The exact differences v5-v8=(0,200,0) and v24-v20=(200,0,0) imply w_V(a,b,c)>=200|a| and >=200|b| for every integer row covector. Thus every nonvertical primitive direction has width at least 200, while primitive vertical directions are ±e3 with width 156. An invertible integer A has three independent rows, at most one of which can be vertical, so after sorting its coordinate spans are at least (156,200,200); the identity attains equality and gives volume 6,240,000. The theorem is correctly limited to the integral-affine orbit, not all realizations of the combinatorial surface.

## Originality

**PASS** — Mizhaev's September 2026 preprint supplies the integer realization, exact coordinates, incidence data and C4 symmetry. The 2020 precursor supplies the earlier geometric construction but its accessible abstract does not state an integer-affine width optimization. The audited result notices the common factor three, proves the normalized difference lattice is saturated, and derives a sharp affine-orbit bounding-box profile from two forcing differences. Targeted searches for an affine-lattice or lattice-width optimality theorem for this equivelar octahedron found no prior statement. Older minimal-coordinate work concerns different genus-3 triangulations and global coordinate searches, not the affine orbit of this eight-nonagon realization.

## Scientific value

**PASS** — The result upgrades a coordinate certificate into a canonical primitive integral normalization and a sharp optimization theorem throughout its full integral-affine orbit. It proves that the visibly large coordinates cannot be reduced within that orbit by any more sophisticated integer affine change, while clearly separating this from the harder open problem of global coordinate minimality among unrelated realizations. The proof is short but gives a clean lattice-geometric invariant and reproducible exact certificate.

## Sources

- Integer Realization of an Equivelar Octahedron of Genus 3 (Ruslan Mizhaev): https://arxiv.org/abs/2609.17700 — Primary 2026 source for the 24 integer vertices, eight planar nonagons, exact verification and C4 symmetry.
- Equivelar octahedron of genus 3 in 3-space (Ruslan Mizhaev): https://doi.org/10.31219/osf.io/hvtey — 2020 precursor for the same incidence construction; accessible metadata/abstract does not state the audited affine-lattice theorem.
- Polyhedra of genus 3 with 10 vertices and minimal coordinates (Stefan Hougardy; Frank H. Lutz; Mariano Zelke): https://arxiv.org/abs/math/0604017 — Prior global minimal-coordinate work for different genus-3 triangulations, not this affine orbit.

## Limitations

- Optimality is only among invertible affine images of this displayed realization that remain integer-coordinate; no global minimum over all realizations is claimed.
- The full 2020 precursor text was not independently inspected in this run; its accessible abstract leaves a residual historical risk for an incidental coordinate observation, though not an evident covering theorem.
- The theorem optimizes axis-aligned spans after integral affine changes, not Euclidean diameter, face quality, or arbitrary real affine aspect ratio.

## Independent checks

```json
{
  "min_coords": [
    -100,
    -100,
    -78
  ],
  "max_coords": [
    100,
    100,
    78
  ],
  "spans": [
    200,
    200,
    156
  ],
  "minor_15_17_23": -8,
  "minor_2_12_15": 1325,
  "minor_gcd": 1,
  "forcing_differences": [
    [
      0,
      200,
      0
    ],
    [
      200,
      0,
      0
    ]
  ],
  "attained_box_volume": 6240000,
  "proof_reconstructed": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. The dated independent-audit pair was verified absent before staging this change set, and `VERIFICATION.md` was read at blob `31a3bb079c3be0cdcbee536377edadb1613bf629`. GitHub was used only as read-only evidence; no repository write was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this run.
