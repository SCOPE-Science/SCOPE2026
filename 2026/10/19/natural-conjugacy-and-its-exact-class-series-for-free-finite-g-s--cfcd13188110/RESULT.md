# Natural conjugacy and its exact class series for free finite \(G\)-sets

## Finding

Let \(G\) be any finite group (not assumed abelian) and let \(m\geq1\). Give \(X_m=G\times\{1,\ldots,m\}\) its free left \(G\)-action, and put \(M_m(G)=\operatorname{End}_G(X_m)\). Write \(\mathfrak n\) for natural conjugacy in this monoid, defined precisely below, and \(N_m(G)=|M_m(G)/\!\sim_{\mathfrak n}|\). Let \(c(G)\) be the number of ordinary conjugacy classes of the **group** \(G\).

**Classification.** Every equivariant endomorphism induces a functional digraph on its image orbits. Two endomorphisms are naturally conjugate if and only if their image-orbit digraphs are isomorphic with corresponding directed cycles carrying the same conjugacy classes of their ordered \(G\)-multipliers. The tree-edge multipliers do not contribute additional invariants. In particular, the exact natural-conjugacy count depends on \(G\) only through \(c(G)\), even when \(G\) is nonabelian.

**Exact generating series.** There is a unique formal series \(T(z)\in z^2\mathbb Z[[z]]\) satisfying
\[
T(z)=z\left(\exp\left(\sum_{j\ge1}\frac{T(z^j)}j\right)-1+z\right).
\]
Put
\[
A(z)=z\exp\left(\sum_{j\ge1}\frac{T(z^j)}j\right).
\]
Then the natural-conjugacy class numbers for all \(m\ge1\) are given by
\[
\boxed{\displaystyle
\sum_{m\ge1}N_m(G)z^m
=\frac{1}{1-z}\left(\prod_{d\ge1}(1-A(z^d))^{-c(G)}-1\right).}
\]
All infinite sums and products are well defined coefficientwise as formal power series. For example, for a trivial group the initial counts \(N_m\), at \(m=1,\ldots,6\), are \(1,3,7,15,30,61\); for \(G=S_3\), with \(c(G)=3\), they are \(3,12,37,103,268,675\).

## Assumptions and scope

We use the functional-composition convention \((uv)(x)=u(v(x))\). A pair \(a,b\in M_m(G)\) is *naturally conjugate*, written \(a\sim_{\mathfrak n}b\), when there exist \(g,h\in M_m(G)\) for which
\[
ag=gb,\qquad bh=ha,\qquad hag=b,\qquad gbh=a.
\]
No commutativity assumption on \(G\) is made. The group \(G\) is finite, \(m\) is a positive integer, and all \(G\)-orbits in \(X_m\) are free and regular. The result does **not** claim a classification for nonfree \(G\)-sets (whose stabilizers may vary).

Every \(a\in M_m(G)\) has a unique description by a map \(f:\{1,\ldots,m\}\to\{1,\ldots,m\}\) and multipliers \(u_i\in G\):
\[
a(g,i)=(g u_i,f(i)).\]
Write \(I=f(\{1,\ldots,m\})\), and regard \(f\vert_I:I\to I\) as a functional digraph with edge \(i\to f(i)\), labeled by \(u_i\) at each \(i\in I\). The label of each directed cycle is the conjugacy class in \(G\) of the ordered product of its edge multipliers, read in cyclic order. Replacing the starting vertex conjugates the product, so the class is well defined.

For a nonempty finite functional digraph \(D\), write \(r(D)\) for its number of vertices and \(s(D)\) for the number of vertices with indegree zero **inside \(D\)**. These are intrinsic to the image-restricted digraph, not to the full orbit map.

## Proof

**1. Natural conjugacy is conjugacy of the image dynamics.** Let \(a,b\in M_m(G)\). The four defining equations imply \(g(b(X_m))=a(X_m)\) and \(h(a(X_m))=b(X_m)\): the first two intertwining equations give inclusions, and the last two give the opposite inclusions. Moreover, combining \(ag=gb\) with \(hag=b\) yields \(hgb=b\), while combining \(bh=ha\) with \(gbh=a\) yields \(gha=a\). Hence the restrictions \(g|_{b(X_m)}\) and \(h|_{a(X_m)}\) are inverse \(G\)-equivariant bijections intertwining \(b\) and \(a\) on the respective images.

