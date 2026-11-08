---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Partial-fraction Fourier transform of g gives, up to nonzero scale, h_lambda(t)=exp(-lambda|t|)(1-exp(-lambda|t|))^2; alternating p-periodization sums to rational R_u(L). Evenness/antiperiodicity pair compatible columns and rows of the cited fiber, reducing a singular even block to the specified 100x100 C(u). Independently implemented fixed 192-bit outward integer intervals and full Gaussian elimination on both exact rational u values: sign(det C(969/1000))=-1 with 99 negative pivots, sign(det C(31/32))=+1 with 100 negative pivots; no interval pivot met zero, worst certified width ~2.14e-50. Continuous rational matrix entries imply a real root between u=31/32 and 969/1000. Both map to beta>1 by the rational -log(1-t)>t+t^2/2 and pi<22/7. General Zibulski–Zeevi fiber singularity => non-frame is relied upon from the cited Ghosh work and not independently reproved in full; its full source remained inaccessible.

## originality

PASS

Ghosh reports a numerical second high-frequency branch at p=200 for the same window/density; a numerical indication does not imply the certified exact rational sign change. The published four-fifths obstruction p=4 is not equivalent to p=200. Belov–Kulikov–Lyubarskii prove frame regions for Herglotz classes but this sign-changing even rational window is not covered by an all-density frame theorem. Ghosh gives a symmetry-reduced criterion, not a published all-p proof, according to the accessible abstract and source summary. The nearest Resultary published certificate concerns density 4/5 (p=4) and a 3x3 determinant. The Ghosh numerical p<=200 scan is not an exact database/certificate that would imply this rigorously checked 100x100 case. The new finite sign certificate plus the prior fiber criterion logically implies a non-frame point; the prior numerical plot alone does not imply it. The theorem is an existence witness, not a classification of all beta values or all p.

## value

PASS

The same natural p/(p+1) density family and exact rational window already had a numerical high-frequency branch at p=200. Certifying the 100x100 determinant sign change makes this hard numerical obstruction a rigorous existence theorem at a nontrivial large index; the precise beta>1 case is mathematically motivated by the source conjecture, not an arbitrary matrix test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
