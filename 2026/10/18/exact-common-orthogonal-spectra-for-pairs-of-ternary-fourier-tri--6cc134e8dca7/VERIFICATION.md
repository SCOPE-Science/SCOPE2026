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

# Verification and reproducibility

The provided `check.py` requires only Python 3 and its standard library. Run `python check.py` from its directory and compare the printed output with `verification-output.txt`.

The script implements the closed rank-based count using exact row reduction modulo three. Separately, it considers each unordered three-frequency set and applies the three-residue Fourier orthogonality criterion directly to every pair of frequency columns. These are two distinct exact computations of the same finite count.

The exhaustive dimension-two check covers every one of the 84 spatial triples against every second spatial triple (7056 ordered pairs), testing all 84 frequency triples. Their common-spectrum multiplicities are 0 (4320 pairs), 3 (2592), 6 (108), and 27 (36). An exhaustive dimension-one boundary test checks its unique triple pair. Further independent randomized pair samples are tested against all 2925 dimension-three and all 85320 dimension-four frequency triples, with deterministic fixed random seed 314159. The explicit incompatible affine triangle and affine line are checked.

The numerical computations neither establish the all-dimension formula nor infer it from data: the independent general proof relies on character-sum rigidity and exact finite-field fiber counting; an elementary orbit count proves the entire dimension-two histogram. No assertion is made about computations in untested finite dimensions or about an independent external audit.
