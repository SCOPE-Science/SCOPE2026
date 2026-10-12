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
# Verification

The proof of the limit is analytic. The accompanying `verify.py` is a regression checker for the exact recurrence and finite source values.

For an admissible canonical edge \(a<b\), it checks
\[
(N-a)b\le T_N,
\]
and iterates the farthest admissible successor \(\lfloor T_N/(N-a)\rfloor\). Dynamic programming for every \(2\le N\le150\) independently confirms that this greedy hitting time is the shortest order-preserving canonical subcycle length.

The checker reproduces the five values quoted in the source:
\[
g_{10}=6,\quad g_{100}=24,\quad g_{10^4}=260,\quad g_{10^6}=2628,\quad g_{10^8}=26304.
\]
It also evaluates a long prefix of
\[
C=\sqrt2\sum_{r=0}^{\infty}\frac{\sqrt{r+1}-\sqrt r}{r+1}
\]
with its leading positive tail and obtains \(2.630472693\ldots\), consistent with the proved constant.

Finite computations do not certify the asymptotic theorem. The infinite claim rests on the exact band-width calculation for the centered recurrence and the dyadic bound controlling all outer bands.
