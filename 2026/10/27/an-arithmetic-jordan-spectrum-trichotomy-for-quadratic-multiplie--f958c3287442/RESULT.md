# An arithmetic Jordan-spectrum trichotomy for quadratic multipliers on a squarefree complete intersection

## Finding

Let \(q\) be **any odd prime power**, and let
\[
A_q=\mathbb F_q[x_1,x_2,x_3,x_4]/(x_1^2,x_2^2,x_3^2,x_4^2).
\]
For every homogeneous quadratic \(Q\in (A_q)_2\), the Jordan partition of multiplication \(m_Q:A_q\to A_q\) is determined and its exact frequency among the \(q^6\) possible quadrics is given below. There are exactly seven partitions, each with positive frequency.

Define \(u=q-1\), \(w=2q-1\), and
\[
\tau(q)=\begin{cases}
1,&3\mid q,\\
2,&q\equiv1\pmod3,\\
0,&q\equiv2\pmod3.
\end{cases}
\]
Introduce the integer quantities
\[
\begin{aligned}
L&=6u+12u^2+4u^3,&N&=3u^3,\\
D&=w^3+3w u^3+(q-2)u^4,&E&=w^3+\tau(q)u^4,\\
H_0&=q^5+(q-1)q^2.
\end{aligned}
\]
For \(r\in\{2,3,4\}\) and \(\varepsilon\in\{0,1\}\), set
\[
\lambda_{r,\varepsilon}=\bigl(3^{\varepsilon},2^{r+2-2\varepsilon},1^{16-2(r+2)+\varepsilon}\bigr),
\]
where an exponent zero signifies omission of that block size, and the tuple lists the sizes of Jordan blocks with multiplicity. The complete spectrum is:

| Jordan partition | Exact number of quadrics |
| --- | ---: |
| \( (1^{16}) \) | \(1\) |
| \(\lambda_{2,0}=(2^4,1^8)\) | \(L\) |
| \(\lambda_{2,1}=(3,2^2,1^9)\) | \(N\) |
| \(\lambda_{3,0}=(2^5,1^6)\) | \(E-1-L\) |
| \(\lambda_{3,1}=(3,2^3,1^7)\) | \(D-E-N\) |
| \(\lambda_{4,0}=(2^6,1^4)\) | \(H_0-E\) |
| \(\lambda_{4,1}=(3,2^4,1^5)\) | \(q^6-H_0-D+E\) |

The seven multiplicities are positive for every odd prime power and add to \(q^6\). In particular, the two rank-three frequencies simplify to
\[
E-1-L=(q-1)^3(4+\tau(q)(q-1)),\qquad
D-E-N=(q-1)^4(q+4-\tau(q)).
\]
Thus they are sensitive to the number \(\tau(q)\) of geometric branches of the binary cubic-root equation: the spectrum undergoes an explicit arithmetic trichotomy in characteristic three, for \(q\equiv1\pmod3\), and for \(q\equiv2\pmod3\). This dependence is not visible from the ordinary rank distribution of zero-diagonal symmetric matrices alone.

## Assumptions and scope

The algebra is commutative, standard graded with Hilbert vector \((1,4,6,4,1)\), and has squarefree monomial basis \(x_S=\prod_{i\in S}x_i\) indexed by \(S\subseteq\{1,2,3,4\}\). The finite field may be nonprime, but its characteristic must be odd. Only homogeneous quadrics \(Q\in(A_q)_2\) are counted, not arbitrary elements of the maximal ideal or degree-one Lefschetz elements. Every \(Q\) is counted as a distinct algebra element, not modulo scaling or algebra automorphisms.

For coefficients \(a_{ij}\in\mathbb F_q\), write \(Q=\sum_{1\le i<j\le4}a_{ij}x_ix_j\). Let \(B(Q)\) be the symmetric \(4\times4\) matrix with zero diagonal and off-diagonal entries \(B(Q)_{ij}=a_{kl}\), where \(\{k,l\}=\{1,2,3,4\}\setminus\{i,j\}\). Define
\[
H(Q)=a_{12}a_{34}+a_{13}a_{24}+a_{14}a_{23}.
\]
The matrix \(B(Q)\) is the degree-one-to-degree-three multiplication matrix under the complementary-monomial bases, and its hafnian is \(H(Q)\). The two invariants \(r=\operatorname{rank}B(Q)\) and \(\varepsilon=\mathbf1_{H(Q)\ne0}\) define the six nonzero strata of the theorem.

