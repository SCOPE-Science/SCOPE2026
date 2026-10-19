# A non-equidimensional characteristic-two Jordan-plane representation variety and its rational orbits

## Finding
For a field \(k\), define the Jordan plane \(R=k\langle u,v\rangle/(uv-vu-v^2)\). Its two-dimensional representation locus is the set of pairs of matrices
\[
\mathcal R_2(k)=\{(X,Y)\in M_2(k)^2:XY-YX=Y^2\}.
\]
All geometric assertions below concern the **reduced** algebraic set over an algebraically closed field of characteristic two; no scheme-theoretic radicality of the originally presented ideal is asserted.

**Geometric theorem.** The reduced set has precisely two irreducible components, of dimensions four and five. The four-dimensional component is \(A=\{Y=0\}\). The five-dimensional component is
\[
B=\{(X,Y):\operatorname{tr}X=\operatorname{tr}Y=0,\ XY-YX=Y^2\}.
\]
The intersection \(A\cap B=\{Y=0,\operatorname{tr}X=0\}\) is a three-dimensional linear space. The singular locus of the **component \(B\)** is the one-dimensional line \(\{(aI_2,0):a\in k\}\). In particular, the reduced representation variety is **not equidimensional**.

**Finite-field orbit theorem.** For each \(q=2^f\), \(f\ge1\), simultaneous conjugacy under \(\mathrm{GL}_2(\mathbb F_q)\) has exactly
\[
\boxed{q^2+q\quad+\quad q^2\quad+\quad q(q-1)\;=\;3q^2}
\]
orbits. The three summands correspond to \(Y=0\), nonzero nilpotent \(Y\), and invertible \(Y\), respectively. The latter two types have respective orbit sizes \(q^2-1\) and \(q(q^2-1)\). The original finite-field **labeled point-count formula** is not claimed as new; it is included below only as a consistency check.

## Assumptions and scope
The matrix commutator means \([X,Y]=XY-YX\), where subtraction equals addition in characteristic two. For geometry, \(k\) is algebraically closed of characteristic two. For arithmetic, \(k=\mathbb F_{2^f}\). Representation isomorphism means a single change of basis conjugating both \(X\) and \(Y\); algebra automorphisms of the Jordan plane are **not** factored out. The reduced geometric locus is distinguished from its possibly nonreduced representation scheme.

## Proof
Write
\[
X=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
Y=\begin{pmatrix}e&f\\g&h\end{pmatrix}.
\]
Taking the trace of \([X,Y]=Y^2\) gives \((e+h)^2=0\), hence \(h=e\) over a field. Put \(s=a+d\). Direct multiplication reduces the remaining equations to
\[
fs=gs=0,\qquad F:=e^2+fg+bg+cf=0.
\]
If \((f,g)=(0,0)\), the last equation gives \(e=0\) and therefore \(Y=0\). Otherwise \(s=0\). Conversely every pair on \(A=\{Y=0\}\) or on \(B=\{s=0,h=e,F=0\}\) solves the equation. This proves the asserted **set-theoretic** decomposition of the reduced locus.

The component \(A\) is an affine four-space. The component \(B\) has coordinates \((a,b,c,e,f,g)\) subject to the single equation
\[
F=fc+e^2+g(b+f)=0.
\]
The polynomial is irreducible over every extension of \(\mathbb F_2\): viewed as degree one in \(c\) over the UFD \(k[a,b,e,f,g]\), its leading coefficient \(f\) is relatively prime to \(e^2+g(b+f)\), since reduction modulo \(f\) gives the nonzero polynomial \(e^2+bg\). Gauss's lemma therefore makes \(F\) irreducible in the polynomial ring. Thus \(B\) is an irreducible five-dimensional hypersurface. Neither \(A\subseteq B\) (take \(Y=0\) with nonzero trace \(X\)) nor \(B\subseteq A\) (take nonzero \(Y\)); hence they are precisely the two irreducible components. Their intersection has equations \(Y=0\) and \(s=0\), so has dimension three.

The partial derivatives of \(F\) in \((a,b,c,e,f,g)\) are
\[
(0,g,f,0,c+g,b+f).
\]
They all vanish on \(F=0\) exactly when \(b=c=e=f=g=0\), with \(a\) arbitrary. This gives the stated singular locus of \(B\) by the Jacobian criterion over the perfect field \(k\).

