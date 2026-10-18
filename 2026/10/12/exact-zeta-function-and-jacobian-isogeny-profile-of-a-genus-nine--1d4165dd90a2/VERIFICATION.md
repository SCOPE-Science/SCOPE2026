---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Exact F2 field enumerations for 1≤n≤9 independently yielded smooth N_n=(4,8,4,24,44,8,116,312,508) after adding the asserted eight Artin–Schreier pole points (4 over odd n, 8 over even n). Independently formed Newton coefficients (1,1,2,0,2,2,−4,−8,−11,5), then the genus-nine functional equation reconstructs the degree-18 numerator, which factors into quadratic 1−T+2T², double quadratic 1+T+2T², quartic 1−T²+4T⁴, octic 1−2T²+T⁴−8T⁶+16T⁸, and evaluates to P(1)=1024. This is exact through the genus 9 FE, not extrapolation from nine sampled degrees. The eight-simple-pole normalization and genus premise is accepted conditionally on the cited primary Proposition 7.2, which could not be independently read.

## originality

PASS

The 2026 source introduces this precise genus-nine curve, ramification and automorphisms; publicly retrievable abstract does not give the complete zeta numerator or Jacobian factorization. Finite arithmetic here is not supplied by a general Jacobian isogeny principle without the actual extension counts. Full Tafazolian paper inaccessible, so no whole-document novelty exclusion is asserted; best-of-knowledge PASS with significant priority risk.

## value

PASS

The zeta function and Frobenius isogeny factors are fundamental exact arithmetic invariants of a distinguished Nakajima-extremal genus-nine curve; their determination is independently useful even absent a family-wide theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
