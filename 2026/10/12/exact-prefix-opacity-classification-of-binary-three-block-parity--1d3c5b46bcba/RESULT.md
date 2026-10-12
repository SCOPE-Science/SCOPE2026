# Exact prefix-opacity classification of binary three-block parity counters

## Finding
Let \(\mathcal B=\{000,001,010,011,100,101,110,111\}\). For each subset \(F\subseteq\mathcal B\), let \(u_F(n)\) be the number, modulo two, of length-three factors of the ordinary binary representation of \(n\) belonging to \(F\); occurrences are overlapping and leading zeros are excluded. For \(n=0\), use the representation `0`. Let \(\varpi(u_F)\) denote normalized prefix-metric opacity of the intrinsic minimal binary automaton, with output alphabet \(\{0,1\}\), as in Allouche--Yao [1].

**Theorem.** Exactly 249 of these 256 sequences have \(\varpi(u_F)=0\). The seven remaining subsets are precisely:

| \(\varpi(u_F)\) | Subsets \(F\) | Count |
| --- | --- | ---: |
| \(1\) | \(\varnothing\), \(\{010,110\}\), \(\{011,111\}\), \(\{010,011,110,111\}\) | 4 |
| \(1/2\) | \(\{000,010,100,110\}\), \(\{001,011,101,111\}\) | 2 |
| \(1/4\) | \(\mathcal B\) | 1 |
| \(0\) | Every other subset | 249 |

Here opacity \(0\) is *transparent*; normalized opacity \(1\) is *opaque*. All 256 defining predicates give distinct automatic sequences, despite the seven exceptional opacity behaviors.

For a compact reproducible encoding, number the eight blocks in lexicographic order starting with index zero and represent \(F\) by \(m(F)=\sum_{j=0}^{7} 2^j\,\mathbf 1_{\{b_j\in F\}}\). The exceptional masks grouped by shortest inhomogeneous-path length \(\ell\) are \(\ell=2:\{0,68,136,204\}\), \(\ell=3:\{85,170\}\), and \(\ell=4:\{255\}\). Every other mask has no inhomogeneous path on its minimal automaton.

## Assumptions and scope
The input alphabet and output alphabet are both \(\{0,1\}\). Every input word is read most significant bit first. Initial zeros are ignored by the internal automaton, including the representation of zero; no extra leading zeros are inserted when counting factors. Opacity is the *normalized prefix-metric* opacity of the intrinsic minimal automaton, not entropy, linear complexity, ordinary automaton state complexity, or a property of a nonminimal presentation. All assertions quantify over the entire family of subsets \(F\) (there are exactly 256 of them) and over every integer \(n\ge0\).

## Proof
**Step 1: A uniform finite transducer.** Introduce a leading-zero state \(L\), and states \((s,p)\) with suffix \(s\in\{\varepsilon,0,1,00,01,10,11\}\) and parity \(p\in\{0,1\}\). State \(L\) outputs zero, has a zero-loop, and on input `1` enters \((1,0)\). At \((s,p)\), reading a bit \(d\) forms \(v=sd\); it toggles \(p\) exactly when \(|v|=3\) and \(v\in F\), then stores the last two symbols of \(v\) (or all of \(v\) if shorter). Every \((s,p)\) outputs \(p\). Induction on the binary digits proves this transducer generates \(u_F\), including \(n=0\). It has at most 15 states, some unreachable.

**Step 2: Exact intrinsic minimization.** Delete unreachable states. Partition states by their output bit. Given a partition \(P\), replace the color of a state \(q\) by the triple consisting of its current color and the colors of its zero- and one-successors. Repeat until the number of colors stabilizes. Each step refines the preceding partition; since there are at most 15 states, stabilization occurs. At stabilization, two states are in the same block precisely when they have identical outputs after every future input word: the forward implication follows by induction using the stable successor colors, and the reverse follows from each finite-depth refinement. Thus the quotient is exactly the intrinsic minimal binary automaton (not merely an arbitrary realization).

