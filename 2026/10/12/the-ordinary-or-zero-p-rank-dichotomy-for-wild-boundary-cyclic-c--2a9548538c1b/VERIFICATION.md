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
# Verification notes

The mathematical argument uses Theorem 4.8 of Kazemifard--Tafazolian for exhaustive boundary models and the Deuring--Shafarevich formula for each degree-\(p\) cover. For the three Kummer bases it computes explicit birational inverses and stable Cartier ranks. The genus-two Hasse--Witt matrix \(\left(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right)\) has square zero in characteristic three; its rank one must not be mistaken for \(p\)-rank one.

Run `python3 verify_prank.py` using Python 3 without third-party dependencies. The program exactly compares three expanded Kummer identities, calculates the two elliptic Hasse invariants and genus-two matrix, and checks Riemann--Hurwitz and Deuring--Shafarevich for the eight specified rows. Expected output: `VERIFY_OK: three Kummer transformations, three Hasse computations, eight genus/p-rank rows`.

The standalone program is an algebraic replay aid, not a proof of the published classification theorem or an independent validation of every external premise. No claim is made about characteristic two, the tame boundary, the Jacobians' full Newton polygons, or possible previously published equivalent rank tables.
