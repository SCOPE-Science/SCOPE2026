# Coprime spectra of Noetherian rings detect Artinian Gorenstein components

## Finding

**Theorem.** Let \(R\) be a nonzero commutative Noetherian ring with identity. Use the coprime-ideal definition of Murphy-Hernandez and Leon-Rodriguez [1]: for ideals \(I,J\) of \(R\), put
\[
[I:J]=(J:\operatorname{Ann}_R(I))
 =\{a\in R:a\operatorname{Ann}_R(I)\subseteq J\},
\]
and call a nonzero ideal \(C\) *coprime* if
\[
C\subseteq[I:J]\ \Longrightarrow\ C\subseteq I\ \text{or}\ C\subseteq J
\]
for every pair of ideals \(I,J\). Write \(\operatorname{CoSp}(R)\) for the set of coprime ideals, with the coprime-spectrum topology of [1].

Among the indecomposable direct factors of \(R\), select those that are Artinian local: there are finitely many and their associated idempotents are canonical up to permutation. Write them as \(A_i=e_iR\), with maximal ideals \(\mathfrak n_i\), residue fields \(k_i=A_i/\mathfrak n_i\), and socles
\[
S_i=\operatorname{Ann}_{A_i}(\mathfrak n_i).
\]
Then **the complete set of coprime ideals** is
\[
\boxed{\operatorname{CoSp}(R)=
 \bigl\{S_i\times 0\text{ in }A_i\times (1-e_i)R:
        \dim_{k_i}S_i=1\bigr\}.}
\]
Equivalently, every coprime ideal is the embedded socle of an Artinian Gorenstein local direct summand, and every such embedded socle is coprime. Fields count as Artinian Gorenstein local factors: their socle is the entire field.

**Consequences.** \(\operatorname{CoSp}(R)\) is always a **finite discrete topological space**. Its cardinality equals the number of Artinian Gorenstein local direct factors; it is empty precisely when there are none. Thus every connected positive-dimensional Noetherian ring has empty coprime spectrum, whereas a connected Artinian local ring has exactly one coprime ideal if and only if it is Gorenstein.

## Assumptions and scope

All rings are commutative, associative, with identity. The zero ring is excluded, and no finiteness is imposed on residue-field cardinalities. Noetherianity is used in three distinct places: finiteness of the chosen coprime ideal as a module for Nakayama; Krull's intersection theorem after localization; and finiteness of minimal primes for the idempotent splitting. The theorem concerns the coproduct-defined coprime ideals of [1], **not** other notions such as coprime/second modules.

For an Artinian local ring \((A,\mathfrak n,k)\), \(S=\operatorname{Ann}_A(\mathfrak n)\) is its socle. The standard zero-dimensional Gorenstein criterion is \(\dim_k S=1\), including the case of a field. An Artinian local *factor* means a direct ring summand, not merely a localization at a maximal ideal of positive dimension.

## Proof

**1. Intrinsic annihilator test.** An ideal \(C\neq0\) is coprime exactly when
\[
\tag{1}C\not\subseteq I\quad\Longrightarrow\quad C\operatorname{Ann}_R(I)=C
\]
for every ideal \(I\). Indeed \(C\operatorname{Ann}_R(I)\subseteq C\); taking \(J=C\operatorname{Ann}_R(I)\) in the defining implication proves necessity. Conversely, if \(C\subseteq[I:J]\), then \(C\operatorname{Ann}_R(I)\subseteq J\); if \(C\not\subseteq I\), (1) implies \(C\subseteq J\). This is the annihilator formulation given in Lemma 1 of [1], also proved here to fix all quantifiers.

