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

In RESULT.md:32–71, use both empty and full prefixes, with T,H,B the seven-coordinate totals, maxima and minima. For 0≤n<2^r, t(2^r+n)=−t(n), and the second half shifts residues by δ_r=2^r mod 7. Thus its prefix values in class j are T_j minus the first-half prefix values in class j−δ_r. This proves the total, max and min transitions exactly, with the stated initialization at r=0. Independent direct digit-parity enumeration at r=7 and 19, not iteration of the proposed transition, reproduced the full two rows of the certificate and all 21 affine equalities (replay: /workspace/reproductions/4.py). The update with phase δ_r commutes with (T,H,B)↦(49T,49H+32,49B−32): for example both max alternatives acquire +32, and both min alternatives −32. Since δ_{r+12}=δ_r, induction proves all r≥7. At j=0, H_7=1 and B_7=−9 give both closed forms; 49^(r/12)=2^(αr) and the twelve progressions bound all prefixes. The extrema magnitudes grow like 49^k at lengths at most 2^(12k+7). Their attaining prefix lengths must diverge, and the normalization stays bounded away from zero along both sequences with opposite signs. The supplied checker was inspected, not executed. Its reported 131071 nonempty checks count all levels 0–16 cumulatively, not the largest level alone; it uses int.bit_count, requiring Python 3.10+ rather than the stated 3.8+. These documentation points do not affect the integer certificate or induction.

## originality

PASS

Credit the prior spectral exponent and rarefaction/sign framework. The supported distinct claim is an exact affine recursion for extrema over finite dyadic prefix windows, with additive constants and a proved starting level across all seven residue classes. The strongest inaccessible same-object paper leaves real priority risk, but the inspected passages and indexed matches do not establish equivalent coverage.

## value

PASS

These natural finite-scale envelopes measure both overshoots of a classical oscillatory rarefied sum, not just its growth order. The exact affine constants and all-residue law determine an infinite family of extremal values from finitely many seeds at high levels, quantitatively distinguishing it from a homogeneous rescaling. No claim is made for exact normalized limsup or liminf constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
