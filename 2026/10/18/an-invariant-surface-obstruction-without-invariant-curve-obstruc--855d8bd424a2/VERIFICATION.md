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

For every integer a≥4 the 12 listed maximal cones have unimodular determinants and exactly 18 two-cone walls. Independently computed each symbolic primitive wall relation using SymPy matrix inverses with a symbolic integer parameter; all 18 anticanonical degrees agree with the source table: constants 2,-1,2,3,2,3,-1,1,2,2,-2,2 and affine terms a+2,1-a,a+1,3-a,a+1,1-a, with none zero for a≥4. Ray-seven star is the fan with five rays (1,1),(1,0),(0,-1),(-1,0),(0,1), hence Bl_p(P1×P1). The classes F1,F2,E form a Picard basis; boundary degree data (2,1,3) imply (-K)|S≡F1+2F2−3E. A general (1,1) curve through p is smooth irreducible rational, has strict transform F1+F2−E, is non-toric, and intersects L by 1+2−3=0. The quoted complete-curve tensor-generation criterion then proves non-generation. For every m≥1, sections of O(mL) are (m,2m)-biforms vanishing order≥3m at p, leaving just s^m t^{2m}; -mL has no sections after push-forward. This analytically justifies the invariant-surface obstruction beyond finite checks. The non-projectivity is established by the original Fujino–Sato primitive relation argument at b=2 and a≠0. Check relies on published tensor-generation criterion and fan classification, not re-proved here.

## originality

PASS

Qualified best-of-knowledge PASS for the explicit infinite canonical-bundle counterfamily, not for the old general criteria. Ito–Zeng–Zeng formulate the all-parameter / invariant-(-1,-1)-curve question and discuss different subfamilies; this computation supplies a family of smooth nonprojective Z13 fans with all 18 invariant curve degrees nonzero but a non-invariant rational degree-zero curve. Fujino–Sato predate the submission and supply the fan, its primitive relations and non-projectivity, but inspected pp.16–18 concern birational/projectivity transformations, not the stated canonical tensor-generation classification. Directly relevant full Ito–Zeng–Zeng HTML/PDF could not be retrieved in this run; authorized institutional download reported VPN disconnected. Consequently there is a residual possibility of stronger previously proved or transformed equivalent statements; no exhaustive priority certification is claimed. Unrelated Resultary hits and unsuccessful exact searches alone were not regarded as proof of novelty.

## value

PASS

The explicit Question 6.6 about a natural non-projective four-parameter toric family motivates exactly this obstruction classification. The theorem gives an infinite counterfamily to invariant-(-1,-1)-curve-only tests, despite all 18 invariant curve canonical degrees being nonzero; the blowup-surface class and non-invariant rational curve explain the obstruction geometrically, not by an arbitrary isolated negative case. A later worker studying tensor-generation or invariant-curve test completeness would need precisely such an example. It does not claim a complete classification, new general categorical criterion, or autoequivalence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
