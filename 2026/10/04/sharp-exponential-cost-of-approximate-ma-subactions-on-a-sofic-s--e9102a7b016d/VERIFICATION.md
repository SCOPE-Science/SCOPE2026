---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The defining source was checked for the exact shift, potential, symbolic metric, maximizing value, and zero-slack obstruction. The proof was then reconstructed from those definitions.

For the lower bound, summing \(f+\phi-\phi\circ\sigma\le\varepsilon\) along \(a^n b a^\infty\) gives
\[
1+\phi(a^n b a^\infty)-\phi(a^\infty)\le(n+1)\varepsilon.
\]
The two endpoints are at distance \(\alpha^n\), which yields the displayed lower bound on the Lipschitz seminorm.

For the upper bound, every prefix has alternating \(b\) and \(c\), so \(-1\le S_kf\le1\). With \(N=\lceil1/\varepsilon\rceil\), the function
\[
u_N=\max_{0\le k<N}S_k(f-\varepsilon)
\]
satisfies \((f-\varepsilon)+u_N\circ\sigma-u_N\le0\). Thus \(\phi=-u_N\) is an admissible approximate subaction. Each \(S_kf\) is constant on length-\(k\) cylinders with range contained in \(\{-1,0,1\}\), giving \(|u_N|_{\mathrm{Lip},\alpha}\le2\alpha^{-N}\).

The lower choice \(n=\lfloor1/\varepsilon\rfloor-2\) and the upper choice \(N=\lceil1/\varepsilon\rceil\) squeeze \(\varepsilon\log\Lambda_\alpha(\varepsilon)\) to \(\log(1/\alpha)\).

No numerical calculation is needed. The verification does not determine the exact finite-slack minimizer or multiplicative asymptotic constant, and it does not generalize the result beyond the stated sofic example.
