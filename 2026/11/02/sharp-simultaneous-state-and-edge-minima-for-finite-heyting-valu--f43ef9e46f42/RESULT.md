# Sharp simultaneous state and edge minima for finite Heyting-valued modal depth

## Finding

Let \(A\) be any nontrivial finite Heyting algebra, \(q=|A|\geq2\), and let \(k\geq1\) be the number of propositional variables. Work in the full class of possibly infinite \(A\)-weighted Kripke models with both residual-box and meet-diamond, the Heyting connectives, and an exact truth test for every element of \(A\). For each \(h\geq0\), define
\[
\mathcal T_0=A^k,\qquad \mathcal T_{h+1}=A^k\times A^{\mathcal T_h},\qquad N_0=q^k,\qquad N_{h+1}=q^kq^{N_h}.
\]
There are exactly \(N_h\) inequivalent pointed theories of modal depth at most \(h\), and each is realized by a finite pointed model. The type-count recursion is included to specify the inputs to the resource theorem; it is an instance of older stratified coalgebraic constructions and is not the standalone novelty claim.

**Sharp joint resource theorem.** For \(h\geq1\), every model containing at least one world of **every** depth-\(h\) pointed theory has at least \(N_h\) worlds and at least
\[
E_h=q^kN_{h-1}(q-1)q^{N_{h-1}-1}
=N_hN_{h-1}\left(1-\frac1q\right)
\]
nonzero weighted accessibility pairs. One finite weighted model realizes **both lower bounds simultaneously**, with every depth-\(h\) type occurring exactly once. On its canonical type-labelled state set, all models attaining both bounds arise as follows: for each state with signature \((c,(r_t)_{t\in\mathcal T_{h-1}})\) and each \(t\) with \(r_t\ne0\), select exactly one successor whose depth-\((h-1)\) type is \(t\), and assign that edge the weight \(r_t\); add no other nonzero edges. Every such selection is valid.

For \(q=2,k=1\), the resource pairs \((N_h,E_h)\) for \(h=1,2\) are \((8,8)\) and \((512,2048)\). For \(q=3,k=1,h=1\), the pair is \((81,162)\).

## Assumptions and scope

A finite Heyting algebra \(A\) is a finite bounded distributive lattice \((A,\wedge,\vee,0,1)\) with implication \(a\to b\) characterized by \(c\leq(a\to b)\iff c\wedge a\leq b\). A weighted Kripke model has a nonempty world set \(W\), an arbitrary function \(R:W\times W\to A\), and pointwise valuations of \(k\) variables into \(A\). It need not be transitive, reflexive, or serial. Zero-weight pairs are not counted as edges. Formula semantics use the Heyting pointwise operations, exact tests \(T_a(v)=1\) for \(v=a\) and \(0\) otherwise, and
\[
\llbracket\Diamond\varphi\rrbracket_x=\bigvee_{y\in W}(R(x,y)\wedge\llbracket\varphi\rrbracket_y),\qquad
\llbracket\Box\varphi\rrbracket_x=\bigwedge_{y\in W}(R(x,y)\to\llbracket\varphi\rrbracket_y).
\]
Arbitrary joins and meets exist because \(A\) is finite. Empty joins and meets are \(0\) and \(1\), respectively. Modal depth counts nested occurrences of either modality. Two pointed models have the same depth-\(h\) theory when every formula of depth at most \(h\) has exactly the same value at their points.

## Proof

**1. Canonical types and tests.** The depth-zero signature is the vector of \(k\) atomic values. Having defined \(\sigma_h(y)\in\mathcal T_h\), define the next signature by
\[
\sigma_{h+1}(x)=\left((\llbracket p_i\rrbracket_x)_{i=1}^k,
\left(\bigvee_{y:\sigma_h(y)=t}R(x,y)\right)_{t\in\mathcal T_h}\right).
\]
The join over an empty fibre is \(0\). When evaluating a depth-\((h+1)\) formula at \(x\), values of all immediate modal subformulas are constant within each \(h\)-type fibre, by induction. If the value on fibre \(t\) is \(v_t\), finite distributivity and the Heyting residual identity give
\[
\bigvee_y(R(x,y)\wedge v_{\sigma_h(y)})=\bigvee_t(r_t\wedge v_t),
\qquad
\bigwedge_y(R(x,y)\to v_{\sigma_h(y)})=\bigwedge_t(r_t\to v_t).
\]
Thus the signature determines every depth-\((h+1)\) formula value. Here the residual identity is \((\bigvee_i a_i)\to b=\bigwedge_i(a_i\to b)\), including an empty or infinite index family; since \(A\) is finite its proof reduces to finite joins.

