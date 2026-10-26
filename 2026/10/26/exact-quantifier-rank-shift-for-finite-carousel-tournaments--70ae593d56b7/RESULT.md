# Exact quantifier-rank shift for finite carousel tournaments

## Finding
For each integer \(m\ge1\), let \(R_{2m+1}\) be the tournament on \(\mathbb Z/(2m+1)\) with \(u\to v\) precisely when \(1\le(v-u)\bmod(2m+1)\le m\). In the first-order language consisting only of equality and the arc relation, for all integers \(m,n,q\ge1\),
\[
R_{2m+1}\equiv_q R_{2n+1}\quad\Longleftrightarrow\quad
\min(m,2^{q-1}-1)=\min(n,2^{q-1}-1).
\]
Here \(\equiv_q\) denotes agreement on every first-order sentence of quantifier rank at most \(q\). Thus the finite carousel tournaments have exactly one rank-\(1\) theory, and for \(q\ge2\) exactly \(2^{q-1}-1\) rank-\(q\) theories. At rank one the smallest representative has index \(m=1\); for \(q\ge2\), the smallest representatives are indexed by \(m=1,\ldots,2^{q-1}-1\), and the sharp uniform bound on their orders is \(2^q-1\). For \(1\le m<n\), their least distinguishing quantifier rank is \(1+\lceil\log_2(m+2)\rceil\).

The stronger structural statement is that, for all \(m,n,q\ge1\),
\[
R_{2m+1}\equiv_q R_{2n+1}\quad\Longleftrightarrow\quad
L_m\equiv_{q-1}L_n,
\]
where \(L_m\) is a strict linear order on \(m\) points and rank-zero equivalence always holds.

## Assumptions and scope
All tournament orders are odd and at least three; the language has no named vertices, no numerical parameters, and no built-in linear order. The arc relation is irreflexive. Quantifier rank counts the maximum number of nested quantifiers and permits arbitrary Boolean combinations. The claimed sharpness is **within this tournament family**; no minimal representative among arbitrary tournaments is asserted.

## Proof
**Lemma 1 (anchored two-chain coding).** Fix an arbitrary vertex \(x\) of \(R_{2m+1}\). By translation assume \(x=0\). Label its outneighbors \(A_i=i\) and its inneighbors \(B_i=m+i\), for \(1\le i\le m\). These labels exhaust all vertices other than \(x\). The arc relation is given by
\[
 x\to A_i,\quad B_i\to x;\qquad
 A_i\to A_j\iff i<j,\qquad B_i\to B_j\iff i<j;
\]
\[
 A_i\to B_j\iff j\le i,\qquad B_i\to A_j\iff j<i.
\]
All six rules follow by subtraction modulo \(2m+1\). Vertex equality is equality of the side and index, except that the anchor is a separate point. Thus the entire atomic diagram of any finite tuple containing \(x\) is determined by the two side labels and the linear-order comparison/equality diagram of their indices.

**Lemma 2 (game lifting).** If \(L_m\equiv_r L_n\), then \(R_{2m+1}\equiv_{r+1}R_{2n+1}\). Play the \((r+1)\)-round Ehrenfeucht–Fraïssé game on the tournaments. After Spoiler's first selection \(x\), Duplicator chooses any vertex \(x'\). Each later selection other than a repeated anchor determines a side \(A\) or \(B\) and an index in \(L_m\) or \(L_n\). Duplicator keeps the side and uses her winning \(r\)-round linear-order strategy on the sequence of indices. The strategy handles repeated indices (including those first selected on the opposite side), as required by the usual game. Lemma 1 guarantees preservation of all atomic arcs and equalities of selected vertices, so Duplicator wins.

