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
The proof has two global ingredients and one equality computation.

First, for every \(z=(s,t)\), each defining branch of \(N(z)\) is at most \(\|z\|_2\), hence \(N(z)\le\|z\|_2\).

Second, the unit ball has eight vertices with Euclidean squared norm
\[
1+(\sqrt2-1)^2=4-2\sqrt2.
\]
Convexity gives
\[
\|z\|_2\le\sqrt{4-2\sqrt2}\,N(z)
\]
for every \(z\). For \(N(x)=N(y)=1\), the Euclidean parallelogram identity then yields
\[
N(x+y)^2+N(x-y)^2\ge\frac4{4-2\sqrt2}.
\]
Dividing by \(4\) gives the claimed lower bound.

For \(x=(1,0)\) and \(y=(2^{-1/2},2^{-1/2})\), direct evaluation gives
\[
N(x+y)=1+2^{-1/2},\qquad N(x-y)=2^{-1/2},
\]
so the lower bound is attained exactly.

The bundled `verify.py` performs exact arithmetic in \(\mathbb Q(\sqrt2)\) for these identities and also verifies that the comparison extrema used in the closest published equality criterion occur at incompatible parameters. Its expected terminal output is `VERIFY_OK`.

The checker does not certify the literature search and does not replace the analytic proof of the global norm comparison.
