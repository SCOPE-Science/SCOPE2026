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

The infinite theorem is proved symbolically in `RESULT.md`.

For odd \(k\ge3\), the critical identity is
\[
v_2(y^k-1)=v_2(y-1)=n+v_2(n),
\]
because \(y\) and \(k\) are odd. This forces
\(y>2^{n+v_2(n)}\), whereas the defining equation has size only
\(n2^n+1\).

For even \(k\), putting \(z=y^{k/2}\) gives a square. The coprime consecutive
integers \((z-1)/2\) and \((z+1)/2\) multiply to
\(m2^{n+t-2}\) when \(n=2^t m\) with \(m\) odd. Hence the even member is at
least \(2^{n+t-2}\) while the odd member is at most \(m\), forcing
\[
2^{n+t-2}\le m+1,
\]
which fails for \(n\ge4\). Direct evaluation leaves only \(n=2,3\).

The packaged checker provides finite corroboration. It verifies all square
indices through \(100000\), checks representative odd exponents through a
stated finite range, and asserts the exact elementary inequalities used in the
proof. These finite checks are not an infinite certificate and are not used to
infer the theorem.
