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

# Verification of order-four three-term zero-sum classification

The unrestricted argument is the five-pattern proof in `RESULT.md`. The identities \((q^2+2)(q^2-2)-(q^4-1)=-3\) and \(((2q)^4-1)-16(q^4-1)=15\) were independently expanded and checked. Translating exponents modulo four is legal because \(q\) is a unit, and the five multiset orbit representatives are exhaustive. The reduction \(e\mid15\), the cases \(e=5,15\), and the exclusion of two-term sums were inspected explicitly.

The standalone `verify.py` uses only the Python standard library and exhausts every coprime residue \(q\pmod e\) of exact order four for \(2\le e\le3000\). It constructs the complete four-element multiplicative subgroup, enumerates all one-, two-, and three-term multisets with repetition, and checks the theorem's precise small-length prediction. The verification output is included in `verification_output.txt`. The finite sweep does not extend to all moduli and is not substituted for the proof.

No external or independent scientific audit is represented by these tests. The theorem does not claim to classify \(m(q,e)\) when it exceeds three, and the full bibliographic novelty question remains subject to future human review.
