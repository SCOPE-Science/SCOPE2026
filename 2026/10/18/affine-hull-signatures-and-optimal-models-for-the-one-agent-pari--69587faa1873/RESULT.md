# Affine-hull signatures and optimal models for the one-agent parity fragment of \(\mathsf{S5}\)

## Finding

**Theorem (exact pointed theories, optimal compression, and census).** Fix an integer \(n\ge1\) and propositional variables \(p_1,\ldots,p_n\). Let \(\mathcal L_{\oplus}^{\mathsf{S5}}\) be the language built using these variables, Boolean constants \(\top,\bot\), exclusive-or \(\oplus\), negation \(\neg\), and the two standard modalities \(\Box,\Diamond\) for one accessibility relation. In any pointed \(\mathsf{S5}\) Kripke model \((M,w)\), write \(a\in\mathbb F_2^n\) for the propositional truth vector at \(w\), \(X\subseteq\mathbb F_2^n\) for the nonempty set of distinct truth vectors represented in its accessibility-equivalence class, and \(H=\operatorname{aff}(X)\) for the affine span over the field of two elements.

1. Two pointed models, whether finite or infinite, satisfy the same formulas of \(\mathcal L_{\oplus}^{\mathsf{S5}}\) **if and only if** their ordered pairs \((a,H)\) agree. Propositional atoms together with formulas \(\Diamond\ell\), for affine parity expressions \(\ell\), already determine this full theory, including formulas of arbitrary modal nesting depth.
2. Each pointed model is equivalent within this language to a single-class model with precisely \(\dim H+1\) worlds. Every logically equivalent pointed model has at least that many worlds accessible from its distinguished world. In particular, the best uniform bound is \(n+1\), and it is attained.
3. Writing \(G_2(n,d)=\prod_{j=0}^{d-1}\frac{2^n-2^j}{2^d-2^j}\) for the number of \(d\)-dimensional linear subspaces of \(\mathbb F_2^n\), the number of distinct pointed theories is

\[
N_n=2^n\sum_{d=0}^{n}G_2(n,d).
\]

For \(n=1,2,3,4,5\), this yields respectively \(4,20,128,1072,11968\).

## Assumptions and scope

A Kripke model consists of a nonempty set of worlds \(W\), an equivalence relation \(R\) on \(W\), and an assignment of truth values to each of the \(n\) atoms at every world. There is exactly **one** accessibility relation. We use the ordinary Boolean semantics of exclusive-or (true when exactly one argument is true) and ordinary Kripke semantics: \(M,w\models\Diamond\varphi\) if some \(v\) with \(wRv\) satisfies \(\varphi\), while \(M,w\models\Box\varphi\) if all such \(v\) satisfy it. Repeated truth vectors are allowed in the original models, but only their set \(X\) is retained in the signature. The affine hull \(H\) is the least affine subspace containing \(X\), and \(\dim H\) is its affine dimension. Every \(X\) is finite as a set of propositional valuations, even if the underlying equivalence class has infinitely many worlds.

An *affine parity expression* is a propositional formula whose truth function is \(\ell(x)=c\oplus\bigoplus_{i\in I}x_i\), for some \(c\in\mathbb F_2\) and \(I\subseteq\{1,\ldots,n\}\). Such functions are exactly those definable using constants and exclusive-or.

## Proof

**Lemma 1 (affine functions and affine spans).** For any nonempty \(X\subseteq\mathbb F_2^n\), affine function \(\ell:\mathbb F_2^n\to\mathbb F_2\), and \(H=\operatorname{aff}(X)\), the function \(\ell\) vanishes identically on \(X\) if and only if it vanishes identically on \(H\). Indeed, choose \(a\in X\). Every element of \(H\) is an affine combination \(a\oplus\sum_j\lambda_j(x_j\oplus a)\), and affine functions preserve such affine combinations. Therefore existence of a point on which \(\ell=1\), and likewise universal truth of \(\ell\), is the same for \(X\) and \(H\).

**Lemma 2 (affine truth within an epistemic class).** For each formula \(\varphi\) there exist a linear function \(L_\varphi:\mathbb F_2^n\to\mathbb F_2\), depending only on \(\varphi\), and a function \(c_\varphi\) assigning a bit to each nonempty affine subspace \(H\subseteq\mathbb F_2^n\), such that in every \(\mathsf{S5}\) class with affine hull \(H\) and at each world of valuation \(x\),

\[
\mathbf 1_{M,x\models\varphi}=L_\varphi(x)\oplus c_\varphi(H).
\]

Prove this by structural induction. Atoms are the coordinate linear functions and constants have zero linear part. Exclusive-or combines linear parts and class offsets by addition over \(\mathbb F_2\); negation flips only the offset. For \(\Diamond\varphi\), the induction hypothesis says that the operand has the affine truth function \(x\mapsto L_\varphi(x)\oplus c_\varphi(H)\) throughout the class. By Lemma 1, whether this function takes the value one at some valuation in \(X\) depends only on \(H\). The modal result is constant at all worlds of the equivalence class, so its linear part is zero and its new offset depends only on \(H\). The case of \(\Box\varphi\) is identical using universal truth, or by \(\Box\varphi\equiv\neg\Diamond\neg\varphi\). Thus every formula depends at the distinguished world only on \((a,H)\).

