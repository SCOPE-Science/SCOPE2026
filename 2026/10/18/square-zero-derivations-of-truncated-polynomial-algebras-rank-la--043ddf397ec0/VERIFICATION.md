---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The Leibniz relation is n*t^(n-1)*f=0 for f=D(t). In odd characteristic and n>=3, applying D^2 to t and t^2 gives ff'=f^2=0, also sufficient on all monomials. For nonzero f of order a the conditions are 2a>=n and, if p does not divide a, 2a-1>=n. This yields exactly the stated cutoff, including the extra layer when n is even and p divides n/2; every such f satisfies the Leibniz relation. The nonzero monomial images have distinct leading degrees, and are indexed by 1<=j<=n-a with p not dividing j. For n=1 only zero is possible, and for n=2 in odd characteristic D(t)=ct and D^2(t)=c^2t. In characteristic two use B=K[s]/s^m and write f=u+tv at length 2m, f=su+tv at length 2m+1. The two summands are direct, and the maps from B multiplying by s or t into their respective target summands are injective in the odd-length parametrization. In either case D^2=0 gives uv=v^2=0 in B, and the image is the cyclic B-span of f of dimension m-min(ord(u),ord(v)), with ord(0)=m. Counting exact orders proves the coefficients and totals; rank m occurs just when u is a unit and v=0. The square-zero set over an algebraic closure is a finite union of the stated incomparable m-planes, hence those are precisely the components of the reduced variety. Hand checks give P_(4,2)=P_(5,2)=1+3z+2z^2 and P_(6,3)=1+2z+24z^2 (the rank-two layers have orders 3 and 4).

## originality

PASS

Best-of-knowledge assessment at the frozen record: the inspected older primary sources do not determine the combined ordinary rank, parity and component laws. Several distinct later-dated indexed records give demonstrably equivalent characteristic-two results, some stronger, and are not credited as independent mathematical advances on the common claims. Their dated catalogue appearance does not demonstrate prior coverage of this frozen result; no earlier version of those statements was identified. The restricted nilpotence and differential-module comparisons do not supply a dominating theorem.

## value

PASS

The rank invariant determines every homology dimension for a natural differential on a basic local algebra. Exact coincidence between even and odd lengths despite their different acyclicity, the uniform component decomposition, and the extra odd-characteristic valuation layer give substantive structural information beyond a derivation parameter count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
