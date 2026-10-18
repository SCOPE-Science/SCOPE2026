# Inverse fibers of negative tense modalities on finite Gödel chains

## Finding
Fix an integer \(n\geq1\), and let \(G_{n+1}\) be the \((n+1)\)-element Gödel (Heyting) chain. A *negative tense expansion* is a quadruple of unary operations \((g,h,f,p)\) on \(G_{n+1}\) satisfying axioms (T1)--(T8) of Almiñana--Pelaitay--Zuluaga [1]. Distinct quadruples on the fixed chain are counted separately; since the underlying finite chain is rigid, this also counts their isomorphism classes.

Let \(X=\{0,1,\ldots,n-1\}\) with its usual order and let \(U_t=\{t,\ldots,n-1\}\) for \(0\leq t\leq n\). Every negative tense expansion is represented uniquely by one of the following relations \(R\subseteq X\times X\):

* the empty relation; or
* a relation with rows \(R(i)=[a_i,b_i]\cap X\), whose integer endpoints satisfy
\[
 n-1\geq a_0\geq a_1\geq\cdots\geq a_{n-1}=0,
 \qquad n-1=b_0\geq b_1\geq\cdots\geq b_{n-1}\geq0,
\]
\[
 a_i\leq b_i\quad(0\leq i<n),\qquad
 b_{i+1}\geq a_i-1\quad(0\leq i<n-1).
\]
These inequalities are both necessary and sufficient.

