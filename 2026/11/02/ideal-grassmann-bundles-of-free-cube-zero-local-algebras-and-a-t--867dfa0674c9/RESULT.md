# Ideal Grassmann bundles of free cube-zero local algebras and a twisted-cubic-cone boundary

## Finding
For each field \(k\) and integer \(n\geq1\), let \(V\) be an \(n\)-dimensional \(k\)-space and put
\[
A_n=k\oplus V\oplus(V\otimes_kV)=T_k(V)/T_k(V)_{\geq3},
\qquad J=V\oplus(V\otimes_kV).
\]
Multiplication is induced by tensor concatenation, so \(J^3=0\) and \(J^2=V\otimes V\). Every proper two-sided ideal \(I\) is classified uniquely by the following data:
\[
U\leq V,\quad B\leq (V/U)\otimes(V/U),\quad
\phi\in\operatorname{Hom}_k\left(U,((V/U)\otimes(V/U))/B\right).
\]
To reconstruct \(I\), let \(W\leq V\otimes V\) be the inverse image of \(B\) under the natural projection \(V\otimes V\to(V/U)\otimes(V/U)\), and take the inverse graph of \(\phi\) inside \(V\oplus(V\otimes V)\), modulo \(W\). If \(u=\dim U\), \(m=n-u\), and \(w=\dim B\), then
\[
\dim I=n^2-m^2+u+w.
\]
For fixed \(u,w\), the reduced locally closed ideal stratum is a vector bundle of rank \(u(m^2-w)\) over the relative Grassmannian of \(w\)-planes in \(\mathcal Q\otimes\mathcal Q\), where \(\mathcal Q\) is the rank-\(m\) universal quotient on \(\operatorname{Gr}(u,V)\). It is smooth, geometrically irreducible, and of dimension
\[
u(n-u)+w(m^2-w)+u(m^2-w).
\]
Over \(\mathbb F_q\), the generating polynomial for the number of distinct two-sided ideals of every vector-space dimension, including \(A_n\), is
\[
\boxed{\displaystyle
Z_n(q;T)=T^{1+n+n^2}+
\sum_{u=0}^{n}\binom{n}{u}_q
\sum_{w=0}^{(n-u)^2}\binom{(n-u)^2}{w}_q
q^{u((n-u)^2-w)}T^{n^2-(n-u)^2+u+w}.}
\]
For \(n=2\), the **reduced variety of four-dimensional two-sided ideals** is projectively isomorphic, over every field and in every characteristic, to the projective cone over a twisted cubic in \(\mathbb P^3\), equivalently to \(\mathbb P(1,1,3)\). Its unique singular point is the ideal \(J^2\). It is a degree-three surface with \(q^2+q+1\) points over every \(\mathbb F_q\), although it is not smooth like \(\mathbb P^2\).

## Assumptions and scope
All vector spaces, ideals, and dimensions are over the given arbitrary field \(k\), not necessarily algebraically closed or perfect; no characteristic restrictions are used. In the expression for \(A_n\), the direct-sum decomposition is the length filtration by words in a free associative algebra, with all words of length at least three zero. Its unit is the empty word. A proper ideal is necessarily contained in \(J\), because every element with nonzero scalar part is a unit. For algebraic-geometric assertions, the ideal locus means the **reduced** closed subscheme of \(\operatorname{Gr}(d,A_n)\) cut out by two-sided multiplication closure. No claim is made about the possible nonreduced scheme structure of the equations.

The finite-field symbol \(\binom{a}{b}_q\) counts \(b\)-dimensional subspaces of \(\mathbb F_q^a\). The power \(T^d\) in \(Z_n\) records an ideal's dimension, not its codimension. A field with \(q\) elements can have any prime-power cardinality; the proof is not restricted to prime fields.

