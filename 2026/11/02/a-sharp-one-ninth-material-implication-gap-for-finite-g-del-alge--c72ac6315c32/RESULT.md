# A sharp one-ninth material-implication gap for finite Gödel algebras

## Finding

Let \(H\) be a finite nontrivial **Gödel algebra**, meaning a finite Heyting algebra satisfying prelinearity \((a\to b)\vee(b\to a)=\top\). Let \(h=|H|\), and count ordered pairs by
\[
\Delta(H)=|\{(a,b)\in H^2:a\to b\ne\neg a\vee b\}|.
\]
Then either \(H\) is Boolean and \(\Delta(H)=0\), or
\[
\boxed{\Delta(H)\ge h^2/9.}
\]
The constant is sharp: among non-Boolean finite Gödel algebras, equality holds **if and only if** \(H\cong C_3\times C_2^k\) for some integer \(k\ge0\), with \(C_j\) the \(j\)-element Heyting chain. Thus the maximum possible satisfaction degree of material implication in a non-Boolean finite Gödel algebra is exactly \(8/9\).

A stronger connected-frame statement underlies the result. Let \(P\) be a nonempty finite rooted tree ordered with its root least and each principal downset a chain, and let \(H=J(P)\) be its downset Heyting algebra of size \(h\). Then
\[
\boxed{\Delta(H)\ge\frac{(h-1)(h-2)}2,}
\]
with equality exactly when \(P\) is a chain. The right-hand side is optimal at every \(h\ge2\), since the \((h-1)\)-element chain yields an \(h\)-element downset algebra.

## Assumptions and scope

All algebras are finite, with uniformly sampled ordered pairs. The one-element algebra may be included vacuously in auxiliary recurrences; the sharp gap concerns nontrivial algebras. For a finite poset \(P\), \(J(P)\) includes the empty and whole downsets and carries implication
\[
A\to B=\{p\in P:(\downarrow p)\cap A\subseteq B\}.
\]
Under finite distributive-lattice duality, Gödel algebras are precisely those \(J(P)\) for which every principal downset of \(P\) is a chain; such a \(P\) is a disjoint union of rooted trees. This standard characterization is used as background, not claimed as new.

Write \(n(H)=|H|\) and introduce the **implication-fixpoint count**
\[
\sigma(H)=|\{(a,b)\in H^2:a\to b=b\}|.
\]
The proof uses exact recurrences for \(\sigma\), followed by a sharp extremal inequality. The value \(\Delta(H)\) counts *failures*, not the number of satisfying pairs; the latter is \(n(H)^2-\Delta(H)\).

## Proof

**1. Products.** Operations in \(H_1\times H_2\) are coordinatewise. Thus
\[
\sigma(H_1\times H_2)=\sigma(H_1)\sigma(H_2),
\quad n(H_1\times H_2)=n(H_1)n(H_2),
\]
and the number of satisfying pairs for the material-implication equation is multiplicative. In particular, its satisfaction *probability* is multiplicative.

**2. Adding a unique least point.** Let \(Q\) be a finite forest and \(P\) the poset obtained by adding a new least point \(r\) below all of \(Q\). Put \(B=J(Q)\), \(m=n(B)\), and \(H=J(P)\). Every nonempty downset of \(P\) is \(\{r\}\cup U\), with \(U\in B\); consequently \(n(H)=m+1\). This identifies \(H\) with \(B\) together with a new bottom element below its old bottom.

For \(x,y\in B\), the implication of their corresponding **nonzero** elements in \(H\) corresponds to \(x\to_B y\). Moreover, every nonzero element \(a\) of \(H\) has \(\neg a=0_H\), since it contains \(r\). To count \(\sigma(H)\), pairs of nonzero elements contribute \(\sigma(B)\); pairs with a nonzero antecedent and zero consequent contribute exactly \(m\); and the zero antecedent contributes exactly one further pair, with top consequent. Therefore
\[
\boxed{\sigma(H)=m+1+\sigma(B).}
\]
For material implication, every pair involving the new zero satisfies the equation. Among the \(m^2\) pairs of nonzero elements, exactly \(\sigma(B)\) satisfy it, so
\[
\boxed{\Delta(H)=m^2-\sigma(B).}
\]
These identities also cover the empty forest \(Q\), for which \(B\) is the one-element Heyting algebra.

