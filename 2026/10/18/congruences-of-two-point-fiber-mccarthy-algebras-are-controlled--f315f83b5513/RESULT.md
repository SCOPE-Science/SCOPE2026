# Congruences of two-point-fiber McCarthy algebras are controlled by a single top-class choice

## Finding

Let \(I=(I,\vee,\bot)\) be any nonempty join-semilattice with least element, finite or infinite. Consider the McCarthy algebra \(A(I)=I[\mathbf 2]\) introduced by Bonzio and St. John, with two-element fibers over \(I\). Every congruence of \(A(I)\) is specified uniquely by a semilattice congruence \(\alpha\in\operatorname{Con}(I)\), together with one optional bit that identifies the two points above the **greatest class of \(I/\alpha\)**. That bit is permitted if and only if the quotient semilattice \(I/\alpha\) has a greatest element. No other identifications between distinct Boolean fibers are possible.

More explicitly, let \(\varepsilon\in\{0,1\}\). The pair \((\alpha,\varepsilon)\) is admissible if \(\varepsilon=0\), or if \(\varepsilon=1\) and \(I/\alpha\) has a top element. It defines the congruence
\[
 b_i\mathrel{\Theta_{\alpha,\varepsilon}}c_j
 \quad\Longleftrightarrow\quad
 i\mathrel{\alpha} j\;\text{and}\;
 \bigl(b=c\ \text{or}\ [\varepsilon=1\text{ and }[i]_\alpha=\top_{I/\alpha}]\bigr),
\]
where \(b,c\in\{0,1\}\). These are **all** congruences, without repetition, and their containment order is the componentwise order on the admissible pairs.

In particular, every finite nonempty join-semilattice has a greatest element, and hence
\[
\boxed{\operatorname{Con}(I[\mathbf2])\cong\operatorname{Con}(I)\times\mathbf2.}
\]
For a chain \(I\) with \(n\geq1\) elements, its \(n-1\) adjacency cuts are freely chosen in a semilattice congruence, so \(\operatorname{Con}(I[\mathbf2])\) is a Boolean lattice of rank \(n\), with exactly \(2^n\) elements. An independent exhaustive check gives fourteen congruences for the two-point-fiber algebra over the four-element Boolean join-semilattice.

## Assumptions and scope

