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

The proof was replayed from the following exact ingredients.

1. The source's Theorem 2.4 states that, under its simple-kernel and nondegeneracy hypotheses, the bifurcation is pitchfork when \(D_{uu}F(\lambda_\circ,u_\circ)[\varphi_\circ,\varphi_\circ]\in R(L)\), and transcritical when that term is outside \(R(L)\).
2. The source's Lemma 5.1 places the symmetric target sector inside \(R(L)\).
3. In one dimension, a symmetric equilibrium has Fourier support at multiples of \(n\). The cosine product identity therefore makes every residue-pair sector invariant under the linearization.
4. Since \(\dim\ker L=1\), the critical kernel vector has support in exactly one nonzero residue-pair sector.
5. Squaring that sector produces only residues \(0\) and \(\pm2r\). A distinct doubled sector is in the range when its restricted linearization is Fredholm of index zero, because its restricted kernel is trivial and index zero then implies surjectivity.
6. For a nonzero residue pair, \(E_{2r}^{(n)}=E_r^{(n)}\) is equivalent to \(2r\equiv-r\pmod n\), hence to \(3r\equiv0\pmod n\). The alternative congruence \(2r\equiv r\pmod n\) would force the symmetric residue.
7. Therefore every nonexceptional residue pair has its quadratic term in \(R(L)\), so the source theorem makes the bifurcation pitchfork.

A finite sanity check enumerated the canonical residue pairs for every \(2\le n\le30\) and confirmed that the doubled pair equals the original pair exactly in the \(3r\equiv0\pmod n\) cases. This enumeration is not part of the proof and is not used to extrapolate to arbitrary \(n\).

Limits checked: simple one-dimensional kernel; one-dimensional cosine-Fourier Ohta--Kawasaki or SKT setting; source nondegeneracy hypotheses; and the stated Fredholm-index-zero condition when the doubled sector is a new nonsymmetric sector. No assertion is made that an exceptional sector must be transcritical, and no two-dimensional classification is claimed.
