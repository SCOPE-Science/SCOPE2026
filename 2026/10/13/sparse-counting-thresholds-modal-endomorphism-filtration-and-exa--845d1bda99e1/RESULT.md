# Sparse counting thresholds, modal endomorphism filtration, and exact retraction supports on finite S5 frames

## Finding
Let \(X=\bigsqcup_{i=1}^{m}C_i\) be a nonempty finite equivalence frame, where \(a_i=|C_i|\ge1\), and fix an integer \(k\ge2\). On its powerset Boolean algebra define the counting operations
\[
D_j(U)=\{x\in X:|U\cap[x]|\ge j\}.
\]
Consider the algebra \(\mathcal A_k(X)=(\mathcal P(X),\cap,\cup,\neg,\varnothing,X,D_1,D_k)\). An endomorphism is required to preserve every displayed operation.

**Sparse-grade endomorphism theorem.** Every endomorphism is uniquely \(h_f(U)=f^{-1}(U)\) for a function \(f:X\to X\). Such \(h_f\) is an endomorphism if and only if, for every source class \(C_i\), the restriction \(f|_{C_i}\) surjects onto some entire target class \(C_j\), and
\[
\begin{cases}
 a_j\le a_i\quad\text{(with arbitrary surjection)},&a_i<k,\\
 a_j=a_i\quad\text{and }f|_{C_i}\text{ is bijective},&a_i\ge k.
\end{cases}
\]
In particular, the endomorphism monoids form the nested filtration
\[
\operatorname{End}(\mathcal A_k(X))\subseteq\operatorname{End}(\mathcal A_{k+1}(X)),
\]
which is strict **exactly when** at least one class has size \(k\) and at least one class has size smaller than \(k\). In contrast, preserving \(D_1,D_2,\ldots,D_K\) for any \(K\ge2\) imposes exactly the same restrictions as preserving \(D_1,D_2\).

Put \(S(a,b)\) for a Stirling number of the second kind (zero when \(b>a\)), and define the nonnegative integer matrix
\[
w_{ij}^{(k)}=\begin{cases}
a_j!S(a_i,a_j),&a_i<k,\ a_i!,&a_i\ge k\text{ and }a_j=a_i,\\0,&\text{otherwise}.
\end{cases}
\]
Then the exact number of endomorphisms is
\[
\boxed{\quad E_k=\prod_{i=1}^{m}\sum_{j=1}^{m}w_{ij}^{(k)}.\quad}
\]
More precisely, for \(J\subseteq\{1,\ldots,m\}\), define \(Q_k(J)=\prod_{i=1}^{m}\sum_{j\in J}w_{ij}^{(k)}\), with \(Q_k(\varnothing)=0\). For nonempty \(J\), the exact number of endomorphisms with \(f(X)=\bigcup_{j\in J}C_j\) is
\[
\boxed{\quad B_k(J)=\sum_{K\subseteq J}(-1)^{|J|-|K|}Q_k(K).\quad}
\]
Hence the exact cardinality spectrum of their image Boolean algebras is encoded by
\[
\boxed{\quad\sum_{\varnothing\ne J\subseteq[m]} B_k(J)\,z^{2^{\sum_{j\in J}a_j}}.\quad}
\]
The idempotent endomorphisms with image supported on precisely the classes indexed by \(J\) are counted by
\[
\boxed{\quad I_k(J)=\prod_{i\notin J}\sum_{j\in J}w_{ij}^{(k)}.\quad}
\]
A nonempty set of class indices \(J\) supports an idempotent exactly when it contains a class of **each distinct size at least \(k\)** and, if any class has size below \(k\), it contains a class of the **globally smallest class size**. If \(c_s\) is the number of classes of size \(s\), the number of possible idempotent supports is
\[
\begin{cases}
(2^{c_{s_0}}-1)\,2^{\sum_{s_0<s<k}c_s}\prod_{s\ge k:c_s>0}(2^{c_s}-1),&s_0=\min_i a_i<k,\\
\prod_{s\ge k:c_s>0}(2^{c_s}-1),&\min_i a_i\ge k.
\end{cases}
\]
All products over empty sets equal one. Distinct supports with the same sum of class sizes may have the same image-algebra cardinality, and the displayed polynomials add their multiplicities.

