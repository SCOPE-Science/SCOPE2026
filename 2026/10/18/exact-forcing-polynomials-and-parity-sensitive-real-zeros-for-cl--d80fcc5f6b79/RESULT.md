# Exact forcing polynomials and parity-sensitive real zeros for clique bouquets

## Finding

For positive integers \(s_1,\ldots,s_t\) with \(t\ge 1\), put \(a=\max_i s_i\ge2\) and let the **clique bouquet** be
\[
G=K_1\vee\left(\bigsqcup_{i=1}^{t}K_{s_i}\right).
\]
Its central vertex is adjacent to every other vertex, while distinct peripheral cliques are anticomplete. It has chromatic number \(q=a+1\). Let \(B\ge1\) be the number of peripheral cliques of order \(a\), let \(S\) be the sum of the orders of all smaller cliques, and define
\[
U=\prod_{i:s_i<a}(a)_{s_i},\qquad
V=\prod_{i:s_i<a}(a-1)_{s_i},\qquad
m=S+B(a-1).
\]
Here \((x)_j=x(x-1)\cdots(x-j+1)\), with empty products equal to one. A partial assignment from the labeled palette of exactly \(q\) colours is called *forcing* when repeated application of the following local rule yields a proper complete \(q\)-colouring: an uncoloured vertex whose coloured neighbours exhibit exactly \(q-1\) distinct colours receives the unique missing colour. Every initial assignment must be proper on its coloured vertices. Define the domain-size enumerator
\[
\mathcal F_G(z)=\sum_{f:\,f\text{ is forcing}}z^{|\operatorname{dom}f|}.
\]

**Theorem.** All forcing partial assignments are characterized by three conditions: (i) every vertex belonging to a smaller peripheral clique is initially coloured; (ii) at most one vertex is initially uncoloured in each largest peripheral clique; and (iii) either the central vertex is initially coloured, or the central vertex is initially uncoloured and its initially coloured neighbours exhibit exactly \(q-1\) distinct colours. For every such clique bouquet,
\[
\boxed{\mathcal F_G(z)=q(a!)^B z^m\big[U(1+z)(z+a)^B-aV\big].}
\]
If each of the \(q\) colours is independently assigned to each vertex with probability \(p\), and the vertex is left blank with probability \(r=1-qp\), for \(0\le p\le1/q\), the probability of forcing is
\[
\boxed{\mathrm{FC}(G;p,q)=q(a!)^B p^m\big[U(p+r)(p+ar)^B-aV r^{B+1}\big].}
\]
Both formulas count assignments to labeled vertices and labeled colours, without identifying symmetric configurations.

For \(t=1\) and \(s_1=a\), the graph is the complete graph \(K_q\); its polynomial reduces to \(q!z^{q-1}(z+q)\), already covered by known complete-graph results. For every **noncomplete** bouquet, the minimum forcing-domain size equals \(m\), and the exact number of minimum partial assignments is
\[
q(a!)^B\big(Ua^B-aV\big)>0.
\]
For the complete-graph exceptional case the minimum size is \(q-1=m+1\), with exactly \(q\cdot q!\) such assignments.

There is also a real-root rigidity theorem. Put \(c=aV/U\), which is strictly positive and at most \(a\). After removing the factor \(q(a!)^B U z^m\), the remaining factor is
\[
H(z)=(z+1)(z+a)^B-c.
\]
All roots of \(H\) are simple. If \(B\) is even, \(H\) has exactly one real root, lying in \((-1,0)\). If \(B\) is odd, it has exactly two real roots: one lies in \(( -\infty,-a)\), while the other lies in \((-1,0)\) for noncomplete bouquets and equals zero in the exceptional complete-graph case. Thus, for every noncomplete bouquet, the parity of the largest-clique count controls the number of *nonzero* real roots of the forcing enumerator. The known single-clique case has one additional zero at the origin in \(H\), while for noncomplete bouquets the origin has multiplicity exactly \(m\).

## Assumptions and scope

Every graph is finite, simple, and has the stated universal vertex. All peripheral cliques have positive integral order; at least one has order at least two. This excludes all-star bouquets, where the chromatic palette has size two and a different forcing mechanism may operate. Exactly \(q=a+1\) colours are available; neither unrestricted palettes nor alternative global notions of defining/forcing colourings are claimed. Forcing means *local propagation*, not mere uniqueness of a proper extension. The stated probability law assigns each of the \(q\) colours with the same probability \(p\), leaving blank with probability \(1-qp\). For counting, a partial assignment is a function with an explicitly chosen domain; colour labels are retained.

