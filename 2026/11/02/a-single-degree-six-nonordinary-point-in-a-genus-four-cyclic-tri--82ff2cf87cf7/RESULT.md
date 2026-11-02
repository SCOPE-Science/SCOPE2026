# A single degree-six nonordinary point in a genus-four cyclic-triple-cover pencil in characteristic five

## Finding
Let \(k\) be an algebraic closure of \(\mathbb F_5\). For \(\lambda\in k\), let \(C_\lambda\subset\mathbb P^3_k\) be the complete intersection
\[
 XW-YZ=0,\qquad X^3+Y^3+Z^3+W^3+\lambda XZW=0.
\]
It is smooth precisely when \(\lambda\ne0\) and \(\lambda^3\ne1\). On this parameter domain it is a nonhyperelliptic curve of genus four. Put
\[
 D(\lambda)=\lambda^6+2\lambda^3-1\in\mathbb F_5[\lambda].
\]
Its Jacobian has \(5\)-rank \(4\) and \(a\)-number \(0\) when \(D(\lambda)\ne0\), and \(5\)-rank \(3\) and \(a\)-number \(1\) when \(D(\lambda)=0\). The polynomial \(D\) is irreducible and separable over \(\mathbb F_5\); hence the nonordinary parameters are precisely six geometric points forming one Frobenius orbit of length six (one reduced closed point of degree six). None lies on the singular boundary.

Every smooth member has a fixed-point-free order-three automorphism and an étale cyclic triple cover of a genus-two curve
\[
 H_\lambda:\quad V^2=(r^3+\lambda r+1)^2-4r^3.
\]
The quotient has \(5\)-rank \(2\) generically and \(1\) on the six-point exceptional locus, with corresponding \(a\)-numbers \(0\) and \(1\); the two-dimensional Prym factor remains ordinary for every smooth parameter.

## Assumptions and scope
All geometric assertions are over \(k=\overline{\mathbb F}_5\). Rank means the geometric \(5\)-rank of the Jacobian; the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,\operatorname{Jac}(C)[5])\). A closed point of parameter space refers to the affine \(\lambda\)-line over \(\mathbb F_5\) with \(\lambda(\lambda^3-1)\ne0\). Parameter values are not asserted to label pairwise nonisomorphic curves.

## Proof
**1. Smoothness and genus.** On the smooth quadric \(XW-YZ=0\), use the Segre coordinates \([s:t],[u:v]\), with \((X,Y,Z,W)=(su,sv,tu,tv)\). The cubic restricts to the bidegree-\((3,3)\) equation
\[
 (s^3+t^3)(u^3+v^3)+\lambda st^2u^2v=0.
\]
The boundary divisors \(s=0,t=0,u=0,v=0\) contain no singularities when \(\lambda\ne0\), directly by partial differentiation (on those divisors the relevant cubic factors have simple roots, since \(3\) is invertible). On \(t=v=1\), write \(f(s,u)=(s^3+1)(u^3+1)+\lambda su^2\). At a singular point with \(s,u\ne0\), \(f=sf_s=uf_u=0\) and \(s^3+1,u^3+1\ne0\). These equations give \(s^3=3\), \(u^3=2\), \(\lambda su^2=3\) in characteristic five; cubing forces \(\lambda^3=1\). Conversely, when \(\lambda^3=1\) the indicated roots can be chosen to satisfy all equations, giving singularities. At \(\lambda=0\) the bidegree polynomial factors. Thus exactly the stated parameter domain is smooth. Adjunction on \(\mathbb P^1\times\mathbb P^1\) gives genus \((3-1)(3-1)=4\).

**2. The genus-four Hasse–Witt matrix.** With the canonical basis of \(H^0(C_\lambda,\omega_{C_\lambda})\) indexed by \(X,Y,Z,W\), the standard complete-intersection coefficient-extraction rule for \((QG)^{5-1}\), where \(Q=XW-YZ\) and \(G=X^3+Y^3+Z^3+W^3+\lambda XZW\), yields (up to the standard dual/transposition convention)
\[
 A_\lambda=\begin{pmatrix}
 0&0&0&1\\
 0&\lambda^2&1-\lambda^3&0\\
 0&1&\lambda^4+\lambda&0\\
 1&0&0&0
 \end{pmatrix}.
\]
Specifically, the \((i,j)\) entry is the coefficient of \(\prod_{m=1}^4 x_m^{5v_{j,m}-v_{i,m}}\) in \((QG)^4\), where \(v_i=(1,\ldots,2,\ldots,1)\) has \(2\) in position \(i\). Direct multiplication gives
\[
 \det A_\lambda=-\bigl(\lambda^6+2\lambda^3-1\bigr).
\]
At \(D\ne0\), the matrix is invertible, hence the curve is ordinary. At \(D=0\), it has rank three: two dimensions form the constant invertible outer block, and the middle block
\[
 B=\begin{pmatrix}\lambda^2&1-\lambda^3\\1&\lambda^4+\lambda\end{pmatrix}
\]
has rank one. For its column \(v=(\lambda^2,1)^t\), a direct calculation modulo \(D\) gives
\[
 Bv^{(5)}=\lambda(\lambda^3-1)v\ne0.
\]
Therefore the stable Frobenius-semilinear rank of \(B\) is one (not zero): the full stable rank is three. The Cartier/Hasse–Witt rank is three, so the \(a\)-number is one.