**2. Localization forces a zero-dimensional component.** Let \(C\) be coprime. Select a maximal ideal \(\mathfrak m\) such that \(C_{\mathfrak m}\neq0\), which exists since \(C\neq0\). For any positive integer \(n\) such that \((\mathfrak mR_{\mathfrak m})^n\neq0\), we claim \(C\subseteq\mathfrak m^n\). Otherwise (1) gives
\[
C_{\mathfrak m}=C_{\mathfrak m}
   (\operatorname{Ann}_R(\mathfrak m^n))_{\mathfrak m}
\subseteq C_{\mathfrak m}
   \operatorname{Ann}_{R_{\mathfrak m}}((\mathfrak mR_{\mathfrak m})^n)
\subseteq(\mathfrak mR_{\mathfrak m})C_{\mathfrak m}.
\]
The last inclusion holds because the annihilator of a nonzero ideal in the local ring \(R_{\mathfrak m}\) is a proper ideal. The reverse inclusion is automatic, so Nakayama's lemma gives \(C_{\mathfrak m}=0\), contradiction. If all localized powers were nonzero, the claim and Krull's intersection theorem [2] would imply
\[
C_{\mathfrak m}\subseteq\bigcap_{n\ge1}(\mathfrak mR_{\mathfrak m})^n=0,
\]
another contradiction. Hence some power of \(\mathfrak mR_{\mathfrak m}\) is zero. The Noetherian local ring \(R_{\mathfrak m}\) is therefore Artinian. In particular \(\mathfrak m\) is both a minimal prime and a maximal ideal of \(R\).

**3. This localization is a direct factor, and \(C\) lives entirely there.** Noetherian rings have finitely many minimal prime ideals. As \(\mathfrak m\) is simultaneously minimal and maximal, the closed set \(V(\mathfrak m)=\{\mathfrak m\}\) is disjoint from the closed sets of all other minimal primes. The complement of \(\{\mathfrak m\}\) is their finite union; thus the singleton is clopen. It corresponds to an idempotent \(e\in R\), giving
\[
R=eR\times(1-e)R,\qquad eR\simeq R_{\mathfrak m},
\]
where \(eR\) is Artinian local.

We also need a consequence of (1): whenever a coprime ideal satisfies \(C\subseteq I+J\), one has \(C\subseteq I\) or \(C\subseteq J\). For if not, (1) twice gives \(C=C\operatorname{Ann}_R(I)\operatorname{Ann}_R(J)\); yet \((I+J)\operatorname{Ann}_R(I)\operatorname{Ann}_R(J)=0\), forcing \(C=0\). Apply this to \(C=eC+(1-e)C\): the coprime ideal lies in exactly one summand. Since \(C_{\mathfrak m}\neq0\), it must lie in \(eR\).

Conversely, for a product \(R=A\times B\) and an ideal \(C=C_A\times0\), (1) holds in \(R\) precisely when it holds for \(C_A\) in \(A\): all annihilators and ideal products are coordinatewise, and \(C\subseteq I_A\times I_B\) is equivalent to \(C_A\subseteq I_A\). Thus the classification reduces exactly to the Artinian local case.

**4. The Artinian local case.** Let \((A,\mathfrak n,k)\) be Artinian local and \(0\neq C\subseteq A\) coprime. If \(0\neq I\subseteq A\) and \(C\not\subseteq I\), (1) implies
\[
C=C\operatorname{Ann}_A(I)\subseteq\mathfrak nC,
\]
because the annihilator of a nonzero ideal is proper. Nakayama contradicts \(C\neq0\). Therefore \(C\) is contained in **every** nonzero ideal of \(A\). Conversely any nonzero ideal with this property satisfies (1), since the only ideal not containing it is the zero ideal and \(\operatorname{Ann}_A(0)=A\).

The socle \(S=\operatorname{Ann}_A(\mathfrak n)\) is nonzero: any nonzero ideal \(I\) meets it, because the final nonzero member of \(I\supseteq\mathfrak nI\supseteq\cdots\) is annihilated by \(\mathfrak n\). If \(\dim_kS=1\), that nonzero intersection forces \(S\subseteq I\) for every nonzero ideal \(I\), so \(S\) is the unique coprime ideal. If \(\dim_kS\ge2\), choose two distinct one-dimensional ideals within \(S\); their intersection is zero, so no nonzero ideal can lie inside every nonzero ideal. Hence there is no coprime ideal. The standard zero-dimensional criterion identifies precisely the former case with Artinian Gorenstein local rings.

