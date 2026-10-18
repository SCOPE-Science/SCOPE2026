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

With n>4, Δ=sqrt(n(n-4)), R_n=((n-Δ)/2)H1+((n+Δ)/2)H2-E and gamma_q=qH1+H2-E, gamma_q²=-2(n-q). Under the explicitly assumed balanced reflection, intersection form H1.H2=1,E²=-2n gives s_gamma(R)=R+(R.gamma)/(n-q)gamma. Its scaled first and second coefficients are A_q=n(n+q²-4q)+(q²-n)Δ and B=n(n-3)+(n-1)Δ. Δ irrational for all integer n>4 by (n-2-Δ)(n-2+Δ)=4 parity argument. The determinant for rationality factors as 2n(q-n)(q-n+2). In range 1<=q<n, only q=n-2. When n even, gcd(n,n-2)=2, not a unit. Independent SymPy bilinear intersection calculation and symbolic factorization confirm these steps for arbitrary formal n,q,Δ. Neither nondegenerate dynamics nor balanced geometry is claimed proven for new q; the obstruction is conditional on their availability.

## originality

PASS

Malara–Merta–Szpond–Zieliński prove the odd-n family, a weight-independent symmetric de Jonquières action for units, and discuss the even-n problem explicitly. The unit q reflection rational-slope determinant and proof that it rules out all even-n unit weights within their precise template are absent from their inspected theorem and question. General Dionne–Roth even-point Seshadri reflections concern different orbit geometry and cannot settle this template-specific obstruction.

## value

PASS

The source explicitly motivates extending the irrational Seshadri examples to even n. Proving a structural no-go for the simplest weight-only extension, even under favorable assumptions about its hard geometry, rules out a real mathematical approach rather than reporting a cosmetic failed computation. It does not solve or foreclose the full even-n question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
