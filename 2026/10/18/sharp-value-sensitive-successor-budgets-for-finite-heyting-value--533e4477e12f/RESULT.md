# Sharp value-sensitive successor budgets for finite Heyting-valued modal logic

## Finding

Fix a nontrivial finite Heyting algebra \(L\), a crisp Kripke model with \(L\)-valued propositional valuations, a world \(w\), and \(q\geq 1\) formulas \(\Box\psi_1,\ldots,\Box\psi_q\). Write \(P=J(L)\) for the finite poset of nonzero join-irreducibles of \(L\), and write \(I(a)=\{p\in P:p\leq a\}\) for the corresponding down-set of \(P\). For each \(i\), let \(m_i=\bigwedge_{v\in R[w]}\llbracket\psi_i\rrbracket(v)\) (an empty meet is \(1\)), and let \(B_i=\min(P\setminus I(m_i))\).

**Exact universal local budget, with value sensitivity.** There is a subset \(E\subseteq R[w]\) of at most \(\sum_{i=1}^q |B_i|\) successors preserving *all* exact values \(m_i\) when the meet over \(R[w]\) is replaced by the meet over \(E\). The bound is optimal **for every prescribed tuple of output values** \((m_1,\ldots,m_q)\in L^q\): some finite one-step model with distinct atomic arguments \(\psi_i\) needs exactly that many successors. Consequently, the smallest worst-case uniform bound over all \(q\)-tuples of boxed atomic formulas is

\[
q\operatorname{width}(J(L)),
\]

and it is attained. This improves the previously available \(q(h(L)-1)=q|J(L)|\) bound whenever the join-irreducible poset has width below its cardinality.

**Exact instance optimization.** For a fixed finite set of successors \(S=R[w]\), define the nonempty hyperedges

\[
H_{i,b}=\{v\in S:b\not\leq\llbracket\psi_i\rrbracket(v)\},\qquad b\in B_i.
\]

A subset \(E\subseteq S\) preserves all the output values precisely when \(E\) intersects every \(H_{i,b}\). Hence the exact optimum is the transversal number of this explicit hypergraph (zero if there are no edges). Determining whether \(k\) successors suffice is NP-complete even for the two-element Boolean algebra, a depth-one star frame, and atomic arguments \(\psi_i\), with the number of boxed formulas part of the input.

## Assumptions and scope

A finite Heyting algebra is a finite bounded distributive lattice with its induced relative pseudocomplement; only the meet operation is needed for the local proof. By finite distributive representation, \(L\cong\operatorname{Down}(P)\), with meets corresponding to intersections and \(I(1)=P\). The accessibility relation is an arbitrary crisp binary relation, and \(\llbracket\Box\psi\rrbracket(w)=\bigwedge_{v\in R[w]}\llbracket\psi\rrbracket(v)\). No reflexivity, transitivity, nonemptiness of the successor set, or bounded modal nesting is required for the local theorem. Atomic valuations may assign arbitrary elements of \(L\). The sharpness construction concerns a single depth-one star with \(q\) independent propositional atoms; no minimum-total-model-size claim is made.

## Proof

**1. Local compression.** For any \(i\), Birkhoff's representation gives \(I(m_i)=\bigcap_{v\in R[w]}I(\llbracket\psi_i\rrbracket(v))\). The complement of the down-set \(I(m_i)\) is an up-set, uniquely generated upward by the antichain \(B_i\). For each \(b\in B_i\), because \(b\notin I(m_i)\), at least one \(v(i,b)\in R[w]\) omits \(b\) from its down-set. Retain the union \(E\) of these witness successors. For each \(i\), its retained meet contains \(I(m_i)\), since a meet over fewer elements can only increase. It contains no \(b\in B_i\). Were it to contain any point above some \(b\in B_i\), downward closure would force it to contain \(b\), a contradiction. Thus its down-set equals \(I(m_i)\). There are at most \(\sum_i|B_i|\) chosen successors. If every \(m_i=1\), all \(B_i\) are empty and \(E=\varnothing\) works, including when the original successor set is empty.

