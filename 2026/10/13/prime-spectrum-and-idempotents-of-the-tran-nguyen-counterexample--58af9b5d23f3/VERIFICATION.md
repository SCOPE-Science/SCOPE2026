---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For R=iota(k[x,y,z])+D with D=k^(Omega), Omega=X×N, X Zariski dense, repeated infinite fibers, iota(A)∩D=0 because nonzero polynomial values repeat infinitely often; hence R/D≅A. Any prime containing D pulls back uniquely from Spec A. A prime P not containing D omits some coordinate idempotent delta_omega; orthogonality ensures exactly one such omega; delta_omega(1−delta_omega)=0 forces 1−delta_omega∈P and then P=M_omega. M_omega are isolated clopen maximal and minimal; D also minimal and dimR=dimA=3. For e=iota(f)+d idempotent, coordinate fibers plus Zariski density force f(f−1)=0 in the domain A, hence f=0 or 1, and e=chi_F or 1−chi_F with F finite. Confirmed actual proof and full exact source assumptions; this is symbolic, not a purported finite verification.

## originality

PASS

Best-of-knowledge PASS: Tran–Nguyen introduce this specific construction to demonstrate annihilator and A2/A3 conditions, but do not derive its entire Spec, minimal-prime list, dimension, and finite/cofinite idempotents. Hong–Kim–Lee–Nielsen 2009 studies general minimal-prime topology before the example and does not name or compute this ring. The generic orthogonal-idempotent argument is elementary and receives credit only as a method, not new general theory.

## value

PASS

Computing Spec and all idempotents for this notable counterexample gives a coherent structural picture of its irreducible components, isolated points and connectedness, directly relevant to why the ring has interesting annihilator behavior. Specific complete classification of a published non-Noetherian example is useful beyond a small type check; no broad classification of all such rings claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
