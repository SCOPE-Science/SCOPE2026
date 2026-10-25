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

# Reproducible finite verification

Run `python verify.py` with the two dependencies pinned by `requirements.txt`. The program builds all graph and unordered two-point cells from the lexicographic subset-incidence definition. It checks the exact signed cellular boundary operators, exhausts all simple hexagons, and constructs each disjoint-hexagon product class.

Its certificate uses a specified \(35\)-by-\(35\) integer torus coefficient minor of determinant \(-1\), a specified \(10\)-by-\(10\) minor of determinant \(+1\), and exact modular rank \(340\) of the degree-two boundary over \(\mathbb F_{101}\). These jointly prove that the thirty-five cycles form an integral basis of \(H_2\). Exact Smith normal form checks the degree-one order-two torsion.

Every stated character trace is obtained by transforming the chosen basis tori as signed cellular chains and projecting with the unimodular coefficient submatrix. The verifier checks the resulting action on all \(375\) cellular coordinates, then decomposes the character against the seven irreducible characters of \(S_5\).

The certificate is exhaustive for the specified twenty-vertex graph. No software result is interpreted as proof about arbitrary graphs, and this verification is not an independent scientific audit.
