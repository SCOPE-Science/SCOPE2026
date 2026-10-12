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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 and its standard library. The program constructs the prescribed codewords without external optimization software and independently enumerates the deletion outputs \(\{(c,d),(a,d),(a,b)\}\) for every codeword. It checks the exact size \(\lceil mn/3\rceil\), correct coordinate alphabets, distinctness of codewords, that every selected word has three distinct received pairs, and complete coverage of every pair in \(X\times Y\). The actual execution tested every \((m,n)\) with \(2\le m,n\le50\), or 2401 parameter pairs, and printed `VERIFY_OK 2401 rectangular parameter pairs`.

A second finite optimization check, independent of this code-construction implementation, formulated the small rectangular covers as binary set-cover integer programs. Completed solves for the base rectangles gave the cardinalities \(2,2,3,3,6\) at sizes \((2,2),(2,3),(2,4),(3,3),(4,4)\), respectively; explicit cover words from these solves appear in `verify.py`. These numerical solves are not used as upper-bound proofs: the elementary three-output lower bound already supplies global optimality whenever the constructed code covers.

The unrestricted theorem follows from the finite bases and symbolic induction adding three rows or columns, not from testing finitely many alphabet sizes. The procedure assumes both alphabets have at least two symbols. No independent audit or human certification is asserted.
