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

The analytic proof has two critical steps. First, if \(m\) is the smallest part size, then \(\Delta=N-m\), and the sum of the \(\Delta+1\) smallest degrees exceeds \(e(G)\); hence \(a(G)\le\Delta(G)\). Second, Gupta's equality criterion gives \(a=(\Delta-1)\alpha\), so \((\Delta-1)M\le\Delta\) for the largest part size \(M\). This forces a complete graph when \(\Delta\ge3\), and only the three order-three/four multipartite possibilities when \(\Delta=2\).

`verify.py` performs an independent finite stress test from the definitions. It generates integer partitions representing all complete multipartite isomorphism types through order \(20\), constructs the degree multiset, computes the annihilation number by its edge-sum definition, computes the residue by Havel--Hakimi reduction, and checks the lemma and equality classification.

Reproduction command:

`python3 verify.py`

Expected terminal line:

`ALL CHECKS PASSED; multipartite_types=2693; max_order=20; equality_types=4`

The computation is finite and does not replace the analytic proof for arbitrary order. No independent audit or external validation is claimed.
