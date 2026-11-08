---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The 2N+1 rational confluent interpolation conditions at 0 and N pairwise-distinct positive squared nodes are nonsingular, giving a unique P of degree <=2N. Independent SymPy exact linear systems produced P_1,P_2,P_3 with degrees 2,4,6 and verified all data. Direct orbit substitution at A=(0,j²,0), B=(j,0,j²), C=(j,-j²,j²) gives prime-three cycles. The first two Jacobians coincide in a square-zero matrix, so the 3-return differential vanishes and polynomial Taylor remainder is quadratically contracting in a small neighborhood. Independent symbolic multiplication found (DF)^3=0 identically for unrestricted formal x,u,v. The polynomial coordinate conjugacy reduces fixed/2-cycle equations to zero; no numerical claim is used to establish all-N.

## originality

PASS

Best-of-knowledge originality of the exact final combined claim, after reviewing primary statements and Resultary hits; credited known partial antecedents. The map is a sign/coordinate variant of an already studied Chamberland/Castañeda family, explicitly acknowledged; the newly asserted object is simultaneous multiplicity of three-cycles with zero return derivatives, not construction of the family or proof of a single nonrepelling three-cycle. Castañeda–Rebollo-Perdomo Theorem 1.1 proves one nonrepelling three-cycle and excludes 2-cycles in a broader family but does not assert simultaneous arbitrary multiplicity; its concluding Section 5 asks whether a 3-cycle might be unique and attracting. The result answers that stated uniqueness question negatively via rational Hermite interpolation. An existence criterion for one nonrepelling orbit and a general Hermite theorem suggest a short proof but do not themselves assert or logically guarantee N simultaneous prime-three superattractors with the same polynomial without constructing and analyzing simultaneous derivatives. This proximity is a material priority risk, not a reason to conceal antecedents.

## value

PASS

An explicit all-N counterexample to uniqueness of attracting three-cycles in an everywhere-nilpotent-Jacobian family resolves a concrete published question. It separates local return contraction from pointwise Jacobian nilpotence and gives a useful uniform degree-cost construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
