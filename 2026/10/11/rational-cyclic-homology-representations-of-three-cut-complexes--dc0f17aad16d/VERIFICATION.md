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

# Computational verification and proof limits

The standalone `verify.py` uses only Python 3 and the standard library. Running `python3 verify.py` in the containing directory produced exactly:

```text
VERIFY_OK dual_faces=6426 dual_rotations=186 mod2_betti=12 direct_cut_actions=42
```

It enumerates all Alexander-dual faces for \(p=2,3,4\) and four consecutive allowed vertex counts beginning at \(n=6p-3\); calculates signs of invariant oriented faces for all nonidentity rotations; computes \(H^1\) ranks by independent exact mod-two boundary elimination; and checks top-homology Lefschetz numbers directly from **ordinary** three-cut simplices for \((n,p)=(9,2),(10,2),(11,2),(12,2)\). It also checks rational character arithmetic for \(2\le p\le6\) and eighteen consecutive valid vertex counts for each value of \(p\).

Finite checks support the claimed formula only for the tested cases and are not a proof for arbitrary parameters. The universal proof in `RESULT.md` uses an explicit all-order orbit argument, the equivariant Alexander-dual sign, and the published non-equivariant shellability result [arXiv:2603.23155v1, Theorem 1.4]. It does not provide an integral-lattice decomposition, a dihedral reflection character, or an independent replication of the source's lengthy shelling proof.
