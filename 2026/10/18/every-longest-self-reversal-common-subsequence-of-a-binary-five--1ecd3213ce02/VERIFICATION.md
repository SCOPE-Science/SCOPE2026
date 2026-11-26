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

PASS applies to the complete repaired RESULT.md. The frozen proof's five-run E/L partition was not exhaustive: for w=01111010 the common word 0111110 draws its five ones from both one-runs in each input. The repair splits on the length j of the middle one-block. If j>max(b,d), both embeddings use both one-runs, confining the two zero-blocks to the outer runs; jointly attainable bounds are (p,b+d,p), whose unique maximum is palindromic. If j<=max(b,d), any split embedding can be made unsplit by keeping the outer zeros and moving all j ones to a long enough one-run; the original E/E and L/L length bounds and E/L and L/E palindromic maximizers are then exhaustive. The repair also makes explicit why split embeddings do not invalidate the four-run two-block argument: the reversed word bounds the length available for consolidating the split block, freeing an endpoint symbol, and if no early-run symbol is used the longer palindrome from the stated bounds exists. The stated orbit relation now correctly uses reversal followed by complementation between the two zero-starting representatives. One- and two-run inputs admit only palindromic optima directly; at three runs the two-run patterns extend and the three-run maximum is symmetric; at four runs the two three-run patterns have independently attainable symmetric maxima and no four-run pattern can embed in both. At five runs all even-run words extend, the five-run maximum and the 101 maximum are symmetric, and the repaired 010 cases cover the rest. Independent subsequence-set enumeration through length seven confirmed every entry of the six-case table and the four exceptions, with maximum length five for each exception. A separate direct position-mask run through length twelve corroborated the finite boundary without substituting for the unrestricted proof.

## originality

PASS

The repair preserves the original scientific claim. The examined sources establish equality of LCS and LPS lengths, analyze fixed tie rules, or study palindromes as a restricted output family; none establishes this sharp binary-run guarantee for every optimal word or the four shortest binary obstructions. The broader alphabet examples do not contradict the binary threshold.

## value

PASS

The repaired theorem supplies a sharp structural condition under which an arbitrary correct LCS backtrack on a word and its reversal must return a longest palindrome. The threshold is motivated by the tie-breaking failure in this standard reduction, not by an arbitrary enumeration length. The first obstruction and its full symmetry orbit are exact minimal test cases that delimit the guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
