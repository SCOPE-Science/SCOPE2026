---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The incidence matrix N of a balanced generalized quadrangle satisfies NNᵀ=(q+1)I+A with strongly regular collinearity eigenvalues q(q+1),q−1,−(q+1). The full point/line powered-distance block matrix reduces on the zero-sum subspace to a constant bipartition branch Fq(p), paired L±=(q−1)2^p−q4^p±sqrt(2q)(3^p−1), and null-incidence L0=q4^p−(q+1)2^p. Substituting x=2^p and γ=log_2 3 yields Fsecond(x)>0,Fprime(1)>0 and a unique crossing inside 0<p<log_2(1+1/q). On that interval direct bounds give L0<0 and L±<0, so exactly one centered sector becomes null, giving 2(q+1)(q²+1)−2 embedding dimension. Taylor at p=0, F(0)=−1, F’(0)=q³log(4/3)+O(q²) proves αq∼1/[q³log(4/3)]. I independently computed the spectral formula and noncontrolling-sector signs for q=2,3,5,9,20; the unrestricted result follows from the symbolic inequalities, not those spot checks. Repair: the original RESULT.md had the false exact identity Fq_prime(0)=q³log(4/3)−q(q+1)log(3/2). The corrected full RESULT.md now has Fq_prime(0)=q³log(4/3)−q²log(3/2)+qlog2, exactly equal to differentiating the displayed Fq(p); the q³ leading term and stated O(q^-4) root asymptotic were separately rechecked. This is an actual corrected scientific source byte replacement, not a disclaimer.

## originality

PASS

Sánchez supplies the determinant test for any finite metric and computes complete bipartite path metrics, not the all-orders generalized quadrangle formula. Exoo–Jajcay and Abreu et al classify geometric incidence graph parameters and girth constructions, not a Schoenberg metric exponent. A projective-plane incidence graph is girth six/diameter three; a generalized hexagon has six shells, so neither is a direct dominating special case. Bounded Resultary and targeted web searches found no exact GQ formula/table, with residual association-scheme priority risk.

## value

PASS

The canonical generalized quadrangle incidence metric has a natural exact negative-type/Hilbert embedding threshold uniform in the incidence geometry and depending only on q, including an endpoint dimension drop and q^-3 law. This is a useful structural classification, not merely a single small finite graph test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
