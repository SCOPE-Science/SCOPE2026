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

The initiating full text was checked at Definition 4.10, Proposition 4.14, Lemmas 6.1 and 6.2, and Theorem 6.7. On a Hodge-good family, Lemma 6.1 gives line bundles
\[
E_i=R^{2i}f_*\mathcal O
\]
with base change, and fibrewise cup powers identify \(E_i\) with \(E_1^{\otimes i}\).

For every \(i\), relative Frobenius induces
\[
h_i:F_S^*E_i\to E_i.
\]
The map on structure sheaves is multiplicative. Therefore, for each \(i\), the square formed by \(F_S^*c_i\), \(c_i\), \(h_1^{\otimes i}\), and \(h_i\) commutes. Since both cup maps are isomorphisms,
\[
h_i=c_i\circ h_1^{\otimes i}\circ(F_S^*c_i)^{-1}.
\]
Thus the associated line-bundle section is exactly the \(i\)-th tensor power of the degree-two section.

Locally write the degree-two section as \(a\). Then the degree-\(2i\) section is \(a^i\). If the base is integral and the Frobenius-split locus is nonempty, \(a\) is a nonzero non-zero-divisor, so the effective Cartier divisors satisfy
\[
D_i=iD_1.
\]
For \(i=n\), Lemma 6.2 identifies nonvanishing with Frobenius splitting, and Theorem 6.7 identifies the Hodge-good complement with infinite quasi-F-split height.

The closest prior Hasse-vanishing-order paper was inspected in full HTML through its Hasse-section definition, Ogus principle, and K3 application. It concerns CY-type \(F\)-zips and does not contain the higher coherent tensor-power comparison above.

No finite experiment is used. The proof is an exact functoriality argument in coherent cohomology. The Cartier-divisor statement is withheld when the base is nonintegral or the Frobenius section is identically zero.