For class sizes \((1,2,3)\), the endomorphism counts at thresholds \(k=2,3,4\) are \(12,18,39\), respectively. At \(k=3\) the only idempotent supports are the union of the size-one and size-three classes and the union of all three classes, giving image-algebra sizes \(16\) and \(64\).

## Assumptions and scope
The underlying frame is a finite nonempty equivalence relation with its **actual labelled classes**; classes of equal sizes remain distinct target choices. The Boolean reduct includes constants and complement, and maps must preserve both \(D_1\) and the single additional \(D_k\). The order and cardinality of the source and target are fixed; the result concerns endomorphisms on one powerset algebra, not equivalences of pointed formulas, arbitrary neighbourhood coalgebras, or all non-unital Boolean maps.

## Proof
**Step 1: finite Boolean representation.** Every unital Boolean homomorphism \(h:\mathcal P(X)\to\mathcal P(X)\) has the form \(h(U)=f^{-1}(U)\) for a unique function \(f:X\to X\). Indeed, the disjoint sets \(h(\{y\})\), for \(y\in X\), partition \(X\); set \(f(x)=y\) precisely when \(x\in h(\{y\})\). Finite additivity then proves the identity for arbitrary subsets.

**Step 2: the ordinary existential grade.** Write \([x]\) for the equivalence class of \(x\). For every \(x\in X\) and \(U\subseteq X\), preservation of \(D_1\) is the statement
\[
U\cap[f(x)]\ne\varnothing\quad\Longleftrightarrow\quad U\cap f([x])\ne\varnothing.
\]
By testing singleton \(U\), this is equivalent to the equality \(f([x])=[f(x)]\). Thus each class \(C_i\) is mapped surjectively onto one whole class \(C_j\); different source classes may independently select targets.

**Step 3: the isolated grade \(k\).** For such a surjection, let the source and target sizes be \(a\) and \(b\), with \(b\le a\). If \(a<k\), both source and target contain fewer than \(k\) points, so both \(D_k\) tests are identically false. If \(a\ge k>b\), take \(U=C_j\); the target has fewer than \(k\) points but the source sees all \(a\ge k\) points in its inverse image, contradicting preservation. If \(a\ge k\) and \(b\ge k\) but the surjection is not injective, choose a target value with at least two preimages. Extend that value to a subset \(U\subseteq C_j\) of exactly \(k-1\) target elements (possible since \(b\ge k\)). Its preimage has at least \(k\) elements, again contradicting preservation. Thus the map must be bijective and \(a=b\). Conversely, a bijection preserves all intersection cardinalities; the small-class case preserves both grades vacuously. This proves the precise classification.

**Step 4: threshold filtration and its strictness.** Increasing the isolated threshold from \(k\) to \(k+1\) only releases the classes of size exactly \(k\), which can newly map onto strictly smaller target classes. Such a target exists if and only if some class has size less than \(k\). Every other source class has the same restrictions before and after, proving both inclusion and its strictness criterion. For the cumulative family including \(D_2\), Step 3 forces every class map to be a bijection onto a same-size class, including the singleton classes, so every other counting grade is automatically preserved.

**Step 5: endomorphism and exact-image counts.** For fixed source \(C_i\) and target \(C_j\), when \(a_i<k\) the number of surjections is \(a_j!S(a_i,a_j)\). In the large-class case the only choices are \(a_i!\) bijections to an equally large target. This proves the matrix formula for \(w^{(k)}_{ij}\). Restrictions on distinct source classes are independent, proving \(E_k\) and \(Q_k(J)\). Inclusion-exclusion over classes that fail to be hit among \(J\) proves \(B_k(J)\). Since each class map is onto its selected class, \(f(X)\) is exactly the union of the selected target classes, and the range of \(h_f\) has \(2^{|f(X)|}\) elements, proving the spectrum polynomial.

