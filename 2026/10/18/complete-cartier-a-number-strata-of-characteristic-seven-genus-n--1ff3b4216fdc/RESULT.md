# Complete Cartier \(a\)-number strata for genus-nine characteristic-seven Artin–Schreier curves

## Finding
Let \(k\) be an algebraically closed field of characteristic \(7\). Every smooth projective Artin–Schreier curve \(X/k\) of genus \(9\) and \(7\)-rank zero can be presented in the form
\[
y^7-y=x^4+a x^2+b x,\qquad a,b\in k.
\]
For any such presentation, the \(a\)-number of its Jacobian, equivalently the kernel dimension of Cartier on regular differentials, is exactly
\[
a(X)=\begin{cases}
6,&a\ne0,\\
7,&a=0,\ b\ne0,\\
9,&a=b=0.
\end{cases}
\]
Thus the possible values are precisely \(6,7,9\); \(8\) cannot occur. On the parameter plane the loci are respectively the open complement of \(a=0\), its punctured line \(a=0,b\ne0\), and the origin. The special monomial case has zero Cartier operator; the first stratum contains the minimal-automorphism example \(a=b=1\) of Tafazolian–Kazemifard.

## Assumptions and scope
All curves are smooth projective normalizations of the indicated affine separable equations over algebraically closed \(k\) of characteristic exactly seven. The term Artin–Schreier curve means one admitting a degree-seven cyclic cover of \(\mathbb P^1\). By Deuring–Shafarevich, rank zero forces one branch point, and Riemann–Hurwitz with genus nine forces its unique reduced ramification jump to be four. Put the branch point at infinity, remove its constant term by an Artin–Schreier translation of \(y\), eliminate the cubic term by translating \(x\), and normalize the nonzero leading quartic coefficient by scaling \(x\). This yields the stated model. No claim is made concerning curves with a different genus, characteristic, or prescribed higher Cartier iterates.

## Proof
For the normalized equation, the unique point \(P\) above infinity has valuations \(v_P(x)=-7\), \(v_P(y)=-4\). The different of the cover at \(P\) has exponent \((7-1)(4+1)=30\); therefore \(\operatorname{div}(dx)=(30-14)P=16P\). Every \(x^iy^jdx\) with \(i\ge0\), \(0\le j\le5\), and \(7i+4j\le16\) is regular, and the nine such forms constitute a basis since the genus is nine:
\[
\mathcal B=(dx,x\,dx,x^2dx,y\,dx,xy\,dx,y^2dx,xy^2dx,y^3dx,y^4dx).
\]
The relation \(y^7=y+f(x)\), where \(f(x)=x^4+ax^2+bx\), yields
\[
\mathcal C(x^iy^jdx)=\sum_{t=0}^{j}\binom jt(-1)^{j-t}y^t\mathcal C\!\left(x^i f(x)^{j-t}dx\right).
\]
For a polynomial \(h(x)=\sum_m h_m x^m\), the Cartier operator selects exactly exponents \(m\equiv6\pmod7\), sending \(h_{7s+6}x^{7s+6}dx\) to \(h_{7s+6}^{1/7}x^sdx\). Since \(k\) is perfect, raising every coefficient of the Cartier matrix to the seventh power preserves its rank. In the basis \(\mathcal B\), all columns except those indexed by \(y^2dx,xy^2dx,y^3dx,y^4dx\) vanish. The only potentially nonzero rows are \(dx,x\,dx,y\,dx,y^2dx\). In precisely these row and column orders, the entrywise seventh power of the Cartier matrix is
\[
\begin{pmatrix}
2a&2b&-a^3-3b^2&-a^2b^2\\
0&0&0&-3b\\
0&0&-a&3a^3+2b^2\\
0&0&0&-2a
\end{pmatrix}.
\]
All coefficients are computed in characteristic seven. If \(a\ne0\), the first, third and fourth columns have independent pivots in the first, third and fourth rows, so rank is three; the first two columns are proportional, hence rank cannot exceed three. If \(a=0,b\ne0\), the second and fourth columns are independent (the last has a nonzero second-row entry), and every other nonzero column is a multiple of the second, giving rank two. If \(a=b=0\), the matrix is zero. Since \(\dim H^0(X,\Omega^1_X)=9\), subtracting these ranks from nine gives the three cases stated. These are identities in \(\mathbb F_7[a,b]\), not a finite-field enumeration.

## Verification
The dependency-free program `verify_cartier7.py` reconstructs the differential basis and computes the symbolic Cartier coefficients in \(\mathbb F_7[a,b]\) by polynomial multiplication and residue selection. It compares all 81 matrix entries with the displayed formula and prints `VERIFY_OK` on success. Running `python3 verify_cartier7.py` produced `BASIS [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3), (0, 4)]`, `NONZERO_SYMBOLIC_ENTRIES 8`, and `VERIFY_OK`. The rank conclusions follow symbolically from the displayed matrix and do not depend on tests over \(\mathbb F_7\) alone.

## Relationship to prior work
Tafazolian and Kazemifard (2026, Lemma 3.3 and Theorem 3.5) construct the \(a=b=1\) equation in this genus with full geometric automorphism group \(C_7\) and establish the permitted genus/rank/automorphism range; they do not determine Cartier \(a\)-number strata. Farnell–Pries (2013, Theorem 1.1) give a constant-\(a\) formula when every jump divides \(p-1\), whereas the jump four here does not divide six. Their discussion of monomial equations and earlier work of Pries already covers the special monomial value; novelty is claimed only for the complete three-stratum classification and its exhaustive exclusion of value eight. Booher–Cais (2020) establish bounds and examples for \(a\)-numbers of Artin–Schreier covers, not the displayed complete locus for the characteristic-seven quartic jump.

## Limitations
This is a classification of the numerical Cartier \(a\)-number, not the full Cartier Jordan structure, Ekedahl–Oort type, Newton polygon, or isomorphism classes of the curves. An equivalent genus-nine characteristic-seven calculation could exist in an unindexed treatment of Artin–Schreier moduli. The three loci are described in normalized coefficient space, and their dimensions must not be misread as dimensions of the coarse moduli of unmarked curves. The arithmetic and automorphism properties of arbitrary \(a,b\) are not classified here.

## References
1. S. Tafazolian and A. Kazemifard, *Artin–Schreier Curves of Prescribed \(p\)-Rank Without Extra Automorphisms*, arXiv:2610.13279v1 (first posted 2026-10-09), Sections 3 and 7.
2. S. Farnell and R. Pries, *Families of Artin–Schreier curves with Cartier-Manin matrix of constant rank*, arXiv:1202.4183v1 (2012), Theorem 1.1 and Remark 2.1.
3. J. Booher and B. Cais, *a-Numbers of Curves in Artin-Schreier Covers*, arXiv:1807.10313v3 (2020), Theorem 1.1 and Section 7.
