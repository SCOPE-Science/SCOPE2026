# Twenty symbol-isomorphism classes of four-symbol shorthand universal cycles

## Finding

Let \(\Sigma=\{0,1,2,3\}\). An *oriented shorthand universal cycle* is a circular word of length \(24\) over \(\Sigma\) in which the \(24\) cyclic factors of length \(3\) are precisely the \(24\) ordered triples of distinct letters, each exactly once. Circular rotations are already identified, but letter relabelings and reversal are initially distinguished. Let \(\mathcal U\) denote these rotation classes. The symmetric group \(S_4\) acts on \(\mathcal U\) by globally permuting letters, and an additional involution \(R\) reverses the circular word.

**Exact isomorphism and mirror classification.** There are \(|\mathcal U|=384\) labeled rotation classes, and
\[
\boxed{|\mathcal U/S_4|=20,\qquad |\mathcal U/(S_4\times\langle R\rangle)|=11.}
\]
Of the twenty relabeling classes, twelve contain \(24\) labeled rotation classes and eight contain \(12\). The latter eight have an alphabet-transposition stabilizer of order \(2\); no other nonidentity alphabet permutation stabilizes a cycle. Under relabeling and reversal together, six orbits have size \(24\) and five have size \(48\). Exactly two of the twenty relabeling classes are self-mirror; the other eighteen occur in nine mirror pairs.

The full fixed-point census is below. Each entry counts labeled **rotation classes** fixed by one permutation of the indicated cycle type; the second numerical column incorporates reversal.

| Cycle type in \(S_4\) | Number of permutations | Fixed by relabeling | Fixed by relabeling followed by reversal |
|---|---:|---:|---:|
| \((1,1,1,1)\) | 1 | 384 | 0 |
| \((2,1,1)\) | 6 | 16 | 0 |
| \((2,2)\) | 3 | 0 | 16 |
| \((3,1)\) | 8 | 0 | 0 |
| \((4)\) | 6 | 0 | 0 |

The accompanying `classes.tsv` is a complete canonical representative list for the twenty relabeling classes, giving each representative, its labeled orbit size, and the index of its reversal partner.

## Assumptions and scope

The alphabet is exactly the four individually labeled symbols \(0,1,2,3\), and every allowed cyclic window has length three and consists of three distinct symbols. Every cycle has exactly \(24\) positions. Rotations act on positions; \(S_4\) acts uniformly on all symbols; reversal reverses the cyclic ordering, without complementing or changing the letters otherwise. The two actions commute. The two quotient counts are different equivalence relations, not two alternative normalizations of a single quantity. Nothing is asserted for longer windows, larger alphabets, or arbitrary permutation families.

## Proof

**1. Euler-tour bijection.** Form the directed graph with \(12\) vertices \((a,b)\), where \(a\ne b\), and \(24\) arcs \((a,b,c):(a,b)\to(b,c)\), where \(a,b,c\) are pairwise distinct. Each vertex has indegree and outdegree \(2\). A closed tour using all arcs once spells exactly one shorthand universal cycle. Conversely every such circular word determines the tour by its consecutive triples. Every cycle contains the arc \((0,1,2)\) exactly once, so there is a unique oriented tour *anchored* at that arc for each rotation class.

**2. Finite exhaustive generation with an independent last-exit check.** A depth-first search starts with arc \((0,1,2)\), repeatedly takes an unused outgoing arc, and accepts exactly those \(24\)-arc trails that return to vertex \((0,1)\). A \(24\)-bit mask records used arcs. Every Euler tour anchored at that arc occurs in precisely one branch; hence the accepted output is a complete census, not a sample. It contains \(384\) distinct cycles.

An independent enumeration uses the directed last-exit form of the BEST correspondence. Fix the root vertex \((0,1)\) and the order of its departures, beginning with \((0,1,2)\). At each of the other eleven vertices choose one of its two outgoing arcs as its last exit. Such a choice is valid exactly when following the chosen arcs from every nonroot vertex eventually reaches \((0,1)\): those arcs form an in-arborescence rooted there. Each valid assignment uniquely determines an Euler tour, with the other outgoing arc used first. The complete finite space has \(2^{11}=2048\) assignments; exactly \(384\) pass the reachability criterion. All \(384\) reconstructed tours coincide with the depth-first-search collection. This is also consistent with the \(12\)-vertex directed Laplacian cofactor \(384\) and the known labeled enumeration [1].