**Step 6: idempotents.** Since \(h_f\circ h_f=h_{f\circ f}\), idempotence is equivalent to \(f^2=f\). For a function, this is equivalent to fixing each point of \(f(X)\). Thus each selected class is pointwise fixed, and each unselected class may choose any admissible surjection to any selected class. Multiplication gives \(I_k(J)\). Every large class of size \(s\ge k\) may map only to an equal-size class, forcing \(J\) to contain at least one class of each such size. If small classes exist and \(s_0\) is their minimum size, an omitted class of size \(s_0\) can map only to a selected class of the same size, so a minimum class must be retained. Conversely, a selected minimum-size class receives surjections from every omitted small class, and a selected class of each large size receives bijections from omitted classes of that size. This proves the criterion. Counting nonempty selections of compulsory sizes and arbitrary selections of other small sizes gives the displayed support count.

## Verification
The standalone \(`verify.py`\) exhaustively enumerates all \(75\) set partitions on sets of size at most five, across \(340\) class-structure and threshold instances. It compares direct preservation of \(D_1\) and \(D_k\), tested on **every subset**, against the structural criterion for each of \(828282\) function/threshold combinations; independently checks the endomorphism counts, exact-image polynomials, and idempotent counts; and checks \(265\) strictness comparisons. A separate six-point computation checks the \((1,2,3)\) boundary case. Output:

```text
VERIFY_OK partition_shapes 75 grade_instances 340 function_grade_comparisons 828282 endomorphism_instances 28803 idempotent_instances 3748 distinct_nonzero_rank_cases 931 filtration_jump_comparisons 265 boundary_counts_1_2_3 [12, 18, 39]
```

Run with \(`python verify.py`\) using standard-library Python 3. These finite experiments are not substitutes for the general proof above. The verifier does not enumerate larger frames exhaustively.

## Relationship to prior work
The finite Boolean duality and ordinary modal bounded-map condition are classical. The modal-algebra endomorphism case with only existential modality \(D_1\) also precedes this result. Otto's 2019 treatment of graded modalities and counting bisimulation, Chen–van Ditmarsch–Greco–Tzimoulis's 2021 graded neighbourhood semantics, and the multiset-coalgebra perspective provide important foundational related work. General finite-multiset coalgebra morphisms preserving all grades enforce multiplicity preservation; they do not directly give the sparse single-threshold filtration and its exact image/support census. Comer's 2024 modal Lovász theorems concern homomorphism counts characterizing graded-logical equivalence, not endomorphisms of this finite Boolean algebra.

The 2022 AiML study of graded modal logic with a single modality gives a particularly plausible terminological antecedent. Available abstract and conclusion describe axiomatics/expressive power for logics with a single threshold. Its full paper was not available for complete comparison here, and an equivalent algebraic characterization in older literature remains possible. No originality is claimed for Stirling-number surjection counts, Boolean inverse-image duality, general graded modalities, or full-multiset preservation. The proposed advance is their precise **sparse-grade filtration, strictness criterion, exact supported-image census, and idempotent support staircase** on finite equivalence frames.

## Limitations
All frames are finite, all Boolean homomorphisms are unital, and the two named operations include \(D_1\). A language containing only \(D_k\), without \(D_1\), is not classified here. This statement is not a classification of general graded neighbourhood coalgebras or infinite S5 models. Different frame sizes and repeated image-algebra cardinalities require the explicit multiplicities in the formulas. No publication-priority assertion, independent proof validation, or exhaustive historical novelty claim is made.

## References
1. Martin Otto, *Graded Modal Logic and Counting Bisimulation*, arXiv:1910.00039, initial public version 2019-09-30. https://arxiv.org/abs/1910.00039
2. Jinsheng Chen, Hans van Ditmarsch, Giuseppe Greco, Apostolos Tzimoulis, *Neighbourhood Semantics for Graded Modal Logic*, arXiv:2105.09202 (2021). https://arxiv.org/abs/2105.09202
3. Jesse Comer, *Lovász Theorems for Modal Languages*, arXiv:2404.15421 (2024). https://arxiv.org/abs/2404.15421
4. Mattia Panettiere and Apostolos Tzimoulis, *Graded Modal Logic with a Single Modality*, Advances in Modal Logic 14 (2022), 643–658.
5. *PSpace Bounds for Rank-1 Modal Logics* (2006), finite-multiset functor semantics (background).
6. Yde Venema, *Algebras and Coalgebras*, lecture notes, discussion of finite modal algebras and bounded morphisms (background).