**3. Sharp implication-fixpoint inequality.** For every finite forest \(Q\), with \(B=J(Q)\) of size \(m\),
\[
\boxed{\sigma(B)\le\frac{m(m+1)}2,}
\]
with equality if and only if \(Q\) is a chain (including the empty chain). Prove this by induction on \(|Q|\). The empty case has \(m=1\) and \(\sigma=1\). If \(Q\) is connected, remove its least point, leaving a smaller forest with algebra size \(t=m-1\). By step 2 and the induction hypothesis,
\[
\sigma(B)\le m+\frac{(m-1)m}{2}=\frac{m(m+1)}2.
\]
Equality requires, and follows from, the remaining forest being a chain; hence the original rooted tree is a chain.

If \(Q\) is disconnected, split it into two nonempty forests with algebra sizes \(u,v\ge2\). Their product algebra has size \(m=uv\), and step 1 and induction give
\[
\sigma(B)\le\frac{u(u+1)v(v+1)}4<\frac{uv(uv+1)}2.
\]
The strict inequality is exactly \((u-1)(v-1)>0\). This completes the induction and its equality classification.

**4. Connected extremality.** In step 2, take \(P\) to be a nonempty rooted tree, with \(Q=P\setminus\{r\}\) a forest. Then \(h=m+1\), and the two boxed formulas yield
\[
\Delta(J(P))=m^2-\sigma(J(Q))
\ge m^2-\frac{m(m+1)}2
=\frac{(h-1)(h-2)}2.
\]
Equality is equivalent to \(Q\) being a chain, equivalently \(P\) being a chain. When \(|P|\ge2\), the connected algebra is non-Boolean and \(h\ge3\).

**5. The one-ninth gap and all equality cases.** Every finite Gödel algebra decomposes as the direct product of the downset algebras of the rooted-tree components of its dual forest. Single-point components yield the Boolean algebra \(C_2\). Every component containing at least two points has at least three downsets and, by step 4, a material-implication failure proportion at least
\[
\frac{(h_i-1)(h_i-2)}{2h_i^2}\ge\frac19
\qquad(h_i\ge3).
\]
The displayed function is strictly increasing for integer \(h_i\ge3\); equality can therefore occur only for \(h_i=3\), namely a two-point chain with algebra \(C_3\). Since satisfaction probabilities multiply across factors, at least one such non-Boolean factor forces the global satisfaction probability to be at most \(8/9\). Equality requires exactly one factor \(C_3\) and all remaining factors Boolean, and each such product attains \(8/9\). A finite Gödel algebra with no non-Boolean factors is Boolean and has no failures. This proves the theorem.

## Verification

The accompanying `verify.py` performs direct enumeration of the downsets, pseudocomplements and implications, entirely independently of the structural formulas used for prediction. For every parent-before-child rooted-forest presentation through seven points, it compares the direct implication-fixpoint count with the exact forest recurrence, checks the sharp auxiliary inequality and its equality cases, checks the rooted-tree failure bound, and checks the global one-ninth gap and equality classification. There are exactly 5,913 such increasing-forest presentations through seven points; every rooted-forest isomorphism type within this cutoff has such a presentation. The checker also tests rooted stars and chains at additional sizes. Run with `python3 verify.py` using Python's standard library. A finite computation checks only the stated finite range; the all-size results follow from the proof above.

## Relationship to prior work

Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first posted 2021-10-21), establish that material implication has **no** finite satisfiability gap over the class of all finite Heyting algebras (their Theorem 3.15). In their Section 6.6 they explicitly identify restricted Gödel algebras as a potentially useful setting for further satisfiability classifications. Their theorem for arbitrary Heyting algebras does not imply a positive bound for this proper subclass. The present result supplies the sharp bound, extremal family, and strengthened connected-frame inequality in that restricted setting.

Flaminio, Godo, Menchón and Rodríguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528 (first posted 2021-10-06), use the standard finite Gödel algebra/finite forest duality. The representation theorem is background; it does not by itself count solutions of the material-implication equation. A prior result formulated with different notation for implication or tree-of-ideals counts could still overlap; the exact statements here should be compared in any independent historical-priority review.

## Limitations

The positive one-ninth gap is restricted to **finite prelinear Heyting algebras**; it does not hold over all finite Heyting algebras. The stronger quadratic lower bound concerns connected rooted-tree duals, not arbitrary products. The work does not assert infinite-algebra measure analogues, alternate nonuniform sampling, or a complete classification of all possible satisfaction degrees. The computational enumeration does not constitute a proof for unbounded carrier size. Historical originality is assessed against accessible sources, not independently certified.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first public version 2021-10-21; Journal of Symbolic Logic (2025). https://arxiv.org/abs/2110.11515
2. T. Flaminio, L. Godo, P. Menchón and R. O. Rodríguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528, first public version 2021-10-06. https://arxiv.org/abs/2110.02528
