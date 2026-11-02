# The ideal lattice and projective abelian-subalgebra geometry of scalar-restricted free class-three Lie algebras

## Finding
For every prime power \(q\) and integer \(m\ge2\), the five-dimensional free class-three nilpotent Lie algebra on two generators over \(K=\mathbb F_{q^m}\), regarded by restriction of scalars as an \(\mathbb F_q\)-Lie algebra \(L\), has a completely described ideal lattice, abelian-subalgebra lattice, maximal-abelian incidence geometry, and maximal-abelian automorphism orbits.

Write \(Q=q^m\), \(P=Q^2+Q+1\), and let \({n\brack d}_q\) denote the number of \(d\)-dimensional \(\mathbb F_q\)-subspaces of an \(n\)-dimensional space; set it to zero outside \(0\le d\le n\). Let \(A_d\) count all \(d\)-dimensional abelian \(\mathbb F_q\)-Lie subalgebras, and \(I_d\) count all \(d\)-dimensional ideals. For every \(0\le d\le5m\),
\[
 A_d=P{3m\brack d}_q-(P-1){2m\brack d}_q,
\]
\[
 I_d={2m\brack d}_q+\mathbf1_{2m<d\le3m}{m\brack d-2m}_q+\mathbf1_{3m<d\le5m}{2m\brack d-3m}_q.
\]
In particular, every maximal abelian subalgebra has dimension \(3m\); there are \(P\) of them, all containing the same \(2m\)-dimensional center and intersecting pairwise in that center. Exactly one of these is an ideal. The induced automorphism action on the \(P\) maximal abelian subalgebras has precisely two orbits, of sizes \(1\) and \(P-1=Q^2+Q\).

The number of ordered pairwise-commuting \(r\)-tuples, for every integer \(r\ge0\), is
\[
 C_r=P Q^{3r}-(P-1)Q^{2r}.
\]

## Assumptions and scope
Fix any prime power \(q\), an integer \(m\ge2\), \(k=\mathbb F_q\), and \(K=\mathbb F_{q^m}\). The Lie algebra \(L\) is a \(5m\)-dimensional vector space over \(k\) with \(K\)-linear coordinates \(aX+bY+cU+dV+eW\), and its \(K\)-bilinear alternating bracket is specified by
\[
 [X,Y]=U,\qquad [X,U]=V,\qquad [Y,U]=W,
\]
with all other basic brackets zero. These relations define a Lie algebra in all characteristics, including characteristic two. Put \(Z=KV\oplus KW\) and \(D=KU\oplus Z\). Thus \(Z=Z(L)\), \(D=[L,L]\), and \(L/Z\cong K^3\) as \(K\)-vector spaces. All subalgebras and ideals in this paper are taken over \(k\), not merely over \(K\). Neither abstract class-three algebras beyond this model nor uniqueness of this model in characteristic two is asserted.

