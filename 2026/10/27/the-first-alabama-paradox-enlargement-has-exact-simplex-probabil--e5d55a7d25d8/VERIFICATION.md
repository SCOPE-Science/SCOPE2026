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

# Reproducible verification
Run `python3 verify.py` from the supplied files using the Python 3 standard library only. The program executes exact Fraction arithmetic, validates the rational witness, verifies the two exact triangular areas \(1/1728\) and global normalized probability \(1/72\), and checks the iff chamber on all positive sorted rational population triples of total population at most \(180\) having strict apportionment cutoffs for house sizes \(1,2,3,4\). Observed: `PASS exact area=1/72, first witness, strict rational profiles= 153762 three-to-four losses= 1925`.

The proof is the abstract analytic shift argument, the strict quota/remainder characterization, and the exact simplex integration in RESULT.md. Exhaustive enumeration of a finite integer grid does not establish a continuum theorem, and ties are excluded rather than arbitrarily broken. The related geometric paper by Bradberry was not fully read, so originality remains subject to that explicit source-access risk.
