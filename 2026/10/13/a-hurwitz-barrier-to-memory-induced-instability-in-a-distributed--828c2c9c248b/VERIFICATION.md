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

With the same scalar Caputo distributed-order symbol Psi(s)=integral omega(alpha)Tc^(alpha-1)s^alpha d alpha, support 0<alpha<=1, nonnegative omega, principal branch, every Re s>=0 has Re Psi(s)>=0. A Hurwitz J has strictly left-half-plane spectrum; hence det(Psi(s)I-J) cannot vanish in Re s>=0, including s=0 because det J !=0. The published distributed-order root criterion gives linear/local asymptotic stability. Separately reconstructed Ali 2026 baseline equilibrium N=902.9557574728, (X,H,Y,Z)=(362.377257655,84.479329039,131.439986279,324.659184500). Independent symbolic differentiation yielded quartic coefficients (0.578669909137,0.088107704477,0.004035626673,0.000039900775658), positive Routh-Hurwitz minors 0.046949650671 and 0.000176110134. This certifies the fixed baseline against every common nonnegative density supported in (0,1], not compartment-specific memory nor altered model parameters.

## originality

PASS

Saberi Najafi et al 2011 develop the general characteristic-root criterion for distributed-order linear systems and discuss robust stability; Theorem 3.1 is credited, not claimed new. The elementary positive-real s^alpha observation yields a model-independent Hurwitz sufficient condition, and the distinctive source-specific contribution is the reconstructed endemic equilibrium and verified all-memory Routh-Hurwitz certificate. Ali 2026 reports numerical searches over memory-shape windows rather than the complete universal density result. No checked primary source states this exact SEIRS parameter certificate.

## value

PASS

The exact all-nonnegative-common-memory conclusion removes the possibility of memory-induced destabilization of a biologically specified endemic equilibrium across an entire infinite-dimensional density class, upgrading a finite parameter scan. It is a motivated stability boundary and reproducible baseline certificate, albeit an easy half-plane principle once the scalar same-order assumption is recognized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
