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

# Verification procedure and bounds

Run `python3 artefacts/check_biclique.py` with Python 3.8 or newer. This deterministic standard-library program computes every edge-neighbourhood colour count from scratch for all reported constructions in a bounded parameter rectangle and exhaustively enumerates each binary colour-class subset of the two exceptional graphs. It also independently enumerates small binary-colouring cases.

Observed outputs:

```
PASS: modular and exceptional constructions for 2 <= a <= 20, a <= b <= 30
PASS: two-colour full labelled enumeration at K_(2,b) b=2,4,6,8 and six obstructions
PASS: 2^12=4096 one-class subsets of K_(3,4), max 4, exactly 18 rectangles
PASS: 2^20=1048576 one-class subsets of K_(4,5), max 6, exactly 1900 maximizers
PASS: complete finite certificate; infinite cases rely on the accompanying proof
```

The bound for a single colour in \(K_{4,5}\) is separately proved for all possible degree configurations in RESULT.md. The finite programme never treats computational trials for bounded \(a,b\) as a proof of the unbounded construction, which instead follows from the elementary inequality given there. No independent human or external mathematical audit was conducted.
