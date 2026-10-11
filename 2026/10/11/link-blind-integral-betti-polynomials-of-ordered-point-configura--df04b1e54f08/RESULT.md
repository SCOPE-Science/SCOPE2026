# Link-blind integral Betti polynomials of ordered point configurations
## Finding
Let \(L\subset\mathbb R^3\) be a smooth link with \(n\ge1\) components and put \(M_L=\mathbb R^3\setminus L\). For every integer \(k\ge1\), the ordered configuration space
\[
F_k(M_L)=\{(x_1,\ldots,x_k)\in M_L^k:x_i\ne x_j\text{ for }i\ne j\}
\]
has torsion-free integral cohomology and exact Poincaré polynomial
\[
P_{L,k}(t):=\sum_{q\ge0}\operatorname{rank}_{\mathbb Z}H^q(F_k(M_L);\mathbb Z)t^q
=\prod_{j=0}^{k-1}\bigl(1+nt+(n+j)t^2\bigr).
\]
The answer depends only on the number of link components, not on knotting or linking. More sharply, for each \(k\ge1\), the ordered configurations in the complements of an unknot and a trefoil have isomorphic graded integral cohomology groups but are not homotopy equivalent.

For example,
\[
\operatorname{rank}H^1(F_k(M_L);\mathbb Z)=nk,\qquad
\operatorname{rank}H^2(F_k(M_L);\mathbb Z)=nk+(n^2+1)\binom{k}{2},
\]
and the top cohomology in degree \(2k\) has rank \(n(n+1)\cdots(n+k-1)\).

## Assumptions and scope
A link means a smooth embedding of a disjoint union of \(n\) copies of the circle into \(\mathbb R^3\). The point configurations are ordered; no quotient by permutations is taken. The topology is the ordinary subspace topology. Cohomology uses constant integral coefficients and is ordinary singular cohomology. The result concerns the fibers consisting of free marked points in a fixed link complement; it does not calculate cohomology of the total space in which the embedded link itself moves.

For the trivial unlink, the space \(F_k(M_L)\) is the fiber of the mixed-configuration fibration introduced in [1]. The proof below also applies to arbitrary nontrivial knots and links, without asserting an analogue of that particular total-space fibration for knotted moving links.

## Proof
**1. Punctured link-complement cohomology.** For any integer \(s\ge0\) and any \(s\)-point subset \(Q\subset M_L\), identify
\[
M_L\setminus Q=S^3\setminus(L\sqcup Q\sqcup\{\infty\}).
\]
The compact set being removed consists of \(n\) disjoint circles and \(s+1\) isolated points. Integral Alexander duality therefore gives
\[
H^0(M_L\setminus Q;\mathbb Z)=\mathbb Z,\quad
H^1(M_L\setminus Q;\mathbb Z)=\mathbb Z^n,\quad
H^2(M_L\setminus Q;\mathbb Z)=\mathbb Z^{n+s},
\]
with zero higher cohomology. This holds for every knotting and linking pattern. To identify explicit bases relative to punctures, consider the pair \((M_L,M_L\setminus Q)\). Excision and local orientation yield relative cohomology \(\mathbb Z^s\) concentrated in degree \(3\). Since \(H^3(M_L;\mathbb Z)=0\), the long exact sequence gives an isomorphism in degree \(1\) and a split short exact sequence
\[
0\longrightarrow H^2(M_L;\mathbb Z)
\longrightarrow H^2(M_L\setminus Q;\mathbb Z)
\longrightarrow\mathbb Z^s\longrightarrow0.
\]
The last map evaluates cohomology on positively oriented small spheres surrounding the \(s\) missing points. In particular, an integral basis of \(H^2(M_L)\), together with \(s\) classes having Kronecker evaluations the standard basis in \(\mathbb Z^s\), forms a basis for the punctured complement.

**2. Global classes in the forgetting fibration.** For \(k\ge2\), forgetting the last point is the Fadell–Neuwirth locally trivial fibration
\[
F_k(M_L)\longrightarrow F_{k-1}(M_L),
\]
whose fiber above \((x_1,\ldots,x_{k-1})\) is \(M_L\setminus\{x_1,\ldots,x_{k-1}\}\). Choose integral bases of \(H^1(M_L)\) and \(H^2(M_L)\) and pull them back to \(F_k(M_L)\) along the coordinate map \((x_1,\ldots,x_k)\mapsto x_k\). For each \(1\le i<k\), the globally defined Gauss map
\[
g_{ik}:F_k(M_L)\longrightarrow S^2,\qquad
g_{ik}(x_1,\ldots,x_k)=\frac{x_k-x_i}{\|x_k-x_i\|}
\]
provides the integral degree-two class \(g_{ik}^*[S^2]^*\), with \([S^2]^*\) the positive generator of \(H^2(S^2;\mathbb Z)\).

On every fiber the pulled-back degree-one classes are a basis for \(H^1\). The pulled-back degree-two classes from \(M_L\) and the \(k-1\) Gauss classes are a basis for \(H^2\): the Gauss map \(g_{ik}\) has degree \(+1\) on a small sphere about the missing point \(x_i\), and degree \(0\) on the small spheres about the other missing points. The classes from \(H^2(M_L)\) evaluate to zero on all such spheres and are a primitive direct summand by the preceding short exact sequence. Together with the unit, the global classes thus restrict to an integral cohomology basis on every fiber.

