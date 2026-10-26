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

The two attached Python 3 programs are independent in their primary verification strategies. `verify_direct.py` constructs the open-neighborhood bitmasks of \(T(n)\) and tests every vertex subset, using an exclusive open-neighborhood witness for each selected vertex to establish inclusion-minimality. `verify_species.py` constructs the labeled exponential generating function of short-legged spiders and computes its coefficients by an exact rational recurrence; no graph-neighborhood enumeration is used. Execute both scripts in the extracted package and compare stdout to the matching `.out` files.

Both programs agree, for \(n=3,4,5,6,7\), on the complete cardinality profiles \((\{2:3\},\{2:12\},\{3:80\},\{4:840\},\{4:630,5:3402\})\). The species script also lists the coefficients through \(n=12\). These checks have been run from the current package, but finite verification is not a proof for all orders. The universal statement rests on the six-step combinatorial proof in `RESULT.md`. No independent external validation is claimed.