**Lemma 3 (outneighborhood interpretation).** If \(R_{2m+1}\equiv_{r+1}R_{2n+1}\), then \(L_m\equiv_r L_n\). The outneighborhood \(N^+(x)\) of every vertex in \(R_{2m+1}\), with its induced arc relation, is a transitive tournament of order \(m\), hence isomorphic to \(L_m\). For any linear-order sentence \(\psi\) of quantifier rank at most \(r\), relativize each quantifier to \(N^+(x)\), replacing \(<\) with \(\to\). Its relativization \(\psi^{N^+(x)}\) has rank at most \(r\) with \(x\) free. The sentence \(\exists x\,\psi^{N^+(x)}\) has rank at most \(r+1\), and is true in \(R_{2m+1}\) exactly when \(L_m\models\psi\). Agreement on tournament sentences therefore implies agreement on rank-\(r\) order sentences. This also covers \(r=0\).

**Lemma 4 (classical finite-order cutoff).** For each integer \(r\ge0\), finite nonempty linear orders of sizes \(m\) and \(n\) are equivalent at rank \(r\) precisely when \(\min(m,2^r-1)=\min(n,2^r-1)\). For sufficiency Duplicator preserves the exact lengths of intervals shorter than \(2^{r'}-1\) and preserves the property of being at least that long, where \(r'\) rounds remain. A chosen point can be matched by splitting the corresponding interval into segments of the same small sizes or both large sizes because \(2^{r'}-1=2(2^{r'-1}-1)+1\). For necessity one constructs recursively, by splitting at a witness point, rank-\(r\) sentences stating that at least \(t\) points exist for every \(1\le t\le2^r-1\); the interval-quantifier recursion partitions \(t-1\) into two parts bounded by \(2^{r-1}-1\). Therefore every size below the cutoff is individually distinguishable and all greater sizes have the same rank-\(r\) theory. At \(r=0\), no nontrivial order property can be expressed by a sentence.

Combining Lemmas 2–4 with \(r=q-1\) proves the equivalence and number of classes. At rank one, all structures agree and the smallest member has three vertices. For \(q\ge2\), the last class first occurs at \(m=2^{q-1}-1\), giving smallest representative order \(2m+1=2^q-1\). If \(m<n\), the first rank at which \(m\) lies strictly below the order cutoff \(2^{q-1}-1\) is the least integer \(q\) satisfying \(m<2^{q-1}-1\), namely \(q=1+\lceil\log_2(m+2)\rceil\), proving the remaining claim.

## Verification
The accompanying standard-library Python program `verify_carousel.py` checks all anchored arc rules for \(1\le m\le75\); computes exact finite atomic/Hintikka signatures independently for tournaments through 35 vertices at ranks at most four and through 13 vertices at rank five; directly computes finite linear-order signatures and their thresholds; and checks the symbolic cutoff partition for ranks one through nine and indices through 99. Its recorded execution ends in `VERIFY_OK`. These finite checks corroborate the formulas; the all-index, all-rank assertion is supplied by the proof.

## Relationship to prior work
Mwesigye and Truss (published online 2010) develop quantifier-depth characters for finite colored linear orders and include the classical uncolored cutoff used in Lemma 4. Coregliano (first public preprint 2015) studies locally transitive carousel tournaments and their asymptotic properties, identifying the same tournament family. Neither of those inspected treatments states the exact arbitrary-rank first-order equivalence transfer and sharp resulting carousel classification. In particular, the new content is the anchored two-chain game reduction and the exact unlabelled-tournament characterization; neither the finite-order cutoff nor the carousel construction is claimed as new.

## Limitations
The theorem concerns only canonical carousel tournaments with the pure arc relation. Enriching the language by a distinguished vertex, order, successor, or additional relations may change the equivalence classes. The finite verification is not a formal proof or an independent audit. Literature searches cannot exclude equivalent statements in unindexed or inaccessible historical sources.

## References
1. A. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, *Order* 28 (2011), 387–397, first published online September 7, 2010. DOI: https://doi.org/10.1007/s11083-010-9178-9. Open-access full text: https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download.
2. L. N. Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124, first submitted March 13, 2015. https://arxiv.org/abs/1503.04124.