**3. Integral Leray–Hirsch and induction.** Since the cohomology of each fiber is concentrated in degrees \(0,1,2\), is free of finite rank, and has the global fiberwise basis just constructed, the integral Leray–Hirsch theorem provides a graded additive isomorphism
\[
H^*(F_k(M_L);\mathbb Z)
\cong H^*(F_{k-1}(M_L);\mathbb Z)\otimes_{\mathbb Z}
\bigl(\mathbb Z[0]\oplus\mathbb Z^n[-1]\oplus\mathbb Z^{n+k-1}[-2]\bigr),
\]
where the bracket notation specifies the cohomological degrees of the additive summands, not a graded ring structure. Thus integral torsion does not appear and
\[
P_{L,k}(t)=P_{L,k-1}(t)\bigl(1+nt+(n+k-1)t^2\bigr).
\]
For \(k=1\), Alexander duality gives \(P_{L,1}(t)=1+nt+nt^2\). Induction gives the displayed product for every integer \(k\ge1\).

**4. Homotopy distinction despite identical Betti polynomials.** The inclusion \(F_k(M_L)\hookrightarrow M_L^k\) is an isomorphism on fundamental groups: the omitted pairwise diagonals have real codimension \(3\), so by general position all loops and all homotopies between loops can be chosen to avoid them. Hence
\[
\pi_1(F_k(M_L))\cong\pi_1(M_L)^k.
\]
For the unknot complement \(\pi_1(M_L)\cong\mathbb Z\); for the trefoil complement the standard presentation \(\langle a,b\mid a^2=b^3\rangle\) has a surjection onto the nonabelian group \(S_3\) by sending \(a\) to a transposition and \(b\) to a three-cycle. Therefore the trefoil group and each of its positive direct powers are nonabelian, while \(\mathbb Z^k\) is abelian. These two families cannot be homotopy equivalent for any \(k\ge1\), although the proved Betti polynomial is identical for both families because both links have one component.

## Verification
The proof is entirely symbolic and works uniformly for all smooth links and all positive integers \(k\). The critical cohomological calculation is integral Alexander duality applied to the \(n\) link circles plus the \(s+1\) point components, not the different Alexander-duality calculation in \(S^3\setminus L\) that omits the point at infinity. The split short exact sequence follows from local cohomology of the deleted points; the Gauss-map degree matrix is the identity on the small puncture spheres. All Leray–Hirsch hypotheses have been checked using the global classes.

As consistency checks, for \(n=1\) and \(k=1\) the polynomial is \(1+t+t^2\), and for \(n=1\) and \(k=2\) it is \(1+2t+4t^2+3t^3+2t^4\). These finite expansions are checks, not the proof of the universal statement. The theorem makes no claim of isomorphism of cohomology rings, nor does it compute unordered configurations, mixed-total-space cohomology, or homotopy groups above degree one.

## Relationship to prior work
Makri [1, Theorem 3.2] introduces mixed configurations of circles and marked points and identifies the fixed-link fiber as \(F_k(\mathbb R^3\setminus L)\) for the trivial unlink. Her Lemma 3.4 and Proposition 3.8 concern fundamental groups and the mixed-space extension, not the integral Betti polynomial. The present statement addresses integral additive cohomology of those ordered fibers and, beyond the source's trivial links, all smooth links.

Bödigheimer–Cohen–Taylor [2, Theorems A–C and Example 5.2] analyze the homology of **unordered** point configurations, including mod-two examples for knot complements. Their knot-complement example lists mod-two Betti numbers for small unordered configurations; it is neither an integral ordered-cohomology calculation nor an all-\(k\) ordered product formula. Knudsen [3] provides rational homology results for unordered configurations of general manifolds. These results are important related coverage, not assertions of the integral ordered statement above. The Fadell–Neuwirth fibration [4] supplies a classical tool used here.

## Limitations
The isomorphism of graded integral abelian groups is noncanonical and does not assert an isomorphism of cup-product rings or an equivalence of configuration spaces. A braid or link can still be detected by stronger invariants. The proof assumes smooth links (not arbitrary wild embeddings), ordered points, and the Euclidean three-space complement including the point at infinity in its compactification. The classification of knots by fundamental group is not claimed.

## References
1. S. Makri, “Mixed configuration spaces, fixed points and Loop braid groups,” arXiv:2610.04382v1 (first public 2026-10-03), particularly Theorem 3.2, Lemma 3.4 and Proposition 3.8. https://arxiv.org/html/2610.04382v1
2. C.-F. Bödigheimer, F. Cohen and L. Taylor, “On the homology of configuration spaces,” *Topology* 28 (1989), 111–123, Theorems A–C and Example 5.2. doi:10.1016/0040-9383(89)90035-9. Author-hosted full text: https://www.math.uni-bonn.de/people/cfb/PUBLICATIONS/on-the-homology-of-configuration-spaces.pdf
3. B. Knudsen, “Betti numbers and stability for configuration spaces via factorization homology,” *Algebraic & Geometric Topology* 17 (2017), 3137–3187. arXiv:1405.6696.
4. E. Fadell and L. Neuwirth, “Configuration spaces,” *Mathematica Scandinavica* 10 (1962), 111–118.
