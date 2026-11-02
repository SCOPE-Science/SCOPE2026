# Three-variable collapse and sharp deletion boundary for finite Steiner triple systems
## Finding
Let \(S=(V,\mathcal B)\) range over **all finite Steiner triple systems of order \(v\ge7\)**, without a coordinatization or transitivity assumption. Write \(S^-_p\) for the induced point-only ternary relational structure on \(V\setminus\{p\}\), for an arbitrary point \(p\in V\); its predicate \(R(x,y,z)\) holds exactly when \(\{x,y,z\}\in\mathcal B\), so it is symmetric and false whenever two arguments coincide. Also write \(S\) for the unpunctured relational structure with the same predicate.

In ordinary **counting-free first-order logic with at most three reusable variables and no quantifier-depth restriction**, there are exactly two theories among the entire union of these families:

\[
S\equiv_{\mathrm{FO}^{3}}T,\qquad
S^-_p\equiv_{\mathrm{FO}^{3}}T^-_q,\qquad
S\not\equiv_{\mathrm{FO}^{3}}T^-_q
\]

for every two eligible Steiner triple systems \(S,T\) and all deleted points \(p,q\). In contrast, all the complete and punctured structures are equivalent in \(\mathrm{FO}^{2}\) (and therefore also in \(\mathrm{FO}^{1}\)). The three-variable separation between the two classes is sharp.

The collapse of the punctured class has a **sharp four-variable boundary**: for any puncture of an order-seven Steiner triple system and any puncture of an order-at-least-nine Steiner triple system, the resulting structures are \(\mathrm{FO}^{3}\)-equivalent but \(\mathrm{FO}^{4}\)-inequivalent. A single four-variable sentence, defined explicitly below, distinguishes them uniformly. No classification of all \(\mathrm{FO}^{4}\) theories is asserted.

## Assumptions and scope
A Steiner triple system is a finite set \(V\) with three-element blocks such that every distinct pair of points lies in exactly one block. Here \(v\ge7\), so the degenerate order-three case is excluded. The admissible orders are congruent to one or three modulo six. The predicate \(R\) records only blocks on three **distinct** points. No point is named, including the deleted point; there are no sort predicates, functions, constants, counting quantifiers, or extra relations. The full and punctured structures use the same signature \(\{R,=\}\).

For a punctured system on \(N=v-1\) points, define the (unoriented) **leave relation** by
\[
M(a,b)\iff a\ne b\ \land\ \neg\exists z\,R(a,b,z).
\]
Because every pair of the original Steiner triple system has a unique completion, the pairs missing after deleting \(p\) are exactly the pairs whose former completion was \(p\). These pairs form a perfect matching on the \(N\) surviving points. Denote the matching mate of \(a\) by \(m(a)\).

## Proof
**1. Complete-system three-pebble strategy.** In an unpunctured system, if two distinct anchors \(a,b\) are fixed, a third point \(z\) has one of four atomic types: \(z=a\), \(z=b\), \(z=c(a,b)\) (the unique block-completing point), or a further point not completing the block. The respective multiplicities are \(1,1,1,v-3\). If the anchors coincide, the types are equality and inequality, with multiplicities \(1,v-1\). All listed types exist for every \(v\ge7\). Hence Duplicator can indefinitely preserve equality and the ternary block relation with three pebbles between any two unpunctured systems. The standard infinite three-pebble game characterizes equivalence for all counting-free \(\mathrm{FO}^{3}\) sentences, with no depth bound.

**2. Punctured-system extension lemma.** In a punctured system, classify any two fixed anchors using equality and the matching \(M\). If \(a=b\), then \(z\) can be \(a\), \(m(a)\), or any of the \(N-2\) other points. If \(a\ne b\) and \(M(a,b)\), then \(z\) can equal \(a\), equal \(b\), or be one of the \(N-2\) remaining points. If \(a\ne b\) and \(\neg M(a,b)\), there are exactly six categories:

\[
\begin{array}{c|c}
\text{category}&\text{multiplicity}\\\hline
z=a&1\\
z=b&1\\
z=m(a)&1\\
z=m(b)&1\\
R(a,b,z)&1\\
\text{none of these}&N-5=v-6.
\end{array}
\]

The five named points are pairwise distinct: the block completion \(c(a,b)\) cannot be \(m(a)\) or \(m(b)\), because a matching pair has no surviving block. Since \(N\ge6\), every displayed category is nonempty. The classification is independent of the original design and of the deleted point.

**3. Permanent strategy for punctures.** Maintain, among up to three pebbled points, their equalities, all pairwise matching facts \(M\), and the ternary block facts \(R\). When Spoiler moves one pebble, at most two anchors remain. The extension lemma supplies a responding point in the other structure realizing precisely the required equality, matching, and block pattern. This also covers repeated anchors and replaying an occupied point. Because the invariant is reestablished after **every** move, Duplicator wins arbitrarily long games. In particular, all punctures are equivalent in unrestricted-depth \(\mathrm{FO}^{3}\).

**4. Sharp three-variable distinction.** The sentence
\[
\exists x\,\exists y\,\bigl(x\ne y\ \land\ \neg\exists z\,R(x,y,z)\bigr)
\]
asserts that a pair has no block completion. It is false in every full Steiner triple system and true in every puncture. On the other hand, an atomic occurrence of \(R\) involving at most two variable symbols necessarily repeats one of them and is therefore false. Thus the \(\mathrm{FO}^{2}\) fragment reduces here to pure equality; all domains have at least six points and hence satisfy the same two-variable equality theory. The distinction first appears at width three.

