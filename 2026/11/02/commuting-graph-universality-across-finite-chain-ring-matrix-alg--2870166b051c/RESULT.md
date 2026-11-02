# Commuting-graph universality across finite chain-ring matrix algebras

## Finding
Let \(R\) and \(S\) be finite commutative chain rings with residue-field cardinalities \(q_R,q_S\), and let \(\ell_R,\ell_S\ge1\) be the lengths of their chains of powers of the maximal ideal. A **full commuting graph** \(\Gamma(M_2(R))\) has all matrices as vertices, including central scalar matrices; two *distinct* matrices are adjacent exactly when they commute.

**Theorem.** For all such \(R,S\),
\[
\Gamma(M_2(R))\cong\Gamma(M_2(S))
\quad\Longleftrightarrow\quad
(q_R,\ell_R)=(q_S,\ell_S).
\]
Moreover, for \(R\) with parameters \((q,\ell)\), scalar matrices contribute \(q^\ell\) vertices with centralizer cardinality \(q^{4\ell}\); for each integer \(0\le s<\ell\), exactly
\[
q^\ell\bigl(q^{3(\ell-s)}-q^{3(\ell-s-1)}\bigr)
\]
vertices have centralizer cardinality \(q^{2\ell+2s}\). In particular the number of ordered pairs of commuting matrices (allowing equality) is
\[
q^{5\ell}+(q^2+q+1)\bigl(q^{6\ell-2}-q^{5\ell-2}\bigr).
\]
The rings \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[t]/(t^2)\) have the same parameters \((2,2)\) but are not isomorphic. Their \(256\)-vertex full matrix commuting graphs are therefore isomorphic (each has \(6400\) ordered commuting pairs), even though the first matrix ring has additive-group exponent \(4\) and the second has additive-group exponent \(2\).

## Assumptions and scope
A finite commutative chain ring is a finite commutative local ring whose ideals are the powers \(R\supsetneq(\pi)\supsetneq\cdots\supsetneq(\pi^{\ell-1})\supsetneq(\pi^\ell)=0\). Its residue field is \(R/(\pi)\cong\mathbb F_q\). All residue-field cardinalities \(q\) are prime powers at least \(2\); characteristic \(2\), mixed characteristic, and \(\ell=1\) are included. The nilpotency length \(\ell\) is the unique integer satisfying \(\pi^\ell=0\) and \(\pi^{\ell-1}\ne0\). We consider actual labelled matrices over \(R\), not matrix conjugacy classes; all statements concern the underlying simple commuting graph, not a ring isomorphism.

For \(a\in R\), write \(v(a)\) for the greatest integer \(s<\ell\) such that \(a\in(\pi^s)\), with \(v(0)=\ell\). All ring quotients \(R/(\pi^k)\), \(1\le k\le\ell\), have \(q^k\) elements.

## Proof
**Step 1: a three-coordinate commutation equation.** Every matrix has a unique expression
\[
A=dI_2+\begin{pmatrix}a&b\\c&0\end{pmatrix},
\qquad d,a,b,c\in R.
\]
Associate to it \(x(A)=(a,b,c)\in R^3\). Direct multiplication gives, for any two such matrices \(A,B\),
\[
[A,B]=0\quad\Longleftrightarrow\quad
x_i(A)x_j(B)-x_j(A)x_i(B)=0
\ \text{for all }1\le i<j\le3.
\]
Indeed, the three entries of the commutator are \(b c'-b'c\), \(a b'-a'b\), and \(c a'-c'a\) (up to a common sign where appropriate). Thus commutation is the determinantal relation \(x(A)\wedge x(B)=0\). Scalar coordinates \(d\) are completely free.

