---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS with a nonessential exposition correction needed: The eight directed trigram counts are nonnegative integer flows on the four-vertex de Bruijn graph, with exactly thirteen divergence sectors (zero plus 12 distinct e_s-e_t). The balanced-flow equation yields A+J+B+2C+3D=m with 0≤B≤C+D and rational generating function (1+z^3)/[(1-z)^2(1-z^2)(1-z^3)(1-z^4)]. Its order-five pole at 1 has coefficient 1/12 and gives H_m=m^4/288+O(m^3). Each open sector is squeezed between H_(m−2) and H_(m+2) by adding length-two paths; connectedness failures lie on coordinate boundary faces of dimension ≤3 and number O(m^3), giving 13 m^4/288+O(m^3). Independently enumerated binary words n=3..12 and recovered Q3(n)=8,15,28,52,92,151,240,363,532,757; symbolic series check produced leading 1/288. Source proof erroneously says all other poles are roots of unity of order ≤2: primitive third and fourth roots also occur, but those poles have lower order and contribute at most O(m^3). Thus the asymptotic conclusion survives; public proof prose must be corrected before import.

## originality

PASS

Best-of-knowledge PASS. Fixed read-length-three, binary, linear multispectrum count has four-dimensional sparse second-order de Bruijn flow polytope and exactly thirteen endpoint-divergence sectors. The earlier counted Markov types are predominantly first-order complete-transition cyclic balanced matrices; simply substitute alphabet size four gives a different (complete) 16-edge graph, not the 8-edge binary second-order graph. General second-order Markov methods are context but inspected references do not supply the 13/288 constant. Published length-two binary multispectrum work counts a different object.

## value

PASS

PASS. The exact leading coefficient 13/288 solves a natural finite-alphabet, fixed-read-length channel capacity question for lossless classification by complete contiguous trigram multiplicities. It quantifies the dimension-four sparsity restriction and linear endpoint freedoms and distinguishes cyclic and linear multispectra and read lengths two versus three. A finite exact formula or constructive efficient coding algorithm is not claimed or needed for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
