---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For each finite block the eigenvalues are \(e^{i\theta_j}\) in the nonorthogonal basis used by the construction. Monotonicity of the positive phases gives finite total variation of \(e^{-i\theta_j}\), so the same partial-sum-projection summation-by-parts estimate bounds the inverse blocks uniformly. For rotated Cesàro kernels \(F_m(t)=m^{-1}\sum_{k=1}^m e^{ikt}\), the identity \(F_m(-t)=\overline{F_m(t)}\) makes the variation sequence for \(\phi-\theta_j\) exactly the forward variation sequence at rotation \(-\phi\). Thus the block-uniform forward multiplier estimate transfers unchanged to \(T^{-1}\). The original signed-average obstruction remains a forward property of the same \(T\), so failure of strong Cesàro boundedness persists.

## originality

PASS

The accessible primary Arnold statement proves only existence of a uniformly Kreiss bounded Hilbert operator that is not strongly Cesàro bounded. Cohen--Cuny--Eisner--Lin study stronger/different absolute-Cesàro, strong-Kreiss and power-growth questions. Resultary searches found no prior two-sided uniform-Kreiss statement. The inverse symmetry is a short strengthening of a very recent construction, with a real access residual risk rather than fabricated noncoverage.

## value

PASS

Requiring the same counterexample to satisfy uniform Kreiss control in both time directions is a mathematically meaningful strengthening: it rules out a natural explanation that the one-sided separation is caused by bad inverse dynamics. The result places a sharp symmetric counterexample next to older two-sided Cesàro questions, even though the new proof is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
