---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With both measures probability-normalized the Laurent basis diagonalizes restriction and yields squared multipliers r^(2j)/m_j. Strict log-convexity of the radial moments places the minimum at an endpoint; its two candidate curves have opposite strict monotonicities and cross in (a,b), since the moment ratio is a weighted mean of t^(4N). On either side, in the ratio to the minimal endpoint all nontrivial terms are strictly monotone towards the crossing, proving the condition optimum as well, including N=1. Writing L=log(b/a) and c=sqrt(ab), the spectrum at c is proportional to ((j+1)L)/sinh((j+1)L), with the removable center at j=-1. The optimal log-radius tends to log c, and the exponential tail still bounds every growing index uniformly; the isolated maximum at -1 therefore persists eventually. The product of endpoint moments gives the reciprocal squared minimum asymptotic ab(b/a)^N/[(b²-a²)N], and the limiting spectral maximum is (b²-a²)/(2ab L), giving the stated prefactor. Independent bounded replay: `cd /workspace && python audit_checks/check_frozen.py 4` uses independent log-radius quadrature and a Fourier-grid Gram spectrum on two bands, plus three fixed annuli at N=320 (peak -1 and condition/asymptotic ratios 0.999804, 0.998602, 0.996887). The general proof is not inferred from the numerical checks. Neither expert nor Lean verification is asserted.

## originality

PASS

Best-knowledge pass for the common unique optimum on a symmetric annular Laurent band and the sharp fixed-annulus asymptotic, not for the underlying diagonalization, moment convexity or generic endpoint-balancing method. The strongest indexed conditioning analogue found is a one-sided disk theorem, whose assumptions and sharp law differ.

## value

PASS

The radius solves two a priori different stability design criteria. Explicit exponential growth alone would not locate the best circle or give its true condition at finite cutoff; the prefactor and the isolated pole mode specify the leading stability loss. The fixed-annulus and complete angular data restrictions are essential; no assertion is made for collapsing annuli or arbitrary angular sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
