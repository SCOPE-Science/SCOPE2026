# Exact free-algebra cardinalities and modal-depth cutoff for height-two partial orders

## Finding

Let \(\mathcal H_2\) be the class of all finite nonempty partial orders whose chains have at most two elements. View \(\leq\) as reflexive Kripke accessibility. For each integer \(k\geq1\), take the ordinary Boolean propositional modal language with variables \(p_1,\ldots,p_k\), Boolean connectives and \(\Diamond\); \(\Box\varphi\) abbreviates \(\neg\Diamond\neg\varphi\). Formulas are equivalent when they agree at every point of every \(k\)-valued frame in \(\mathcal H_2\).

Put \(q=2^k\). The number of equivalence classes of formulas of modal depth at most \(d\), for \(d=0,1\), is exactly
\[
\left|F_k^{(0)}\right|=2^{q},\qquad
\left|F_k^{(1)}\right|=2^{q2^{q-1}}.
\]
Every formula is equivalent over \(\mathcal H_2\) to one of modal depth at most two, and
\[
\boxed{\left|F_k\right|=\left|F_k^{(2)}\right|=2^{q(2^q-1)}.}
\]
The depth-two bound is sharp for each \(k\geq1\). In particular, the one-generated free modal algebra has exactly \(64\) elements, the two-generated one has \(2^{60}\) elements, and the three-generated one has \(2^{2040}\) elements. The Boolean algebra underlying \(F_k\) has precisely \(q(2^q-1)\) atoms.

A constructive, \(k\)-coloured, height-two pointed Kripke model on exactly \(q(2^q-1)\) points realizes all distinguishable pointed modal theories. No smaller single *fixed coloured model* can realize all those theories simultaneously. This minimality assertion is about a fixed valuation and is not a claim about uncoloured frames evaluated under varying valuations.

## Assumptions and scope

A finite partial order here has a reflexive, antisymmetric, transitive accessibility relation. Height at most two means that there are no three pairwise distinct points \(x<y<z\). Every propositional variable may have an arbitrary valuation. A colour \(r\in C=\{0,1\}^k\) is the complete truth-value vector of these variables at a point. Denote by \(\alpha_r\) its Boolean minterm. A maximal point sees only itself. Every strict successor of a nonmaximal point is maximal.

The modality is the standard existential successor modality: \(x\models\Diamond\varphi\) precisely when \(x\leq y\) for some \(y\models\varphi\). Formula equivalence is over *all* finite frames in this class, with all valuations. The free algebra is the Lindenbaum–Tarski Boolean modal algebra of this equivalence relation, not the free algebra for unrestricted \(\mathsf{S4}\), nor one for all preorders with nontrivial clusters.

## Proof

**Step 1: The complete pointed types.** Let \(x\) have colour \(r\), and let \(S(x)\subseteq C\) be the set of colours of its *strict* successors. Such successors are all maximal. If \(S(x)\subseteq\{r\}\), then the pointed model at \(x\) is bisimilar to a reflexive one-point model of colour \(r\): relate every point above \(x\) to that one point. Write this terminal type as \(t_r\). Otherwise, write the type as \((r,S(x))\); thus \(S(x)\setminus\{r\}\ne\varnothing\). There are \(2^q-2\) admissible sets \(S\) per \(r\), plus one terminal type, hence
\[
T=q(2^q-1)
\]
types. Two pointed models with the same specified type are bisimilar: relate roots and the matching maximal-colour successors, allowing their multiplicity to be ignored. For terminal types, use the preceding collapse. By induction on modal formulas, every formula is constant on each type.

**Step 2: Modal-depth-two characteristic formulas.** For \(s\ne r\), the depth-one formula \(\Diamond\alpha_s\) at an \(r\)-coloured root is equivalent to \(s\in S(x)\). Therefore the terminal-type formula is
\[
\tau_r=\alpha_r\wedge\bigwedge_{s\in C\setminus\{r\}}\neg\Diamond\alpha_s.
\]
On a nonterminal \(r\)-root, the depth-two formula
\[
\eta_r=\Diamond(\alpha_r\wedge\Box\alpha_r)
\]
holds exactly when \(r\in S(x)\). Indeed, because an off-colour strict successor exists, the root itself does not satisfy \(\Box\alpha_r\), whereas each maximal \(r\)-coloured successor satisfies \(\alpha_r\wedge\Box\alpha_r\). For every nonterminal pair \((r,S)\), the conjunction of \(\alpha_r\), the appropriate positive or negative literals \(\Diamond\alpha_s\) for all \(s\ne r\), and either \(\eta_r\) or \(\neg\eta_r\) according to whether \(r\in S\), holds precisely on type \((r,S)\). Consequently every type has a characteristic formula of modal depth at most two. Their finite disjunctions define all subsets of the \(T\) types. Since no two formulas with different subsets can be equivalent, \(F_k\) is the full Boolean powerset of the type set and has \(2^T\) elements; every modal operation respects this representation. In particular, nesting past modal depth two adds no equivalence classes.

