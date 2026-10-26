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

# Analytic verification

The source's exact Lemma 4 and uniform GRH character bound (equation (2), Section 4) were compared to the proof here. The potentially delicate \(p\mid k\) terms are all below any cutoff \(X\ge k\), so no excluded prime appears in the nonprincipal-character tail. Averaging the tail over nonprincipal characters yields the claimed uniform bound without a spurious factor of \(\varphi(k)\).

For \(X=k^{2+\delta}\), the tail relative to the target scale satisfies
\[
\frac{\varphi(k)}{\log k}\frac{\log^2(kX)}{\sqrt X}\ll\frac{\log k}{k^{\delta/2}}\to0.
\]
Mertens gives \(Z(X)/(e^\gamma\log k)\to2+\delta\). For primes \(r\le c\varphi(k)\), the uniform minimum of \(W(r)\) occurs asymptotically at the upper edge since \(\log r/r\) eventually decreases; the finitely many small primes have fixed positive weights. The limit inferior lower bound therefore is at least \(1/c-(2+\delta)\) for every \(\delta>0\), hence at least \(1/c-2\).

The prime number theorem converts the inclusion of prime classes into \(N_+(k)\ge(c+o(1))\varphi(k)/\log k\); the source's Theorem 5 supplies only the corresponding upper bound. These are complete asymptotic proofs, not computer-assisted certificates. No finite experiment is offered as proof of GRH or of an infinite statement. Independent validation has not been performed.
