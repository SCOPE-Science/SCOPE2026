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

The proof reduces the definition to exact neighborhood counts. For \(S\) encoded by selected index sets \(I,J\) and omitted index sets \(X,Y\):

- every \(a_i\) sees exactly \(|J|-\mathbf 1_{i\in J}\) selected neighbors;
- every \(b_i\) sees exactly \(|I|-\mathbf 1_{i\in I}\) selected neighbors;
- every omitted \(a_i\) sees exactly \(|Y|-\mathbf 1_{i\in Y}\) omitted neighbors;
- every omitted \(b_i\) sees exactly \(|X|-\mathbf 1_{i\in X}\) omitted neighbors.

These identities prove the side-size bounds and show that the only overlap restriction is \(X\cap Y=\varnothing\) when \(|X|=k\) or \(|Y|=k\). The coefficient formula then counts ordered omitted-index pairs by their two sizes.

The packaged checker independently enumerates all subsets for every \(3\le n\le8\) and every \(1\le k\le n-1\), compares the direct neighborhood definition with the structural criterion, reconstructs the entire coefficient dictionary from the formula, and checks the minimum value and number of minimum sets.

Replay result:

`VERIFY_OK n_range=3..8 subset_checks=582528 criterion_checks=582528 coefficient_checks=83 minimum_checks=54 max_order=16`

Limits: exhaustive enumeration is finite and does not prove the theorem for unbounded \(n\); the infinite claim is supported by the symbolic argument in `RESULT.md`. No independent audit has been performed.
