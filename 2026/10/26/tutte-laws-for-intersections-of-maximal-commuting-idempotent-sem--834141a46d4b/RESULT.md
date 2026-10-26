# Tutte laws for intersections of maximal commuting idempotent semilattices of incidence monoids

## Finding
Let \(P\) be a nonempty finite poset with \(n\) points and \(m\) strict comparable pairs; let \(q\) be any prime power. In its incidence algebra \(A=I(P,\mathbb F_q)\), write \(J\) for the strictly upper-interval ideal, \(U=1+J\), and \(D\) for the Boolean multiplicative semilattice of diagonal idempotents. The **maximal commutative idempotent subsemigroups** of the multiplicative monoid of \(A\) are precisely
\[
S_u=uDu^{-1}\quad(u\in U),
\]
with different \(u\) giving different subsemigroups. There are exactly \(q^m\) of them; each has \(2^n\) elements.

Let \(G\) be the undirected *comparability graph* of \(P\), with one edge for every strict comparable pair. For \(g\in U\), let \(H_g\subseteq G\) be the spanning subgraph with edge \(\{x,y\}\) when the interval coordinate \(g(x,y)\ne0\). If \(c(H_g)\) denotes its number of connected components, including isolates, then
\[
|S_u\cap S_v|=2^{c(H_{u^{-1}v})}.
\]
For independently uniformly chosen maximal semilattices \(S,T\), the exact probability-generating polynomial of \(\log_2|S\cap T|\) is
\[
F_{P,q}(t):=\mathbb E[t^{\log_2|S\cap T|}]
=q^{-m}\sum_{B\subseteq E(G)}(q-1)^{|B|}t^{c(B)}
=q^{-m}t^{c(G)}(q-1)^{n-c(G)}T_G\!\left(1+\frac{t}{q-1},q\right),
\]
where \(T_G\) is the ordinary graph Tutte polynomial, and \(c(B)\) counts spanning-subgraph components. Consequently, precisely
\[
q^m\sum_{B\subseteq E(G):\,c(B)=j}(q-1)^{|B|}
\]
ordered pairs of maximal semilattices have intersection cardinality \(2^j\).

For a fixed \(n\), the family \(\{F_{P,q}:q\text{ a prime power}\}\) determines \(T_G\) (and conversely the Tutte polynomial determines all such distributions). If \(G\) is connected and \(n\ge2\), let \(\lambda\) be its edge connectivity and \(b_\lambda\) its number of minimum cuts. Then, as prime powers \(q\to\infty\),
\[
\Pr(|S\cap T|>2)=b_\lambda q^{-\lambda}+O_G(q^{-\lambda-1}).
\]
Thus intersections of compatible retraction systems encode both the full Tutte polynomial and the sharp minimum-cut rarity exponent of the original comparability graph.

## Assumptions and scope
An incidence-algebra element is a function on intervals \((x,y)\), \(x\le y\); its convolution product is \((fg)(x,y)=\sum_{x\le z\le y}f(x,z)g(z,y)\). A diagonal element has no strict-interval entries. A commutative idempotent subsemigroup means a subset closed under multiplication whose members square to themselves and commute pairwise; maximality is by inclusion among such subsets (not among all commutative subsemigroups). Multiplicative identity and zero lie in every maximal subset. A strict comparable pair includes every \(x<y\), not only Hasse covers. No bound on poset height or finite-field characteristic is required. The empty poset is excluded only to keep the statement nondegenerate.

## Proof
**Simultaneous diagonalization within the incidence algebra.** Consider an arbitrary finite set of pairwise commuting idempotents \(e_1,\ldots,e_k\in A\). For each bit vector \(\sigma\in\{0,1\}^k\), set \(p_\sigma=\prod_{i=1}^k e_i^{\sigma_i}(1-e_i)^{1-\sigma_i}\), with the notation denoting a choice of \(e_i\) or \(1-e_i\), not a division operation. The \(p_\sigma\) are pairwise orthogonal idempotents and sum to \(1\). Let \(d_\sigma\) be their diagonal parts. A diagonal entry of an idempotent is zero or one, so the \(d_\sigma\) form an orthogonal diagonal partition of unity. Define \(u=\sum_\sigma p_\sigma d_\sigma\). Its diagonal is \(1\), hence \(u\in U\) is invertible (the ideal \(J\) is nilpotent). Orthogonality gives \(p_\sigma u=u d_\sigma\), and summing over \(\sigma\) with \(\sigma_i=1\) yields \(e_i=u\operatorname{diag}(e_i)u^{-1}\). This proof works over every characteristic, without choosing eigenvectors.

**Maximality and uniqueness.** The simultaneous reduction puts every commutative idempotent subsemigroup inside some conjugate \(S_u\). Every idempotent commuting with every diagonal idempotent is itself diagonal, since the \((x,y)\)-entry of its commutator with the diagonal primitive idempotent at \(x\) detects every off-diagonal coordinate. Hence each \(S_u\) is maximal. Suppose \(S_u=S_v\), and put \(g=u^{-1}v\in U\). Since \(gDg^{-1}=D\), taking diagonals shows \(\operatorname{diag}(g d g^{-1})=d\) for \(d\in D\), because \(g\) has diagonal \(1\). But a diagonal member of \(D\) is determined by its diagonal; therefore \(gd=dg\) for every \(d\in D\), forcing \(g=1\). Thus \(u=v\). The \(m\) strict interval coordinates of \(U=1+J\) are arbitrary field elements, whence \(|U|=q^m\).

