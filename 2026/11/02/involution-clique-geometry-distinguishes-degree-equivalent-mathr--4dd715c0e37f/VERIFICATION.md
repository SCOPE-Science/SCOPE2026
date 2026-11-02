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

# Reproducibility and verification

The proof reduces the classification to two explicit computations valid for every \(q=2^f\): the trace-zero congruence-kernel description and the rank-one nilpotent centralizers in \(\mathfrak{sl}_2(\mathbb F_q)\). Its key identities and incidence assertions are written step by step in `RESULT.md`.

Run `python verify.py` from this directory. The Python script constructs the four finite rings directly, enumerates the complete \(\mathrm{SL}_2\) groups, and compares every matrix square and every pair of elements squaring to one. If `networkx` is installed, it additionally enumerates all maximal cliques in the induced commuting graph and checks their sizes and counts. On the checked installation the optional graph package was present and all four clique tests completed.

Observed results:

- \(q=2\), split ring: \(|G|=48\), \(|I|=20\), commuting ordered pairs \(208\), maximal cliques \(4\), three-stratum \(c_I\)-distribution \(\{8:12,12:6,20:2\}\).
- \(q=2\), Witt ring: \(|G|=48\), \(|I|=8\), commuting ordered pairs \(64\), maximal cliques \(1\), constant \(c_I=8\).
- \(q=4\), split ring: \(|G|=3840\), \(|I|=304\), commuting ordered pairs \(23296\), maximal cliques \(6\), spectrum \(\{64:240,112:60,304:4\}\).
- \(q=4\), Witt ring: \(|G|=3840\), \(|I|=64\), commuting ordered pairs \(4096\), maximal cliques \(1\), constant \(c_I=64\).

The \(q=4\) Witt ring is explicitly \((\mathbb Z/4\mathbb Z)[z]/(z^2+z+1)\), whose residue field is \(\mathbb F_4\). The \(q=2\) Witt ring is \(\mathbb Z/4\mathbb Z\). The code does not test all field orders, prove any general theorem by exhaustion, compute character tables, or perform independent mathematical audit.
