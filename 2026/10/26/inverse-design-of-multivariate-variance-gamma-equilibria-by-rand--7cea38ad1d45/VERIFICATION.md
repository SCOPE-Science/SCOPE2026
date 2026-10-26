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

# Reproducibility and proof boundary

Execute `python3 verify.py` using the Python 3 standard library. The verifier checks 5,769 rational moment/inequality identities for representative \(q\ge1\) and \(h\in(0,1]\), including the \(q=1\) atom case and nine \(0<q<1\) impossibility witnesses. It also performs 60 separate midpoint quadratures of the beta integral at several scales. The program prints `PASS 5829 exact/numerical identity checks` on success.

The analytically required equations are \(\mathbb E U^{2n}=1-hn/(q+n-1)\), uniqueness of moment measures on \([0,1]\), the beta integral, and the Poisson Brownian resolvent equation. The program tests finite instances only; in particular no finite enumeration establishes an infinite-moment theorem, uniqueness of an invariant law, or a universal novelty conclusion. Those conclusions are justified by the proof in `RESULT.md` and require mathematical evaluation.
