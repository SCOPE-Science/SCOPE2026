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

The proof in `RESULT.md` reduces the unrestricted minimum problem to four exact
target equations.

For five distinct prime factors, Hagis--Lord's inequality gives
\[
H^*(n)>\frac{64}{7},
\]
so an integral unitary harmonic mean is at least \(10\). The verifier therefore
checks only
\[
h\in\{10,11,12,13\}.
\]

For a fixed target, it represents the ordered exact prime-power components by
\[
x_1<\cdots<x_5
\]
and maintains the exact prefix product
\[
P=\prod \frac{x_i}{x_i+1}.
\]
If \(r\) components remain and \(x\) is the next one, monotonicity gives the
necessary inequality
\[
P\left(\frac{x}{x+1}\right)^r\le\frac{h}{32}.
\]
This yields a finite next-component bound. The implementation tests the
cleared-denominator form with integers, so it introduces no floating-point
rounding. Only genuine prime powers with unused prime bases are admitted.

When one component remains, the verifier solves it exactly from
\[
x=\frac{T}{P-T},\qquad T=\frac{h}{32}.
\]
Every returned component tuple is then substituted back into the defining
product and its prime bases are checked to be pairwise distinct.

Expected complete output:
- mean \(10\): no solution;
- mean \(11\): no solution;
- mean \(12\): no solution;
- mean \(13\): exactly the component tuples
  \((2,5,7,9,13)\) and \((3,4,5,7,13)\), whose products are \(8190\) and \(5460\).

The finite recursion is exhaustive because the branch inequality is proved
before enumeration and its left side is strictly increasing in the candidate
component.
