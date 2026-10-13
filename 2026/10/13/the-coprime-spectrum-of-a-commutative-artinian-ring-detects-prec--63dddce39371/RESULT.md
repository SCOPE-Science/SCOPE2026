# The coprime spectrum of a commutative Artinian ring detects precisely its Gorenstein local factors

## Finding
Let \(A\) be a commutative Artinian ring with identity, written in its canonical local decomposition \(A\cong\prod_{i=1}^{r} A_i\), where the \(A_i\) are nonzero Artinian local rings with maximal ideals \(\mathfrak m_i\). For each \(i\), let \(S_i=(0:_{A_i}\mathfrak m_i)\) be its socle and \(k_i=A_i/\mathfrak m_i\). The empty decomposition is allowed for the zero ring.

Use the coproduct of ideals \([I:J]=(J:\operatorname{ann}_A(I))\) and call a nonzero ideal \(C\) *coprime* when, for all ideals \(I,J\),
\[
C\subseteq[I:J]\quad\Longrightarrow\quad C\subseteq I\ \text{or}\ C\subseteq J.
\]
The set of such ideals, with closed subsets \(V_c(I)=\{C:C\subseteq I\}\), is \(\operatorname{CoSp}(A)\).

**Classification.** Every coprime ideal of \(A\) is exactly one of the ideals
\[
C_i=0\times\cdots\times 0\times S_i\times 0\times\cdots\times 0
\]
for which \(\dim_{k_i}S_i=1\). In particular,
\[
\#\operatorname{CoSp}(A)
=\#\{i:\text{the Artinian local ring }A_i\text{ is Gorenstein}\}.
\]
The coprime spectrum is a finite **discrete** space. Consequently, for nonzero Artinian rings the annihilator map reaches the **entire** ordinary prime spectrum exactly when the ring is Gorenstein. More precisely, the annihilator map is a homeomorphism
\[
\operatorname{ann}:\operatorname{CoSp}(A)\longrightarrow
\{\mathfrak M\in\operatorname{Spec}(A):A_{\mathfrak M}\text{ is Gorenstein}\}
\]
onto the Gorenstein locus endowed with the subspace topology, where \(\mathfrak M_i=A_1\times\cdots\times\mathfrak m_i\times\cdots\times A_r\).

Equivalently, for a nonzero commutative Artinian **local** ring \(A\), its coprime spectrum is empty if and only if its socle has dimension at least two over the residue field; otherwise its sole point is the socle. This includes fields, whose socle equals the whole ring.

## Assumptions and scope
The ring is commutative, unital and Artinian; no field structure, finiteness of its underlying set, or characteristic restriction is imposed. The zero ring has empty prime and coprime spectra. A nonzero Artinian ring is a finite product of nonzero Artinian local rings. We use the standard zero-dimensional criterion that an Artinian local ring is Gorenstein if and only if its socle has dimension one over the residue field.

The assertion concerns the coproduct-based coprimality defined above, not ordinary comaximality of ideals. The number of coprime ideals is independent of residue-field cardinalities or local lengths, except through whether each local factor is Gorenstein.

## Proof
**Step 1: a local elimination lemma.** Let \((R,\mathfrak m)\) be any nonzero Artinian local ring, with \(S=(0:_R\mathfrak m)\). Nilpotence of \(\mathfrak m\) shows that every nonzero ideal contains a nonzero simple ideal: if \(C\ne0\), choose the final nonzero term in the sequence \(C,\mathfrak m C,\mathfrak m^2 C,\ldots\); a nonzero element there generates an ideal killed by \(\mathfrak m\). Every simple ideal is a one-dimensional subspace of \(S\), and its annihilator equals \(\mathfrak m\).

Fix a nonzero ideal \(C\) which is **not** simple. Choose any simple ideal \(L\) of \(R\). Since \(C\nsubseteq L\), and since \(C\nsubseteq\mathfrak m C\) by Nakayama's lemma, the two proper candidates \(I=L\) and \(J=\mathfrak m C\) neither contain \(C\). But \(\operatorname{ann}(L)=\mathfrak m\), so
\[
C\mathfrak m=\mathfrak m C\subseteq J
\quad\Longrightarrow\quad
C\subseteq(J:\mathfrak m)=[L:J].
\]
Hence \(C\) is not coprime. Thus **every** coprime ideal of \(R\) must be simple.

Now suppose that \(\dim_{R/\mathfrak m}S\ge2\). Given any simple ideal \(C\), choose a different simple ideal \(L\) in \(S\). Then \(C\nsubseteq L\) and \(C\nsubseteq0\), while
\[
C\subseteq S=(0:\mathfrak m)=[L:0],
\]
so \(C\) is not coprime. No coprime ideal exists.

