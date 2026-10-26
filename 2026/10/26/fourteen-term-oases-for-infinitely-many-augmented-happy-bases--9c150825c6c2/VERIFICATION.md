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

The self-contained Python 3 program `verify.py` enumerates all three-digit defects for each even base through \(28\), returning exact maximal consecutive-run lengths \(2,6,5,8,8,8,8,8,8,9,11,9,11,14\) for the even bases \(2,4,\ldots,28\). The underlying published mirage reduction proves these finite maxima bound oasis lengths; the program verifies a positive run attaining the bound in every tested base.

The same program checks all fourteen explicit fixed-point digits at the first four Pell indices and confirms that the supplied norm-preserving affine recurrence maps one valid integer solution to another. Finite checks do not prove infinitude. The infinite proof is the exact norm identity, divisibility preservation, strict growth, and universal witness identities in `RESULT.md`.

Reproduce with `python verify.py` using only Python 3 standard library. The first base is \(28\) and its exhibited interval of augmenting constants is \([8686,8699]\). No external or independent audit has yet been performed.
