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

The claim has two parts and both were checked directly.

For existence of the SCD origin, select countably many distinct coordinates from the infinite index set. For every integer \(K\ge2\), points chosen from the corresponding coordinate slices split into a distinguished-coordinate part and a remainder. The remainder has norm at most \((p/K)^{1/p}\) after averaging, while disjointness of the distinguished coordinates gives the second bound \(K^{1/p-1}\). Their sum tends to zero for \(1<p<\infty\). The selected points outside those countably many coordinates are included in the remainders, so no hidden countability or separability assumption on the ambient direct sum is used.

For uniqueness under the Daugavet hypothesis, the full arXiv text of Proposition 3.11 in arXiv:2311.03064v2 was inspected. It applies to \(E\oplus_pY\) with \(E\) Daugavet and \(Y\) arbitrary, and forces the \(E\)-coordinate of every SCD point to be zero. Regrouping the arbitrary-index sum around each single coordinate therefore forces all coordinates to vanish.

The source's Proposition 3.7 and Theorem 3.6 were also inspected. They are formally stated for sequences indexed by \(\mathbb N\), so the proof above supplies the missing arbitrary-index existence step rather than merely renaming the source theorem.

No numerical experiment, finite enumeration, or external certificate is needed. The proof does not address \(p=1\) or \(p=\infty\), and it makes no claim about arbitrary-index sums whose coordinate spaces fail the Daugavet hypothesis beyond the existence of the SCD origin.
