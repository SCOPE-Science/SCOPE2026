---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the monomial cyclic shift |T| and |T*| are commuting positive diagonals with eigenvalues a^j and a^(j+1 mod n). Their norm/numerical radius maxima reduce exactly to 1/4 max{U+V,Z+1}+1/2 max{P,Q}. For n=2 this is strictly increasing with max(theta,1-theta). For n>=3, F=U+V-Z-1 strictly decreases, with F(1/2)>0 and F((n-1)/n)<0; crossing tau is unique. On [1/2,tau], derivative has sign of strictly increasing G with G(1/2)<0; post-crossing branches are increasing. Thus the classified unique global optimizer and strict n>=3 gain follow. Verified exact rational n10,a=6/5,r=1 certificate using Fraction integers, and independent numeric n3 tau≈0.518032178392, Phi≈8.571894479<9 plus n10 smooth theta≈0.5484123. Finite tests supplement global analytic monotonicity, not an all-n proof.

## originality

PASS

The 2026 Mondal--Mohapatra--Dewage paper introduces the parameterized weighted upper bound and proves existence of optimum but not the exact optimizing parameter for geometric finite cyclic shifts. Older Chang--Wang and Chien--Nakazato papers optimize/analyze actual numerical radius or different infinite unilateral shifts, not this 2026 weighted-bound functional. No searched prior exact all-dimensional nonsmooth/smooth regime theorem implies the claim.

## value

PASS

The parent weighted numerical-radius inequality explicitly introduces an optimizer θ but only guarantees existence. Geometric cyclic monomial matrices are a natural invertible test family where wraparound creates a structural switching threshold. Complete all-dimensional uniqueness and exact n=2-versus-n>=3 gain, with two genuinely realized smooth/nonsmooth optimizer regimes, provide motivated exact parameter geometry; the claim explicitly does not pretend to compute w(T) itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
