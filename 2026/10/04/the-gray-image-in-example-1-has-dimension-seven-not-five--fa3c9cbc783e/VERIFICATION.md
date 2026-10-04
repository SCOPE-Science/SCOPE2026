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
`artifacts/verify.py` uses only the Python standard library.

The verifier encodes \(\mathbb F_4=\{0,1,\omega,\omega^2\}\) as pairs over \(\mathbb F_2\), with \(\omega^2=\omega+1\). It reconstructs the five mixed-alphabet rows printed in Example 1 and implements the article's module multiplication and Gray map exactly.

The first three displayed rows contribute one binary degree of freedom each. Each of the final two rows contributes two binary degrees of freedom, using coefficients \(1\) and \(\omega\). The resulting binary generator has rank \(7\).

The verifier then enumerates the full coefficient space \(2^3\cdot4^2=128\), confirms \(128\) distinct mixed words and \(128\) distinct Gray images, and checks the complete binary weight distribution
\[
A_0=1,\quad A_4=12,\quad A_6=30,\quad A_8=63,\quad A_{10}=18,\quad A_{12}=4.
\]
Thus the reconstructed image has exact parameters \([15,7,4]_2\).

The external statement that optimal binary \([15,7]\) distance is \(5\) is a literature/database comparison and is not established by the verifier itself.
