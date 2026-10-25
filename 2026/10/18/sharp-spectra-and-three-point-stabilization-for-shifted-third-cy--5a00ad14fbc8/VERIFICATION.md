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

Using F(n+d)-F(n)=d(2n+d+1) and 4F(n)=(2n+1)^2+3, prime powers split into p|d with p≡1 mod3 (two Hensel-simple roots), p|(d²+3) with p>=5 (one affine root), and p=3 ramified valuation one iff n≡1 mod3 and 3|d. p=2 absent. A third shifted value forces p|d, giving G_{d,r}=gcd(F(n),d) for all r>=3. Independent congruence tests covered 24000 (d,n) instances; exact local residue counts, CRT product weights and root-translation invariance prove all divisor frequencies, maximum T and least period T. Mathematical proof covers all d,n>=1 and r>=2 beyond sampled finite checks.

## originality

PASS

Bodin--Drouin general polynomial-pair gcd resultant theory implies periodicity, root local factors and often maximal valuation bounds, but their main results do not themselves give the explicit A_d/B_d/E_d cyclotomic family, all-window three-point stabilization, sharp period and full frequencies. Earlier Drouin thesis/preprint was identified but complete text not obtained, retained as priority risk. General identities (Hensel, CRT, resultant) are duly prior.

## value

PASS

A natural explicit arithmetic-progression gcd classification for Phi3, with sharp least periods, full divisor spectra and densities, and an exact finite-length stabilization phenomenon; useful concrete arithmetic invariant not merely a rename of generic resultant bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
