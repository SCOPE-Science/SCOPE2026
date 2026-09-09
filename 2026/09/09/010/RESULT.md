# Complete certified careful-synchronizability map of the C7 one-hole ball

## Context and motivation

Careful synchronization of partial automata (the Martyugin/Vorel program)
asks how undefined transitions inflate reset cost: a careful word must never
attempt an undefined transition on its current image set. The Černý extremal
$C_7$ is the canonical smallest number of states at which binary partial
(reset) thresholds can exceed the ordinary $(n-1)^2$ value (Cambie–de Bondt–Don:
maximal binary-PFA threshold $>(n-1)^2$ iff $n\ge 6$). The full single-deletion
ball around $C_7$ is therefore the extremal-anchored canonical neighbourhood
for benchmarking the cost of carefulness versus ordinary completion. The
original target was a strict careful-vs-ordinary separation witness; the
attained result is the admitted fallback: the complete certified map showing
no such separation exists in scope, plus a 98-cell ordinary-length fill
landscape.

## Definitions

- $Q=\{0,\dots,6\}$, alphabet $\{a,b\}$, words act on the right.
- **$C_7$:** complete binary DFA with $a(i)=(i+1)\bmod 7$ (7-cycle) and
  $b(i)=i$ for $i<6$, $b(6)=0$.
- **One-hole mutant:** partial automaton obtained by deleting exactly one
  transition entry: letter $\ell\in\{a,b\}$ at state $s\in Q$ becomes
  undefined ($\bot$). There are exactly $2\cdot 7=14$ such mutants.
- **Careful synchronization:** a word $w$ whose every prefix is defined at
  every state of the current image set starting from $Q$, and whose final
  image is a singleton. A careful power-automaton step from set $S$ by letter
  $d$ is allowed only if $d$ is defined on all of $S$.
- **Canonical completion** of mutant $(\ell,s)$: restore the deleted entry to
  its $C_7$ value (hence every canonical completion equals $C_7$).
- **Fill $(\ell,s)=v$:** total DFA obtained by filling hole $(\ell,s)$ with
  value $v\in Q$ (98 completions). Ordinary reset length is the shortest word
  collapsing $Q$ to a singleton, or non-synchronizing (NS).

## Result

**Theorem 1 (baseline).** $C_7$ has ordinary shortest reset length exactly
$36$, e.g. via
$w_0=$ `baaaaaabaaaaaabaaaaaabaaaaaabaaaaaab` with $w_0(Q)=\{0\}$,
and no shorter reset word exists.

**Theorem 2 (main census: no careful word anywhere in the ball).**
None of the 14 one-hole mutants of $C_7$ is carefully synchronizing.

**Corollary (gap table).** Since no mutant admits a finite careful length,
the strict careful-vs-ordinary gap is vacuous over the whole ball: every row
reads careful verdict NO / length undef / canonical-completion ordinary
length $36$ / gap N/A.

**Proposition (completion-fill landscape, exact data).** Filling hole
$(\ell,s)$ with $v\in Q$ yields ordinary shortest reset length (or NS):

| hole | v=0 | v=1 | v=2 | v=3 | v=4 | v=5 | v=6 |
|------|------|------|------|------|------|------|------|
| a0 | 6 | 36 | 25 | 17 | 11 | 7 | 6 |
| a1 | NS | 6 | 36 | 25 | 16 | 10 | 6 |
| a2 | NS | NS | 6 | 36 | 25 | 16 | 9 |
| a3 | NS | NS | NS | 6 | 36 | 25 | 16 |
| a4 | NS | NS | NS | NS | 6 | 36 | 25 |
| a5 | NS | NS | NS | NS | NS | 6 | 36 |
| a6 | 36 | NS | 26 | NS | NS | NS | 6 |
| b0 | 36 | 16 | 16 | 16 | 12 | 10 | NS |
| b1 | 9 | 36 | 20 | 13 | 12 | 13 | 10 |
| b2 | 10 | 9 | 36 | 18 | 15 | 13 | 12 |
| b3 | 15 | 13 | 9 | 36 | 18 | 15 | 16 |
| b4 | 14 | 17 | 12 | 9 | 36 | 20 | 15 |
| b5 | 13 | 14 | 17 | 11 | 9 | 36 | 16 |
| b6 | 36 | 31 | 26 | 21 | 16 | 11 | NS |

