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

The universal proof was checked symbolically at its critical steps: balanced equality forces the support size \(2(p-1)\); rationality gives cyclotomic Galois invariance of Fourier support; the principal character is excluded by the \(p-1\) divisibility of nonzero scalar orbits; and the remaining Fourier support consists of exactly two punctured dual lines. Fourier inversion then reduces the claim to the sharp multiplicity lemma for a sum of two one-variable functions.

The bundled `verify.py` supplies independent finite consistency checks. It enumerates all integer value-multiplicity partitions for \(p\in\{3,5,7,11\}\) and confirms that the bound
\[
\#\{U+V=0\}\le(p-1)^2+1
\]
has the unique equality multiplicity pattern \((p-1,1)\) on both sides. It also exhausts all \(3^9-1\) nonzero functions from \(\mathbb F_3^2\) to \(\{-1,0,1\}\), computes Fourier support exactly in \(\mathbb Q(\zeta_3)\), and verifies that the balanced equality functions are exactly the \(108\) signed differences of nonparallel affine-line indicators.

The verifier prints `VERIFY_OK`. These finite computations are replay checks only; no finite enumeration is used as proof for arbitrary primes.