Conversely, suppose an equivariant bijection \(\theta:b(X_m)\to a(X_m)\) satisfies \(a\theta=\theta b\) on \(b(X_m)\). Define \(g=\theta\) on \(b(X_m)\). On each free \(G\)-orbit outside \(b(X_m)\), choose one representative \(x\), choose \(y\in a^{-1}(\theta(b(x)))\), and extend equivariantly by \(g(kx)=ky\). Such a preimage exists because \(\theta(b(x))\in a(X_m)\), and such an extension is well defined because the source orbit is free. Then \(ag=gb\) on all of \(X_m\). Construct \(h\) similarly, extending \(\theta^{-1}\) from \(a(X_m)\), so \(bh=ha\). As \(h\theta\) is the identity on \(b(X_m)\), \(hag=b\); as \(g\theta^{-1}\) is the identity on \(a(X_m)\), \(gbh=a\). This proves the equivalence.

**2. Gauge reduction to conjugacy classes of cycle products.** Let \((f,u)\) and \((p,v)\) describe \(a\) and \(b\). An equivariant image bijection induces a bijection \(\sigma:I\to J\) of orbit indices, where \(J=p(\{1,\ldots,m\})\), and is given by right multipliers \(t_i\in G\) on each orbit. The necessary and sufficient equations are
\[
\sigma(f(i))=p(\sigma(i)),\qquad
u_i t_{f(i)}=t_i v_{\sigma(i)}\quad(i\in I),
\]
On a directed cycle, multiplying these equations in order yields that the two ordered cycle products are conjugate in \(G\). Conversely, given the same class of cycle product and a graph isomorphism \(\sigma\), choose one \(t_i\) on each cycle to conjugate its two products. Solve the remaining equations successively around that cycle. Then solve \(t_i=u_i t_{f(i)}v_{\sigma(i)}^{-1}\) recursively on all off-cycle vertices, working backward from the cycles. Every solution is in \(G\), and it defines the required image bijection. No tree-edge labels survive. Thus functional digraph isomorphism together with one \(G\)-conjugacy-class color per directed cycle is a complete classification.

**3. Which image digraphs are realizable?** Let \(D\) have \(r\) vertices and \(s\) indegree-zero vertices. If \(D\) is \(f|_I\) for some full orbit map on \(m\) vertices, each of its \(s\) indegree-zero image vertices must have an incoming edge from a distinct index outside \(I\), since every vertex of \(I=f(\{1,\ldots,m\})\) has a preimage. Hence \(m-r\ge s\). Conversely, if \(r+s\le m\), adjoin \(m-r\) exterior vertices, send \(s\) of them bijectively to the indegree-zero vertices of \(D\), and send the rest anywhere into \(D\). The full map has image exactly the prescribed \(r\) vertices and restricts to \(D\). Assign arbitrary group multipliers. Therefore the realizable colored image digraphs are *exactly* those with \(r(D)+s(D)\le m\).

**4. Unlabeled enumeration with source marking.** Give each vertex of a functional digraph weight \(z\), with an extra factor \(z\) when its indegree is zero. Its total weight is \(z^{r(D)+s(D)}\). An unordered rooted in-tree feeding into a cycle vertex has generating series \(T(z)\): a noncycle root with a nonempty multiset of child trees has weight \(z\), while a root with no children is an indegree-zero vertex and has weight \(z^2\). The ordinary generating series for unordered multisets of objects counted by \(T(z)\) is
\[
E(z)=\exp\left(\sum_{j\ge1}\frac{T(z^j)}j\right)
=\prod_{d\ge1}(1-z^d)^{-[z^d]T(z)}.
\]
Thus \(T(z)=z(E(z)-1)+z^2\), and the cycle-vertex-with-attached-multiset series is \(A(z)=zE(z)\). Since \(T\) has no constant or linear term, this equation recursively determines each coefficient, starting with \([z^2]T(z)=1\).

