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
# Verification

The general proof has three critical steps.

First, a topology on a finite set has only finitely many distinct opens, so arbitrary intersections reduce to finite intersections. It is therefore Alexandrov and equals the up-set topology of its specialization preorder.

Second, in a finite preorder every point reaches a maximal equivalence class. The union \(M\) of all maximal classes is an up-set and is dense. Any dense up-set must meet each maximal class and therefore contain that class entirely. Hence \(M\) is the unique least dense open.

Third, on the fixed chain \(C_n\), all intuitionistic up-sets are nested tails. Any selection of the \(n-1\) intermediate tails, together with the whole set and empty set, is a topology. This gives \(2^{n-1}\) topologies. Fixing the least nonempty tail gives the stated multiplicities.

The bundled `verify.py` enumerates all labelled preorders on at most four points and checks the least-dense-core theorem. It also enumerates all chain up-space topologies for \(1\le n\le10\), checks the total count, reconstructs specialization, and verifies every terminal-block multiplicity. It prints `VERIFY_OK`.

## Limits

The finite computations are consistency checks only. The theorem for arbitrary finite carriers follows from the proof. No infinite Alexandrov-collapse claim is made.
