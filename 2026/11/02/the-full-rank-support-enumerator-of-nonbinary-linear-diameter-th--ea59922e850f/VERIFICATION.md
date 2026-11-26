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

For a labelled F_q-linear code of diameter at most three, a word nonzero at each pivot bounds rank by three. Uniform words have mean weight s(q-1)/q, so support is at most four, at most three for q>=5; the mean obstruction is even strict for nonzero codes because the zero word has weight zero, excluding s=4 for q=4. For support four, rank one is impossible, and rank three is a hyperplane with check-vector support t=2,3 or 4. Nonzero check-coordinate entries can be chosen in opposite pairs for even t and to form a nonzero triple summing to zero for t=3 (choose two nonzero entries with nonzero sum, possible for q>=3); arbitrary other entries give a weight-four word. For rank two, the four nonzero columns must represent all projective directions, since otherwise there is a row direction vanishing on none of them. In the ternary case each direction then occurs once, all words other than zero have weight three, and ordered column choices divided by GL_2(3) give 24*16/48=8. For s<=3 all support subspaces are valid, so one counts full-support lines up to scalar, planes by removing the three coordinate planes in length three, and full coordinate spaces in their respective ranks. The exact polynomial, totals, leading coefficients, and n=0 follow. Independent replay: python3 -B /workspace/reproductions/anticodes.py constructs distinct word-set subspaces by extensions, including all ranks, and directly checks every coefficient at (q,n)=(3,5),(4,4),(5,4) after scanning 2664, 529 and 1120 subspaces; it gives respectively 226, 141 and 215 qualifying subspaces and 40 rank-two support-four codes in the first case. The frozen verify.py prints a full support/rank tally but only asserts the total and the exceptional coefficient, not all coefficients as the verification prose claims; the independent finite check compares them individually. The proof, not a finite test, establishes the full range.

## originality

PASS

Credit existing fixed-diameter polynomial support reduction, support bounds, the resulting growth degrees and the classical ternary simplex code. The distinct supported result is the exhaustive maximum-weight-three labelled rank-by-support census across nonbinary fields, particularly the classification and exact multiplicity of all admissible four-supported codes rather than existence of one tetracode. The prior bounds and checked code parameters do not evaluate that coefficient or give the complete rank-refined census; priority is bounded by the materials inspected.

## value

PASS

Fixed-diameter anticode counts are motivated by the prior polynomial framework with unevaluated coefficients. The new exact part identifies every exceptional four-supported case and yields its labelled contribution and leading coefficient, while the complete rank refinement answers the count on each support without treating the known asymptotic degrees or tetracode construction as new. This is useful beyond verifying one code or one parameter point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