A connected functional digraph consists of a directed cycle of such decorated cycle vertices. The cyclic isomorphism counts are given by the cycle index of directed cycles. An unordered collection of connected functional digraphs, each directed cycle receiving one of \(c=c(G)\) independent colors, consequently has the formal product
\[
F_c(z)=\prod_{d\ge1}(1-A(z^d))^{-c}.
\]
For completeness, its formal logarithm follows by writing the cycle index for one color as
\[
\sum_{k\ge1}\frac{\varphi(k)}k
\log\frac1{1-A(z^k)},
\]
then applying the ordinary multiset transform and the elementary divisor identity \(\sum_{k\mid n}\varphi(k)=n\). The exponent \(c\) accounts for the choice of the group-conjugacy-class color independently on each directed cycle. The empty graph contributes one, so the coefficient of \(z^q\) in \(F_c(z)-1\) counts precisely the nonempty colored image digraphs with \(r+s=q\). By step 3 a single such diagram corresponds to one natural-conjugacy class for every \(m\ge q\). Summing \(z^m\) over \(m\ge q\) multiplies by \(1/(1-z)\), proving the stated formula.

## Verification

A standalone Python-standard-library program at `verification/check.py` (run with `python3 verification/check.py`) reconstructs the formal coefficients and independently enumerates finite endomorphisms. For the nonabelian group \(S_3\) acting on two free orbits, the program builds all \(144\) equivariant endomorphisms, checks all \(10{,}296\) unordered distinct pairs against the **four defining monoid equations**, and separately tests isomorphism of restricted image dynamics. The criteria agree pairwise, and exactly \(12\) equivalence classes occur, with class sizes \(1,4,4,6,6,9,12,12,12,18,24,36\). For the trivial group and \(1\le m\le5\), an unrelated exhaustive enumeration of functional maps up to isomorphism of image restrictions gives \(1,3,7,15,30\), matching the formal series. The verifier also checks initial formal coefficients for \(c=1\) and \(c=3\). These checks are finite corroboration; the proof above, not the tests, establishes all-parameter claims.

## Relationship to prior work

Araújo, Bentz, Kinyon, Konieczny, Malheiro, and Mercier, arXiv:2301.04252 (first publicly posted January 11, 2023; version 3 dated April 28, 2026), develop natural conjugacy for transformation monoids. Their Section 4.4 explicitly assumes an **abelian** group in its finite \(G\)-set theorem (Theorem 4.29); their Problem 7.4 asks for the **nonabelian** extension. The present classification handles the *free-orbit* case without commutativity and supplements it with a complete closed-form class-count series, whose dependence only on \(c(G)\) is new in this setting. The unrestricted nonfree-group-action version of their question is not addressed.

The same paper's full transformation monoid characterization is the \(G\) trivial special case, so that aspect of the classification alone is not original. The class-number formula for all \(m\), its source-weighted combinatorial construction, and its nonabelian-group specialization are the substantive additional claims. Standard cycle-index and Pólya multiset identities are used as counting machinery, not asserted as new results. Earlier work on inverse-semigroup conjugacy, arXiv:1810.03208, treats a different class of semigroups and different hypotheses. Available descriptions of monoid wreath-product *relative rank* theorems likewise do not imply a natural-conjugacy orbit enumerator.

## Limitations

The result is confined to **finite free** \(G\)-sets; variable stabilizers or nonfree orbits may produce additional invariants. It concerns the specific four-equation natural conjugacy and is not a classification of all semigroup conjugacy relations. The displayed formula is an exact formal generating function, not a claimed elementary closed formula for individual coefficients or a growth asymptotic. Independent audit has not been performed. Although extensive targeted literature comparisons did not locate an equivalent nonabelian free-orbit enumerator, unindexed prior work or less-obvious species formulations remain an originality risk.

## References

1. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, and V. Mercier, *Conjugacy in Abstract Semigroups, Transformation and Diagram Monoids, and Conjugacy Growth*, arXiv:2301.04252, first version January 11, 2023, particularly Section 4.4, Theorem 4.29, and Problem 7.4. Available at https://arxiv.org/html/2301.04252v3 and https://arxiv.org/abs/2301.04252.
2. J. Araújo, M. Kinyon, and J. Konieczny, *Conjugacy in inverse semigroups*, arXiv:1810.03208; *Journal of Algebra* 533 (2019), 142–173.
3. F. Bergeron, G. Labelle, and P. Leroux, *Combinatorial Species and Tree-Like Structures*, Cambridge University Press, 1998, for the classical cycle-index and multiset enumeration machinery.
