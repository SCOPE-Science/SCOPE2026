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

Run `python3 verify.py` with Python 3.9 or later. The checker uses only the standard library (`itertools`, `collections`, `math`, and `fractions`). It reconstructs all elements from injective words and their doubled-first-letter variants. A normalization of concatenated tuples implements multiplication independently of the graph formulas. All unordered pairs are checked for commutation, then exact components, maximal-clique sizes, ordered pair counts and predicted spectrum dimensions are compared with graph computations.

For the Laplacian, the checker builds integral matrices and performs Gaussian elimination over rational numbers to find nullities of \(L-\lambda I\). Since the matrices are symmetric, the sum of exact eigenspace multiplicities tests the complete eigenvalue multiset.

Recorded successful ranks are 2, 3 and 4. At rank 4, 128 elements, 16 components, 664 ordered commuting pairs and 48 maximal cliques were checked. The complete rank-4 spectrum is zero (multiplicity 16), one (12), two (8), three (36), five (36), seven (12), and seventeen (8). Higher ranks are not exhaustively checked; no computational evidence is presented as an infinite proof.
