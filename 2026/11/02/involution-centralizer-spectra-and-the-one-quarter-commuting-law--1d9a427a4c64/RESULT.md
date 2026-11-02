# Involution-centralizer spectra and the one-quarter commuting law for four-dimensional unitriangular groups in characteristic two

## Finding
For every finite field \(F=\mathbb F_q\) with \(q=2^m\) and \(m\ge1\), let \(G=UT_4(F)\) and \(I=\{g\in G:g^2=1\}\), including the identity. The complete spectrum of centralizer sizes *within the involution set*, \(c(g)=|\{h\in I:gh=hg\}|\), consists of exactly the following four levels. The first coordinate is the multiplicity of the second:

\[
\begin{array}{c|c}
\text{multiplicity}&c(g)\\ \hline
q&2q^4-q^2\\
q^3-q&q^4+q^3-q^2\\
q^4-q^2&2q^3-q^2\\
q^4-q^3&q^4
\end{array}
\]

These sizes are pairwise distinct for every \(q\ge2\). In particular,
\[
|I|=2q^4-q^2,\qquad
|\{(g,h)\in I^2:gh=hg\}|=q^8+2q^7-2q^5,
\]
and independently uniform involutions commute with probability
\[
\boxed{\frac{q(q^3+2q^2-2)}{(2q^2-1)^2}},
\]
which tends to \(1/4\) as \(q\) ranges through even prime powers. The commuting graph on \(I\setminus\{1\}\), with distinct commuting elements adjacent, has four degree strata given by \(c(g)-2\), with the central stratum multiplicity \(q-1\) and all other multiplicities as above. It has \((q^8+2q^7-2q^5-3(2q^4-q^2)+2)/2\) edges.

## Assumptions and scope
The characteristic is exactly two; \(q\) may be any power of two, not necessarily a prime. The word involution is used in the equation-defined sense \(g^2=1\), including the identity. The centralizers \(c(g)\) are taken inside \(I\), **not** the group-theoretic centralizers \(C_G(g)\); \(I\) is generally not a subgroup. All counts concern labeled matrices in \(UT_4(F)\), not conjugacy classes. The graph convention excludes loops and excludes the identity but includes other central elements.

## Proof
Write \(g=1+N\) with the six strictly upper triangular entries
\[
N_{12}=u,\quad N_{23}=v,\quad N_{34}=w,\quad
N_{13}=s,\quad N_{24}=t,\quad N_{14}=z.
\]
Since the characteristic is two, \(g^2=1\) exactly when \(N^2=0\), equivalent to
\[
uv=0,\qquad vw=0,\qquad ut+sw=0. \tag{1}
\]
The coordinate \(z\) is unrestricted. For \(v\ne0\), equations (1) force \(u=w=0\), giving \((q-1)q^3\) involutions. For \(v=0\), form the \(2\)-by-\(2\) matrix
\[
X=\begin{pmatrix}u&s\\w&t\end{pmatrix};\quad \det X=ut+sw.
\]
The number of matrices \(X\) of rank at most one is
\(S=q^3+q^2-q\): the nonzero rank-one matrices number \((q^2-1)^2/(q-1)\), and zero contributes one. The free \(z\) and the \(v\ne0\) stratum give
\[
|I|=qS+(q-1)q^3=2q^4-q^2. \tag{2}
\]

