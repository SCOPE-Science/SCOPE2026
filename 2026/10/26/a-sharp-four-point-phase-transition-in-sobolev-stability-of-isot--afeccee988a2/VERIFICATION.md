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

The estimator is the Euclidean projection, not Sobolev projection; only the input/output norm uses Q=I+gamma D^T D. Every contiguous block composition has a strict KKT interior: take centered strictly decreasing residuals inside each block (all proper prefix sums positive) and strictly increasing block means. On that cell P is block averaging. For a straight segment the finitely many affine pieces give the maximum-cell norm bound by summing segment lengths, also on faces by continuity. Inside any strict cell a small displacement in an operator-norm maximizing direction gives an actual sharp pair. Independently, with B the block-indicator matrix and G=(B^TB)^(-1), I compressed the nonzero eigenvalues of Q^(-1) E Q E to those of G(B^T Q B)G(B^T Q^(-1)B); the exact factorization for n=2,3,4 and KKT checks for both printed attaining pairs are replayable with python /workspace/checks/2.py using SymPy (output /workspace/checks/2.txt). The only nonunit largest roots are A, B, H as printed. H is strictly dominated, A-B has the sign of 2 gamma-1 and derivative 1/126 at equality. The crossing gives 15/14 and a derivative jump of 1/126 for the squared modulus, with all four maximizing cells at equality. The leading coefficient ratio is 14/9; n=2 has no amplification and the mirror pair-cells tie for all gamma>0 at n=3. No limiting argument for larger n or unsupported inference from numerical data is needed. The submitted checker was inspected, not executed.

## originality

PASS

The supported distinct claim is the sharp finite-positive-coupling amplification and its change of maximizing pooling patterns. Yang–Barber's same-map theorem supplies a criterion for contractivity, not the modulus above one; another same-map Resultary record studies only the gradient seminorm without vertex masses. Exact formula and transition do not follow from either. Remaining literature access risks are stated separately.

## value

PASS

Ordinary isotonic denoising applied to data with path-weighted errors can amplify the gradient contribution even though it is Euclidean-nonexpansive. The smallest chain with a change in the extremizing block geometry and an exact cusp is a useful sharp sensitivity benchmark, not merely an example of failure of contraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