**Step 3: Exact depth-zero and depth-one levels.** Depth-zero formulas depend only on the root colour, yielding exactly \(q\) atoms and \(2^q\) Boolean combinations. Depth-one formulas can observe the root colour \(r\) and the set of successor colours. Reflexivity ensures that this set contains \(r\), and every subset containing \(r\) occurs. Therefore there are \(q2^{q-1}\) distinct depth-one types. The minterm \(\alpha_r\), together with the literals \(\Diamond\alpha_s\) or their negations for \(s\ne r\), defines each such type. This gives exactly \(2^{q2^{q-1}}\) depth-one equivalence classes.

**Step 4: Sharpness.** Choose distinct colours \(r,s\). Compare two height-two rooted models: one has a root of colour \(r\) with one strict successor of colour \(s\); the other has a root of colour \(r\) with strict successors of colours \(s\) and \(r\). At each root the set of all successor colours is exactly \(\{r,s\}\). Their depth-one theories coincide, but \(\eta_r\) is false in the first and true in the second. Thus the depth-two bound cannot be reduced.

**Step 5: Canonical representative and its stated minimality.** Take one reflexive terminal vertex \(t_r\) of each colour \(r\in C\). For each \(r\in C\) and each \(S\subseteq C\) containing a colour other than \(r\), add one root \(u_{r,S}\) of colour \(r\), with accessibility to itself and to exactly those terminals \(t_s\) with \(s\in S\). There are exactly \(T\) vertices. The relation is a reflexive partial order of height at most two; all \(T\) types occur once. Since no vertex can realize two different distinguishable pointed theories, a fixed coloured model realizing them all requires at least \(T\) vertices.

## Verification

The standalone `verify_height_two.py` constructs the canonical coloured frame, calculates modal observational partitions by successive Boolean/modal refinement, and checks the exact numbers of types for \(k=1,2,3\). The refinement stages are respectively \((2,4,6)\), \((4,32,60)\), and \((8,1024,2040)\). For \(k=1\) it independently closes the generated Boolean algebra under complementation, meet, join and the diamond operation, obtaining all \(64\) subsets of its six states. Command: `python3 verify_height_two.py`; expected final line: `TWO_LEVEL_MODAL_TYPES_EXACT_OK`. These are finite corroborations; the unrestricted-in-\(k\) theorem is proved by the arguments above.

## Relationship to prior work

Agnew's *On Local Finiteness of Modal K4 Algebras* (arXiv:2606.02941v1, first public 2026-06-01) studies tunable Kripke/general frames and conditions characterizing local finiteness. Its qualitative results motivate quantitative free-algebra calculations but do not state this height-two partial-order depth filtration or cardinality. The established finite-height local-tabularity theorem already supplies finiteness qualitatively; that is not claimed as a new result.

Bezhanishvili, Ghilardi and Jibladze's *Free modal algebras revisited: the step-by-step method* (2014), especially Section 5, Proposition 15 and Theorem 4, supplies a powerful one-step construction of free \(\mathsf{S4}\)-algebras. That construction covers all reflexive transitive frames, including preorders and arbitrarily long chains, and does not directly give the stated finite-depth exact counts for the restricted height-two antisymmetric class. The present statement derives explicit equivalence classes and a sharp two-step collapse in that subclass. It remains possible that older special-purpose local-tabularity literature contains this exact enumeration in another language; an absence of a search hit is not a proof of priority.

## Limitations

Only the finite height-two partial-order frame class with the standard single forward modality is considered. No statement is made for all height-two *preorders* with nontrivial equivalence clusters, for height three, or for multimodal and fixpoint languages. The canonical frame's minimality is for one simultaneously representative *fixed colouring*, not for universal validity tests over uncoloured frames with variable valuations. Finite verification is not an independent certification, and historical priority beyond the inspected sources remains open to independent review.

## References

1. Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941v1 (2026-06-01), https://arxiv.org/abs/2606.02941 .
2. Nick Bezhanishvili, Silvio Ghilardi and Mamuka Jibladze, *Free modal algebras revisited: the step-by-step method* (2014), https://staff.science.uva.nl/n.bezhanishvili/Papers/Bezh-Ghi-Jib-Revised.pdf .
3. Ilya Shapirovsky, *Locally Tabular Polymodal Logics* (slides, 2022), for historical finite-height local-tabularity context, https://www.sambuz.com/doc/locally-tabular-polymodal-logics-ppt-presentation-823190 .
