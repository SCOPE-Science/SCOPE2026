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
The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative only.

Critical checks:
- the source affine sum is \(\binom{m+n+1}{2}\);
- the source facet offset equals \(\binom{s+1}{2}-\Gamma\), where \(\Gamma\) counts cross-pairs between distinct right blocks;
- the intrinsic normal of an \(s\)-coordinate subset has squared norm \(s(N-s)/N\);
- the exact uniform-center facet distance is the displayed two-term formula;
- the global lower bound follows from \(s(N-s)\ge N-1\) and \(\Gamma\ge0\);
- equality requires \(s\in\{1,N-1\}\) and at most one right block;
- the singleton simplex summands produce \(x_i\ge1\), yielding the matching all-center upper bound and uniqueness.

`verify.py` independently rebuilds the simplex-summand family from Proposition 3.21 for \(2\le m,n\le7\). For every nonempty proper coordinate subset it directly counts contained summands, checks the block formula, computes exact squared center-to-support distance, and verifies all minimizers. It does not replace the arbitrary-parameter proof and does not assess originality.
