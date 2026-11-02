# Rigidity and exact Bell-number census of three-level S5-confluent frames

## Finding

Fix three pairwise disjoint, nonempty, labelled finite sets \(A,B,C\), with
\[|A|=a,\qquad |B|=b,\qquad |C|=c.\]
Put \(P=A\oplus B\oplus C\): elements of a common level are incomparable unless equal, and every point of an earlier level is strictly below every point of a later level. Let \(R\subseteq P\times P\) be an **equivalence relation**. Impose the two modal-persistence conditions
\[
\begin{aligned}
(\mathrm{D})&\quad x\le y\ \&\ yRz\quad\Longrightarrow\quad
  \exists w\ (xRw\ \&\ w\le z),\\
(\mathrm{U})&\quad x\le y\ \&\ xRz\quad\Longrightarrow\quad
  \exists w\ (yRw\ \&\ z\le w).
\end{aligned}
\]
These are precisely the two order/accessibility confluence conditions (40) and (41) in Sedlár--Vigiani's modal generalised Nelson semantics. The additional requirement that \(R\) be an equivalence relation is the present, epistemically motivated specialization; it is not part of those authors' general definition.

**Complete structural theorem.** Exactly the following five mutually exclusive possibilities occur:

1. **Levelwise:** no equivalence class meets two levels; the partitions of \(A\), \(B\), and \(C\) are arbitrary and independent.
2. **Lower merger:** \(A\cup B\) is a single equivalence class, while \(C\) carries an arbitrary partition.
3. **Upper merger:** \(B\cup C\) is a single equivalence class, while \(A\) carries an arbitrary partition.
4. **Opposed mergers:** for one nonempty proper subset \(U\subsetneq B\), the only two classes are \(A\cup U\) and \((B\setminus U)\cup C\).
5. **Universal:** all of \(P\) is one class.

All five cases satisfy both conditions, and there are no others. In particular, any class meeting nonadjacent levels forces the whole relation to be universal. Every nonuniversal cross-level relation has at most two crossing classes and contains a whole end level in each such class.

Write \(\operatorname{Bell}(m)\) for the number of partitions of an \(m\)-element labelled set. The **exact number of labelled admissible equivalence relations** on \(P\) is
\[
\boxed{\displaystyle
N(a,b,c)=\operatorname{Bell}(a)\operatorname{Bell}(b)\operatorname{Bell}(c)
+\operatorname{Bell}(a)+\operatorname{Bell}(c)+2^{b}-1.}
\]
This formula is valid for **all** positive integers \(a,b,c\), including singleton levels. The five contributions, in order, are
\[
\operatorname{Bell}(a)\operatorname{Bell}(b)\operatorname{Bell}(c),\quad
\operatorname{Bell}(c),\quad\operatorname{Bell}(a),\quad 2^b-2,\quad 1.
\]
For example, \(N(1,2,1)=7\), \(N(2,2,2)=15\), and \(N(2,3,2)=31\).

## Assumptions and scope

The carrier is a *fixed labelled* ordinal sum of exactly three nonempty antichains. The order is reflexive, antisymmetric, and transitive. In this setting, \(x\le y\) holds exactly when \(x=y\) or the level of \(x\) is strictly below the level of \(y\).

The relation \(R\) is assumed reflexive, symmetric, and transitive. We count **binary relations**, not valuations or logical theories. Neither the source paper's bilateral valuations nor additional restrictions associated with logics using an inconsistent-state predicate are counted. The frame conditions (D) and (U) are the two common clauses of its Definition 12; the result applies, for example, as a relational subclass of the \(\mathbf{BN}_1\) (Nelson \(\mathbf{N4}\)) modal setting, without imposing the additional inconsistent-state condition (42) required for other members of the family.

The named sets may have size one. Empty levels are excluded: deleting one would change the classification and its counting formula. The term ``S5'' denotes only the stipulated equivalence property of \(R\), not a claimed axiomatization or completeness theorem for an enriched Nelson logic.

## Proof

For a world \(t\), write \([t]\) for its \(R\)-equivalence class. The two conditions can be restated as follows: whenever \(x\le y\), every element of \([y]\) is above some element of \([x]\), and every element of \([x]\) is below some element of \([y]\).

