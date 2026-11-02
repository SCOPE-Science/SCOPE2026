# Automorphisms of complete-bipartite evolution algebras over odd finite fields

## Finding
Let \(m,n\ge2\) and \(k=\mathbb F_q\) of odd characteristic \(p\). For the evolution algebra of the complete bipartite graph \(K_{m,n}\), define \(s_d=(1,\ldots,1)^T\in k^d\), \(B_d(x,y)=x^Ty\), and
\[
\mathcal F_d(z,t)=\#\{M\in\operatorname{GL}_d(k):M^TM=tI_d,\ Ms_d=zs_d\},\qquad z,t\in k^\times.
\]
Its full automorphism group is the set of side-preserving pairs \((A,D)\) with
\[
A^TA=bI_m,\quad As_m=as_m,\qquad D^TD=aI_n,\quad Ds_n=bs_n,\qquad a,b\in k^\times,
\]
and, only if \(m=n\), the additional coset obtained by exchanging the two coordinate sides. In particular,
\[
|\operatorname{Aut}(E_{m,n})|=(1+\mathbf1_{m=n})\sum_{a,b\in k^\times}\mathcal F_m(a,b)\mathcal F_n(b,a).
\]
The factors are explicit. Set \(O_d=|O(s_d^\perp)|\) for \(p\nmid d\), with the restricted dot product having dimension \(d-1\) and discriminant \(1/d\); set \(H_d=|O(T_d)|\) for \(p\mid d\), where \(T_d\) is a nondegenerate space of dimension \(d-2\), discriminant \(-1\), obtained by splitting a hyperbolic plane through \(s_d\). These orthogonal-group orders are the standard finite-field orders determined by dimension and discriminant. Put \(\epsilon_d=1\) if \(d\) is odd and \(0\) otherwise. The exact cardinality is
\[
|\operatorname{Aut}(E_{m,n})|=(1+\mathbf1_{m=n})\begin{cases}
\gcd(3,q-1)O_mO_n,&p\nmid mn,\\
\frac{q-1}{2^{\epsilon_m}}q^{m-2}H_mO_n,&p\mid m,\ p\nmid n,\\
\frac{q-1}{2^{\epsilon_n}}q^{n-2}O_mH_n,&p\nmid m,\ p\mid n,\\
\frac{(q-1)^2}{2^{\epsilon_m+\epsilon_n}}q^{m+n-4}H_mH_n,&p\mid m,\ p\mid n.
\end{cases}
\]
In particular, simultaneous divisibility \(p\mid m,n\) gives a distinct double-isotropic parabolic regime.

## Assumptions and scope
The algebra is \(E_{m,n}=U\oplus V\), where \(U=k^m\), \(V=k^n\), with the bilinear product
\[
(u,v)(u',v')=\bigl(B_n(v,v')s_m,\ B_m(u,u')s_n\bigr).
\]
In a natural basis each vertex squares to the sum of its neighbors and pairwise distinct basis vectors multiply to zero. There are no restrictions on \(m,n\) beyond \(m,n\ge2\), including cases divisible by \(p\). Automorphisms are \(k\)-linear algebra automorphisms, not merely graph permutations. The theorem is a classification of rational finite-field points, not a claim about the automorphism-group scheme.

## Proof
First \(E_{m,n}^2=ks_m\oplus ks_n\) because both dot products are nondegenerate. This two-plane is characteristic. For \(\ell\in(E_{m,n}^2)^*\), write \(\alpha=\ell(s_m)\), \(\beta=\ell(s_n)\). The scalar-valued bilinear form \(\ell(xy)\) has Gram matrix \(\operatorname{diag}(\beta I_m,\alpha I_n)\), so its determinant, up to a nonzero scalar, is \(\beta^m\alpha^n\). Its degeneracy locus in the projective line \(\mathbb P((E^2)^*)\) consists of two distinct points, intrinsically defined by the multiplication. Any automorphism preserves or exchanges these points; therefore it preserves or exchanges the two lines \(ks_m\), \(ks_n\). An exchange requires equality of their coranks, hence \(m=n\).

Suppose the lines are preserved and write \(g(s_m)=as_m\), \(g(s_n)=bs_n\), where \(a,b\in k^\times\). Relative to \(U\oplus V\), write \(g=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\). Comparing \(g(xx')\) and \(g(x)g(x')\) for \(x,x'\in U\), then for \(x,x'\in V\), gives \(A^TA=bI_m,\ C^TC=0,\ D^TD=aI_n,\ B^TB=0\); comparing cross terms gives \(A^TB=C^TD=0\). The first and third identities make \(A,D\) invertible; therefore \(B=C=0\). The image identities are exactly \(As_m=as_m\), \(Ds_n=bs_n\). Conversely these four equations directly preserve every product. When \(m=n\), canonical exchange \((u,v)\mapsto(v,u)\) is an automorphism, giving the second coset.

