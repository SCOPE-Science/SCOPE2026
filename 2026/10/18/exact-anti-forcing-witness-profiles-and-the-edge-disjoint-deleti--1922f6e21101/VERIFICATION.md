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

# Reproduction instructions

Run `python3 verify_orbits.py` and `python3 verify_direct.py` (Python 3.9+ standard library only). The output of each command must match the corresponding `.out` file byte-for-byte, ignoring only an optional terminal newline if the execution environment reformats it. These outputs show complete counts and terminal markers `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`.

The first verifier builds \(GP(10,2)\), recursively enumerates every perfect matching, enumerates its complete automorphism group using exact adjacency-preserving backtracking, and searches every size layer of eligible deleted-edge subsets until the minimum in each automorphism orbit is located. For the disjoint variant, each candidate is explicitly tested for repeated endpoints. It reports numbers and representatives of every minimum type, together with the complete ordinary certificate adjacent-edge-pair histograms.

The second verifier independently builds the twenty-vertex LCF presentation, confirms an explicit isomorphism to \(GP(10,2)\), uses integer bit masks to enumerate all perfect matchings, and checks every eligible deletion subset through cardinality eight for **all 36 matchings**, with no use of symmetry. It crosschecks the complete four-parameter profiles and multiplicities.

For fixed \(M\), each program applies the exact equivalence that a candidate \(S\subseteq E(D)\setminus M\) leaves \(M\) unique if and only if it intersects \(N\setminus M\) for every other perfect matching \(N\). The scripts prove claims about this finite graph only. Their recorded terminal success markers do not constitute independent external scientific audit, which remains unperformed.
