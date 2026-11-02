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

For every integer \(n\ge5\), represent a binary configuration on \(KG(n,2)\) by a bit mask indexed lexicographically by the edges of \(K_n\). The two executable programs implement the open-neighborhood NOR update directly from pairwise disjointness of the underlying edges. Neither imports the theorem's proof or a precomputed transition table.

Run `python3 verify_exhaustive.py`. Its successful output `verify_exhaustive.out` records exhaustive \(n=5,6\) verification, including the identity \(F^3=F\), all orbit counts, every basin-size multiplicity, and the exact distinguished basin. Run `g++ -std=c++17 -O3 verify_cpp.cpp -o verifier && ./verifier`. Its actual successful output `verify_cpp.out` records \(n=5,6,7\), including \(2{,}097{,}152\) initial configurations in the largest case. All arithmetic in the verifiers uses integer masks and exact comparisons.

The tests establish these finite checks only. The general theorem rests on the mathematical proof by an exhaustive **symbolic** cover test and exact inverse-fiber counting in RESULT.md, not on program extrapolation. Published antecedents on self-inclusive minterm networks have a different local update rule. A plausible original 2012 article was not available in full; bibliographic novelty remains conditional. No independent audit has been performed.
