# Canonical palette-word census of modal term operations on finite S4.3 cluster chains

## Finding

Fix a nonempty finite reflexive linear-preorder frame \(W=C_1\sqcup\cdots\sqcup C_h\), in which a world of \(C_i\) accesses exactly \(C_i\cup\cdots\cup C_h\). Put \(a_i=|C_i|\ge1\). Its full Boolean modal algebra is \(\mathcal A=(\mathcal P(W),\cap,\complement,\varnothing,W,\Diamond)\), where \(\Diamond U=\{x:\exists y\in U\ (xRy)\}\).

For every integer \(r\ge0\), let \(q=2^r\), and identify the possible valuations of the \(r\) inputs at one world with the alphabet \(Q=[q]\). Define \(\mathcal L_{\mathbf a}(q)\) to consist of all nonempty finite words \((A_1,\ldots,A_t)\) of nonempty subsets of \(Q\) satisfying:

1. \(1\le t\le h\) and \(A_j\not\subseteq A_{j+1}\) for \(1\le j<t\);
2. there are indices \(1\le i_1<\cdots<i_t=h\) such that \(|A_j|\le a_{i_j}\) for every \(j\).

Then the *exact* number of distinct \(r\)-ary term operations of \(\mathcal A\) is

\[
\boxed{\ |\operatorname{Clo}_r(\mathcal A)|=2^{E_{\mathbf a}(q)},\qquad
E_{\mathbf a}(q)=\sum_{(A_1,\ldots,A_t)\in\mathcal L_{\mathbf a}(q)}|A_1|,\qquad q=2^r.\ }
\]

The formula is finite, requires no enumeration of individual modal terms, and works for arbitrary positive cluster sizes in their specified order. It also gives a canonical normal form for pointed modal types, not merely an operation count.

If every cluster is a singleton (a reflexive linear chain of length \(h\)), the formula simplifies to

\[
E_{(1,\ldots,1)}(q)=\sum_{t=1}^{h}q(q-1)^{t-1},\qquad
|\operatorname{Clo}_r(\mathcal A)|=2^{q\sum_{j=0}^{h-1}(q-1)^j},
\]

with the usual empty-product convention \(0^0=1\). In particular, there are exactly \(4^h\) unary term operations. Cluster order matters: the three-world chains of sizes \((2,1)\) and \((1,2)\) have respectively \(256\) and \(64\) unary term operations.

## Assumptions and scope

All frames and algebras are finite. Accessibility is *reflexive and transitive*, and the cluster quotient is a linear order in the indicated forward direction. The Boolean signature includes constants, complementation, and the usual existential modality. An \(r\)-ary term operation is a function \(\mathcal P(W)^r\to\mathcal P(W)\) obtained from those operations and \(r\) variables; two terms count as the same operation exactly when they agree on every input tuple. The statement is not an enumeration of syntactic formulas, is not about strict linear orders, and does not assert that the displayed formula is polynomial-time computable in a succinct binary encoding.

For a fixed valuation of the input variables, write \(S_i\subseteq Q\) for the nonempty set of truth-value colors occurring in \(C_i\). Multiplicities inside a cluster are ignored by ordinary modal logic. For each suffix \((S_i,\ldots,S_h)\), form a *reduced palette word* from right to left: keep the rightmost palette, and whenever processing an earlier palette \(S\), discard it if \(S\) is contained in the first palette already kept, otherwise prepend it.

The pointed normal form at a world \(x\in C_i\) is the pair of its own color \(c(x)\) and the reduced palette word of its suffix. It will be proved that two pointed colored frames of this type satisfy exactly the same ordinary modal formulas if and only if their pointed normal forms coincide, even when they arise from different valuations or different cluster sizes.

## Proof

