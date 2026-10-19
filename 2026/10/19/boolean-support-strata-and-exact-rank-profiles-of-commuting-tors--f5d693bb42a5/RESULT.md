# Boolean support strata and exact rank profiles of commuting torsion partial permutations

## Finding
Let \(\mathcal I_n\) be the symmetric inverse monoid of all partial bijections on \([n]\), including the empty map. Fix an integer \(r\ge1\) and positive integers \(d_1,\ldots,d_r\). For a tuple \(\mathbf f=(f_1,\ldots,f_r)\), write \(D_i=\operatorname{dom}(f_i)\) and require
\[
f_if_j=f_jf_i\quad(1\le i,j\le r),\qquad f_i^{d_i}=\operatorname{id}_{D_i}\quad(1\le i\le r).
\]
The identity in the second equation is the partial identity on the indicated domain, not the global identity. For each subset \(S\subseteq[r]\), define the **exact support atom**
\[
X_S=\{x\in[n]:\{i:x\in D_i\}=S\}.
\]
For every nonempty \(S\), let \(G_S=\prod_{i\in S}C_{d_i}\), a finite abelian group. The complete exact-support enumerator is
\[
\boxed{\sum_{n\ge0}\frac{x^n}{n!}\sum_{\mathbf f}\prod_{\varnothing\ne S\subseteq[r]}t_S^{|X_S|}
=\exp\!\left(x+\sum_{\varnothing\ne S\subseteq[r]}\ \sum_{H\le G_S}
\frac{(xt_S)^{[G_S:H]}}{[G_S:H]}\right).}
\]
The inner sum runs over **all actual subgroups**, not just subgroup isomorphism types. This is an identity of formal power series over \(\mathbb Q[\mathbf t]\), for every fixed choice of the positive integers \(r,d_1,\ldots,d_r\).

The formula determines simultaneously the ranks of all nonempty products of the commuting elements. For a nonempty \(T\subseteq[r]\), the product \(\prod_{i\in T}f_i\) has domain exactly \(\bigcup_{S\supseteq T}X_S\). In particular, replacing each \(t_S\) by \(\prod_{\varnothing\ne T\subseteq S}z_T\) gives the complete joint rank polynomial of all these products.

For two elements with prescribed powers \(a,b\ge1\), write
\[
F_{n;a,b}(u,v,w)=\sum_{\substack{f,g\in\mathcal I_n\\f^a=\operatorname{id}_{\operatorname{dom}f},\ g^b=\operatorname{id}_{\operatorname{dom}g}\\fg=gf}}u^{\operatorname{rank}f}v^{\operatorname{rank}g}w^{\operatorname{rank}(fg)}.
\]
Define the explicit subgroup-index multiplicity
\[
s_{a,b}(k)=\sum_{\substack{d\mid a,\ e\mid b\\de=k}}\gcd(d,b/e),
\]
interpreted as zero if there is no such pair of divisors. Then
\[
\boxed{\sum_{n\ge0}F_{n;a,b}(u,v,w)\frac{x^n}{n!}
=\exp\!\left(x+\sum_{d\mid a}\frac{(xu)^d}{d}+\sum_{e\mid b}\frac{(xv)^e}{e}
+\sum_{k\mid ab}\frac{s_{a,b}(k)}{k}(xuvw)^k\right).}
\]
This is a finite, explicit prescription for every coefficient of the three-rank distribution for every \(n,a,b\).

## Assumptions and scope
All underlying sets are labeled. Composition is ordinary composition of partial functions; the stated commutation is equality of partial maps, including their domains. A power condition forces the partial map to be a permutation of its domain, rather than allowing chains whose powers eventually vanish. The empty domain is allowed. The integer \(n=0\) is included, with one empty tuple.

The ambient monoid contains all partial bijections, but the enumerated elements satisfy the specified power identities. No count of unrestricted commuting pairs in \(\mathcal I_n\) is asserted. The result concerns ordered tuples, not conjugacy classes, unlabeled objects, or arbitrary nilpotent partial injections.