**Step 3: An exact finite opacity test.** For the quotient graph, a path is inhomogeneous if its incoming edges to some target state include both input labels. Explore paths breadth-first from the initial state while recording, for each state, which of labels zero and one have occurred on incoming edges along the current path. If a newly used edge has the opposite label to an earlier edge entering its target, record its length as \(\ell\). Otherwise extend the recorded label profile. Merging identical pairs (current state, label profile) loses no future behavior. This is an exhaustive finite reachability computation: each quotient has finitely many states and only four possible label profiles per state. If the search exhausts without conflict, every path is homogeneous; if a conflict occurs, breadth-first search gives the shortest inhomogeneous length. By Theorems 1 and 2 of [1], the normalized opacity is zero in the first case and \(2^{2-\ell}\) in the second, because the normalization constant for binary automata is \(1/2\).

**Step 4: Complete case split.** `verify.py` implements Steps 1--3 without external packages. It performs them for every integer mask \(0\le m<256\); the assertions establish that the only finite shortest conflict lengths are \(2\), \(3\), and \(4\), with the mask classes shown under Finding, and all 249 other searches exhaust with no conflict. The program also independently counts occurrences directly in the binary representations of \(n=0,1,\ldots,2047\) for each mask and verifies output agreement. Because Steps 1--3 are exact finite-state reductions and the mask loop is exhaustive, the case split certifies the asserted theorem for all natural-number inputs; no bounded-length sampling is substituted for the infinite conclusion.

**Step 5: Different predicates give different sequences.** For any three-bit word \(1ab\), \(u_F(1ab)=\mathbf 1_{\{1ab\in F\}}\). For any three-bit word \(0ab\), one has \(u_F(10ab)=\mathbf 1_{\{10a\in F\}}\oplus\mathbf 1_{\{0ab\in F\}}\), where \(\oplus\) is XOR. Consequently all eight indicator values can be uniquely recovered from the sequence, proving the asserted distinctness.

## Verification
Run `python3 verify.py` with the Python standard library. The expected summary is `VERIFY_OK total=256 transparent=249 opacity_one=4 opacity_half=2 opacity_quarter=1 max_minimal_states=10 max_bfs_configurations=572`. A second line supplies the seven shortest-path witnesses. The exact assertions check the exceptional mask sets as well as the complete complement. The verifier must be executed against the supplied source, not a prior log. No randomness, heuristic pruning, external downloaded data, or timeouts enter the certificate.

## Relationship to prior work
Allouche and Yao [1], first public on April 21, 2024, introduce prefix-metric opacity and prove the intrinsic-automaton and shortest-inhomogeneous-path criteria used in the proof. Their paper treats well-known named sequences, but its inspected results and examples do not tabulate or classify all 256 arbitrary three-block parity predicates. The present contribution is this *complete exact first multi-pattern classification*, including the seven exceptional combinations and 249 transparent cases, rather than a new definition or generic opacity algorithm. Pattern-counting sequences, including the single all-one pattern, are considered in [2]; its results concern other combinatorial invariants, not the full opacity census. A classification of individual single-pattern counters does not, by itself, determine these XOR combinations because minimal-state quotienting and opacity are nonlinear under such combinations.

## Limitations
This is a finite, exact classification of length-three Boolean predicates only; it is not a closed-form classification for all pattern lengths or all alphabets. It relies on the stated exhaustive Moore-minimization and finite-graph reachability certificate for the complete 256-case split. The algebraic correctness of the finite reductions is proved above; executing the supplied verifier is necessary to reproduce the finite certificate. No independent validation or publication-priority guarantee is claimed.

## References
[1] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601, first publicly posted April 21, 2024. https://arxiv.org/html/2404.13601v1

[2] R. J. Hendel, *Runs, Squares, Palindromes, and Unbordered Factors of a Family of Binary Pattern Sequences with the All-One Pattern*, arXiv:2505.20547. https://arxiv.org/html/2505.20547v5
