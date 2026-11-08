---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For k>=2 orthogonal positive norm-one summands g in C([0,1]), each summand has a norm-one peak in a distinct component of {g>0}. They give k ordered peaks value 1, separated by k-1 true zeroes, hence d>= ordered minimax value. For any ordered witness and δ equal to peak/valley cost, lower envelope L=max(f-δ,0), upper U=min(f+δ,1) and a continuous interpolant w taking 1 at peaks and 0 at separators give g=L+(U-L)w with exactly those 1/0 values; splitting across zeroes produces k valid orthogonal summands. That yields equality (1) and attainment characterization. Compact limit of witnesses for a convergent g_n∈I_k cannot collide adjacent 1/0 points, proving I_k norm closed. For f(t)=t, a t1<s1 witness has max(1-t1,s1)>1/2, but clustered witnesses approach 1/2, so infimum unattained. Merging summands gives monotonic d_k; vanishing lower bound m, uniform continuity obstruction to arbitrarily many alternations at δ<1/2, and clustering near f nearest 1/2 jointly give limit max(1/2,m). For piecewise-affine f, any δ<1/2 witness can shift highs and lows to strict ordered extreme vertices, giving finite formula (3). Independent exact rational evaluations: vertex heights [0,1,0,1] gave d2=0,d3=1/2; [0,3/4,0,3/4,0] gave d2=1/4,d3=1/2. Tests do not cover all continuous functions.

## originality

PASS

PASS for exact all-k point-to-locus uniform distance, nonproximinality and piecewise-linear finite minimax. Taghavi’s new 2026 paper proves I_2(C(X)) closed for locally path-connected X and distance from identity for general unital A; those known facts are credited. Neither gives d_k(f) for arbitrary positive norm-one f or the unattained infimum from f(t)=t. One-dimensional persistence/pairing of extrema may offer alternate language, but no checked theorem yields this very constrained orthogonal-unit target exactly. The exact peak–valley minimax is independently motivated as nonlinear best uniform approximation, with priority risk from older persistence/approximation literature.

## value

PASS

The nonlinear locus of mutually orthogonal positive unit summands is natural in C*-algebra geometry and explicitly nonproximinal despite closedness. Exact d_k(f), its attainment characterization and k→∞ limit give a complete one-dimensional approximation theory rather than a routine restatement of qualitative closedness. Finite rational formula is directly usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
