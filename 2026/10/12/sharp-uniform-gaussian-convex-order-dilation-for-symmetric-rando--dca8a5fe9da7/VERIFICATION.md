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

## Analytical requirements
The finding uses classical characterization of convex order by upper integrated quantiles, strict concavity of the Gaussian profile, and preservation of convex order under convolution of independent random variables. Finite support reduces each base law to at most three positive cut points. The proof enumerates all such points and gives strict rational certificates at all noncentral cuts. Every larger integer size is a sum of allowed block sizes, which supplies the infinite extension without extrapolation from computations.

## Reproducible check
Run `python verification/checker.py` using a standard Python 3 installation. The script computes a rational enclosure for \(\pi\) from Machin's arctangent identity and verifies a rational enclosure for \(\sqrt{2\pi}\); it then uses finite Taylor inequalities for \(\int_0^z e^{-t^2/2}\,dt\) and \(e^{-z^2/2}\) to certify every normal-quantile comparison. It checks \(c_3\) bracketing, the strict inequality \(c_3<c_2\), and all finite binomial telescoping identities in sizes two through five. The script terminates with the message `PASS: pi, Gaussian quantile brackets, 2/3/4/5-step tail cuts, c2>c3, combinatorial identities`.

## Scope and limits
The checker certifies explicit finite inequalities, not originality, broader mathematical significance, or any result outside the stated iid equal-weight symmetric-sign class. Neither independent validation nor independent audit has been performed.