## Proof
**1. The commutation criterion.** For \(v=(a,b,c)\) and \(v'=(a',b',c')\) in \(K^3\), choose lifts in \(L\). Their bracket is
\[
 (ab'-ba')U+(ac'-ca')V+(bc'-cb')W.
\]
Since \(U,V,W\) are \(K\)-linearly independent, the bracket vanishes exactly when the matrix with rows \(v,v'\) has rank at most one over \(K\). In particular two nonzero projected vectors commute exactly when they span the same \(K\)-projective point of \(\mathbb P^2(K)\). This also confirms \(Z(L)=Z\).

**2. Complete abelian-subalgebra classification.** Let \(\pi:L\to L/Z=K^3\). For every projective line \(\ell=K v\subseteq K^3\), define \(M_\ell=\pi^{-1}(\ell)\). The preceding criterion shows \(M_\ell\) is an abelian \(k\)-subalgebra of dimension \(3m\), and \(M_\ell\cap M_{\ell'}=Z\) whenever \(\ell\ne\ell'\). Conversely, for any abelian \(k\)-subalgebra \(A\) with nonzero projection, any two nonzero vectors in \(\pi(A)\) are \(K\)-dependent; hence \(\pi(A)\) lies in one unique \(K\)-line \(\ell\), so \(A\subseteq M_\ell\). If \(\pi(A)=0\), then \(A\subseteq Z\). Therefore the distinct \(M_\ell\) are all maximal abelian subalgebras. The \(P=(Q^3-1)/(Q-1)\) full \(k\)-subspace lattices of the \(M_\ell\) overlap in exactly the entire subspace lattice of \(Z\). Counting each noncentral subspace once gives
\[
 A_d=P{3m\brack d}_q-(P-1){2m\brack d}_q.
\]
Exactly the same disjoint-counting argument on ordered tuples gives \(C_r=P(Q^3)^r-(P-1)(Q^2)^r\), including the empty tuple at \(r=0\).

**3. Complete ideal classification.** We claim that the \(k\)-ideals are exactly:

(i) every \(k\)-subspace \(I\le Z\);

(ii) \(I=Z\oplus T\) for each nonzero \(k\)-subspace \(T\le KU\);

(iii) \(I=D\oplus A\) for each nonzero \(k\)-subspace \(A\le KX\oplus KY\).

The sums are with respect to the displayed coordinate decomposition. Every listed space is an ideal by the bracket relations. Conversely, suppose an ideal \(I\) contains a vector with a nonzero \(X\)- or \(Y\)-coordinate. Taking brackets with all elements of \(KX\oplus KY\) shows that \([L,I]\) projects surjectively to \(KU\) modulo \(Z\). Taking brackets again with \(KX\) and \(KY\) gives all of \(KV\oplus KW=Z\); since \(I\) is an ideal, \(Z\subseteq I\), and then \(KU\subseteq I\). Thus \(D\subseteq I\) and \(I=D\oplus A\) for a nonzero \(k\)-subspace \(A\subseteq KX\oplus KY\). If instead \(I\subseteq D\) but has an element with nonzero \(U\)-coordinate, bracketing it with \(KX\) and \(KY\) forces \(Z\subseteq I\), so \(I=Z\oplus T\) for some nonzero \(T\le KU\). The remaining ideals lie within \(Z\). The classification is disjoint. Counting their dimensions gives \(I_d\) as stated.

Among the maximal abelian \(M_\ell\), the unique one that is an ideal is \(D=M_{K(0,0,1)}\). Indeed \(D\) is abelian. Any other \(M_\ell\) has nonzero \(X\) or \(Y\) component but cannot contain \(D\), since its \(U\)-component projects into a one-dimensional \(K\)-line not equal to \(KU\). By the ideal classification it cannot be an ideal. Every abelian ideal lies in \(D\), since any ideal containing \(D\) properly has nonzero \(X\) or \(Y\) component and does not commute with \(U\).

**4. Automorphism-orbit distinction.** Both \(D=[L,L]\) and \(Z=Z(L)\) are characteristic, so \(D\) is fixed by every \(k\)-Lie automorphism; this gives the singleton orbit. To prove the other projective points form one orbit, use the following explicit automorphisms. Every \(g\in\operatorname{GL}_2(K)\) defines an automorphism by sending \((X,Y)\) to the \(K\)-linear pair \(g(X,Y)\) and sending \(U,V,W\) to the brackets dictated by these generator images. The image of \(U\) is \(\det(g)U\), and the images of \(V,W\) are an invertible linear combination determined by \(g\) and \(\det(g)\); the map is invertible. Moreover, for every \(\alpha,\beta\in K\), the substitution \(X\mapsto X+\alpha U\), \(Y\mapsto Y+\beta U\) extends uniquely to a \(K\)-Lie automorphism and induces \((a,b,c)\mapsto(a,b,c+\alpha a+\beta b)\) on \(L/Z\). Thus the \(\operatorname{GL}_2(K)\) action moves every projective point with \((a,b)\ne(0,0)\) to one with \((a,b)=(1,0)\), and then a suitable shear sets \(c=0\). The orbit of \(M_{K(1,0,0)}\) consists of all \(P-1\) other maximal abelian subalgebras, proving the two-orbit assertion.

## Verification
The accompanying `verify.py` is a standalone Python program using only the standard library. It constructs the bracket directly, tests field multiplication and Jacobi identities, exhaustively enumerates all \(k\)-subspaces in dimensions five over \(\mathbb F_2\) and \(\mathbb F_3\), and independently compares their ideal and abelian conditions with the formulas. For the ten-dimensional example \((q,m)=(2,2)\), it exhaustively enumerates all one- and two-dimensional \(\mathbb F_2\)-subspaces, explicitly checks all \(2^{20}=1,048,576\) ordered element pairs for commutation, checks closure for all \(137\) classified ideals, and verifies the \(21\)-point projective incidence construction and automorphism orbit mechanism. Finite tests corroborate, but do not replace, the argument for arbitrary \(q,m\).

At \((q,m)=(2,2)\), there are exactly \(21\) maximal abelian six-dimensional subalgebras, exactly one of which is an ideal. The abelian-subalgebra counts in dimensions \(0\) through \(10\) are
\[
 (1,1023,12971,28995,13651,1323,21,0,0,0,0),
\]
and ideal counts are
\[
 (1,15,35,15,1,3,1,15,35,15,1).
\]
The number of ordered commuting pairs is \(80896\).

## Relationship to prior work
Kundu, Naik, and Singh [1] classify class-three Lie algebras with two centralizer dimensions over finite fields; their model \(\mathfrak g_m\) is the algebra studied here, and the underlying isomorphism classification is **prior work**, not a new assertion. Their Theorem 1.3 assumes \(q\ge3\); our direct algebraic result on this explicitly defined model also holds at \(q=2\), without claiming their general uniqueness theorem there. Their classification does not give this exact double enumeration of all \(\mathbb F_q\)-linear ideals and abelian subalgebras or the two orbit sizes for maximal abelian subalgebras. Ceballos–Towers [2] study maximal dimensions of abelian subalgebras/ideals, rather than counting these finite-field subspace lattices. Carnevale–Schein–Voll [3] give ideal zeta functions for a broad class of class-two nilpotent Lie rings, which does not cover the class-three scalar restriction in this theorem. Benito–Roldán-López [4] describe automorphism groups of free nilpotent Lie algebras in characteristic zero, without the current finite-field incidence and enumerative claims.

The five-dimensional (\(m=1\)) case is not claimed here. The proposed new scope is \(m\ge2\), where the \(K\)-projective spread in the \(k\)-vector space is essential.

## Limitations
The theorem is restricted to this fixed five-dimensional class-three free Lie algebra over an extension field, viewed over its subfield; it does not classify all class-three nilpotent Lie algebras. The maximum-abelian orbit statement proves precisely two orbits, not the full automorphism group order or stabilizer structure. Publication priority remains provisional, particularly because older general studies of free nilpotent subalgebras may conceal equivalent descriptions. Finite experiments are not an infinite mathematical proof. Independent mathematical audit has not been performed.

## References
[1] R. Kundu, T. K. Naik, A. Singh, *Nilpotent Lie algebras with two centralizer dimensions over a finite field*, arXiv:2208.07676v1 (first public 2022-08-16), https://arxiv.org/abs/2208.07676.

[2] M. Ceballos, D. A. Towers, *On abelian subalgebras and ideals of maximal dimension in supersolvable Lie algebras*, arXiv:1110.2389v1 (2011), https://arxiv.org/abs/1110.2389.

[3] A. Carnevale, M. M. Schein, C. Voll, *Generalized Igusa functions and ideal growth in nilpotent Lie rings*, arXiv:1903.03090v1 (2019), https://arxiv.org/abs/1903.03090.

[4] P. Benito, J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1 (2019), https://arxiv.org/abs/1911.01897.
