---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Only the symmetric part contributes to \(q(z)=\langle Bz,z\rangle\). If \(q\) vanishes at a nonzero vector, the denominator vanishes on a nonzero pair; if \(q\) takes both signs, positive rescaling of two vectors makes the two quadratic values cancel. Conversely, a strictly positive or strictly negative quadratic form makes every nonzero-pair denominator one-signed. A coercive estimate \(|q(z)|\ge\beta\|z\|^2\) gives the uniform quotient bound, while strict positivity without coercivity is insufficient: on \(\ell^2\), \(B e_n=n^{-1}e_n\) gives unit vectors with denominator tending to zero. The actual primary source was checked: Theorem 2.1 and Theorem 2.3 literally assume only that \(B\) is bounded while dividing by the displayed quadratic denominator, and the Holling-IV application prints \(BY=(1-\mu(x))Y\) for merely \(\mu\in L^\infty\), so \(\mu\equiv1\) makes \(B=0\).

## originality

PASS

The primary paper itself is the decisive comparison: its main stabilization theorems print only boundedness of \(B\), and a concrete advertised Holling-IV specialization permits a zero operator. Searches for the paper title, DOI, feedback quotient and later corrections found no published erratum or theorem adding the missing one-sign/coercivity condition. The audited result is not merely a counterexample: it gives the exact well-definedness classification and separates strict one-sign from the stronger coercivity needed for uniform boundedness.

## value

PASS

This is a substantive correctness boundary for a published stabilization theorem, not a cosmetic type check: the literal theorem may prescribe an undefined control, and a named application family contains the zero-operator case. The exact one-sign/coercivity distinction supplies a usable repair criterion for future proofs and applications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
