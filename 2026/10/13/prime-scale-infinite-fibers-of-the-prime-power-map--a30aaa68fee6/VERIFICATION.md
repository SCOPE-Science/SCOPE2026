---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Fix y≥1 and pairwise distinct primes r_j,s_j>y for 1≤j≤y. CRT gives a unique reduced class a mod M=product r_js_j with a≡−j mod r_js_j. Every prime q≡a (mod M) gives q+j divisible by distinct primes r_j,s_j for all j, so no q+1,…,q+y is a prime power. q itself is prime, hence the largest prime power ≤q+y is q and the defining non-prime-power branch yields P(q+y)=y. Dirichlet ensures infinitely many q; the PNT in fixed reduced residue class proves liminf F_y(X)log X/X≥1/phi(M). Checked no use of only finite experiments to obtain the universal asymptotic and independently reconstructed explicit small-y CRT examples.

## originality

PASS

Best-of-knowledge PASS for every-fiber infinite preimages with quantitative prime-scale lower bound. Steven–Hoseana define the map and analyze forward orbits and a special minimal preimage relation, not arbitrary inverse fibers or positive asymptotic density at X/log X scale. The Chinese remainder theorem and PNT in AP are standard ingredients, not claimed as discoveries.

## value

PASS

A natural inverse-dynamical question for a studied number-theoretic map is answered completely for every target, with explicit prime-progression witnesses and quantitative lower bounds. This identifies infinite branching of each vertex while forward-orbit questions remain open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
