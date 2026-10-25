---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The theorem explicitly fixes complex Taft T_n, n>=2, ζ=exp(2πi/n), Δx=x⊗1+g⊗x and PBW basis x^r g^b as ORTHONORMAL (singular values depend on this choice). Quantum binomial expansion gives Ψ2(x^r g^b)=∑_{j=0}^r c_{r,j} ζ^{j(j+b)} x^r g^{2b+j} for c recurrence c_{r,j}=c_{r−1,j}+ζ^{r−j}c_{r−1,j−1}. Its r-block matrix is unitary-conjugate via Fourier and two quadratic diagonal unitary factors to a scaled cyclic Hankel matrix K_r(a+b), K_r(c)=ζ^{c²}∑_j c_{r,j}ζ^{j(j+c)}. Fourier basis vectors are permuted with weights Λ_r,k, proving complete SV multiset |Λ_r,k|/sqrt n including zero multiplicities. For r0, the doubling map yields odd n unitary or even sqrt2/zero each n/2. For r1, even n orthogonal two-supported columns yield sqrt2 everywhere; odd n weighted cyclic shift yields |1+ζ^k| and condition csc(π/(2n)). Independently built EVERY PBW block using the claimed coproduct and quantum recurrence for n=2..10, and used direct numpy singular-value decompositions compared to independent DFT of K_r; max discrepancy below 4e-14 over every r, including odd/even first layers. Finite matrices corroborate the all-n algebraic factorization, not replace it.

## originality

PASS

Best-of-knowledge primary-statement comparison plus actual Resultary query, checked exact and broader implications, and explicit residual source-access risk. The novelty is the substantive stated result, not a theorem inferred merely from negative search.

## value

PASS

On a canonical finite-dimensional nonsemisimple Hopf family, metric-dependent singular values of a natural Sweedler power quantify rank and conditioning rather than only trace or eigenvalue. One all-dimension Fourier–Hankel reduction and a sharp even/odd first-radical-layer conditioning dichotomy with asymptotic n growth give a substantive exact structural invariant in the explicitly declared PBW metric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
