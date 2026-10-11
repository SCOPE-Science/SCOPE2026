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

For the saturated scalar CPT, Theorem 2 reduces \(O^*\) to the Euclidean distance from one cyclic shift to the affine hull of the others. Fourier diagonalization of the circulant orbit gives \((O^*)^2=n/\sum_{k=1}^{n-1}|\widehat x_k|^{-2}\) when all non-DC Fourier coefficients are nonzero, while any non-DC zero supplies an affine dependence and forces zero distance. For two ones at separation \(d\), \(|\widehat x_k|^2=4\cos^2(\pi kd/n)\). Writing \(N=n/\gcd(n,d)\), even \(N\) creates a zero; for odd \(N\), residue multiplicities and \(\sum_{r=0}^{N-1}\sec^2(\pi r/N)=N^2\) give the exact denominator \((nN-1)/4\). Independent least-squares calculations for \(n=20\) reproduced exactly the four positive separations and \(\sqrt{80/99}\), with error below \(3\times10^{-14}\).

## originality

PASS

The complete Lei--Bickel source defines \(O^*\), proves the general residual representation, emphasizes its row-order dependence and formulates row pre-ordering as a nonlinear traveling-salesman problem for which it uses heuristics. It does not derive the circulant Fourier altitude identity or the two-active-row gcd/parity classification. Focused Resultary and web searches found no earlier exact arithmetic solution of this sparse binary CPT family.

## value

PASS

Exactly two active rows is a natural rare-binary-predictor design. The theorem completely solves the source-motivated row-order sensitivity in this family, exposes a qualitative power-of-two obstruction, and gives a concrete exact 5-percent saturated case. That is a motivated structural classification and benchmark, not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
