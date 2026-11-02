---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The source result fixes the input as standard unsigned base-2 numerals without leading zeros and counts overlapping length-3 factors in a chosen subset modulo 2. A suffix/parity transducer with one leading-zero initial state and at most 14 suffix/parity states computes it by induction. Reachability restriction followed by stable Moore color refinement yields the unique intrinsic minimal DFAO, preserving the initial zero-loop. In the quotient, a state of a finite-path search is (current quotient state, for each target the subset of 0/1 incoming labels already used on this path). This is a complete sufficient statistic for future conflicts. A conflict is precisely an inhomogeneous path (a target previously entered under the opposite label), and BFS yields its shortest possible length; absence upon exhausting the finite profile graph proves transparency for all path lengths. Allouche--Yao Theorem 1 identifies the intrinsic automaton and their Theorem 2 makes the normalized opacity 0 when no conflict, or 2^(2-ell) at shortest conflict length ell (binary maximum unnormalized opacity 1/2). An independent differently structured implementation enumerated all 256 masks, independently minimized every transducer, and exhausted every path-profile graph: ell 2 exactly masks [0,68,136,204], ell 3 exactly [85,170], ell 4 exactly [255], ell=0 otherwise (249 masks). It counted a maximum 10 minimal states and 572 reachable profile configurations, with 256 direct numeral crosschecks per mask. The infinite sequence conclusion uses the finite automata argument, not the bounded numeral checks. Distinctness is analytically proved because u_F(1ab) recovers membership of 1ab, while u_F(10ab)=1_{10a in F} XOR 1_{0ab in F} recovers 0ab for all a,b in {0,1}. The empty mask and the full mask, the n=0 representation, 000 and 111 factors, and masks with zero or more exceptions are explicitly covered.

## originality

PASS

The distinctive statement is the complete seven-exception classification among all eight-block Boolean parity predicates. The cited Allouche–Yao theorem supplies an algorithm and individual named examples, not the exact 256-mask result; an earlier restricted all-one-pattern study treats other invariants. The exception set requires additional nontrivial finite minimization and reachability computation. Priority is best-of-knowledge with risks recorded.

## value

PASS

An exact natural complete classification of the first multi-pattern binary parity family with all eight 3-block local contexts selectable. The exceptional masks quantitatively show that intrinsic prefix-opacity is not additive under XOR, with nonzero levels 1, 1/2, 1/4; this is not a recomputation of an identified table and is a useful reference for extending beyond single-pattern counters. No longer-window theorem or general algorithmic improvement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
