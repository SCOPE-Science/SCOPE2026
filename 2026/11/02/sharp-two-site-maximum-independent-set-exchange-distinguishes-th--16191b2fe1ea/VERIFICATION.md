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
# Reproducible finite checks

Execute `python3 verify_bruteforce.py` and `python3 verify_algebra.py` from the same folder. No external Python package is required.

`verify_bruteforce.py` enumerates all \(inom{16}{5}=4368\) 5-subsets and \(inom{16}{4}=1820\) 4-subsets per graph, verifies exact independence, and constructs every size-two intersection adjacency and all distances. `verify_algebra.py` builds the four order-four subgroups and their cosets independently of 4-subset enumeration, checks all pair intersections and the doubled tetrahedral subdivision, then enumerates permutations to check the other Cayley graph. Both are exact finite procedures. These checks complement, but do not replace, the mathematical coset and permutation proofs.

Known limitations: the source-publication day for Peeters's 1993 memorandum is unavailable, as is the full text of the closest matched 2026 research-record entry. The remaining originality risk cannot be reduced to zero by these checks. Independent external validation is not performed.
