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

The proof has two logically separate components.

First, the source-supported model-theoretic component says that the universal process is ultrahomogeneous and that its relational predicates are finite-dimensional probabilities. Therefore the full joint law of an injective finite tuple is a complete automorphism-orbit invariant.

Second, the self-contained linear-algebra component fixes the independent uniform law \(u\) on \(S^n\), writes \(p=u+h\), and identifies the perturbation space with
\[
\bigcap_{i=1}^n\ker M_i=W^{\otimes n},
\qquad
W=\left\{v\in\mathbb R^S:\sum_{s\in S}v(s)=0\right\}.
\]
Thus the affine dimension is \((q-1)^n\). Because \(u\) is strictly positive, this affine space meets the simplex in a relative neighborhood of \(u\), hence in continuum many laws. Independent uniform pair marginals ensure non-degeneracy, universality realizes every such law, and separability supplies the matching continuum upper bound.

The accompanying `verify.py` is an independent finite replay of the linear constraints. It computes exact rational ranks for representative \((q,n)\) values and checks the binary parity family by exact rational marginalization. Its role is error detection only; the general theorem does not rely on extrapolation from those finite cases.
