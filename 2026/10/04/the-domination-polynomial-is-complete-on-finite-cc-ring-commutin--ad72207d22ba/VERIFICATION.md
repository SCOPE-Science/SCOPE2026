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

The verification has three independent finite components.

1. **Cluster-polynomial reconstruction.** For a clique profile
\[
(m_1,\ldots,m_t),
\]
the checker forms
\[
\prod_i((1+x)^{m_i}-1),
\]
substitutes \(x=y-1\), recursively constructs the cyclotomic polynomials, and uses exact integer polynomial division to recover all cyclotomic exponents. It then reconstructs every exact component multiplicity by descending divisibility inversion.

2. **Exhaustive profile collision search.** Every integer partition of every total graph order at most \(12\) is treated as a cluster profile. The checker verifies that no two distinct profiles produce the same domination polynomial and that each polynomial reconstructs its original profile exactly.

3. **Direct ring examples.** The checker constructs
\[
UT_2(\mathbb F_2)
\quad\text{and}\quad
UT_2(\mathbb F_3)
\]
from matrix multiplication, deletes the scalar center, and builds the commuting graph. It obtains
\[
3K_2
\quad\text{and}\quad
4K_6.
\]
For the six-vertex binary case it also exhaustively tests all vertex subsets and confirms the predicted domination polynomial.

Exact output:

```text
VERIFY_OK
cluster_profiles_exhaustive_total_order_le_12=271
UT2_F2_noncentral=6 center=2 components=3xK2 brute_polynomial=matched
UT2_F3_noncentral=24 center=3 components=4xK6
cyclotomic_profile_reconstruction=passed
```

These finite computations are corroborative. The theorem for arbitrary finite CC-rings is proved by the published clique decomposition, unique cyclotomic factorization, and Möbius inversion.