**Lemma 3 (separating distinct signatures).** If the distinguished valuations differ, an atom \(p_i\) separates them. Suppose the valuations agree but the affine subspaces \(H,H'\) differ. Without loss of generality, \(H'\not\subseteq H\). Any affine subspace is the common zero set of a finite collection of affine linear equations. Therefore there exists an affine function \(\ell\) that vanishes everywhere on \(H\) but takes value one at some element of \(H'\). By Lemma 1, \(\Diamond\ell\) is false throughout the first class and true throughout the second. The truth functions \(\ell\) have expressions in the permitted propositional vocabulary. This proves both the converse and the depth-one separating assertion.

**Optimal compression.** Let \(a\in X\) be the distinguished valuation, and put \(d=\dim H\). The vectors \(\{x\oplus a:x\in X\}\) span a \(d\)-dimensional linear space; choose \(d\) of these differences forming a basis. Together with the marked vector \(a\), their originating valuations give an affine basis \(B\subseteq X\) with \(d+1\) distinct points and containing \(a\). Construct a \(d+1\)-world model with universal equivalence relation and precisely these valuation vectors, marking the world of valuation \(a\). Its signature is \((a,H)\), hence it is logically equivalent by Lemmas 2 and 3. Conversely, any set of \(s\) distinct valuation vectors has affine dimension at most \(s-1\). A model equivalent to the original must have affine hull \(H\), so its accessible class contains at least \(d+1\) worlds. Taking \(H=\mathbb F_2^n\) proves sharpness of the uniform \(n+1\) bound.

**Counting.** For each dimension \(d\), there are \(G_2(n,d)\) linear \(d\)-dimensional subspaces. Each has exactly \(2^{n-d}\) affine translates and each affine translate has \(2^d\) possible marked valuation vectors \(a\). Consequently the number of pairs \((a,H)\) with \(\dim H=d\) is \(G_2(n,d)2^{n-d}2^d=2^nG_2(n,d)\). Every such pair is realized by an affine-basis model, and Lemma 3 shows distinct pairs yield distinct theories. Summing over \(d\) gives the formula. The displayed small values follow by the finite Gaussian-binomial products. This completes the proof.

## Verification

The standalone `check.py` computes the affine hulls and original Kripke \(\Box,\Diamond\) semantics independently of the induction. It exhaustively processes every nonempty set of truth vectors on \(n=1,2,3\) atoms, compares modal existence for **all affine Boolean functions** before and after hull formation (4,212 checks), evaluates 500 random and structured modal formula templates at all pointed models (182,088 comparisons), and verifies the number of distinct signatures as \(4,20,128\). It also computes the Gaussian-product counts through \(n=5\), yielding \(4,20,128,1072,11968\). The program prints `AFFINE_S5_VERIFY_OK` on success. These bounded experiments are sanity checks; Lemmas 1–3 prove the unrestricted claims.

## Relationship to prior work

Krebs and Meier, *When Symmetry Yields NP-Hardness: Affine ML-SAT on S5 Frames* (arXiv:2512.17378, first public December 19, 2025), investigate satisfiability for affine modal syntax; their principal hardness construction explicitly uses **two** equivalence relations. It does not give a one-agent pointed-theory equivalence criterion or the sharp one-agent quotient cardinalities. Bezhanishvili, ten Cate, Ganguly and Meier, *Modal Fragments* (arXiv:2603.05055, first public March 5, 2026), discuss Boolean-basis restrictions and formulate a question about basis-sensitive bisimulation. The present invariant supplies an exact one-agent affine example but does not answer that question for arbitrary bases or frame classes. Hemaspaandra, Schnoor and Schnoor, *Generalized Modal Satisfiability* (arXiv:0804.2729), address complexity of connective-restricted satisfiability rather than this pointed theory quotient. Classical depth-one modal normal forms for unrestricted Boolean \(\mathsf{S5}\) do not by themselves identify the affine-hull invariant, its exact pointed-type counts, or its sharp minimum-class sizes.

## Limitations

The theorem is **only** for a single equivalence relation and exactly the Boolean clone of affine parity operations. With conjunction added, the three vectors \(\{00,01,10\}\) and the whole \(\mathbb F_2^2\) have the same affine span, but \(\Diamond(p_1\wedge p_2)\) distinguishes the corresponding models. Independent accessibility relations may detect arrangements not captured by one affine hull. The result concerns logical equivalence of pointed models, not the number of syntactically inequivalent formulas or a complete multi-agent complexity classification. Previously unindexed equivalent literature remains a priority risk; the listed comparisons do not establish absolute historical uniqueness. All proofs are mathematical rather than machine-formalized, and no independent audit has been performed.

## References

1. A. Krebs and A. Meier, *When Symmetry Yields NP-Hardness: Affine ML-SAT on S5 Frames*, arXiv:2512.17378, version 1, December 19, 2025. https://arxiv.org/html/2512.17378
2. N. Bezhanishvili, B. ten Cate, S. Ganguly and A. Meier, *Modal Fragments*, arXiv:2603.05055, March 5, 2026. https://arxiv.org/abs/2603.05055
3. E. Hemaspaandra, H. Schnoor and I. Schnoor, *Generalized Modal Satisfiability*, arXiv:0804.2729, April 2008. https://arxiv.org/abs/0804.2729
4. A. Indrzejczak, *Simple Decision Procedure for S5 in Standard Cut-Free Sequent Calculus*, Bulletin of the Section of Logic 45(2), 2016 (classical depth-one normal forms). https://dspace.uni.lodz.pl/xmlui/handle/11089/21628
