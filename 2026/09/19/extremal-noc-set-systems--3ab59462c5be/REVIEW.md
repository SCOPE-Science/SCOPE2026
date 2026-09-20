# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Equality in the published levelwise estimate forces equality at every cardinality. At a fixed k-level, the chosen NOC witnesses occupy exactly n-k+1 distinct ground elements, leaving exactly k-1 non-witness elements; therefore every k-set is the common (k-1)-element core plus its private witness. The only remaining issue is compatibility between consecutive levels. For any petal x at level k, its NOC witness property makes every level-(k+1) set containing x comparable with the k-set. If x is outside the next core, its corresponding next-level set forces core containment directly. If x is inside the next core, all next-level sets contain x and therefore contain the k-set; intersecting those at least two sets again forces core containment. Thus the cores form a strict chain, yielding the claimed ordered family. The converse is the published sharpness construction after relabeling.

The uniqueness count follows because the intersections of the non-top levels recover the core chain, determining the first n-2 labels in order and leaving only the final two labels interchangeable. The Hasse arc and reticulation formulas follow by listing adjacent-level containments. A standalone verifier exhaustively checks every nonempty set family for n<=4 and separately checks the Hasse statistics for the canonical family through n=10. These finite checks support but do not replace the proof.

Adversarial checks included k=1, k=n-1, n=2, the case where a level-k witness belongs to the next core, and the possibility of additional Hasse covers skipping a cardinality. The nested-core description resolves all of these cases; every non-top set has an intermediate adjacent-level superset, so no skipped-level cover occurs.

## Originality

**PASS, to the best of our knowledge.** The full current arXiv v1 of Lindeberg--Hellmuth was inspected. Its Lemma 5 proves the sharp n(n+1)/2 bound and supplies one ordered extremal construction; it does not state an equality classification, uniqueness up to relabeling, or the n!/2 count. Corollary 9 transfers sharpness to tree-child and normal network cluster counts, while the concluding section explicitly identifies enumeration of NOC clustering systems and refinement by reticulation number as directions for further work.

The accessible full text of Alcalà--Llabrés--Rosselló--Rullan (2014) was inspected around its strict-compatibility characterization. It establishes the equivalence with tree-child cluster realizability but does not give the later quadratic NOC bound or its equality cases. Exact and synonymous searches using NOC, not-overlap-covered, inclusion-visible, strict-compatible, tree-child cluster systems, private elements, full sunflowers, and nested cores found no equivalent classification or stronger theorem.

A residual risk remains that the levelwise equality argument may appear in older extremal-set-system literature under unrelated terminology, because the same-level step is a private-element extremal statement. Very recent unindexed parallel work is another residual risk. No concrete source found in the search states the cross-level nested-core rigidity, the n!/2 labeled enumeration, or the corresponding extremal normal-network count.

## Value

**PASS.** The result converts a sharp upper bound with one witness construction into a complete equality theorem. It shows that there are no other extremal geometries, gives an exact n!/2 enumeration on a labeled ground set, and translates that rigidity to canonical normal-network classes that the source paper explicitly connects to enumeration. The additional Hasse formulas identify the exact arc and reticulation counts of every extremal regular realization. This is a structural and enumerative strengthening rather than a new numerical example.

## Limitations

The theorem concerns exact extremizers only and does not provide a stability theorem for near-equality. It does not enumerate all NOC systems. The network enumeration applies to strong-phylogenetic normal networks and phylogenetic separated normal networks via the published bijections; arbitrary non-regular realizations of the same cluster system are not counted. Older literature under substantially different set-system terminology and very recent unindexed work remain residual originality risks. Finite computation is supporting evidence only. No independent validation or independent audit has been performed.