## Proof
**1. A power identity gives a local permutation.** Suppose a partial injection \(f\) satisfies \(f^d=\operatorname{id}_D\), where \(D=\operatorname{dom}f\) and \(d\ge1\). Every \(x\in D\) has an entire defined \(d\)-step orbit, so \(f(D)\subseteq D\). Injectivity and finiteness imply \(f(D)=D\). Thus \(f\) is a permutation of \(D\), with order dividing \(d\). Conversely, every such permutation, undefined off \(D\), satisfies the displayed power identity.

**2. Intersection invariance is forced by commutation.** Suppose \(f\) and \(g\) are permutations of supports \(A\) and \(B\), respectively, and put \(I=A\cap B\). Since the support is invariant under its permutation,
\[
\operatorname{dom}(f\circ g)=g^{-1}(I),\qquad
\operatorname{dom}(g\circ f)=f^{-1}(I).
\]
If the two partial products are equal, these inverse images are the same subset \(K\). The first is contained in \(B\), the second in \(A\), so \(K\subseteq I\). Each inverse image has size \(|I|\), because \(f\) and \(g\) are permutations of their supports. Consequently \(K=I\), and \(f(I)=g(I)=I\). The restrictions \(f|_I,g|_I\) must commute. Conversely, if \(I\) is invariant under both maps and the two restrictions commute, their products agree on \(I\) and both are undefined outside \(I\); hence the partial maps commute.

**3. Canonical Boolean support decomposition.** Apply step 2 to every pair \(f_i,f_j\). In particular, each \(f_i\) preserves \(D_i\cap D_j\) and its complement within \(D_i\), namely \(D_i\setminus D_j\). Intersecting these invariant sets for all \(j\) shows that \(f_i\) preserves every atom \(X_S\) for which \(i\in S\), and is undefined on atoms with \(i\notin S\). On each nonempty \(X_S\), the restrictions of the \(f_i\) for \(i\in S\) are commuting permutations of orders dividing \(d_i\), hence specify a uniquely determined action of \(G_S\). Conversely, any partition into the atoms together with an independent \(G_S\)-action on each nonempty atom yields the required commuting tuple. Thus this construction is a bijection, including all degenerate empty atoms and trivial cyclic factors.

**4. Count the actions, not only orbit types.** For a finite abelian group \(G\), transitive \(G\)-sets of cardinality \(k\) are the coset sets \(G/H\) with \([G:H]=k\), one type for each actual subgroup \(H\). On a specified labeled \(k\)-element set, the number of actions isomorphic to the given \(G/H\)-action is \(k!/|\operatorname{Aut}_G(G/H)|=k!/k=(k-1)!\), since \(\operatorname{Aut}_G(G/H)\cong G/H\). Dividing by \(k!\) in the exponential generating series gives the connected-orbit term \(x^k/k\) for each \(H\). All \(G\)-sets are disjoint unions of their orbits, so the exponential formula gives \(\exp(\sum_{H\le G}x^{[G:H]}/[G:H])\). The atoms with empty support are singleton unlabeled-action components and contribute \(\exp(x)\). Applying the labeled product construction across the support atoms, with weight \(t_S\) per vertex, yields the first displayed formula. Because all maps preserve the support atoms, the domain of a product indexed by \(T\) is precisely the union of atoms \(X_S\) with \(T\subseteq S\), proving the rank refinement.

**5. Evaluate the two-factor subgroup sums exactly.** Every subgroup of \(C_a\times C_b\) is the image of a unique finite-index lattice \(\Lambda\subseteq\mathbb Z^2\) containing \(a\mathbb Z\times b\mathbb Z\). In the unique Hermite normal form, \(\Lambda\) has basis \((d,0),(c,e)\), with \(d,e\ge1\) and \(0\le c<d\). Its index in \(\mathbb Z^2\) is \(de\). The containment condition is equivalent to \(d\mid a\), \(e\mid b\), and \(d\mid(b/e)c\). For each such divisor pair, exactly \(\gcd(d,b/e)\) residues \(c\pmod d\) satisfy the last condition. This proves the formula for \(s_{a,b}(k)\). In the two-atom specialization, \(X_{\{1\}}\) contributes rank weight \(u\), \(X_{\{2\}}\) contributes \(v\), and \(X_{\{1,2\}}\) contributes \(uvw\) because the common atom is exactly the domain of the product. Substitution yields the second displayed identity.