**Intersection support lemma.** Conjugation reduces \(S_u\cap S_v\) to \(D\cap gDg^{-1}\), with \(g=u^{-1}v\). If \(d\in D\), then \(g^{-1}dg\in D\) iff it has the same diagonal \(d\), equivalently \(gd=dg\). On a strict interval \(x<y\), this condition is exactly \(g(x,y)[d(y,y)-d(x,x)]=0\). Each diagonal bit is therefore constant precisely on connected components of \(H_g\); independently assigning a bit to each component gives \(2^{c(H_g)}\) intersection elements and a Boolean semilattice on the components.

**Exact counting and graph-polynomial identification.** The free and transitive \(U\)-parametrization makes \(u^{-1}v\) uniform in \(U\) when \(u,v\) are independent uniform. The \(m\) strict-interval coordinates are independent uniform \(\mathbb F_q\), so each comparability edge belongs to \(H_g\) with probability \((q-1)/q\), independently of all other edges. For an exact edge set \(B\), its probability is \(q^{-m}(q-1)^{|B|}\). Summing by component count gives the displayed generating polynomial and ordered-pair enumeration. The last identity is the standard Fortuin–Kasteleyn/Tutte identity \(\sum_B t^{c(B)}v^{|B|}=t^{c(G)}v^{n-c(G)}T_G(1+t/v,1+v)\), with \(v=q-1\).

**Reconstruction and min-cut law.** Multiplying \(F_{P,q}(t)\) by \(q^m\) and regarding \(q-1\) as an indeterminate recovers the coefficients \(\sum_{B:c(B)=j}(q-1)^{|B|}\) by polynomial interpolation from infinitely many prime powers. The maximum-degree term determines \(m\), and \(n\) is recovered from the top exponent of \(t\); the preceding random-cluster identity then recovers \(T_G\). Conversely the identity determines each law from \(T_G\). For connected \(G\), having \(c(H_g)>1\) requires deletion of an edge cut of size at least \(\lambda\). Each of the \(b_\lambda\) distinct minimum cuts is absent with probability \(q^{-\lambda}\). Intersections of distinct minimum-cut deletion events require at least \(\lambda+1\) absent edges; all larger cut events have probability \(O_G(q^{-\lambda-1})\). Inclusion–exclusion gives the sharp asymptotic. No claim is made that the statistic distinguishes distinct orientations of the same comparability graph.

## Verification
The supplied standalone `verify.py` constructs incidence-algebra multiplication explicitly over prime fields, enumerates every idempotent and unipotent unit in six small instances, checks all conjugate diagonal semilattices for maximality, checks their pairwise-intersection histograms against an independent spanning-subgraph enumeration, and independently enumerates all maximal cliques of pairwise commuting idempotents in four small cases. Its execution produced `VERIFY_OK`. Examples: for a three-element V poset over \(\mathbb F_2\), the intersection-cardinality histogram relative to one fixed maximal semilattice is \(\{2:1,4:2,8:1\}\); for a three-element chain it is \(\{2:4,4:3,8:1\}\). These are finite corroborations rather than a substitute for the proof.

## Relationship to prior work
Can, Casimiro and Malheiro (arXiv:2208.01073v1) establish structure and individual-idempotent orbit information for incidence monoids, including conjugacy descriptions by diagonal patterns. Can (arXiv:2105.09826v1) studies incidence-monoid automorphisms and complexity. Gargate and Gargate (arXiv:2009.04243v1) enumerate individual potent elements of incidence algebras over finite fields. The classical Fortuin–Kasteleyn identity supplies the graph-polynomial conversion. These inputs cover individual idempotents or the graph identity; they do not, in the inspected material, give the pairwise intersection distributions of maximal commuting idempotent subsemilattices or the edge-connectivity asymptotic. The new claim is their incidence-monoid interaction census, not the existence of diagonal idempotents or the Tutte identity alone.

## Limitations
This theorem concerns maximal all-idempotent *commutative* subsemigroups and does not classify maximal general commutative subsemigroups. The distribution depends on the comparability graph, not its orientation: an oriented V-shaped three-point poset and its order dual have identical spectra. The asymptotic is for fixed connected comparability graph and increasing prime power, not for growing posets. A more general theorem on intersections of conjugate diagonal Boolean algebras in incidence algebras might imply portions of the statement; exhaustive bibliographic priority is not asserted. Independent external mathematical audit has not been performed.

## References
1. M. B. Can, E. Casimiro and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073v1 (first public 2022-08-01), https://arxiv.org/abs/2208.01073.
2. M. B. Can, *Incidence Monoids: Automorphisms and Complexity*, arXiv:2105.09826v1 (2021), https://arxiv.org/abs/2105.09826.
3. R. Gargate and M. Gargate, *(k+1)-potent Matrices in Triangular Matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243v1 (2020), https://arxiv.org/abs/2009.04243.
4. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, in *Surveys in Combinatorics* (2005), arXiv:math/0503607.