**3. Exactly one exceptional closed point.** The polynomial \(D\) is monic of degree six. Polynomial Euclidean arithmetic over \(\mathbb F_5\) verifies
\[
 \gcd(D,\lambda^{5^j}-\lambda)=1\quad(j=1,2,3),
 \qquad D\mid(\lambda^{5^6}-\lambda).
\]
Consequently \(D\) is irreducible of degree six, and hence separable. The six roots are a single Frobenius orbit. Since \(D(0)=-1\) and \(D\) is coprime to \(\lambda^3-1\), every root lies in the smooth parameter domain. Over \(\mathbb F_{5^m}\), exceptional parameter values exist exactly when \(6\mid m\), in which case there are exactly six.

**4. Triple cover, quotient and Prym.** Choose a primitive cube root \(\zeta\) in \(k\). The automorphism \([s:t],[u:v]\mapsto[\zeta s:t],[\zeta u:v]\) preserves the bidegree equation and has potential fixed points only at the four corners \((s,t),(u,v)\in\{[0:1],[1:0]\}\), none of which lies on the curve. Thus the quotient is an unramified cyclic cover of degree three; Riemann–Hurwitz gives quotient genus two. On \(t=v=1\), the invariant functions \(r=s/u\) and \(z=u^3\) satisfy
\[
 r^3z^2+(r^3+\lambda r+1)z+1=0.
\]
Setting \(V=2r^3z+r^3+\lambda r+1\) gives the stated hyperelliptic model of \(H_\lambda\). The genus-two Hasse–Witt extraction from the square of its sextic right-hand side gives
\[
 A^{(2)}_\lambda=\begin{pmatrix}\lambda^4+\lambda&1-\lambda^3\\1&\lambda^2\end{pmatrix},
\quad\det A^{(2)}_\lambda=D(\lambda).
\]
At roots of \(D\), its semilinear square is nonzero, so its stable rank is one. Else it has stable rank two. Finally, the norm/pullback decomposition for this étale degree-three cover gives an isogeny of degree prime to five between \(\operatorname{Jac}(C_\lambda)\) and \(\operatorname{Jac}(H_\lambda)\times\operatorname{Prym}(C_\lambda/H_\lambda)\). Additivity of \(5\)-rank forces the dimension-two Prym to have rank two at all smooth parameters, hence to be ordinary.

## Verification
Run `python3 verify_canonical.py` and `python3 verify_quotient.py` in a directory containing these two standalone files. Both use only Python's standard library. The first exactly expands \((QG)^4\) over \(\mathbb F_5[\lambda]\) and verifies every matrix entry and its determinant. The second independently expands the genus-two hyperelliptic polynomial, verifies its Hasse–Witt matrix and determinant, proves irreducibility by polynomial gcd/exponentiation, and checks the Frobenius-semilinear rank at all six conjugate exceptional parameters in the quotient field. These finite symbolic identities underpin the stated uniform conclusions; no finite-sample extrapolation is used.

## Relationship to prior work
The canonical genus-four \((2,3)\)-complete-intersection form and Hasse–Witt coefficient-extraction criterion are standard and appear explicitly in Kudo–Harashita (2017). Camacho-Navarro (2020) studies genus-four \(p\)-rank and \(a\)-number configurations more generally. Bruin–Flynn–Shnidman (2021) treat genus-two curves with cubic torsion structures, which provides a related perspective on étale cyclic triple covers; their moduli question does not state the explicit characteristic-five stratification proved here. The novelty claim is restricted to this particular symmetric pencil's complete ordinary/nonordinary classification, one degree-six exceptional closed point, and the everywhere-ordinary Prym factor. General algorithms, the canonical model, and the triple-cover isogeny principle are not new claims.

## Limitations
This is a statement about one explicitly defined pencil, not all genus-four curves or all cyclic cubic covers. The six parameters may yield fewer geometric isomorphism classes; no assertion of parameter-injective moduli is made. The source survey and mathematical-record searches do not establish exhaustive global priority, and an unindexed prior calculation may exist.

## References
- M. Kudo and S. Harashita, *Enumerating superspecial curves of genus 4 over prime fields*, arXiv:1702.05313 (first public version 2017-02-17), especially §2.1 on complete-intersection Hasse–Witt coefficients. https://arxiv.org/abs/1702.05313
- C. Camacho-Navarro, *The a-number, p-rank and Cartier points of genus 4 curves*, arXiv:2012.08705 (2020). https://arxiv.org/abs/2012.08705
- N. Bruin, E. V. Flynn and A. Shnidman, *Genus two curves with full \(\sqrt3\)-level structure and Tate–Shafarevich groups*, arXiv:2102.04319 (2021). https://arxiv.org/abs/2102.04319
