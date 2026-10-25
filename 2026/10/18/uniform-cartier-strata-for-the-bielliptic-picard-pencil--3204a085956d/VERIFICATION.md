---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Reconstructed smoothness: quartic RHS has distinct roots iff t^2!=1; genus3 Picard plane quartic, basis dx/y^2, x dx/y^2, dx/y. Cartier p-semilinearity preserves zero/rank patterns. For p=6m+1, diagonal coefficient polynomials satisfy A=[z^{3m}]Q^{4m}=(t^2-1)^m H and B=[z^{2m}]Q^{4m}=(-1)^m binom(4m,m)(t^2-1)^m, so rank3 for H!=0 and rank1 at H=0. For p=6m+5, Cartier exchanges two basis vectors, with A=[z^{3m+2}]Q^{4m+3}=2(t^2-1)^{m+1}H; rank2 or zero, and semilinear iterates stabilize ranks. H has exact degree m, H(±1)!=0 from binomial coefficients (<p), and satisfies a hypergeometric coefficient ODE forcing simplicity of its roots because m<p. Re-derived coefficient polynomial identities independently for every prime 5..79 (20 primes), including exact degree, nonzero boundaries and gcd(H,H')=1, and specifically p11,t0=H=0 Cartier zero. A finite prime list is corroboration only, not the uniform proof.

## originality

PASS

Best-of-knowledge originality based on actual compared primary scientific claims and explicit residual risks; inaccessible texts not presumed to be absent or covering.

## value

PASS

The pencil is the natural bielliptic genus-three Picard family already studied geometrically. A single explicit characteristic-dependent Hasse polynomial gives a complete geometric p-rank and a-number stratification uniformly across all p>=5 with the precise number of exceptional smooth parameters and superspecial cases. This resolves a genuine natural invariant, not a table for arbitrary primes; full Newton polygons and geometric moduli remain outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
