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

The proof was checked as an implication chain rather than by computation.

For each metric piece \(M_j\), a bi-Lipschitz embedding into a finite-dimensional normed space identifies \(M_j\) bi-Lipschitzly with its image. Canonical linearization of the map and its inverse gives
\[
\mathcal F(M_j)\cong\mathcal F(N_j).
\]
Finite-dimensional norm equivalence then gives a bi-Lipschitz identification of \(N_j\) with a subset of some Euclidean space. Mason's 2026 Corollary 2 therefore gives the Dunford--Pettis property for every \(\mathcal F(M_j)\).

Mason's Lemma 12 verifies the two permanence facts required next: the Dunford--Pettis property passes to complemented subspaces and to countable \(\ell_1\)-sums. Thus
\[
\left(\bigoplus_j\mathcal F(M_j)\right)_{\ell_1}
\]
has the Dunford--Pettis property.

Mason's Lemma 13 uses the Godefroy--Kalton lifting theorem to show that if a separable Banach space \(X\) fails the Dunford--Pettis property, then \(\mathcal F(X)\) fails it as well. Therefore \(\mathcal F(X)\) cannot be isomorphic to a complemented subspace of the target sum, because such a complemented subspace would inherit the Dunford--Pettis property.

The boundary cases were checked explicitly: no uniform finite-dimensional distortion is required; the argument does not cover non-complemented embeddings; and it does not apply when \(X\) itself has the Dunford--Pettis property. The first public date and primary MSC were checked from arXiv:2609.28842v1.