**5. Topology and completeness.** Steps 2--4 show that **all** coprime ideals are the embedded socles \(C_1,\dots,C_s\) from the qualifying factors, and each occurs. In the coprime-spectrum topology [1], the closed hulls are of the form
\[
V_c(J)=\{C\in\operatorname{CoSp}(R): C\subseteq J\}.
\]
For each subset \(T\subseteq\{1,\dots,s\}\), choose \(J_T=\sum_{i\in T}C_i\). Different ideals \(C_i\) lie in different orthogonal direct summands, so \(V_c(J_T)=\{C_i:i\in T\}\). Every subset is closed; the topology is discrete and finite. This proves all assertions.

## Verification

The included standalone \(\mathbb F_2\)-algebra checker `verify_coprime_artinian.py` exhaustively enumerates ideals from binary subspaces in seven explicitly specified small Artinian local rings. It computes annihilators by multiplication and tests every nonzero ideal against every ordered pair of ideals using **the original coproduct condition**, not the classification theorem. It then tests ten products, ranging from two- to three-factor mixed Gorenstein/non-Gorenstein rings, and checks that all subsets of the computed coprime spectrum arise as closed hulls.

All **17 Artinian configurations** pass and produce the predicted zero-or-one local spectrum and sum of component spectra. The checker itself verifies associativity of each multiplication table. Run `python verify_coprime_artinian.py` from the package. The finite calculations stress-test but do **not** establish the Noetherian theorem; the proof above supplies that argument by Nakayama, Krull intersection, and idempotent decomposition.

Illustrative infinite Noetherian examples: \(k[t]\times k[\varepsilon]/(\varepsilon^2)\times k[x,y]/(x,y)^2\) has precisely one coprime point, from the middle factor; \(k[t]\times k[x,y]/(x,y)^2\) has none. All examples hold for any field \(k\).

## Relationship to prior work

Murphy-Hernandez and Leon-Rodriguez [1] introduced this ideal coproduct and its coprime spectrum, established the annihilator test and join-primality, classified the domain case, and proved that for **dual rings** the coprime spectrum is homeomorphic to the ordinary prime spectrum. The definitions and annihilator test are credited to [1] (with a reconstruction here for clarity). The present theorem concerns **all Noetherian commutative rings**, including mixed positive-dimensional/Artinian factors and non-Gorenstein Artinian local factors, not just domains or dual rings. It also gives an exact local Gorenstein selection criterion and proves finiteness and discreteness of the resulting space. It is therefore not an assertion that every Artinian factor contributes a point.

The proof uses standard algebraic results: Nakayama's lemma, Krull's intersection [2], clopen-idempotent decomposition, and the classical Artinian Gorenstein socle criterion [3]. They are not proposed as new statements. Earlier uses of “coprime submodule” in module theory refer to different definitions and are not interchangeable with [1].

## Limitations

The theorem requires commutativity, identity, and Noetherianity; it does not classify coprime spectra of arbitrary non-Noetherian rings. In particular, [1] gives a non-Noetherian example with Sierpinski-type topology, showing discreteness is not universal beyond this scope. The source comparison covers the motivating paper's accessible introduction, fundamental results, and advertised dual-ring theorem, along with targeted searches; it does not exhaust unindexed prior literature. Small-field enumeration is finite corroboration only. No independent mathematical audit has been performed.

## References

[1] F. Murphy-Hernandez and E. Leon-Rodriguez, *The Coproduct of Ideals and the Coprime Spectrum*, arXiv:2609.23351, first public September 20, 2026. https://arxiv.org/abs/2609.23351

[2] The Stacks Project, Lemma 10.51.4, *Krull's intersection theorem* (Tag 00IP). https://stacks.math.columbia.edu/tag/00IP

[3] Classical characterization of zero-dimensional Gorenstein local rings by their one-dimensional socle; see standard treatments of Artinian Gorenstein rings (the characterization is used, not claimed as new).
