# A counterexample for saturation with multiple forbidden ordered graphs

## Finding

Let \(B\) be the ordered matching on \([6]\) with edge set \(\{(1,3),(2,5),(4,6)\}\). Let \(A\) be the ordered matching on \([8]\) with edge set \(\{(1,3),(2,7),(4,5),(6,8)\}\). These are, respectively, \(\Gamma_3\) and \(\Gamma_{\{0,1,0\}}\) in Bošković and Keszegh's notation. Then

\[
\operatorname{sat}_{<}(n,A)=O(1),\qquad
\operatorname{sat}_{<}(n,\{A,B\})\ge \frac{n-1}{4}.
\]

Thus the proposed comparison \(\operatorname{sat}_{<}(n,\{A,B\})=O(\operatorname{sat}_{<}(n,A))\) is false.

## Assumptions and scope

All graphs are finite and simple, and their vertices carry a fixed linear order. An ordered subgraph embedding preserves the vertex order but is not required to be induced. For a finite family \(\mathcal F\), \(\operatorname{sat}_{<}(n,\mathcal F)\) denotes the minimum number of edges in an \(n\)-vertex ordered graph containing no member of \(\mathcal F\) such that adding any missing edge creates a copy of at least one member of \(\mathcal F\). The family version is the natural extension of the single-forbidden-graph definition in the cited paper.

The graph \(B=\Gamma_3\) has edges \((1,3),(2,5),(4,6)\), none of which joins consecutive positions. The graph \(A=\Gamma_{\{0,1,0\}}\) is obtained by inserting two vertices inside the interval of the middle link edge of \(B\), but outside the other two link edges, and joining those two inserted consecutive vertices. With the resulting order labeled \([8]\), its edges are \((1,3),(2,7),(4,5),(6,8)\). Its only edge whose endpoints are consecutive in the order is \((4,5)\). Deleting those two vertices from an ordered copy of \(A\) leaves an ordered copy of \(B\).

## Proof

**Bounded saturation of \(A\).** The cited paper proves in Theorem 20 and Claim 21 that \(\operatorname{sat}_{<}(n,\Gamma_{\{0,1,0\}})=O(1)\). Claim 21 supplies a witness graph and verifies both avoidance and the edge-addition property; Lemma 13 then turns the witness into bounded saturation. Hence \(\operatorname{sat}_{<}(n,A)=O(1)\).

**Linear lower bound for the pair.** Let \(H\) be any \(\{A,B\}\)-saturated ordered graph on \(n\) vertices. Suppose that two consecutive vertices \(u<v\) in the order are both isolated in \(H\). Adding \(uv\) must create a copy of \(A\) or \(B\), and any such new copy must use \(uv\), since \(H\) avoids both graphs.

No edge of \(B\) can map to \(uv\): each edge of \(B\) has at least one vertex of the pattern strictly between its endpoints, while there is no vertex of \(H\) between consecutive \(u,v\). Therefore the new copy must be a copy of \(A\). The same order argument forces \(uv\) to play the role of the unique consecutive-endpoint edge \((4,5)\) of \(A\). The other three edges of that copy are old edges of \(H\). Removing the two vertices representing \((4,5)\) leaves an order-preserving copy of \(B\) using only old edges, contradicting that \(H\) is \(B\)-free.

Consequently, no two isolated vertices of \(H\) are consecutive in its vertex order. Write \(r\) for the number of non-isolated vertices and \(z=n-r\) for the number of isolated vertices. At most one isolated vertex can occur in each gap before, between, or after the \(r\) non-isolated vertices, so \(z\le r+1\). Thus \(r\ge (n-1)/2\). Every non-isolated vertex has degree at least one, whence \(2|E(H)|\ge r\) and

\[
|E(H)|\ge \frac{n-1}{4}.
\]

Taking the minimum over all such \(H\) gives \(\operatorname{sat}_{<}(n,\{A,B\})\ge(n-1)/4\). Since \(\operatorname{sat}_{<}(n,A)\) is bounded, the pair function cannot be \(O(\operatorname{sat}_{<}(n,A))\). This disproves Problem 43 of the cited paper.

## Verification

The definitions of \(\Gamma_k\) and \(\Gamma_{\{m_1,m_2,m_3\}}\) in the source give the displayed edge sets directly. The source's open-access PDF was inspected at the definitions, Theorem 20/Claim 21 (including the witness diagram and case analysis), Corollary 18, and Problem 43. The lower-bound argument above is an infinite counting proof; it uses no finite experiment or computational certificate. No exact value or matching upper bound for \(\operatorname{sat}_{<}(n,\{A,B\})\) is claimed.

## Relationship to prior work

Bošković and Keszegh prove bounded saturation for \(\Gamma_{\{0,1,0\}}\), linear saturation for \(\Gamma_3\), and explicitly ask whether adding a second forbidden ordered graph can increase saturation beyond \(O(\operatorname{sat}_{<}(n,A))\) (Problem 43). Their paper does not state the pair \((\Gamma_{\{0,1,0\}},\Gamma_3)\) as a counterexample. The new implication is that the minedge-deleted skeleton \(B\) is forced into every newly created copy of \(A\) when an edge is added between consecutive isolates, making bounded pair saturation impossible.

## Limitations

The result proves a linear lower bound for the pair saturation number, sufficient to refute the proposed comparison. It does not establish a matching \(O(n)\) upper bound or the exact pair saturation number. The literature comparison used the primary full text and targeted semantic searches; those searches are not an exhaustive proof that no independent later account exists.

## References

V. Bošković and B. Keszegh, “Saturation of Ordered Graphs,” arXiv:2203.05307v1, first publicly available 10 March 2022. Published as *SIAM Journal on Discrete Mathematics* 37(2) (2023), 1118–1141. DOI: 10.1137/22M1485735. Primary source: https://arxiv.org/abs/2203.05307; open-access PDF: https://arxiv.org/pdf/2203.05307.
