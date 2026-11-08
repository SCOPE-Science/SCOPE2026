---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For odd m>=3, q=2^m, d=(m+1)/2, let s=2^d, H(u)=u^(s+1). Since (s-1)(s+1)=2^(m+1)-1 ≡1 mod(q-1), H is a permutation with inverse x^(s-1), also at zero. Direct exponent identities yield F_delta(H(u))=H(u)+L(u)+delta=H(u+1)+1+delta with L(u)=u+u^s. Therefore F_1 is conjugate to fixed-point-free translation u->u+1 and consists of q/2 two-cycles. As gcd(d,m)=1, ker L={0,1}; im L is the trace-zero hyperplane (size q/2); F_delta has exactly two fixed points iff Tr(delta)=0, otherwise none. If F_delta^2(H(u))=H(u), set v=H^(-1)(F_delta(H(u))); then L(v)=L(u), so v=u (fixed point) or v=u+1 (forces delta=1 via H(u+1)-H(u)=L(u)+1). No other primitive two-cycles exist. The formula covers all delta and m odd; all 168 translates in GF(2^3),GF(2^5),GF(2^7) independently checked by direct field arithmetic.

## originality

PASS

Ding–Qu–Wang–J. Yuan–P. Yuan establish the unshifted polynomial as a permutation for odd m, but bijectivity alone does not decide the translated orbit census; the affine conjugacy and trace-fiber dichotomy give a stronger, structurally different exact result. No identified prior formulation supplies the all-translate prohibition on nonexceptional two-cycles. Published journal article theorem numbering differs from the frozen citation to its arXiv v1; bibliographic version precision warrants correction before publication, not scientific rejection.

## value

PASS

Exact periods one and two of an entire natural q-parameter family of finite-field permutations are useful arithmetic-dynamical invariants; the unique involutory parameter and trace-controlled fixed-point counting provide a sharp structural classification extending the classical permutation property.

The dated certificate retains the supplied scientific assessment, sources and limitations.
