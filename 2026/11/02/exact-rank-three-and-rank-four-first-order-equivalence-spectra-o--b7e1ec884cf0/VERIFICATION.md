---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For G_n=P_n^2, adjacency iff 1<=|i-j|<=2, in the equality-and-adjacency language with no order/constants, rank-q EF equivalence equals equality of recursively constructed sets of atomic extension types. Pinned verify_types.cpp was inspected, compiled and actually executed through n=47, recovering rank-3 classes min(n,11) and rank-4 classes min(n,26) for each of those n. The separate all-size Duplicator invariant matches equal gaps shorter than B_r=3*2^r and large gaps >=B_r; splitting at B_{r+1}=2B_r and B_0=3 preserves adjacency at game termination. It proves infinite tail equivalence for n,m>=23 at rank 3 and >=47 at rank 4; finite type overlap by transitivity gives sharp all-n thresholds 11 and 26. The finite program is not an infinite proof; the game-strategy and threshold bridge are necessary.

## originality

PASS

Best-of-knowledge originality of the specific final claim, excluding established background components; real Resultary searches and relevant primary-source statements did not show a dominating equivalent, with explicit primary access and unindexed-source residual risks. Published result for directed paths gives 2^q threshold in successor language; the claimed q=3 cutoff 11 and q=4 cutoff26 are neither equal nor consequences. Interval FO model checking yields no numeric cutoff.

## value

PASS

Sharp complete low-quantifier-rank EF spectra of an elementary but structurally nontrivial graph power, including two provably optimal stabilization thresholds; this distinguishes adjacency-only squared paths from ordinary paths and directed successors. A natural exact logical invariant, not a routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
