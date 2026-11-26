---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Expand the ideal projector as 2^(-n) times the graph-stabilizer sum. For subset sizes i,j in the two parts, all vertices of part A are supported when j is odd, otherwise just the selected i; likewise B is wholly supported when i is odd, otherwise just the selected j. X and Z at the same vertex still give a nonidentity Pauli. Trace orthogonality and depolarizing eigenvalue r=1-q give a fidelity sum of r^weight, yielding the displayed four terms by splitting (i,j) by parity. Independently for n=4 the weight polynomials are 1+6r^2+9r^4 and 1+2r^2+8r^3+5r^4, recovering the exact 49/256 versus 45/256 at r=1/2. With x=u/t and y=r/t we have x+y=1 and both strictly between zero and one. For b>=a+2, m=b-a-1, subtraction after normalization by t^n/4 gives two positive differences y x^a(1-x^m), x y^a(1-y^m), minus (y-x)(xy)^a(y^m-x^m). If y>x the latter is strictly less than the first positive term, since (y-x)/y, y^a and (y^m-x^m)/(1-x^m) are each in (0,1); if x>y exchange x and y; equality x=y makes the correction zero. Thus all adjacent comparisons are strict, including the last allowed step for either parity of n. The normalized balanced limit is 1 since both sizes diverge; for fixed a only 1+x^a+y^a survives, equal to 2 at a=1. The formula gives 1 and 2^(-n) at the endpoints, where no strict comparison holds. These are exact overlap statements for IID post-preparation depolarization, not entanglement or circuit-preparation thresholds. Inspected VERIFICATION.md and verify.py; the reported VERIFY_OK 3612 is a finite replay, not an all-size certificate. It was not rerun.

## originality

PASS

The stabilizer-weight identity and the star/GHZ formula are prior, and a distinct indexed qudit entry has an equivalent weight polynomial for qubit bicliques with both sides at least two. The defensible distinct result is the strict fidelity ordering across every adjacent split at all interior strengths and the sharp fixed-noise relative asymptotic, not the underlying Pauli-weight framework or the star formula.

## value

PASS

The exact ordering is a uniform optimization result in a natural graph-state family under a standard channel, with a quantifiable relative gain even though both overlaps decay. Neither a known star formula nor arbitrary individual biclique evaluations decide the extremizers over all splits and interior strengths. No entanglement, hardware, or wider graph-family optimality is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
