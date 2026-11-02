# Burnside classification of finite Kripke presentations of a fixed closure-modal theory

## Finding
For any nonempty **finite** closure model \(\mathcal M=(W,G,\operatorname{cl},V)\) satisfying the same-world Kripke representability condition \((\mathsf{KRep})\), there is an exact formula for the number of **isomorphism classes** of all Kripke models \((W,R,V)\) that preserve the truth of every modal formula at each labelled world of \(\mathcal M\). The formula depends only on sizes of complete modal-theory classes and the canonical successor-type support relation; it does **not** require enumerating the \(2^{|W|^2}\) binary relations.

Partition \(W\) by equality of complete pointed modal theories into nonempty classes \(T_1,\ldots,T_r\), and write \(s_i=|T_i|\). Put
\[
H_w=\operatorname{cl}(G(w)),\qquad U_w=\bigcap_{\psi\in H_w}\llbracket\psi\rrbracket_{\mathcal M}.
\]
The set \(U_w\) is a union of complete modal-theory classes, and \(U_w\) depends only on the class of \(w\). For \(w\in T_i\), define \(I_i=\{j:T_j\subseteq U_w\}\); this is well-defined. For an integer partition \(\lambda\), with multiplicity \(m_d\) of part \(d\), put
\[
z_\lambda=\prod_{d\ge1}d^{m_d}m_d!,\qquad
c_a(\lambda)=\sum_{b\in\lambda}\gcd(a,b),
\]
where the sum over \(b\in\lambda\) includes repeated parts. Then the number of isomorphism classes of same-carrier, same-valuation Kripke representations is **exactly**
\[
\boxed{
\mathcal U(\mathcal M)=
\sum_{\substack{\lambda_i\vdash s_i\\1\le i\le r}}
\left(\prod_{i=1}^r\frac1{z_{\lambda_i}}\right)
\prod_{i=1}^r\prod_{a\in\lambda_i}\prod_{j\in I_i}
\left(2^{c_a(\lambda_j)}-1\right).
}
\]
Every fixed-count factor \(2^{c_a(\lambda_j)}-1\) is an integer, and the rational sum is a nonnegative integer. An empty inner product is one. This is a **complete** isomorphism classification: the equivalence relation is ordinary valuation-preserving Kripke-model isomorphism, and two representing relations are isomorphic if and only if they lie in the same orbit of the product of symmetric groups on the modal-theory classes.

Examples are natural models with a universal original accessibility relation. If all propositional variables have constant truth values on an \(n\)-world carrier, the resulting single complete modal-theory class has \(s_1=n\) and \(I_1=\{1\}\). There are \(70\) isomorphism classes of representing relations for \(n=3\) and \(2340\) for \(n=4\). If the valuation of one atom distinguishes a two-world class from a one-world class and the original relation is universal, then \((s_1,s_2)=(2,1)\), both target classes are required at every world, and the isomorphism-class count is \(15\). For two two-world classes with universal accessibility and a distinguishing atomic valuation, it is \(1701\). The respective **labelled** counts, already determined by the earlier rowwise classification, are \(343,50625,27,6561\); they are reproduced only as controls, not claimed new.

## Assumptions and scope
The language has ordinary Boolean propositional connectives and one modal box. In the closure semantics of Nishimura, \(\mathcal M,w\models\Box\varphi\) means exactly \(\varphi\in H_w\). The finite world set \(W\) is nonempty; the generated formula sets and language may be infinite, and \(\operatorname{cl}\) may be any set operator. The model satisfies \((\mathsf{KRep})\) when, for every \(w\) and formula \(\varphi\),
\[
\varphi\in H_w\quad\Longleftrightarrow\quad U_w\subseteq\llbracket\varphi\rrbracket_{\mathcal M}.
\]
This is Nishimura's Definition 4.22, not a newly asserted theorem. The source also constructs the canonical same-world representation with successor set \(U_w\). A separate finite-model argument already classifies **labelled** representing relations by nonempty choices within each required modal-theory class. The present claim concerns the finer question of **isomorphism orbits**, not the known labelled formula.

The group \(\prod_i\operatorname{Sym}(T_i)\) is the set of all permutations of the **fixed carrier** preserving each complete modal-theory class. In particular, it preserves the atomic valuation. All isomorphism types counted have this same distinguished valuation in the sense that the candidate Kripke model is built on \((W,V)\); their worlds are not individually named after passing to isomorphism classes.

