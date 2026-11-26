---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The interval theorem stands as written; the corrected full RESULT.md in /workspace/repairs/5 fixes statements about distinct eigenvalues and entries, and distinguishes a negative entry from an entrywise negative matrix at the sign witnesses. At n=2 the sectors with eigenvalues 2 and n coincide and t10=t01. The 36-vertex 'negative' examples have positive diagonals, so the corrected text names the actual negative entries. Independent replay /workspace/branches/replay_5.py derived the quartics from the coincidence projectors, checked exact matrix examples with T1=1, reconstructed Sturm sequences by rational polynomial division for all eleven orders 7–17, and evaluated the symbolic witness and recovery remainders. The diagonal is positive from the positive scalar map; the opposite-coordinate class is positive for h>0 since g(t)/t strictly decreases, giving g(a+b)<g(a)+g(b). Thus both edge numerators must be nonnegative and suffice. B has all positive coefficients at n=2,3, and at n≥4 a unique simple positive root by the negative leading coefficient and Descartes' rule. A has positive coefficients at n≤6 and equal Sturm variation one at zero and positive infinity for each n=7,…,17. For every n≥18 the shifted polynomial certificate makes A(8/n)<0; positive endpoints and two sign changes give exactly two simple roots. Both A and B are positive at sqrt(12/n)>8/n, so this witness lies strictly between β_n and γ_n, establishing separated intervals of positive length and including all equality cases. At n=18 the exact sign pairs (A,B) at 1/3,2/5,4/5,6/5 are (+,+),(−,+),(+,+),(+,−), respectively. The n=18 approximate roots also reproduce; these are not used to prove signs or ordering. No internal-stage, general graph, or repeated-step classification is entailed.

## originality

PASS

The supported distinct claim is the graph-specific finite-timestep partition, including recovery cutoff and onset at eighteen. The same map on a broader product family has an indexed all-timestep classification, which covers the unconditional case and eventual failure here by specialization. Neither that result nor the other inspected analyses give this complete finite-step classification. No independent originality is attributed to the four-cycle case or to those overlapping qualitative subclaims.

## value

PASS

The natural mass-conserving diffusion model separates scalar spectral positivity from entrywise monotonicity. It exhibits two different edge mechanisms, with one losing and regaining its sign before the other fails permanently. The exact n=18 cutoff and finite recovered interval answer a question left open by all-step classifications or sufficient timestep bounds and can guide the choice of endpoint step on this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
