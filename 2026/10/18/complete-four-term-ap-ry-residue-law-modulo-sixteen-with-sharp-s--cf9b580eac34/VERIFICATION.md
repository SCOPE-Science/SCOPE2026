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

Squaring the central-binomial factor kills k of binary weight at least two modulo 16. At k=2^j the remaining Lucas bit is b_j xor b_(j+1), including zero for k>n. Thus A_n=1+4(n mod 2)+8r(n) mod 16. Appending 0 gives (0,u xor p,u); appending 1 gives (1,u,v xor (1-p)). I rebuilt the eight-state matrix, checked its characteristic polynomial x^3(x-2)(x-1)^2(x^2-2x+2) and the stated annihilator. The column and row sums give the constant dominant projection and the annihilator precludes loss of a polynomial factor at the other nonzero eigenvalues. A fixed prefix gives the same entrywise O(2^(L/2)) bound on every aligned block of length 2^L; geometric summation yields the all-cutoff error. The even word decodes its three bits, and for each parity of t the odd parameterization decodes the underlying three-bit state bijectively. Thus truncations at arbitrary N change counts by at most O(1) on splitting into the parity subclasses, giving 8/16 and 16/32 as the two contributions to total mass. For sharpness, the L=4,8,12 counts are 1,36,496; after four steps the surviving recurrence roots are 16,1,-4, giving the claimed sequence from m=1. An independent check of the identity is that s(t)=(0,0,0) iff t=4a with an even number of runs of 1s in a. For L=4m there are binom(L-1,2j) suffix strings with j such runs; filtering for j even gives 2^(L-3)+Re((1+i)^(L-1))/2. Replay: python3 /workspace/branches/independent_replay.py 1 independently checks direct binomial sums through n=179, 8,192 windows, the transfer polynomial, and the special state at four dyadic cutoffs. The finite data corroborate the proof; the frozen verifier was read, not run.

## originality

PASS

Rowland–Yassawi's pointwise run-count congruence is exact prior coverage and is not the new result. No inspected source supplies the complete four-window support, the two rational word frequencies with uniform square-root error, and the explicit sharp cell for this Apéry sequence. The closest finite-state and digit-sum comparisons use different sequences/statistics or provide general methods rather than evaluating this joint law.

## value

PASS

This is a natural exact local correlation law for the classical mod-16 Apéry sequence, not a selection of a few tested residues. It explains all eight extra exclusions beyond alternating mod-4 classes, quantifies the unequal frequencies of the permitted words, and supplies a concrete cell witnessing that all-cutoff square-root accuracy cannot be uniformly improved. These are more informative than the one-point congruence or mere automaton recognition; no claim is made for longer blocks or larger moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
