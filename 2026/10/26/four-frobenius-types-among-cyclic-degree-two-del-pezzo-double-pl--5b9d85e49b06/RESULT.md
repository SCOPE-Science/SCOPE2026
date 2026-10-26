# Four Frobenius types among cyclic degree-two del Pezzo double planes over the two-element field

## Finding
Over \(k=\mathbb F_2\), set
\[
q=xy+xz+yz,\quad A=x^4+y^4+z^4,\quad B=x^3y+y^3z+z^3x,
\]
\[
C=x^3z+y^3x+z^3y,\quad D=x^2y^2+y^2z^2+z^2x^2=q^2,\quad E=xyz(x+y+z).
\]
Consider the complete five-dimensional space of cyclically invariant quartic terms and the associated 32 weighted double planes
\[
S_{a,b,c,d,e}:\quad w^2+qw+aA+bB+cC+dD+eE=0\quad\subset\mathbb P_k(1,1,1,2),
\]
with all coefficients in \(\mathbb F_2\). The coordinates \(x,y,z\) have weight one and \(w\) weight two. Every surface carries the coordinate-cycle action \([x:y:z:w]\mapsto[y:z:x:w]\).

**Classification.** The surface is geometrically smooth exactly when
\[
e=a,\qquad (b+a,c+a)\ne(0,0).
\]
Thus 12 of the 32 equations are smooth degree-two del Pezzo surfaces. They represent precisely four \(\mathbb F_2\)-isomorphism classes. For each class the following table gives the quartic term in a representative, the characteristic polynomial \(P(T)=\det(T-\operatorname{Frob}|\operatorname{Pic}(S_{\bar k}))\), the number \(N_1=\#S(\mathbb F_2)\), and the rank \(\rho_k=\operatorname{rank}\operatorname{Pic}(S)\):

| Quartic term | \(P(T)\) | \(N_1\) | \(\rho_k\) |
|---|---|---:|---:|
| \(B\) (also \(C\)) | \((T-1)(T+1)(T^2-T+1)(T^2+T+1)^2\) | 3 | 1 |
| \(B+C\) | \((T-1)^4(T+1)^2(T^2-T+1)\) | 11 | 4 |
| \(B+D\) (also \(C+D\)) | \((T-1)^2(T^2-T+1)^2(T^2+T+1)\) | 11 | 2 |
| \(B+C+D\) | \((T-1)^3(T+1)^3(T^2+T+1)\) | 3 | 3 |

The four polynomials are distinct, so the four representatives are pairwise nonisomorphic over \(\mathbb F_2\). In particular, the two three-point surfaces have different arithmetic Picard ranks (one and three), and the two eleven-point surfaces also have different arithmetic Picard ranks (four and two). For every \(n\ge1\), writing \(p_n\) for the sum of the \(n\)th powers of the eight roots of the table's polynomial,
\[
\#S(\mathbb F_{2^n})=1+4^n+2^n p_n,\qquad
Z(S/\mathbb F_2,t)=\frac{1}{(1-t)(1-4t)\det(1-2t\operatorname{Frob}|\operatorname{Pic})}.
\]

## Assumptions and scope
The coefficient field is exactly \(\mathbb F_2\). All smoothness claims are geometric, i.e. over an algebraic closure. The classification concerns the explicitly normalized family with fixed nonsingular branch conic \(q=0\) and an invariant quartic term under the coordinate three-cycle; it is not a classification of all del Pezzo surfaces over \(\mathbb F_2\). The arithmetic Picard rank means the rank of divisors defined over the base field, equivalently the multiplicity of the eigenvalue one on the geometric Picard group over a finite field.

## Proof
**1. Exhaustion and coordinate equivalence.** The cyclic permutation acts freely on the fifteen degree-four monomials in three variables; there are five three-element orbits, with sums \(A,B,C,D,E\). This proves that all cyclically invariant quartic terms occur in the displayed family. In characteristic two put \(r=(x+y+z)^2\). The weighted coordinate substitution \(w\mapsto w+r\) transforms the quartic term by
\[
r^2+qr=A+B+C+E.
\]
It therefore toggles \((a,b,c,e)\) simultaneously, leaving \(d\) unchanged; every member is isomorphic over \(\mathbb F_2\) to one with \(a=0\). Switching \(y,z\) exchanges \(B,C\) and preserves \(q,D,E\). Over \(\mathbb F_4\), the substitution \(w\mapsto w+\alpha q\), where \(\alpha^2+\alpha=1\), toggles \(d\). It proves that geometric smoothness is independent of \(d\) and identifies this toggle as the Geiser twist over \(\mathbb F_2\).

**2. Geometric smoothness.** Write \(f=aA+bB+cC+dD+eE\). The weighted surface avoids the ambient singular point and has derivative \(\partial_w(w^2+qw+f)=q\), so every singular point lies over the smooth conic \(q=0\). The conic admits the homogeneous parametrization
\[
[x:y:z]=[u(u+v):v(u+v):uv].
\]
After normalizing \(a=0\), at each of the endpoints \([1:0:0]\) and \([0:1:0]\) there is a singular point exactly if \(b=c=0\). On \(u\ne0\), put \(t=v/u\) and
\[
(x,y,z)=(1+t,t+t^2,t),\quad P(t)=f(1+t,t+t^2,t),\quad G(t)=\partial_x f(1+t,t+t^2,t).
\]
For \(t\ne0\), \(q_x=t^2\). The tangent and normal derivative equations and the defining equation together show that there is a singular point over a given \(t\) if and only if
\[
P'(t)=0,\qquad G(t)^2+t^4P(t)=0.
\]
Because the base field is algebraically closed for this test, the two univariate polynomials have no common *nonzero* root precisely when their gcd is a nonzero power of \(t\). In the following table, \(g_{bce}(t)\) denotes their gcd after \(a=d=0\); the \(d\)-term does not enter because \(D=q^2\) vanishes with its first derivatives along the conic:

| \((b,c,e)\) | \(g_{bce}(t)\) |
|---|---|
| \((0,0,0)\) | zero polynomial |
| \((0,0,1)\) | \(t^2(t+1)^2\) |
| \((0,1,0)\) | \(1\) |
| \((0,1,1)\) | \((t^3+t+1)^2\) |
| \((1,0,0)\) | \(1\) |
| \((1,0,1)\) | \((t^3+t^2+1)^2\) |
| \((1,1,0)\) | \(t^2\) |
| \((1,1,1)\) | \(t^4(t^2+t+1)^4\) |

All gcds are computed by exact Euclidean polynomial division in \(\mathbb F_2[t]\), not by testing finitely many field points. The endpoint condition excludes the two cases with \(b=c=0\); the remaining cases show that smoothness holds exactly when \(e=0\) and \((b,c)\ne(0,0)\) for normalized \(a=0\). Undoing the coordinate change gives the stated criterion \(e=a\) and \((b+a,c+a)\ne(0,0)\), and counts twelve smooth coefficient vectors.

**3. Complete point counts, not merely finite evidence.** Fix any of the six normalized smooth quartics \(B,C,B+C,B+D,C+D,B+C+D\) and put \(K=\mathbb F_{2^n}\). For each \(Q\in\mathbb P^2(K)\), the equation in \(w\) has one solution if \(q(Q)=0\). If \(q(Q)\ne0\), write \(s=w/q(Q)\); the equation becomes \(s^2+s=f(Q)/q(Q)^2\), which has two solutions exactly when
\[
\operatorname{Tr}_{K/\mathbb F_2}\big(f(Q)/q(Q)^2\big)=0
\]
and otherwise none. Exhaustively evaluating all normalized projective points of \(\mathbb P^2(K)\) gives the following exact \(p_n=(\#S(K)-1-4^n)/2^n\), for \(n=1,\ldots,8\):

| Quartic term | \((p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8)\) |
|---|---|
| \(B\) or \(C\) | \((-1,-1,2,-1,-1,8,-1,-1)\) |
| \(B+C\) | \((3,5,0,5,3,8,3,5)\) |
| \(B+D\) or \(C+D\) | \((3,-1,0,-1,3,8,3,-1)\) |
| \(B+C+D\) | \((-1,5,2,5,-1,8,-1,5)\) |

Every smooth degree-two del Pezzo surface is geometrically a blowup of \(\mathbb P^2\) in seven points in general position, so its geometric Picard group has rank eight and its entire second étale cohomology is algebraic. The Grothendieck trace formula gives \(p_n=\operatorname{tr}(\operatorname{Frob}^n|\operatorname{Pic}(S_{\bar k}))\). The first eight exact traces determine the monic degree-eight characteristic polynomial *uniquely* by Newton's identities. Those computations produce precisely the four displayed factorizations. Unlike extrapolation from point-count data, this step proves the formula for every extension degree \(n\), relying on the rank-eight geometric theorem. The multiplicities of \(T-1\) give the stated arithmetic Picard ranks.

**4. Isomorphism classes.** The change \(w\mapsto w+r\) pairs the twelve smooth coefficients into six normalized representatives, and switching \(y,z\) pairs \(B\) with \(C\) and \(B+D\) with \(C+D\). This gives at most four classes; their four distinct Frobenius characteristic polynomials are invariants under \(\mathbb F_2\)-isomorphism, so at least four classes occur. Hence there are exactly four.

## Verification
Run the included, dependency-free Python 3 file `del_pezzo_cyclic_verifier.py`. It checks the quartic orbit basis and the weighted translation identity, computes each Euclidean gcd as an exact polynomial identity over \(\mathbb F_2[t]\), exhausts the 32 smoothness cases algebraically, and counts points over the eight extensions of degree \(1\) through \(8\) by field-trace arithmetic. The verifier checks every nonzero finite-field element for an inverse, independently checks the smallest three fields by direct solution of the equation in \(w\), and computes the degree-eight characteristic polynomial using Newton identities. Its output ends with `VERIFY_OK: 32 cyclic models, 12 smooth, 4 zeta types; fields degrees 1..8 and low-degree direct lifts`. The general smoothness and all-extension zeta conclusions additionally use the explicit geometric reasoning and known structural theorem explained in the proof; the finite check alone is not treated as an infinite proof.

## Relationship to prior work
Festi and van Luijk (first preprint 2014) establish unirationality of degree-two del Pezzo surfaces over finite fields and the relevant characteristic-two weighted-double-plane framework. Their theorem concerns unirationality rather than classification of this cyclic coefficient space. Knecht and Reyes (2015) investigate the much stronger condition that all rational points lie on exceptional curves of *split* degree-two surfaces, not this restricted symmetry-family count. Banwait, Fité and Loughran (2016) study possible Frobenius traces of del Pezzo surfaces; such existence/trace classifications do not determine which coefficient vectors of the displayed family are smooth nor their full characteristic polynomials. Loughran and Trepalin (2018) classify which Weyl-group conjugacy types occur over finite fields, including \(\mathbb F_2\), but do not enumerate this explicit 32-model cyclic family or assign a Frobenius polynomial to each smooth member. The 2022 quantitative Frobenius study by Bergvall explicitly concerns odd characteristic. The present assertion is the joint explicit smoothness, isomorphism and arithmetic classification *within the specified characteristic-two invariant family*, not a new existence theorem for Frobenius types or a new unirationality theorem.

## Limitations
The family fixes the branch conic \(q=0\) and the specified coordinate three-cycle. Its four classes should not be interpreted as all degree-two del Pezzo surfaces over \(\mathbb F_2\), or even as all surfaces admitting an order-three automorphism after arbitrary change of coordinates. A broader moduli-theoretic classification and automorphism-group census are not proved. Related finite-field classification papers may contain equivalent descriptions under another choice of coordinates or Weyl-group notation; the literature search does not prove global uniqueness. No independent scientific audit has been performed.

## References
1. D. Festi and R. van Luijk, *Unirationality of del Pezzo surfaces of degree two over finite fields (extended version)*, first posted 2014-08-01, arXiv:1408.0269, https://arxiv.org/abs/1408.0269. Shorter version arXiv:1505.01145, first posted 2015-05-05.
2. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, first posted 2015-10-15, arXiv:1510.04621, https://arxiv.org/abs/1510.04621.
3. B. Banwait, F. Fité and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, first posted 2016-06-01, arXiv:1606.00300, https://arxiv.org/abs/1606.00300.
4. D. Loughran and A. Trepalin, *Inverse Galois problem for del Pezzo surfaces over finite fields*, first posted 2018-11-16, arXiv:1811.06785, https://arxiv.org/abs/1811.06785; especially §1.2 and §3.
5. O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, first posted 2022-11-23, arXiv:2211.12855, https://arxiv.org/abs/2211.12855.