The *single-operator reduct* is \(g\). There are exactly
\[
 \boxed{1+\binom{2n-2}{n-1}}
\]
distinct \(g\)-reducts that extend to a negative tense expansion. The constant-zero reduct has exactly one completion. Every other reduct has a unique nonincreasing endpoint sequence \(a=(a_0,\ldots,a_{n-1})\) as above, and its exact number of full negative tense completions is
\[
\boxed{\displaystyle
 F_n(a)=\#\left\{(b_1,\ldots,b_{n-1})\in X^{n-1}:\ n-1=b_0\geq b_1\geq\cdots\geq b_{n-1},\ b_i\geq a_i,\ b_{i+1}\geq a_i-1\right\}.}
\]
Here \(b_i\geq a_i\) ranges over \(0\leq i<n\), with \(b_0=n-1\), and the adjacent inequality ranges over \(0\leq i<n-1\); when \(n=1\), the unique empty tuple contributes one completion. More finely, the distribution by number of incidences in the dual relation is the explicitly finite polynomial
\[
 F_n(a;z)=\sum_{b\ \mathrm{admissible\ for}\ a}z^{\sum_{i=0}^{n-1}(b_i-a_i+1)}.
\]
For every \(n\geq2\), the nonzero reduct fibers obey the sharp bounds
\[
 \boxed{2\leq F_n(a)\leq\binom{2n-2}{n-1}.}
\]
Both bounds are attained: the upper bound at \(a=(0,\ldots,0)\), and the lower at \(a=(n-1,\ldots,n-1,0)\). Thus, except for the zero reduct, forgetting three tense operators is never faithful once the chain has at least three elements. The complete numbers of expansions for \(n=1,2,3,4,5\) are respectively \(2,5,30,267,2763\).

## Assumptions and scope
The chain \(G_{n+1}\) is fixed, finite, and nonempty, with \(n\geq1\). The operations satisfy *all eight* equations/inequalities (T1)--(T8) in Definition 2.1 of [1], not merely the antitone Galois-adjunction laws. The poset \(X\) is the finite Esakia dual of this chain; its upsets \(U_t\) give precisely the chain elements. Here \(g\) means the negative existential modality in [1, Example 2.2], not a classical Kripke necessity operator. The fibers count fully distinct compatible quadruples, not arbitrary unary antitone maps outside the displayed extendable family.

## Proof
**1. Dual correspondence.** Theorem 4.4, Lemma 4.4 and Proposition 4.3 of [1] identify negative tense expansions of a fixed finite Heyting algebra with admissible relations on its finite Esakia dual. In Definition 4.1 of [1], admissibility requires (S1) closed rows and inverse rows, (S2) order-convex rows, and (S3) the four induced operations on clopen upsets to return clopen upsets. On a finite chain every subset is closed, so (S1) is automatic. An order-convex row is either empty or an interval. The operations are, for each upset \(U\),
\[
 g_R(U)=\{i:R(i)\cap(X\setminus U)\ne\varnothing\},\quad
 f_R(U)=\{i:R(i)\subseteq X\setminus U\},
\]
with \(h_R,p_R\) defined by the inverse relation in the same way.

**2. No mixed empty fibers.** Taking \(U=X\), the upset \(f_R(X)\) is precisely the set of empty rows; taking \(U=\varnothing\), the upset \(g_R(\varnothing)\) is the complementary set of nonempty rows. Complementary subsets of a finite total order that are both upsets must be \(\varnothing\) and \(X\). Thus all rows are empty or all are nonempty. Applying the same argument to \(h_R,p_R\) shows all columns are empty or all are nonempty. Hence any nonempty admissible relation has every row and every column nonempty.

**3. Necessity of the endpoint conditions.** For nonempty rows \(R(i)=[a_i,b_i]\), the equations
\[
 i\in g_R(U_t)\iff a_i<t,\qquad i\in f_R(U_t)\iff b_i<t
\]
hold for every \(0\leq t\leq n\). Since both outputs must be upsets, \(a_i\) and \(b_i\) are nonincreasing in \(i\). Full column coverage forces \(a_{n-1}=0\) and \(b_0=n-1\). Moreover, if \(b_{i+1}<a_i-1\) for some adjacent rows, an integer \(j\) strictly between those endpoints is covered by no row: earlier rows start at or to the right of \(a_i\), whereas later rows end at or to the left of \(b_{i+1}\). Therefore \(b_{i+1}\geq a_i-1\).

**4. Sufficiency.** Conversely, suppose the displayed endpoint inequalities hold. Every row is a nonempty interval. The rows sweep from the rightmost column in the first row to the leftmost column in the last row, with no gaps between successive intervals, so every column is nonempty. For a fixed column \(j\), its row-index set is the intersection of the suffix \(\{i:a_i\leq j\}\) and the prefix \(\{i:b_i\geq j\}\), hence an interval. For \(j<k\), its minimal and maximal row indices are at least those for column \(k\): any first occurrence of \(j\) is no earlier than that of \(k\), and any last occurrence of \(j\) is no earlier than that of \(k\), using nonincreasing row endpoints and column nonemptiness. Thus the two endpoints of the column intervals are nonincreasing in \(j\), which makes \(h_R(U_t)\) and \(p_R(U_t)\) upsets for all \(t\). The row endpoint monotonicity similarly makes \(g_R(U_t)\) and \(f_R(U_t)\) upsets. Hence (S1)--(S3) hold. Faithfulness of [1]'s duality makes the resulting quadruple unique for each relation.

**5. Classification of single-operator fibers.** The values \(g_R(U_t)\) determine every row-minimum \(a_i\), by the equivalence in Step 3; and the zero operator comes only from the empty relation because a nonempty relation has \(g_R(\varnothing)=X\). Conversely, every nonincreasing \(a\) with \(a_{n-1}=0\) extends by taking every \(b_i=n-1\). Such \(a\)'s are multisets of size \(n-1\) drawn from \(n\) possible endpoint values, so their number is \(\binom{2n-2}{n-1}\). For fixed \(a\), the precise completion count is the number of \(b\)'s in the displayed conditions, yielding \(F_n(a)\) and its incidence-refined polynomial.

**6. Sharp reconstruction bounds.** Every admissible \(b\) is a weakly decreasing sequence with \(b_0=n-1\) and \(n-1\) further entries in \(X\), of which there are \(\binom{2n-2}{n-1}\). For \(a=(0,\ldots,0)\) all of them are admissible, proving the sharp maximum. For any \(a\) and \(n\geq2\), both \(b_i=n-1\) for every \(i\), and the sequence obtained by changing only the final entry to \(n-2\), are admissible. This gives the lower bound two. If \(a=(n-1,\ldots,n-1,0)\), all earlier \(b_i\) are forced to \(n-1\), and the final \(b_{n-1}\) is \(n-2\) or \(n-1\); hence the lower bound is attained. For \(n=1\), each of the two reducts has exactly one completion.

## Verification
The standalone `verify.py` checks the classification by three distinct finite mechanisms: (i) enumerating the endpoint parameters, their \(g\)-fibers and relation sizes through \(n=5\); (ii) enumerating all possible interval relations and checking the four upset-preservation predicates directly through \(n=4\); (iii) independently enumerating all antitone unary operations satisfying the original (T1)--(T8) algebraic axioms on chains with two through four elements. All tests agree, with `VERIFY_OK`. The Python program uses only the standard library and can be run with `python3 verify.py`. These finite computations are not the proof for general \(n\); the preceding argument is uniform.

## Relationship to prior work
Almiñana, Pelaitay, and Zuluaga [1] introduce the axioms and prove the general Priestley/Esakia-style dual equivalence, including the four relationally induced operations. That result supplies the representation theorem used here, but does not give this chain-specific endpoint classification, the exact one-operator inverse fibers, or their sharp bounds. Ma and Li [2] introduce intuitionistic propositional logic with Galois negations and its relational semantics; no chain-specific fiber classification is asserted here as a result of [2]. Existing classical enumeration of interval-convex polyominoes could encompass some unrefined parameter counts after a reduction; no novelty is claimed for general combinatorial enumeration methods themselves. The new claim is the precise logical reconstruction question, its complete parameter classification, and the exact inverse-fiber bounds.

## Limitations
The formulas concern finite chains, not arbitrary Heyting algebras or infinite Gödel structures. The counting is for fixed labelled chain operations (equivalently isomorphism types because automorphisms of a finite chain are trivial). The relation-incidence generating polynomials enumerate a dual representation, not additional independent operators. The priority comparison remains subject to equivalent older work on Galois pairs, convex matrices or polyominoes under other terminology. Independent mathematical and priority review has not been performed.

## References
[1] F. G. Almiñana, G. Pelaitay, and W. Zuluaga, *On Heyting algebras with negative tense operators*, arXiv:2212.14756v1, first posted 23 December 2022; *Studia Logica* 111 (2023), 1015–1036, doi:10.1007/s11225-023-10053-6. Definition 2.1, Example 2.2, Definition 4.1, Lemma 4.4, Proposition 4.3, Theorem 4.4.

[2] M. Ma and G. Li, *Intuitionistic propositional logic with Galois negations*, *Studia Logica* 111 (2023), 21–56, doi:10.1007/s11225-022-10014-5; first publisher-public date 26 September 2022.