Conversely, define a Boolean-valued characteristic formula \(\chi_t\) for each type by induction. For atomic \(c=(c_1,\ldots,c_k)\), put \(\chi_c=\bigwedge_i T_{c_i}(p_i)\). For \(\tau=(c,(r_t)_t)\), put
\[
\chi_\tau=\chi_c\wedge\bigwedge_{t\in\mathcal T_h}T_{r_t}(\Diamond\chi_t).
\]
Because each \(\chi_t\) has values only \(0,1\), \(\Diamond\chi_t\) evaluates to exactly \(r_t\). Hence \(\chi_\tau\) evaluates to \(1\) exactly at points of type \(\tau\) and to \(0\) elsewhere. Different signatures are therefore semantically distinguishable by formulas of the prescribed depth.

**2. Realization and truncation.** Every type is realized by a finite rooted weighted tree: for \(\tau=(c,(r_t)_t)\), create a new root of colour \(c\), and, for every \(t\) with \(r_t\ne0\), attach one independently realized child of type \(t\) with edge weight \(r_t\), assigning zero to all other pairs. This proves the exact type count \(N_h\). Every depth-\(h\) type has a canonical depth-\((h-1)\) truncation \(\pi_h\), obtained by forgetting one modal layer. The truncations are onto, because every lower type is realized in some pointed model and its point has a higher signature. Explicitly, \(\pi_1(c,r)=c\), while for \(h\ge2\)
\[
\pi_h(c,(r_t)_{t\in\mathcal T_{h-1}})=
\left(c,\left(\bigvee_{t:\pi_{h-1}(t)=s}r_t\right)_{s\in\mathcal T_{h-2}}\right).
\]
Let \(\pi_{h,j}\) be the iterated truncation from depth \(h\) to depth \(j\).

**3. Necessary edges.** Suppose \(M\) contains a state of each depth-\(h\) type. A state of signature \(\tau=(c,(r_t)_t)\) has, for every lower type \(t\) with \(r_t\ne0\), at least one nonzero-weight edge to a state of type \(t\), since the join over that fibre equals the nonzero element \(r_t\). Different \(t\) require different edges. Distinct \(\tau\) require distinct source states. Summing the lower bound over all \(q^kq^{N_{h-1}}\) signatures gives
\[
\sum_{\tau\in\mathcal T_h}\#\{t:r_t(\tau)\ne0\}=q^kN_{h-1}(q-1)q^{N_{h-1}-1}=E_h.
\]
The count uses that among all functions from the \(N_{h-1}\)-element type set to \(A\), exactly \((q-1)q^{N_{h-1}-1}\) take a nonzero value at a specified coordinate. Also at least \(N_h\) states are necessary, since distinct types cannot share a state.

**4. Simultaneous sharpness.** Take the state set to be exactly \(\mathcal T_h\). Choose, for every \(t\in\mathcal T_{h-1}\), an extension \(s(t)\in\pi_h^{-1}(t)\). Give each state \(\tau=(c,(r_t)_t)\) atomic colour \(c\), and set \(R(\tau,s(t))=r_t\) for every \(t\) with \(r_t\ne0\), and every other weight to \(0\). Different \(t\) give different target states because their truncations differ. By induction on \(j=0,\ldots,h\), the actual depth-\(j\) signature at state \(\tau\) equals \(\pi_{h,j}(\tau)\): this is immediate for \(j=0\); at the next step, target \(s(t)\) has the projected type of \(t\), and joins of edge weights across each projected fibre are exactly the coordinates prescribed by truncation. At \(j=h\), every state realizes its own name. Thus there are exactly \(N_h\) states and \(E_h\) nonzero edges.