It remains to count \(\mathcal F_d(z,t)\). If \(p\nmid d\), then \(B_d(s_d,s_d)=d\ne0\), so \(t=z^2\); the restriction to \(s_d^\perp\) can be any isometry after composing with scalar \(z^{-1}\), giving \(\mathcal F_d(z,t)=O_d\) exactly when \(t=z^2\), otherwise zero. Since the original dot form has determinant one and the line of \(s_d\) has determinant \(d\), the complementary determinant square-class is \(1/d\).

If \(p\mid d\), the nonzero vector \(s_d\) is isotropic. Choose an isotropic partner \(v\) with \(B(s_d,v)=1\); because \(p\ne2\), replacing \(v\) by \(v-B(v,v)s_d/2\) produces a hyperbolic plane. Its orthogonal complement \(T_d\) has dimension \(d-2\) and discriminant \(-1\). To count similitudes with multiplier \(t\) and \(s_d\mapsto zs_d\), first choose an arbitrary multiplier-\(t\) similitude of \(T_d\). For each such choice the stabilizer's unipotent radical is parameterized freely by \(T_d\), giving exactly \(q^{d-2}\) choices; the remaining hyperbolic basis vector is uniquely determined by pairing and isotropy equations. The multiplier map on the similitude group of a nondegenerate quadratic space over \(\mathbb F_q\) is surjective for even dimension (e.g. via the two-plane decomposition into hyperbolic or anisotropic norm planes), whereas in odd dimension its image is precisely the squares (take determinants of \(M^TM=tB\), and scalar similitudes give all squares). Thus
\[
\mathcal F_d(z,t)=q^{d-2}H_d\begin{cases}
1,&d\text{ even, or }t\in(k^\times)^2,\\0,&d\text{ odd and }t\notin(k^\times)^2.
\end{cases}\qquad(p\mid d).
\]
This is independent of \(z\ne0\). Substitute these two expressions in the double sum. When neither size is divisible by \(p\), the conditions \(b=a^2\) and \(a=b^2\) give \(a^3=1\), hence \(\gcd(3,q-1)\) choices. When exactly one size is divisible, the nondivisible side fixes the other multiplier to be a square and leaves \((q-1)/2^{\epsilon_d}\) scalar possibilities. When both are divisible, the multipliers \(a,b\) vary independently, with a square restriction from each odd-dimensional isotropic side. This yields all four formulas.

## Verification
The companion `verify.py` exhaustively constructs the relevant finite-field similitude matrices for six prime-field parameter sets \((q,m,n)=(3,2,2),(3,2,3),(3,3,2),(3,3,3),(5,2,2),(7,2,2)\). It compares exact counts with the formulas, including the case \(p\mid m,n\). Executing `python verify.py` prints `BIPARTITE_EVOLUTION_AUTOMORPHISMS_OK 6`. These finite instances check the numerical consequences but do not replace the arbitrary-dimension proof.

## Relationship to prior work
Elduque and Labra, *Evolution algebras and graphs* (2013), establish the graph framework and automorphism results for perfect evolution algebras, and exhibit an orthogonal automorphism phenomenon in a separate example. Rodiño Montoya, Viana Bedoya and Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs* (2025), analyze graph symmetries, automorphism actions and particular small graph examples. The present formula treats the complete-bipartite family with both parts of size at least two, gives the full orthogonal-similitude stabilizer and four finite-field arithmetic regimes. The literature comparison is not proof of publication priority. In particular, known results for one-leaf stars do not provide the double-isotropic regime of this theorem.

## Limitations
Only odd-characteristic finite fields, complete bipartite graphs with both parts at least two, and rational automorphisms are treated. No classification of automorphism-group schemes, characteristic-two automorphisms, or general bipartite graphs is claimed. Equivalent group descriptions in unpublished or incompletely indexed literature may exist, and independent mathematical validation has not been performed.

## References
1. Alberto Elduque and Alicia Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (first posted 2013-12-17), https://arxiv.org/html/1312.4685v1.
2. Mary Luz Rodiño Montoya, Natalia A. Viana Bedoya, and Carlos Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604v2, https://arxiv.org/html/2505.15604v2.
