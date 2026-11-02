# Automorphism groups of star-graph evolution algebras over odd finite fields

## Finding

Let \(k=\mathbb F_q\) be any field of odd order \(q=p^f\), and let \(m\geq3\). Define the evolution algebra \(E_m=k a\oplus W\) with basis \(a,b_1,\ldots,b_m\) and products \(a^2=s:=\sum_{i=1}^m b_i\), \(b_i^2=a\), and products between distinct basis elements zero. Let \(B\) be the standard dot product on \(W=\langle b_1,\ldots,b_m\rangle\). This is the evolution algebra of the unweighted star graph \(K_{1,m}\).

The full automorphism group, not merely its graph-permutation or diagonal subgroup, is
\[
\operatorname{Aut}_k(E_m)=\{(u,g):u\in k^\times,\ g\in\mathrm{GL}(W),\ B(gv,gw)=uB(v,w)\ (\forall v,w),\quad g(s)=u^2s\}.
\]
The pair acts by \(a\mapsto ua\) and \(v\mapsto gv\), and composition is componentwise.

Write \(O_d^{\epsilon}(q)\) for the full orthogonal group of a nondegenerate quadratic space of even dimension \(d\) and sign \(\epsilon\in\{+1,-1\}\), and \(O_d(q)\) for odd dimension. Their orders (with \(r\ge0\) in the odd-dimensional expression and \(r\ge1\) in the even-dimensional expression, and with empty products equal to one) are
\[
|O_{2r+1}(q)|=2q^{r^2}\prod_{i=1}^{r}(q^{2i}-1),\qquad
|O_{2r}^{\epsilon}(q)|=2q^{r(r-1)}(q^r-\epsilon)\prod_{i=1}^{r-1}(q^{2i}-1).
\]
Let \(\chi\) denote the quadratic character of \(k^\times\).

**Nonresonant case \(p\nmid m\).** Put \(H=s^\perp\), a nondegenerate space of dimension \(d=m-1\). There is an explicit group isomorphism
\[
\operatorname{Aut}_k(E_m)\cong\mu_3(k)\times O(H),
\qquad |\operatorname{Aut}_k(E_m)|=\gcd(3,q-1)|O(H)|.
\]
For even \(d=2r\), the orthogonal sign is \(\epsilon=\chi((-1)^r m)\); the odd-dimensional order is independent of the discriminant.

**Resonant case \(p\mid m\).** Put \(d=m-2\), and let \(U\) be any nondegenerate complement of a hyperbolic plane through \(s\) in \(W\). Then \(\dim U=d\) and its determinant has square class \(-1\). The group has an explicit \(q^d\)-parameter parabolic description; in particular,
\[
|\operatorname{Aut}_k(E_m)|=q^d\,\tau_{q,m}\,|O(U)|,\qquad
\tau_{q,m}=\begin{cases}q-1,&m\text{ even},\\(q-1)/2,&m\text{ odd}.\end{cases}
\]
For even \(d=2r\), the sign is \(\epsilon=\chi((-1)^{r+1})\). The displayed orthogonal-order formulas therefore evaluate both cases without any unspecified group cardinalities. These two regimes expose a genuine characteristic-divisibility jump.

For instance, over \(\mathbb F_5\) with \(m=3\), the full group has \(12\) elements, strictly more than the \(6\) star-graph permutations. Over \(\mathbb F_3\) with \(m=3\), it has \(6\) elements, whereas over \(\mathbb F_9\) it has \(72\).

## Assumptions and scope

All vector spaces and algebra automorphisms are \(k\)-linear. The graph is the labeled simple star \(K_{1,m}\), and its attached algebra uses its adjacency matrix as structure matrix (not a stochastic transition matrix). The characteristic is odd, \(m\ge3\), and \(q\) can be any odd prime power. The symbol \(m\) is regarded as an element of \(k\) wherever it appears in a norm calculation. No identification of distinct field characteristics is implicit.

## Proof

**Intrinsic recovery of the center vertex and leaf space.** Every product in \(E_m\) belongs to \(D=E_m^2=ka\oplus ks\). The annihilator of \(D\) is exactly \(s^\perp\subset W\): multiplication by \(a\) forces the \(a\)-coordinate to vanish, while multiplication by \(s\) imposes \(B(w,s)=0\). The restriction of \(B\) to \(s^\perp\) is nonzero for \(m\ge3\): if \(p\nmid m\) it has rank \(m-1\), and if \(p\mid m\) it has rank \(m-2\). Consequently, \((\operatorname{Ann}(D))^2=ka\), an intrinsically defined one-dimensional subspace. Every automorphism therefore sends \(a\) to \(ua\) for a unique \(u\in k^\times\). Since \(\operatorname{Ann}(a)=W\), it preserves \(W\) and acts there by some \(g\in\operatorname{GL}(W)\). Preservation of \(a^2=s\) gives \(gs=u^2s\), and preservation of \(vw=B(v,w)a\) gives \(B(gv,gw)=uB(v,w)\) for every \(v,w\in W\). Conversely these two relations preserve every product and define an invertible algebra endomorphism, proving the first assertion.

