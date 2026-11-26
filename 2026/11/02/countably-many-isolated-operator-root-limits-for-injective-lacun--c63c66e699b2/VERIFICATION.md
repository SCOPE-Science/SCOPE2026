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

For each basis vector the logarithm of the root entry is minus c/n times the spike sum on [k,k+n-1]. Take q^m<=n<q^(m+1) and extract a convergent ratio n/q^m. An interior ratio u yields exp(-cq/((q-1)u)) at every fixed k. At ratio 1, a fixed offset n-q^m=d gives the cut k<=-d, while a diverging offset gives alpha I. At ratio q, a fixed deficit q^(m+1)-n=d gives the cut k<=d, while a diverging deficit gives beta I. The initial prefix is constant in n for each fixed k. The sequences q^j-s, floor(u q^j), and q^j±j realize all steps, interior scalars, and endpoints, respectively. On the uniformly bounded diagonal family coordinate convergence is both weak and strong convergence, and diagonal subsequence extraction shows that every scalar limit along a unit vector comes from one of these operators. Testing entries s,s+1 isolates each step; the scalar interval is connected, and the steps have the stated strong limits at both ends. Negative-index windows give norm of each root and power equal to one; long negative blocks give numerical radius one. Strict positivity gives injectivity and puts every basis vector in the range. Since all cluster operators have norm at most beta<1, no norm-convergent subsequence is possible. The included checker was inspected, not rerun; its recorded 18,600 checks test finite spike sums, not the infinite theorem, for which the exhaustive analytical argument suffices.

## originality

PASS

Pass is for the exact geometrically spaced bilateral family, including two-sided accumulation of steps and the uniform gap between all weak/strong cluster norms and the norms of the roots. The existence of disconnected clusters, even the qualitative combination of an interval, countably many isolated steps and identical vector scalar ranges, is not new by itself.

## value

PASS

Finite-ratio spikes occupy a materially different regime from the superlacunary example: earlier spikes retain nonzero normalized mass, so every strong cluster operator loses a fixed amount of norm even though every root has norm one. The full cut classification also gives two distinct strong accumulation limits for the isolated operators, not just another disconnection witness. This is a natural exact boundary example for how operator-root limits, scalar asymptotic numerical ranges and spectral radii can differ.

The dated certificate retains the supplied scientific assessment, sources and limitations.
