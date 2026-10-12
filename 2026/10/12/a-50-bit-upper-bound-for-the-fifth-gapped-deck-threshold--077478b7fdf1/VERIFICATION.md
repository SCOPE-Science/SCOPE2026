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

Run `python3 verify.py` in the directory containing `certificate.json`.

The verifier reconstructs the published length-\(24\) pair \(x,y\), checks that their gapped \(4\)-decks agree, and then forms
\[
u=\mathtt0xy\mathtt1,\qquad v=\mathtt0yx\mathtt1.
\]
It verifies that both words have length \(50\), are distinct, and have identical gapped subsequence multiplicities for every binary pattern of lengths \(1\) through \(5\).

Two independent exact procedures are used. The first is the prefix recurrence
\[
N_j(qb)=N_{j-1}(qb)+[w_j=b]N_{j-2}(q).
\]
The second directly enumerates all nonadjacent index tuples. For every \(\ell\in\{1,\ldots,5\}\), the total multiplicity is also checked against
\[
\binom{50-\ell+1}{\ell}.
\]

The verification proves only \(G(5)\le50\). It does not prove that no shorter collision exists. Independent audit has not been performed.