The original-entry column of each row reads $36$ throughout ($=C_7$).

## Proof / evidence

*Theorem 1:* direct simulation gives $w_0(Q)=\{0\}$; exhaustive BFS over the
power automaton ($2^7=128$ subsets, 2 letters) certifies distance $36$ minimal.

*Theorem 2 (trap identities):* $F=b(Q)=\{0,\dots,5\}$, $G=a(F)=\{1,\dots,6\}$;
(i) $b(Q)=F$; (ii) $b(F)=F$ ($b$ fixes $F$ pointwise);
(iii) $a(F)=G$; (iv) $b(G)=F$; (v) $a(Q)=Q$.
- (a-hole, $s<6$): first $b$ sends $Q$ to $F$; first $a$ is undefined at
  $s\in Q$ (else $Q\to Q$ loop). From $F$, $b$ self-loops and $a$ is undefined
  at $s\in F$. No singleton carefully reachable.
- (a-hole at 6): $Q\to_b F\to_a G$ avoids the hole; from $G$ only $b$ is
  defined (back to $F$); from $F$ only $a$ progresses (back to $G$).
  Reachable carefully-defined sets stay in $\{Q,F,G\}$, all of size $>1$.
- (b-hole, $s<6$): $Q\to_b$ is undefined at $s\in Q$; $Q\to_a Q$ loops; any
  visit to $F$ or $G$ needs a $b$-step undefined at $s\in F\cap G$.
- (b-hole at 6): $b$ undefined at $6\in Q$; $a$ permutes $Q$ so no careful
  step ever leaves $Q$.
Hence no careful word reaches a singleton. Independent careful power-automaton
BFS ($\le 128$ states per mutant, transition allowed only if defined on the
whole current set) returns "no singleton reachable" for all 14 mutants.

*Fill landscape:* each entry is the exact ordinary-BFS distance (or certified
unreachable) over the 128-set power automaton; every synchronizing cell's
witness word was simulated to a singleton.

## Limitations

- Strict-separation target was NOT attained: no finite careful length exists
  in scope, so no gap witness is claimed.
- All values are relative to the stated $C_7$ labelling ($a$ 7-cycle;
  $b$ identity except $6\to 0$); other labellings, $n\ne 7$, and multi-hole
  mutants are out of scope.
- Fill-landscape cells are exact BFS + simulation certificates, not
  hand-proved individually.
- Careful semantics must be preserved on reuse; results do not transfer to
  exact/ordinary PFA synchronization variants.

## Reproducibility

Run `python3 output/artifacts/verify.py` (stdlib only) → prints `VERIFY_OK`.
It re-verifies: C7 witness + BFS $=36$ (R1); trap identities + 14 careful-BFS
emptiness verdicts (R2); 14 canonical completions $=36$ (R3); all 98 fill
cells against `fill_landscape.csv` (R4). Tables: `gap_table.csv`,
`fill_landscape.csv`. Auditor independently recomputed all claims with fresh
BFS code: 0 mismatches.

## References

- V. Vorel, Subset Synchronization and Careful Synchronization of Binary
  Finite Automata. https://arxiv.org/abs/1403.3972
- S. Cambie, M. de Bondt, H. Don, Extremal Binary PFAs with Small Number of
  States. https://arxiv.org/abs/2108.13927
- M. de Bondt, H. Don, H. Zantema, Lower Bounds for Synchronizing Word
  Lengths in Partial Automata. https://arxiv.org/abs/1801.10436
- P. V. Martyugin, Synchronization of Automata with One Undefined or
  Ambiguous Transition, CIAA 2012.
  https://link.springer.com/chapter/10.1007/978-3-642-31606-7_24
- M. Szykula, Synchronizing Automata: Open Problems (survey framing careful/
  subset synchronization as live frontier).
  https://arxiv.org/abs/2608.24245