**2. Sharpness for every output-value tuple.** Fix arbitrary \(m_1,\dots,m_q\in L\). For every ordered pair \((i,b)\) with \(b\in B_i\), create a separate successor \(v_{i,b}\), and interpret \(\psi_j\) as the independent atom \(p_j\). At \(v_{i,b}\), set \(p_i\) to the down-set \(P\setminus\uparrow b\), and set each other \(p_j\) to top \(P\). The intersection for coordinate \(i\) is precisely \(P\setminus\uparrow B_i=I(m_i)\). For a fixed pair \((i,b)\), every other successor retains \(b\) in coordinate \(i\): another \(b'\in B_i\) is incomparable with \(b\), and a successor for another coordinate assigns top there. Deleting \(v_{i,b}\) therefore strictly increases the \(i\)-th meet. Every successor is indispensable, so the minimum is \(\sum_i|B_i|\). If all boundaries are empty, take a root with no successors. Taking each \(B_i\) to be a maximum antichain of \(P\), and \(m_i\) the down-set \(P\setminus\uparrow B_i\), gives the matching worst-case lower bound \(q\operatorname{width}(P)\). Every boundary is an antichain, giving the upper bound.

**3. Exact hypergraph.** Given a fixed finite successor set \(S\), for \(E\subseteq S\) the resulting meet in coordinate \(i\) is a superset of \(I(m_i)\). Equality holds if and only if each minimal missing generator \(b\in B_i\) is omitted by at least one retained successor. This is equivalent to \(E\cap H_{i,b}\ne\varnothing\) for every pair \((i,b)\). Therefore minimum-size pruning is exactly the ordinary minimum hitting-set problem on the displayed hypergraph.

**4. Complexity boundary.** The optimization decision problem is in NP: given the finite matrix of successor truth values and a proposed subset \(E\), compute all \(q\) original and retained meets and compare. For hardness, start with any finite HITTING SET instance with nonempty hyperedges \(F_1,\ldots,F_q\) on a finite vertex set \(S\). Use Boolean \(L=\{0,1\}\), one root with successor set \(S\), and an atom \(p_i\) false at successor \(v\) exactly when \(v\in F_i\). Each original value \(\Box p_i\) at the root is false. It remains false after pruning to \(E\) if and only if \(E\cap F_i\ne\varnothing\). Thus the proposed size-\(k\) pruning exists precisely when the original HITTING SET instance has a transversal of size at most \(k\). This is a polynomial many-one reduction even on a depth-one star and establishes NP-completeness.

**5. Finite exact-value tree certificates.** In the finite-tree construction of Das, Ray and Mali (2026, Section 5.2), at each node apply step 1 simultaneously to the boxed subformulas relevant at that node rather than the height-based meet-compression lemma. Structural induction on formula complexity, using unchanged propositional valuations at copied nodes and the exact-meet condition at modal nodes, preserves every relevant subformula's value. Thus one may uniformly replace the original per-node branching estimate \(q(h(L)-1)\) by \(q\operatorname{width}(J(L))\), or use the smaller \(\sum_i |\min(J(L)\setminus I(m_i))|\) at an individual node. This is a valid upper bound for an extracted tree, not an assertion that the minimum number of nodes in every equivalent model equals this quantity.

## Verification

The standalone `artifacts/verify.py` uses exact finite-set arithmetic. It exhaustively compares meet preservation with the asserted hypergraph condition across successor-value matrices on four representative small posets (three-element chain; three-element antichain; three-point fork; four-point diamond), verifies the bound, and constructs the indispensable-witness sharpness example for every one- and two-coordinate target-value tuple. It separately tests a three-edge Boolean HITTING SET instance. The script prints `VALUE_SENSITIVE_MODAL_CERTIFICATES_VERIFY_OK` on success. The infinite-arities theorem and NP-hardness are established by the arguments above, not by enumerating finite examples.

## Relationship to prior work

Das, Ray and Mali (2026, arXiv:2608.05550v1, Section 5) prove meet compression by height and obtain a branching bound depending on \(h(L)-1\). The present claim keeps their semantics but gives a sharp, output-value-dependent bound using the antichain boundary of a down-set, a simultaneous sharpness construction, and an instance-exact hypergraph characterization with an NP-completeness boundary. The finite distributive representation and the general notion of lattice breadth are classical and are not claimed to be novel. Existing multivalued counterexample generation for De Morgan-algebra CTL is relevant background but does not, from accessible bibliographic materials, resolve the particular Fitting finite-Heyting certificate budget.

## Limitations

Historical-priority uncertainty remains: the sharp local lemma could be implicit in classical lattice-breadth arguments, and some earlier multivalued model-checking source may contain a separately expressed minimum-witness reduction. The published-source and indexed-record searches do not prove uniqueness. The algorithmic NP-completeness statement treats the number of atomic box obligations as part of the input; no hardness assertion is made for fixed \(q\). The result concerns exact one-step successor pruning and a justified improved extracted-certificate bound, not minimum global equivalent-model size or minimal countermodel size. Verification is a finite cross-check and not an exhaustive proof of the unbounded statement. Independent validation has not been performed.

## References

1. Litan Kumar Das, Kumar Sankar Ray, Prakash Chandra Mali, *A Bitopological Approach to Finite Reduction and Bounded Exact-Value Certificates for Fitting's Finite Heyting-valued Modal Logic*, arXiv:2608.05550v1 (first public version August 6, 2026), especially Sections 2.1 and 5. https://arxiv.org/abs/2608.05550
2. G. Birkhoff, finite distributive-lattice representation theorem; see D. Davey and H. Priestley, *Introduction to Lattices and Order*, Cambridge University Press, 2002, for the standard down-set representation and finite lattice theory.
3. A. Gurfinkel and M. Chechik, *Generating Counterexamples for Multi-valued Model-Checking*, FME 2003, LNCS 2805, pp. 503–521, doi:10.1007/978-3-540-45236-2_28. Different De Morgan-algebra CTL setting.
4. SageMath reference documentation, *Finite lattices and semilattices*, `breadth()` and `canonical_meetands()`: https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/posets/lattices.html (classical breadth context).
