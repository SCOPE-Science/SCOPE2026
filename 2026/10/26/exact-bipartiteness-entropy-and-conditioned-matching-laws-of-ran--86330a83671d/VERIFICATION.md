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
# Reproduction and scope

Run `python verify.py` with Python 3.10+ and no external libraries. The program exhausts the 24 top matchings of two fixed four-cycles and identifies exactly eight bipartite outputs. It separately exhausts 40,320 permutations for each of two pairs of eight-vertex bipartite child graphs and finds 1,152 accepted matchings in each case. It verifies a nonbipartite-child obstruction, exact rational recurrences/products through dimension six, and finite numerical checks of the logarithmic expansion through dimension fourteen.

The exact theoretical conclusions come from connected regular bipartition balance, the conditional count \(2((m/2)!)^2/m!\), recursion with either independent or copied children, and the central-binomial Stirling asymptotic with summable errors. Finite enumeration alone cannot establish either infinite-dimensional asymptotic statement or literature originality. Numerical testing of large factorial logs uses floating-point approximations and does not supply rigorous asymptotic error certificates; the displayed analytic estimates do.

The code reconstructs its graphs directly from the stated recursive model, without using stored artifacts, remote services, or random seeds. Its examples do not exhaust the randomness of dimensions four and above; instead it exhausts the one-step matching choices conditional on representative child colorings and separately proves that this conditional count is universal.
