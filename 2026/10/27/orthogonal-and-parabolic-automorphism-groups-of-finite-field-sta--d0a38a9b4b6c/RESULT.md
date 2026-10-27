# Orthogonal and parabolic automorphism groups of finite-field star evolution algebras

## Finding

Let \(q\) be an odd prime power of characteristic \(p\), and let \(m\ge 2\). Consider the evolution algebra \(A_m(q)\) of the star \(K_{1,m}\), with natural basis \(c,v_1,\ldots,v_m\) and products
\[
c^2=s=\sum_{i=1}^m v_i,\qquad v_i^2=c,\qquad cv_i=v_iv_j=0\quad(i\ne j).
\]
Put \(V=\langle v_1,\ldots,v_m\rangle\) and give \(V\) the standard symmetric dot product \(\langle x,y\rangle=\sum_i x_i y_i\). Every \(\mathbb F_q\)-algebra automorphism, and only an automorphism, has the unique form
\[
T_{a,W}(c)=ac,\quad T_{a,W}|_V=W,\quad
 a\in\mathbb F_q^\times,\quad W^TW=aI_m,\quad Ws=a^2s.
\tag{1}
\]
The resulting exact orders exhibit a divisibility-by-characteristic transition.

If \(p\nmid m\), let \(H=s^\perp\subset V\). This is nondegenerate of dimension \(m-1\), and the group is
\[
\operatorname{Aut}_{\mathbb F_q}(A_m(q))\cong
\mu_3(\mathbb F_q)\times O(H),\qquad
|\operatorname{Aut}(A_m(q))|=\gcd(3,q-1)\,|O(H)|.
\tag{2}
\]
Here \(\mu_3(\mathbb F_q)=\{a\in\mathbb F_q^\times:a^3=1\}\), and the Gram determinant of \(H\) has square class \(m\).

If \(p\mid m\), then \(s\) is a nonzero isotropic vector. Choose a hyperbolic partner \(t\) with \(\langle s,t\rangle=1\) and \(\langle t,t\rangle=0\), and put \(K=(\mathbb F_qs\oplus\mathbb F_qt)^\perp\), of dimension \(m-2\) and Gram determinant square class \(-1\). Then the group is the explicitly parametrized parabolic-similitude subgroup described by (1), and
\[
|\operatorname{Aut}(A_m(q))|
=q^{m-2}|O(K)|\times
\begin{cases}
(q-1)/2,&m\text{ odd},\\
q-1,&m\text{ even}.
\end{cases}
\tag{3}
\]
These formulas specify all odd finite fields and every number of leaves \(m\ge2\), including primes dividing \(m\).

To make (2) and (3) fully numerical, for a nondegenerate \(d\)-dimensional quadratic space with Gram determinant square class \(\delta\), put \(\chi\) for the quadratic character of \(\mathbb F_q^\times\). Standard orthogonal orders are
\[
|O(2r+1,q)|=2q^{r^2}\prod_{j=1}^r(q^{2j}-1),\qquad r\ge0,
\]
\[
|O^{\epsilon}(2r,q)|=2q^{r(r-1)}(q^r-\epsilon)
 \prod_{j=1}^{r-1}(q^{2j}-1),\qquad
\epsilon=\chi((-1)^r\delta),\quad r\ge1.
\]
In (2), take \(d=m-1\) and \(\delta=m\); in (3), take \(d=m-2\) and \(\delta=-1\). For example, \(|\operatorname{Aut}(A_3(5))|=12\), \(|\operatorname{Aut}(A_3(7))|=36\), \(|\operatorname{Aut}(A_4(3))|=48\), and \(|\operatorname{Aut}(A_5(5))|=60000\).

## Assumptions and scope

Fields are \(\mathbb F_q\) of odd characteristic. All automorphisms are invertible linear maps preserving multiplication; field automorphisms are **not** included. No bound is imposed on \(m\) other than \(m\ge2\). The forms and orthogonal groups are taken over \(\mathbb F_q\), not its algebraic closure. The displayed finite-group orders count \(\mathbb F_q\)-rational automorphisms, not geometric connected components.

## Proof

**Reduction to the similitude stabilizer.** Write any algebra automorphism as \(T(c)=ac+u\), \(T(v_i)=b_i c+w_i\), with \(u,w_i\in V\). Squaring the images of \(v_i\) gives
\[
T(c)=T(v_i)^2=\langle w_i,w_i\rangle c+b_i^2s,
\]
so all \(b_i^2\) are equal. For distinct \(i,j\), multiplying their images gives \(b_ib_j s+\langle w_i,w_j\rangle c=0\); since \(c,s\) are independent, \(b_ib_j=0\). Because \(m\ge2\), every \(b_i=0\), and hence \(u=0\). Invertibility forces \(a\ne0\). The squares and cross products now read \(W^TW=aI_m\). Finally \(T(c^2)=T(s)=Ws\) and \(T(c)^2=a^2s\), giving \(Ws=a^2s\). Conversely these equalities preserve every defining product, and \(a\ne0\) plus \(W^TW=aI_m\) ensure invertibility, proving (1).

**Nonisotropic case.** Suppose \(p\nmid m\). Since \(\langle s,s\rangle=m\), applying the two identities in (1) to \(s\) gives \(a^4m=am\), hence \(a^3=1\). Put \(U=a^{-2}W\). Then \(U^TU=a^{-3}I_m=I_m\) and \(Us=s\). Conversely any cube root \(a\) and isometry \(U\) fixing \(s\) yield \(W=a^2U\). The point stabilizer in \(O(V)\) of the nonisotropic vector \(s\) restricts isomorphically to \(O(s^\perp)\). This proves the direct-product structure and order in (2). In the basis \(v_i-v_m\), \(1\le i<m\), the Gram matrix of \(H\) is \(I_{m-1}+J_{m-1}\), with determinant \(m\), establishing the discriminant assertion.

