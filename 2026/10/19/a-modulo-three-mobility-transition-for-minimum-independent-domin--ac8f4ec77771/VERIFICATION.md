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
# Reproducibility
Run `g++ -O2 -std=c++17 verify_bruteforce.cpp -o verify_bruteforce` followed by `./verify_bruteforce > brute_certificate.tsv`. Run `python3 verify_structural.py > constructive_full.txt`; its lines preceding `EXTENDED_CHECKS` form `constructive_certificate.tsv` (equivalently filter the final line). Compare the two TSV certificates byte-for-byte. The C++ implementation exhaustively tests all \(2^{2n}\) subsets for \(5\le n\le12\). The Python implementation constructs the mathematical path-family solutions for \(5\le n\le21\) and tests exchange adjacency, components, and predicted counts. The finite checks do not establish the theorem for unbounded \(n\); the proof in RESULT.md supplies the universal argument.

No independent external scientific audit was performed. All included data and scripts are locally replayable. The cited 2018 maximal-independent-set paper was not inspected in full text, leaving an acknowledged originality comparison risk.