**1. Deletion of a dominated cluster.** Suppose adjacent palettes in a colored cluster chain satisfy \(S_i\subseteq S_{i+1}\). Delete \(C_i\) from the frame, mapping each world of \(C_i\) to a world of the same color in \(C_{i+1}\) and fixing all other worlds. This map is surjective, color-preserving and a bounded morphism: the image of the full successor set of a world is exactly the full successor set of its image. At an earlier cluster, the removed cluster contributes nothing not already present at the following cluster; at the removed cluster itself, all images lie in the next cluster, whose entire successor set is attained. Thus modal truth at every world is preserved. Iterating the prescribed right-to-left deletions yields a reduced chain with adjacent palettes satisfying \(A_j\not\subseteq A_{j+1}\). The original world maps to the world of its color in the first surviving palette of the reduced suffix.

**2. Different levels of a reduced chain are modally distinguishable.** Let \((A_1,\ldots,A_t)\) be reduced. Write \(\chi_A\) for the disjunction of the complete propositional color formulas \(\chi_c\) with \(c\in A\). Define \(\eta_{t+1}=\bot\) and, for \(i=t,t-1,\ldots,1\),

\[
\eta_i=\Box(\eta_{i+1}\lor\chi_{A_i}).
\]

By downward induction, \(\eta_i\) holds exactly on the union of clusters \(i,i+1,\ldots,t\). It is true on that suffix because \(\eta_{i+1}\) holds above \(i\) and all worlds at level \(i\) have colors in \(A_i\). For a world at any earlier level, a successor in level \(i-1\) has a color in \(A_{i-1}\setminus A_i\), which exists by reducedness, and does not satisfy \(\eta_{i+1}\). Thus \(\eta_i\) fails there. Consequently \(\eta_i\land\neg\eta_{i+1}\), with the evident final-cluster convention, isolates cluster \(i\); within that cluster the color formulas isolate its distinct color classes. Its bisimulation quotient therefore has exactly one state per color in every reduced cluster.

**3. Uniqueness across colored frames.** Every world in the first cluster of a reduced suffix sees every world of that suffix. Suppose pointed worlds at the roots of two reduced colored suffixes are bisimilar. The relation witnessing bisimilarity covers all states in both suffixes by the back-and-forth conditions. By Step 2, their quotients by bisimilarity have no repetitions of pointed types; any such cross-model bisimulation is therefore the graph of a bijection between the quotients. Back-and-forth makes it a color-preserving isomorphism of reflexive linear-preorder quotients. It must preserve the ordered clusters and each cluster's color set, so the two reduced palette words are equal; atomic harmony gives equality of the distinguished colors. Conversely equal reduced words and equal distinguished colors clearly give bisimilar quotients, and Step 1 lifts bisimilarity back to the original pointed models. Finite-image Hennessy--Milner equivalence makes bisimilarity equivalent to agreement on all ordinary modal formulas. The promised normal form follows.

**4. Which normal forms can occur?** If \((A_1,\ldots,A_t)\) is the reduced word of a pointed suffix, its surviving source levels have indices \(i_1<\cdots<i_t=h\). The last source level is necessarily retained; and each surviving palette satisfies \(|A_j|\le a_{i_j}\). Conversely suppose a word meets the two defining conditions of \(\mathcal L_{\mathbf a}(q)\). Place precisely the colors of \(A_j\) in level \(i_j\) (possible because \(|A_j|\le a_{i_j}\)). At every level strictly between \(i_j\) and \(i_{j+1}\), use a singleton color from \(A_{j+1}\). These intermediate palettes disappear in the right-to-left reduction, while every \(A_j\) survives because \(A_j\not\subseteq A_{j+1}\). The color distribution at levels preceding \(i_1\) can be arbitrary, and a chosen world at \(i_1\) can have any specified color of \(A_1\). Hence exactly the normal forms \((c,(A_1,\ldots,A_t))\) with \((A_1,\ldots,A_t)\in\mathcal L_{\mathbf a}(q)\) and \(c\in A_1\) occur. Their number is \(E_{\mathbf a}(q)\).

