# Scientific review

## Correctness — PASS

The theorem states one uniform claim with two parameter regimes, \(k\ge2\) and \(n\ge4k\). The proof first bounds every refinement class by the reflection-distance orbit. It then computes exact second-round neighbourhood counts and inductively proves that the refinement front advances by exactly \(k\) shells per subsequent round, unless the remaining tail is a single shell. At the seam \(n=4k\), explicit counts prove the unique second-round collision and a third-round witness separates it. This establishes the complete partition formula and the sharp depth formula. The two independent Python checks were run against actual standalone files. No finite experiment is taken as an infinite proof.

## Originality — PASS, with residual priority risk

Primary comparisons were made with Arvind–Köbler–Rattan–Verbitsky (arXiv:1502.01255; definitions, amenability/refinability and general graph-theoretic hierarchy), Kluge (arXiv:2204.01054; complete relevant Section 4 on group-ring refinement and prime-order Cayley graphs, particularly Lemma 38), and Verbitsky–Zhukovskii (arXiv:2310.05788; introduction and random-circulant main theorem). The Arvind paper supplies general concepts but no exact marked cycle-power round counts. Kluge's prime-order one-mark stable partition can cover an orbit-level conclusion for its prime subfamily but gives neither the all-order wavefront nor sharp round counts or the \(n=4k\) seam. The random-circulant result does not determine these deterministic families. A distinct earlier result on unmarked path powers concerns identification among arbitrary graphs, not this rooted cycle-power refinement process.

Relevant published-finding corpus semantic searches on rooted cycle powers, equivalences, exact rounds, and the antipodal seam found no claimed equivalent or dominating theorem. This is evidence of non-overlap, not a proof of publication priority. A specialist text on circulant equitable partitions could conceivably contain an implicit derivation; independent priority verification remains to be done.

## Value — PASS

Cycle powers are a canonical multi-generator circulant family, and colour-refinement convergence time is a natural logical/algorithmic invariant. The result determines **every** intermediate partition for an unbounded two-parameter family and proves the **minimal** number of rounds, not merely an eventual orbit-equality statement. The exact \(k\)-shell propagation law and its exceptional antipodal collision show an abrupt nonmonotonicity at \(n=4k\) versus \(n=4k+1\). This offers a controlled benchmark for individualization in highly symmetric graphs. The claim does not assert a graph-isomorphism identification theorem or cover denser powers.

## Limitations and closest literature

The sharp formula is proved for \(n\ge4k\) only. The analyses of other circulants and of multiple marked vertices remain open in this note. Prime-order orbit recovery is closely related to Kluge's Lemma 38; the original step-by-step and all-composite-order claims are the distinction. Third-party full-text priority checks beyond the accessed relevant sources are incomplete.

Self-review: passed. Independent audit: not yet performed.
