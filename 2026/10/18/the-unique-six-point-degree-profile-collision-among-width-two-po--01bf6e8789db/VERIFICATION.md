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
# Direct finite verification

Run `python3 verify_uppertriangular.py`, `python3 verify_permutation.py`, and `python3 verify_witness.py` with Python 3 standard library; no external library or network resource is needed. The companion three text outputs are records of successful local runs, not substitutes for running the programs.

The upper-triangular verifier enumerates every subset of the \(\binom n2\) ordered pairs in one linear extension for every \(1\le n\le6\), checks transitivity and exclusion of three-element antichains, and exhaustively tests degree-preserving isomorphisms. Counts: isomorphism types \((1,2,4,10,26,75)\); degree-profile classes \((1,2,4,10,26,74)\). The single six-element collision consists of precisely two types. A second independent enumeration by \(321\)-avoiding permutations returns identical totals.

The witness program checks two transitive, connected width-two relations explicitly, shows that their paired degree multisets coincide with six distinct entries, forces the only possible profile-preserving bijection, and detects an arc disagreement. Consequently, even the corresponding labelled net-degree vectors can be made equal, despite different arc relations.

The completeness proof depends on elementary finite enumeration and exact isomorphism tests, not timeouts or partial search. Nothing is asserted about seven or more elements. Verification here is same-model reproduction and has not undergone independent audit.
