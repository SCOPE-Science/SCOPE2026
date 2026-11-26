---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Substituting r=γh/(1+γh) gives the absolutely summable coefficients (1−r)r^k[1+ak−a(k+1)r]; projection onto residue classes mod n gives the asserted kernel. For a forward row shift the bracket exceeds the diagonal bracket by aj(1−r^n), so the diagonal controls positivity. Independent replay /workspace/branches/replay_4.py reconstructed all six exact Bernstein minima for dimensions 2–4, checked the five-cycle witness and directly inverted circulants at rational r for three sizes, and recomputed both n=5 endpoints and c*. The n=5 value at r=3/5 is strictly negative; H_(n+1)−H_n=r^n[1−an(1−r)] is strictly negative there for n≥5. With H_n(0)=1 and H_n(1)=n, two roots are forced and Descartes' two-sign-change bound makes them simple and exhaustive. Pointwise limits on compactly bracketed fixed r locate the lower root at 1/a; bracketing the upper root on r=1−c/n reduces its scaled limit to the unique strictly positive zero of e^c−1−(a/√2)c. Thus the asymptotic claims do not rely on numerical fitting. Unit row sums follow from R(0)=1; at zero the map is I, and at either positive boundary only the diagonal vanishes. The analysis is for exact end steps on uniform one-way cycles, not general or internal-stage positivity.

## originality

PASS

The L-stable rational function, its method-wide positivity bound, and its use on periodic upwind advection already exist. The matched primary coverage and related catalogue claims do not establish the same map's complete dimension-dependent cyclic positivity region, including the sharp five-state loss/recovery threshold and the upper asymptotic law. No global publication-priority claim is supported.

## value

PASS

This separates a useful sufficient timestep restriction from exact endpoint positivity on a standard model of periodic transport. It explains why a stochastic endpoint can recover beyond a forbidden band, gives the smallest such cycle and exact entry diagnostics, and distinguishes an order-one initial bound from order-n recovery. These are structural and directly useful facts, not sample-specific sign tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
