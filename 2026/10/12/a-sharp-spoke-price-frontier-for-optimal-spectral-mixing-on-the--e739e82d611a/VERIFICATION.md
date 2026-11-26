---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On the mean-zero subspace the gap is the minimum of linear Rayleigh objectives. Averaging over shifts, reflection and the cycle-interchanging automorphism gives an optimizer with weights u,v and budget 10u+5tv=1. The zero-frequency eigenvalues are 0 and 2v; the other four Fourier blocks share eigenvalues 5u/2+v±sqrt(v²+5u²/4). Thus at ratio r=v/u the active eigenvalue is 2v for r≤1 and the lower Fourier eigenvalue for r≥1. With N(r)=5/2+r−sqrt(r²+5/4), the derivative on the second branch has sign D=(2+tr)N'−tN; D'=(2+tr)N''<0, D(1)=(2−5t)/3 and D(∞)=−5t/2. The first branch strictly increases, the endpoints u=0 and v=0 disconnect, and the unique symmetric optimum is r=1 for t≥2/5, otherwise the root of D=0 at r>1. The positive radical branch satisfies the unsquared equation because 2r−5t/4>0 in its applicable range. I separately checked the radical identity, frontier value, t=1/5 and small-price expansion with symbolic arithmetic (/workspace/independent_checks.py, petersen). For any asymmetric optimizer, equality of averaged Rayleigh quotients forces its Laplacian to agree with the symmetric one on the symmetric optimum's four nonconstant Fourier Fiedler modes (also present at the fivefold degeneracy). For the difference of weights, the k=1 outer imaginary equation makes all outer differences a common A; k=1 and k=2 outer real equations with swapped positive amplitudes p,q cancel the spoke difference and force (pα+qβ)A=0. Since p≠q, each spoke difference vanishes. The k=1 inner imaginary and real equations then make all inner differences constant and zero. Averaging alone would not establish uniqueness; these equations do. All weights are positive and the gap multiplicity is four below and five at and above the frontier.

## originality

PASS

The exact heterogeneous-price frontier and rigidity over arbitrary conductances are distinct from the known equal-price optimum, discrete-time Petersen result, and neighboring graph examples. No inspected stronger theorem directly yields the frozen classification. The unweighted spectrum and SDP framework are not asserted as original.

## value

PASS

The heterogeneous budget poses a natural optimizer-design question for a standard nontrivial graph. The answer identifies a plateau of identical edge weights despite unequal prices, a precise onset for favoring cheaper spokes, and positive uniquely determined weights everywhere. Establishing uniqueness rather than existence of a symmetric solution matters for interpreting this as a design rule and requires a graph-specific equality analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
