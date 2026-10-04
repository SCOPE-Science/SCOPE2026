# Co-degree reconstruction of complete multipartite graphs without singleton parts
## Finding
Let \\(G=K_{n_1,\\ldots,n_r}\\) be a finite simple complete multipartite graph with \\(r\\ge 2\\) and \\(n_i\\ge2\\) for every part. Then the co-degree sequence of \\(G\\) uniquely determines the multiset \\(\\{n_1,\\ldots,n_r\\}\\), and therefore determines \\(G\\) up to isomorphism.

More explicitly, put \\(n=|V(G)|\\). For a pair of distinct vertices \\(x,y\\), write \\(c_{xy}=|N(x)\\cap N(y)|\\) and call \\(d_{xy}=n-c_{xy}\\) its defect. Let \\(f_s\\) be the number of unordered vertex pairs with defect \\(s\\). If \\(m_s\\) is the number of parts of size \\(s\\) and \\(p_s=s m_s\\), then \\(p_1=0\\) and
\[
p_s=\\frac{2f_s-\\sum_{a=2}^{s-2}p_a p_{s-a}+\\mathbf 1_{2\\mid s}\\frac{s}{2}p_{s/2}}{s-1}
\]
for every \\(2\\le s\\le n\\). Hence the co-degree sequence gives the part-size profile by a triangular recurrence.

## Assumptions and scope
The co-degree sequence is the multiset of all values \\(c_{xy}\\) over unordered pairs of distinct vertices, as in Ascolese--Negrini--Pagani--Pellegrini. The theorem assumes the input graph is complete multipartite and that every part has size at least \\(2\\). It includes complete bipartite graphs with both sides of size at least \\(2\\) and arbitrary multipartite graphs with any number of parts.

The order \\(n\\) is recoverable from the length \\(\\binom n2\\) of the co-degree sequence. Once \\(n\\) is known, the defect multiset is obtained by replacing each co-degree \\(c\\) by \\(n-c\\).

## Proof
Suppose first that \\(x,y\\) lie in one part of size \\(s\\). Their common neighbors are exactly the vertices outside that part, so
\[
c_{xy}=n-s,\\qquad d_{xy}=s.
\]
If instead \\(x\\) and \\(y\\) lie in distinct parts of sizes \\(a\\) and \\(b\\), respectively, then their common neighbors are exactly the vertices outside those two parts, so
\[
c_{xy}=n-a-b,\\qquad d_{xy}=a+b.
\]

Define the two ordinary generating polynomials
\[
P(z)=\\sum_{s\\ge2}p_s z^s,
\\qquad
F(z)=\\sum_{s\\ge2}f_s z^s.
\]
The contribution to \\(F(z)\\) from pairs in the same part is
\[
\\frac12\\sum_{s\\ge2}(s-1)p_s z^s.
\]
For pairs in distinct parts, \\(P(z)^2\\) counts ordered choices of one vertex from each of two parts, but it also includes choices where both vertices come from the same part. For parts of size \\(s\\), those diagonal ordered choices contribute \\(s p_s z^{2s}\\). Dividing the remaining ordered count by \\(2\\) therefore gives
\[
F(z)=\\frac12P(z)^2-\\frac12\\sum_{s\\ge2}s p_s z^{2s}
      +\\frac12\\sum_{s\\ge2}(s-1)p_s z^s.
\]
Equivalently,
\[
2F(z)=P(z)^2-z^2P'(z^2)+zP'(z)-P(z).
\]
Taking the coefficient of \\(z^s\\) yields
\[
2f_s=\\sum_{a=2}^{s-2}p_a p_{s-a}
      -\\mathbf 1_{2\\mid s}\\frac{s}{2}p_{s/2}
      +(s-1)p_s.
\]
Because every index in the convolution is smaller than \\(s\\), this equation is triangular and rearranges to the displayed recurrence. Starting from \\(p_1=0\\), it determines \\(p_2,p_3,\\ldots,p_n\\) uniquely. Finally, \\(m_s=p_s/s\\), so all part multiplicities are determined and the complete multipartite graph is determined up to isomorphism.

For recognition within this class, run the recurrence on the observed defect frequencies, require every recovered \\(p_s\\) to be a nonnegative multiple of \\(s\\), require \\(\\sum_s p_s=n\\), and reconstruct the candidate complete multipartite graph. A forward recomputation of its co-degree multiset is then an exact final check.

## Verification
The accompanying verifier enumerates every integer partition of every order from \\(4\\) through \\(30\\) having at least two parts and every part at least \\(2\\). For all \\(5574\\) such complete multipartite types it forms the defect frequencies directly from the part sizes and verifies that the recurrence recovers the exact original partition. For all \\(65\\) such types of order at most \\(12\\), it additionally constructs the graph vertex-by-vertex and recomputes every common-neighbor count directly from adjacency, independently checking the defect formula.

The verifier reports `ALL CHECKS PASSED; reconstructed_types=5574; direct_types=65; max_order=30`. These finite checks are stress tests only; the universal statement follows from the coefficient identity and triangular recurrence above.

## Relationship to prior work
Ascolese, Negrini, Pagani, and Pellegrini introduced the co-degree realization problem in this form and gave a full solution for planar \\(C_4\\)-free graphs. Their motivating problem is broader than the present theorem, but their solved class is structurally different: complete multipartite graphs with several nontrivial parts are typically dense and contain many \\(4\\)-cycles. Inspection of the paper and searches for complete-multipartite terminology did not reveal a reconstruction theorem for this family.

Targeted searches for “co-degree sequence complete multipartite”, “common-neighbor sequence complete multipartite”, and equivalent defect-polynomial formulations did not locate a published formula implying the recurrence above. Semantic-index searches likewise returned complete-multipartite results for unrelated invariants rather than co-degree reconstruction. Thus the theorem supplies a constructive exact family result for the newly posed realization problem rather than a restatement of the planar \\(C_4\\)-free classification.

## Limitations
The proof deliberately excludes singleton parts. Algebraically, the coefficient of \\(p_1\\) in the linear term of the generating identity vanishes, so the triangular inversion needs an additional argument when singleton parts are allowed. No claim is made here that arbitrary complete multipartite graphs, or arbitrary graphs, are reconstructible from their co-degree sequences. Finite experiments outside the proved scope are not used as evidence for such a stronger statement.

## References
1. Michela Ascolese, Pietro Negrini, Silvia Maria Carla Pagani, Marco Antonio Pellegrini, “A graph reconstruction problem involving common neighbors,” arXiv:2609.08803, first submitted 2026-09-08.
