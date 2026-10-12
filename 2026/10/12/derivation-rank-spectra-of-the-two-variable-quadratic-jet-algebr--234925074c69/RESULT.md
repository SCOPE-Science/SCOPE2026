# Derivation-rank spectra of the two-variable quadratic jet algebra

## Finding

Let \(q\) be any prime power, let \(k=\mathbb F_q\), and let
\[
A_q=k[X,Y]/(X,Y)^3.
\]
For every \(j\geq 0\), write \(h_q(j)\) for the number of \(k\)-linear derivations \(D:A_q\to A_q\) whose rank as a linear map on the six-dimensional \(k\)-space \(A_q\) is \(j\). The complete rank enumerator is \(H_q(T)=\sum_{j\geq0}h_q(j)T^j\).

Set
\[
P=\frac{(q^2-1)(q^3-1)}{q-1},\qquad
Q=(q^3-1)(q^3-q),\qquad
L=(q-1)(q+1)^2,\qquad
G=(q^2-1)(q^2-q),\qquad
S=q^2(q-1).
\]
When \(q\) is odd, the exact formula is
\[
\boxed{H_q(T)=1+PT+QT^2+Lq^5T^3+
\bigl(L(q-1)q^5+Sq^6\bigr)T^4+(G-S)q^6T^5.}
\]
When \(q\) is even, the exact formula is
\[
\boxed{H_q(T)=1+PT+\bigl(Q+(q-1)q^6+Lq^4\bigr)T^2+
\bigl(L(q^2-1)q^4+(G-q+1)q^6\bigr)T^3.}
\]
All unlisted coefficients are zero, and \(H_q(1)=q^{10}\). In odd characteristic every rank from zero through five occurs; in characteristic two every rank from zero through three occurs and no derivation has rank four or five. Equivalently, a derivation with constants exactly \(k\) exists if and only if the characteristic is odd. In characteristic two, \(1,X^2,Y^2\) are fixed by every derivation.

In particular,
\[
H_2(T)=1+21T+250T^2+752T^3,\qquad
H_3(T)=1+104T+624T^2+7776T^3+28674T^4+21870T^5.
\]
These are counts of derivations, not automorphism orbits or centralizers inside the derivation Lie algebra.

## Assumptions and scope

The result concerns \(k\)-linear Leibniz derivations of the *commutative unital algebra* \(A_q\), considered as ordinary linear operators on \(A_q\). A basis is \((1,x,y,x^2,xy,y^2)\), where \(x,y\) are the residue classes of \(X,Y\). The polynomial \(T\) is a formal indeterminate; its exponent records linear-operator rank. Arbitrary prime powers are allowed, including extension fields. No restriction to nilpotent, semisimple, inner, or homogeneous derivations is imposed.

## Proof

**1. All derivations are parametrized by ten field coordinates.** Write the constant terms of \(D(x)\) and \(D(y)\) as \(u\) and \(v\). The relations \(x^2y=xy^2=0\) imply, respectively, \(2uxy+vx^2=0\) and \(uy^2+2vxy=0\). Linear independence of the quadratic monomials forces \(u=v=0\) in every characteristic. Conversely, arbitrary choices \(D(x),D(y)\in(x,y)\) respect every cubic relation by Leibniz's rule; they therefore define unique derivations. Thus \(\dim_k\operatorname{Der}_k(A_q)=10\).

