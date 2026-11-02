---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS: For p=2q+1 with q odd prime, all nonzero quadratic nonresidues are primitive except the order-two element −1; the exact indicator (1−χ(x))/2−1_{x=−1} gives 2S=Σ_{x≠0}χ(Q(x))−T−2χ(Q(−1)). Standard separable quadratic character sum equals −χ(a), including linear a=0 via χ(0)=0; subtract χ(c), giving S and N± from primitive root count (p−3)/2. When ac≠0, E:y²=xQ(x) is nonsingular elliptic and contains rational 2-torsion (0,0), so even integer trace obeys |T|≤2 floor sqrt(p) by Hasse. For ac=0, a simple quadratic-character sum gives T=−χ(b). Therefore |S|≤floor sqrt p+2 and Nε≥(p−11−2floor sqrt p)/4>0 for p≥23. Finite exact independently enumerated normalized polynomials p23,p47 and witnesses, plus p7,p11. The p5 q-even case is explicitly excluded from exact formula but included as small-prime obstruction; no extrapolation from the finite cases.

## originality

PASS

Qualified best-of-knowledge statement-based originality after checking primary comparison and relevant published Resultary records; no uninspected full text asserted not covering. If both Q and −Q have primitive value at a primitive input then two-sign existence follows for safe p≡3 mod4, so prior work covers that component for genuine quadratics outside listed exceptions. The exact signed counts, uniform sharp envelope and inclusion of all safe p≥23 remain additional and are the basis for originality PASS.

## value

PASS

PASS: Primitive-root signs of separable quadratic evaluations are a natural arithmetic distribution invariant and explicitly posed by Sun. The result obtains a uniform sharp-at-examples discrepancy, complete safe-prime existence threshold, and exact signed counts in terms of elliptic trace. It goes beyond previously covered sufficiently-large genuine-quadratic existence and treats eligible linear and p=23 boundary cases; standard Hasse machinery is acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
