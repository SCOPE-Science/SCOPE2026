---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Weight-one differences with nonzero f-image force associated parity rows of weight>=3; weight-two differences with distinct nonzero images force parity-row pair distance>=2. Fix one parity coordinate: hypercube matching pairs by its toggle have 2^(r-1) pairs, of which exactly r (prefix weights 0 or 1) have both endpoints weight<=2, hence <=2^(r-1)-r selected rows; this lower bound is sharp by assigning distinct odd-weight rows of weight>=3. For x with wt<=3 and f(x)!=0, 1,2,3 selected nonzero rows give nonzero parity in the necessary cases (three odd-weight rows have odd XOR; two distinct labels do not cancel). For larger x, systematic weight >=4. The proof treats zero/repeated images and empty function. Independent small-dimensional exhaustive parity testing found no violation; finite cases complement the uniform algebraic proof.

## originality

PASS

Ho explicitly addresses systematic linear separation and solves distances <=3, with distance-four listed as later work according to the inspected abstract/published summary; the all-binary ν(f) invariant extends the classical extended Hamming identity-function case. The older Clark–Dunning–Rogers set-function/parity-check work is an unresolved priority risk because its full text could not be inspected; access alone does not justify scientific rejection.

## value

PASS

This determines an entire natural binary systematic function-correction problem at the first separation beyond earlier studied distances, including functions with kernels, zeros and repeated nonzero image columns. The ν invariant is an unexpectedly complete reduction from a global family of protected-message constraints to one discrete count; the tight matching construction is independently useful for systematic code design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
