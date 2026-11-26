# Sharp depth for frame-validity axiomatizations at bounded reachability

## Finding

For every integer \(h\ge0\), let \(\mathcal B_h\) consist of the nonempty finite Kripke frames satisfying \(R^*=\bigcup_{j=0}^hR^j\), with \(R^0\) the identity relation. The least uniform modal-depth bound for defining, relative to \(\mathcal B_h\), **all basic-modally definable frame classes** is exactly \(h+1\). Definability means validity at all worlds under all valuations of a possibly infinite set of formulas. No universal modality is used.

In particular, every class closed under generated subframes, finite disjoint unions and surjective bounded-morphic images admits a relative axiomatization of depth at most \(h+1\); conversely basic modal validity is preserved by these operations. For the lower bound, for each \(h\) two frames in \(\mathcal B_h\) agree on the validity of every basic formula of depth at most \(h\) but differ on an explicit formula of depth \(h+1\). Thus even allowing an arbitrary set of formulas of depth at most \(h\) does not suffice. This bound concerns validity on frames, not just descriptions at a distinguished point.

## Upper bound

For a frame \(G\) and a point \(g\), write \(G_g\) for the generated subframe of points reachable from \(g\). The three operations preserve \(\mathcal B_h\). This is immediate for generated subframes and disjoint unions. For a surjective bounded morphism, lift a target path from a preimage of its start using the back condition; then a path of length at most \(h\) between the lifted endpoints projects to a target path using forth. Basic frame validity is preserved under generated subframes by extension of valuations, under disjoint unions componentwise, and under surjective bounded morphisms by pullback of valuations and forth/back.

For \(F\in\mathcal B_h\) and \(w\in F\), introduce one fresh atom \(p_x\) for each \(x\in F\). Let \(E_F\) assert that exactly one label holds and, for each possible label \(p_x\), that the set of successor labels is precisely those indexed by successors of \(x\). The latter requirement consists of \(p_x\to\Diamond p_y\) for each edge \(xRy\), and \(p_x\to\Box\bigvee_{xRy}p_y\), with the empty disjunction interpreted as false. Set
\[
\delta_{F,w}=p_w\land\bigwedge_{j=0}^h\Box^jE_F.
\]
This has depth at most \(h+1\). For \(G\in\mathcal B_h\), it is satisfiable at \(g\) exactly when a rooted surjective bounded morphism \(G_g\to F_w\) exists. Indeed \(E_F\) holds at every reachable point, and the unique labels give a map with forth and back. Forth places its image in \(F_w\), and back puts every point of \(F_w\) in its image by lifting a path from \(w\). Conversely such a map supplies the labels, and labels outside \(G_g\) do not affect truth at \(g\). The identity map shows that the diagram is satisfiable at \(w\) in \(F\).

Suppose \(\mathcal K\subseteq\mathcal B_h\) has the three closures. Let \(F\in\mathcal B_h\) satisfy all the depth-at-most-\(h+1\) formulas valid in \(\mathcal K\). For each \(w\in F\), \(F\) does not validate \(\neg\delta_{F,w}\), so this negation is not valid throughout \(\mathcal K\). Some pointed frame in \(\mathcal K\) thus satisfies the diagram. Its generated subframe maps onto \(F_w\), so \(F_w\in\mathcal K\). The finite disjoint union of the \(F_w\)'s maps onto \(F\) by the inclusions on each copy (successors stay in that copy of the generated subframe). Thus \(F\in\mathcal K\). The empty class is defined by false. This gives the upper bound, since every definable class has the closures.

## Sharpness for frame validity

Write \(D_j\) for the chain \(0\to1\to\cdots\to j\) ending at a dead end and \(L_j\) for the same chain with a loop at \(j\). Both belong to \(\mathcal B_j\). For \(h\ge1\) take
\[
G=D_h\sqcup L_{h-1},\qquad F=G\sqcup L_h.
\]
The two frames lie in \(\mathcal B_h\). To compare depth-at-most-\(h\) validity, a failure at an existing world of \(G\) is of course still a failure in \(F\). For the extra component \(L_h\), any pointed failure at a nonroot world transfers identically to the corresponding generated suffix of \(L_{h-1}\). A pointed failure at the root transfers to the root of \(D_h\) by using the same atom values along the two paths. A formula of depth at most \(h\) at the root can inspect atom values at the terminal world but cannot inspect its outgoing edges, since exactly \(h\) steps are needed to reach it. Formally the depth-\(d\) types at index \(i\) agree for \(d\le h-i\), by induction on \(d\) matching the single successor when \(i<h\). This holds for every valuation and any finite set of atoms occurring in a formula. Consequently \(G\) and \(F\) have identical depth-at-most-\(h\) frame theories.

On the other hand, \(G\) validates the depth-\(h+1\) formula
\[
\psi_h=\neg\bigl(\Diamond^{h-1}p\land\Diamond^h\neg p\land\Diamond^{h+1}\top\bigr).
\]
In the dead-end chain the last conjunct is false everywhere. In the shorter loop-ending chain the walks of lengths \(h-1\) and \(h\) from any world both end at the loop, so the first two conjuncts cannot both hold. In the added \(L_h\), choose \(p\) true at \(h-1\) and false at \(h\). At its root the conjunction is then true, so \(F\) does not validate \(\psi_h\). For \(h=0\) use \(G=D_0\), \(F=G\sqcup L_0\) and \(\psi_0=\Box\bot\); any depth-zero failure in either component transfers to the single world of \(G\). In both cases the subclass of \(\mathcal B_h\) defined by \(\psi_h\) cannot be axiomatized at depth \(h\), because such a theory cannot distinguish \(F\) and \(G\).

## Related results and verification

The upper-bound construction is a finite relative version of standard diagram methods. Compare Blackburn, de Rijke and Venema, *Modal Logic* (2001), §3.4 on finite transitive frames; Badia, Caicedo and Noguera, [DOI:10.1016/j.apal.2023.103273](https://doi.org/10.1016/j.apal.2023.103273), §4.3 on finite frames with local p-morphic images and the ordinary operation on finite transitive frames; and van Benthem, ten Cate and Yang, [arXiv:2603.12171](https://arxiv.org/abs/2603.12171), §5.1, for a finite theorem with a universal modality. The quantitative claim here concerns the sharp uniform depth for frame validity within \(\mathcal B_h\), with a lower bound that matches all roots up to depth \(h\), not a priority claim for finite diagram methods.

Run `python3 CHECK.py` for small-case corroboration of the lower-bound pair: it compares all pointed depth types over one atom under arbitrary valuations of each component and checks the displayed separator at every root. The proof transfers depth-\(h\) validity for arbitrary finite atom sets and handles all \(h\).
