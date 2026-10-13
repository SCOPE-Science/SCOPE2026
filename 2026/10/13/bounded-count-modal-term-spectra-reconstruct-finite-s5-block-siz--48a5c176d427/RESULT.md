# Bounded-count modal term spectra reconstruct finite S5 block sizes

## Finding
Let \(X\) be a nonempty finite equivalence frame, and let \(S_X\subseteq\mathbb Z_{>0}\) be the **set of distinct sizes** of its equivalence classes; repetitions are deliberately discarded. For a fixed integer \(K\ge1\), put
\[
D_j(U)=\{x\in X:|U\cap[x]|\ge j\},\qquad 1\le j\le K,
\]
where \([x]\) is the equivalence class of \(x\). Consider the Boolean set algebra \(\mathcal P(X)\) expanded by these \(K\) graded modalities and let \(T_{X,K}(r)\) count its distinct \(r\)-ary term operations, including nullary operations when \(r=0\).

**Spectral reconstruction theorem.** For any two such nonempty finite frames \(X,Y\) and fixed \(K\),
\[
\bigl(\forall r\ge0:\ T_{X,K}(r)=T_{Y,K}(r)\bigr)
\quad\Longleftrightarrow\quad
\begin{cases}
\max S_X=\max S_Y,&K=1,\\
S_X=S_Y,&K\ge2.
\end{cases}
\]
No arity-wise term-operation count detects multiplicities of equivalence classes having the same size. The jump from the ordinary possibility modality \(D_1\) to allowing \(D_2\) therefore changes exactly which block-size information is recoverable: all distinct sizes, rather than only the largest.

Here is an explicit exact census behind the theorem. Set \(q=2^r\), \(M=\max S_X\), and write \([z^s]F(z)\) for the coefficient of \(z^s\). Define
\[
 B_K(z)=\sum_{i=0}^Kz^i,\quad C_K(z)=\sum_{i=1}^Kz^i,
 \quad B_{K-1}(z)=\sum_{i=0}^{K-1}z^i,\quad
 C_{K-1}(z)=\sum_{i=1}^{K-1}z^i.
\]
(The final sum is zero for \(K=1\).) Then
\[
\begin{split}
E_{S_X,K}(q)=q\Bigg(&\sum_{s\in S_X}[z^s]C_{K-1}(z)B_{K-1}(z)^{q-1}\\
&+\sum_{s=0}^{M}[z^s]\Bigl(C_K(z)B_K(z)^{q-1}
-C_{K-1}(z)B_{K-1}(z)^{q-1}\Bigr)\Bigg),
\end{split}
\]
and the exact number of term operations is
\[
\boxed{T_{X,K}(r)=2^{E_{S_X,K}(2^r)}.}
\]
All term operations admit equivalent formulas of modal nesting depth at most one. The census and the classification include \(r=0\).

As a concrete separation, one frame with only two-point classes and another with both singleton and two-point classes have the same ordinary arity-one term-operation count \(2^4=16\). When \(D_2\) is present the corresponding counts are \(2^4=16\) and \(2^6=64\), respectively. The distinction is not visible to any ordinary arity-wise term count.

## Assumptions and scope
The language has Boolean operations (including Boolean constants) and exactly the counting operators \(D_1,\ldots,D_K\). The relations are equivalence relations; the frame is nonempty and finite, but has arbitrarily many, possibly repeated, block sizes. A term operation is a function \(\mathcal P(X)^r\to\mathcal P(X)\) induced by a formal term, not a map of pointed models or a homomorphism between frames. Equality of the sequences of operation **counts** is the invariant being classified; the theorem does not claim that such algebras are isomorphic. \(K\) is fixed when frames are compared. No graded modalities of threshold greater than \(K\), counting across equivalence classes, or global modalities are present.

## Proof
Write the \(r\) Boolean input predicates as one partition of \(X\) into \(q=2^r\) possibly empty propositional color classes. At \(x\in X\), let \(c\in[q]\) be the color of \(x\), let \(m_i\) be the number of color-\(i\) elements in \([x]\), and set \(t_i=\min(K,m_i)\). Thus \(t=(t_1,\ldots,t_q)\in\{0,\ldots,K\}^q\), with \(t_c\ge1\).