## Proof
**1. Ideals are controlled by their first two radical layers.** Set \(M=V\otimes V=J^2\). Let \(I\subset J\) be an ideal, let \(U\) be its projection to \(V\), and let \(W=I\cap M\). For each \(u\in U\), choose any lift \(u+t\in I\), with \(t\in M\). Multiplication on the left and right by \(v\in V\) yields \(v\otimes u\) and \(u\otimes v\), hence
\[
V\otimes U+U\otimes V\subseteq W.
\]
The kernel of the canonical map \(M\to(V/U)\otimes(V/U)\) is exactly \(V\otimes U+U\otimes V\). Thus \(W\) corresponds to a unique subspace \(B\leq(V/U)\otimes(V/U)\). Modulo \(W\), the possible lifts form the graph of a unique linear map \(\phi:U\to M/W\cong((V/U)\otimes(V/U))/B\). Conversely, any such \(U,B,\phi\) gives a subspace closed under both multiplications by \(V\); scalar multiplication and multiplication by \(J^2\) add no conditions because \(J^3=0\). This proves the classification in both directions, including uniqueness.

**2. Dimensions, geometry, and counts.** Writing \(m=n-u\), the kernel \(V\otimes U+U\otimes V\) has dimension \(n^2-m^2\). Consequently \(\dim W=n^2-m^2+w\), whence \(\dim I=n^2-m^2+u+w\). On \(\operatorname{Gr}(u,V)\), let \(\mathcal S\) and \(\mathcal Q\) be the tautological rank-\(u\) subbundle and rank-\(m\) quotient. Over \(\operatorname{Gr}_{\operatorname{Gr}(u,V)}(w,\mathcal Q\otimes\mathcal Q)\), write \(\mathcal B\) for the tautological rank-\(w\) subbundle. The lifts comprise the total space of
\[
\operatorname{Hom}\bigl(\mathcal S,(\mathcal Q\otimes\mathcal Q)/\mathcal B\bigr).
\]
This is a vector bundle over a Grassmann bundle, giving smoothness, geometric irreducibility and the displayed dimension. On \(\mathbb F_q\)-points there are \(\binom{n}{u}_q\) choices for \(U\), \(\binom{m^2}{w}_q\) choices for \(B\), and \(q^{u(m^2-w)}\) choices for \(\phi\). Summing, and adjoining the sole nonproper ideal \(A_n\), proves \(Z_n(q;T)\). The same argument yields the motivic identity obtained by replacing Gaussian counts by Grassmannian classes and the power of \(q\) by the corresponding affine-space class.

**3. The exceptional two-loop projective surface.** Now let \(n=2\), \(V=kx\oplus ky\), and \(M=\langle x^2,xy,yx,y^2\rangle\). If \(\dim I=4\), the dimension formula leaves precisely two possibilities: either \(U=0,W=M\), hence \(I=J^2\), or \(\dim U=1\), \(B=0\), \(\dim W=3\). In the second case take \(U=k(ax+by)\), with \((a,b)\ne(0,0)\), and \(W=V\otimes U+U\otimes V\).

