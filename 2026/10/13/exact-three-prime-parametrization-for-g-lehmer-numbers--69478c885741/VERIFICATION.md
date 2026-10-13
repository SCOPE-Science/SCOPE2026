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

The universal theorem is symbolic. Its critical chain is:

1. an odd \(G\)-Lehmer number is squarefree;
2. for three prime factors,
\[
\Phi(n)\ge\frac{64}{125}n
\]
and \(n\ge105\), so
\[
\mathcal F(n)<2\Phi(n);
\]
3. divisibility therefore forces \(\Phi(n)=\mathcal F(n)\);
4. after assigning each prime its sign \(\beta(p)\), equality is exactly
\[
xy+xz+yz=x+y+z;
\]
5. the two mixed sign patterns are exactly the two quadratic factorization families stated in `RESULT.md`.

The packaged `verify.py` independently enumerates every product of three distinct odd primes not exceeding
\[
5\,000\,000
\]
and compares the direct divisibility predicate with the two factorization predicates. It also checks that every direct hit has quotient exactly \(1\). The expected direct-hit list is
\[
255,\ 385,\ 34561,\ 195841,\ 1034881,\ 4070401,\ 4746241.
\]

This finite sweep is corroborative only. It is not used to infer the theorem beyond the tested range.
