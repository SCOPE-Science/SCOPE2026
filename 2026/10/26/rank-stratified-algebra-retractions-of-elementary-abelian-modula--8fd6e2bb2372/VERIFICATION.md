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

# Reproducible checks

Execute `python3 check_retractions.py` using the standard Python 3 library. The checker directly multiplies monomials in finite truncated polynomial rings, evaluates compositions of ring endomorphisms and identifies their induced cotangent ranks.

Observed output:

```
P2_M2_AND_M3_IDEMPOTENTS_EXHAUSTIVE_OK
p=2,q=2,m=2 ranks 0..2: 1 12 1
p=2,q=2,m=3 ranks 0..3: 1 448 3584 1
GF3_M2_RANKONE_IMAGES_EXHAUSTIVE_OK embeddings=5832 images=972 per-image-retractions=9
TRUNCATED_RETRACTION_CENSUS_OK
```

The binary tests inspect every candidate with idempotent cotangent matrix, a necessary condition for idempotence, and then test each remaining generator tuple explicitly. The ternary check exhausts rank-one embeddings and uses exact row-space equality to identify generated image subalgebras; nine retractions per image are obtained analytically, not by enumerating all algebra maps. A further 200 seeded ternary substitutions test multiplication identities. The unlimited field and generator parameters are established by the written algebraic proof, not by finite enumeration. No external validation was performed.
