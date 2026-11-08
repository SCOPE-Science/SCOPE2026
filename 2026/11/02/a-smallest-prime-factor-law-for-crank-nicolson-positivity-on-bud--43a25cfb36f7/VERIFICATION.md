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

Set s=hB/(2|E|); then C=2(I+sL)^{-1}-I. Irreducible M-matrix inverse gives strictly positive off-diagonals, leaving diagonal crossing only. Complete multipartite Laplacian eigenprojectors yield R_a(s)=1/N+(N-a)/(aN(1+Ns))+(a-1)/(a(1+(N-a)s)). Independently verified R_a-1/2=[1+as-(N-2)(N-a)s²]/[2(1+Ns)(1+(N-a)s)], the strictly monotone class order R_a>R_b for a>b and positive root sigma_N(a). For integer partitions with minimum size a, edge count N(N-a)/2-delta. Continuous F(x)=N(x+D(x))/[4(N-2)] has derivative 0<F’<=sigma_N(x)/2; independently checked derivative identity d(D²/(2N-x)²)/dx=8x/(2N-x)^3 and key square difference. If a<=largest proper divisor d=N/p, monotonic F gives bound; if a>d the nonuniform edge deficit delta>=(a+1)/2 strictly defeats F(a)-F(d). Unique optimum p equal-sized parts of size d follows; the fixed-p asymptotic expansion is consistent. All-order conclusion is analytic, not finite census.

## originality

PASS

Qualified best-of-knowledge result is sharp fixed-total-edge-conductance complete-multipartite optimization and smallest-prime-factor equality classification. The general resolvent-return positivity criterion is prior and explicitly excluded from novelty; generic Laplacian spectra alone do not supply integer global optimum.

## value

PASS

A budgeted network design problem with a precise physical time-step objective naturally depends on integer topology. The theorem gives exact positivity radii for every complete multipartite graph and solves the nontrivial global topology optimization, including a number-theoretic smallest-prime-factor phase boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
