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

# Verification of the finite symmetry classification

Both Python programs are standalone and use only the standard library. From their directory, run:

```sh
python3 check_orbits.py
python3 check_antichains.py
```

`check_orbits.py` independently enumerates all 65,536 Boolean masks of candidate families over the 16 teams, checks convexity using the full inclusion-interval predicate, applies the signed-coordinate group of eight and the full symmetric group of 24 to the resulting families, and checks their fixed and orbit counts. Its expected last line is:

```text
ORBIT_CERT_OK convex=3938 D8_orbits=700 orbit_sizes={1:26,2:54,4:289,8:331} fixed_types={1^4:3938,1^2_2:526,2^2:186,4:26} S4_orbits=349
```

`check_antichains.py` enumerates the 168 antichains of the team-inclusion lattice, exhaustively pairs compatible minimum and maximum antichains, includes the empty meaning, and independently computes the signed action on those pairs. Its expected last line is:

```text
ANTICHAIN_CERT_OK antichains=168 valid_pairs=3938 fixed_sorted=[26,26,186,186,186,526,526,3938] orbits=700 sizes={1:26,2:54,4:289,8:331}
```

The finite quotient-poset lemma and minimum/maximum-antichain characterization supply the mathematical reduction. Both programs are exhaustive **for exactly two propositional atoms**; they do not establish counts for three or more atoms. Sources that motivate the class do not by themselves prove historical novelty. No independent audit has been performed.
