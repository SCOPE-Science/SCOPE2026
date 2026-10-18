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

# Reproducibility and verification

The following files form an exact standalone Python 3 package: `fano_rainbow_1.py`, `fano_rainbow_1.out`, `fano_rainbow_2.py`, and `fano_rainbow_2.out`. All arithmetic and enumeration is integer-valued; no external Python libraries, solver packages or internet access are needed.

To replay, use the following commands from the same directory:

```sh
python3 fano_rainbow_1.py > replay1.out
python3 fano_rainbow_2.py > replay2.out
cmp replay1.out fano_rainbow_1.out
cmp replay2.out fano_rainbow_2.out
```

Both programs actually executed successfully and emitted matching recorded outputs. The first finds eight proper three-edge-colourings up to palette renaming by complete constraint backtracking; checks 28 pairs and their three geodesics; recovers the seven-antiflag obstruction sets, the twofold incidence multiplicities, and the full fresh-fourth-colour matching repair spectrum; validates a four-colour certificate. The second uses a different PG(2,2) incidence construction, enumerates all 24 perfect matchings and 48 named proper 3-edge-colourings, checks all 91 vertex-pair distances and the four-colour rainbow geodesics, and independently exhausts all matching recolourings for all 48 named proper inputs. Successful marker strings are `ALL_VERIFY_OK` and `INDEPENDENT_VERIFY_OK` and are not claims of external independent validation.

The mathematical completeness argument derives from (i) unique shortest two-edge paths force proper three-edge colouring; (ii) fixing the three colours at a chosen cubic vertex is a lossless palette normalization; (iii) all proper assignments are visited by backtracking; and (iv) every fresh-fourth-colour selection compatible with strong geodesic coloring is a matching of size at most seven. The computational results are finite graph theorems, not evidence of a universal parameter-family formula. Independent audit status remains unperformed.
