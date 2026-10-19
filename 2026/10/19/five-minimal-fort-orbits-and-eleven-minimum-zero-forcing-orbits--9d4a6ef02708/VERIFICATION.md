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

# Verification and scope

The following checks were run on the complete programs in this package, for the labelled four-cube with integer vertices `0..15` and Hamming-distance-one adjacency. They are exhaustive finite computations, not a general theorem for other hypercubes, and do not constitute independent mathematical review.

```
python3 verify_forcing.py
python3 verify_forts.py
python3 verify_crosscheck.py
```

`verify_forcing.py` exhausts 65,536 initial black subsets by synchronous color changes, confirms polynomial coefficients `(8:2360, 9:6016, 10:6240, 11:4032, 12:1792, 13:560, 14:120, 15:16, 16:1)`, determines 2,360 inclusion-minimal sets all of size 8, and measures minimum-set round counts `(1:8, 2:816, 3:1152, 4:384)`.

`verify_forts.py` independently constructs the cube adjacency matrix, classifies all 65,536 subsets as 17,487 forts or not, and uses an exact all-proper-subset recurrence to identify 348 inclusion-minimal forts of sizes `(4:28, 6:32, 8:288)`. Its transversal test reproduces all nine forcing-polynomial coefficients. Both programs construct all 384 cube automorphisms and generate the five and eleven complete orbits listed in `CLASSIFICATION.json`.

`verify_crosscheck.py` tests every one of 65,536 initial black sets for equality between the direct forcing decision and the complementary-fort decision, and checks all minimal sets and orbit tables. The scripts include executable assertions; the absence of errors and their `OK` outputs are verifiable from the supplied programs, not external log files.

The previously published total of 348 minimal forts and the scalar `Z(Q4)=8` are acknowledged as known. An exact probability curve in a 2023 dissertation also implicitly contains the zero forcing polynomial; the retained novelty is the orbit classification, well-forcedness and propagation counts. Full independent validation and priority review remain unperformed.
