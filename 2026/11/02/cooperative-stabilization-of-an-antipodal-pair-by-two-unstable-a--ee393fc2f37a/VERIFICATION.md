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

In each head, the weight matrix at the pair has eigenvalues 1 and q_h on the symmetric and antisymmetric token directions, with (q_1,q_2)=(1/2,3/4). The joint unnormalized radial gain is 9/4. Score derivatives vanish on the tangent because all perturbations have zero first coordinate and the base second coordinates vanish. Thus in coordinate two the pre-normalization multipliers are 1+4-4=1 and 1+4q_1-4q_2=0. Both token directions in each of coordinates three and four have pre-normalization multiplier 1. Spherical normalization scales all six by 4/9. The isolated radial gains are 3/2 and 7/4, giving symmetric transverse multipliers 10/3 and -12/7, and antisymmetric multipliers 2 and -8/7. The joint derivative has Euclidean norm 4/9 in a tangent chart, hence a small invariant contracting neighborhood exists. The derivative minus the identity is invertible, so the implicit function theorem and continuity of the derivative give a unique nearby attracting fixed point under small smooth parameter changes. Within the bias-free architecture, the swap-and-negate symmetry actually forces the nearby fixed point to remain antipodal; that symmetry need not hold for general perturbations. check.py lines 41–74 and checker_output.txt were inspected, not executed: the rational identities, six finite-difference columns and finite trajectory tests are corroboration, not the proof or a formal certification.

## originality

PASS

The supported distinct claim is an explicit stable antipodal fixed point of the cited discrete two-head architecture with both specified isolated ablations expanding, not a new general stability theorem or the first instance of antipodal behavior in attention. No inspected statement supplies or implies this conjunction.

## value

PASS

The exact example answers an existence question explicitly left open in the same architecture and tests the substantive inference that head-wise expansion rules out joint attraction. It isolates cancellation of the antisymmetric transverse update independently of radial gain, and shows the joint attraction is not conditional on exact tuning of the full Jacobian. This is a useful local counterexample, not a claim about practical transformer behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
