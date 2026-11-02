---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: Differentiating cubic words forces both generator-image constant terms to vanish for every characteristic, and freely choosing linear M∈M2(F_q) and quadratic B∈M_{4x2}(F_q) gives exactly q^12 derivations. On V⊕(V⊗V), D=[[M,0],[B,T_M]] with T_M=M⊗I+I⊗M. Its rank equals rank M+rank T_M plus rank of uniform induced map ker M→coker T_M. For odd characteristic the T_M ranks from cyclic 2x2 normal form partition M into zero, rank1 trace0, rank1 trace nonzero, invertible trace0 and invertible trace nonzero; in characteristic2 nonzero scalar M gives T_M=0, all nonscalars rank T_M=2. Exact 2x2 class sizes and uniform B fiber law give all displayed N0..N6; sums equal q^12. Independently enumerated all 2^12=4096 derivations via bitwise exact rank over F2, obtaining [1,45,466,576,3008,0,0] (matches theorem). The inspected full source check_derivations.py additionally describes exhaustive F3 and sampled F4/F5 checks, but its logged results alone were not used as proof.

## originality

PASS

Best-of-knowledge comparison of the precise claim against related primary statements, algebraic implications, four named searches, and inspected published records; prior building blocks acknowledged, with explicit limitations for inaccessible full texts.

## value

PASS

PASS: The radical-cube-zero two-loop free algebra is the natural smallest two-generator noncommutative truncated algebra with an induced tensor-square action. Complete rank frequencies and the sharp characteristic-two six-to-four collapse give substantive structure not implied by the dimension of Der or by module homological invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
