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

The bundled `verify.py` is dependency-free and uses exact integer/rational polynomial arithmetic.

It checks the following parts of the new argument:

1. From the displayed five-by-three Cox differential matrix, the selected maximal minors are exactly
\[
-4t^2(3s^4+t^4),\qquad
-4s(s-t)^2(s^3-st^2-2t^3),\qquad
4st^2(2s-t).
\]
These identities support the exhaustive global rank-three argument. No finite sample is used to infer unramifiedness.

2. Substituting \(t=2s\) into the first minor gives \(-304s^6\), the contradiction needed in the \(st\ne0\) branch.

3. The source's reduced two-by-two quotient matrix
\[
4\begin{pmatrix}0&4\varepsilon-1\\ \varepsilon&-2\end{pmatrix}
\]
has determinant \(16\varepsilon(1-4\varepsilon)\). Multiplying by the source's nonzero complementary minor \(256\) gives \(4096\varepsilon(1-4\varepsilon)\).

4. The quotient matrix has rank one at \(\varepsilon=0\) and \(\varepsilon=1/4\), and rank two otherwise. Together with complementary rank \(14\), this gives full-matrix ranks \(15\) and \(16\), respectively.

5. For a rank-two degree-\(12\) split bundle \(\mathcal O(a)\oplus\mathcal O(12-a)\) with \(a\le6\), the equality \(h^0(N(-7))=1\) forces \(a=5\).

The checker imports no conclusion about the geometric parameter space. The Cox rank criterion, the relative cohomology construction, and the fact that its determinant defines the first jump divisor on the unramified locus are cited from arXiv:2609.39309v1.

Limit: the verification and theorem are characteristic zero. The source itself treats other characteristics separately.
