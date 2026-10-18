# The \(2^t+1\) geometric components of commuting rank-one niltriangular four-by-four tuples

## Finding
Let \(k\) be any field and let \(t\ge 1\). Write \(\mathfrak u_4(k)\) for the associative algebra of strictly upper-triangular \(4\times4\) matrices. Let \(X_t\) be the **reduced** affine algebraic variety of ordered tuples \((A_1,\ldots,A_t)\) such that every \(A_i\) has rank at most one and \([A_i,A_j]=0\) for all \(i,j\). All components mentioned below are geometrically irreducible.

**Theorem.** The variety \(X_t\) has exactly \(2^t+1\) geometric irreducible components. Three have dimension \(3t\); for each nonempty proper subset \(S\subsetneq\{1,\ldots,t\}\) there is one further component of dimension \(2t+1\). Therefore \(X_1\) is equidimensional, while \(X_t\) is non-equidimensional for every \(t\ge2\).

Write each matrix as
\[
 A_i=\begin{pmatrix}
 0&a_i&b_i&c_i\\
 0&0&d_i&e_i\\
 0&0&0&f_i\\
 0&0&0&0
 \end{pmatrix}.
\]
The three distinguished components are
\[
 L_t:\ d_i=e_i=f_i=0;\qquad
 R_t:\ a_i=b_i=d_i=0;\qquad
 D_t:\ a_i=f_i=0,\quad b_i e_i=c_i d_i,
\]
with the indicated conditions for every index \(i\). Each is an irreducible variety of dimension \(3t\).

For a nonempty proper subset \(S\subsetneq\{1,\ldots,t\}\), the component \(M_S\) has \(d_i=0\) for every \(i\), \((e_i,f_i)=(0,0)\) for \(i\in S\), and \((a_j,b_j)=(0,0)\) for \(j\notin S\). In addition, there is a single line \(\ell\subset k^2\) such that
\[
 (a_i,b_i)\in\ell\quad (i\in S),\qquad
 (e_j,f_j)\in\ell^\perp\quad (j\notin S),
\]
where \(\perp\) uses the nondegenerate standard dot product. The coordinates \(c_i\) are unrestricted. This incidence description is closed and makes \(M_S\) geometrically irreducible of dimension \(2t+1\), including in characteristic two.

