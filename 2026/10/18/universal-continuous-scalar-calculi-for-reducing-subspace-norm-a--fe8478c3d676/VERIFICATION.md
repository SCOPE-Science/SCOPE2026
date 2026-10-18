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

# Verification and reproducibility

The proof is analytic. Reconstruct the positive spectral criteria from [1, Theorem 2.2 and Corollary 2.17]; for a pure point operator verify directly that continuous \(f\) maps every eigenvector for \(A\) to an eigenvector for \(f(A)\). Check that strict increase/decrease of image eigenvalues forces the corresponding strict orientation of preimages when \(f\) is weakly monotone.

For the converse, choose any scalar crossing \(f(a)>f(b)\) with \(a<b\), fix \(\ell\in(f(b),f(a))\), and construct the first undercrossing and last overcrossing levels as in the proof. Directly verify \(x_n\downarrow c\), \(f(x_n)\uparrow\ell\) and \(y_n\uparrow d\), \(f(y_n)\downarrow\ell\), with every inequality strict and the respective extremal image value unattained. The reverse crossing \(f(a)<f(b)\) supplies the two exchanged-class failures. For nonstrict monotone \(f\), select any nondegenerate flat interval and exhibit one increasing and one decreasing diagonal ladder: both become scalar under \(f\) although their original extremal attainment fails in the appropriate orientation.

No auxiliary code, finite experiment, computer-assisted proof, external certification or numerical tolerance is required. Independent audit has not been performed; the 2023 related article's unavailable full material remains a publication-priority limitation.
