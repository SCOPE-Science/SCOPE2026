# Exact hypercube height and width for complete height-two posets \(P_{a,b}\)

## Finding

Let \(P_{a,b}\) be the finite height-two poset with \(a\ge2\) minimal elements and \(b\ge2\) maximal elements, every minimal element below every maximal element, and no comparabilities within either level. Define

\[\mu(a)=\min\left\{u\ge2:\binom{u}{\lfloor u/2\rfloor}\ge a\right\}.\]

The exact hypercube invariants are

\[h^*(P_{a,b})=\mu(a)+1,\qquad w^*(P_{a,b})=\mu(a)+b.\]

Here \(h^*(P)\) is the least rank bound \(h\) for which some Boolean lattice contains an induced copy of \(P\) using only sets of size at most \(h\); \(w^*(P)\) is the least ground-set size at that optimal rank bound. In particular, \(w^*(P_{a,b})=|P_{a,b}|\) precisely for \(a\in\{2,3,4\}\) in this family.

## Assumptions and scope

All posets are finite. The order relation is set inclusion in a Boolean lattice, and copies are induced: two chosen sets are comparable exactly when the corresponding poset elements are comparable. The parameters satisfy \(a,b\ge2\); one-level cases are not included. Write \([u]=\{1,\ldots,u\}\) and \(\binom{[u]}{\le h}\) for the sets of size at most \(h\).

## Proof

Put \(u=\mu(a)\). Consider any induced embedding of \(P_{a,b}\) into a Boolean lattice whose chosen sets have size at most \(h\). Let the lower-level sets be \(B_1,\ldots,B_a\), the upper-level sets be \(T_1,\ldots,T_b\), and let \(U=\bigcup_{i=1}^a B_i\), with \(s=|U|\).

The sets \(B_i\) form an antichain. Since \(a\ge2\), none is empty and none equals \(U\): either case would make it comparable with every other lower-level set. Sperner's theorem applied to the ground set \(U\) gives \(a\le\binom{s}{\lfloor s/2\rfloor}\), so \(s\ge\mu(a)=u\). Every \(T_j\) contains \(U\). Because \(b\ge2\) and the \(T_j\) form an antichain, no \(T_j\) can equal \(U\); hence each has at least one element outside \(U\). Thus \(h\ge s+1\ge u+1\).

For the matching construction, minimality of \(u\) implies \(a>\binom{u-1}{\lfloor (u-1)/2\rfloor}\). Choose any \(a\) members of the middle layer of \(2^{[u]}\). They form an antichain by equal cardinality. Their union is all of \([u]\): if they omitted a coordinate, they would form an antichain of size greater than \(\binom{u-1}{\lfloor (u-1)/2\rfloor}\) on the remaining \(u-1\) coordinates, contradicting Sperner's theorem. Call these sets \(B_1,\ldots,B_a\). Add \(b\) new coordinates and set \(T_j=[u]\cup\{u+j\}\) for \(1\le j\le b\). Each \(T_j\) has size \(u+1\); the upper-level sets are pairwise incomparable, and every \(B_i\) is a proper subset of every \(T_j\). This is an induced copy, proving \(h^*(P_{a,b})=u+1\).

Now restrict the ground-set size to \(w^*(P_{a,b})\) while keeping the rank bound \(u+1\). In any such embedding, the union of the lower-level sets has size at least \(u\), and every upper-level set strictly contains that union. Since no chosen set can exceed size \(u+1\), the union must have size exactly \(u\), and every upper-level set is that union plus one new coordinate. The \(b\) upper-level sets need distinct new coordinates, so \(w^*(P_{a,b})\ge u+b\). The construction above uses exactly \(u+b\) coordinates, giving equality.

Finally, \(\mu(2)=2\), \(\mu(3)=3\), and \(\mu(4)=4\). For every \(a\ge5\), the central binomial coefficient \(\binom{a-1}{\lfloor(a-1)/2\rfloor}\ge a\), so \(\mu(a)\le a-1\). Therefore \(\mu(a)=a\) exactly when \(a\in\{2,3,4\}\), proving the stated equality criterion.

## Verification

The lower bound follows from Sperner's theorem and the fact that all upper-level sets must properly contain the union of the lower-level sets. The construction realizes the lower bound for height and width. The equality criterion follows from the definition of \(\mu\) and the central-binomial inequality above. No computation or finite search is used as a substitute for the proof.

## Relationship to prior work

Flídr, Ivan, and Jaffe define hypercube-height and hypercube-width, prove the general bound \(w^*(P)\le |P|\), and explicitly ask which posets attain equality (Question 8). The formula here evaluates both invariants for the natural complete height-two family \(P_{a,b}\); it does not purport to classify equality for arbitrary posets. The proof uses the classical antichain bound of Sperner.

## Limitations

The result is limited to complete height-two posets with at least two elements in each level. It does not characterize \(w^*(P)=|P|\) for general finite posets, and it does not cover cases with a singleton level. The literature search did not establish global novelty; the closest source itself notes that other equality examples are easy to construct, so the contribution claimed here is the uniform exact formula for this full family, not the existence of isolated equality examples.

## References

1. T. Flídr, M.-R. Ivan, and S. Jaffe, *Optimal Embeddings of Posets in Hypercubes*, arXiv:2509.26630v1, first public 2025-09-30. Relevant material: definitions of \(h^*\) and \(w^*\), the two-layered-poset argument, Theorem 4, and Question 8.
2. E. Sperner, *Ein Satz über Untermengen einer endlichen Menge*, Mathematische Zeitschrift 27 (1928), 544–548.