**Step 2: the universal projective forest.** For a vector \(x\ne0\), set \(s=\min_i v(x_i)\). There is a unique primitive \(\bar u\in(R/(\pi^{\ell-s}))^3\) such that \(x=\pi^s\bar u\), where the multiplication identifies the quotient with the ideal \((\pi^s)\) coordinatewise. Because \(\bar u\) has a unit coordinate, its projective direction \([\bar u]\in\mathbb P^2(R/(\pi^{\ell-s}))\) is well-defined. Once a direction is chosen, \(\bar u\) is specified by a unit scalar. The scalar fiber has cardinality
\[
(q-1)q^{\ell-s-1}.
\]

For every \(k\ge1\), projective points over \(R/(\pi^k)\) reduce to projective points over \(R/(\pi^{k-1})\). There are \(q^2+q+1\) points at level \(k=1\), and **every** point at level \(k-1\) has exactly \(q^2\) lifts at level \(k\). To see this, normalize each primitive triple by dividing by its first unit coordinate. Fixing its reduction then leaves precisely two free lifts by elements of the one-dimensional additive kernel \((\pi^{k-1})/(\pi^k)\), each with \(q\) choices. The normalized coordinate that is \(1\) stays fixed; the first unit pivot is unchanged by reduction. The reduction diagram is therefore a rooted forest consisting of \(q^2+q+1\) roots, each node with \(q^2\) children, up to level \(\ell\). Its isomorphism type depends only on \((q,\ell)\).

**Step 3: the entire commutation relation is forest-theoretic.** Suppose nonzero \(x=\pi^s\bar u\) and \(y=\pi^t\bar v\). If \(s+t\ge\ell\), all their minors vanish. Otherwise, put \(k=\ell-s-t\ge1\). Then
\[
x\wedge y=0\quad\Longleftrightarrow\quad
\bar u\wedge\bar v=0\pmod{\pi^k}
\quad\Longleftrightarrow\quad
[\bar u]\bmod\pi^k=[\bar v]\bmod\pi^k.
\]
The second equivalence holds because a primitive vector over a local ring has a unit coordinate: vanishing of its minors forces the other vector to be its scalar multiple. Thus two nonzero vectors commute precisely according to their valuations and the coincidence of their ancestors at level \(k\). A zero vector commutes with every vector.

Given two chain rings with identical \((q,\ell)\), choose an isomorphism of their projective forests and arbitrary bijections of the equally large unit-scalar fibers above corresponding nodes. This gives a bijection \(R^3\to S^3\) preserving and reflecting the wedge-zero relation. Choose in addition any bijection \(R\to S\) for the free scalar coordinate \(d\). By Step 1, their full commuting graphs are isomorphic. This construction includes the zero vector and every scalar matrix.

**Step 4: centralizers and parameter recovery.** Fix \(A\) with nonzero coordinate vector \(x\) of valuation \(s\). In the quotient \(R/(\pi^{\ell-s})\), the primitive vector \(\bar u\) has a unit coordinate. The condition on \(y\in R^3\) is that its reduction modulo \(\pi^{\ell-s}\) be an arbitrary scalar multiple of \(\bar u\). There are exactly \(q^{\ell-s}\) distinct multiples and \(q^{3s}\) lifts to \(R^3\), hence \(q^{\ell+2s}\) compatible \(y\). The free scalar coordinate of \(B\) adds a factor \(q^\ell\), so
\[
|C_{M_2(R)}(A)|=q^{2\ell+2s}.
\]
There are \(q^{3(\ell-s)}-q^{3(\ell-s-1)}\) coordinate vectors of valuation \(s\), and \(q^\ell\) scalar choices for each. If \(x=0\), there are \(q^\ell\) scalar matrices whose centralizers are all \(M_2(R)\), of cardinality \(q^{4\ell}\). These values are pairwise distinct for \(s=0,\ldots,\ell-1\), and give the stated multiplicities.

In the full **simple** graph, each degree is the corresponding centralizer cardinality minus \(1\). Therefore the number of distinct graph degrees is exactly \(\ell+1\), recovering \(\ell\) from the graph. The number of vertices is \(q^{4\ell}\), which then uniquely recovers the positive integer \(q\). Graph isomorphism consequently forces the two parameters to match, proving the converse.

