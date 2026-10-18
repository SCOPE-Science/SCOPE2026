---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For k>=4, 0<theta<1, lambda>0, reconstruct the Kissel–Külske–Rozikov positive boundary-law equations u=a(1+u^k+theta v^k)/(1+u^k+v^k), v=a(1+theta u^k+v^k)/(1+u^k+v^k), a=lambda^(1/k). Symmetric u=v=r branch has strictly increasing a(r). For u≠v the source linear elimination is reversible; q=v/u>1, D=sum_{0..k}q^j,E=sum_{0..k-1}q^j,C=sum_{1..k-1}q^j and H=C-theta D give u^k=1/H and lambda=D^k/(E^k H). H>0 iff theta<(k-1)/(k+1) and 1<q<q_theta, by monotonic sinh((k-1)x)/sinh((k+1)x), q=e^(2x). Strict derivative positivity follows the universal coefficient identity N_theta/(q-1)=(1-theta)D P_k+k q^(k-1) R_k with all P,R coefficients >0. Endpoint at q=1 gives lambda_c=((k+1)/k)^k/(k-1-(k+1)theta); endpoint H=0 gives infinity. Precisely one nonsymmetric pair exists iff lambda>lambda_c; plus unique symmetric branch gives exact count 1/3. Independently expanded the claimed polynomial factorization over rational/symbolic theta for k=4..12, verified representative reconstructions in the original system; unbounded conclusion rests on coefficient formula.

## originality

PASS

Kissel–Külske–Rozikov (2019) Theorem 6 explicitly gives one or at least three in separated regimes and then Conjecture 1 posits exact one/three for k>=4, with only Mathematica evidence k=4..15. The new globally monotone activity-vs-ratio parametrization resolves precisely that open statement, unlike later time-dependent Gibbs–non-Gibbs results. No Resultary or literature equivalent all-order proof was found; weak-indexed later resolution remains possible.

## value

PASS

The theorem resolves a named phase-diagram conjecture for every k>=4 and proves there are no hidden branches beyond the symmetric state and one spin-exchanged pair. The coefficientwise positivity identity supplies a reusable global monotonicity mechanism, stronger than merely reproducing an observed numerical critical curve. These are major structural constraints on a natural tree Gibbs specification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
