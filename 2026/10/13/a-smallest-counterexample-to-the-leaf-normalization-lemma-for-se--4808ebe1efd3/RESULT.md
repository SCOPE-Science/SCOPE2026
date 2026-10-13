# A smallest counterexample to the leaf-normalization lemma for secure Italian domination
## Finding
Let \(G\) have vertices
\[
\{\ell,x,y,p,q\}
\]
and edges
\[
\{\ell x,xy,xp,xq,yp,yq\}.
\]
Equivalently, start with a diamond \(K_4-e\) on \(\{x,y,p,q\}\), where \(p\) and \(q\) are the nonadjacent degree-two vertices, and attach the leaf \(\ell\) to \(x\).

Then
\[
\gamma_I^s(G)=3,
\]
and the unique minimum secure Italian dominating function is
\[
f(x)=2,\qquad f(y)=1,\qquad f(\ell)=f(p)=f(q)=0.
\]
Thus the unique leaf \(\ell\) is labeled \(0\) in every minimum secure Italian dominating function. This contradicts the published leaf-normalization lemma asserting that every graph with at least one leaf has a minimum secure Italian dominating function assigning label \(1\) to every leaf.

Moreover, exhaustive enumeration of all simple graphs on fewer than five vertices with at least one leaf finds no counterexample, so five vertices is the smallest possible order.

## Assumptions and scope
An Italian dominating function is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that each vertex \(v\) with \(f(v)=0\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge2.
\]
For adjacent vertices \(u,v\) with \(f(u)>0\) and \(f(v)=0\), write \(f_{u\to v}\) for the function obtained by decreasing \(f(u)\) by one and setting \(f(v)=1\). A secure Italian dominating function is an Italian dominating function for which every zero-labeled vertex \(v\) has some positive neighbor \(u\) such that \(f_{u\to v}\) is still Italian dominating.

The conclusion concerns the published leaf-normalization statement itself. It does not claim that every later theorem that cites that lemma is false; such statements require separate proofs or counterexamples.

## Proof
Define
\[
f(\ell)=0,\quad f(x)=2,\quad f(y)=1,\quad f(p)=f(q)=0.
\]
The zero vertex \(\ell\) sees weight \(2\) from \(x\), and each of \(p,q\) sees total weight \(3\) from \(x,y\). Hence \(f\) is Italian dominating.

It is secure. For \(\ell\), transfer one unit from \(x\) to \(\ell\). The resulting labels on \((\ell,x,y,p,q)\) are
\[
(1,1,1,0,0),
\]
and each of \(p,q\) sees weight \(2\). For \(p\), transfer one unit from \(y\) to \(p\); then \(\ell\) still sees \(2\) at \(x\), while \(q\) sees weight \(2\) from \(x\). The argument for \(q\) is symmetric. Thus
\[
\gamma_I^s(G)\le3.
\]

No function of weight at most \(2\) is secure Italian. Weight \(1\) is impossible. If weight \(2\) consists of one label \(2\), the only possible Italian placement is at the universal vertex \(x\). But then a transfer from \(x\) to \(p\) leaves \(\ell\) with only one unit in its neighborhood, so \(p\) has no valid moving neighbor. If weight \(2\) consists of two labels \(1\), then either \(\ell=0\), which is impossible because its unique neighbor contributes at most one, or \(\ell=1\), leaving only one additional unit and making at least one of \(p,q\) insufficiently dominated. Therefore
\[
\gamma_I^s(G)=3.
\]

It remains to prove uniqueness at weight \(3\). A weight-three labeling has type \((2,1)\) or \((1,1,1)\).

For type \((2,1)\), if \(\ell=0\), then \(x=2\) is forced. Placing the remaining label \(1\) at \(\ell\), \(p\), or \(q\) fails security: respectively, defending \(p\) or \(q\) from \(x\) leaves another zero vertex, or the leaf, with neighborhood weight one. The placement at \(y\) is exactly the function above. If \(\ell=1\) and \(x\ne2\), the only possible weight-three Italian pattern is \(f(y)=2\) with all other nonleaf vertices zero, and moving from \(y\) to either \(p\) or \(q\) leaves the other with neighborhood weight one. No placement with \(\ell=2\) is Italian. Hence the displayed \((2,1)\) function is the only secure one.

