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

Run `python3 check_cep_one_point.py` from the directory containing this file and the accompanying checker. The checker reconstructs Boolean subalgebras from all partitions of the atom set, evaluates operation compatibility of every candidate global/local ideal directly on all element pairs, and tests literal restriction of global congruences to subalgebras.

The exhaustive run for every admissible \((S,T)\) at \(n=2,3,4,5\) produces:

```text
n=2: CEP=5, nonCEP=0, total=5
n=3: CEP=10, nonCEP=9, total=19
n=4: CEP=19, nonCEP=46, total=65
n=5: CEP=36, nonCEP=175, total=211
ONE_POINT_BOOLEAN_CEP_CENSUS_OK
```

These are finite checks; they do not establish claims for unbounded \(n\). The arbitrary-size claim is established by the kernel-ideal and partition proof in `RESULT.md`, including explicit witnesses for every failing parameter family. The checker requires only Python 3 with its standard library. No machine proof assistant or external validation was used. Independent audit has not been performed.
