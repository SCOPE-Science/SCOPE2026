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

For homogeneous Rhaly action on Drury--Arveson H_d^2 and fixed coordinate j, output degree N maps z^alpha to z^(alpha+(N-m)e_j) with normalized squared entry |a_N|^2 binom(m,r)/binom(N,r), r=m-alpha_j. Counting r among d-1 other variables and applying two hockey-stick sums gives A1=N+1, A2=(N+1)H_(N+1), and A_d=(N+1)/(d-2)(binom(N+d-1,d-2)-1) for d>=3. Orthogonal output-degree rows prove exact Hilbert--Schmidt norm sum and iff convergence; monomial basis establishes converse. Asymptotics A1~N, A2~NlogN, A_d~N^(d-1)/[(d-2)(d-2)!] give claimed power/log endpoints; 2D harmonic identity sum H_k/k=1/2(H_K^2+H_K^(2)) proves 1/2(log K)^2. Independent exact matrix coefficient sums checked 72 (d,N) pairs; all-degree proof is the combinatorial identity, not finite tests.

## originality

PASS

Best-of-knowledge original multivariate homogeneous Rhaly Hilbert--Schmidt coefficient isometry and exceptional dimension-two harmonic factor. The one-variable Rhaly Schatten theory and Pilla several-variable Rhaly definitions overlap notation but available abstracts concern norm/boundedness and basic properties, not the claimed explicit coefficient weights or critical truncation coefficients. Pilla full text was unavailable despite arXiv/OA attempts and Oxford returned vpn_disconnected, a serious residual source risk.

## value

PASS

The exact coefficient-space isometry of a natural multivariate operator into S2, valid for all dimensions, yields a full sharp coefficient criterion and exposes a special d=2 logarithmic transition missed by general exponent counting. This is more than a single finite coefficient calculation and can serve as a precise boundary case for other operator ideals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
