# The smallest binary primitive nonsynchronizing nonpermutation boundary
## Finding
Consider complete deterministic binary automata on a finite state set, with at least one non-permutation letter. Primitivity means that no nontrivial equivalence relation on the states is preserved by both letter maps; synchronizability means that some word induces a constant map.

No primitive nonsynchronizing automaton in this domain exists on fewer than five states. On five labeled states there are exactly
\[
2880
\]
ordered transition pairs that are primitive and nonsynchronizing.

Modulo simultaneous relabeling of the five states and exchange of the two input letters, those \(2880\) automata form exactly
\[
12
\]
isomorphism classes. Every class has orbit size \(240=2\cdot5!\). Eight classes have two rank-\(3\) letters, and four classes have one rank-\(3\) letter and one permutation.

With states ordered as \(0,1,2,3,4\), one representative transition pair \((a,b)\) from each class is:

| class | \(a\) | \(b\) |
|---:|:---|:---|
| 1 | \((4,0,2,2,0)\) | \((3,1,1,0,0)\) |
| 2 | \((2,0,4,4,0)\) | \((3,1,1,0,0)\) |
| 3 | \((0,2,3,4,1)\) | \((3,1,1,0,0)\) |
| 4 | \((4,2,0,0,2)\) | \((3,1,1,0,0)\) |
| 5 | \((0,2,4,4,2)\) | \((3,1,1,0,0)\) |
| 6 | \((0,4,1,2,3)\) | \((3,1,1,0,0)\) |
| 7 | \((0,4,2,2,4)\) | \((3,1,1,0,0)\) |
| 8 | \((2,1,3,4,0)\) | \((1,3,1,0,0)\) |
| 9 | \((1,2,4,4,1)\) | \((1,3,1,0,0)\) |
| 10 | \((2,1,4,4,2)\) | \((1,3,1,0,0)\) |
| 11 | \((4,1,0,2,3)\) | \((1,3,1,0,0)\) |
| 12 | \((4,1,2,2,4)\) | \((1,3,1,0,0)\) |

## Assumptions and scope
A letter is a total map from the state set to itself. Its rank is the size of its image. A binary automaton is excluded when both letters are permutations, because a purely permutation automaton is nonsynchronizing for the trivial reason that every generated map is bijective.

An equivalence relation is a congruence exactly when it is preserved by each generator. Therefore an automaton is primitive exactly when the two letter maps have no common preserved nontrivial state partition.

The classification is for ordered labeled transition pairs before quotienting. The final isomorphism action simultaneously relabels all states and also allows exchange of the two letters.

## Proof
For \(n\) states, enumerate every ordered pair of total maps. For \(n=2,3,4,5\), this gives respectively \(2^4\), \(3^6\), \(4^8\), and \(5^{10}\) ordered binary automata.

For each automaton, first discard the case in which both maps are permutations. Next enumerate every set partition of the state set. A partition is preserved by a map when equivalent states always have equivalent images. The automaton is primitive if and only if none of the nontrivial partitions is preserved by both maps. This criterion is exhaustive because every congruence is itself such a partition, and preservation by the generators is equivalent to preservation by the whole transition monoid.

For each primitive candidate, run breadth-first search in the nonempty subset automaton from the full state set. A singleton is reached if and only if the automaton is synchronizing. The counts of primitive nonsynchronizing nonpermutation automata are
\[
0,\quad0,\quad0,\quad2880
\]
for \(n=2,3,4,5\), respectively. Hence five states is minimal.

Every accepted five-state automaton is independently rechecked for primitivity by generating the least congruence containing each unordered pair of distinct states; primitivity requires every such generated congruence to be universal. Nonsynchronizability is independently rechecked through pair compressibility: a complete automaton is synchronizing exactly when every pair of states can be compressed.

For classification, each of the \(2880\) five-state automata is transformed by all \(5!\) state relabelings and by both letter orders, and the lexicographically least encoded pair is used as a canonical key. Exactly \(12\) keys occur. Each key occurs for exactly \(240\) labeled ordered pairs, so every class has the full orbit size. Rank counting gives \(1920\) labeled automata, or eight classes, of type \((3,3)\), and \(960\) labeled automata, or four classes, with ranks \(3\) and \(5\).

## Verification
Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The verifier regenerates the complete enumeration for \(n=2,3,4,5\), the state partitions, subset-automaton reachability, the twelve canonical classes, all orbit sizes, and the rank split. On every accepted five-state automaton it also performs the independent generated-congruence and pair-compressibility checks described above.

The expected successful output begins with `VERIFY_OK n2=0 n3=0 n4=0 n5_labeled=2880 classes=12`.

## Relationship to prior work
Rystsov and Szykuła explicitly show that the deficiency restriction in their synchronization criteria is essential: their Figure 2 gives primitive nonsynchronizing automata on five states once a deficiency-\(2\) letter is admitted, and the left-hand example is binary. Their Example 7 proves primitivity and nonsynchronizability of the displayed counterexamples. Their experimental Table 1 verifies proposed synchronization conjectures for restricted letter types, but it does not enumerate all five-state binary primitive nonsynchronizing automata.

Volkov independently proves that a primitive automaton is synchronizing whenever it has a letter of defect \(1\), or more generally a word of rank \(2\). He also discusses the same five-state defect-\(2\) counterexamples. These results explain why defect \(2\) is the first structurally relevant boundary, but they do not imply the minimal-state census, the count \(2880\), or the twelve isomorphism classes.

Targeted searches for five-state binary primitive nonsynchronizing automata, smallest counterexamples, defect-\(2\) examples, and equality classifications located the above sources and related synchronization censuses, but no published complete twelve-class census.

## Limitations
The result is finite and specific to a binary alphabet. It does not classify primitive nonsynchronizing automata with larger alphabets or more than five states.

The classification excludes automata whose letters are both permutations; those are nonsynchronizing for a different, purely group-theoretic reason. Unpublished enumeration data associated with earlier computational experiments could contain the same five-state filtered census even though the inspected publications do not report it.

## References
1. M. V. Volkov, “Synchronization of Primitive Automata,” arXiv:2306.13317v1, first public version 2023-06-23; RAIRO-Theoretical Informatics and Applications 58 (2024), Article 3, DOI 10.1051/ita/2024003.
2. I. Rystsov and M. Szykuła, “Primitive Automata that are Synchronizing,” arXiv:2307.01302v1, first public version 2023-07-03.
