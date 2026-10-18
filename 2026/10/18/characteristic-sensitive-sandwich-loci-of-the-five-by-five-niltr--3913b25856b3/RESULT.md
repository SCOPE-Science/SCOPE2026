# Characteristic-sensitive sandwich loci of the five-by-five niltriangular Lie algebra

## Finding

Let \(k\) be any field and let \(L=\mathfrak n_5(k)\) be the Lie algebra of strictly upper-triangular \(5\times5\) matrices with bracket \([X,Y]=XY-YX\). Its *sandwich locus* is the reduced algebraic set
\[
\mathcal S_k=\{X\in L:\operatorname{ad}_X^2(Y)=[X,[X,Y]]=0\text{ for every }Y\in L\}.
\]
The geometry changes sharply with the characteristic. If \(\operatorname{char}k=2\), the geometric irreducible components over an algebraic closure are **three** varieties, each of dimension \(7\); two are irreducible determinant-quadric cones times affine space and the third is linear. If \(\operatorname{char}k\ne2\), there are **five** components, all linear: three of dimension \(6\), two of dimension \(5\).

For every finite field \(k=\mathbb F_q\), the exact number of sandwich elements is
\[
|\mathcal S_k(k)|=\begin{cases}
3q^7-q^6-q^5,&\operatorname{char}k=2,\\
3q^6-2q^4,&\operatorname{char}k\ne2.
\end{cases}
\]
Thus the maximal component dimension jumps from \(6\) in odd characteristic to \(7\) in characteristic two. The statement concerns the **reduced set**, not reducedness or primary decomposition of the scheme cut out by the adjoint-square equations.

## Assumptions and scope

Use independent matrix entries
\[
X=\begin{pmatrix}
0&a&b&c&d\\0&0&e&f&g\\0&0&0&h&i\\0&0&0&0&j\\0&0&0&0&0
\end{pmatrix}.
\]
All coordinate equations and irreducible-component claims hold over any field after extending to an algebraic closure. The coordinates \(c,d,g\) are unrestricted throughout. Here *dimension* means geometric Krull dimension of a reduced affine algebraic set; an irreducible component is maximal among irreducible closed subsets.

In characteristic two, the three components are exactly
\[
\begin{aligned}
C_1&=V(e,j,af+bh),\\
C_2&=V(a,h,ei+fj),\\
C_3&=V(e,f,h).
\end{aligned}
\]
In other characteristics, the five components are exactly
\[
\begin{aligned}
D_1&=V(a,b,e,j),\\
D_2&=V(a,h,e,j),\\
D_3&=V(a,h,i,j),\\
D_4&=V(e,f,h,i,j),\\
D_5&=V(a,b,e,f,h).
\end{aligned}
\]
Here \(V(\cdots)\) denotes the common zero locus of its displayed polynomials in the ten matrix-entry coordinates.

## Proof

For a matrix unit \(E_{rs}\), \([X,E_{rs}]\) is computed from the \(r\)-th column and the \(s\)-th row of \(X\). Applying this operation twice to all ten units \(E_{rs}\) with \(1\le r<s\le5\), and removing duplicated entries and irrelevant signs, gives the following complete collection of adjoint-square coefficient equations:
\[
ae=0,\quad af+bh=0,\quad eh=0,\quad ei+fj=0,\quad hj=0,
\]
\[
2ah=0,\quad2ai=0,\quad2aj=0,\quad2bj=0,\quad2ej=0.
\]
These equations are *equivalent* to \(\operatorname{ad}_X^2=0\) because each coefficient of each output matrix unit vanishes if and only if the linear operator vanishes on the matrix-unit basis. They use no characteristic restrictions, and \(c,d,g\) do not appear.

**Characteristic two.** The five equations in the first display suffice. If \(h\ne0\), \(eh=hj=0\) implies \(e=j=0\); the remaining equation is \(af+bh=0\), giving a point of \(C_1\). If \(h=0\) but \(a\ne0\), the equations \(ae=0\) and \(af+bh=0\) force \(e=f=0\), giving a point of \(C_3\). If \(h=a=0\), the only surviving constraint is \(ei+fj=0\), giving a point of \(C_2\). Conversely every point of these three varieties satisfies all five equations, so their union is the entire reduced sandwich locus.