For a second involution \(h=1+N'\), matrix commutation is equivalent to \(NN'=N'N\). Direct multiplication gives the three independent conditions
\[
uv'+u'v=0,\qquad vw'+v'w=0,\qquad
ut'+u't+sw'+s'w=0. \tag{3}
\]
The coordinates \(z,z'\) never enter these conditions. When \(v=v'=0\), equation (3) says \(\det(X+X')=0\), because \(\det X=\det X'=0\). For any fixed nonzero rank-one matrix \(X\), its commuting partners \(X'\) of rank at most one have either the same column space or the same row space as \(X\); these two families have \(q^2\) elements each and intersect in the \(q\) scalar multiples of \(X\). Thus their union has exactly \(2q^2-q\) matrices. For \(X=0\), every one of the \(S\) matrices is a partner.

If \(v\ne0\), then \(u=w=0\). Equations (3) force \(u'=w'=0\) for every commuting involution, regardless of \(v'\). The remaining \(v',s',t',z'\) have \(q^4\) choices. This gives centralizer size \(q^4\) for all \((q-1)q^3=q^4-q^3\) members of this stratum.

If \(v=0\) and \((u,w)\ne(0,0)\), equations (3) force \(v'=0\). The preceding rank-one calculation leaves \((2q^2-q)q=2q^3-q^2\) partners, including the free \(z'\). Their number is \((q^2-1)q^2=q^4-q^2\): there are \(q^2-1\) choices of \((u,w)\), \(q\) solutions \((s,t)\) of (1), and \(q\) choices of \(z\).

If \(v=u=w=0\) but \((s,t)\ne(0,0)\), then \(X\) is nonzero rank one. The \(v'=0\) partners contribute \(q(2q^2-q)\); additional \(v'\ne0\) partners necessarily have \(u'=w'=0\) and contribute \((q-1)q^3\). This yields \(q^4+q^3-q^2\) commuting involutions, for \(q(q^2-1)=q^3-q\) elements.

Finally, \(v=u=w=s=t=0\), with arbitrary \(z\), describes exactly \(q\) central elements, each commuting with all \(I\), of size \(2q^4-q^2\). This proves the four-row spectrum. Multiplicity-weighted summation gives
\[
\begin{aligned}
\sum_{g\in I}c(g)
={}&q(2q^4-q^2)+(q^3-q)(q^4+q^3-q^2)\\
&+(q^4-q^2)(2q^3-q^2)+(q^4-q^3)q^4\\
={}&q^8+2q^7-2q^5.\tag{4}
\end{aligned}
\]
Dividing (4) by the square of (2) proves the probability formula; division by \(q^8\) proves the limit. Every \(g\ne1\) is adjacent to precisely \(c(g)-2\) other nonidentity elements (excluding itself and the identity). Summing degrees yields the asserted edge number.

## Verification
The accompanying self-contained file `ut4_even_involution_verify.py` enumerates all candidate unitriangular matrices, checks \(g^2=1\) by actual finite-field matrix multiplication, and recomputes commuting centralizers from the product operation independently of the displayed proof formulas. It exhaustively checks **each** involution centralizer over \(\mathbb F_2\) and \(\mathbb F_4\), including the ordered commuting-pair sum and stratum multiplicities. Over \(\mathbb F_8\) it enumerates all involutions, verifies all four multiplicities, and checks one representative centralizer per stratum. The program reports `VERIFY_OK`; finite testing is corroboration, not a proof of the assertions for all \(q\).

## Relationship to prior work
The Jordan-type enumeration of strictly upper triangular matrices by Fuchs and Kirillov [1] is directly relevant to the square-zero locus. Their distribution by Jordan type does not contain the joint commutation fiber sizes on that locus. Bhunia [2] studies conjugacy classes of group centralizers for upper triangular groups over infinite fields of characteristic different from two, and does not cover this even-characteristic restricted spectrum. Gargate and Gargate [3] analyze conjugate involutions in an odd-characteristic triangular setting, which likewise differs. Majeed and Ramkumar [4] give the coordinate commutation equations and **full-group** centralizer orders for \(UT_4(\mathbb F_p)\). Its core mathematical statements, centralizer table, and section organization were inspected, and the searchable full text was checked for the target terms; the source does not state the cardinalities of centralizers **inside the square-one subset**, their multiplicities, or the resulting probability. The present proof independently rederives the common commutation equations and then imposes the characteristic-two square-zero constraint, with a separate rank-one matrix incidence argument. Counting all matrices in the ambient centralizers is not sufficient to obtain these new counts.

## Limitations
This is a dimension-four, characteristic-two result. No formula is asserted for higher unitriangular dimensions or odd characteristic. The graph degrees do not alone classify the entire induced involution-commuting graph. Literature searches and comparisons cannot establish worldwide publication priority; in particular, equivalent counts may occur in work on square-zero matrix varieties or finite group involution commuting probabilities. No independent external validation was performed.

## References
[1] D. Fuchs and A. Kirillov, *Jordan Types of Triangular Matrices over a Finite Field*, arXiv:2204.00066, first posted 2022-03-31, https://arxiv.org/abs/2204.00066.

[2] S. Bhunia, *Conjugacy Classes of Centralizers in the Group of Upper Triangular Matrices*, arXiv:1901.07869, first posted 2019-01-23, https://arxiv.org/abs/1901.07869.

[3] S. Gargate and S. Gargate, *Coninvolutions on Upper Triangular Matrix Group over the Ring of Gaussian Integers and Quaternions modulo p*, arXiv:2008.00575, first posted 2020-08-02, https://arxiv.org/abs/2008.00575.

[4] M. Majeed and P. B. Ramkumar, *Commuting Graph of Unitriangular Group UT(4; p)*, arXiv:2608.09235, first posted 2026-08-10, https://arxiv.org/abs/2608.09235.
