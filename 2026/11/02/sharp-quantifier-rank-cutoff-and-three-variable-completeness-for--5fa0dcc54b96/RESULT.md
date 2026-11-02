# Sharp quantifier-rank cutoff and three-variable completeness for finite cyclic orders

## Finding

Let \(\mathcal C_n\), for every integer \(n\ge3\), be the finite structure with universe \(\mathbb Z/n\mathbb Z\) and a single ternary relation \(C\), where \(C(a,b,c)\) holds precisely when \(a,b,c\) are distinct and, traveling forward cyclically from \(a\), one encounters \(b\) before \(c\). Equality is logical; there are no named points, successor, other relations, or counting quantifiers. Write \(\equiv_q\) for agreement on all first-order sentences of quantifier rank at most \(q\), and \(\equiv_q^{\mathrm{FO}^3}\) for agreement on such sentences using at most three variable names.

**Theorem.** For every integer \(q\ge3\) and every pair of integers \(3\le m<n\),
\[
\mathcal C_m\equiv_q^{\mathrm{FO}^3}\mathcal C_n
\quad\Longleftrightarrow\quad
\mathcal C_m\equiv_q\mathcal C_n
\quad\Longleftrightarrow\quad
m\ge 2^{q-1}.
\]
Isomorphic structures are equivalent, so this is a complete equivalence classification for arbitrary \(m,n\ge3\). For \(q\le2\), all structures in the family are rank-\(q\) equivalent. Consequently, at rank \(q\ge3\) there are exactly \(2^{q-1}-2\) equivalence classes: each order \(3,4,\ldots,2^{q-1}-1\) is a singleton class and all orders \(n\ge2^{q-1}\) form one final class. The sharp maximum size of a smallest class representative is \(2^{q-1}\). For \(3\le m<n\), their least distinguishing quantifier rank is \(\lfloor\log_2 m\rfloor+2\). In contrast, ordinary two-variable logic at unrestricted quantifier depth has just one theory on this entire family.

In particular, **the three-variable fragment and unrestricted first-order logic induce exactly the same equivalences on these structures, at every fixed quantifier rank**, despite the proper loss of all order information at width two.

## Assumptions and scope

The models are nonempty finite *total oriented cyclic orders*, with at least three elements, represented in the pure **strict ternary cyclic-order signature**. A triple \(C(a,b,c)\) is false whenever any two entries coincide. The logical width is the number of distinct variable symbols allowed in a formula, permitting reuse and shadowing. Quantifier rank is maximum quantifier nesting, not the total number of quantifiers. The theorem concerns sentences and exact rank preservation, not an equivalence of arbitrary formulas with several free variables. All inequalities and equivalences in the theorem quantify over every indicated finite order and every integer rank.

## Proof

**Step 1: exact interior-size tests using three variables.** For two distinct points \(x,y\), denote by \(I(x,y)\) the set of points encountered strictly after \(x\) and before \(y\) around the positive orientation. For integers \(r\ge0\) and \(0\le s\le 2^r-1\), define a formula \(F_{r,s}(x,y)\) recursively. Let \(F_{r,0}(x,y)\) be true. For \(r\ge1\), \(s\ge1\), set
\[
a=\lfloor(s-1)/2\rfloor,\qquad b=s-1-a,
\]
so \(a,b\le2^{r-1}-1\), and let
\[
F_{r,s}(x,y)\ :=\ \exists z\,[C(x,z,y)\wedge F_{r-1,a}(x,z)\wedge F_{r-1,b}(z,y)].
\]
Each occurrence of \(F\) is obtained by consistently renaming its two free endpoint variables and using the remaining third variable for its local quantifier. Thus the formula uses only the three variable names \(x,y,z\) (with branch-local shadowing) and has quantifier rank at most \(r\).

