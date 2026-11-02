# Matroid basis concepts have equal static and adaptive shattering dimensions

## Finding
Let \(M=(E,\mathcal I)\) be any finite matroid, including matroids with loops and coloops, and let \(r\) be its rank function. Write \(\mathcal B(M)\) for the Boolean concept class whose concepts are the incidence vectors of bases, queried at individual ground elements. Then
\[
\operatorname{Ldim}(\mathcal B(M))
=\operatorname{VCdim}(\mathcal B(M))
=\max\{|S|:S\in\mathcal I(M)\cap\mathcal I(M^*)\}
=\min_{A\subseteq E}\bigl(2r(A)+|E\setminus A|-r(E)\bigr).
\]
In particular, both dimensions can be computed by one ordinary matroid-intersection computation using the independence oracles of \(M\) and its dual.

There is a stronger root-choice conclusion. If an element \(e\in E\) is neither a loop nor a coloop, then an optimal complete shattered binary query tree can be chosen to ask whether \(e\) belongs to the basis at its root. This holds for **every** such \(e\), not merely for one specially selected query.

## Assumptions and scope
A matroid here is finite and specified by its hereditary, augmentable family of independent subsets of a ground set \(E\). The dual matroid \(M^*\) has complements of bases of \(M\) as its bases. A set \(S\subseteq E\) is independent in \(M^*\) exactly when \(E\setminus S\) contains a basis of \(M\). The VC dimension is the maximum cardinality of a support on which all binary assignments occur. The Littlestone dimension is the greatest depth of a complete binary query tree whose every root-to-leaf answer sequence is realized by a member of the concept class. A class with one concept has dimension zero by both definitions.

No representability over a field, simplicity, connectivity, nondegeneracy, or rank restriction is assumed. The statement also includes the empty-ground-set case. Queries are **individual element membership** questions; it does not claim results for arbitrary subset-intersection or independence-oracle queries.

## Proof
**Step 1: Characterization of shattered supports.** A support \(S\subseteq E\) is VC-shattered by \(\mathcal B(M)\) if and only if it is independent in both \(M\) and \(M^*\). Indeed, the all-positive labeling requires a basis containing \(S\), and thus independence in \(M\). The all-negative labeling requires a basis disjoint from \(S\), and thus independence in the dual. Conversely, if these two conditions hold, take any \(T\subseteq S\). Then \(T\) is independent and \(E\setminus S\) spans \(M\); consequently \(T\cup(E\setminus S)\) has full rank. The basis extension axiom extends \(T\) to a basis lying inside that union. Such a basis meets \(S\) exactly in \(T\), realizing the arbitrary labeling. Hence the VC dimension is the maximum cardinality of a common independent set of \(M\) and \(M^*\).

**Step 2: The rank minimum.** Edmonds' matroid intersection min-max theorem gives
\[
\nu(M):=\max\{|S|:S\in\mathcal I(M)\cap\mathcal I(M^*)\}
=\min_{A\subseteq E}\left(r_M(A)+r_{M^*}(E\setminus A)\right).
\]
The standard dual-rank identity is
\[
r_{M^*}(E\setminus A)=|E\setminus A|-r_M(E)+r_M(A).
\]
Substitution yields the stated rank minimum.

**Step 3: Deletion-contraction identity.** Let \(e\) be neither a loop nor a coloop, and put \(n=|E|\), \(r_0=r_M(E)\), and
\[
F_M(A)=2r_M(A)+n-|A|-r_0.
\]
For \(A\subseteq E\setminus\{e\}\), the deletion \(M\setminus e\) still has rank \(r_0\) and the contraction \(M/e\) has rank \(r_0-1\). Their rank functions satisfy \(r_{M\setminus e}(A)=r_M(A)\) and \(r_{M/e}(A)=r_M(A\cup\{e\})-1\). Applying Step 2 to each minor therefore gives
\[
\nu(M\setminus e)=\min_{A\not\ni e}F_M(A)-1,
\qquad
\nu(M/e)=\min_{A\ni e}F_M(A)-1.
\]
The two indexing families partition the power set of \(E\). Hence
\[
\boxed{\nu(M)=1+\min\{\nu(M\setminus e),\nu(M/e)\}.}
\]
This holds for **every** element with both membership answers possible.

