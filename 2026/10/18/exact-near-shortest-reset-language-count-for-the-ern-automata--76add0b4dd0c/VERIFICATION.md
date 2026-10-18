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
# Reproducibility and limits

The standalone standard-library program `artifacts/verify.py` independently constructs the forward image-subset transition graph of the specified automaton. Its integer-valued dynamic program counts *all distinct input words*, weighted by their actual letter choices, rather than treating a graph edge as a unique word when two letter actions coincide. It confirms that the shortest reset length is \((n-1)^2\), there is exactly one shortest reset word, and exactly \((n-2)^2+3\) words of length \((n-1)^2+1\), for all \(3\le n\le13\). It also checks explicit witnesses and inverse-phase no-op properties.

For \(n=3,4,5\) it independently enumerates **every** binary word at the target length and compares the exact reset-word set with the explicit family. The deterministic successful output ends with `CERNY_NEAR_RESET_PASS n=3..13 count_checks=11 exhaustive_n=3,4,5`.

Invoke `python3 artifacts/verify.py` with Python 3.10 or later; no extra libraries or external files are needed. Finite checks do not prove the unrestricted assertion; its proof is in `RESULT.md`. The classifications are confined to the stated automaton and excess length one. No independent third-party audit has been carried out.