**5. Counting operations.** Form the finite disjoint union of all pointed valuations of the \(r\) variables on the fixed frame. By Steps 1--4, its modal-equivalence classes are precisely the \(E_{\mathbf a}(q)\) normal forms. On any finite collection of finite pointed Kripke models, each modal-equivalence class is definable by a modal formula: for each inequivalent competitor choose a distinguishing formula, and conjoin the finitely many choices. Therefore every subset of the \(E_{\mathbf a}(q)\) classes is definable by a modal formula, and two such subsets induce different term operations. There are exactly \(2^{E_{\mathbf a}(q)}\) operations.

For singleton clusters, the reduced palettes are single colors with consecutive colors unequal. At length \(t\) there are \(q(q-1)^{t-1}\) reduced words, and every length at most \(h\) occurs, proving the closed form. For cluster sizes \((2,1)\) with \(q=2\), there are two types of one-palette word and six types of two-palette word, giving exponent \(8\); for \((1,2)\), there are four one-palette types and two two-palette types, giving exponent \(6\).

## Verification

The self-contained file `verify.py` constructs the reduced normal forms independently of a capacity-subsequence enumeration; it also builds a disjoint union of every valuation for selected small frames and computes its true bisimulation partition by iterative color-and-successor refinement. Separately, it constructs entire truth tables of term operations and closes them under Boolean operations and the modal operator, without using the normal-form formula.

Reproduction: `python3 verify.py` from the directory containing this result and the script. The successful execution printed:

```text
VERIFY_OK language_cases 42 cross_model_bisimulations 27 bisimulation_worlds 4176 direct_term_closures 8 orientation_example (256, 64)
```

The finite tests include nonuniform cluster sizes, one and several propositional colors, and direct computation of all term operations for eight small cases. They are corroborating tests, not an infinite-size proof. The unrestricted theorem follows from the five mathematical steps above.

## Relationship to prior work

The 2022 paper by ten Cate and Koudijs on finite characterisations of modal formulas connects finite-frame expressive power to local tabularity and exact learnability. Their arguments concern classes of frames and finite distinguishing examples, not a precise term-operation cardinality for each fixed finite ordered-cluster frame. The earlier preprint was publicly available on 2022-06-13.

Kurucz, Wolter and Zakharyaschev's 2023 preprint studies interpolant existence and bisimilar models for linear transitive frames, explicitly using cluster chains and generated Boolean modal algebras. Its inspected sections on finite generated descriptive frames, clusters, and bisimulation do not furnish the capacity-indexed reduced-palette census above. That study addresses interpolation, not the number of all operations on a fixed finite powerset modal algebra.

Classical bounded-morphism invariance, finite-model Hennessy--Milner equivalence and finite modal filtration underpin the proof and are not claimed as new. The separate question of whether a *fixed tuple of generators* generates the full modal algebra does not directly give the number of *all possible term functions across every tuple of inputs*. The present theorem is an explicit full-clone count for arbitrary ordered cluster-capacity vectors.

## Limitations

The enumeration is finite but may be exponentially costly in \(q=2^r\); no optimal computational complexity is claimed. It concerns ordinary, ungraded, unimodal Boolean operations on finite reflexive linear-preorder frames; adding converse, counting modalities, or removing reflexivity changes the behavior. The proof does not establish syntactic formula-length minima or independence from previously unpublished work. A historically equivalent normal form or full-clone count in older modal-algebra literature remains a residual originality risk. The scientific assessment supplied with this result is a self-review only, not independent validation.

## References

1. Balder ten Cate and Raoul Koudijs, *Characterising Modal Formulas with Examples*, preprint first released 2022-06-13, arXiv:2206.06049; later versions include arXiv:2304.06646.
2. Agi Kurucz, Frank Wolter and Michael Zakharyaschev, *A Non-Uniform View of Craig Interpolation in Modal Logics with Linear Frames*, arXiv:2312.05929, first posted 2023-12-10. Relevant material: Sections 2--4, in particular modal algebras, cluster orders, finite generation and bisimulation.
3. A. Chagrov and M. Zakharyaschev, *Modal Logic*, Oxford Logic Guides 35, 1997; standard background on bounded morphisms and modal bisimulation.
