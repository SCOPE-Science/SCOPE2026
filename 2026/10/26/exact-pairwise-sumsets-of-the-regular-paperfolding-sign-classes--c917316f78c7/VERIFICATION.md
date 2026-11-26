---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The scope is ordinary two-summand sumsets on N0, including repeated summands, with A and B given by the odd part of n+1. The recursions split the even terms into 4N0 for A and 4N0+2 for B, and reduce every odd term 2u+1 to u. For A+A, residues 0,1,3 mod 4 have explicit witnesses using 0,1,3, and residue 2 reduces to a smaller even target by requiring two lifted odd terms. For A+B, residues 2,3 have immediate witnesses and residue 1 is represented from 5 onward using the B-term 5; the multiples of 4 from 8 onward lift the already represented odd targets 2m-1. The only possible B-term below 5 is 2, ruling out 0,1,4. For B+B, two even terms cover the positive multiples of four, and using 5 or 11 with an even B-term covers odd residues from 7 or 13, respectively. Below those bounds the odd totals 1,3,5,9 are impossible by the actual initial B-terms. A target congruent to 2 mod 4 forces two odd terms and is representable iff (n-2)/2 is. Every such chain stays even and terminates; the only missed terminal value is zero, whose backwards orbit is 2^k-2 for k>=1. Counting that disjoint even family gives floor(log_2(X+2)) for real X>=0, and the four odd indicators give the rest. Density one follows. Fresh direct enumeration allowing repeats matched all three sumsets and the integer-threshold counting formula through 4095.

## originality

PASS

The normalizing rule for the paperfolding classes is classical. The inspected additive works and exact same-day sign-class findings do not give the three sumsets of these classes, including the precise dyadic defect. No publication priority is established.

## value

PASS

For a canonical automatic partition, an exact width-two additive classification distinguishes a full basis, a cofinite mixed sumset, and a density-one sumset with infinitely many holes. The dyadic backward orbit and four odd exceptions specify which large targets fail, not merely how often failure occurs, giving an exact benchmark for additive-basis methods on automatic sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
