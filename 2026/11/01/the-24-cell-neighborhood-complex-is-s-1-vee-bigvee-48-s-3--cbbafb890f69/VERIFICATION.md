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

Run `python3 verify_24cell.py` and `python3 homology_f2.py` from this package using only Python 3.9+ standard library. Expected stdout is reproduced verbatim in `verification_output.txt` and `mod2_output.txt`.

The main verifier independently builds all vertices, 96 edges and 5088 faces, enumerates 2519 matched pairs and 50 unmatched faces, then constructs all 22128 incidences of the face-poset Hasse diagram and checks that reversing precisely the matched edges gives a DAG by full Kahn topological elimination (5088 of 5088 nodes visited). These are exact integer and bit-mask checks; no random data or finite numerical approximation is involved.

The separate homology verifier constructs boundary matrices mod two directly from the face list, without using the Morse pairing, and obtains ranks \(23,240,720,840,504,168,24\) for dimensions one through seven. Mod-two ranks are a consistency check and are not misrepresented as an integral homotopy proof. The integral homotopy conclusion uses the certified acyclic matching, discrete Morse theory and the fact that every map \(S^2\to S^1\) is null-homotopic.

No equivariant, deformed-polytope or publication-priority certification is claimed. External mathematical validation has not been performed.