## Proof
**1. Type classes can be isolated by formulas.** If distinct worlds \(v,v'\) have different pointed modal theories, there is a formula true at one and false at the other. For any one modal-theory class \(T_i\), choose an oriented distinguishing formula against every other class, and take their finite conjunction. Since \(W\) is finite, the result is a characteristic formula \(\delta_i\) whose truth set in \(\mathcal M\) is precisely \(T_i\). Every definable truth set is a union of these classes, and every union of classes is definable by a disjunction of characteristic formulas. In particular \(U_w\) is a union of classes. Also, if \(w,w'\in T_i\), then \(\Box\psi\) has the same truth value at \(w,w'\) for every \(\psi\), so \(H_w=H_{w'}\) and \(U_w=U_{w'}\), justifying \(I_i\).

**2. Reconstruct the earlier labelled row criterion, without claiming it new.** Let \(R\) be any binary relation on \(W\). The Kripke model \((W,R,V)\) agrees with \(\mathcal M\) on the truth of **all** formulas at **all** worlds if and only if, for each \(w\), \(R[w]\) intersects precisely those modal-theory classes which \(U_w\) intersects. Necessity: agreement on \(\Box\varphi\), combined with agreement on \(\varphi\), means that for all formulas \(\varphi\),
\[
R[w]\subseteq\llbracket\varphi\rrbracket_{\mathcal M}\quad\Longleftrightarrow\quad U_w\subseteq\llbracket\varphi\rrbracket_{\mathcal M}.
\]
If \(R[w]\) meets an excluded class, a formula defining \(U_w\) disproves this equivalence. If \(R[w]\) misses a required class \(T_j\), the formula \(\neg\delta_j\) disproves it. Conversely, meeting the same classes guarantees the equivalence because every formula is constant on each class; structural induction on modal formulas then proves truth preservation. Thus, for each ordered pair \((i,j)\), if \(j\notin I_i\) the submatrix of \(R\) with source rows in \(T_i\) and target columns in \(T_j\) is identically zero; if \(j\in I_i\), every row of this binary submatrix is nonzero. The conditions on different ordered type pairs are independent.

**3. Identify the exact isomorphism group.** Any isomorphism between two such Kripke representations preserves the truth of every modal formula. Since both representations agree pointwise with \(\mathcal M\), the isomorphism must map each complete modal-theory class \(T_i\) onto itself. Conversely, every permutation acting independently inside the \(T_i\) preserves the valuation and maps allowable row-support patterns to allowable row-support patterns, because \(I_i\) depends only on the source class. The isomorphism classes are therefore precisely the conjugation orbits of
\[
\Gamma=\operatorname{Sym}(T_1)\times\cdots\times\operatorname{Sym}(T_r)
\]
on the set of allowable binary relations.

**4. Fixed relation count for a prescribed permutation.** Fix \(\sigma=(\sigma_1,\ldots,\sigma_r)\in\Gamma\). Consider a required ordered type pair \((i,j)\), so its \(s_i\)-by-\(s_j\) binary block has no empty row. Take a cycle of length \(a\) of the row permutation \(\sigma_i\), and choose the neighbors in \(T_j\) of one representative source row. Invariance under \(\sigma\) determines every other row in that source cycle. Consistency after the full row cycle is equivalent to the chosen target subset being invariant under \(\sigma_j^a\). Such a subset is a union of cycles of \(\sigma_j^a\); it is nonempty in exactly
\[
2^{\#\operatorname{cycles}(\sigma_j^a)}-1
\]
ways. Source row cycles give independent choices. This argument remains valid when \(i=j\), where the *same* permutation acts simultaneously on row and column indices. An excluded block has exactly one fixed choice (the all-zero block). Hence the number of relations fixed by \(\sigma\) is
\[
\prod_{i=1}^r\prod_{a\in\operatorname{cyc}(\sigma_i)}\prod_{j\in I_i}
\left(2^{\#\operatorname{cycles}(\sigma_j^a)}-1\right).
\]

**5. Apply Burnside's lemma and eliminate explicit permutations.** If \(\sigma_j\) has cycle-type partition \(\lambda_j\), a cycle of length \(b\) splits into \(\gcd(a,b)\) cycles under the power \(\sigma_j^a\). Thus \(\#\operatorname{cycles}(\sigma_j^a)=c_a(\lambda_j)\). There are \(s_j!/z_{\lambda_j}\) permutations of that cycle type on \(T_j\). Burnside's orbit formula is the mean of the fixed-relation count over \(\Gamma\). Grouping the permutations by the tuple of cycle-type partitions gives exactly the displayed sum. This also proves integrality and completes the classification.

**6. Worked values and small exact checks.** For a single type of size \(3\) with nonempty successor row at every world, the three cycle types contribute fixed counts \(343\), \(21\), and \(7\); their conjugacy-class multiplicities are respectively \(1,3,2\). Therefore the orbit count is \((343+3\cdot21+2\cdot7)/6=70\). For a single type of size \(4\), the cycle types \((1,1,1,1)\), \((2,1,1)\), \((2,2)\), \((3,1)\), \((4)\) have fixed counts \(50625,735,225,45,15\) and multiplicities \(1,6,3,8,6\), so the orbit count is \(2340\). For required supports between two type classes of sizes \((2,1)\) and \((2,2)\), the same formula gives \(15\) and \(1701\), respectively.

## Verification
Run `python3 checker.py` with the standard Python library. The verifier independently (a) evaluates the partition-sum formula using exact rational arithmetic, (b) directly enumerates every allowed relation in four finite configurations and computes its orbit using actual permutations, and (c) on three worlds, independently checks preservation of **all** modal formulas by saturating pairs of original/candidate truth-set masks under the Boolean operations and box operators until a finite fixed point is reached. Part (c) is not depth-limited: saturation accounts for arbitrarily nested finite modal formulas. Its three valuation tests return the expected labelled counts \(343,27,1\). Parts (a) and (b) return exactly \((343,70)\), \((50625,2340)\), \((27,15)\), and \((6561,1701)\) for (labelled,unlabelled) counts. The complete checker returned `ALL_CHECKS_OK`.

These computations verify the finite-cycle count and sample semantic equivalences. The symbolic proof establishes the formula for arbitrary finite modal-type partitions and admissible successor-support patterns; finite experiments are not used as infinite proofs. The code does not provide an effective procedure for extracting the complete modal-theory classes from an arbitrary encoded closure operator.

## Relationship to prior work
Nishimura (2026) defines \((\mathsf{KRep})\), proves implications to normal modal conditions, and constructs a canonical truth-preserving Kripke relation on the same worlds. The **finite labelled** classification of all such relations, using intersections with complete modal-theory classes, is already known and is reconstructed in proof step 2 as input rather than offered as new. The result assessed here is the full **unlabelled** classification, including the coupled row/column permutation fixed-point formula, which is not supplied by a labelled product count or by existence of a canonical relation. Burnside's lemma and symmetric-group cycle-type counts are classical tools, not claimed as original. Enumeration of serial directed graphs without marked types supplies familiar small special cases, but does not by itself state the general modal-theory support-indexed orbit formula.

Searches compared same-world Kripke representation, modal-theory class multiplicities, and fixed-relation orbits against relevant published mathematical records and semantic-index entries. Generic Pólya and graph-species counting results could conceivably imply the formula when specialized to block-coloured digraphs; that possible historical coverage, and the classification's dependence on the already established row-support criterion, are explicit limitations on originality. No absolute uniqueness assertion is made.

## Limitations
The formula counts **isomorphism classes** only inside the set of Kripke relations that preserve every modal formula's truth at each labelled original world. It is not a count of all frames validating the same modal formulas, nor a classification of every Kripke frame up to modal equivalence under arbitrary valuations. Its group acts within complete pointed theory classes; arbitrary permutations that interchange different types are not valuation-preserving modal isomorphisms in this fixed-model problem. It assumes a finite carrier and the source's exact \((\mathsf{KRep})\) condition, not merely the weaker frame \((\mathsf G)+(\mathsf K)\). Standard general directed-graph cycle-index theory may contain a stronger specialization, and no independently audited historical-priority determination is claimed.

## References
1. Y. Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations*, arXiv:2610.01433v1, first publicly posted 1 October 2026; Definition 2.2, Definition 4.22, Theorem 4.30. https://arxiv.org/abs/2610.01433.
2. Burnside's orbit-counting lemma and the symmetric-group conjugacy-class formula \(s!/z_\lambda\) are standard enumerative results. Their use is reconstructed explicitly above; no new general orbit-counting theorem is asserted.
