---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The supplied `rank_kernel_checker.py` uses Python's standard library, computes all symbolic transfer coefficients in exact integers, and independently enumerates all self-maps on finite labeled sets of sizes one through six. Each idempotent is detected by explicitly checking the equation \(f\circ f=f\). The checker compares the distribution of \(|f(A)|\) for each specified size of \(A\) against the formula, and checks every coefficient, nonnegativity, row-sum identity, strict diagonal inequality and idempotent total count. For sets through size four, it separately enumerates all ordered pairs of idempotents and compares product-image rank counts with the squared kernel, including the direction-asymmetry counts at size four. Additional exact-arithmetic identities are checked for sizes seven, nine and twelve.

The final execution returned `ALL_EXACT_CHECKS_PASSED`. The number of idempotents for ground-set sizes one through six was respectively \(1,3,10,41,196,1057\). At four points the exact kernel diagonal was \((41,25,7,1)\), its two-step rank distribution was \((636,948,96,1)\), and the ordered factor-rank triples \((2,3,1)\) and \((3,2,1)\) occurred \(48\) and \(36\) times.

These computations are finite corroborations. The general claim for every \(n\) and every product length rests on the occupancy bijection and triangular-matrix proof in `RESULT.md`. There is no claim of independent mathematical audit or of a uniform asymptotic as \(n\) grows.
