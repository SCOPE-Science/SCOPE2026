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
The theorem is proved symbolically in `RESULT.md`; finite enumeration is corroborative only.

Critical checks:
- the type-\(D_n\) spin orbit is the \(\frac12\)-scaled sign vectors with fixed sign parity;
- its H-description consists of coordinate bounds and parity inequalities;
- coordinate facets lie at distance \(1/2\) from the origin;
- parity facets lie at distance \((n-2)/(2\sqrt n)\);
- these two distances agree exactly at \(n=4\), while the parity distance is larger for \(n\ge5\);
- opposite coordinate facets force the unique radius-\(1/2\) center to be \(0\);
- every spin-orbit vertex has norm \(\sqrt n/2\);
- Weyl invariance forces both unique extremal ellipsoids to be Euclidean balls, hence the John and Löwner ellipsoids are the inball and circumball.

`verify.py` enumerates the spin-weight vertices for \(4\le n\le12\), verifies every displayed parity and coordinate inequality, checks the exact contact orbit, and confirms affine independence for representative facets. It does not replace the arbitrary-dimensional proof and does not assess originality.
