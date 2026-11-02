---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

There are 31 rational points/lines of PG(2,5), 10 homogeneous cubic monomials, (5^10−1)/(5−1)=2,441,406 scalar-normalized equations. A rational smooth curve point has a unique nonzero gradient whose orthogonal 6-point rational line is its tangent; union masks yield coverage. Independently programmed an exact GF(5) C enumerator for ALL normalized equations, recovered complete 32-bin source histogram, maximum 29 and 186,000 winners, with 93,000 each at rational point counts 8 and 10. Independently generated five polynomial substitution matrices and enumerated all 186,000 maximizing forms under GL3 generator action; exactly TWO PGL3 orbits each 93,000. |PGL3(F5)|=372,000 gives stabilizer four. Read actual source independently implemented gradient and flag enumerators and their polynomial code: both finite methods exhaust same domain; projective representative checks and partial derivative contradictions over algebraic closure prove geometric smoothness for each representative. Verification is finite exhaustive of exactly the claimed fixed field; none asserts other fields.

## originality

PASS

Prior Asgarli–Ghioca tangent-filling theory and earlier F5 no-filling obstruction rule out coverage 31 but do not establish the sharp coverage maximum 29 or the exact two-orbit equality classification in the inspected full primary theorem. Coolsaet complete (k,3)-arc classification is related finite incidence classification but no mathematical implication to this tangent coverage was established; its full content was not read, preserving priority risk. Best-of-knowledge PASS.

## value

PASS

This is a complete fixed-field extremal classification for a natural tangent-filling question: strictly stronger than merely showing cubics are non-filling, with two different elliptic smooth extremal orbits and sharp two-point coverage deficit. Natural exact finite invariant even without extension to all prime powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