**5. All joint minimizers.** In a universal model on exactly \(N_h\) states, the depth-\(h\) types label states bijectively. Attaining exactly \(E_h\) edges forces every lower-bound summand in step 3 to be tight. Hence for each nonzero coordinate \(r_t\) there is precisely one edge to a state whose depth-\((h-1)\) type is \(t\), and the edge weight must equal \(r_t\). There can be no other nonzero edge. Conversely, any independent choices of such targets reproduce every prescribed signature by the induction in step 4, so the characterization is necessary and sufficient.

## Verification

`python3 checker.py` uses only Python's standard library and independently computes finite chains and a four-element Boolean Heyting algebra. It exhaustively checks the modal aggregation identities for every three-successor assignment and every unary truth table on the underlying finite algebra, then constructs and reinterprets the sparse universal models at parameter choices \((q,k,h)=(2,1,1),(3,1,1),(4,1,1),(2,2,1),(2,1,2)\). The implementation checks the depth-by-depth state signatures, formula-accessible successor-weight coordinates, and edge totals. Its expected final line is `ALL_CHECKS_OK`. Exhaustive finite tests are corroboration; the all-size claims are proved above.

## Relationship to prior work

Lin and Liau (2022, arXiv:2209.14688) already develop a general many-valued coalgebraic terminal-sequence stratification and finite canonical model constructions. Accordingly, this result does **not** claim that stratified modal types or universal canonical models were first discovered here. Lin and Liau (2020, arXiv:2012.05604) explicitly describe many-valued weighted-Kripke modalities. Das, Ray, and Mali (2026, arXiv:2608.05550) prove different finite reduction and per-formula exact-value certificate bounds in finite Heyting-valued modal logic; Das (2026, arXiv:2608.08755) studies exact-truth-test expressivity over crisp accessibility. The additional assertion investigated here is the all-depth **sharp joint state/positive-edge minimum**, its closed edge formula, and characterization of all joint minimizers for arbitrary finite Heyting truth algebras. This optimization statement was not found in the inspected primary texts. Earlier generic coalgebraic constructions provide significant ingredients, and an implicit equivalent optimization in the wider literature remains possible.

## Limitations

Truth tests for every algebra element are required; without them, distinct signatures need not be definable. Accessibility is arbitrary and may be fuzzy rather than crisp; imposing S5, seriality, or other frame axioms changes the realizable types and minima. Edges mean nonzero weighted ordered pairs, not distinct undirected connections. The theorem gives extremal resource counts for representing **all** pointed depth-bounded theories in one model; it does not give a minimal size for an arbitrary individual formula or an optimal infinite-depth model. The stratified type-count part overlaps existing coalgebraic constructions. The claimed original addition is the jointly sharp positive-edge extremum and its structural equality classification, subject to further historical verification. No independent audit has been performed.

## References

1. L. K. Das, K. S. Ray, P. C. Mali, *A Bitopological Approach to Finite Reduction and Bounded Exact-Value Certificates for Fitting's Finite Heyting-valued Modal Logic*, arXiv:2608.05550, first posted 2026-08-06. https://arxiv.org/abs/2608.05550
2. L. K. Das, *Lindström Maximality for Fitting's Finite Heyting-Valued Modal Logic with Exact Truth Tests*, arXiv:2608.08755, first posted 2026-08-09. https://arxiv.org/abs/2608.08755
3. C.-Y. Lin and C.-J. Liau, *An Inductive Construction for Many-Valued Coalgebraic Modal Logic*, arXiv:2209.14688, first posted 2022-09-29. https://arxiv.org/abs/2209.14688
4. C.-Y. Lin and C.-J. Liau, *Many-Valued Coalgebraic Modal Logic: One-step Completeness and Finite Model Property*, arXiv:2012.05604, first posted 2020-12-10. https://arxiv.org/abs/2012.05604
5. A. Stanković, M. Ćirić, J. Ignjatović, *Hennessy-Milner Type Theorems for Fuzzy Multimodal Logics Over Heyting Algebras*, arXiv:2502.10126, first posted 2025-02-14. https://arxiv.org/abs/2502.10126