## Proof

**1. Reduction to two elementary invariants.** Multiplication by \(Q\) increases homogeneous degree by two. Its only potentially nonzero graded pieces are \((A_q)_0\to(A_q)_2\), \((A_q)_1\to(A_q)_3\), and \((A_q)_2\to(A_q)_4\). For \(Q\ne0\), the first and last have rank one: the last uses the perfect complementary-monomial pairing between degrees two and two. The middle map has matrix \(B(Q)\). Consequently
\[
\operatorname{rank}m_Q=2+\operatorname{rank}B(Q).
\]
Further, \(m_Q^3=0\), while
\[
Q^2=2H(Q)x_1x_2x_3x_4,
\qquad \operatorname{rank}m_Q^2=\mathbf1_{H(Q)\ne0}.
\]
The assumption of odd characteristic is essential to the second equality. For a nilpotent operator on a sixteen-dimensional vector space with \(m^3=0\), if \(R_1\) and \(R_2\) denote its first- and second-power ranks, its numbers of blocks of sizes \(3,2,1\) are respectively \(R_2\), \(R_1-2R_2\), and \(16-2R_1+R_2\). This gives \(\lambda_{r,\varepsilon}\).

**2. Rank-two hollow symmetric matrices.** A symmetric rank-one matrix with zero diagonal is zero in odd characteristic. For rank two, quotienting by its radical yields a nondegenerate symmetric bilinear form in dimension two with nonzero isotropic vectors (the diagonal entries vanish). It is therefore split hyperbolic. The nonzero column vectors all lie on one of the two isotropic lines; both occur. Hence the edge support of \(B\) is a complete bipartite graph on its active vertices, with all cross-entries nonzero and an outer-product constraint for a balanced bipartition. With four labelled positions, the cases are a single edge (\(6u\)), a two-edge star (\(12u^2\)), a three-edge star (\(4u^3\)), and a rank-one weighted \(K_{2,2}\) (\(3u^3\)). In the first three cases the hafnian is zero. In the last case, its two nonzero perfect-matching products coincide, so \(H=2\cdot\text{(nonzero product)}\ne0\). Therefore the rank-two counts with \(H=0\) and \(H\ne0\) are exactly \(L\) and \(N\).

