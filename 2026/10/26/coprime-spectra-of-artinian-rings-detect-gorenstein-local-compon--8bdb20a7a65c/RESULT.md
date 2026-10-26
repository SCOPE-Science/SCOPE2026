# Coprime spectra of Artinian rings detect Gorenstein local components

## Finding

Let \(R\) be a nonzero commutative Artinian ring with identity. Following Murphy-Hernandez and Leon-Rodriguez [1], define the coproduct of two ideals by
\[
[I:J]=(J:\operatorname{ann}_R(I))
\]
and call a nonzero ideal \(C\) *coprime* when, for all ideals \(I,J\) of \(R\),
\[
C\subseteq[I:J]\quad\Longrightarrow\quad
C\subseteq I\ \text{or}\ C\subseteq J.
\]
Write \(\operatorname{CoSp}(R)\) for the set of coprime ideals with closed subsets
\(V_c(K)=\{C\in\operatorname{CoSp}(R):C\subseteq K\}\).

**Classification theorem.** Decompose \(R\) canonically up to permutation into its finitely many local Artinian factors,
\[
R\cong\prod_{i=1}^{s}(R_i,\mathfrak m_i),\qquad
k_i=R_i/\mathfrak m_i,
\qquad S_i=\operatorname{ann}_{R_i}(\mathfrak m_i).
\]
Then the complete collection of coprime ideals is
\[
\boxed{\operatorname{CoSp}(R)=\{0\times\cdots\times S_i\times\cdots\times0:
\dim_{k_i}S_i=1\}.}
\]
In particular, a local Artinian ring has one coprime ideal, namely its socle, if it is Gorenstein; otherwise it has none. The annihilator map is a canonical homeomorphism
\[
\boxed{\operatorname{CoSp}(R)\ \longrightarrow\
\{\mathfrak p\in\operatorname{Spec}(R):R_{\mathfrak p}\text{ is Gorenstein}\},
\quad C\longmapsto\operatorname{ann}_R(C).}
\]
Both spaces in this homeomorphism have the discrete topology. Thus the cardinality of the coprime spectrum is exactly the number of Gorenstein factors of an arbitrary commutative Artinian ring, including mixed Gorenstein/non-Gorenstein products.

For example, for any field \(k\), the square-zero local ring \(k[x,y]/(x,y)^2\) has empty coprime spectrum, whereas
\[
k[t]/(t^3)\times k[x,y]/(x,y)^2
\]
has a one-point coprime spectrum despite having two maximal ideals.

## Assumptions and scope

All rings are commutative, associative, and unital. Artinian refers to the descending chain condition on ideals; the residue fields may be infinite and the rings need not contain a field. The zero ring is excluded for convenience (its spectrum and coprime spectrum are both empty). The primary MSC2020 subject is \(13A15\). The Gorenstein criterion used here is the standard zero-dimensional local criterion: \((R_i,\mathfrak m_i)\) is Gorenstein precisely when its socle \(S_i=0:\mathfrak m_i\) is one-dimensional over its residue field [3].

The central content is the determination of coprime ideals in *non-dual* local Artinian rings and the behavior of the coproduct under arbitrary finite local products. The dual/Gorenstein special case and the definition of the spectrum are already established in [1].

## Proof

**Step 1: essential socle and annihilator of a socle line.** Let \((A,\mathfrak m,k)\) be a nonzero Artinian local ring and let \(S=\operatorname{ann}_A(\mathfrak m)\). The maximal ideal \(\mathfrak m\) is nilpotent [2]. Therefore \(S\ne0\). For every nonzero ideal \(I\), choose a maximal integer \(j\ge0\) with \(\mathfrak m^j I\ne0\). Then
\[
0\ne\mathfrak m^jI\subseteq I\cap S.
\]
Consequently, when \(\dim_kS=1\), every nonzero ideal contains \(S\).

For any one-dimensional \(k\)-subspace \(L\subseteq S\), the subspace \(L\) is a minimal nonzero ideal of \(A\). It is annihilated by \(\mathfrak m\) and cannot be annihilated by a unit, so
\[
\operatorname{ann}_A(L)=\mathfrak m.
\]

**Step 2: local exclusion certificate.** Let \(C\ne0\) be an ideal of \(A\) that is not equal to the unique socle line (or suppose no unique socle line exists). Choose a one-dimensional subspace \(L\subseteq S\) with \(C\not\subseteq L\): when \(\dim_kS\ge2\), this is possible for every \(C\ne0\), while when \(\dim_kS=1\) it is possible exactly for \(C\ne S\), by Step 1.

Put \(I=L\) and \(J=\mathfrak m C\). Using \(\operatorname{ann}(I)=\mathfrak m\), we obtain
\[
C\operatorname{ann}(I)=C\mathfrak m=J,
\qquad\text{hence}\qquad
C\subseteq(J:\operatorname{ann}(I))=[I:J].
\]
By construction \(C\not\subseteq I\). Also \(C\not\subseteq\mathfrak m C=J\): otherwise \(C=\mathfrak m C\), contradicting Nakayama's lemma, since \(C\) is finitely generated and nonzero. Hence \(C\) is **not** coprime. This explicit pair \((I,J)\) excludes every ideal except the sole socle line when it exists.

