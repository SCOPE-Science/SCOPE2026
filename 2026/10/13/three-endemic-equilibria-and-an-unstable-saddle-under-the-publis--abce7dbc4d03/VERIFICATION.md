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

Wang–Wang–Teng's publisher PDF confirms model (1.1), Table 3's stated hypotheses, the separate uniqueness sentence before Theorem 2.1, and local asymptotic stability in Theorem 2.1(ii). The function h is smooth on I≥0, h(0)=0 and h'(0)=1; h(I) lies between I/4 and I, and h'≥1/9 follows from 8(1+I)^3−54I=2(2I−1)^2(I+4). Use N=S+V and W=S−V. Then W'=−(1+h/10)W, N'=96−(1+h/10)N and I'=Nh/10−3I. At I=0 the source formula gives R0=16/5. Eliminating N gives 96h/(10+h)−3I, exactly the stated rational function. Its three simple positive roots lie in (0,2), at 2, and in (2,21), respectively. Here S=V>0 and N+I=96−2I<96 so all three are inside the source's invariant region. At I=2, W=0, N=90, h=2/3 and h'=5/9. The (N,I) block has rows (−16/15,−5),(1/15,2), trace 14/15 and determinant −9/5, giving (7±sqrt(454))/15; the W eigenvalue is −16/15. Thus the middle point is a saddle. The source uses a derivative-to-ratio comparison which fails here, with its l̂33 equal to −2. The bundled checker was inspected only; it uses sp.N for some sign checks, but exact inequalities above justify those signs. This refutes the stated deterministic uniqueness and stability conclusions only.

## originality

PASS

The contribution is an exact counterexample to a particular published deterministic claim, satisfying the exact printed hypotheses and exposing the proof's sign gap. Multiple equilibria or middle-branch saddles in nonlinear models more generally are not claimed as new.

## value

PASS

The counterexample separates statements dependent only on the linearization at zero from nonlinear uniqueness and stability assertions. It corrects a concrete published theorem by verifying admissibility, multiplicity and instability exactly, rather than merely pointing out a possible gap in a proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
