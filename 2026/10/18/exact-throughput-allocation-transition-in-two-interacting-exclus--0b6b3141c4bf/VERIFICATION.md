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

The stationary law gives physical signed total current B J_c; B>0 has no effect on maximizers. Expanding in s=u+v and p=uv gives J_c=s-s^2+p[2-c(2-s)]. The product interval [max(0,s-1),s^2/4] reduces maximization to boundary or diagonal except for a flat fiber. The empty-lane edges attain 1/4 uniquely at half filling; full-lane edges are strictly below the global envelope. On a flat fiber with 1<c<2, s(1-s) can attain 1/4 only at c=4/3, where the exact diagonal witness is 260/1029>1/4; for c>=2 the fiber is nonpositive, and c<=1 gives no interior flat fiber. The first root of 1-2(1+c)q+3cq^2=0 is the unique diagonal maximum, has strictly positive value, and the value decreases from 1/2 to 0 since its c-derivative is -2q^2(1-q). Equating the value to 1/4 yields the strictly increasing cubic in the finding. The inward derivative at the half-filled edge changes sign at 4/3; there the feasible perturbation u=1/2-2v/3 gives the positive leading term v^2/9. The diagonal has negative parallel Hessian eigenvalue and its transverse eigenvalue vanishes at c_s=(5-sqrt(5))/2. Along u=q+h+d, v=q+h-d at c_s, h=-c_s d^2/A gives (c_s^2/A)d^4+O(d^6)>0 with A=2(1+c_s-3c_s q), so equality is not a local maximum. The two exact witnesses, 260/1029 at 4/3 and M(c_s)=(sqrt(5)-1)/5, bracket the unique global crossing. Replay: RESULT.md lines 50–87 and the identities above; python3 /workspace/review_evidence/bounded_checks.py confirms c*=1.35700320530497618. The frozen verifier was inspected, not rerun; its random grid cannot prove uniqueness or exhaust the square. The result is optimization across product measures at independently variable densities, not dynamical selection at conserved lane numbers.

## originality

PASS

The flux law is prior and explicitly credited. An indexed record with a later date states the same complete global optimizer classification under a sign change. That is exact coverage of the global part, not evidence of antecedence relative to the frozen record's date; absolute priority and provenance are not established. The two strict local thresholds and their equality behavior were not in the matched statement. Earlier inspected sources either provide the current only or study different constrained objectives. The decision credits only the independent-density allocation/stability classification against the dated evidence, not the stationary current itself.

## value

PASS

The full-square signed-flux optimization is a natural stationary comparison and has an exact first-order change in the maximizing allocation. Exhausting flat fibers rules out extra optima at coexistence. The two distinct spinodals, including their non-maximal equality cases, give a nonzero interval of coexisting local optima and distinguish the global transition from a Hessian instability. No dynamical hysteresis or open-system selection is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
