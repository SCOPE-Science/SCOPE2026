---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Integrated the exact endpoint kernel: with r=a/b,s=c/b,w=(z/b)^2, the numerator is Aw^2+Bw+C, A=1-r+s, B=(1-r)(r-s^2)-s(r^2+1), C=rs(r-(1-r)s)>0. Its discriminant factors as -(1-r)(r-s)(1+s)Q_r(s), Q_r(s)=(1-r)s^2+(r^2+6r+1)s-r(1-r). Q increases strictly with a single root in (0,r); B>0 on the nonnegative-discriminant branch. The pole locations cannot cancel. Mapping the two w-roots by square roots proves the complete upper-plane classification, holomorphic multiplicities, and square-root opening. Independent SymPy checks confirmed rational identity, discriminant, two-interval polynomial and exact (r,s)=(2/5,1/15) collision and prefactor squared 91/100. One/two bands permit zero/one upper zeros respectively. This is an algebraic all-parameter proof, not a numerical extrapolation.

## originality

PASS

The available primary wavelet papers give the holomorphic Cauchy-wavelet setting and behavior of phase retrieval near zeros, but do not supply this exact three-uniform-band discriminant or minimal component collision classification. Resultary semantic searches returned no statement dominating the submitted phase diagram. The priority judgment is best-of-knowledge, conditional on unindexed rational Cauchy-transform literature.

## value

PASS

Zeros and their coalescence control analytic-wavelet phase singularities. The smallest possible number of equal-height bands producing an upper-plane double zero and a sharp dimensionless parameter frontier is a motivated global classification, beyond a single numerical example; it is not a claim of phase-reconstruction robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