Finally, summing the centralizer cardinalities over every matrix gives the number of ordered commuting pairs:
\[
q^{5\ell}+\sum_{s=0}^{\ell-1}q^\ell\bigl(q^{3(\ell-s)}-q^{3(\ell-s-1)}\bigr)q^{2\ell+2s}
=q^{5\ell}+(q^2+q+1)(q^{6\ell-2}-q^{5\ell-2}).
\]
This completes the proof. \(\square\)

## Verification
The standalone standard-library script `verify.py` constructs modular rings \(\mathbb Z/p^\ell\mathbb Z\) and truncated polynomial rings \(\mathbb F_p[t]/(t^\ell)\) using separately implemented arithmetic, explicitly constructs their projective reduction forests, checks a degree-preserving commuting-graph bijection on **all** coordinate vectors, and compares direct commutator calculations with the determinantal equation. All \(4^4=256\) matrices over \(\mathbb Z/4\mathbb Z\) are also independently tested against each other using direct matrix multiplication, giving \(6400\) commuting ordered pairs. Parameters \((p,\ell)=(2,1),(2,2),(2,3),(3,2)\) are tested; all pass. These finite tests corroborate the universal proof but are not its substitute.

Execute from the package directory with `python3 verify.py`; it ends in `VERIFY_OK` on success. The script uses only Python's standard library.

## Relationship to prior work
Hengbin Zhang, *Automorphism group of the commuting graph of \(2\times2\) matrix ring over \(\mathbb Z_{p^s}\)* (2021), gives a detailed partition and graph-automorphism theorem for the **noncentral-vertex graph of the one family** \(M_2(\mathbb Z/p^s\mathbb Z)\). In particular, his Lemma 3.3 and Lemma 3.5 already contain related valuation-level commutation and \(p^2\)-branching phenomena for that family; these are prior work and are not asserted to be new. The present theorem concerns an **isomorphism classification across arbitrary finite commutative chain rings**, including residue fields of nonprime order and mixed-versus-equal characteristic, while retaining all scalar vertices. The proof supplies the needed ring-independent projective-forest model and the converse graph reconstruction.

Mohammadian (2010) proves rigidity when the comparison ring is a full matrix algebra over a **finite field**. That result does not compare two nonfield chain-ring matrix algebras. Abdollahi (2008) similarly treats the finite-field target and supplies background on matrix commuting graphs. Neither yields a ring isomorphism for the two nonisomorphic rings of length two in the example.

## Limitations
The if-and-only-if theorem is restricted to full \(2\times2\) matrix algebras over finite **commutative principal-ideal local** (chain) rings. It does not classify \(3\times3\) matrix graphs, matrix graphs over non-chain local rings, or reconstruction of a ring from all of its multiplication. The graph includes the center, unlike the conventional noncentral-only commuting graph; that convention is essential to the exact vertex and degree formulas quoted here. The finite checks do not prove the infinite family. The priority comparison relies on accessible literature; a more general unlocated matrix-ring graph theorem might imply parts of this result. No independent mathematical audit has been performed.

## References
1. Hengbin Zhang, “Automorphism group of the commuting graph of 2 × 2 matrix ring over \(\mathbb Z_{p^s}\),” *AIMS Mathematics* **6** (2021), 12650–12659, DOI 10.3934/math.2021729. First public date verified from the publisher: 2021-09-02. Full primary PDF inspected, especially Lemmas 3.2–3.5 and Theorem 3.8.
2. A. Mohammadian, “On Commuting Graphs of Finite Matrix Rings,” *Communications in Algebra* **38** (2010), 988–994, DOI 10.1080/00927870902911771. Abstract inspected; full text not accessed.
3. Alireza Abdollahi, “Commuting graphs of full matrix rings over finite fields,” *Linear Algebra and its Applications* **428** (2008), 2947–2954, DOI 10.1016/j.laa.2008.01.036. Abstract inspected; full text not accessed.