Let \(X,Y,P,Q,R,S\) denote the dual basis of \(x,y,x^2,xy,yx,y^2\) in \(J^*\). Define
\[
p=bX-aY,\qquad \ell=b^2P-abQ-abR+a^2S.
\]
The line annihilating \(W\) in \(M^*\) is \(k\ell\). A lift of \(U\) has the form \(u+v\), with \(u=ax+by\) and \(v\in M\). Choose \(p'\in V^*\) with \(p'(u)=1\). Then the annihilator of \(I\) in \(J^*\) is the two-plane
\[
I^{\perp}=\langle p,\ell-\ell(v)p'\rangle.
\]
Since \(p\wedge p'=X\wedge Y\), its Plücker point is
\[
[p\wedge\ell-\ell(v)X\wedge Y].
\]
Direct expansion shows that all these Plücker coordinates lie in a projective \(\mathbb P^4\), in which (after fixed linear changes of coordinates) they are
\[
[Z:C_0:C_1:C_2:C_3]=[Z:a^3:a^2b:ab^2:b^3].
\]
For each \([a:b]\in\mathbb P^1\), every \(Z\in k\) occurs, since \(\ell\ne0\); rescaling \((a,b)\) rescales all the coordinates cubically. The remaining ideal \(J^2\) maps to the vertex \([1:0:0:0:0]\). The reduced image is exactly the projective variety cut out by the three quadrics
\[
C_0C_2-C_1^2=0,\qquad C_0C_3-C_1C_2=0,\qquad C_1C_3-C_2^2=0.
\]
Indeed these are the homogeneous prime ideal of the cubic Veronese image of \(\mathbb P^1\); adjoining the free coordinate \(Z\) forms its projective cone. On each nonvertex chart where \(C_0\ne0\) or \(C_3\ne0\), the coordinates \((b/a,Z/a^3)\) or \((a/b,Z/b^3)\) give affine-plane charts. The cone therefore is smooth off the vertex. All defining quadrics lack linear terms at the vertex, where the Zariski tangent space has dimension four but the surface has dimension two. Hence the vertex, corresponding exactly to \(J^2\), is the unique singular point. The coordinate ring is the third Veronese of \(k[a,b,Z]\) with weights \((1,1,3)\), proving the weighted-projective-plane description. Over \(\mathbb F_q\), there are \(q\) nonvertex ideals for each of the \(q+1\) lines \(U\), plus \(J^2\), giving \(q^2+q+1\).

## Verification
The standalone file `verify.py` constructs truncated tensor multiplication from first principles and enumerates all vector subspaces of \(J\) for \(n=1\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and for \(n=2\) over \(\mathbb F_2,\mathbb F_3\). It checks left and right ideal closure without using the classification in its test. It then compares the dimension distributions with the closed formula. For every four-dimensional two-loop ideal it independently checks that the dual Plücker coordinates lie in the stated five-space and satisfy all three twisted-cubic quadrics; it also checks the explicit projective parameterization is exhaustive. All five configurations pass. In particular, for \(n=2\) the full ideal counts are \(78\) over \(\mathbb F_2\) and \(230\) over \(\mathbb F_3\), with \(7\) and \(13\) four-dimensional ideals respectively. See `verify_output.txt` and `VERIFICATION.md`. Finite enumeration checks only those fields; the arbitrary-field assertions are proved above.

## Relationship to prior work
Hubery's *Irreducible components of quiver Grassmannians* (first publicly submitted March 19, 2013) supplies general submodule-Grassmannian and component methods, but does not give this algebra's full ideal-dimension census or identify its four-ideal locus with a singular cubic cone. Luo's *Local algebras with radical cubic zero are PCM-free* (2013) concerns Gorenstein-projective modules, not an ideal parameterization. Babson, Huisgen-Zimmermann and Thomas's *Generic representation theory of quivers with relations* (2014) treats generic modules over truncated path algebras; its generic-module theorems do not state this ideal count or Plücker cone. Feigin and Reineke's *From brick manifolds to Grassmannians of bimodules* (2025) constructs special sub-bimodule Grassmannians over path algebras of acyclic quivers, unlike the regular-bimodule ideal locus for the truncated two-loop algebra. General constructions are acknowledged, and no universal absence of an earlier equivalent result is claimed.

## Limitations
The geometrical classification is of reduced loci and locally closed strata, not a proof that the original ideal-closure schemes are reduced. The general stratification does not classify every irreducible component or all intersections among strata for arbitrary \(n,d\). The singular projective-cone identification is specific to four-dimensional ideals of the two-loop cube-zero algebra. The result does not cover extra relations beyond truncation, one-sided ideals, or longer radical filtrations. Exhaustive historical priority and independent mathematical validation have not been established.

## References
1. A. Hubery, *Irreducible components of quiver Grassmannians*, arXiv:1303.4585, first submitted 2013-03-19, https://arxiv.org/abs/1303.4585.
2. R. Luo, *Local algebras with radical cubic zero are PCM-free*, arXiv:1308.6059, first submitted 2013-08-28, https://arxiv.org/abs/1308.6059.
3. E. Babson, B. Huisgen-Zimmermann, R. Thomas, *Generic representation theory of quivers with relations*, arXiv:1407.2673, first submitted 2014-07-10, https://arxiv.org/abs/1407.2673.
4. E. Feigin, M. Reineke, *From brick manifolds to Grassmannians of bimodules*, arXiv:2510.21319, first submitted 2025-10-24, https://arxiv.org/abs/2510.21319.
