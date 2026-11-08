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

The oriented complete-graph edge incidence columns e_i-e_j give B B^T=nI-J and Gram=(1-2w)I+wB^T B for odd normalized Gegenbauer kernel w=P_{n,l}(1/2). Thus the incidence projector has eigenvalue 1+(n-2)w of multiplicity n-1 and its orthogonal complement has 1-2w of multiplicity (n-1)(n-2)/2. Independently computed normalized Gegenbauer recurrence symbolically, verifying w3=(n-11)/(8(n-2)) and w5=(n-5)(n-27)/(32n(n-2)); the resulting positive eigenvalues and rank yield interpolation, sharp condition number and three integer vanishing pairs. In ambient dimension four (n=5), Chebyshev U_l gives P_l(1/2)=sin((l+1)pi/3)/((l+1)sin(pi/3)); even l disallowed by nonzero P_l(0), so exactly l congruent 5 mod 6 is fully orthogonal. Independent exact checks at n=4,5,11,27,50 corroborate, but all-n proof is spectral factorization.

## originality

PASS

Delsarte-Goethals-Seidel 1977 and Zhu et al. 2015 supply the general Gegenbauer addition and design machinery. The A4 all-degree l=5 mod 6 law is also present in a previously audited related A4 sampling result and is NOT treated as wholly new. The surviving contribution here is the variable-n cubic/quintic two-eigenvalue spectra, sharp interpolation, and exceptional n=11 and n=27 resonances. Search did not establish that older Johnson-scheme sources lack these computations: Delsarte full text was inaccessible and authorized Oxford returned vpn_disconnected.

## value

PASS

The full rank/conditioning and arithmetic orthogonality classification tell when exact-degree harmonic interpolation on a canonical root/edge geometry is perfectly conditioned without inversion. The resonances 55 cubic kernel sections at n=11 and 351 quintic at n=27 are natural exact spectral phenomena, rather than an arbitrary sampled number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
