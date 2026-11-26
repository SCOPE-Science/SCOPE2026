---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independence gives the five-digit mask product up to unit phase; stripping common 3-powers preserves modulus. For primitive pairs the first factor is at most 2/5, and is 1/5 if both coordinates are units mod 3. At level two a transverse nonzero lift gives factor at most 2/5, and axial residues ±4 mod 9 give factor strictly less than 3/5. The only other primitive paths are signed axial residues ±1 and ±2 mod 9. At the first later departure, a transverse lift again gives factor at most 2/5. For a purely axial departure the angle is, up to cosine symmetry, 2π/3 ± δ with δ=2πa/3^j≤4π/27<π/6 for j≥3 and a≤2. This last bound uses the explicit 3^j≥27 in the proof; the weaker inequality 3^j>6a by itself would not justify the stated angle interval. The factor is then strictly below 3/5, giving a product below 6/25. A path that never departs is the corresponding ordinary signed axial integer. The positive products at a=1 and 2 are strictly ordered termwise and the chord and geometric-tail bounds give B>4466/18225>6/25. Fourier diagonalization gives the two asserted norms on the stated subspaces. An independent decimal product and analytic tail estimate reproduce the reported decimals; no finite frequency box is used in the classification.

## originality

PASS

The ordered extrema and strict gap for this equal-weight planar cross measure are distinct from the inspected related theorems. The IFS Fourier product, the geometric construction, and ternary residue pruning as a technique are not credited as new.

## value

PASS

The canonical equal-weight planar cross and its torus-convolution norms are natural. The first two moduli and all their infinite dilation families identify extremal eigenmodes, and the rigorous uniform cutoff separates them from every remaining mode. The residue calculation is model-specific, not a substitution into a formula already ranking all such measures. The separator is not claimed optimal as a bound on the third level.

The dated certificate retains the supplied scientific assessment, sources and limitations.
