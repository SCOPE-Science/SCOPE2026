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

The theorem is supported by the full mathematical proof in `RESULT.md`. The critical checks are (i) the intrinsic edge-direction test for the full root-stabilizer orbit description; (ii) the walk-count induction for colour refinement; (iii) the exact rooted shortest-path multiplicities, including the even antipode; (iv) the distance-one two-walk and three-walk witnesses; and (v) the noninteraction of the root's colour beyond \(t\) hops in a regular graph. These steps prove the result for every integer \(n\ge5\), \(m\ge2\).

`verify_graph.py` executes direct vertex-level refinement on \(392\) parameter pairs \((n,m)\) with \(5\le n\le60\), \(2\le m\le8\), checking exact rounds and the stable orbit partition; see `verification_graph.txt`.

`verify_quotient.py` constructs the independent weighted orbit quotient and refines its \(2(D+1)\) quotient types on \(864\) pairs, \(5\le n\le100\), \(2\le m\le10\); see `verification_quotient.txt`. These finite experiments do not establish the general theorem on their own. There was no independent external audit or proof-assistant certification.
