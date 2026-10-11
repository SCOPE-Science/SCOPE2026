---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

A tuple is a locally constant map from Cantor space into \(A^k\); composing pointwise with the diagonal \(G\)-orbit map gives a finite nonempty support of orbit types. Mayr--Ruškuc's semidirect automorphism decomposition shows this support is invariant. Conversely, equal supports determine clopen partitions with the same marked-point incidences; Cantor clopen homogeneity gives a homeomorphism fixing the filtering points and matching the parts, and a finite clopen refinement supports a continuous local \(G\)-valued gauge that maps the tuple values pointwise while being compatible at each marked point. Thus support equality is exactly automorphism equivalence. For \(r\ge1\), exactly the \(r\) required marked orbit types must be present and every superset is realizable, giving \(2^{q_k-r}\); for \(r=0\), the support must merely be nonempty, giving \(2^{q_k}-1\). Signed Stirling inversion then converts all-tuple to injective profiles. Fresh arithmetic independently reproduced the packaged Example 1.2 values through \(k=6\).

## originality

PASS

The focal 2024 paper proves the automorphism semidirect decomposition and \(\omega\)-categoricity but does not state an exact oligomorphic profile. The older Apps paper studies \(\aleph_0\)-categorical finite extensions of Boolean powers through topological permutation systems, again without the submitted tuple-support count in the inspected material. Focused Resultary and web searches over Boolean powers, oligomorphic profiles, tuple orbits, and automorphism counts found no equivalent \(2^{q_k-r}\) theorem. A published SCOPE record with the numerical sequence \(2^{2^k-2}\) concerns a different random-distributive-lattice structure and only coincides with one specialization.

## value

PASS

The source's main qualitative conclusion is \(\omega\)-categoricity, whose quantitative refinement is precisely the oligomorphic tuple-orbit profile. The theorem gives that profile in closed form for every arity from the finite action \(G\curvearrowright A^k\), plus injective and asymptotic consequences. This is a natural structural classification of a canonical family rather than an arbitrary count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