For type \((1,1,1)\), the only Italian supports are \(\{\ell,x,y\}\) and \(\{\ell,p,q\}\). The first is not secure because moving either \(x\) or \(y\) to one of \(p,q\) leaves the other with neighborhood weight one. The second is not secure because no transfer into \(x\) preserves Italian domination: moving from \(\ell\) leaves the leaf with only one neighboring unit, while moving from \(p\) or \(q\) leaves the moved-from vertex insufficiently dominated. Thus no all-one labeling is secure.

Therefore the displayed function is the unique minimum SIDF, and its leaf has label \(0\).

Finally, the included exhaustive checker enumerates every labeled simple graph of orders one through four, keeps every graph having at least one leaf, computes all minimum SIDFs directly from the definition, and verifies that at least one minimum function labels every leaf by \(1\). Hence no graph of smaller order is a counterexample.

## Verification
The included independent checker implements Italian domination and the one-unit security transfer directly from adjacency. On the five-vertex graph it exhausts all \(3^5\) labelings and verifies minimum weight \(3\), uniqueness, and the exact minimum labeling above.

It also verifies the precise failure in the published normalization step: transferring one unit from \(x\) to the leaf produces an Italian dominating function, but that transferred function is not secure Italian dominating. Thus preservation of Italian domination alone does not justify preservation of security.

For minimality by order, the checker exhausts all labeled simple graphs on fewer than five vertices that have at least one leaf, and for each graph exhausts all ternary labelings. It finds no smaller counterexample.

## Relationship to prior work
The foundational secure Italian domination paper defines the same transfer-based invariant and states a lemma asserting that every graph with a leaf has a minimum SIDF assigning label \(1\) to every leaf. Its proof handles a leaf labeled \(0\) by transferring one unit from its support and concludes that the transferred function is again a minimum SIDF. The present graph shows that this conclusion can fail: the transfer remains Italian dominating but loses the security property.

The same paper uses the leaf-normalization lemma in the proof of its rooted-product NP-hardness theorem and again invokes it in later tree arguments. The counterexample therefore identifies a proof dependency that requires independent re-verification. It does not, by itself, establish that those downstream statements are false.

A later secure \(w\)-domination framework identifies secure Italian domination with the vector \((2,0,0)\), and a 2024 survey uses the equivalent secure Roman \(\{2\}\)-domination formulation. Targeted searches under both names, together with searches for leaf, pendant, diamond, and correction terminology, did not locate an earlier counterexample or published correction of this lemma.

## Limitations
The result falsifies one specific normalization lemma and its stated proof step. It does not supply corrected versions of later theorems and does not claim that any downstream theorem is false.

The smallest-order statement is computational but exhaustive: all simple graphs on fewer than five vertices with a leaf are enumerated, and all labelings are checked. The arbitrary mathematical claim about the displayed graph is also proved directly without relying on the enumeration.

Literature searches cannot exclude a differently phrased or non-indexed correction.

## References
1. M. Dettlaff, M. Lemańska, J. A. Rodríguez-Velázquez, “Secure Italian domination in graphs,” Journal of Combinatorial Optimization 41 (2021), 56–72, DOI 10.1007/s10878-020-00658-1; published online 28 October 2020.
2. A. Cabrera Martínez, A. Estrada-Moreno, J. A. Rodríguez-Velázquez, “Secure w-Domination in Graphs,” Symmetry 12 (2020), 1948, DOI 10.3390/sym12121948; published 25 November 2020.
3. “Survey on Roman \(\{2\}\)-Domination,” Mathematics 12 (2024), 2771, DOI 10.3390/math12172771; published 7 September 2024.
