---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The rowwise two-point Hadamard transform separates the all-zero-character columns into the plus channel and sends the second frequency column at each \(t\) to exactly one exceptional plus row and otherwise to the minus channel. This gives the block operator \(\mathcal T=\begin{pmatrix}I&K\\0&I-K\end{pmatrix}\) with \(\|K\|^2=(p+1)/(2p)\le2/3\). Since \(\|K\|<1\), the inverse exists, and the stated norm bounds give squared condition number at most \((380+152\sqrt6)/3\approx250.774<251\). The actual verifier was inspected; it checks the channel assignment and exact endpoint arithmetic on representative odd primes, while the proof of the uniform theorem is analytic.

## originality

PASS

The closest primary source introduces this exact family, proves that its fibers admit no simultaneous exponential basis, and explicitly says it is unknown whether the Riesz ratio stays bounded independently of \(p\). The audited construction answers that stated question with a concrete uniform bound; no stronger covering theorem or later exact-family result was found.

## value

PASS

The result directly resolves a concrete obstruction family singled out in the defining paper and shows that the simultaneous-fiber-basis condition is not necessary for uniformly bounded Riesz behavior. An explicit universal constant is a natural quantitative answer, even though it is not optimized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
