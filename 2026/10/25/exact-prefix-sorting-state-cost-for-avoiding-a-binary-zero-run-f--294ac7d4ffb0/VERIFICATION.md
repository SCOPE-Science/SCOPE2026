---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed the precise universally quantified claim for all integers r>=1, forbidden contiguous 0^r1 over 0<1, trim partial deterministic automata with all states final and missing transitions rejecting. The ordinary minimal DFA counts trailing zeros j=0..r with 0-transition j->min(r,j+1), 1-transition j->0 for j<r, and undefined 1 from r; each state j is reached by 0^j and i<j are distinguished by suffix 0^{r-j}1 (accepted from i, not from j). For each 0<=i<j<=r the strict colex triple 0^i<0^j<10^i has first/last reaching class i and middle reaching j; the standard DFA maximum colex separation property forces all pairs incomparable, giving width r+1. For the explicit 2r+1-state WDFA A_0..A_r,B_0..B_{r-1}, order A_0<...<A_r<B_{r-1}<...<B_0, verified state-fibres, all 0-target monotonicities, common 1-target B_0, incoming-label consistency, and r=1 and terminal boundary. In any deterministic Wheeler order each reached-word fibre is colex convex and lies inside one Myhill–Nerode class; each j<r has interleaving 0^j<0^{j+1}<10^j, so needs >=2 fibre components; terminal class r needs >=1, proving lower bound 2r+1. Independently implemented (not the provided CHECKER.py) state machine and all ordered-pair Wheeler axioms for r=1..6; exhaustively enumerated all binary words through length 2r+7 per parameter (respectively 1023,4095,16383,65535,262143,1048575 words), checked acceptance versus substring condition, exact reached classes, and observed 2r+1 colex input-fibre intervals. Finite checks corroborate only small parameters; the symbolic argument establishes all r.

## originality

PASS

Best-of-knowledge PASS for the precisely stated language avoiding 0^r1, not a claim of new Wheeler existence, a new interval theorem, or a new state-overhead mechanism. A newly inspected and previously uncited particularly close predecessor, D’Agostino–Martincigh–Policriti, arXiv:2203.12534 §3.1, explicitly proves the SAME numerical WDFA size 2n+1 and essentially the same colex splitting witnesses for a DISTINCT language avoiding a^{n+1}; its ordinary minimum likewise has n+1 states and exhibits maximal colex incomparability by the same triples. The present L_r instead forbids 0^r1 while allowing arbitrarily long terminal zero runs; at trailing-zero state r, it has a 0 self-loop and no 1-transition, whereas the prior pure-run avoidance has no 0-transition and resets on 1. Thus the prior worked example is a close template but is not literally this language, a simple letter renaming, or a theorem asserting all one-factor forbidden languages have this exact state count. The independently audited family-specific construction, word-fibre partition and lower bound supply the necessary boundary-sensitive argument; all qualitative ideas and the 2r+1 phenomenon are credited to prior work. Searches cannot establish absolute priority; especially close-analogue and unindexed-example risks remain substantial.

## value

PASS

A single forbidden factor 0^r1 is a natural, uniformly parametrized constraint on text/path languages; exact minimal Wheeler state counts determine the storage cost of imposing a colex index versus ordinary DFA minimization, so an exact infinite-family formula has a plausible independent use. The distinctive unrestricted terminal zero tail changes transition semantics relative to the prior a^{r+1} factor-avoidance example, and it was not mechanically implied by a stated theorem for the target language: the absorbing-class boundary and exact convex class partition must be checked. The resulting width r+1 and exact Wheeler count 2r+1 are mathematical facts about this precise natural language and are not an arbitrary cutoff or numerical slice. Mathematical significance is modest: 2022 literature already exhibited the same state-cost phenomenon and exact 2r+1 for a very close pure-run avoidance family. This audit does not claim a new method or new qualitative state tradeoff; the independent family-specific exact determination, despite its simplicity, meets the bounded exact-invariant value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
