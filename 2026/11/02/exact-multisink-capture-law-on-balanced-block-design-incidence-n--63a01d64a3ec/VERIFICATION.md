---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For 3≤t<v, BBᵀ=δI+λ11ᵀ has full row rank and acts as δ on the zero-sum space. Applying A² to a sink point generates the constant point vector modulo that sink, hence the minimal adjacency orbit is W⊕BᵀW, where W is spanned by the sink coordinates and 1. The orthogonal complement is invariant and lossless. An eigenvector of the dissipative generator in this orbit with zero real part would have every sink coordinate zero by strict positivity of the losses; it would then be an adjacency eigenvector orthogonal to every orbit generator and hence zero. All orbit modes decay, including in the presence of Jordan blocks. The resulting orthogonal projector averages the s unmarked point coordinates. On the block side the row-space leverage is k/(vρ)+(k−k²/v)/δ=k/ρ=v/b, and its dark subspace subtracts u(s−u)/(sδ). This proves the point, block and trace laws and the stated certainty criteria. For s=1 the correction is zero. The Fano line-intersection distributions are one line with three marked points and six with one for a collinear triple, versus three with two, three with one and one with none for a noncollinear triple. The prior independent replay used literal adjacency powers on 237 sink sets, including unequal positive rates and labeled repeated blocks; finite propagation is corroboration, not the limit proof. The frozen checker uses s−u in the symmetric product and was not executed. The frozen slogan was false if read at t=v: s=0 makes the block expression undefined and the true mixed efficiency is 2v/(v+b), not 2(v+1)/(v+b). The complete replacement repairs/2/SLOGAN.txt restores 3≤t<v and the uniform positive hopping hypothesis, without changing the theorem.

## originality

PASS

The distinct claim is the evaluated local intersection law and certainty obstruction for arbitrary balanced 2-design incidence graphs with the stated point sinks, not the known Krylov projection principle or design spectra. The two-point affine-plane result genuinely overlaps in the model, but not the stated range or family. Related multi-marked Hermitian search and capture ranks on other host graphs do not give these sitewise probabilities.

## value

PASS

The local and mixed efficiencies answer different natural transport questions. The Fano cases give different perfect-capture behavior at the same mean. The leverage bound gives a strict placement-independent obstruction for block starts in nonsymmetric designs even at s=1, where the variance correction vanishes. The law is a useful exact diagnostic over the full design family, without claims about time to capture or noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
