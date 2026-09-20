# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

For a vertex subset meeting both factors in \(x,y\ge1\) vertices, pseudoforest sparsity gives
\[
e\le xy+x+y-2+d,
\]
where \(d\in\{0,1,2\}\) is the number of unicyclic factors. The corresponding density \(\phi_d(x,y)\) has discrete coordinate differences with numerators \(y^2-y+1-d\) and \(x^2-x+1-d\). These are nonnegative for \(d\le1\), and for \(d=2\) they are positive away from the one-vertex boundary. On that boundary the exact internal edge count is zero, giving density at most 2, while the full join of two unicyclic graphs has density strictly greater than 2. One-factor subgraphs are still sparser. Thus the whole vertex set maximizes the Nash--Williams quotient, proving the formula and, after taking ceilings, the arboricity statement.

The independent-set extension uses the analogous density \(\psi_\varepsilon(x,y)\), whose discrete differences have numerators \(y^2-\varepsilon\) and \((x-1)^2-\varepsilon\). The only apparent negative boundary in the unicyclic case again comes from a deliberately loose one-vertex bound; the actual density there is 1. The proof therefore covers all parameter boundary cases, including \(K_1\) as a tree.

A standalone definition-level verifier enumerates all 35 graph-atlas pseudotrees on at most six vertices. It exhaustively checks the Nash--Williams density on 440 pseudotree-pair joins of total order at most 11 and on 191 pseudotree--independent-set joins, with no discrepancy. Finite computation is supporting evidence and is not used as a substitute for the proof.

Correctness status: PASS.

## Originality

The closest current source is Kuanyshov--Yeginbay (arXiv:2609.20606, submitted 17 September 2026). Its abstract and full v1 were inspected, including Theorem 23 and the join examples. It proves only general join bounds and then computes complete bipartite graphs, fans, \(P_4*\overline K_3\), and wheels. It does not state an exact arbitrary-tree, arbitrary-unicyclic, or pseudotree join formula.

Searches were performed under `arboricity`, `fractional arboricity`, `graph join`, `graph sum`, `complete sum`, `pseudotree`, `pseudoforest`, `unicyclic`, `1-balanced`, `strongly balanced`, and `uniformly dense`, including equivalent density formulations. No matching exact theorem was found.

The principal residual risk is Hobbs--Kannan--Lai--Lai--Weng, *Balanced and 1-balanced graph constructions*, Discrete Applied Mathematics 158 (2010), 1511--1523, DOI 10.1016/j.dam.2010.05.004. Accessible publisher text and theorem excerpts were inspected. That paper develops generalized Cartesian-product constructions from equal-size modules joined by regular bipartite graphs; it does not state the present formulas in the inspected material. Some equal-order special cases of tree joins may be derivable from its framework. The full article was not checked line-by-line, so hidden equivalent coverage remains possible. This risk is material but does not presently supply concrete coverage of the arbitrary-order theorem, especially the unicyclic cases where a factor itself need not be 1-balanced.

Originality status: PASS, to the best of our knowledge, with the preceding residual risk retained.

## Value

The result resolves a natural structural slice left open by a very recent paper whose join theorem gives only bounds. It upgrades three isolated example types to a single exact mechanism, identifies an entire family of 1-balanced joins, and shows that the answer is insensitive to pseudotree shape. The independent-set extension simultaneously subsumes fans, wheels, joins of all trees with independent sets, and joins of all unicyclic graphs with independent sets. The proof is short and reusable as a density template for other sparse-factor join classes.

Value status: PASS.

## Limitations

The result does not classify joins of disconnected pseudoforests, cacti with several cycles, or graphs of larger cyclomatic number. The independent-set theorem has only one pseudotree factor. The complete 2010 1-balanced-construction article was not checked line-by-line. The verifier covers finite small instances only. Independent audit and independent validation have not been performed.