Induction on \(r\) shows that, whenever \(x\ne y\),
\[
\mathcal C_n\models F_{r,s}(x,y)\quad\Longleftrightarrow\quad |I(x,y)|\ge s.
\]
Indeed, an interior witness \(z\) partitions its containing open arc into two arcs of sizes whose sum is \(|I(x,y)|-1\). A witness satisfying the two recursive requirements exists exactly when at least \(a+b+1=s\) interior points exist. This proves both directions, including \(s=0\).

**Step 2: every smaller order is distinguished at the claimed rank.** Fix \(q\ge3\), put \(r=q-2\), \(K=2^r-1\), and \(T=2+2K=2^{q-1}\). Suppose \(3\le m<n\) and \(m<T\). Choose nonnegative integers \(a,b\le K\) with
\[
a+b+2=\min(n,T).
\]
Such a choice exists since \(\min(n,T)-2\le2K\). The rank-\(q\), three-variable sentence
\[
\exists x\exists y\,[x\ne y\wedge F_{r,a}(x,y)\wedge F_{r,b}(y,x)]
\]
is true in \(\mathcal C_n\): a pair of vertices can be placed with at least \(a\) points in one oriented arc and at least \(b\) in the other. It is false in \(\mathcal C_m\), because the two open arcs of any distinct pair partition the remaining \(m-2<a+b\) points. The formula is valid for every small order and every larger comparator; it establishes the exact lower bound on the rank and on representative sizes.

**Step 3: the interval splitting lemma.** Put \(K_r=2^r-1\). Say two nonnegative integers are \(r\)-equivalent when they are equal below \(K_r\), or both are at least \(K_r\). For \(r\ge1\), if \(a,b\) are \(r\)-equivalent, any partition \(a=a_1+1+a_2\), corresponding to selecting one interior point, can be matched by a partition \(b=b_1+1+b_2\) such that \(a_1,b_1\) and \(a_2,b_2\) are each \((r-1)\)-equivalent. When \(a<K_r\), copy both parts exactly. Otherwise write \(K_r=2K_{r-1}+1\). If one part is below \(K_{r-1}\), copy that part exactly, leaving at least \(K_{r-1}\) on the other side; if neither is below the threshold, choose \(b_1=K_{r-1}\), leaving \(b_2\ge K_{r-1}\). The lemma is symmetric in \(a,b\). Unsplit gaps preserve equivalence at the lower threshold as well.

**Step 4: all large orders agree even in unrestricted first-order logic.** Let \(m,n\ge T=2^{q-1}\). Consider the ordinary \(q\)-round Ehrenfeucht–Fraïssé game with arbitrarily many distinct pebble pairs. Duplicator matches the first chosen point by any point, using cyclic rotation. Whenever the second *distinct* point is first chosen, say on move \(j\ge2\), the two points cut each circle into two directed open arcs. Duplicator matches the two arc sizes up to threshold \(K_{q-j}\): copy a smaller-than-threshold arc exactly, or, when both arcs are large, make both responding arcs at least the threshold. Such a split exists because each circle has at least \(T=2+2K_{q-2}\ge2+2K_{q-j}\) elements. Selections repeating an earlier point are always copied.

After \(t\ge2\) **moves**, provided at least two distinct points have been selected, Duplicator maintains an orientation-preserving correspondence of all selected points and, for every open arc between consecutive selected points, equality of its size below \(K_{q-t}\) or largeness on both sides. On a new distinct selection, the chosen gap is split; the lemma supplies a corresponding selection, and the threshold decreases by one level. A repeated selection leaves the gaps unchanged and automatically preserves their equivalence at the smaller threshold. If only one distinct point has been selected, the rotation matching suffices until a second distinct point appears. At the end \(K_0=0\), and preservation of the cyclic order of all selected triples is exactly the required partial isomorphism. Thus Duplicator wins the unrestricted \(q\)-round game, proving \(\mathcal C_m\equiv_q\mathcal C_n\), and hence \(\mathcal C_m\equiv_q^{\mathrm{FO}^3}\mathcal C_n\).