**3. Exact fixed-point classification.** For a valid cycle \(c\), define \(N(c)\) as its unique rotation beginning with the triple \((0,1,2)\). For any alphabet permutation \(\sigma\) and exponent \(\epsilon\in\{0,1\}\), the induced action on anchored words is
\[
 c\longmapsto N\bigl(\sigma(R^{\epsilon}c)\bigr).
\]
It is therefore enough to test equality with \(c\) among the explicitly exhaustively generated \(384\) anchored words. Exhausting the \(24\) permutations and both reversal choices gives exactly the five conjugacy-class rows in the Finding table. The `verify.py` program implements both independently complete tour enumerations, all \(48\) group actions and all fixed-point equalities, and regenerates the complete representative table `classes.tsv`. No untested objects remain at this alphabet size.

**4. Burnside and orbit-stabilizer.** Burnside's lemma applied to the \(24\)-element relabeling group yields
\[
 \frac{384+6\cdot16}{24}=20.
\]
Its application to the \(48\)-element commuting relabeling-and-reversal group yields
\[
 \frac{384+6\cdot16+3\cdot16}{48}=11.
\]
For the first action, the fixed-point census shows that the only possible nonidentity stabilizer consists of a single transposition. A stabilizer cannot contain two different transpositions: their product is a nonidentity permutation of one of the other listed cycle types, none of which fixes a cycle. Exactly \(6\cdot16=96\) labeled cycles therefore have stabilizer order \(2\); they form \(96/12=8\) orbits of size \(12\). The other \(288\) labeled cycles form \(288/24=12\) orbits of size \(24\). Direct canonical quotient enumeration gives six joint orbits of size \(24\) and five of size \(48\). Two relabeling orbits are invariant under the reversal action, leaving nine paired orbits, as recorded in `classes.tsv`.

## Verification

Run `python3 verify.py` next to `classes.tsv`, using only the Python standard library. The program independently regenerates the canonical collection with two complete methods, asserts both sets are identical, checks all \(48\) transformations of every cycle, recomputes every fixed-point count and orbit size, and compares the full canonical representative table byte for byte with `classes.tsv`. The observed output begins with `VERIFY_OK` and reports the counts \(2048\), \(384\), \(20\), and \(11\). The finite space is completely enumerated at the stated four-letter alphabet; the proof does not extrapolate this census to other alphabet sizes.

## Relationship to prior work

Chang and Xue [1] give a general exact **labeled** count for universal cycles of injective triples; its specialization to four symbols is \(384\). Knowing this total does not determine the quotient counts, since the relabeling action is nonfree: eight classes have a transposition stabilizer. Holroyd, Ruskey and Williams [2] identify these shorthand cycles with permutation Gray codes and study weights, extremal families and constructions; their cited characterizations do not compute this complete \(S_4\)-stabilizer and mirror-orbit profile. Chang, Wang and Xue [3] extend labeled enumeration to four-letter injective windows, which are a different window length and do not yield the present group-fixed-point data. This result adds the complete isomorphism and reversal classification for the first nontrivial four-symbol shorthand case rather than reasserting the established labeled total.

## Limitations

The classification is an exact finite one for four alphabet symbols; there is no infinite-family classification or asymptotic estimate. The exhaustive certificate is a proof of the stated finite enumeration because the anchoring and directed-tour bijections account for every admissible word, not because random tests suggest the counts. The known labeled value \(384\) is not claimed to be new. Publicly indexed literature and related exact tables were compared, but an unindexed prior classification of the same symmetry quotients cannot be excluded. An independent mathematical audit has not yet been performed.

## References

[1] Z. Chang and J. Xue, *Enumerations of Universal Cycles for \(k\)-Permutations*, first posted November 27, 2021, https://arxiv.org/abs/2111.13814 , Theorem 1.3 and Section 3.

[2] A. E. Holroyd, F. Ruskey and A. Williams, *Shorthand Universal Cycles for Permutations*, *Algorithmica* 64 (2012), 215–245, https://doi.org/10.1007/s00453-011-9544-z , particularly Sections 1–3.

[3] Z. Chang, Q. Wang and J. Xue, *An effective approach to enumerate universal cycles for \(k\)-permutations*, SETA 2024 pre-proceedings, pp. 1–3 of that paper, https://seta-2024.github.io/files/Pre-proceedings.pdf , Theorems 5–6.
