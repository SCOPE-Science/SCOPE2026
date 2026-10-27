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
# Verification record

The standalone `verify_periodic_ssa2.py` is ordinary Python 3 standard-library code. From the embedded file, run `python3 verify_periodic_ssa2.py`. The expected success line is:

`PERIODIC_DNA_SSA2_PASS choices=729 nonzero_det_groups=18 polynomial_identity=exact trace_n=1..45 direct_n=1..10 necklaces_n=1..24`

The code builds the six explicit non-self-reverse-complement dinucleotide pairs, enumerates all \(729\) three-choice exclusion patterns, computes each \(\det(I-zA)\) by a four-column permutation expansion, verifies all 18 nonzero-weight characteristic-polynomial classes, and checks a full integer polynomial identity for the claimed zeta factorization. It then derives \(c_n\) using Newton coefficient identities for every \(1\le n\le45\) and directly enumerates all words of lengths \(1\) through \(10\). It tests integral Burnside necklace counts through length \(24\).

The proof for all lengths is the structural finite-exclusion expansion and exact rational determinant calculation, not finite experimental extrapolation. Source interpretation follows the explicitly defined infinite periodic-extension convention, which is stronger than requiring two disjoint stems only in one finite traversal. The complete 2024 journal extension was not available for inspection. This package has not received independent mathematical auditing.
