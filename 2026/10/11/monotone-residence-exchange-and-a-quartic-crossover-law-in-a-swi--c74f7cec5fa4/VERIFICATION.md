---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The Hamiltonian V(x)=dplus*x^4/4 (x>=0), c|x|^3/3+dminus|x|^4/4 (x<0) is coercive with unique minimum, yielding periodic ovals for E>0. Exact side-time scaling gives P(0,dplus) and P(cE^-1/4,dminus). With inverse potential z_alpha(u), derivative of G_alpha=alpha z²+d z³ satisfies ∂_alpha G=alpha z²/[3(alpha+d z)]>0 for alpha>0, making P strictly decreasing. Beta integrals establish endpoint E^(1/12) and limit. Differentiated regularized root integral gives P_prime(0,d)=-sqrt2/(3d); therefore contrast crossing E* grows like Delta^-4 with displayed coefficient. Inspected independent quadrature code and algebra; finite sampled checks do not prove all energies.

## originality

PASS

Chen–Li–Yu source establishes center conditions and global periodic annuli for the switching model; available abstract does not state physical-time residence partition, all-energy monotonicity, or contrast asymptotics. Resultary semantic searches found related period problems but not an equivalent side-share theorem for the mixed cubic/quartic Hamiltonian. Full primary manuscript inaccessible; this remains priority risk.

## value

PASS

The physical-time residence fraction, rather than transformed-clock or total period, is a motivated orbit statistic of the asymmetric global center. Its exact monotonicity and unique equality criterion, together with a sharp singular fourth-power crossover, describe a natural transition between cubic and quartic restoring regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