For any finite field \(\mathbb F_q\), with \(q\) any prime power, the exact number of labeled ordered commuting tuples is
\[
 \boxed{\begin{aligned}
 \#X_t(\mathbb F_q)={}&q^t\bigl[2q^{2t}+(q+1)(2q-1)^t-2(q+1)q^t+q\bigr]\\
 &+(q^3+q^2-q)^t-(2q^2-q)^t.
 \end{aligned}}
\]
In particular, \(\#X_2(\mathbb F_2)=212\), \(\#X_2(\mathbb F_3)=2601\), and \(\#X_3(\mathbb F_2)=2088\).

## Assumptions and scope
All matrices lie in the **fixed, standard** strictly upper-triangular algebra; no simultaneous conjugacy quotient is taken. Rank zero is permitted, and the zero tuple is counted. The tuple positions are labeled and repetitions are allowed. The component assertion is about the underlying reduced variety, not its possibly nonreduced defining scheme. The geometric statement is valid over an arbitrary field after scalar extension to an algebraic closure; the arithmetic statement is valid for every finite field.

## Proof
**Step 1: entrywise equations.** The \(2\times2\) minors show that \(\operatorname{rank}(A_i)\le1\) is equivalent, for each \(i\), to
\[
 a_i d_i=a_i e_i=a_i f_i=b_i f_i=d_i f_i=0,
 \qquad b_i e_i=c_i d_i.
\]
Direct matrix multiplication gives \([A_i,A_j]=0\) if and only if
\[
 a_i d_j=a_j d_i,\qquad d_i f_j=d_j f_i,
 \qquad a_i e_j+b_i f_j=a_j e_i+b_j f_i.
\]
These conditions include every defining rank and commutation equation; no other matrix entry can contribute.

**Step 2: a nonzero middle coordinate.** Regard \(\mathbf a=(a_i)\), \(\mathbf d=(d_i)\), and \(\mathbf f=(f_i)\) as vectors in \(k^t\). If \(\mathbf d\ne0\), the first two commutation equations force \(\mathbf a\) and \(\mathbf f\) to be scalar multiples of \(\mathbf d\). The pointwise equations \(a_i d_i=d_i f_i=0\) force both multiples to be zero, since at least one \(d_i\ne0\). Thus this locus lies in \(D_t\). Conversely every point of \(D_t\) obeys all commutation equations. For each index the equation \(b_i e_i=c_i d_i\) cuts out the usual \(2\times2\) rank-at-most-one determinantal cone in four coordinates, an absolutely irreducible hypersurface of dimension three. Their product is geometrically irreducible of dimension \(3t\). Since its open subset \(\mathbf d\ne0\) is nonempty and dense, \(D_t\) is the closure of the nonzero-middle-coordinate locus.

**Step 3: a zero middle coordinate.** If every \(d_i=0\), the rank minors imply
\[
 (a_i,b_i)=(0,0)\quad\text{or}\quad(e_i,f_i)=(0,0).
\]
Put \(x_i=(a_i,b_i)\) and \(y_i=(e_i,f_i)\). The only remaining commutation equation is \(x_i\cdot y_j=x_j\cdot y_i\). At each index at most one of \(x_i,y_i\) is nonzero. If all \(y_i\) vanish, the tuple is in \(L_t\); if all \(x_i\) vanish, it is in \(R_t\). Otherwise both types occur, and for every nonzero \(x_i\) and nonzero \(y_j\), commutation gives \(x_i\cdot y_j=0\). Choose one nonzero vector of each type. Since a nonzero vector in the nondegenerate \(k^2\) pairing has a one-dimensional annihilator, *all* nonzero \(x_i\) lie on one line \(\ell\), and *all* nonzero \(y_j\) lie on \(\ell^\perp\). Assign every zero-type index to either side to obtain one of the stated \(M_S\). Conversely all points in every \(L_t,R_t,M_S\) commute and obey the rank bound.

**Step 4: irreducibility and completeness.** The varieties \(L_t\) and \(R_t\) are affine spaces of dimension \(3t\). For fixed \(S\), the incidence variety parametrizing a projective line \(\ell\in\mathbb P^1\), all vectors \(x_i\in\ell\) for \(i\in S\), all vectors \(y_j\in\ell^\perp\) for \(j\notin S\), and arbitrary \(c_i\), is a rank-\(2t\) vector bundle over \(\mathbb P^1\). It is geometrically irreducible of dimension \(2t+1\). Projection to tuple coordinates is a closed map (the line parameter is proper), so its image \(M_S\) is closed and irreducible. If both types contain a nonzero vector, the line is uniquely recovered; hence the dimension does not drop under projection. A generic point of each \(M_S\) has \(x_i\ne0\) exactly at indices in \(S\) and \(y_j\ne0\) exactly outside \(S\), with both \(a_i\) and \(f_j\) nonzero for suitable line. Thus it lies in no other \(M_T\), nor in \(L_t,R_t,D_t\). Generic points of \(L_t,R_t,D_t\) likewise lie in no other component, by their nonzero coordinate patterns. These finitely many closed irreducible sets cover \(X_t\) and none contains another; they are exactly its irreducible components. There are \(3+(2^t-2)=2^t+1\) of them. The indicated dimensions yield the equidimensionality statement.

**Step 5: finite-field enumeration.** Split the tuples by whether \(\mathbf d\ne0\). For a fixed index with \(d_i\ne0\), the \(D_t\) equation allows \(q^2\) choices of \((b_i,e_i,c_i)\); for \(d_i=0\), it allows \(q(2q-1)\), since \(b_i e_i=0\). Summing independently over the possible values of each \(d_i\) and removing the all-zero \(\mathbf d\) case gives
\[
 (q^3+q^2-q)^t-(2q^2-q)^t.
\]
For \(\mathbf d=0\), every \(c_i\) is free, contributing \(q^t\). If all \(y_i=0\) or all \(x_i=0\), there are \(2q^{2t}-1\) possibilities for the remaining \(x,y\) coordinates, with the all-zero array counted just once. Otherwise let \(s\ge1\) indices carry nonzero \(x_i\), and \(u\ge1\) indices carry nonzero \(y_i\). A common projective line \(\ell\) is uniquely determined and has \(q+1\) choices; every selected nonzero vector has \(q-1\) choices in its required line. Summing over disjoint labeled index sets gives
\[
 (q+1)\bigl[(2q-1)^t-2q^t+1\bigr].
\]
Multiplying this zero-middle-coordinate subtotal by \(q^t\) and adding the preceding nonzero-middle-coordinate subtotal proves the formula.

## Verification
The standalone `verify_rankone_n4.py` enumerates literal \(4\times4\) matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\). It checks rank by all \(2\times2\) minors, commutation by full matrix products, and the formula by exhaustive tuple enumeration in eleven configurations, with tuple length up to four. It also exhaustively checks the component cover and provides a point belonging to each component alone for \(q=2\), \(t=2,3\). All checks passed with final marker `VERIFY_OK_TRIANGULAR_RANKONE`. Finite checks corroborate, but do not prove, the unrestricted geometric and all-prime-power statements.

## Relationship to prior work
Basili's arXiv:0803.0722 studies the **unrestricted** commuting variety of pairs of strictly upper-triangular matrices. Its Section 2, Example A identifies two irreducible components for the unrestricted \(4\times4\) pair variety; its Section 3 revisits that geometry. This does not determine the components of the **rank-at-most-one subvariety** (which has five components already for pairs), still less the all-arity formula. Wong, Ma and Zhou (2014) classify automorphisms of a directed zero-divisor graph on rank-one upper-triangular matrices, rather than the present constrained tuple variety. Ou and Zhong's subsequent 2016 work determines automorphisms of a commuting graph of rank-one upper-triangular matrices, not the component geometry of these rank-constrained strictly triangular tuple varieties. The latter two sources concern the same class of matrix supports and motivate the restriction, but neither supplies the stated result in the material examined.

## Limitations
The result is fixed at matrix size four and rank at most one. It does not classify higher-size cases, scheme-theoretic nilpotents, singularity schemes, conjugacy classes, or tuple counts without the rank restriction. Broader priority against differently phrased determinantal-incidence classifications has not been independently audited.

## References
1. R. Basili, *Some remarks on varieties of pairs of commuting upper triangular matrices and an interpretation of commuting varieties*, arXiv:0803.0722, publicly posted 5 March 2008. https://arxiv.org/abs/0803.0722.
2. D. Wong, X. Ma, and J. Zhou, *The group of automorphisms of a zero-divisor graph based on rank one upper triangular matrices*, Linear Algebra Appl. 460 (2014), 242–258, DOI:10.1016/j.laa.2014.07.041.
3. S. Ou and J. Zhong, *Automorphisms of a commuting graph of rank one upper triangular matrices*, Electron. J. Linear Algebra 31 (2016), 774–793, DOI:10.13001/1081-3810.3064.
4. R. Basili, *On commuting varieties of upper triangular matrices*, Comm. Algebra 45 (2017), 1533–1541, posted online 7 October 2016, DOI:10.1080/00927872.2016.1178272.
