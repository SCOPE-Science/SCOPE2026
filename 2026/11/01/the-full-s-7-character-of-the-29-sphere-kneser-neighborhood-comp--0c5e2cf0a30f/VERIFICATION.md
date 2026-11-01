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

# Reproducibility and limits
The exact standalone calculation is supplied as `verify.py`, with a recorded replay in `verify_output.txt`. Execute `python3 verify.py` using Python 3 standard library. The script verifies all 17,724 nonempty faces and independently obtains the face vector by an inclusion-exclusion count of graph edge-sets on at most five original symbols; every permutation belongs to one of the fifteen checked \(S_7\) cycle types. All signed fixed-simplex traces and the character formula are evaluated by exact integer arithmetic. The two proposed irreducible summands have characters of norm one and are orthogonal; the full-group invariant multiplicity is zero.

**External mathematical input:** Theorem 1.3 of Nilakantan–Singh, arXiv:1802.05848, identifies the nonequivariant homotopy type, ensuring that only reduced third rational homology survives. The standalone checker verifies neither that published theorem nor any integral representation-lattice conclusion. It uses no random samples or timeouts as negative evidence.
