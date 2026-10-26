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

The theorem is supported by a complete bisimulation-and-orbit-counting proof in `RESULT.md`. The provided standalone script `s4_bouquet_check.py` uses only the Python standard library; it enumerates every valuation on fourteen explicitly listed small finite rooted bouquet frames, including cases with no propositional letters, and computes modal theories through depths zero to four, sets of terminal-cluster colour supports, and centered automorphism-orbit classes via histograms.

Run using `python3 s4_bouquet_check.py`. The script was executed, finishing with `BOUQUET_MODAL_CREDAL_FINITE_OK`. Representative exact checks were `(k,t,s)=(1,3,2)`: depth counts `[2,4,14,14,14]`, 14 distinct root support types and 20 invariant measure vertices; `(1,1,3)`: `[2,4,6,6,6]`, 6 observable types and 8 extreme priors; `(2,2,2)`: `[4,32,220,220,220]`, 220 observable types and 220 extreme priors.

These finite checks do not enumerate arbitrary sizes or prove the uniform theorem, nor do they establish historical priority. The unrestricted proof is the stated combinatorial and modal argument. No external validation or independent certification is claimed.
