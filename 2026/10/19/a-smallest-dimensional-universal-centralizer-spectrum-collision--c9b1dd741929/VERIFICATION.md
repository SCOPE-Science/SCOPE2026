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

For a support S of nonzero coordinate vectors in k^t, edges to its complement kill exactly the coefficients in N[S]∖S. In a component of the induced graph on S, a solution nonzero at one vertex must propagate nonzero values along every edge and force all support vectors to have one projective direction. When they do, the solution is one-dimensional, since dividing by the nonzero scalar coordinates makes the edge equations equality constraints. The rank is therefore |N[S]| minus the number of such components. Choosing a projective direction and a nonzero scalar at each vertex gives exactly P_t(q−1)^c choices on a size-c component, and the free edge coordinates give q^(mt). This proof includes characteristic two. An independent bounded enumeration at /workspace/audit-evidence/3_graphical_centralizers.py (run with python3) reconstructed both profiles via set unions and matched all 27 bins of profile.tsv and all 64 supports per graph. Different triangle-incidence multisets certify graph nonisomorphism, which Mainkar's Theorem 1.1 transfers in odd characteristic. At dimension <13, connectedness gives n≤6 and for n=6 only 5 or 6 edges. Exhaustive orbit marking under relabelings and independent signature construction reproduced 1,1,2,6,21 connected classes through n=5 and 6,13 respectively at (n,m)=(6,5),(6,6), with no equal one-tuple coefficient signatures within a fixed (n,m). Total elements and the rank-zero term recover n+m and m for connected graphs with n≥2: a purported central vertex coefficient is zero by an incident edge bracket in its independent edge slot. The one-vertex algebra is unique by dimension. Since an unequal polynomial in q−1 cannot agree at all prime powers, these checks prove the finite cutoff, not just samples at two primes. The frozen scripts were inspected, not executed.

## originality

PASS

The supported contribution is the explicit universal collision with the sharp connected-family minimum. Both the general simultaneous enumerator and the one-element polynomial are prior results and are credited as such by the record. No checked source supplied the equal profiles of these two witnesses or the sharp dimension cutoff.

## value

PASS

The counterexample resolves a natural inverse question with a witness that survives every tuple length and field size, rather than a coincidence at one prime or for one element. The connected-graph dimension cutoff is sharp, and the distinction between the lower-dimensional one-tuple rigidity and the all-tuple collision is structurally useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
