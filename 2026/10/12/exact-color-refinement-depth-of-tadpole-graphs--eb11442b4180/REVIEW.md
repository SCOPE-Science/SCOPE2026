# Self-review

## Correctness
PASS. The proof uses the published equivalence between color-refinement rounds and truncated rooted universal covers, then writes the universal cover of a tadpole explicitly as a bi-infinite spine with degree-three branch points every \(m\) edges and a pendant path of length \(k\) at each branch point. The three possible slow comparisons are separately reconstructed: cycle-position separation, tail-position separation, and the cycle-neighbor versus tail-neighbor comparison. The last pair is checked to agree through round \(\min\{m,k\}-1\) and split in round \(\min\{m,k\}\). These upper and lower witnesses coincide in the stated maximum. The fixed-order corollary is an immediate optimization of the exact formula.

The standalone verifier checks \(3840\) parameter pairs, the exact cross-branch witness round for all of them, and every total order from \(4\) through \(100\).

## Originality
PASS with residual literature risk. published-finding corpus searches for tadpole, kite, and dragon graphs combined with color refinement, 1-WL, Weisfeiler-Leman, stabilization depth, and iteration number produced no matching result. Web searches under the same aliases likewise found the named family and unrelated tadpole invariants but no color-refinement formula. The full Krebs--Verbitsky text supplies the universal-cover equivalence but no tadpole calculation. The full Kiefer--McKay text studies iteration numbers globally, explicitly discusses paths, and contains no tadpole-family formula in the inspected material. DeMaio--Jacobson establishes the standard tadpole notation and studies a different invariant.

## Value
PASS. Tadpoles are a standard named unicyclic family, and the iteration number of color refinement is a studied invariant. The exact answer is not a one-scale path calculation: it is the maximum of three independent propagation lengths, with \(\min\{m,k\}\) arising from a delayed ambiguity between the cycle and tail incident to the attachment vertex. This mechanism can dominate both the cycle-radius and tail-radius terms, and it yields a clean sharp half-order extremum within the whole tadpole family.

## Closest literature and limitations
The closest methodological source is Krebs--Verbitsky, arXiv:1407.3175, especially Lemma 2.6, which identifies round colors with rooted universal-cover truncations. Kiefer--McKay, arXiv:2005.10182, is the closest source on the iteration-number parameter and gives unrestricted extremal results. DeMaio--Jacobson, DOI:10.5614/ejgta.2014.2.2.5, confirms the standard tadpole family and notation but treats independent-set counts. No independent literature audit has been performed, and an obscure family-specific computation under nonstandard terminology could still exist.

Self-review: passed. Independent audit: not yet performed.