**Isotropic case.** Suppose \(p\mid m\). Then \(s\ne0\) and \(\langle s,s\rangle=0\). Because the dot product on \(V\) is nondegenerate and \(p\ne2\), there is an isotropic \(t\) with \(\langle s,t\rangle=1\), giving the orthogonal decomposition \(V=\langle s,t\rangle\perp K\). Since the hyperbolic-plane determinant is \(-1\) up to squares and \(\det V=1\), \(\det K\) has square class \(-1\).

Let \(a\in\mathbb F_q^\times\). Every \(W\) in (1) is uniquely determined by a similitude \(g:K\to K\) of multiplier \(a\) and a vector \(z\in K\) as follows:
\[
\begin{aligned}
Ws&=a^2s,\\
Wu&=gu-a\langle gu,z\rangle s &&(u\in K),\\
Wt&=a^{-1}t+z-\tfrac a2\langle z,z\rangle s.
\end{aligned}
\tag{4}
\]
Indeed, pairing the image of \(s\) with \(Wt\) forces its \(t\)-coefficient to equal \(a^{-1}\); pairing \(Wu\) with \(Wt\) forces the shown \(s\)-coefficient of \(Wu\); and the equation \(\langle Wt,Wt\rangle=0\) forces the final coefficient. Conversely direct substitution in (4) gives \(W^TW=aI\) and \(Ws=a^2s\). The parameter \(z\) is arbitrary, contributing \(q^{m-2}\) choices for each \(g\).

For a nondegenerate odd-dimensional \(K\), the similarity multiplier \(a\) must be a square: taking determinants of \(g^TG=aG\) gives \((\det g)^2=a^{\dim K}\). Every square occurs by scalar multiplication of an isometry. For even-dimensional \(K\), every nonzero multiplier occurs: the standard classification splits \(K\) into hyperbolic planes and possibly an anisotropic plane; a hyperbolic plane has a similitude of every multiplier, while on an anisotropic plane multiplication in \(\mathbb F_{q^2}\) realizes every multiplier by surjectivity of the norm. In either case each nonempty multiplier fiber is an \(O(K)\)-coset. As \(\dim K=m-2\), there are \((q-1)/2\) fibers when \(m\) is odd and \(q-1\) otherwise. Multiplying by \(q^{m-2}|O(K)|\) proves (3).

The displayed orthogonal-order formulas are the classical orders of nondegenerate orthogonal groups over odd finite fields; they apply to the specified determinants and include the \(d=1\) boundary.

## Verification

Run `python verify_star.py` using Python 3 and its standard library. The program independently counts all column matrices \(W\) satisfying (1) by exhaustive enumeration for \((q,m)=(3,2),(5,2),(7,2),(3,3),(5,3),(7,3),(3,4)\). The observed and predicted group orders are respectively \(2,2,6,6,12,36,48\). It also builds an explicit modular example at \((q,m)=(5,5)\) with multiplier \(a=4\), for which \(a^3\ne1\), and verifies the defining Gram and eigenvector equations. Finite experiments are corroboration, not the proof for arbitrary \(q,m\).

## Relationship to prior work

Cadavid, Rodiño Montoya and Rodriguez (arXiv:1807.02493, first public 2018-07-06) analyze derivations of graph-associated evolution algebras through graph twin classes; a star's leaves form such a class. Reis and Cadavid (arXiv:2006.11934, first public 2020-06-21) extend derivation results to arbitrary characteristic. Their derivation statements do not determine the finite-field automorphism-group orders in (2)–(3).

The later Rodiño Montoya, Viana Bedoya and Henao (arXiv:2505.15604) treat graph symmetries acting on automorphisms; their Theorem 2.17 gives a free action and their Example 3.3 considers the diagonal subgroup for a four-leaf star. A free symmetry action does not determine the number of its orbits, and that example does not enumerate the full automorphism group. The new step here is the exact matrix classification (1), its nonisotropic orthogonal reduction and isotropic parabolic jump with rational-point counts. Known orthogonal-group order formulas are standard input, not asserted as new.

## Limitations

The results exclude characteristic two. They count field-linear automorphisms, not semilinear automorphisms or automorphisms of the graph itself. The matching computational cases do not establish the infinite-family theorem independently of the written proof. The literature comparison cannot rule out an earlier result presented under orthogonal-similitude stabilizers rather than evolution-algebra terminology, particularly in general works on symmetric bilinear-form algebras. The cited 2020 derivation paper was located and its scope compared, but its full text was not available in the inspected sources.

## References

1. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodriguez, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, arXiv:1807.02493 (submitted 2018-07-06), Linear and Multilinear Algebra 68 (2020), 1340–1354.
2. T. Reis and P. Cadavid, *Derivations of Evolution Algebras associated to graphs over a field of any characteristic*, arXiv:2006.11934 (submitted 2020-06-21).
3. M. L. Rodiño Montoya, N. A. Viana Bedoya and C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604 (submitted 2025-05-21).
4. Standard finite-orthogonal-group order formulas and the classification of quadratic forms over finite fields of odd characteristic (used in the proof; not assigned priority for the new claim).
