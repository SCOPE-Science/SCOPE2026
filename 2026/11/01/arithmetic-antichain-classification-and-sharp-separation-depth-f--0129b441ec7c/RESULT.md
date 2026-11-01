# Arithmetic antichain classification and sharp separation depth for finite deterministic modal frames

## Finding

Let \(F=(W,f)\) and \(G=(V,g)\) be nonempty finite serial deterministic Kripke frames: each world has precisely one successor. Let \(\operatorname{Log}(F)\) be the set of all ordinary basic-modal formulas valid at every world of \(F\), under every valuation, with no universal modality. For a world \(w\), let \(t_F(w)\) be the least nonnegative index at which its forward orbit enters a directed cycle, and let \(p_F(w)\) be the length of that cycle. Equip \(\mathbb N_0\times\mathbb N_{\ge1}\) with the divisibility-tail order
\[
 (t,p)\preceq(T,P)\quad\Longleftrightarrow\quad t\le T\ \text{and}\ p\mid P.
\]
Let \(A_F\) denote the set of maximal distinct signatures \((t_F(w),p_F(w))\), under this order.

**Theorem (complete arithmetic classification).** For all such \(F,G\),
\[
\operatorname{Log}(F)\subseteq\operatorname{Log}(G)
\quad\Longleftrightarrow\quad
(\forall(t,p)\in A_G)(\exists(T,P)\in A_F)\bigl[t\le T\land p\mid P\bigr].
\]
Thus \(\operatorname{Log}(F)=\operatorname{Log}(G)\) if and only if \(A_F=A_G\). Conversely every nonempty finite antichain in this arithmetic order occurs as \(A_F\) for a finite serial deterministic frame, by taking the disjoint union of the corresponding directed lassos.

**Effective finite separation.** If \(\operatorname{Log}(F)\not\subseteq\operatorname{Log}(G)\), there is a basic modal formula valid on \(F\) but invalid on \(G\), with modal depth at most \(|W|\) and using at most \(\lceil\log_2 |V|\rceil\) propositional letters. The upper bound \(|W|\) is sharp for every positive size \(|W|=n\): a directed tail of \(n\) worlds ending in a self-loop and a directed cycle of \(n+1\) worlds validate the same formulas of depth less than \(n\), but differ on \(\Box^{n-1}p\leftrightarrow\Box^n p\).

## Assumptions and scope

The signature is the standard classical propositional modal language with arbitrary Boolean connectives and the unary forward \(\Box\) modality. Under the sole-successor semantics, \(\Box\varphi\) at a world means \(\varphi\) at its unique successor. There is no universal modality, nominals, graded counting modality, or fixed-point operator. Valuations are arbitrary subsets of the full finite world set for each propositional letter. Both frames are finite, nonempty, and *total functional*; neither injectivity nor connectedness is assumed. The least preperiod and period are uniquely defined by finiteness, and every forward orbit has exactly \(t+p\) distinct worlds.

By a directed lasso of signature \((t,p)\) we mean the function on \(\{0,1,\ldots,t+p-1\}\) taking \(i\mapsto i+1\) for \(i<t+p-1\) and \(t+p-1\mapsto t\). In particular, \(t=0\) gives a directed cycle. The zero-step modal iterate is the identity. The finite antichain is nonempty because the frame is nonempty.

## Proof

**1. Rooted orbit morphisms.** Fix worlds \(w\in F\) and \(v\in G\) with signatures \((T,P)\) and \((t,p)\), respectively. Consider the map of their forward-generated subframes which sends \(f^j(w)\) to \(g^j(v)\) for each nonnegative integer \(j\). It is well-defined if and only if \(t\le T\) and \(p\mid P\): the unique first equality on the source orbit is between indices \(T\) and \(T+P\), which must also be an equality on the target orbit. The source's cycle then maps onto the target's cycle, and the entire target orbit is reached. The map is a surjective bounded morphism for functional relations (it commutes with successor and preserves the unique forth/back successor), and it maps the chosen source root to the chosen target root. Pulling a valuation backward preserves truth of every basic modal formula at the related roots, by induction on its formation.

**2. Sufficient condition for theory inclusion.** Suppose every signature in \(A_G\) is dominated by one in \(A_F\). Every \(v\in G\) has signature below a maximal signature of \(G\), hence below a signature realized by some \(w\in F\). If a formula fails at \(v\) under a valuation on \(G\), restrict that valuation to its forward orbit and pull it back to the rooted orbit at \(w\) using step 1. The formula then fails at \(w\) in a valuation extended arbitrarily over other worlds of \(F\). Therefore any formula valid on \(F\) is valid on \(G\).

**3. Explicit separating formula.** Conversely suppose a world \(v\in G\) has signature \((t,p)\) not dominated by any signature realized in \(F\). Put \(L=\max_{w\in F}\bigl(t_F(w)+p_F(w)\bigr)\). Every forward-generated orbit uses at most \(|W|\) worlds, so \(L\le|W|\). Colour the \(t+p\) distinct forward-orbit worlds of \(v\) by pairwise distinct binary strings of length \(k=\lceil\log_2 |V|\rceil\), with \(k\) propositional variables. Write \(\chi_j\) for the full conjunction of positive and negative literals encoding the colour assigned to orbit world number \(j\), for \(0\le j<t+p\). Write \(c(i)\) for the unique representative in \(\{0,\ldots,t+p-1\}\) of the world \(g^i(v)\); namely \(c(i)=i\) for \(i<t\), and \(c(i)=t+((i-t)\bmod p)\) otherwise. Form
\[
\Theta=\bigwedge_{i=0}^{L}\Box^i\chi_{c(i)}.
\]
Give the target orbit its designated colours and extend the valuation arbitrarily to the rest of \(G\). Then \(\Theta\) is true at \(v\).