No distributivity, finiteness or meet operation is assumed for \(I\), but \(I\) must have a least element. The carrier is the disjoint union of \(\{0_i,1_i\}\) over \(i\in I\). The operations, written with the lower coordinate as a Boolean bit, are
\[
(0_i)'=1_i,\qquad(1_i)'=0_i,\qquad 1=1_\bot,
\]
\[
 0_i\cdot b_j=0_i,\qquad 1_i\cdot b_j=b_{i\vee j}\quad(b\in\{0,1\}).
\]
The constant \(0=0_\bot\) and McCarthy disjunction \(x+y=(x'\cdot y')'\) are term-defined. A congruence respects these operations and constants. A top class of \(I/\alpha\) means a class \(t\) satisfying \(t\vee [j]_\alpha=t\) for every \(j\in I\).

## Proof

**1. The index relation of an arbitrary congruence.** Fix \(\Theta\in\operatorname{Con}(A(I))\), and define \(i\mathrel{\alpha} j\) iff \(0_i\mathrel{\Theta}0_j\). This is an equivalence relation. Since \(0_i+0_j=0_{i\vee j}\) and \(+\) is a term operation, \(\alpha\) respects \(\vee\); hence \(\alpha\in\operatorname{Con}(I)\). Involution gives \(0_i\mathrel{\Theta}0_j\) iff \(1_i\mathrel{\Theta}1_j\). Moreover the unary term \(t(x)=x\cdot0_\bot\) maps both \(0_i\) and \(1_i\) to \(0_i\). Thus a mixed-bit identification \(0_i\mathrel{\Theta}1_j\) implies \(i\mathrel{\alpha} j\). Combining this with the already established same-bit equivalence shows that any mixed identification is equivalent to \(0_i\mathrel{\Theta}1_i\) within a single \(\alpha\)-class.

**2. A collapsed fiber must be greatest in the quotient.** Suppose \(0_i\mathrel{\Theta}1_i\). For every \(j\in I\), multiplication on the right by \(1_j\) yields
\[
 0_i=0_i\cdot1_j\mathrel{\Theta}1_i\cdot1_j=1_{i\vee j}.
\]
Applying the term \(t\) then gives \(0_i\mathrel{\Theta}0_{i\vee j}\); therefore \([i]_\alpha\vee[j]_\alpha=[i]_\alpha\) for every \(j\). Hence \([i]_\alpha\) is the greatest element of \(I/\alpha\). The same-bit equivalences propagate the mixed-bit identification to every index in this greatest class, and no other class can collapse. Consequently \(\Theta\) has the asserted form, with the bit uniquely determined.

**3. Every permitted pair works.** For any \(\alpha\), the natural map \(A(I)\to A(I/\alpha)\), given by \(b_i\mapsto b_{[i]_\alpha}\), is a surjective homomorphism because the product uses only the join of indices. Its kernel is \(\Theta_{\alpha,0}\). If \(I/\alpha\) has greatest class \(T\), additionally merge precisely \(0_T\) and \(1_T\) in \(A(I/\alpha)\). This merger respects involution. It respects products: with a left operand in the merged fiber both products land in that fiber; with a right operand in that fiber, a left zero ignores it and a left one returns an element of that same fiber. It is therefore a congruence, and its inverse image is exactly \(\Theta_{\alpha,1}\). This proves existence and exhaustiveness.

**4. Order and the finite split.** A relation \(\Theta_{\alpha,\varepsilon}\) is contained in \(\Theta_{\beta,\delta}\) precisely when \(\alpha\subseteq\beta\) and \(\varepsilon\le\delta\). The forward implication follows by restricting to zero-bit pairs and, if necessary, witnessing a collapsed mixed-bit pair; the reverse follows because a greatest \(\alpha\)-class maps to the greatest \(\beta\)-class whenever \(\alpha\subseteq\beta\). This identifies the entire congruence lattice with the stated partially doubled order. For finite \(I\), the join of all elements is a top, so every quotient also has a top; all pairs are admitted, giving the direct-product formula. For a chain, join-congruence classes are exactly intervals, and each of the \(n-1\) adjacent boundaries may independently be retained or removed. This gives the Boolean-rank and cardinality corollaries.

## Verification

The standalone Python 3 script `verify_congruences.py` enumerates **every equivalence partition** of the complete two-fiber carrier (not a random sample), checks compatibility with negation and multiplication, and compares the resulting congruence set against the claimed index-class/top-bit construction. It independently enumerates join-congruences of each index semilattice. The script verifies chains with one through four indices, the four-element diamond, and a five-element semilattice with three incomparable atoms. Its output finishes with `MCCARTHY_SEMILATTICE_CONGRUENCE_PRODUCT_OK`. The arbitrary-cardinality theorem is a mathematical proof, not a generalization inferred from those finite tests.

## Relationship to prior work

Bonzio and St. John, *On the structure and theory of McCarthy algebras*, arXiv:2503.10816 (public March 13, 2025), Section 6.1, supply the two-point-fiber construction and show that collapsing a greatest fiber yields a congruence (Propositions 6.3 and 6.5 of the 2026 journal version). The present finding is the **converse completeness theorem**: every congruence is one of these after first taking a quotient of the index semilattice; it also derives the full congruence order and finite product description. Their semilattice decomposition theorem does not by itself state this congruence classification. Vali, Sundarayya and Swamy (2010) study ideal-induced congruences of general conditional algebras, prove relations among them and explicitly note that not all congruences are ideal-induced outside the Boolean case; their results do not state the present complete classification for this specific two-fiber family. The source of the fiber construction, the top-fiber identification, and the general ideal-congruence machinery is credited rather than claimed new.

## Limitations

The product formula is asserted only for finite index semilattices, or more generally when every semilattice quotient has a greatest element; for arbitrary infinite indices the precise partial-doubling description, not a universal direct product, is proved. The theorem concerns the explicit two-point-fiber construction, not all McCarthy algebras or larger Boolean fibers. An older representation of conditional-algebra congruences could possibly imply the classification without using the same terminology; historical priority is not guaranteed. The finite checker does not establish the general theorem independently of the written proof.

## References

1. S. Bonzio and G. St. John, *On the structure and theory of McCarthy algebras*, arXiv:2503.10816 (first public March 13, 2025), especially Sections 5 and 6.1; journal version *Semigroup Forum* 113 (2026), DOI: 10.1007/s00233-026-10641-7.
2. S. Kalesha Vali, P. Sundarayya, and U. M. Swamy, *Ideal Congruences on a C-algebra*, *International Journal of Open Problems in Computer Science and Mathematics* 3(3) (2010), 295–303, especially Theorems 4.6–4.9.
3. F. Guzmán and C. C. Squier, *The Algebra of Conditional Logic*, *Algebra Universalis* 27 (1990), 88–110 (historical background; complete full-text comparison not performed).
