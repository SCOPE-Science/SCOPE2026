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

# Exact verification

Run `python3 verification.py`. The script has no dependencies outside the Python 3 standard library. Every small-network comparison uses exact rational Gaussian elimination, not floating-point tolerances. It covers the complete connected labeled three-uniform hypergraph space at orders three, four, and five and every absent group, with opinion patterns reduced solely by global opinion complementation.

Expected results include 1 connected three-vertex hypergraph with zero additions, 11 connected four-vertex hypergraphs with 128 exact comparisons, and 958 connected five-vertex hypergraphs with 73,760 exact comparisons. None produces an increase. The total for orders four and five is 73,888 exact comparisons.

For the six-person witness, unit-weight exact polarization values are `2585/16854` before and `1193/7776` afterward for opinions in `{0,1}`. Their difference is `977/21842784`. An additional algebraic certificate checks an explicit rational equilibrium vector and the identity that the increase for added weight \(t>0\) is \(2t(553t+424)/[8427(19t+53)^2]\). These coefficient identities hold for all real \(t\), and their numerator and denominator signs give the stated positivity.

The binary normalization is exact: mapping \(\{-1,+1\}\) to \(\{0,1\}\) by an affine transformation divides centered squared polarization by four, leaving every sign comparison unchanged.

No claim of publication priority, external formal verification, or independent validation is made by the program or its output. The universal statement is restricted to unit pre-existing and newly added group weights and the enumerated network orders; the all-positive-added-weight formula is for the displayed six-agent witness alone.