## Proof

**Local obstruction and characterization.** A vertex in a peripheral clique of order \(s<a\) has degree \(s\le a-1=q-2\) and hence can never see \(q-1\) different coloured neighbours, even after other vertices are coloured. It must therefore be coloured at time zero. A vertex in a peripheral clique of order \(a\) has precisely \(a=q-1\) neighbours: its peripheral clique-mates and the centre. If two vertices in this clique start blank, neither can be the first of the pair to become coloured: when the first is considered, at least the other remains blank, so it has at most \(q-2\) coloured neighbours. Therefore at most one vertex may start blank in each largest peripheral clique.

Suppose the centre is initially blank. Every peripheral vertex has the centre among its neighbours, so no peripheral vertex can be locally forced before the centre. Thus the centre must be the first forced vertex. It is eligible precisely when its initially coloured neighbours display exactly \(q-1\) different colours. These three restrictions are necessary.

They are also sufficient for a proper initial partial colouring: if the centre is already coloured, each large clique has at most one blank, and all that blank vertex's \(q-1\) neighbours are coloured distinctly (the clique, including the centre, is complete). The missing colour completes the clique. If the centre starts blank and the colour-coverage condition holds, the centre is forced first, after which the same argument fills the last vertex of each largest clique. The remaining cliques are already complete. Each forcing step is uniquely determined and preserves properness; hence every forcing partial assignment has a unique proper complete extension.

**Exact enumerator.** Fix a proper full \(q\)-colouring. Its central colour can be selected in \(q\) ways. Each peripheral clique of order \(a\) uses all \(a\) noncentral colours exactly once, giving \(a!\) choices per maximal clique. Each peripheral clique of smaller order \(s\) uses an injective choice of \(s\) of those \(a\) colours, yielding \((a)_s\) choices. The number of full colourings is consequently \(q(a!)^B U\).

Conditional on a fixed full colouring, the small-clique vertices must all belong to the initial domain, accounting for \(z^S\). Within each maximum clique one may initially colour all \(a\) vertices or all but one of the \(a\) vertices. The corresponding weight is
\[
z^a+az^{a-1}=z^{a-1}(z+a).
\]
If the centre is initially coloured, its factor is \(z\); all the permitted choices of the maximum-clique blanks work, giving the fixed-full-colouring contribution \(z^{m+1}(z+a)^B\).

If the centre is initially blank, it can be forced exactly when its noncentral neighbours collectively expose all \(a\) noncentral colours. Across the maximum cliques, one colour is absent from the initial domain **only** if that same colour is the omitted vertex-colour in every maximum clique, and it also occurs nowhere in a smaller peripheral clique. Fixing which of the \(a\) colours is absent, each small clique of size \(s\) must have its complete colouring drawn injectively from the remaining \(a-1\) colours, which has \((a-1)_s\) possibilities. Thus, among all \(q(a!)^B U\) full colourings, the total pair-count correction for uncovered centre-blank patterns is \(q(a!)^B aV z^m\); the selection of one omitted vertex in each largest clique is determined by the absent colour. Hence the all-colouring count, with no double-counting because successful partial assignments have unique full extensions, is
\[
\begin{aligned}
\mathcal F_G(z)
&=q(a!)^B U z^{m+1}(z+a)^B
+q(a!)^B U z^{m}(z+a)^B
-q(a!)^B aV z^m\\
&=q(a!)^B z^m\left[U(1+z)(z+a)^B-aV\right].
\end{aligned}
\]
For clarity, the correction counts failed centre-blank assignments with their underlying full colouring; as each such pattern omits the centre and exactly one vertex in every largest clique, it has weight \(z^m\). They are subtracted before interpreting the result as a set of forcing partial assignments.

**Probability substitution.** The graph has \(n=m+B+1\) vertices. Each successful assignment with \(k\) initially coloured vertices has probability \(p^k r^{n-k}\), where \(r=1-qp\). Multiply the above counting decomposition by these weights. The centre-coloured contribution becomes \(q(a!)^B U p^{m+1}(p+ar)^B\); the centre-blank contribution is \(q(a!)^B U p^m r(p+ar)^B\), minus the un-covered patterns \(q(a!)^B aV p^m r^{B+1}\). Factoring proves the claimed expression.

