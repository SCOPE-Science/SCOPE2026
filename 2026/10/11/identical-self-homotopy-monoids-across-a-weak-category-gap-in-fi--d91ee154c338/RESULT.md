# Identical self-homotopy monoids across a weak-category gap in finite spaces

## Finding
Let \(D_m\) be the discrete poset on \(m\) points, let \(R=P(9)\) be the nine-point weakly contractible noncontractible finite space of Cianci and Ottina in the explicit presentation of Mosquera-Lois and Tanaka, and take the ordinal sums
\[
X_m=R\oplus D_m,\qquad B_m=D_2\oplus D_m,\qquad m\ge2.
\]
Write \(\operatorname{End}_h(Y)=[Y,Y]\) for the monoid of unbased finite-space homotopy classes of order-preserving selfmaps, with composition. For \(m\ge2\), let \(T_m\) be the full transformation monoid of \([m]=\{1,\ldots,m\}\), and let \(T_m^{\mathrm{nc}}\) be its set of nonconstant transformations. Define a monoid \(M_m\) consisting of a zero and pairs \((\varepsilon,\sigma)\in C_2\times T_m^{\mathrm{nc}}\), with multiplication
\[
(\varepsilon,\sigma)(\eta,\tau)=
\begin{cases}
(\varepsilon\eta,\sigma\circ\tau),&\sigma\circ\tau\text{ is nonconstant},\\
0,&\sigma\circ\tau\text{ is constant},
\end{cases}
\]
and an absorbing zero. Then
\[
\boxed{\operatorname{End}_h(X_m)\cong M_m\cong\operatorname{End}_h(B_m),\quad
|M_m|=1+2(m^m-m).}
\]
Nevertheless their unreduced weak/stable/ordinary Lusternik–Schnirelmann categories are different:
\[
(\operatorname{cat}_w,\operatorname{cat}_s,\operatorname{cat})(X_m)=(1,2,m),\qquad
(\operatorname{cat}_w,\operatorname{cat}_s,\operatorname{cat})(B_m)=(2,2,m).
\]
Indeed, \(X_m\) is weakly contractible and \(H_1(B_m;\mathbb Z)\cong\mathbb Z^{m-1}\). Thus the full self-homotopy *monoid*, not merely its cardinality, fails to determine weak category or even weak contractibility for these connected finite spaces.

## Assumptions and scope
Finite \(T_0\)-spaces are identified with posets, with lower-set topology. A continuous map is an order-preserving map, and two maps are homotopic if and only if they lie in the same connected component of the finite poset of maps under pointwise comparison. The ordinal sum \(Q\oplus D_m\) keeps the orders on its summands and declares every point of \(Q\) smaller than every point of \(D_m\). All homotopies and endomorphisms are unbased. The category convention is unreduced; the ordinal-sum families are considered only for integers \(m\ge2\).

The nine vertices of \(R\), ordered for the verification algorithm as \(c_0,c_1,c_2,p,q,y,g,h,k\), have precisely the covering relations
\[
\begin{gathered}
c_0<p,y;\quad c_1<p,q,y;\quad c_2<q,y;\\
p<g,h;\quad q<g,k;\quad y<h,k.
\end{gathered}
\]
Their transitive closure defines the whole order. The other base \(D_2\) has two incomparable points. Both bases have no greatest element and each has exactly two order automorphisms, forming \(C_2\).

## Proof
**A cap lemma.** Let \(Q\) be a nonempty finite poset with no greatest element, such that (i) every nonautomorphism selfmap of \(Q\) is homotopic in \(Q\) to a constant map; and (ii) every automorphism of \(Q\) is isolated in the pointwise selfmap poset. For any \(m\ge2\), the endomorphism monoid of \(Y=Q\oplus D_m\) consists of one nullhomotopy class and one isolated class for each pair \((\alpha,\sigma)\) where \(\alpha\in\operatorname{Aut}(Q)\) and \(\sigma:[m]\to[m]\) is nonconstant, with precisely the composition law obtained by sending pairs with constant composite \(\sigma\circ\tau\) to zero.

To prove the lemma, let \(f:Y\to Y\) be order-preserving, and write \(z_1,\ldots,z_m\) for the new maxima. If \(f(Q)\) contains a new maximum \(z_i\), then \(f(z_j)=z_i\) for every \(j\), because every old vertex lies below every new maximum. Thus \(f\le c_{z_i}\) pointwise, and \(f\) is nullhomotopic.

Otherwise \(f(Q)\subseteq Q\). For each new maximum \(z_j\) with \(f(z_j)\in Q\), raise its image to a chosen new maximum; if \(f(z_j)\) is already a new maximum, retain that image. These changes are pointwise increases, preserve all order relations because \(f(Q)\subseteq Q\), and fix \(f|_Q\). Thus \(f\) is homotopic to a map \(f'\) that maps every new maximum among the new maxima. If \(f'|_Q\) is a nonautomorphism, its homotopy to a constant in \(Q\) extends over \(Y\) with the images of all new maxima fixed. The resulting map, constant with value \(q\in Q\) on \(Q\), is pointwise above the constant map \(c_q\) on \(Y\), so is nullhomotopic. If \(f'|_Q=\alpha\) is an automorphism but all new maxima have the same image \(z_i\), then \(f'\le c_{z_i}\), so it too is nullhomotopic.

