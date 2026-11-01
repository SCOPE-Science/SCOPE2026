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

Execute `python verify_icosahedral_five_cut.py` with Python 3.10+ and SymPy. The executable graph edge list, simplex enumeration, orientation convention, complete acyclic matching construction, exact chain cancellation and Smith normal forms are self-contained in the script. The deterministic JSON output must agree with `verification_output.json`.

The graph has 12 vertices, 30 edges and 20 triangular faces, and its explicit edges are isomorphic to the standard icosahedral graph. Two independent methods enumerate the 300 facets and exactly 2,618 total faces. The face counts in dimensions from \(-1\) through \(6\) are \(1,12,66,220,495,792,732,300\).

The increasing and decreasing order matchings have 1,286 and 1,285 pairs. A complete acyclicity test traverses 13,224 face incidences for each order. The first reduced integral boundary ranks in degrees five and six are five and two, with Smith factors \((1,1,1,1,2)\) and \((1,1)\). The second has ranks five and three with factors \((1,1,1,1,2)\) and \((1,1,1)\). Both satisfy the chain-square-zero assertion and give identical integral homology. Direct full simplicial mod-two boundary ranks in degrees one to six are \((11,55,165,330,461,270)\), providing an independent field check. This is an exact finite computation; no infinite parameter range is certified.

The package records the full resulting integral Morse boundary matrices and output marker `ICOSAHEDRAL_FIVE_CUT_INTEGRAL_TORSION_EXACT_VERIFIED`. Neither this certificate nor the review represents an independent external audit.