**Lemma 1 (end-level absorption).** If one class meets both \(A\) and \(B\), it contains all of \(A\). Indeed, choose \(a\in A\), \(u\in B\) in the same class. For any \(a'\in A\), use \(a'\le u\) and \(uRa\) in (D). It gives \(a'Rw\le a\). Since \(a\) is minimal, \(w=a\), so \(a'Ra\). Dually, if one class meets both \(B\) and \(C\), it contains all of \(C\): choose \(v\in B,c\in C\) in the class, and for each \(c'\in C\) apply (U) to \(v\le c'\) and \(vRc\); maximality of \(c\) forces \(c'Rc\).

**Lemma 2 (nonadjacent absorption).** If any class meets both \(A\) and \(C\), the relation is universal. Choose \(a\in A,c\in C\) in that class. Lemma 1's arguments, with \(a'\le c\), \(cRa\), and \(a\le c'\), \(aRc\), force every point of \(A\cup C\) into the class. For each \(b\in B\), apply (U) to \(a\le b\) and \(aRc\). It produces \(bRw\ge c\); maximality of \(c\) gives \(w=c\). Hence \(bRc\). All worlds are therefore in one class.

For the rest of the necessity proof assume \(R\) is not universal. A class meeting \(A\) and \(B\) is unique if it exists, since it contains all of \(A\); denote it \(L\). A class meeting \(B\) and \(C\) is likewise unique if it exists, since it contains all of \(C\); denote it \(H\). If both exist, they are different by Lemma 2. Write \(U=L\cap B\) and \(V=H\cap B\), both nonempty whenever the respective classes exist.

**Lemma 3 (no middle residual class).** If \(L\) exists and \(b_0\in B\setminus L\), then \(b_0\in H\). Choose \(a\in A\subset L\) and \(u\in U\). Applying (U) to \(a\le b_0\) and \(aRu\) gives \(b_0Rw\) with \(u\le w\). As \(b_0\notin L\), \(w\ne u\) and \(w\notin U\); within the three-level poset, a point greater than or equal to \(u\in B\) is either \(u\) or a point of \(C\). Hence \(w\in C\), showing that \([b_0]\) meets \(B,C\) and is \(H\). Dually, if \(H\) exists and \(b_0\in B\setminus H\), choose \(c\in C\subset H\) and \(v\in V\). Condition (D), applied to \(b_0\le c\) and \(cRv\), gives \(b_0Rw\le v\). Because \(b_0\notin H\), \(w\ne v\), and in this order \(w\in A\). Hence \(b_0\in L\).

The classification follows. With neither \(L\) nor \(H\), Lemma 2 rules out all cross-level classes, giving case 1. With only \(L\), Lemma 3 forces \(U=B\), and \(L=A\cup B\), while \(C\) remains freely partitionable, giving case 2. With only \(H\), similarly \(H=B\cup C\), giving case 3. With both, Lemma 3 yields \(B=U\mathbin{\dot\cup}V\), while the absorption lemmas yield \(L=A\cup U\), \(H=V\cup C\); these are the only classes, giving case 4. Lemma 2 accounts for case 5.

**Sufficiency.** In case 1, take \(x<y\). Every \(z\in[y]\) lies on the same higher level as \(y\), so \(x\in[x]\) itself satisfies \(x\le z\) for (D); likewise \(z\in[x]\) lies on the same lower level as \(x\), so \(y\in[y]\) itself satisfies \(z\le y\) for (U). In cases 2--4, whenever \(x<y\) but \([x]\ne[y]\), the class \([x]\) contains some element \(a_0\in A\) and \([y]\) contains some element \(c_0\in C\). Every \(z\in[y]\) satisfies \(a_0\le z\), verifying (D); every \(z\in[x]\) satisfies \(z\le c_0\), verifying (U). If \([x]=[y]\), one may choose \(w=z\) in both conditions. Case 5 has this last property for every pair. The reflexive case \(x=y\) always permits \(w=z\). Thus all listed relations are admissible.

**Enumeration.** The five cases are disjoint by their cross-level class patterns. Case 1 independently chooses partitions on \(A,B,C\), giving the product of Bell numbers. In case 2, only the partition of \(C\) is free; in case 3, only that of \(A\) is free. Case 4 is in bijection with the nonempty proper subsets \(U\subsetneq B\), of which there are \(2^b-2\). Case 5 contributes one. Their sum proves the formula.

## Verification

The accompanying standalone `checker.py` enumerates **every labelled equivalence relation** as a set partition on each carrier with total size between three and eight. It independently tests both quantified existential-witness conditions (D) and (U), categorizes each partition using the five structural cases, and verifies equality for every partition, not just equality of final totals. It checks all 56 triples \((a,b,c)\) with \(a,b,c\ge1\) and \(3\le a+b+c\le8\): **102,487** candidate partitions, of which **4,113** satisfy both confluences. For every triple it also verifies the exact five individual type counts and the Bell-number formula. The program prints `ALL_CHECKS_OK`.

The program is standard-library-only. Reproduce using `python3 checker.py` from a directory containing that file. These finite checks corroborate the exhaustive structural proof above; they make no assertion about carriers larger than eight based solely on enumeration.

## Relationship to prior work

Sedlár and Vigiani, *Modal Extensions of Generalised Nelson Logics*, arXiv:2610.10008v1 (7 October 2026), Definition 12, specify the two confluence conditions (40) and (41) for arbitrary modal accessibility relations. Their Section 3.2 develops persistence and soundness/completeness semantics, not the present equivalence-only three-level frame classification or Bell-number enumeration. Both source conditions are acknowledged as **pre-existing**, not new.

The published mathematical finding *Endpoint normal form and exact census for finite-chain KI frames* specializes the same two confluence conditions to a **totally ordered** carrier and arbitrary binary accessibility relation, obtaining row endpoint monotonicity. This does not imply the three-level antichain-sum classification, where a branching middle level allows two opposed equivalence classes and the count depends on three independent Bell numbers. The published finding *Maxima normal form and exact census for chain birelational relations* uses a different pair of order-relational conditions on a **total chain**; its extrema and enumerator do not imply the present equivalence-confluence statement.

Other nearby work counts arbitrary forward-confluent relations on complete two-level orders. That is neither an equivalence restriction nor a simultaneous two-confluence, three-level theorem. A stronger *triangle* confluence for equivalence relations on connected posets forces the universal relation; it is a different hypothesis and cannot replace the two witness conditions studied here.

Full source texts and semantic search comparisons did not locate a theorem covering the five-type classification or its exact three-parameter count. This establishes the scope of the reported comparison, **not** an independent certification of historical originality.

## Limitations

Equivalence of \(R\), the complete cross-level comparabilities, and exactly three nonempty levels are essential assumptions. This is not a census of arbitrary accessibility relations, models with valuations, larger modal languages, four-or-more-level weak orders, or equivalences under relabelling. No result is asserted for systems requiring additional frame/predicate conditions beyond (D) and (U).

An older equivalent statement might exist in the theory of Egli--Milner monotone partitions, order-compatible equivalences, or relational lax simulations under terminology not captured by the searches. Independent scholarly assessment of priority remains outstanding. The finite checker is not an independent infinite proof.

## References

[1] Igor Sedlár and Pietro Vigiani, *Modal Extensions of Generalised Nelson Logics*, arXiv:2610.10008v1, first posted 7 October 2026, Section 3.2 and Definition 12. https://arxiv.org/html/2610.10008v1

[2] *Endpoint normal form and exact census for finite-chain KI frames*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-endpoint-normal-form-and-exact-census-for-finite-chain-ki-frames--df6301f11b97

[3] *Maxima normal form and exact census for chain birelational relations*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-maxima-normal-form-and-exact-census-for-chain-birelational-relat--f1e0f9b64170

[4] Justus Becker, Anupam Das, Sonia Marin, Paaras Padhiar, *The proof theory and semantics of second-order (intuitionistic) tense logic*, arXiv:2602.06253, first posted 5 February 2026; contextual comparison of birelational conditions.
