---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

PASS. On unit-edge cube d_H, ||f||Lip=2 max_i||D_i f||∞, D_i f=(f(+)-f(-))/2. Derivation D_i Q_A f=T_{A_i}D_i f reduces upper bound to convolution operator ℓ∞-norm E|K_i|. Fix maximizing i, define g=sgn K_i and f(x)=x_i g(x_without_i)-g(o_without_i); its edge oscillations are bounded by 2 and its i-edge oscillation attains 2, while the projected i-derivative at basepoint has modulus E|K_i|. This gives exact sharpness for arbitrary family and both real/complex scalars. Pointed translations U_y f(x)=f(xy)-f(y) diagonalize Walsh basis; averaging arbitrary projection onto the given span yields unique diagonal Q_A with norm not greater, and dual argument gives free-space minimality. For degree k shadows are degree k-1 Krawtchouk kernels; elementary symmetric walk identity gives quadratic coefficient m*binom(m-1,floor((m-1)/2))/2^{m-1}. Independent exact integer-Walsh checks exhausted all nonempty support families n=1,2,3 (1+7+127) and matched extrema. General proof, not finite testing, covers all n.

## originality

PASS

PASS on material comparisons with bounded risk. Defant et al (2022/2023) give Walsh multiplier convolution norms and projection constants in C({±1}^m) with sup norm; their kernel formula is acknowledged prior. They do not provide the Lipschitz seminorm transfer/shadow optimization and globally compatible witness or adjoint free-space minimum. Cúth–Doucha group-action orbit projections are not arbitrary Walsh spectral projections. Equivalent functional-analytic presentation may be unindexed; failed Resultary is not proof of novelty.

## value

PASS

PASS. An exact relative projection constant for arbitrary Walsh spectrum in Hamming Lipschitz and free spaces is a natural Banach-space geometric operator invariant. The sharp realization of a coordinate convolution bound by one globally Lipschitz function, plus minimum norm among ALL projections, provides nontrivial structural information beyond familiar sup-norm kernel identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
