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

The unrestricted proof is symbolic and appears in `RESULT.md`.

The critical chain is:
\[
\sigma(n)\text{ is an even square}
\Longrightarrow b=v_2(\sigma(n))\ge2\text{ and }2\mid b,
\]
followed by
\[
2-\frac1n
=I(n)I(\sigma(n))
\ge
\left(\prod_{p\mid n}\left(1+\frac1p\right)\right)(2-2^{-b}).
\]
The strict upper bound \(2-1/n<2\) then yields the claimed product and least-prime inequalities.

For odd \(p\) and odd \(a\), the checker verifies the local identity
\[
v_2\left(\frac{p^{a+1}-1}{p-1}\right)
=v_2(p+1)+v_2(a+1)-1
\]
on a finite grid. The proof uses the standard \(2\)-adic LTE theorem, not this finite check.

The checker also searches \(1<n\le200000\) for the defining equation and finds no solution. This finite absence is not used to infer nonexistence.
