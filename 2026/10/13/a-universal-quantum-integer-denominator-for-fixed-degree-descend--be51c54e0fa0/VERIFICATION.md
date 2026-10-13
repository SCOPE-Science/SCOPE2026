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
The proof was checked directly against Corollary 3.9 of arXiv:2502.17236v3, the vertex multiplicities in Definition 2.5, finiteness in Proposition 2.6 and Remark 2.7, and the coefficientwise identification in Theorem A.

The bundled `verify_denominator.py` enumerates ordinary integer partitions for all integers up to \(12\) and confirms that the maximum number of parts of size \(\ell\) is \(\lfloor p/\ell\rfloor\); it also checks additivity for several multi-index degree vectors. Its recorded output is `VERIFY_OK`.

The finite computation is not the proof of the universal claim. The universal denominator follows deductively from the partition constraint \(\sum_\ell \ell k_{\ell j}=p_j\). The root-of-unity statement is an upper bound only; cancellations are not excluded. No independent audit has been performed.
