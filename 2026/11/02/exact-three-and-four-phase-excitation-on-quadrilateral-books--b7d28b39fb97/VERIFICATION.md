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

# Reproducibility and bounded verification

The package supplies an executable all-parameter finite-state certificate and a separately implemented direct-state test. From the directory containing `RESULT.md`, run `python3 code/verify_symbolic.py --csv evidence/support_classes.csv` and compare the generated 4599-row table with `evidence/support_classes.csv`. The checker enumerates every hub-state and nonempty support of initially present page-pair types, asserts the exact recurrence-entry and circulation-sign classification, and calculates the support-size histograms and power-sum coefficients. Its observed terminal output is in `evidence/symbolic_output.txt`.

For an independent implementation, compile `g++ -std=c++17 -O3 code/verify_direct.cpp -o verify_direct` and execute `./verify_direct`. It builds the labelled graph and checks actual vertex-state transitions without using the support reduction. Its output, `evidence/direct_output.txt`, certifies exact agreement of period-one, -three, and -four orbit counts, basin sizes, and sharp entrance times for each \(1\le k\le6\), totalling 5,380,830 configurations. This bounded enumeration is corroboration; the complete 4599-case support reduction supplies the all-size proof.

The page-support reduction is valid because equal initial page-pair states see the same two hubs forever and the hubs only test whether at least one page coordinate is excited. Multiplicities therefore do not affect any transition. The nine pair types and nine possible hub pairs yield exactly \(9(2^9-1)=4599\) complete reduced initial cases. The computed periodicity bound implies the global identity \(F_k^{17}=F_k^5\), with no extrapolation from the bounded direct-state tests.

Limitations: the support-state classification is computer-assisted and assumes the included finite integer program has been read and executed as specified. It does not establish independent external validation, coverage of all historical literature, or claims for other graphs or update rules.