If instead \(\dim_{R/\mathfrak m}S=1\), there is exactly one simple ideal, namely \(S\). It lies in every nonzero ideal: every nonzero ideal contains a simple ideal, and the latter must equal \(S\). To show that \(S\) is coprime, suppose \(S\subseteq[I:J]\) but \(S\nsubseteq I\) and \(S\nsubseteq J\). Essentiality forces \(I=J=0\), whereas \([0:0]=(0:\operatorname{ann}(0))=(0:R)=0\), contrary to \(S\ne0\). This completes the local classification, also when \(R\) is a field.

**Step 2: passage to finite products.** In \(A=\prod_i A_i\), every ideal is a product \(C=\prod_i C_i\); annihilators, ideal quotients and coproducts are computed coordinatewise. A coprime ideal cannot have two nonzero coordinates. Indeed, if it does, partition its nonzero coordinates into two nonempty groups and let \(I,J\) be the corresponding coordinate-supported ideals, with \(C=I+J\). Then \(C\nsubseteq I,J\), yet
\[
C=I+J\subseteq[I:J],
\]
since \((I+J)\operatorname{ann}(I)\subseteq J\). This contradicts coprimality.

Conversely, a nonzero ideal supported in precisely coordinate \(i\) is coprime in \(A\) if and only if its sole nonzero coordinate is coprime in \(A_i\). This is immediate from the coordinatewise coproduct identity: inclusion of the supported ideal in \([I:J]\) is exactly inclusion of that coordinate in \([I_i:J_i]\), while inclusion in \(I\) or \(J\) is tested in the same coordinate. Combining with Step 1 gives precisely the displayed \(C_i\).

**Step 3: topology and annihilator.** For every subset \(T\) of the surviving indices, define an ideal whose \(i\)-th coordinate is \(S_i\) for \(i\in T\) and zero otherwise. Its \(V_c\) equals precisely \(\{C_i:i\in T\}\). Every subset of \(\operatorname{CoSp}(A)\) is closed, so the topology is discrete. Finally, \(\operatorname{ann}_A(C_i)=\mathfrak M_i\), and the Artinian local Gorenstein criterion identifies the surviving indices with the Gorenstein points of \(\operatorname{Spec}(A)\). As the latter space is finite discrete, annihilation gives the asserted homeomorphism.

## Verification
The proof is uniform for all commutative Artinian rings. An independent finite-field enumeration implements the coproduct directly from the multiplication tables and tests its defining universal quantifier over all ideals. Run `python verify.py` using Python 3 with no dependencies. The exhaustive tests cover nine small \(\mathbb F_2\)-algebras: a field, two truncated polynomial local rings, two square-zero non-Gorenstein local rings, a non-Gorenstein local ring with nonzero square of its radical, a product of a field with dual numbers, and products of a field with each of the latter two non-Gorenstein types. Every computed coprime-ideal count agrees with the classification (the test ends in `VERIFY_OK`). Exhaustion in these small examples is not a proof of the unrestricted theorem; the argument above provides that proof.

Two illustrative cases over any field \(k\): the local ring \(k[x,y]/(x^2,xy,y^2)\) has two-dimensional socle, hence empty coprime spectrum despite having one prime ideal; and \(k[t]/(t^2)\times k[x,y]/(x^2,xy,y^2)\) has exactly one coprime point although its ordinary prime spectrum has two points.

## Relationship to prior work
Murphy-Hernandez and Leon-Rodriguez introduced \([I:J]=(J:\operatorname{ann}(I))\) and the coprime spectrum in arXiv:2609.23351v1 (first submitted 20 September 2026). Their paper proves that the coprime spectrum agrees with the prime spectrum on **dual rings**, and gives examples including a non-Gorenstein square-zero local ring. This theorem instead classifies the coprime ideals for **every** commutative Artinian ring, including all non-dual local rings and mixed products, identifying the exact part of the ordinary spectrum retained in the latter cases. The result also uses the classical Artinian Gorenstein criterion via the socle.

## Limitations
No extension to non-Artinian or noncommutative rings is asserted. The result is a consequence of a new coprimality definition and classical local-ring methods; it is not an independent classification of Gorenstein rings themselves. An equivalent formulation in earlier ideal-lattice terminology remains possible. A later attempt to retrieve all sections of the closest primary article was unsuccessful; the comparison is based on its accessible HTML introductory theorem inventory, its ideal-operation definitions, its square-zero example, and its stated dual-ring theorem. 

## References
1. Frank Murphy-Hernandez and Eduardo Leon-Rodriguez, *The Coproduct of Ideals and the Coprime Spectrum*, arXiv:2609.23351v1 (20 September 2026), https://arxiv.org/abs/2609.23351 and https://arxiv.org/html/2609.23351.
2. Eric W. Weisstein, *Gorenstein Ring*, Wolfram MathWorld, https://mathworld.wolfram.com/GorensteinRing.html (Artinian local socle criterion).
3. D. Eisenbud, *Commutative Algebra with a View toward Algebraic Geometry*, Springer, 1995, Proposition 21.5 (classical socle criterion; bibliographic reference, not independently inspected).
