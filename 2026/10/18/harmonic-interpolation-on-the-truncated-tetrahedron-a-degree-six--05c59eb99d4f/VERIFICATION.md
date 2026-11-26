---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The dot product of ordered-edge vertices has numerator −9+4(4δ_ik+2δ_il+2δ_jk+δ_jl). Its classes give the stated row-sum operator, which on constants, symmetric zero-row-sum arrays, and antisymmetric zero-row-sum arrays has exactly the three scalar actions claimed. Source and target coordinate arrays from the sum-zero four-vertex space are perpendicular to those three subspaces; substituting them gives the two columns of the displayed block. Their basis metric on each pair is proportional to [[3,−1],[−1,3]], so any block pseudoinverse must use its inherited inner product, not a Euclidean pseudoinverse of the nonorthogonal matrix. The addition theorem gives Gram = (2ℓ+1) times the normalized matrix. A newly written raw-Gram check, using the original coordinates and not the frozen code, reproduced ranks 1,3,5,7,9,11,9 by exact row reduction and positive definiteness by rational Schur pivots at every degree 7–575 (569 degrees). It also verified that the four oriented triangular cycles span a three-dimensional kernel at degree six. Orthogonality to these vectors is the zero-circulation condition, and the lone zero block at degree five is the constants. The finite check is not an infinite proof: in the Laplace integral, the absolute integrand is (1−(1−t²)sin²θ)^(ℓ/2); bounding it by a Gaussian on each half interval gives the stated √(π/[2ℓ(1−t²)]) estimate. Thus at ℓ≥576 the squared row bound is less than 322102/(560ℓ)<1, giving strict diagonal dominance. The kernel interpolant uses (2ℓ+1) times the normalized Gram and is the minimum-norm solution because it lies in the orthogonal complement of the evaluation kernel. Finite replay from the workspace root: python3 reproductions/4/independent_gram_check.py --max-degree 575; output in reproductions/4/full_run.txt.

## originality

PASS

The bounded comparison did not establish antecedent coverage. A distinct catalogue record indexed under a later date demonstrably contains the entire rank law and the equivalent degree-six kernel; these are not unique to the assigned text in the current catalogue. The index dates do not establish priority or derivation. The assigned uniform spectral-block formulas are not supplied by that record's rank certificates. The inspected earlier geometry, harmonic-design and transform passages do not imply the fixed-orbit rank or spectral law.

## value

PASS

The orbit is the classical uniform truncation, and exact-degree interpolation asks a different question from bandlimited sampling. The sample rank drops despite increasing source dimension, with a precise geometric obstruction in edge circulations, then recovers permanently at the next degree. The block spectrum provides structural information beyond a rank table and a way to solve interpolation in each sample channel. The finding does not rely for its value on high-degree eventual invertibility alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