**Lemma 1 (depth-one types).** Two pointed input configurations, possibly from different frames, agree on every term in this language if and only if their pairs \((c,t)\) agree. The forward direction follows from explicitly isolating the color \(c\) by an input Boolean minterm \(\chi_c\), then isolating each clipped count by \(D_{t_i}(\chi_i)\wedge\neg D_{t_i+1}(\chi_i)\) when \(1\le t_i<K\), by \(\neg D_1(\chi_i)\) when \(t_i=0\), and by \(D_K(\chi_i)\) when \(t_i=K\). Their conjunction, including \(\chi_c\), is a depth-one characteristic formula for \((c,t)\). Conversely, induction on terms shows that their truth at a state is a function of \((c,t)\): each lower-complexity formula selects, uniformly within any class having histogram \(t\), some set of input colors; its number of satisfying elements, truncated at \(K\), is determined by \(t\). Every Boolean combination of the characteristic formulas is therefore a term, and every term is such a combination. This proves both the depth-one assertion and the operation count \(2^{\#\text{realizable pointed types}}\).

**Lemma 2 (realizability).** A candidate \((c,t)\) is realizable over some class size in \(S_X\) precisely when \(t_c\ge1\) and either (i) no coordinate of \(t\) is \(K\) and \(\sum_i t_i\in S_X\), or (ii) at least one coordinate equals \(K\) and \(\sum_i t_i\le M\). Indeed, in case (i) the actual histogram must equal \(t\); in case (ii) any additional \(M-\sum_i t_i\) elements can be assigned to a coordinate already capped at \(K\). Choosing one element of the required color as the distinguished point completes the construction. A finite frame can realize all these local configurations by varying its input predicates independently from one trial to the next.

A fixed distinguished color has truncated coordinate in \(\{1,\ldots,K\}\), while its \(q-1\) companions lie in \(\{0,\ldots,K\}\). The second summation in the displayed formula counts the capped histograms with total truncated mass at most \(M\), by subtracting all histograms whose coordinates are strictly below \(K\). The first summation counts uncapped histograms of total mass belonging to \(S_X\). Multiplying by the \(q\) choices for the distinguished color gives \(E_{S_X,K}(q)\). Lemmas 1 and 2 give the exact census.

**Lemma 3 (polynomial fingerprints).** Suppose \(K\ge2\). Put
\[
 A_s(q)=[z^s]C_{K-1}(z)B_{K-1}(z)^{q-1},
\qquad
 R_{M,K}(q)=\sum_{s=0}^{M}[z^s]
 \bigl(C_K(z)B_K(z)^{q-1}-C_{K-1}(z)B_{K-1}(z)^{q-1}\bigr).
\]
For every fixed \(s\ge1\), \(A_s(q)\) is a rational polynomial in \(q\) of degree exactly \(s-1\), with leading coefficient \(1/(s-1)!\). To see this, the highest-degree contribution selects the distinguished color once and selects \(s-1\) other, pairwise distinct colors once each; any repeated count uses fewer independently selectable colors. In \(R_{M,K}\), a capped histogram consumes at least \(K\) units at one color, leaving at most \(M-K\) distinct freely chosen companion colors. Therefore \(R_{M,K}(q)\) has degree at most \(M-K\) (or vanishes if \(M<K\)). In particular, \(E_{S_X,K}(q)/q\) has degree \(M-1\), with leading coefficient \(1/(M-1)!\).

If two spectra for \(K\ge2\) agree for every \(q=2^r\), their rational polynomials agree identically. Comparing degrees first recovers \(M\), because a polynomial of degree \(M-1\) cannot equal one of another degree. Their common \(R_{M,K}\) cancels. If the underlying size sets differ, choose the largest \(s\) in their symmetric difference: the difference of the \(A_s\)-sums then has nonzero leading term of degree \(s-1\). Hence the sets must coincide. Conversely, equal sets have equal formulas.

For \(K=1\), the first summation vanishes, while a clipped histogram is just its nonempty color support. Thus
\[
\frac{E_{S_X,1}(q)}q=\sum_{j=0}^{M-1}\binom{q-1}{j}.
\]
This depends only on \(M\) and is a polynomial of degree \(M-1\) with positive leading coefficient. Equality on all \(q=2^r\) therefore recovers exactly \(M\), completing the classification. Repeated blocks of the same size never enter the realizability condition and are invisible for every \(K\).

## Verification
The included standalone Python program `verify.py` checks the exact coefficient formula against explicit enumeration of colored equivalence classes; compares the proposed depth-one pointed types with finite graded-modal partition refinement on several multi-block frames; directly constructs the Boolean algebra of unary term operations from all valuations in nine small frames; and tests the polynomial reconstruction criterion for all nonempty size sets contained in \(\{1,\ldots,5\}\) at a large alphabet. Running `python3 verify.py` reports:

```
VERIFY_OK formula_cases 496 exhaustive_valuations 114816 partition_refinement_states 5862 term_algebra_instances 9 term_algebra_pointed_states 162 spectral_reconstruction_checked True
```

The program uses only the Python standard library. The experiments are finite checks and do not replace Lemmas 1–3 or the polynomial identity argument. In particular the final identification of **all** finite spectra follows from polynomial equality at infinitely many arities, not from the finitely tested alphabet sizes.

## Relationship to prior work
Otto, *Graded modal logic and counting bisimulation* (first public version 30 September 2019, arXiv:1910.00039), develops graded back-and-forth and finite-depth expressive completeness; this supplies an established general conceptual framework for distinguishability, not the finite-S5 term-operation spectrum or its arity-profile reconstruction dichotomy. Chen, van Ditmarsch, Greco, and Tzimoulis, *Neighbourhood semantics for graded modal logic* (first public version 19 May 2021, arXiv:2105.09202), studies alternative semantics and graded bisimulation, including its connection to graded epistemic S5 modalities; it does not supply the exact coefficient count or the classification of block-size sets by term counts.

The one-equivalence-class special case of the clipped-histogram census is already known in related finite modal-algebra counting work. We do **not** claim that clipped histograms, graded modalities, or finite bisimulation are new. The claim here is the precise reconstruction threshold across *arbitrary finite disjoint S5 clusters*, with exact arity-wise invariants and a proof separating \(K=1\) from \(K\ge2\). An equivalent prior clone-classification theorem in older graded epistemic or universal-algebra literature remains a possibility.

## Limitations
Only finite equivalence frames and fixed finite threshold \(K\) are treated. The term counts cannot detect the multiplicities of blocks of any given size, and the theorem does not reconstruct a frame up to isomorphism. Equal term counts at a single arity need not recover the stated information: the classification uses every arity, equivalently equality of the resulting polynomial functions. The result does not address arbitrary relations, unbounded counting modalities in the signature, or infinite frames. The verification is same-model and computationally finite; independent mathematical and originality validation has not been performed.

## References
1. M. Otto, *Graded modal logic and counting bisimulation*, arXiv:1910.00039, first public 2019-09-30; version 2 dated 2023-07-18. https://arxiv.org/abs/1910.00039
2. J. Chen, H. van Ditmarsch, G. Greco, A. Tzimoulis, *Neighbourhood semantics for graded modal logic*, arXiv:2105.09202, first public 2021-05-19. https://arxiv.org/abs/2105.09202
