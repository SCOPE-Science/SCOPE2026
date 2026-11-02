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

# Finite exact certificates

`verify_direct.py` independently constructs the binary-vector Fano plane, checks all \(\binom{21}{3}=1330\) candidate flag triples and all \(\binom{21}{4}=5985\) possible four-flag sets. It constructs the exchange graph by deleting and adding exactly one flag, performs all \(84\) full breadth-first searches, and verifies every distance and excess-move pair.

`verify_cyclic.py` uses an independent cyclic \((7,3,1)\) difference-set construction, generates the exchange graph from all \(84\) compatible two-flag pairs, counts their three completions, independently enumerates the \(168\) collineations, and derives all distances from one representative of each collineation orbit. No external library or network access is required.

Both programs were executed from the packaged source files. Observed terminal markers:

```text
DIRECT_FANO_FLAG_EXCHANGE_PASS
CYCLIC_FLAG_PAIR_AND_AUTOMORPHISM_PASS
```

These exhaustive finite calculations establish the numerical statements for the unique Fano incidence graph; they are not a proof for larger projective planes. The statement of \(\nu_s(H)=3\) is independently justified by the four-point tangent-line obstruction. Historical priority and independent scholarly validation were not certified by these programs.
