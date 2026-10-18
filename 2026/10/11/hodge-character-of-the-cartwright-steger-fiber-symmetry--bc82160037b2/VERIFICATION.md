---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For a genus-19 invariant curve F with quotient genus6 under C3, invariant holomorphic differentials have d0=6 and d1+d2=13. Holomorphic Lefschetz for exactly three points with tangent multiplier omega^2 yields 1-conj(tr_H10)=3/(1-omega^2)=1-omega; hence tr_H10=omega^2. Since tr=6+d1*omega+d2*omega^2 and omega^2=-1-omega, this gives d1=6,d2=7. Complex-conjugate H01 contributes eigenvalue multiplicities (6,7,6), so H1 multiplicities (12,13,13), characteristic polynomial (t-1)^12(t²+t+1)^13. Its degree 38 and trace -1 agree with genus and ordinary Lefschetz; Riemann–Hurwitz: 36=3*10+3*2, checks quotient genus. Prym dimension=19-6=13, Hodge multiplicities 6/7. This is an exact symbolic argument conditional on quoted generator/local-multiplier convention, not an invented verification of the unavailable primary passage.

## originality

PASS

The Cartwright–Steger and Akhmedov–Yeung papers supply surface/fiber geometry, quotient genus and Lefschetz-trace inputs, but no located published result states the full H^{1,0} character or the associated Prym Hodge multiplicities. General holomorphic Lefschetz/Chevalley–Weil is precisely the standard tool applied here; it does not by itself publish the values for this special fiber without branch/genus inputs. Best-of-knowledge PASS with serious residual risk due inaccessible 2026 primary full text and the directness of the corollary.

## value

PASS

The exact Eisenstein Hodge signature of a natural 13-dimensional Prym in a well-studied ball-quotient fibration is an identifiable representation-theoretic invariant potentially needed for polarization, deformation and monodromy comparisons. It refines merely knowing genus19, quotient genus6 and total H1 trace. This is a narrow natural exact invariant, not a claim to solve integral lattice or handle-return monodromy problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
