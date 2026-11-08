---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For K_{p,q} with p<=q, N>=3 and s=ch, the Laplacian spectrum is 0,q (p−1),p (q−1),N. Exact projectors give diagonal F_A=1/N+(p−1)r(qs)/p+q*r(Ns)/(pN), and G_B analogously. Differentiation verifies r'<0 and φ(z)=(1−r(z))/z has φ'<0 for z>0: within-class off-diagonal entries are positive differences φ(ps)−φ(Ns) or φ(qs)−φ(Ns), cross-class entry (1−r(Ns))/N>0. Both diagonal functions strictly decrease 1 to 2/N−1 and G_B>=F_A (strict when p<q), yielding a unique cutoff from F_A=0. K_{1,1} has all entries strictly positive for finite s>0. For t=qs, F_A(t/q)−r(t) is O(1/q) uniformly for 1<=p<=q on each compact t-set; r has one simple positive zero z0≈4.644370709, so qs*=z0+O(1/q). Independently differentiated scalar identities and compared full rational Laplacian matrices in small bicliques; no extrapolation from finite tests for universal cutoff.

## originality

PASS

Best-of-knowledge PASS for the sharp [3/3] endpoint positivity horizon on every uniform biclique, all-positive off-diagonals and uniform star-to-balanced scaling. Zappavigna et al 2010/2012 study broad sufficient positivity criteria, not exact necessary biclique cutoffs. Local published [2/2] Padé and Crank–Nicolson results concern different stability rational functions. Wade 2004/2005 entire paper was inaccessible (abstract examined, Oxford VPN disconnected), so potential relevant overlap remains a named risk, not a fabricated negative comparison.

## value

PASS

Entrywise positive graph diffusion time steppers require a usable maximum step; the proved exact sharp cutoff is stronger than generic sufficient stability bounds and remains uniform over all class proportions, including stars. Off-diagonal positivity at all steps and one specific diagonal obstruction identify a meaningful structural phase boundary for a standard sixth-order integration scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
