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

The mathematical proof uses a digit-carry characterization of even–even and odd–odd sums, inclusion–exclusion on their overlap, and an exact classification of pure-digit integers. The base condition is essential: at \(g\ge4\), an isolated power beyond the units position has at least two opposite-parity carry decompositions.

Run `python3 check.py` from the extracted package directory. This enumerates unordered positive summand pairs independently of the proof formulas. The run completed with `CERTIFICATE_OK configurations=21 direct_summand_pairs=3550513`, checking all bases \(4\le g\le10\) at cutoffs \(g^{2k}\) for \(1\le k\le3\). The complete console result is in `check.log`.

Finite enumeration does not prove the assertion for all bases and depths; that rests on the constructive carry-count argument. Independent audit has not been performed.