For the orbit theorem, fix \(k=\mathbb F_q\). Cayley--Hamilton and \(\operatorname{tr}Y=0\) show \(Y^2=(\det Y)I_2\). There is a unique \(\lambda\in k\) with \(\lambda^2=\det Y\). Put \(N=Y+\lambda I_2\). Then \(N^2=0\). If \(N=0\), the equation forces \(\lambda=0\), giving \(Y=0\). Otherwise \(N\) is nonzero rank-one nilpotent, conjugate to \(E_{12}\), and in that basis the complete set of solutions is
\[
Y=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},\qquad
X=\begin{pmatrix}a&b\\\lambda^2&a\end{pmatrix},\qquad a,b,\lambda\in k.
\]
The invertible centralizer of \(E_{12}\) comprises \(uI_2+vE_{12}\), with \(u\ne0\). Writing \(t=v/u\), its conjugation action on the displayed \(X\) is
\[
(a,b)\longmapsto(a+t\lambda^2,\ b+t^2\lambda^2).
\]
If \(\lambda=0\), this action is trivial, producing \(q^2\) orbits indexed by \((a,b)\); each has size \(q^2-1\), the size of the conjugacy orbit of \(E_{12}\). If \(\lambda\ne0\), the action is free and the complete invariant is
\[
\mu=a^2+\lambda^2b,
\]
which is the scalar defined by \(X^2=\mu I_2\). For each of the \(q-1\) nonzero values of \(\lambda\) and each \(\mu\in k\), there is exactly one orbit, represented by
\[
Y=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix},\qquad
X=\begin{pmatrix}0&\mu/\lambda^2\\\lambda^2&0\end{pmatrix}.
\]
Its stabilizer in \(\mathrm{GL}_2(k)\) consists only of scalar matrices, hence its orbit has \(q(q^2-1)\) elements. This proves the final \(q(q-1)\) classes. For \(Y=0\), conjugacy is just similarity of arbitrary two-by-two matrices; rational canonical forms give \(q\) scalar classes, \(q\) nonsemisimple repeated-root classes, \(q(q-1)/2\) split-distinct-root classes, and \((q^2-q)/2\) irreducible-quadratic classes, totaling \(q^2+q\).

The classification also shows that the \(Y\ne0\), \(\lambda\ne0\) representations are absolutely simple: the unique invariant line of \(Y\) is not invariant under \(X\). This is a consequence, not a separate new irreducible-module classification.

## Verification
The standalone checker `jordan_plane_checker.py`, using polynomial-basis implementations of \(\mathbb F_2\) and \(\mathbb F_4\), exhaustively enumerates every ordered pair of two-by-two matrices, tests the defining relation, constructs all \(\mathrm{GL}_2\) conjugacy orbits, and checks the component point counts and orbit sizes. It prints `VERIFY_JORDAN_PLANE_OK` on success. For \(q=2\) it finds 40 solutions and 12 orbits, with \((6,4,2)\) classes in the three strata; for \(q=4\) it finds 1216 solutions and 48 orbits, with \((20,16,12)\) classes. These finite checks are independent of, and do not replace, the proof valid for all \(q=2^f\).

As a consistency check with previously established labeled enumeration, the \(q\) possible values of \(\lambda\), the \(q^2-1\) nonzero nilpotent matrices \(N\), and the \(q^2\) solutions \(X\) per such \(Y\), together with \(Y=0\), give
\[
\#\mathcal R_2(\mathbb F_q)=q^5+q^4-q^3.
\]
In particular, \(\#B(\mathbb F_q)=q^5\), \(\#A(\mathbb F_q)=q^4\), and \(\#(A\cap B)(\mathbb F_q)=q^3\). The point count alone cannot determine either the geometric component structure or the simultaneous-conjugacy orbit classification.

## Relationship to prior work
Iyudu's characteristic-zero classification of the Jordan-plane representation space proves equidimensionality in all matrix dimensions, with component dimension the matrix dimension squared. Its explicit assumption of algebraically closed characteristic zero makes the characteristic-two non-equidimensional result outside its scope. Benkart--Lopes--Ondrus treat the positive-characteristic irreducible modules of the general Ore-extension family containing the Jordan plane; their Corollary 7.8 encompasses the absolutely simple two-dimensional sector, but does not give the **full** reducible/irreducible finite-field orbit census or the reduced two-component geometry established here. Shirikov's earlier positive-characteristic paper studies the primary spectrum, automorphisms, and central prime-ideal extensions; the available abstract does not establish the present geometric-orbit statement. The full Shirikov text was not inspected, so specialized priority remains a genuine risk.

## Limitations
No claim is made about the radicality, embedded components, nilpotent structure, or singularities of the **entire original representation scheme**; the component and singular-locus assertions concern its reduced algebraic set and, for singularities, the irreducible component \(B\) only. The formula for labeled solutions was established in earlier enumeration work and is not proposed as an independent discovery. The rational orbit count is for fields of characteristic two and two-dimensional representations only, without factoring out automorphisms of \(R\). A specialized source not accessed in full could contain a stronger theorem. No independent mathematical audit has been performed.

## References
1. N. K. Iyudu, *Representation spaces of the Jordan plane*, arXiv:1209.0746v1 (4 September 2012), especially Sections 2 and 13; later *Communications in Algebra* 42 (2014), 3507–3540.
2. G. Benkart, S. A. Lopes, M. Ondrus, *A Parametric Family of Subalgebras of the Weyl Algebra II. Irreducible Modules*, arXiv:1212.1404v1 (6 December 2012), especially Section 7; later *Contemporary Mathematics* 602 (2013), 73–98.
3. E. N. Shirikov, *The Jordan Plane over a Field of Positive Characteristic*, *Mathematical Notes* 82 (2007), 238–256, DOI 10.1134/S0001434607070292. Bibliographic record and abstract inspected; full text unavailable during this study.