**Step 5: endpoints and width.** A rank-\(q\) sentence for \(q\le2\) cannot simultaneously assign three distinct variables within a true atom of the only nonlogical relation; equality conditions alone cannot distinguish sizes at least three. Similarly, unrestricted-depth two-variable sentences see the ternary relation only on triples with repeated entries, where it is invariably false. Their remaining equality-only two-variable theories agree for all cardinalities at least two. Finally, for \(3\le m<n\), the first rank at which \(m<2^{q-1}\) is exactly \(\lfloor\log_2 m\rfloor+2\). All conclusions follow.

## Verification

Two independently structured standard-library Python checkers accompany this statement. The first computes all three-pebble assignment types up to rotation, then applies the exact quantifier-rank refinement (sets of obtainable lower-rank types for each variable replacement). For orders \(3\) through \(40\) and ranks \(0\) through \(6\), it recovers the predicted class counts \(1,1,1,2,6,14,30\), with cutoffs \(4,8,16,32\) at ranks \(3,4,5,6\). This directly checks the logical game rather than imposing interval formulas.

The second checker independently tests the recursive interval-formula semantics for \(10{,}795\) parameter configurations, the truncation/splitting stabilization for \(312\) configurations, and the finite arithmetic feasibility of the explicit distinguishing formulas at ranks \(3\) through \(8\). Its checks use bounded examples; the theorem for arbitrary size and rank is established by the preceding inductive proof, not by these finite tests. Run `python3 verify_rank_types.py` and `python3 verify_intervals.py` with Python 3 standard library.

## Relationship to prior work

Spencer and St. John analyze first-order Ehrenfeucht–Fraïssé games for random **circular bit sequences**, explicitly in a ternary circular-order language, and prove logarithmic-order tenacity bounds in the very sparse regime. Their inspected section on all-zero inputs develops a split-interval method and treats precise linear-order sizes; it does not state this exact rank-by-rank partition of all finite uncoloured ternary cyclic orders or the rank-preserving three-variable equivalence. The present invariant and interval formulas sharpen the uncoloured circular specialization to an attained finite cutoff.

Classical work on linear-order rank equivalence (including Siders's local rank-normal-form theory) and the Immerman–Kozen three-variable property for linear orders provides essential related techniques but concerns a binary linear-order signature. Neither inspected statement directly gives the exact ternary circular cutoff without the two-arc analysis, and a generic variable-property theorem does not by itself establish preservation of quantifier rank. The elementary circular-order structures also appear in the broader combinatorial study of cyclic orders by Alles, Nešetřil, and Poljak, whose identified abstract concerns order extension and dimension rather than first-order rank spectra.

## Limitations

The theorem is specific to uncoloured total **oriented** cyclic orders of size at least three, the strict ternary language, and noncounting first-order logic. It does not address unary vertex colors, successor or adjacency, arbitrary partial cyclic orders, structures with a named point, counting quantifiers, or arbitrary formulas with free variables. The precise first-public-date evidence belongs to the cited background literature and does not represent a publication or external certification of this theorem. The originality comparison is literature-based and not an exhaustive historical-priority proof: a more general published treatment of rank types of circular orders could subsume the result. Independent mathematical audit has not been performed.

## References

- J. H. Spencer and K. St. John, *The Tenacity of Zero-One Laws*, Electronic Journal of Combinatorics 8(2), R17 (2001), first online record 2000-08-06, doi:10.37236/1616. Open full text: https://stjohn.github.io/research/ejc01.pdf.
- N. Immerman, *Descriptive Complexity*, Chapter 6, section 6.4, Theorem 6.31, three-variable property for linear orders and its attribution to Immerman–Kozen. https://people.cs.umass.edu/~immerman/book/ch6.pdf.
- R. Siders, *On quantifier-rank equivalence between linear orders*, Information and Computation 208 (2010), 417–432, doi:10.1016/j.ic.2009.11.006. Abstract and bibliographic metadata inspected.
- P. Alles, J. Nešetřil, and S. Poljak, *Extendability, Dimensions, and Diagrams of Cyclic Orders*, SIAM Journal on Discrete Mathematics (1991), doi:10.1137/0404041. Abstract inspected.
