---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The regenerative proof closes the stated necessary-and-sufficient mean-square boundary. With normalized estimator \(y_k=g_k/\lambda\), a compressed step multiplies it by \(R=1-sZ\), where \(Z=(2/n)\sum_i\delta_i\), \(\mathbb E Z=1\), and \(\mathbb E Z^2=1+1/n\). Between full-gradient refreshes, the geometric-length series \(S\) satisfies \(S\overset d=1+BRS'\) with \(B\sim\mathrm{Bernoulli}(1/2)\). Its first two moment recursions give \(m=2/(1+s)\) and, after substitution into \(\psi_n(s)=\mathbb E(1-sS)^2\), \(\psi_n(s)-1=2s((n+2)s^2-ns-2n)/((1+s)(n+2ns-(n+1)s^2))\). Independent symbolic reconstruction reproduced this identity exactly. On the candidate stable interval the denominator and within-cycle second moment are finite, so refresh-epoch contraction plus the regenerative convolution gives all-time second-moment convergence. At or above the positive root, the refresh subsequence does not converge in mean square; when the cycle second moment itself ceases to be finite this only strengthens necessity. The positive root is exactly \(s_n=(n+\sqrt{9n^2+16n})/(2(n+2))\), with \(s_1=1\), strict increase to 2, and the stated expansion.

## originality

PASS

The defining MARINA paper was inspected at the algorithm, expected-density definition and the independent-compressor stepsize corollary. For scalar half dropout its density-matched choice is exactly \(p=1/2\), and its theorem yields the sufficient restriction \(s\le(1+n^{-1/2})^{-1}\); it does not give a necessary-and-sufficient scalar mean-square frontier. The later permutation-compressor paper broadens compressor structure and Hessian-variance analysis but does not supply this half-dropout regenerative boundary in the material inspected. Fresh Resultary searches for the same method, compressor, scalar quadratic and exact stability formula returned no equivalent published finding. The audited statement therefore survives implication-based comparison: it sharpens a sufficient theorem to an exact phase boundary on a natural benchmark rather than merely restating the source.

## value

PASS

The model is the smallest density-matched MARINA benchmark and the exact boundary answers a concrete stability question left hidden by a general sufficient theorem. The dependence on client count is structurally informative: independent averaging continuously recovers the uncompressed ceiling two while the generic theorem saturates at one. An exact necessary-and-sufficient benchmark of a standard distributed optimizer is a motivated reusable fact, not an arbitrary scalar exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
