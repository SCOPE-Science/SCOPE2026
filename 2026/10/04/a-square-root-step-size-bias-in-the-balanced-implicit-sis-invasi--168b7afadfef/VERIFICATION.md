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
The exact disease-free BIM multiplier was reconstructed directly from the published SIS update and balancing weight for \(F_1\equiv0\) and \(F_2(S,I)=\sigma S/K\). The specialization obeys the source convergence condition because \(F_2/S=\sigma/K\).

The packaged `verify.py` checks the multiplier identity at representative values and replays the Gaussian-moment coefficient algebra giving \(a-\sigma^2/2\) at order \(h\), \(\sqrt{2/\pi}\,\sigma(2\sigma^2-a)\) at order \(h^{3/2}\), and the positive critical coefficient \((3/2)\sqrt{2/\pi}\,\sigma^3\).

The proof of the asymptotic remainder is analytic: fourth derivatives of the logarithms are dominated by an integrable polynomial in \(|Z|\) on a small uniform neighborhood. No finite numerical experiment is used to infer the infinite-time exponent. The claim is limited to the local disease-free transverse linearization and small positive step sizes.
