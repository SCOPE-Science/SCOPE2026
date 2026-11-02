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

# Reproducibility and verification

The mathematical proof in `RESULT.md` derives the complete Jordan forms for every permitted order, matching size, and characteristic-two finite field. It uses an incidence-matrix reduction to an explicitly described finite-dimensional operator. Its central unbounded steps are the even-coordinate rank calculations and the implication of the polynomial identities for the periodic and nilpotent components.

`rank_verifier.py` constructs each line-graph adjacency matrix independently and checks the formulas for ranks of its first three powers at every \(3\le n\le16\), for each \(0\le k\le\lfloor n/2\rfloor\). It also checks the characteristic-two polynomial identity and the additional rank controlling the two-cycles in the odd case. This covers 77 matrix instances. Run with `python3 rank_verifier.py`; expected output is in `rank_output.txt`.

`independent_enumeration.cpp` constructs the actual neighbor masks for every root-edge variable, then evolves **every** binary initial state for all \(3\le n\le7\) and allowed matching sizes. The independent census checks each exact first-entry and eventual-period total against the formulas. This covers 16 root-graph instances and 3,995,516 initial states. Compile with `g++ -std=c++17 -O3 independent_enumeration.cpp -o enumerate` and run `./enumerate`; expected output is in `brute_output.txt`.

These finite computations cannot establish the theorem for arbitrarily large graphs or nonbinary characteristic-two fields. The general proof is the algebraic incidence calculation. No outside formal proof certificate is claimed, and no independent audit has been performed.
