# Independent mathematical audit

## correctness

PASS

The binary greedy-arch scan (store first unseen letter, close at first different letter) has number of complete arches equal to scattered-subsequence universality index iota; any length-iota binary word chooses its symbols arch by arch, while a target of length iota+1 is missing after the incomplete one-letter suffix. For each Dyck prefix define K arches, register L, height H≤h, parity J=K mod2, and R=prefix_length−B(K), B(2q)=2hq+2, B(2q+1)=2h(q+1). The six-case potential Φ(H,L,J) in actual RESULT.md satisfies R≤Φ by direct one-step transition inequalities, using reachable-state restrictions H=h⇒L=0 and H=h−1⇒L≠1. The final state H=0 has Φ≤0, proving semilength n≤h(k+1)/2 for odd k and n≤hk/2+1 for even k. Words (0^h1^h)^q and its appended 01 reach both bounds; partial final mountains prove the stated minimum-index n/h residue formula and height1 alternate case. Independent exhaustive n≤8 Dyck generation, direct target-subsequence tests, and exact greedy-index comparison yielded 2055 word checks and 64 min-pairs; finite tests do not establish arbitrary height, for which the displayed symbolic potential is decisive.

## originality

PASS

The final statement, not the title or isolated numbers, was compared against the actual prior implications and synonyms, with bounded source reading and explicit priority risks. The surviving precise assertion is not implied by the inspected sources. Best-of-knowledge PASS, not unconditional certification. Different-language results on maximum binary path length at fixed transition-matching number, nested-parenthesis universality, or older Dyck/arch combinatorics could imply the same bounds. The searched primary articles do not yield a direct domination; search failure is not priority proof.

## value

PASS

Nesting height is the standard stack-depth or Dyck-path amplitude parameter, while scattered-subsequence universality is a natural universality invariant. The theorem gives the exact global tradeoff at every height h and index k with explicit extremal words, sharpening algorithmic arch methods into a structural optimization linking path complexity and pattern coverage. This is an infinite exact classification, not a renamed arch-count algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
