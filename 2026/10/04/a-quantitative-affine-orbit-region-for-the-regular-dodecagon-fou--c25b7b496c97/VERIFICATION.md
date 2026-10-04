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

The argument was checked symbolically and against the full primary source.

Checks performed:

- Source hypothesis: arXiv:2609.10517v1 is primary MSC 52A40, first public on 9 September 2026, and Theorem 1.7 states that for the regular dodecagon the minimising directions are exactly the side-midpoint directions.
- Fourier covariance: for \(A\in SL(2,\mathbb{R})\), direct change of variables gives \(\widehat{\chi_{AP}}(\xi)=\widehat{\chi_P}(A^T\xi)\), hence \(\mathcal{N}(AP)=A^{-T}\mathcal{N}(P)\).
- Singular values: if \(s=\sigma_{\max}(A)\), then \(A^{-T}\) has singular values \(s\) and \(s^{-1}\) because \(\det A=1\).
- Angular covering: twelve midpoint directions give six unoriented lines separated by \(\pi/6\), so one lies within \(\pi/12\) of the minor singular axis.
- Exact norm bound: for angular distance \(\theta\), the squared norm is \(s^{-2}\cos^2\theta+s^2\sin^2\theta\), increasing in \(\theta\in[0,\pi/2]\) for \(s\ge1\).
- Exact cutoff: with \(q=s^2\) and \(\delta=\pi/12\),
  \[
  q\bigl(q\sin^2\delta+q^{-1}\cos^2\delta-1\bigr)
  =\sin^2\delta\,(q-1)(q-\cot^2\delta).
  \]
  Since \(\cot(\pi/12)=2+\sqrt3\), strict decrease holds exactly throughout \(1<s<2+\sqrt3\) for this witness inequality.
- Witness sharpness: placing the minor singular axis halfway between adjacent midpoint lines makes the nearest angular distance exactly \(\pi/12\), so the finite-witness bound itself is attained.

Unproved limits and risks:

- No claim is made that \(2+\sqrt3\) is the true affine-orbit threshold; it is the exact cutoff for the twelve-nearest-zero certificate.
- The behaviour for stronger anisotropy may depend on farther Fourier zeros of the source dodecagon.
- A prior equivalent affine-Fourier observation under different terminology cannot be completely excluded by targeted searches.