**Step 4: Adaptive shattering.** For any finite nonempty concept class \(\mathcal C\) with at least two concepts, the complete-tree recurrence is
\[
\operatorname{Ldim}(\mathcal C)
=1+\max_{x:\,\mathcal C_{x=0},\mathcal C_{x=1}\ne\varnothing}
\min\{\operatorname{Ldim}(\mathcal C_{x=0}),\operatorname{Ldim}(\mathcal C_{x=1})\}.
\]
In a matroid basis concept class, a query on a nonloop, noncoloop element \(e\) splits the family precisely into bases of \(M\setminus e\) and bases of \(M/e\), after deleting the fixed queried coordinate. Loops and coloops give only constant answers and do not enter the maximum. We now induct on \(|E|\). If all elements are loops or coloops, the basis is unique, both dimensions are zero, and \(\nu(M)=0\). Otherwise every legal root \(e\) has, by the induction hypothesis and Step 3, an optimal depth contribution equal to \(1+\min\{\nu(M\setminus e),\nu(M/e)\}=\nu(M)\). Thus the maximum equals \(\nu(M)\), and any nonconstant coordinate is an optimal root. The base case \(E=\varnothing\) is immediate.

**Step 5: Computational and graphic consequences.** Matroid intersection finds a maximum common independent set of \(M\) and \(M^*\) in polynomially many independence-oracle operations. The dual oracle is implemented by testing whether the complement spans \(M\). For a connected graph, the bases of its cycle matroid are spanning trees; consequently the two dimensions equal the greatest size of an edge set that is both acyclic and deletable without disconnecting the graph. For a uniform matroid \(U_{r,n}\), they equal \(\min\{r,n-r\}\). For the direct sum \(U_{1,5}\oplus U_{4,5}\), they equal \(2\), even though both rank and corank are \(5\). Thus neither the rank nor corank alone determines the common dimension.

## Verification
The accompanying standalone Python program `verify.py` computes, by **separate exhaustive recurrences**, the VC dimension, Littlestone dimension, rank-minimum invariant, and all eligible-root optimality identities of a collection of finite matroids. It enumerates distinct matroids represented by all binary matrices of up to five columns and at most three rows, adds seeded six- and seven-column binary configurations, and checks a rank-five direct sum on ten elements. It found \(1347\) distinct binary matroids in the deduplicated sample, and all comparisons passed. Run `python3 verify.py`; the exact console output appears in `check_output.txt`. This finite experiment corroborates the unrestricted mathematical proof but does not constitute an exhaustive test of all finite matroids or of nonrepresentable matroids.

## Relationship to prior work
The general Littlestone/tree-shattering recurrence belongs to online learning and model-theoretic classification; the matroid intersection min-max theorem and dual-rank formula are classical matroid theory. Lendl, Peis and Timmermans (2019 preprint, 2021 journal) study matroid **basis intersection constraints**, but their primary question is optimization over pairs of matroid bases, rather than VC/Littlestone dimension of the single-basis incidence family. Chase, Freitag and Reyzin (2023) develop general applications of Littlestone dimension to query learning, but do not formulate a basis-family rank formula in the inspected article. Guingona and collaborators (2021) establish equality of these dimensions for families of **linear-combination zero sets**, not for matroid bases. Manurangsi and Rubinstein (2017) give hardness results for general explicitly represented concept classes, in contrast to the matroid-restricted polynomial-time formula here.

The asserted contribution is the **simultaneous identification** of the static and adaptive shattering dimensions of every finite matroid basis class with a classical common-independence optimization invariant, including the universal optimal-root property. It does not claim originality for Edmonds' theorem, rank duality, or the standard concept-class recurrence.

## Limitations
The bound concerns basis-membership labels only. It does not extend by the proof to arbitrary independence systems, arbitrary matroid independence-set classes, or query types other than ground-element membership. The finite verifier covers a limited selection of representable matroids. Historical priority has not been exhaustively established, particularly against older literature on shattering of matroidal set systems and broad structural theorems about online dimensions; the full texts specifically inspected do not supply this precise combined statement. No independent scientific audit has been conducted.

## References
1. P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, arXiv:1705.09517, first posted 2017-05-26, https://arxiv.org/abs/1705.09517.
2. S. Lendl, B. Peis and V. Timmermans, *Matroid Bases with Cardinality Constraints on the Intersection*, arXiv:1907.04741, first posted 2019-07-10; journal DOI:10.1007/s10107-021-01642-1, https://arxiv.org/abs/1907.04741.
3. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first posted 2021-09-10, https://arxiv.org/abs/2109.04805.
4. H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812v1, first posted 2023-10-07, https://arxiv.org/abs/2310.04812.
5. J. Edmonds, *Matroid intersection*, classical maximum-common-independent-set min-max theorem, used as background; see the matroid intersection discussion and references in Reference 2.
