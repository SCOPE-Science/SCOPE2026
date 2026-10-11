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

The decomposition is correct and supplies the required infinite proof. Writing an exponential-perfect integer uniquely as \(n=cm\), with \(c\) the product of prime powers having exponent at least two and \(m\) its coprime squarefree part, multiplicativity and \(\sigma^{(e)}(m)=m\) show that \(n\) is exponential-perfect exactly when \(c\) is. Hagis's primary paper uses this same powerful-core decomposition and records the prior finiteness theorem for powerful exponential-perfect numbers with fewer than any prescribed number of prime factors. The later handbook explicitly records the prior classification that \(36\) is the only exponential-perfect integer with two distinct prime factors. For fixed \(r\), summing Landau's fixed-\(k\) squarefree almost-prime asymptotic over the finitely many cores shows that the unique two-prime core \(36\) contributes \(X(\log\log X)^{r-3}/(36(r-3)!\log X)\), while every core with at least three prime factors loses at least one power of \(\log\log X\), or contributes only \(O(1)\) when \(r=3\). A fresh independent enumeration through \(20{,}000\) found \(175\) exponential-perfect integers and exactly \(36\) in the two-prime layer. This finite check is corroborative only.

## originality

PASS

Hagis proves a global positive-density result by summing squarefree multiples of powerful exponential-perfect cores, and explicitly relies on the finiteness of cores with bounded prime support. The two-prime classification \(36\) is also prior. Neither inspected source refines the global count by a fixed value of \(\omega(n)\), identifies the unique \(36\)-core as the dominant contribution in every fixed layer, or states the consecutive-layer ratio. Current Resultary searches returned the assigned theorem as the exact same-object hit and no earlier fixed-\(\omega\) result. The claim therefore survives best-of-knowledge originality as a natural stratified refinement of the prior decomposition rather than a special case of Hagis's global density theorem.

## value

PASS

Prime-factor layers are a natural refinement of a multiplicative counting problem, and the theorem identifies a sharp hierarchy in which one primitive core controls every fixed layer. The explicit main term and consecutive-layer ratio add structural information not visible in the global density. This is a motivated asymptotic classification rather than a finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
