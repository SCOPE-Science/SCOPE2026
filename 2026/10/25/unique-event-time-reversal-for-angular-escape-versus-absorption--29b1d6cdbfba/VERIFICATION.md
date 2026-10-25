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

# Reproducibility and verification

The finding is a theorem about a one-dimensional angular diffusion during **one bound episode** at a reactive wall. Its proof uses the exact exit-time Laplace transform, event-conditioning identities, an analytic one-minimum argument for the sign function, and small-/large-rate expansions. These analytic steps establish all continuum parameter values; numerical sampling is not substituted for them.

## Direct checks

The formula \(F=\cosh(uz)/\cosh z\) is the unique solution to the backward diffusion boundary problem and reproduces the angular Green-function result in Bressloff's equations (3.18)–(3.25). The exact identity
\[
\tau_{\rm esc}-\tau_{\rm abs}=\frac{H(z,u)}{\kappa(1-F)}
\]
allows a sign check without subtracting two potentially close conditional means. The derivative proof gives exactly one interior root, because the comparison function has a single strict minimum and its endpoint signs are fixed. Taylor expansion to order \(z^6\) and the layer substitution \(u=1-w/z\) give the two endpoint laws. An independent moment calculation of \(\mathbb E[T]\) and \(\mathbb E[T^2]\) recovers the weak-killing threshold \(u=1/\sqrt5\).

## Standalone computation

Run `python3 checker.py` from the extracted package directory. It requires only the Python standard library. The script checks the root/sign relation at \(z=0.5,1,3,10,30\), verifies equality of conditional means at those numerically located roots, and tests the weak- and strong-killing limits. Floating-point checks cannot certify uniqueness or asymptotics by themselves; the proof in `RESULT.md` supplies the universal quantifiers.

## Known limits

At \(u=1\), killing before escape has zero probability and its conditional mean is undefined, so the theorem explicitly assumes \(u<1\). At \(\kappa=0\), killing never happens, so the weak-killing threshold describes the right-sided limit only. The result does not cover memory-dependent killing, drift in orientation, or bulk excursions and returns.
