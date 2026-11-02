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

# Verification of the integral equivariant Kneser homology claim

**Exact proof checks.** Pairwise-intersecting edge families of a complete graph are either stars or triangles. The star union admits the stated explicit equivariant strong deformation retraction onto subdivided \(K_n\). Relative oriented 2-simplices are indexed by underlying triples; their connecting map is augmentation contraction into the integral cycle lattice. The triangles through a fixed root form a full integral basis of that lattice, so the exact sequence and kernel argument work integrally for all \(n\ge4\). Its kernel is \(\bigwedge^3 V_n\) as a natural submodule; the chosen root is used only for an auxiliary abelian-group splitting.

**Reproducibility.** Run `python3 verify.py` and `python3 verify_alt.py` from the directory containing these files; both depend only on the standard Python library. The first enumerates all simplicial faces and signed automorphism actions, verifying reduced Betti ranks modulo 101 and the complete signed Lefschetz character on every conjugacy class for \(4\le n\le7\). The second checks sign equivariance of every oriented triangle boundary under adjacent transpositions and the integral tetrahedral kernel relations for \(4\le n\le9\). The expected successful final lines are `DIRECT_CHAIN_CERTIFICATE_OK` and `INTEGRAL_EQUIVARIANT_CERTIFICATE_OK`; both were observed in execution.

**Limits.** Finite computations do not prove the infinite quantifiers, integrality beyond their range, or literature priority. Those mathematical claims are supported by the symbolic proof and the separately stated source comparison. No independent audit has been performed.