Write
\[
D(x)=ax+cy+\alpha x^2+\beta xy+\gamma y^2,\qquad
D(y)=bx+dy+\delta x^2+\varepsilon xy+\zeta y^2.
\]
On \((x,y,x^2,xy,y^2)\), the matrix is
\[
M_D=\begin{pmatrix}
a&b&0&0&0\\
c&d&0&0&0\\
\alpha&\delta&2a&b&0\\
\beta&\varepsilon&2c&a+d&2b\\
\gamma&\zeta&0&c&2d
\end{pmatrix}=
\begin{pmatrix}A&0\\ B&T_A\end{pmatrix},
\qquad
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
The first basis element \(1\) lies in the kernel, so the rank of \(D\) equals that of \(M_D\). The \(3\)-square block \(T_A\) is the derivation-induced action of \(A\) on the symmetric square.

**2. Counting the quadratic coefficients at fixed linear part.** Suppose \(s=\operatorname{rank}A\), \(t=\operatorname{rank}T_A\), and put \(d_0=2-s\), \(c_0=3-t\). Quotienting the target by \(\operatorname{im}T_A\) gives
\[
\operatorname{rank}M_D=t+s+j,
\qquad j=\operatorname{rank}\bigl(\overline{B}|_{\ker A}:\ker A\to\operatorname{coker}T_A\bigr).
\]
Here \(B:k^2\to k^3\) is completely unrestricted. For \(0\le j\le\min(d_0,c_0)\), the exact number of such \(B\) is
\[
q^{2t+sc_0} R_q(c_0,d_0,j)
=q^{6-d_0c_0} R_q(c_0,d_0,j),
\]
where \(R_q(c,d,j)={d\brack j}_q\prod_{i=0}^{j-1}(q^c-q^i)\) counts \(c\)-by-\(d\) matrices of rank \(j\), and \({d\brack j}_q\) is the Gaussian binomial coefficient. Indeed, \(\overline B\) has an arbitrary restriction to a complement of \(\ker A\), and every map into the cokernel has exactly \(q^{2t}\) lifts to \(B\).

**3. The linear-part strata.** Directly,
\[
T_A=\begin{pmatrix}2a&b&0\\ 2c&a+d&2b\\ 0&c&2d\end{pmatrix},
\qquad \det T_A=4(a+d)(ad-bc).
\]
There are exactly \(L=(q-1)(q+1)^2\) matrices of rank one in \(M_2(k)\) and \(G=(q^2-1)(q^2-q)\) invertible matrices. If the characteristic is odd, the pairs \((s,t)\) and their multiplicities are:
\[
(0,0):1,\qquad (1,2):L,\qquad (2,2):S,\qquad (2,3):G-S.
\]
For rank-one \(A\), conjugacy reduces to a nonzero diagonal projection or a nonzero nilpotent block; each yields \(\operatorname{rank}T_A=2\). For invertible trace-zero \(A\), the eigenvalues over an algebraic closure are opposite nonzero numbers, so the induced symmetric-square infinitesimal action has rank two. The number of invertible traceless matrices is \(S=q^2(q-1)\): there are \(q^3\) traceless matrices and exactly \(q^2\) singular ones. Invertible matrices of nonzero trace have full-rank \(T_A\).

In characteristic two,
\[
T_A=\begin{pmatrix}0&b&0\\0&a+d&0\\0&c&0\end{pmatrix},
\]
so \(T_A=0\) precisely for scalar \(A\). The pairs \((s,t)\) and multiplicities are then
\[
(0,0):1,\qquad (1,1):L,\qquad (2,0):q-1,\qquad (2,1):G-(q-1).
\]

**4. Assemble ranks.** In both characteristics \(A=0\) contributes \(1\) at rank zero, \(P=R_q(3,2,1)\) at rank one, and \(Q=R_q(3,2,2)\) at rank two. For odd \(q\), the rank-one stratum of \(A\) gives ranks three and four with factors \(q^5\) and \((q-1)q^5\); invertible trace-zero and nonzero-trace matrices add ranks four and five with \(q^6\) choices of \(B\) each. For even \(q\), nonzero scalar \(A\) contributes rank two with \(q^6\) choices of \(B\); rank-one \(A\) contributes ranks two and three with factors \(q^4\) and \((q^2-1)q^4\); nonscalar invertible \(A\) contributes rank three with \(q^6\) choices of \(B\). Substitution gives both displayed enumerators and exhausts all derivations. Since the coefficient sets partition the \(q^4\) possibilities for \(A\), each admitting \(q^6\) possibilities for \(B\), the sum is \(q^{10}\). \(\square\)

## Verification

The self-contained Python program `verify.py` directly constructs each derivation's Leibniz matrix and computes its rank by Gaussian elimination over the field. It exhausts all \(2^{10}=1024\) and \(3^{10}=59049\) derivations over \(\mathbb F_2\) and \(\mathbb F_3\). Separately it enumerates every \(2\)-by-\(2\) linear part and checks the joint \((\operatorname{rank}A,\operatorname{rank}T_A)\) strata over fields of orders \(2,3,4,5\). The \(\mathbb F_4\) implementation uses a polynomial basis with modulus \(t^2+t+1\); further selected quadratic coefficient families over \(\mathbb F_4\) and \(\mathbb F_5\) are checked directly. Polynomial normalization is checked numerically for \(q=2,3,4,5,7,8,9,11\). These finite computations test, but do not replace, the proof for arbitrary prime powers. Run `python3 verify.py` in the directory containing this document.

## Relationship to prior work

Bois [1, Section 1.2] studies derivations and centralizers of \(k[x_1,\ldots,x_m]/(x_1^p,\ldots,x_m^p)\) over an algebraically closed field of characteristic \(p>3\), in the context of generation of Cartan-type Lie algebras. Premet [2, Sections 1--3] studies regular derivations of that *same variablewise-truncated ring* and characterizes regularity using Lie-centralizer and invariant-theoretic criteria. The present algebra is instead truncated by the *total-degree cubic ideal*, and the enumerated rank is the rank of a derivation on the commutative algebra, not its adjoint rank within its Lie algebra. Neither inspected paper gives the displayed finite-field fiber counts. The rank-one and invertible-matrix factors are standard finite linear algebra and are not separately claimed as discoveries.

## Limitations

The result concerns this exact two-variable quadratic-jet algebra, not all truncated polynomial rings or all short local algebras. It does not count isomorphism classes or conjugacy orbits of derivations and does not determine the full Jordan form of each operator. The main proof is algebraic and valid for arbitrary finite fields; exhaustive tests cover only the explicitly named small cases. The literature comparison does not establish globally unique priority: equivalent older formulas under different terminology may exist. No external independent audit or certification has been performed.

## References

1. J.-M. Bois, *Generators of simple Lie algebras II*, arXiv:0806.4496v1, first publicly submitted 27 June 2008; especially Section 1.2. https://arxiv.org/html/0806.4496v1
2. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426, first publicly submitted 10 May 2014; corrected version v3 (22 July 2014), Sections 1--3. https://arxiv.org/html/1405.2426v3