**5. A sharp four-variable distinction between punctures.** For distinct anchors \(x,y\) with a surviving block completion, call \(z\) *free* when \(z\) is neither anchor, is not the completion of \(x,y\), and is not the matching mate of either anchor. The following formula expresses this with only the variable symbols \(x,y,z,w\):
\[
\begin{aligned}
F_{x,y}(z):={}& z\ne x\land z\ne y\land\neg R(x,y,z)\\
&\land(\exists w\,R(x,z,w))\land(\exists w\,R(y,z,w)).
\end{aligned}
\]

The analogous \(F_{x,y}(w)\) is written using the locally bound \(z\) in each of its two existential completion tests; these local bindings may shadow the other outer witness. Consequently the following is a bona fide formula using at most four reusable variables, after the displayed abbreviations are expanded:
\[
\begin{aligned}
\Phi:=\exists x\,\exists y\bigl(&x\ne y\land(\exists z\,R(x,y,z))\\
 &\land\exists z\,\exists w\,(z\ne w\land F_{x,y}(z)\land F_{x,y}(w))\bigr).
\end{aligned}
\]

For any completed anchor pair, precisely \(N-5=v-6\) points satisfy \(F_{x,y}\). Thus \(\Phi\) is false on every puncture of \(v=7\) (one free point), and true on every puncture of \(v\ge9\) (at least three free points). Every puncture of \(v\ge7\) contains completed pairs: for each point there is only one missing mate, and \(N\ge6\). This proves the four-variable separation. Since Step 3 shows equivalence at width three, the width four is minimal.

## Verification
Two standalone programs are included. `punctured_verify.py` independently constructs order-seven (binary projective), order-nine (ternary affine), cyclic order-thirteen, and binary projective order-fifteen Steiner triple systems. It checks exact Steiner pair coverage, forms one puncture per system, enumerates all third-point extension types, and performs noncounting three-variable fixed-point refinement on all eight complete and punctured relational structures. At stabilization the four full structures have a common empty-position type and the four punctures another common, distinct type. It also verifies the four-variable free-witness threshold on every tested puncture.

`deletion_extension_verify.py` builds the same four parent families independently, then deletes **every** point and checks all extension multiplicities directly. This checks \(44\) point-deleted structures, \(5{,}640\) ordered anchor pairs and \(69{,}744\) third-point choices; every expected extension class and the four-variable threshold passes. Each script runs with Python's standard library alone. Their recorded outputs accompany them, and the results can be reproduced with `python3 punctured_verify.py` and `python3 deletion_extension_verify.py`.

The finite calculations are cross-checks. The universal theorem follows from Steps 1–5, not extrapolation from the tested orders.

## Relationship to prior work
Andersen, Hilton, and Mendelsohn (1980) analyze embeddings of partial Steiner triple systems and explicitly use their missing-edge (leave) graphs, but their verified published abstract concerns embedding bounds and equitable partial systems rather than finite-variable theories. Barbina and Casanovas (arXiv:1805.06767) give a model-theoretic treatment of Steiner triple systems and their functional quasigroups; their model-completion and quantifier-elimination results concern the generic infinite functional setting, not a common unrestricted three-variable theory of finite point-deleted relational systems. The inspected text explicitly distinguishes functional and relational signatures. Grohe and Otto (arXiv:1204.1990) provide general pebble-game techniques, not a Steiner-puncture classification.

The published result *Real-rooted one-point extension spectra of partial Steiner triple systems* studies the matching generating polynomial of the leave and its real-rootedness. Its full displayed theorem and proof concern **counts of induced one-point extensions**, not the all-depth \(\mathrm{FO}^{3}\) equivalence of **one-point deletions** or the four-variable separating sentence here. The earlier rank-five study *Four rank-five theories of nontrivial finite additive Steiner triple systems* treats unpunctured systems at bounded quantifier rank, not the point-deleted, unrestricted-depth variable-width statement.

Targeted searches for the point-deletion/leave-matching formulation, unrestricted three-variable theories, three-pebble equivalence, and four-variable separators identified no decisive published implication. Non-identification is not a proof of historical novelty; a broader characterization of partial Steiner systems under finite-variable logic might imply the result.

## Limitations
The theorem is restricted to the pure symmetric **irreflexive** ternary block predicate and finite Steiner triple systems of order at least seven. It says nothing about arbitrary partial Steiner triple systems, named deleted points, functional quasigroup terms, counting quantifiers, or the entire four-variable spectrum. The arXiv model-completion paper and the published one-point-extension result were inspected, but an unidentified equivalent formulation or inaccessible older literature remains a historical-priority risk. No independent mathematical audit has been performed.

## References
1. L. D. Andersen, A. J. W. Hilton, and E. Mendelsohn, *Embedding Partial Steiner Triple Systems*, Proceedings of the London Mathematical Society 41 (1980), 557–576. DOI: 10.1112/plms/s3-41.3.557 (published 1980-11-01).
2. Silvia Barbina and Enrique Casanovas, *Model theory of Steiner triple systems*, Journal of Mathematical Logic 20 (2020), 2050010; arXiv:1805.06767 (first arXiv version 2018-05-17).
3. Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (first version 2012-04-09).
4. Charles J. Colbourn, Jeffrey H. Dinitz, and Alexander Rosa, *Bicoloring Steiner Triple Systems*, Electronic Journal of Combinatorics 6 (1999), R25; DOI: 10.37236/1457.
5. *Real-rooted one-point extension spectra of partial Steiner triple systems*, published research result, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-real-rooted-one-point-extension-spectra-of-partial-steiner-tripl--9599713a6632/RESULT.md.