**Minimum seed number.** The lowest possible coefficient has degree \(m\), with coefficient \(q(a!)^B(Ua^B-aV)\). Since \(V\le U\), this is positive if \(B\ge2\), because \(a^B>a\); if \(B=1\) and at least one smaller clique exists, \(U>V\), because \((a)_s>(a-1)_s\) for each \(1\le s\le a-1\). Thus it is strictly positive in every noncomplete bouquet. The single complete-graph case has \(B=1,S=0,U=V=1\), and direct reduction gives \(\mathcal F_{K_q}(z)=q!z^{q-1}(z+q)\), with minimum degree \(q-1=m+1\).

**Parity and simplicity of nonzero roots.** Since \(U>0\), the only nonzero roots are zeros of \(H(z)=(z+1)(z+a)^B-c\), where \(0<c=aV/U\le a\). On \((-1,0)\), the product \((z+1)(z+a)^B\) strictly increases from zero to \(a^B\ge a\ge c\); in the equality case \(B=1,U=V=1\), the upper boundary is an extra root at zero, handled as the known complete graph exception. On \((-a,-1)\), the product is negative, hence cannot equal positive \(c\). If \(B\) is even, the product is negative also for \(z<-a\), so there is no root there. If \(B\) is odd, the product is positive on \(( -\infty,-a)\) and strictly decreases from \(+\infty\) to zero as \(z\) increases, giving exactly one root. On \([0,\infty)\), the product is at least \(a^B\) and increases, so there is no positive root (again allowing the stated complete-graph boundary at zero). Finally,
\[
H'(z)=(z+a)^{B-1}\big((B+1)z+a+B\big).
\]
A possible common zero of \(H\) and \(H'\) would be \(z=-a\), where \(H(-a)=-c\ne0\), or \(z=-(a+B)/(B+1)\), which lies strictly in \((-a,-1)\) for \(a>1\), where \(H<0\). Therefore all roots of \(H\) are simple. This proves the real-root census, including both parity cases.

## Verification

A standalone exhaustive verifier (`verify.py`) constructs the graph directly from peripheral clique sizes, enumerates every assignment with each vertex either blank or one of the \(q\) labelled colours, applies the defining local forcing rule until it stops, and compares the resulting exact coefficient vector with the formula above. It checked 16 graph instances with largest peripheral clique orders two, three and four, including unequal clique sizes and complete-graph boundary cases. A total of 1,185,610 labelled partial assignments were classified; every comparison passed. The verifier is a finite consistency check only; the infinite statements follow from the mathematical arguments above. Run using `python3 verify.py` with Python's standard library.

## Relationship to prior work

G. E. Farr, *The forced colouring function of a graph* (2026, arXiv:2609.17108v1), develops the local forcing invariant, supplies formulas for empty and complete graphs and small orders, and proves general properties and hardness. The single-clique special case here is already encompassed by its complete-graph formula. The present theorem instead gives the exact locally forcing assignment polynomial and its real-root census on the entire infinite noncomplete family of heterogeneous clique bouquets. G. E. Farr and K. Morgan, *Graph polynomials: some questions on the edge* (2024, arXiv:2406.15746v1), introduces and motivates related partial-colouring polynomials and their forcing interpretation. Existing complete-multipartite forcing results are for distinct graph structures: a noncomplete clique bouquet with at least two peripheral cliques is not generally complete multipartite. Work on zero forcing of friendship graphs concerns a different update rule, and cannot be used to infer these coefficients or their zeros. Relevant exact family comparisons found no matching general theorem, but exhaustive publication priority is not claimed.

## Limitations

The palette must be exactly the chromatic number \(q=a+1\). All-star bouquets with \(a=1\), globally unique-colourable extensions without local forcing, lists, precoloured graph homomorphisms, and graph classes beyond clique bouquets are outside scope. The finite verifier does not certify every integer tuple; the proof is the source of the unrestricted result. Bibliographic priority beyond inspected sources and published mathematical-record searches remains subject to independent verification. No independent mathematical audit has been performed.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first public September 15, 2026. https://arxiv.org/abs/2609.17108
2. G. E. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1, first public June 22, 2024. https://arxiv.org/abs/2406.15746
3. A. Harary, A. Slany, and O. Verbitsky, *On the Computational Complexity of the Forcing Chromatic Number* (2007), for a different, global uniqueness-based forcing chromatic notion. https://arxiv.org/abs/cs/0406044