Suppose \(\Theta\) were true at some world \(w\in F\) under any valuation. Let its orbit signature be \((T,P)\). Because \(T+P\le L\), the one world \(f^T(w)=f^{T+P}(w)\) would have to satisfy both complete literal codes \(\chi_{c(T)}\) and \(\chi_{c(T+P)}\). Pairwise distinct codes imply \(c(T)=c(T+P)\). A direct inspection of a lasso's forward orbit shows that equality is possible exactly when \(T\ge t\) and \(p\mid P\), contradicting the choice of \(v\). Thus \(\neg\Theta\) is valid on \(F\) but invalid on \(G\). Its depth is \(L\le|W|\). In this noncoverage case the target orbit cannot have just one world, because signature \((0,1)\) is below every signature, so there are enough distinct Boolean colour codes.

**4. Reduction to maximal antichains and completeness.** A finite set of signatures is generated downward by its unique set of maximal elements. Applying steps 2–3 in both directions shows that equality of validity theories is exactly equality of the finite maximal antichains. Any chosen finite nonempty antichain \(A\) is realized by taking the disjoint union of the lassos indexed by its elements: the root of the \((t,p)\)-lasso realizes that signature, and every other world in that component has a signature below it. Hence the maximal signature set is exactly \(A\). There is no hidden realizability restriction.

**5. Optimality of the depth bound.** Let \(F_n\) have vertices \(0,\ldots,n-1\), successor \(i\mapsto\min(i+1,n-1)\). Let \(G_n\) be the \((n+1)\)-cycle. The successive worlds at indices \(0,1,\ldots,n-1\) from the root \(0\) in each frame are distinct. Fix any finite set of letters in a modal formula and any depth \(d<n\). In a total functional frame, truth at a root of a formula of depth at most \(d\) depends only on the propositional truth-values at successive points \(0,\ldots,d\). Both rooted frames realize *every* possible such length-\(d+1\) valuation word (assign each of these distinct worlds independently). Thus they have identical depth-less-than-\(n\) validity theories, despite their different sizes. At every world of \(F_n\), \(f^{n-1}(w)=f^n(w)\), so the depth-\(n\) formula \(\Box^{n-1}p\leftrightarrow\Box^n p\) is valid. At a world of \(G_n\), the two iterates are different; a valuation separating them makes the formula false. This proves the optimality claim, including \(n=1\).

## Verification

Run `python3 checker.py` using only the Python standard library. It computes every total function on labelled sets of sizes \(1\) through \(4\), obtains its maximal signature antichain, and independently compares the predicted modal-theory inclusion with inclusion of all finite colour words (every colouring over an alphabet of size equal to the world count, on length \(2n+2\) forward paths). It also independently tests all pairs of lasso signature types with total orbit length at most four. Successful execution prints `ALL_CHECKS_OK`. These are finite regression checks, not a replacement for the unrestricted proof. The explicit separating formula and sharp depth example are proved symbolically above.

## Relationship to prior work

Johan van Benthem, Balder ten Cate and Xi Yang, *When do modal definability and preservation theorems transfer to the finite?* (arXiv:2603.12171, posted March 12, 2026) investigate finite-frame modal definability and the relationship with morphisms and closure operations. Their Section 5.1 discusses a version with the universal modality. The result here concerns **only** the ordinary basic modal language and the special, but all-size, class of nonempty finite total-functional frames, and identifies a concrete arithmetic normal form and a sharp finite separating depth. The standard valuation-pullback principle for bounded morphisms is inherited from classical modal model theory, and is not claimed anew. Closest related published research addresses measurable modal quotients characterized by partial-function frames; that result does not give the present frame-validity antichain or separating depth. None of the inspected source passages was found to state the full arithmetic classification and sharp bound; equivalence to an older deterministic-frame classification under different terminology remains a priority risk.

## Limitations

No assertion is made for nondeterministic, partial-functional, infinite, multiagent, or nonserial frames, nor for the addition of a universal modality or fixed-point modalities. The size bound controls modal depth and propositional-letter count, not formula length: the displayed separating formula has \(L+1\) conjuncts and may be quadratic in its explicit written length. The computational checks cover only the stated finite instances. Searches cannot prove historical uniqueness; a classical formulation through monounary algebras or modal varieties might be equivalent or stronger, although no decisive covering statement was located in inspected sources. Independent review has not been performed.

## References

1. J. van Benthem, B. ten Cate, X. Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1 (first posted March 12, 2026), https://arxiv.org/html/2603.12171 ; https://arxiv.org/abs/2603.12171.
2. P. Blackburn, M. de Rijke and Y. Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press (2001). Standard reference for bounded morphisms; no novelty claimed for the preservation lemma.
