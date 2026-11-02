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

# Reproducible scientific checks

The standalone file `verify.py` uses Python 3 standard-library integer arithmetic. Execute `python3 verify.py` in the directory containing that file. Its exact polynomial operations independently reconstruct the four-gap weighted generating numerator and denominator, check the reduced numerator \(P(q)\) and denominator \(H(q)\), confirm polynomial remainders \(864,32,6,-12\), and compare \(41\) initial coefficients to direct four-part partition enumeration.

It also checks least periods and periodicity samples at primes \(5,7,11,13,17,37,101\). The output of the executed checker was:

`VERIFY_OK numerator_degree=24 reduced_denominator_degree=22 cyclotomic_residues=864,32,-12,6 direct_partition_terms=41 prime_periods=5:300,7:84,11:132,13:156,17:204,37:444,101:1212`

The infinite scientific claim does not depend on numerical extrapolation: the complete proof establishes the exact rational identity and then characterizes all possible periods over each prime field by factor divisibility and root multiplicities.

The originating literature conjectured some particular periods. Absolute bibliographic priority and independent scientific review are not certified.
