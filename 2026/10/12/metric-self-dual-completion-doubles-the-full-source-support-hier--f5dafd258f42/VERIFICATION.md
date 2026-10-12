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
`artifacts/verify.py` tests the new support-theoretic deduction independently of the source construction internals.

For every binary linear source code of every length
\[
1\le m\le4,
\]
it builds a surrogate extension satisfying exactly the two source-theorem premises used in the proof:

- a linear embedding that doubles every Hamming weight;
- all non-embedded nonzero words have weight strictly above the cutoff
\[
H=2m.
\]

Every source code and every relevant subcode dimension is exhausted exactly. The verifier computes the complete support-size histogram of source subcodes and the complete histogram of extension subcodes whose support is at most \(H\), then checks that the latter is obtained by doubling every source support size with identical multiplicity.

It also computes all generalized Hamming weights directly and verifies
\[
d_r(\text{extension})=2d_r(C)
\]
for every tested source code and every
\[
1\le r\le\dim C.
\]

Finally, for every enumerated binary subspace it verifies the counting identity
\[
\sum_{u\in U}\operatorname{wt}(u)=2^{r-1}|\operatorname{Supp}(U)|.
\]

This finite replay checks the algebraic implication used in the result; the existence of the self-dual completion itself is the published premise from arXiv:2609.22669v1. Successful replay prints `VERIFY_OK`.