Both \(af+bh\) and \(ei+fj\) are irreducible polynomials over an algebraic closure: they are the determinants of generic \(2\times2\) matrices (in characteristic two, the determinant's minus sign equals plus), and a rank-two determinantal hypersurface is irreducible. Hence \(C_1\) and \(C_2\) are geometrically irreducible of dimension \(7\), and \(C_3\) is affine-linear of dimension \(7\). None is contained in another: generic points with \(h\ne0\) distinguish \(C_1\), generic points with \(e\ne0\) distinguish \(C_2\), and points with \(a\ne0\), \(j\ne0\), \(e=f=h=0\) distinguish \(C_3\). Thus they are exactly the three irreducible components.

**Odd characteristic.** The last five equations also imply \(ah=ai=aj=bj=ej=0\). If \(h\ne0\), then \(a=e=j=0\), and \(af+bh=0\) forces \(b=0\), giving \(D_1\). If \(h=0\), \(a\ne0\), then \(e=f=i=j=0\), giving \(D_4\). If \(a=h=0\), \(j\ne0\), the constraints imply \(b=e=f=0\), giving \(D_5\). In the remaining case \(a=h=j=0\), the only constraint is \(ei=0\); its two branches \(e=0\) and \(i=0\) give \(D_2\) and \(D_3\). All five displayed linear subspaces satisfy the original equations. They are pairwise non-contained and therefore are precisely the geometric components, of respective dimensions \(6,6,6,5,5\).

**Finite-field enumeration.** Let \(q=|k|\). In characteristic two, split the seven constrained coordinates into disjoint cases \(h\ne0\), \(h=0,a\ne0\), and \(h=a=0\). Including the three free coordinates, the first two cases contribute \((q-1)q^6\) each. In the third, the number of solutions of \(ei+fj=0\) in four variables equals \(q^3+q^2-q\): for the coefficient vector \((e,f)=0\) there are \(q^2\) choices of \((i,j)\), whereas each of the \(q^2-1\) nonzero coefficient vectors has \(q\) solutions. The remaining free coordinates contribute \(q^4\). Hence
\[
2(q-1)q^6+q^4(q^3+q^2-q)=3q^7-q^6-q^5.
\]
For odd characteristic use the disjoint cases \(h\ne0\), \(h=0,a\ne0\), \(h=a=0,j\ne0\), and \(h=a=j=0\). They contribute respectively \((q-1)q^5\), \((q-1)q^4\), \((q-1)q^4\), and \(q^5(2q-1)\), since \(ei=0\) has \(2q-1\) solutions. Their sum is \(3q^6-2q^4\). This also establishes the formulas for all prime powers, without assuming a prime field.

## Verification

The standalone \(\texttt{verify.py}\) uses only Python's standard library and can be replayed by executing `python3 verify.py`. It independently forms each \(10\times10\) adjoint matrix on the standard matrix-unit basis and tests the vanishing of its square. It also directly enumerates the seven relevant coordinates and compares the explicit component-membership predicates to the operator-derived equations over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). The degree-two model for \(\mathbb F_4\) uses \(u^2+u+1=0\). It verifies the cardinalities \(288,2025,44032,45625\), respectively, and checks all \(1024\) binary matrices at the adjoint-operator level; for each other listed field it checks \(2048\) deterministic matrices at that level. These are independent finite corroborations, not proofs for arbitrary fields.

## Relationship to prior work

Cohen, Ivanyos and Roozemond (2007) call elements satisfying \(\operatorname{ad}_X^2=0\) *sandwiches*, but study extremal elements and generation in simple Lie algebras, not the explicit sandwich geometry of the solvable algebra \(\mathfrak n_5\), particularly not characteristic two. The triangular-similarity classification of Tsai, Bogale and Huang (2020), building on five-by-five canonical forms studied by Kobal (2005), concerns conjugacy orbits of nilpotent triangular matrices. It is relevant background but does not itself state the five-versus-three component description or the finite-field point counts. These are not merely counts of conjugacy orbits: they are equations and irreducible components of a different invariant closed locus.

## Limitations

Only the reduced geometric loci and their \(\mathbb F_q\)-rational cardinalities are classified; the scheme defined by the quadratic operator equations is not claimed to be reduced or equidimensional as a scheme. The result is specific to the five-by-five niltriangular Lie algebra, not all strictly upper-triangular sizes. No claim is made that the finite-field formulas alone settle the entire conjugacy classification. A previously unpublished or inaccessible treatment of five-by-five upper-triangular orbit geometry could in principle contain these facts; the 2005 article was available only through its bibliographic abstract and indirect citations, not primary full text.

## References

1. A. M. Cohen, G. Ivanyos and D. A. Roozemond, *Simple Lie Algebras having Extremal Elements* (first public arXiv posting 2007-11-27), https://arxiv.org/abs/0711.4268.
2. M.-C. Tsai, M. Bogale and H. Huang, *On triangular similarity of nilpotent triangular matrices* (first public arXiv posting 2020-02-24), https://arxiv.org/abs/2002.10088.
3. D. Kobal, *Belitskii's canonical form for 5×5 upper triangular matrices under upper triangular similarity*, Linear Algebra Appl. (2005), https://doi.org/10.1016/j.laa.2005.01.028 (abstract-level comparison; full text not obtained).