**Step 3: the unique socle line is coprime.** Assume \(\dim_kS=1\). Let \(S\subseteq[I:J]\). If \(I\ne0\), Step 1 gives \(S\subseteq I\). If \(I=0\), then
\[
[0:J]=(J:\operatorname{ann}(0))=(J:A)=J,
\]
so \(S\subseteq J\). This proves coprimality and finishes the local classification, also covering the field case \(\mathfrak m=0\), where \(S=A\).

**Step 4: product decomposition.** By the Artinian decomposition theorem [2], write \(R=\prod_{i=1}^sR_i\). Every ideal and every annihilator is a coordinatewise product, and
\[
[I:J]_R=\prod_{i=1}^s[I_i:J_i]_{R_i}.
\]
If an ideal \(C=\prod C_i\) has nonzero coordinates at two or more indices, choose one such index \(i\), let \(e_i\) be the corresponding central primitive idempotent, and put \(I=e_iR\), \(J=(1-e_i)R\). Then \(\operatorname{ann}(I)=J\) and
\[
[I:J]=(J:J)=R,
\]
although \(C\not\subseteq I\) and \(C\not\subseteq J\). Thus \(C\) is not coprime. If exactly one coordinate of \(C\) is nonzero, the defining condition for coprimality is equivalent, by the coordinatewise formula, to coprimality of that one coordinate in its local ring. Applying Steps 2 and 3 gives precisely the displayed classification.

**Step 5: annihilator and topology.** When \(S_i\) has dimension one, its annihilator inside \(R_i\) is \(\mathfrak m_i\), by Step 1. The annihilator of the corresponding coordinate ideal \(C_i\subset R\) is therefore
\[
\operatorname{ann}_R(C_i)
=R_1\times\cdots\times\mathfrak m_i\times\cdots\times R_s,
\]
the maximal ideal associated with the \(i\)th local factor. These are exactly the Gorenstein points of \(\operatorname{Spec}(R)\), and the annihilator assignment is bijective. For each such \(C_i\), the closed set \(V_c(C_i)\) equals \(\{C_i\}\), because different coordinate socles are disjoint. Since the set of points is finite, all subsets are closed. The Gorenstein subset of the finite Artinian prime spectrum is likewise discrete. This proves the homeomorphism.

## Verification

The standalone program `verify.py` exhaustively enumerates ideals and checks the coprime definition, without assuming the classification. It covers six local algebras over \(\mathbb F_2\), two finite products over \(\mathbb F_2\), and four integer quotient rings in mixed or pure prime-power characteristic. The tested local examples include one-dimensional and two-dimensional socles, and products combine both types. Run from the directory containing the program:

```bash
python3 verify.py
```

The observed last line is `VERIFY_OK exhaustive_coproduct_checks=12`. In particular, \(\mathbb Z/12\mathbb Z\) has two coprime ideals while \(\mathbb F_2[x,y]/(x,y)^2\) has none. The proof above is uniform for all Artinian commutative rings; the computations are finite cross-checks rather than an argument from enumeration to an infinite statement.

## Relationship to prior work

Murphy-Hernandez and Leon-Rodriguez [1] introduce the operation \([I:J]=(J:\operatorname{ann}(I))\), coprime ideals, and their topology. Their dual-ring theorem identifies the coprime and ordinary prime spectra when the double-annihilator property holds; this includes Artinian Gorenstein rings. Their square-zero two-variable example demonstrates that a minimal nilpotent ideal can fail coprimality. The present result adds the opposite direction for *all* non-Gorenstein Artinian local rings (no coprime ideal whatsoever) and characterizes arbitrary finite products, including mixed products where the ambient ring is not Gorenstein. It thus identifies the exact subset of the prime spectrum retained by the new invariant, not merely a special counterexample.

The Artinian product theorem [2] and the zero-dimensional Gorenstein socle criterion [3] are standard inputs. A classification of irreducible ideals or a result about ordinary comaximal ideals does not by itself settle the displayed coproduct condition; its witness involves \(\operatorname{ann}(I)\) and \(\mathfrak m C\).

## Limitations

The classification is restricted to Artinian commutative rings. Neither the local essential-socle argument nor the finite-product conclusion automatically applies to non-Artinian Noetherian rings, even when a nonzero socle exists. The result does not characterize coprime spectra of arbitrary rings or claim a new notion of coprime ideal. The isomorphism of the two spaces is a homeomorphism of topological spaces, not a ringed-space or functorial equivalence. Its distinct contribution should be checked against any unindexed earlier classification in the new coprime-ideal sense.

## References

[1] F. Murphy-Hernandez and E. Leon-Rodriguez, *The Coproduct of Ideals and the Coprime Spectrum*, arXiv:2609.23351, first publicly submitted 2026-09-20, version 2 dated 2026-10-05. https://arxiv.org/abs/2609.23351

[2] The Stacks Project, *Artinian rings*, Section 10.53, Lemma 10.53.6, Tag 00JB. https://stacks.math.columbia.edu/tag/00J4

[3] The Stacks Project, *Gorenstein rings*, Section 47.21, including the zero-dimensional local criterion via \(\operatorname{Hom}_A(k,A)\). https://stacks.math.columbia.edu/tag/0DW6