**When \(p\nmid m\).** The vector \(s\) has norm \(B(s,s)=m\ne0\), and \(W=ks\perp H\) with \(H=s^\perp\) nondegenerate. Comparing the norm of \(gs=u^2s\) with its multiplier \(u\) forces \(u^4m=um\), hence \(u^3=1\). The restriction \(g|_H\) preserves \(H\); setting \(h=u^{-2}g|_H\) gives \(B(hv,hw)=u^{-3}B(v,w)=B(v,w)\). Thus \(h\in O(H)\). Conversely, given \(u\in\mu_3(k)\) and \(h\in O(H)\), define \(g(s)=u^2s\), \(g|_H=u^2h\). This is an isomorphism of groups because scalar maps commute with \(O(H)\). In a basis \((s,h_1,\ldots,h_d)\), determinants give \(\det H\equiv1/m\) modulo squares, so for even \(d=2r\), the split/nonsplit sign is \(\chi((-1)^r/m)=\chi((-1)^rm)\).

**When \(p\mid m\).** The nonzero vector \(s\) is isotropic. Since the characteristic is odd and \(B\) is nondegenerate, extend \(s\) to a hyperbolic pair \((s,t)\) with \(B(s,t)=1\) and \(B(t,t)=0\), and put \(U=(ks+kt)^\perp\). Then \(W=ks\oplus U\oplus kt\), the Gram determinant of the hyperbolic plane is \(-1\), and \(\det U\equiv-1\) modulo squares. For each multiplier \(u\in k^\times\), each vector \(y\in U\), and each \(h\in GO(U)\) with similarity multiplier \(u\), put
\[
\begin{aligned}
g(s)&=u^2s,\\
g(t)&=u^{-1}t+y-\frac{u}{2}B(y,y)s,\\
g(z)&=h(z)-u B(h(z),y)s\quad(z\in U).
\end{aligned}
\]
Direct pairings on \(s,t,U\) give \(B(gv,gw)=uB(v,w)\), and the map fixes the required line and scale of \(s\). Conversely any such \(g\) uniquely has this form: its coefficient of \(t\) in \(g(t)\) is forced to be \(u^{-1}\), its \(U\)-component gives \(y\), its \(s\)-component follows from \(B(g(t),g(t))=0\), and orthogonality determines \(g(z)\). There are \(q^d\) choices of \(y\) for each \((u,h)\). For nondegenerate quadratic spaces over odd finite fields, the multiplier map \(GO(U)\to k^\times\) is surjective if \(d\) is even; if \(d\) is odd, its image is precisely the squares (necessity follows by taking determinants, sufficiency from scalar similarities). Every nonempty fibre has size \(|O(U)|\). This gives \(\tau_{q,m}=q-1\) when \(m\) is even, and \((q-1)/2\) when \(m\) is odd. The discriminant relation gives the stated even-dimensional sign. Applying the standard finite orthogonal group orders completes the count.

**Boundary checks.** The proof of recovering \(ka\) uses \(m\ge3\) essentially; nothing is claimed for \(m=1\) or \(m=2\). All arguments invoke division by \(2\) only in the stated odd characteristic. The integer-divisibility distinction \(p\mid m\) includes extension fields \(\mathbb F_{p^f}\), not merely prime fields.

## Verification

The enclosed standalone `verify.py` enumerates all candidates \((u,g)\) satisfying the original full multiplication equations over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\) when \(m=3\), and \(\mathbb F_3\) when \(m=4\). The finite-extension case uses an explicit representation \(\mathbb F_9=\mathbb F_3[z]/(z^2+1)\). Counts \(6,12,36,72,48\), respectively, agree with the uniform orthogonal-order formulas. The independent finite enumerations test the low-dimensional assertions; the preceding proof supplies the all-parameter justification. Reproduce with `python verify.py` using standard Python only.

## Relationship to prior work

Elduque and Labra (arXiv:1312.4685v1, 2013) constructed the graph-evolution correspondence and proved finiteness of automorphisms in the perfect case \(E=E^2\). Their Example 4.1 also exhibits orthogonal symmetry for a different nonperfect three-dimensional example, so the mere appearance of an orthogonal group is not claimed as original. Here \(E_m^2\) has dimension two and \(m\ge3\); the contribution is the full star-family identification, both characteristic-divisibility cases, and exact odd-field cardinalities.

Rodiño Montoya, Viana Bedoya and Henao (arXiv:2505.15604v2, 2025), §2 and Examples 2.19–2.21, identify the full automorphism group of the three-vertex path \(K_{1,2}\) over \(\mathbb C\); Example 3.3 treats the **diagonal subgroup** of \(K_{1,4}\), without a full star automorphism-group classification. Their group-action theorem only yields a full count when all automorphisms arise from graph symmetries, a hypothesis not satisfied in general here. Cadavid, Rodiño Montoya and Rodríguez (arXiv:1710.10516v2, 2017) focus on isomorphisms between adjacency- and random-walk-associated graph evolution algebras, not the count here. Characteristic-two results on square-zero derivations of complete-bipartite evolution algebras address a different map, identity, and characteristic and do not imply this theorem.

## Limitations

The result excludes characteristic two, stars with fewer than three leaves, random-walk evolution algebras, and arbitrary graphs. It counts labeled \(k\)-linear automorphisms, not automorphism-conjugacy classes or geometric components of an automorphism scheme. The finite computations do not certify the theorem for all \(q\) or \(m\). Priority remains subject to independent literature review, particularly for unpublished specializations of orthogonal stabilizer descriptions.

## References

1. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (first posted 2013-12-17), https://arxiv.org/abs/1312.4685.
2. M. L. Rodiño Montoya, N. A. Viana Bedoya and C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604v2 (2025), https://arxiv.org/html/2505.15604v2.
3. P. Cadavid, M. L. Rodiño Montoya and P. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516v2 (2017), https://arxiv.org/abs/1710.10516.
4. P. Cadavid and collaborators, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, arXiv:1807.02493 (2018), https://arxiv.org/abs/1807.02493.
