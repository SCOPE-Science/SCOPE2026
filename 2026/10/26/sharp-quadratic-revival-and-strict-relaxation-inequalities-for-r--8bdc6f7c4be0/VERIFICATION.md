---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the stated normalization the central H commutes with every noise conjugation, the dissipative law stays diagonal, and measurement after coherent evolution convolves that law with the central probability Q_s. Central Fourier transforms are scalar with factors exp(-gamma*t*(1-r_lambda)) and kappa_lambda respectively. Counting-measure Plancherel gives the claimed 1/n! prefactor and nonnegative deficit. At finite t the classical factors are positive in every mode. Equality forces unit absolute value of every scalar transform of Q_s, including the trivial one, so Plancherel gives squared mass one. The resulting single atom is central and hence the identity for n>=3. Since the coherent operator is a convolution, its identity column being a phase times the identity basis vector forces scalarity. For the period the content gaps for n=3,4 have gcd 3,2; for n>=5 the three displayed partitions exist and have gaps n, 2(n-1), 3(n-1), of gcd one. Dividing the normalized denominator C by that gcd gives the least period in units of 2*pi. For the curvature, the transposition amplitudes at leading order are -i*delta/C and H^2(e,e)=1/C; real H makes each Q_delta(g) even. Thus Q_delta=delta_e+(delta^2/C)(mu_2-delta_e)+O(delta^4), giving exactly the stated K_n, positive because the standard mode has positive spectral gap. At t=0 the physical phase is zero; the fixed-t deficit function has the stated expansion in its formal phase variable. For bounded corroboration, independently assembled 6- and 24-dimensional matrices at gamma=0.7, t=0.8 (index (g,h) receives 1/C for each tau with g=tau*h) gave revival Frobenius errors below 1e-14 and positive deficits 0.193350989 and 0.263066558 at half the respective periods. At delta=0.004 the divided deficits were 0.168669855 and 0.098016012 versus analytic coefficients 0.168670687 and 0.098016258. Uploaded verify.py and its recorded PASS were inspected, not rerun; proof, not this bounded test, gives the all-n result.

## originality

PASS

The normalized model, convolution, spectral input, a recurrence upper bound and the quadratic expansion of the coherent law have prior coverage. The verified prior statements do not give the evaluated least-period gcd for all n with its exceptions, or the finite-time L2 equality set and positive local deficit at exactly those phases. The distinction between a common revival and the least scalar revival is substantive; the closest prior recurrence arithmetic overestimates the least period already for n=5. The exact joint classification, not general nonstrict convolution contraction, is the supported contribution.

## value

PASS

The normalized least period is a natural invariant with physically different scaling from a recurrence upper estimate. The measured-law equality result identifies exactly when coherent coupling makes no improvement in the specified squared distance, and the positive explicit curvature quantifies how strictness starts near those phases. Neither the equality set nor the rate coefficient is extracted from an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
