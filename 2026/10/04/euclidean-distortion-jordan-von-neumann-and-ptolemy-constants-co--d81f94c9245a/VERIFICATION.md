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

The following checks were replayed from the displayed definitions.

1. The normalized Lorentz norm satisfies
\[
N_a(x,y)^2=\max\{x^2+a y^2,\;a x^2+y^2\}
\]
for every \(a\in(0,1]\).

2. Averaging the two quadratic forms and using \(a\le1\) gives the sharp Euclidean sandwich
\[
\frac{1+a}{2}\|z\|_2^2\le N_a(z)^2\le\|z\|_2^2.
\]

3. For an arbitrary ellipse \(E_A\), the implication \(E_A\subseteq E_Q\Rightarrow Q\preceq A\) was checked through generalized Rayleigh quotients. Applying it to both Lorentz defining ellipses gives \(p,q\ge1\). The two points \((1,\pm1)/\sqrt{1+a}\) then force every admissible outer dilation to satisfy \(\lambda^2\ge2/(1+a)\).

4. The Jordan--von Neumann upper bound follows from the Euclidean parallelogram identity and the same norm sandwich. The pair \((1,\pm1)/\sqrt{1+a}\) attains it.

5. The Ptolemy upper bound follows from Euclidean Ptolemy and the product form of the sandwich. The triple \((1/2,1/2)\), \((1/2,-1/2)\), \((1,0)\) attains it.

No numerical experiment, finite enumeration, or inaccessible external lemma is required for correctness. Literature access limitations affect only originality coverage, not the proof.
