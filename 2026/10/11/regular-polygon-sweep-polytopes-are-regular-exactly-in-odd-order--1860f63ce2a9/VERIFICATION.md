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
The all-\(n\) proof is given in `RESULT.md`.

Critical checks:
- the source normalization is the centered Minkowski sum of all pairwise half-difference segments;
- the chord direction of \(a_i-a_j\) depends only on \(i+j\pmod n\);
- there are exactly \(n\) equally spaced generator-direction classes, hence exactly \(2n\) polygon edges;
- for odd \(n=2m+1\),
  \[
  2\sum_{d=1}^{m}\sin\frac{\pi d}{n}
  =
  \cot\frac{\pi}{2n};
  \]
- for even \(n=2m\), the even and odd direction classes have lengths
  \[
  2\sum_{i=1}^{m-1}\sin\frac{i\pi}{m}
  =
  2\cot\frac{\pi}{n},
  \]
  and
  \[
  2\sum_{r=0}^{m-1}\sin\frac{(2r+1)\pi}{2m}
  =
  2\csc\frac{\pi}{n};
  \]
- the even-order support equations yield
  \[
  p=\frac{1+\cos^2(\pi/n)}{\sin^2(\pi/n)},
  \qquad
  q=\frac{2\cos(\pi/n)}{\sin^2(\pi/n)};
  \]
- every even-order vertex has one common radius, proving cyclicity;
- summing \(hL/2\) over all edges gives the stated area;
- unequal alternating sides exclude any odd edge-step symmetry when \(n\) is even.

`verify.py` independently constructs all half-chord generators for \(3\le n\le60\), evaluates support numbers directly from those generators, reconstructs every vertex from consecutive support lines, and checks side lengths, perimeter, area, cyclicity, and the parity formulas. Finite computation is corroborative only and does not assess originality.
