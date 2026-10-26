# Exactly two rank-four theories of nontrivial Steiner designs in point-collinearity language
## Finding
Let \(\mathcal D=(V,\mathcal B)\) be a finite nontrivial Steiner \(2\)-design with parameters \(2\text{-}(v,k,1)\), where \(3\le k<v\): every block has \(k\) points and every pair of distinct points lies on exactly one block. In the one-sorted signature consisting of equality and the ternary relation
\[
R(a,b,c)\quad\Longleftrightarrow\quad
 a,b,c\text{ are pairwise distinct and lie on one block},
\]
write \(\mathbf C(\mathcal D)=(V,R)\) for its point-collinearity structure. Then, for arbitrary such designs \(\mathcal D\) and \(\mathcal D'\) with respective block sizes \(k,k'\),
\[
\mathbf C(\mathcal D)\equiv_4\mathbf C(\mathcal D')
\quad\Longleftrightarrow\quad
(k=3\Longleftrightarrow k'=3).
\]
In particular, there are exactly **two** rank-four first-order theories across all finite nontrivial Steiner \(2\)-designs, and all these point structures are equivalent at rank at most three. Rank four is the first level at which any two members can be separated.

## Assumptions and scope
Here a nontrivial Steiner \(2\)-design has \(3\le k<v\) and distinct blocks; the point set is nonempty. It is not assumed that the design is affine, projective, symmetric, resolvable, Desarguesian, or homogeneous. The sole nonlogical relation is **irreflexive** collinearity of three *distinct* points, not a binary quasigroup operation and not a separate sort for lines. Quantifier rank is the maximum nesting depth of first-order quantifiers; \(\equiv_q\) denotes equality of all first-order sentences of rank at most \(q\). There is no restriction on the number of variables in a sentence other than its quantifier rank.

## Proof
**1. The numerical reservoir bound.** Set \(b=|\mathcal B|\). Each point belongs to \(r=(v-1)/(k-1)>1\) blocks, and \(b=v(v-1)/(k(k-1))\). Let \(N\) be the point-by-block incidence matrix. By unique pair incidence, \(NN^{\mathsf T}=(r-1)I+J\). The right-hand matrix is nonsingular over the reals because \(r>1\). Thus \(\operatorname{rank}N=v\le b\), and hence
\[
v\ge k(k-1)+1.
\]
This proves the required instance of Fisher's inequality directly, without an assumption about a particular design's order.

**2. All four-point extension patterns.** Take any ordered triple of previously chosen points. If some points repeat, each fresh point creates a fixed equality pattern, and whether the selected distinct points lie on a block is determined by the unique-pair axiom; the same patterns exist in every design under consideration. For three distinct chosen points \(a,b,c\), the possible *fresh* fourth points are as follows.

If \(a,b,c\) are collinear, all three pair-lines coincide. Exactly \(k-3\) remaining points lie on that line; such a point gives all three ternary incidences \(R(a,b,z)\), \(R(a,c,z)\), and \(R(b,c,z)\). The remaining \(v-k>0\) points lie off the line and give none. The first class exists exactly when \(k\ge4\), and the second always exists.

If \(a,b,c\) are not collinear, the three distinct lines through the pairs intersect one another only at the corresponding chosen points. Each pair-line contributes exactly \(k-2>0\) fresh points; these realize, separately, precisely one of the three possible pair incidences. Every point outside the union of these three lines realizes none. The number of such outside points is
\[
v-3-3(k-2)=v-3k+3\ \ge\ (k-2)^2>0.
\]
Consequently, for an ordered triple the set of possible **atomic** four-tuple types of its extensions is completely determined by the equality-and-collinearity atomic type of the triple together with the single bit \(k=3\) versus \(k\ge4\). Reusing a previously chosen point produces the forced corresponding equality type. No incidence patterns have been omitted.

**3. Four-round back-and-forth.** Consider two designs on the same side of that block-size dichotomy. In a four-round Ehrenfeucht–Fraïssé game, the second player matches the atomic type of the growing ordered tuple. With three choices already made, part 2 guarantees a matching fourth response in either direction. With at most two choices already made, all atomic extensions to three points exist in both designs: a distinct pair has a third point on its unique line (\(k-2\ge1\)) and another off that line (\(v-k>0\)); repetitions are matched by equality. Each possible three-point atomic type has exactly the same future four-point extension inventory in both designs. The same downward induction applies from one or zero choices. Hence the second player wins all four rounds, proving equivalence at rank four. This argument applies to arbitrary sequences of moves, including repeated selections and moves alternating between the two structures.

**4. Sharpness and the number of theories.** All members share the same atomic extension patterns through triples, so the preceding argument truncated one round shows that every two members are rank-three equivalent. The first-order sentence
\[
\exists a\,\exists b\,\exists c\,\exists d\;
\bigl(\mathrm{Distinct}(a,b,c,d)\wedge R(a,b,c)\wedge R(a,b,d)\bigr),
\]
where \(\mathrm{Distinct}\) abbreviates the quantifier-free conjunction of the six pairwise inequalities, has quantifier rank four. It holds precisely when \(k\ge4\), because uniqueness of the block through \(a,b\) makes both triple relations refer to the same block. Both cases occur: the Fano plane \(2\text{-}(7,3,1)\) has \(k=3\), and the projective plane of order three \(2\text{-}(13,4,1)\) has \(k=4\). Therefore there are exactly two equivalence classes, and the separation depth four is optimal.

## Verification
The self-contained program `verify_collinearity.py` builds five finite Steiner designs: the Fano projective plane (\(v=7,k=3\)), the ternary affine plane (\(v=9,k=3\)), the ternary projective plane (\(v=13,k=4\)), the four-symbol affine plane (\(v=16,k=4\)), and the four-symbol projective plane (\(v=21,k=5\)). It independently checks every pair's unique block, constructs exact rank-four Hintikka profiles by recursive extension of ordered tuples, and separately enumerates every three-point set's fourth-point incidence options. The recorded output `verification_output.txt` reports two rank-four profiles and ends in `VERIFY_OK`. These checks test representative finite designs; the infinite all-design assertion is proved by the incidence-matrix and extension-inventory arguments above, not by finite testing.

## Relationship to prior work
Fisher's classical incidence-matrix inequality provides the essential numerical lower bound on point count; it does not concern logical rank. Linial and Luria study entropy bounds on the number of Steiner triple systems, not bounded-rank equivalence of point-collinearity structures. Barbina and Casanovas develop model theory for Steiner triple systems and their quasigroup language, principally infinite structures and model completion, without providing this rank-four classification for finite designs of *variable* block size. Paolini and Quadrellaro study free/open (nondegenerate infinite) incidence structures, not the finite designs in the one-sorted ternary point language. Previous low-rank incidence or counting-logic results in *different signatures* do not imply the present four-round classification merely by naming similar geometries: the translation of point collinearity through a block sort increases logical resources and its converse is not quantifier-free. These comparisons do not establish absolute novelty beyond the examined sources.

## Limitations
The result is only about first-order quantifier rank at most four and the stated one-sorted point-collinearity reduct. It makes no claim about rank five, counting logic, other languages, partial designs, or systems with varying block sizes *inside one design*. The result is not an isomorphism classification, and does not determine individual orders or block parameters. No independent scientific audit or external validation of the result has been performed. Published or unindexed literature may contain equivalent observations despite the documented comparisons.

## References
1. R. A. Fisher, "An examination of the different possible solutions of a problem in incomplete blocks," *Annals of Eugenics* 10 (1940), 52–75, DOI: `10.1111/j.1469-1809.1940.tb02237.x`. Publisher metadata gives January 1940, not an exact release day.
2. N. Linial and Z. Luria, "An Upper bound on the number of Steiner triple systems," arXiv:`1108.5042`, first posted 25 August 2011. https://arxiv.org/abs/1108.5042
3. S. Barbina and E. Casanovas, "Model theory of Steiner triple systems," arXiv:`1805.06767`, first posted 17 May 2018. https://arxiv.org/abs/1805.06767
4. G. Paolini and D. E. Quadrellaro, "On the Model Theory of Open Incidence Structures: The Rank 2 Case," arXiv:`2411.10792`, first posted 16 November 2024. https://arxiv.org/abs/2411.10792
5. P. J. Cameron, "Infinite linear spaces," *Discrete Mathematics* 129 (1994), 29–41.