## Verification
For commuting partial involutions (\(a=b=2\)), the unweighted exponential series specializes to
\[
\sum_{n\ge0}F_{n;2,2}(1,1,1)\frac{x^n}{n!}
=\exp\!\left(4x+\frac52x^2+\frac14x^4\right).
\]
It predicts exactly \(1,4,21,124,817,5844\) ordered pairs for \(n=0,1,2,3,4,5\). For three commuting partial involutions the analogous unweighted series is
\[
\exp\!\left(8x+\frac{19}{2}x^2+\frac52x^4+\frac18x^8\right),
\]
with initial counts \(1,8,83,968\) for \(n=0,1,2,3\).

The standalone standard-library program `checker.py` constructs permitted partial permutations directly, compares partial compositions entry-by-entry, and tabulates the full \((\operatorname{rank}f,\operatorname{rank}g,\operatorname{rank}(fg))\) distribution. Separately, it computes the proposed generating function by exact rational formal-series recurrence; it does not use a support decomposition for the direct enumeration. Complete coefficient tables agree for all degrees \(0\le n\le5\) for the prescribed-power pairs \((1,1),(1,3),(2,2),(2,3)\), and for degrees \(0\le n\le4\) for \((3,3),(2,4)\). A separate subgroup closure routine checks the Hermite-normal-form arithmetic for six pairs of cyclic groups; direct triple enumeration verifies the claimed three-involution totals for \(0\le n\le3\). The checker prints `ALL_EXACT_CHECKS_PASSED` when all tests succeed.

These finite computations are independent tests, not the proof for arbitrary positive integer parameters; the infinite proof is the five-step argument above.

## Relationship to prior work
The 2023 paper by Elliott, Levine, and Mitchell (arXiv:2303.12387, first public March 22, 2023) classifies and counts isomorphism types of monogenic submonoids and inverse submonoids. Its Theorem 1 is an order-spectrum identity rather than a labeled commutation enumeration. That work motivates looking for simultaneous finite-order invariants in symmetric inverse monoids, but its theorem does not give the present support-resolved tuple distribution.

Araújo, Bentz, and Konieczny (arXiv:1205.1664, 2012) give a general commutation criterion for arbitrary partial injections in Proposition 2.2, and study clique numbers, diameters and largest commutative subsemigroups. The present proof specializes commutation to the restricted group-bound element class and counts **all** permitted ordered tuples with their Boolean support sizes by finite-abelian-action orbits. The earlier criterion is acknowledged as a structural predecessor; it is not claimed as new.

The exponential formula for sets of transitive group actions and the subgroup-coset description are standard tools. The assessed contribution is the unified exact joint-rank enumerator for simultaneously commuting prescribed-power elements of the symmetric inverse monoid, together with the explicit two-cyclic-factor subgroup-index arithmetic. No theorem about full unrestricted commuting pairs is implied.

## Limitations
Novelty is established only relative to the sources and mathematical records inspected, not by any comprehensive uniqueness guarantee. A formulation under partial group actions, species of finite abelian group actions, or centralizers could give an equivalent result; this remains a literature risk. The proof is combinatorial and supplies no effective asymptotic estimates beyond the exact coefficient formulas. It does not enumerate tuples containing partial chains or other non-group-bound elements. The verification program exhausts only the stated finite test ranges.

## References
1. L. Elliott, A. Levine, J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (first posted 2023-03-22); Communications in Algebra 51 (2023), 4654–4661. https://arxiv.org/abs/2303.12387
2. J. Araújo, W. Bentz, J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664 (2012); Israel Journal of Mathematics 207 (2015), 103–149. https://arxiv.org/abs/1205.1664