**3. A weighted determinant cone.** For a general symmetric hollow matrix write its six off-diagonal entries as \(a,b,c,d,e,f\), in the order \(12,13,14,23,24,34\). Put \(X=af\), \(Y=be\), and \(Z=cd\). Direct expansion gives
\[
\det B=X^2+Y^2+Z^2-2(XY+XZ+YZ),\qquad H=X+Y+Z.
\]
For each prescribed product, there are exactly \(w=2q-1\) choices of an ordered factor pair giving zero and exactly \(u=q-1\) choices giving a specified nonzero value. Thus the number of matrices in a set of product triples is the sum of weights \(w^{\#\text{zero coordinates}}u^{\#\text{nonzero coordinates}}\).

Set \(F(X,Y,Z)=X^2+Y^2+Z^2-2(XY+XZ+YZ)\). Since
\[
F=(X-Y-Z)^2-4YZ,
\]
its total number of zeros in \(\mathbb F_q^3\) is \(q^2\): summing \(1+\chi(YZ)\) over \(Y,Z\) with the quadratic character \(\chi(0)=0\) gives \(q^2\). The zero triple is one solution; there are none with exactly one nonzero coordinate, exactly \(3u\) with two nonzero coordinates (the two values must agree), and \(u(q-2)\) with all three coordinates nonzero. Weighting gives the total number of singular matrices
\[
D=w^3+3u\cdot w u^2+u(q-2)u^3.
\]

**4. The arithmetic intersection.** On the hyperplane \(H=0\), substitute \(Z=-X-Y\). Then
\[
F(X,Y,-X-Y)=4(X^2+XY+Y^2).
\]
If \(3\mid q\), the displayed binary quadratic is a square and its nonzero zero locus is one line; if \(q\equiv1\pmod3\), it has two distinct rational lines; if \(q\equiv2\pmod3\), it has no nonzero rational point. On each nonzero line all three product coordinates are nonzero. Consequently the number of matrices with \(\det B=0\) and \(H=0\) is
\[
E=w^3+\tau(q)u^4.
\]
Separately, direct counting of solutions to \(af+be+cd=0\) by whether \((a,b,c)\) is zero gives the number with \(H=0\):
\[
H_0=q^3+(q^3-1)q^2=q^5+(q-1)q^2.
\]

**5. Subtraction into disjoint strata.** Rank zero contributes the unique zero matrix, and rank one is impossible. Rank two contributes \(L\) at \(H=0\) and \(N\) at \(H\ne0\). Subtracting these from the singular determinant counts \(E,D\), and then from the total \(H=0\) count \(H_0\) and \(q^6\), yields exactly the six displayed nonzero rows. Their total plus one is identically \(q^6\). Positivity is immediate for \(q=3\) and follows in general from the explicit nonempty rank/hafnian configurations and field extension of those configurations; it also follows from the closed expressions for \(q\ge3\). Each rank/hafnian stratum maps to the asserted partition by step one. This proves completeness, the frequencies, and the trichotomy.

## Verification

A standalone Python 3 checker (`verify.py`) uses literal squarefree monomial multiplication on all sixteen basis monomials; it does not assume the proposed Jordan ranks in those tests. It exhaustively enumerates all \(q^6\) quadrics for \(q=3,5,7\), independently computes the rank and hafnian of the complementary coefficient matrix, and checks all seven predicted multiplicities. It also checks actual multiplication ranks and squares for every quadric over \(\mathbb F_3\) and hundreds of deterministic cases over \(\mathbb F_5\) and \(\mathbb F_7\). Finally it tests the quadratic-product weighting in \(\mathbb F_9\) and direct multiplication on deterministic extension-field samples. Execute `python3 verify.py` from the directory containing this file. The expected success marker is `VERIFY_OK_DEGREE_TWO_SQUAREFREE_JORDAN`.

The finite checks are not a proof of the uniform statement; steps 1–5 prove it for every odd prime power.

## Relationship to prior work

Lewis, Liu, Morales, Panova, Sam and Zhang (2010 preprint, later revised) develop rank enumeration of finite-field symmetric matrices with prescribed zero diagonal, particularly in Sections 3–4. Their rank counts are a **coarser** invariant: they do not specify simultaneous vanishing of the hafnian, which is precisely the additional information determining the length-three Jordan blocks of quadratic multiplication. The present result is an exact joint rank/hafnian enumeration for the four-variable squarefree complete intersection, with a mod-three arithmetic split not determined by the marginal rank counts.

Cook (2011 preprint) addresses weak and strong Lefschetz properties of monomial complete intersections, predominantly through multiplication by **linear** forms and powers thereof. It provides the natural algebraic context but not a census of homogeneous quadratic multipliers by Jordan type. Earlier classical Lefschetz results establish existence of appropriate linear forms, not the distribution presented here.

Related research records about Jordan types in other Artinian Gorenstein Hilbert functions do not imply these seven frequencies: their degree sequence, algebra, and multipliers differ. Priority remains a literature-risk question; exhaustive historical uniqueness is not asserted.

## Limitations

The result is restricted to the sixteen-dimensional algebra shown and to homogeneous degree-two elements over **odd** finite fields. Characteristic two has different squares, and unrestricted elements of the maximal ideal can have longer nilpotency chains. The enumeration is a finite-field point count, not a classification of algebra-automorphism orbits or a statement about all monomial complete intersections. Earlier literature could contain an equivalent count under different language.

## References

1. Joel Brewster Lewis, Ricky Ini Liu, Alejandro H. Morales, Greta Panova, Steven V. Sam and Yan X. Zhang, *Matrices with restricted entries and \(q\)-analogues of permutations*, arXiv:1011.4539, initial public version 20 November 2010, especially Sections 3 and 4. https://arxiv.org/abs/1011.4539
2. David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979, initial public version 21 November 2011, especially Sections 1 and 2. https://arxiv.org/abs/1111.4979
