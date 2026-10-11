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

From the package directory, run `python3 verify_paley29.py`. The replay regenerates the Paley-29 graph, all independent faces, every Hasse cover, the complete staged matching, and the signed Morse boundary. It terminates with `VERIFY_OK`.

The checked finite data are: face vector \((29,203,406,203)\), 841 nonempty faces, 2436 Hasse covers, 397 matched pairs, and critical-cell counts one in dimension 0, 37 in dimension 2, and 9 in dimension 3. The Morse boundary has shape \(37\times9\), a certified unit \(8\times8\) minor, a certified full-rank minor of determinant \(-2\), and mod-2 rank 8. Those checks force Smith invariant factors \(1^8,2\).

A separately built mod-2 simplicial chain complex has boundary ranks \((28,175,202)\), giving reduced mod-2 Betti ranks 29 in degree 2 and 1 in degree 3. This is consistent with \(\mathbb Z^{28}\oplus\mathbb Z/2\) in integral degree 2 and the claimed Moore summand.

The verifier proves the finite combinatorial and algebraic assertions. The conversion of the Morse CW boundary to the final wedge-plus-Moore homotopy type uses standard discrete Morse theory, Hurewicz for a wedge of 2-spheres, and standard integral cell slides/cancellations; those general theorems are not re-proved by the script.
