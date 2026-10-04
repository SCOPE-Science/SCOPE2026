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

The claim reduces to three independently checkable ingredients.

First, Malikiosis's Corollary 5.2 applies to the vector \(\eta_N(j)=e^{-j^2}\) because it is the specialization \(z_j=\xi^{j^2}\) with the transcendental parameter \(\xi=e^{-1}\). This establishes full spark for every finite cyclic dimension.

Second, for the ambiguity function, reducing \(j-k\) to \(r_k(j)\in\{0,\ldots,N-1\}\) gives the exact exponent \(s_k(j)=j^2+r_k(j)^2\). On the branches \(j\ge k\) and \(j<k\), these exponents are strictly increasing and have minima \(k^2\) and \((N-k)^2\), respectively. In odd dimensions the minima cannot tie. The remaining weights, relative to the unique leading weight, sum to less than
\[
\frac{e^{-2}+e^{-3}}{1-e^{-6}}<\frac15,
\]
so every ambiguity value is bounded below in modulus by \(\frac45e^{-m_k}\), hence by \(\frac45e^{-(N-1)^2/4}\).

Third, in even dimension and at the half-period shift \(k=N/2\), indices \(j\) and \(j+N/2\) have identical positive ambiguity weights, while their modulation factors differ by \((-1)^\ell\). They therefore cancel pairwise for every odd \(\ell\).

Bojarovska--Flinth Theorem 2.2 converts zero-free ambiguity into phase retrieval for the full finite Gabor measurement set. No computation is required for the proof, and no finite test is used to infer the all-dimension statement.