It remains to examine a map \(F_{\alpha,\sigma}\) restricting to an automorphism \(\alpha\) on \(Q\) and having nonconstant images \(F(z_j)=z_{\sigma(j)}\). Such a map is an isolated point of \(\operatorname{Map}(Y,Y)\). Indeed, if \(G\ge F\), maximality fixes all new-maximum images of \(G\) to those of \(F\). Because \(\sigma\) takes at least two different values, an image \(G(q)\) of an old point must lie below two different new maxima, hence lies in \(Q\). Therefore \(G|_Q\ge\alpha\), which forces equality by isolation of \(\alpha\), and consequently \(G=F\). If \(G\le F\), then \(G(Q)\subseteq Q\) and \(G|_Q\le\alpha\), again forcing equality. Every \(G(z_j)\) is then a common upper bound of all points of \(Q=\alpha(Q)\). Since \(Q\) has no greatest point, it must be one of the new maxima; the inequality \(G(z_j)\le z_{\sigma(j)}\) forces equality. Thus also \(G=F\). Distinct such maps give distinct singleton homotopy components, while all remaining maps are nullhomotopic and belong to one component because \(Y\) is connected. Composition sends \(F_{\alpha,\sigma}F_{\beta,\tau}\) to \(F_{\alpha\beta,\sigma\circ\tau}\) if the apex composite is nonconstant and to a null map otherwise. This proves the lemma.

**The two bases satisfy the lemma.** For \(Q=D_2\), the two order automorphisms are its two permutations, each isolated, and the two other selfmaps are constant. For \(Q=R\), the displayed Hasse relations show that \(y\) is the unique middle point above all three minima, \(c_1\) is the unique minimum below all three middle points, and \(g\) is the unique maximum not above \(y\). An automorphism can therefore only exchange \(c_0\leftrightarrow c_2\), \(p\leftrightarrow q\), and \(h\leftrightarrow k\) simultaneously or fix every point. Both are indeed automorphisms. Exhaustive enumeration of all \(12{,}575\) isotone selfmaps of \(R\), with comparability components reconstructed from all valid one-coordinate changes, yields exactly three components: one of size \(12{,}573\) containing the constant maps, and the two singleton automorphisms. This verifies both hypotheses for \(R\). The standalone `verify.py` checks the complete enumeration and, independently, the \(m=2\) cap, which has \(232{,}727\) selfmaps in components of sizes \(232{,}723,1,1,1,1\). No finite computation is used to justify the cap lemma's quantification over all \(m\).

Both automorphism groups are \(C_2\), so applying the lemma to each base gives the claimed identical monoid \(M_m\). There are \(m^m\) total selfmaps of \([m]\), of which exactly \(m\) are constant; each nonconstant one is paired with two base automorphisms. The unit group is \(C_2\times S_m\), but the monoid also retains noninvertible transformation classes when \(m\ge3\).

Finally, Mosquera-Lois and Tanaka compute the category triple of \(R\oplus D_m\) as \((1,2,m)\) (Corollary 4.2) and that of \(D_2\oplus D_m\) as \((2,2,m)\) (Proposition 5.2). Their first family is weakly contractible. The order complex of the second is the complete bipartite graph \(K_{2,m}\), whose first integral homology has rank \(m-1\). This proves the topological separation despite monoid equality.

## Verification
The included `verify.py` requires only the Python standard library. Its \(R\) enumeration uses the transitive closure of the thirteen displayed covers, enumerates every isotone map by assigning images in a linear extension, and connects two maps whenever they differ at one coordinate by comparable values while remaining isotone. These elementary edges recover all components: if \(f\le g\), increasing images from maximal domain elements downwards supplies a chain of valid one-coordinate comparisons from \(f\) to \(g\). Its output is:

```text
P9: maps=12575, components=3, component_sizes=[12573, 1, 1], isolated=2
P9+D2: maps=232727, components=5, component_sizes=[232723, 1, 1, 1, 1], isolated=4
abstract_monoid(m=2): size=5, units=4, associative=YES
abstract_monoid(m=3): size=49, units=12, associative=YES
VERIFY_OK
```

Run `python3 verify.py` in a directory containing the extracted script. The \(m=2\) cap enumeration and the small explicit monoid tables are cross-checks; the all-\(m\) statement follows from the preceding cap lemma.

## Relationship to prior work
Mosquera-Lois and Tanaka (arXiv:2609.39615v1, first public 2026-09-30) introduce and compute the two category triples and describe the nine-point order and the height-one comparison family. Their work does not compute the capped families' homotopy endomorphism monoids or assert the coincidence across different weak category. Two other published finite-space calculations respectively give the three selfmap homotopy classes of the *uncapped* nine-point space, and the numerical formula \(1+2(m^m-m)\) for the height-one comparison family. Those computations support the contrast but do not cover the capped nine-point endomorphism monoid, the cap lemma, or the composition-preserving cross-family isomorphism established here.

## Limitations
The conclusion concerns \(\pi_0\) of the selfmapping space with composition, not the homotopy type of the entire selfmapping space. It does not assert that \(X_m\) and \(B_m\) are weakly or ordinarily homotopy equivalent; the computed integral first homology rules out weak equivalence. The finite enumeration verifies the specific nine-point base and \(m=2\); the symbolic argument is essential for all \(m\ge2\). An analogous coincidence for other bases is not claimed.

## References
1. D. Mosquera-Lois and K. Tanaka, *Weak, stable, and ordinary Lusternik–Schnirelmann category of finite spaces*, arXiv:2609.39615v1 (2026-09-30), primary MSC 55M30, Theorem 1.1, Lemma 4.1, Corollary 4.2, and Proposition 5.2. https://arxiv.org/html/2609.39615v1
2. *Three self-homotopy classes on the minimal nine-point weakly contractible finite space*, published mathematical record `2026/10/4/SCOPE-three-self-homotopy-classes-on-the-minimal-nine-point-weakly-con--b3c00d24be81` (the uncapped base).
3. *Exact self-homotopy classes of complete height-two finite bouquet models*, published mathematical record `2026/10/4/SCOPE-exact-self-homotopy-classes-of-complete-height-two-finite-bouque--6eb4a5c941d8` (the height-one base family).
