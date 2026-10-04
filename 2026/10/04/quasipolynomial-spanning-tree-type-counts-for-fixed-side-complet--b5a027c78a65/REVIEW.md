# Same-model review

## Correctness
PASS. For \(m>d\), the smaller bipartition class of every spanning tree is intrinsic, so deleting precisely the leaves in the larger class is isomorphism-invariant and yields a uniquely recoverable core. The identity \(\sum_{v\notin A}(\deg(v)-1)=d-1\) bounds the core by \(d-1\) large-side vertices. Conversely every core plus a weak composition of the remaining leaves gives a spanning tree, and isomorphism classes for a fixed core are exactly automorphism orbits of those weak compositions. The core action on the \(d\)-side is faithful because two distinct degree-at-least-two vertices with the same neighbourhood would create a four-cycle. Burnside's lemma therefore gives the stated exact generating function. Root-of-unity poles give quasipolynomiality, and the identity permutation gives the unique pole order \(d\); orbit-stabilizer combined with Yan--Zhang's labelled-core count yields the stated leading coefficient. The checker supplies independent finite stress tests but is not used as an infinite proof.

## Originality
PASS. The closest 2026 primary source, Yan--Zhang, proves only the fixed-\(d\) asymptotic and explicitly treats repeated-coordinate leaf vectors as an \(O_d(m^{d-2})\) error; the exact stabilizer/orbit contribution is not stated there. Johnson--Nochumson give lower and upper bounds rather than exact fixed-side enumeration. Targeted searches for quasipolynomial, Burnside, rational-generating-function, and fixed-side formulations found no general theorem matching the claim. Historical material does contain exact formulas for \(d=2,3,4\), so those are treated as covered special cases rather than novelty evidence. The uninspected 2008 Mohr thesis is retained as a specific archival risk, not ignored.

## Value
PASS. The result upgrades the precise asymptotic baseline used in a new extremal theorem to an exact computable structure for every fixed side size. It explains why residue-class formulas appear in the older \(d=2,3,4\) cases, supplies a uniform finite algorithm through core automorphism groups, and recovers the recent leading constant exactly. This is a structural enumeration theorem rather than a routine finite extension or arbitrary parameter slice.

## Closest literature and limitations
The nearest result is Proposition 5.1 of Yan--Zhang (2026), whose core decomposition gives the same finite structural objects but stops at asymptotic orbit counting. Johnson--Nochumson (2026) provide general bounds. Van den Boomen (2009) gives the exact \(K_{4,t}\) formula and reports Mohr's exact \(K_{2,t}\) and \(K_{3,t}\) formulas. The theorem here is restricted to \(m>d\), gives only a period divisibility bound, and does not claim a simplified closed residue-class expression for general \(d\).

Same-model review: passed. Independent audit: not yet performed.
