---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS. Balanced events give a four-cell probability vector (a/2,a/2,b/2,b/2) after choosing correlation sign, a=(1+s)/2 and b=(1−s)/2. The expectation identities P=E+X⊗E(X⋅) and Q=E+Y⊗E(Y⋅) yield C=s[X E(Yf)−Y E(Xf)]. Four-cell conditional Jensen reduction and pairwise antisymmetrization preserve the output and decrease Lp input norm even for complex values. On the surviving two-coordinate sector input norm is (a|U|^p+b|V|^p)^{1/p}; output swaps coordinates with factors 2sa and 2sb, so the weighted off-diagonal induced norm is max of two exact coefficients: 2s a^{1−θ}b^θ. Direct rational four-cell P,Q matrix construction and sharp sector witnesses check sampled correlations/exponents independently. Derivative log optimization sign 1+(1−2θ)s−2s² gives unique interior s_p; at endpoint θ=0 the supremum 2 is unattained for noncommuting pairs and c=0 or |c|=1 give identically zero C, not a continuous endpoint filling. The universal result comes from algebra, not sampled tests.

## originality

PASS

PASS best-of-knowledge: all-p balanced-event difference norms, sharp correlation choice and endpoint jump are not supplied by previous binary-product norms or numerical-radius studies; extensive historical alternating-expectation literature could contain an equivalent expression.

## value

PASS

PASS. The exact all-Lp commutator interpolates a concrete noncommutativity measure, determines the extremal correlation, and exposes a genuine endpoint-vs-interior near-identical-partition instability. Unlike a routine Hilbert commutator bound, it supplies the complete phase across Lp including p=1,∞, a natural structural dependence invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
