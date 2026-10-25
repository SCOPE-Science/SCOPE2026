---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The exact Ehrenfest transition-row generating polynomial is A(z)^i B(z)^(n−i) with p=(1−a)/2,q=(1+a)/2; summing rows gives [B(z)^(n+1)−A(z)^(n+1)]/[a(1−z)]. The binomial likelihood ratio switches only once, so unique central column maximizes unweighted ℓ1. Differentiating the central binomial tail gives c_n/a integral_0^a(1−s²)^m ds, increasing from1 to c_n. Quotient Boolean-cube row absolute-derivative sums imply exact infinity norm 2 n a P(Bin(n−1,p)=floor np); local binomial CLT, uniform small/large time bound imply (γ+o(1))sqrt n. At a=n^(−1/2), t=(log n)/4, central-column derivative C_m′(t)/sqrt n->4β, hence M1>=(β+o(1))sqrt n log n. Individually checked 15 finite Q-matrix examples; no matching upper asymptotic of M1 is claimed.

## originality

PASS

Classical Krawtchouk diagonalization and reversible binomial stationarity do not determine unweighted counting-column norms or time-weighted endpoint derivative separation. Generic Markov-column-sum papers are not an exact Ehrenfest-ℓ1 radius theorem. Searches found no covering normalized logarithmic endpoint bound; older Ehrenfest literature may have equivalent expressions.

## value

PASS

Counting ℓ1 and ℓ∞ endpoint derivatives differ despite reversible Ehrenfest dynamics, with a sharp logarithmic lower order and explicit constants. The contrast isolates lumping/coordinate-counting geometry as a mathematically meaningful source of norm amplification; this is not the spectral eigenvalue calculation itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
