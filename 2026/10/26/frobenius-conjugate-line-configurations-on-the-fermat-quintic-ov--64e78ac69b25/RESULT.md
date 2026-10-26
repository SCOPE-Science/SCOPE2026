# Frobenius-conjugate line configurations on the Fermat quintic over \(\mathbb F_2\)

## Finding

Let \(S\subset\mathbb P^3_{\mathbb F_2}\) be the Fermat quintic surface
\[
X_0^5+X_1^5+X_2^5+X_3^5=0,
\]
and let \(\sigma\) denote coefficientwise squaring on its geometric lines. Call a line **coordinate-pair** if it comes from one of the three partitions of the four coordinates into two pairs, with each pair satisfying a relation \(X_i=\zeta X_j\) for some \(\zeta^5=1\). There are \(75\) such lines. Call the other lines **exceptional**.

**Theorem.** The finite Fano scheme \(F_1(S)\) is étale of degree \(325\), and, over \(\mathbb F_2\),
\[
F_1(S)\cong
\coprod_{3}\operatorname{Spec}\mathbb F_2\;\amalg\;
\operatorname{Spec}\mathbb F_4\;\amalg\;
\coprod_{80}\operatorname{Spec}\mathbb F_{16}.
\]
All its geometric points are lines defined over \(\mathbb F_{16}\). Exactly \(75\) are coordinate-pair lines and \(250\) are exceptional. The Frobenius orbits and the *induced intersection graphs* on their four-element orbits are completely classified by the following table:

| Line family | Fixed lines | Two-element orbits | Empty four-orbits | Matching four-orbits | Four-cycle orbits | Four-clique orbits |
|---|---:|---:|---:|---:|---:|---:|
| Coordinate-pair (\(75\) lines) | \(3\) | \(0\) | \(12\) | \(0\) | \(0\) | \(6\) |
| Exceptional (\(250\) lines) | \(0\) | \(1\) | \(36\) | \(14\) | \(12\) | \(0\) |

Here the four-orbit's graph has as vertices its four distinct conjugate lines, with an edge when the corresponding projective lines meet. A matching consists of two disjoint edges, a four-cycle has four edges, and a four-clique has all six edges.

The five lines defined over \(\mathbb F_4\) are concurrent at \(P=[1:1:1:1]\): they comprise the three \(\mathbb F_2\)-lines and the exceptional conjugate pair. The six four-clique orbits are precisely the five-line star remainders through the other six \(\mathbb F_2\)-points of \(S\): each such point lies on one \(\mathbb F_2\)-line and four mutually meeting \(\mathbb F_{16}\)-conjugate coordinate-pair lines.

## Assumptions and scope

Work in characteristic \(2\), with the displayed surface defined over the prime field. A geometric line means a projective line in \(S\) after base change to an algebraic closure. Intersections are set-theoretic nonempty intersections of two **distinct** geometric lines in \(\mathbb P^3\); the table does not count self-intersection. The Fano scheme is the closed subscheme of \(\operatorname{Gr}(2,4)\) parametrizing embedded lines in this fixed surface. The result does not classify arbitrary quintic surfaces or all twists of Hermitian surfaces.

## Proof

**1. Smoothness, rigidity, and the field of definition.** The partial derivatives of the equation are \(X_i^4\), and never vanish simultaneously projectively, so \(S\) is smooth. For any line \(L=\mathbb P\langle a,b\rangle\) on \(S\), expanding its defining equation at \(sa+tb\) gives the four coefficients
\[
\sum_i a_i^5,\quad \sum_i a_i^4b_i,\quad
\sum_i a_i b_i^4,\quad \sum_i b_i^5.
\]
They all vanish. Hence, writing \(V=\overline{\mathbb F}_2^4\), one has \(L^{(4)}\subseteq L^\perp\) for the ordinary dot product on \(V\), where the symbol \(L\) denotes the underlying two-dimensional subspace. Both sides have dimension \(2\), so \(L^{(4)}=L^\perp\). Applying fourth Frobenius powers again gives
\[
L^{(16)}=(L^\perp)^{(4)}=(L^{(4)})^\perp
=(L^\perp)^\perp=L.
\]
Thus every geometric line is defined over \(\mathbb F_{16}\). By the normal sequence of \(L\subset S\subset\mathbb P^3\),
\[
0\longrightarrow N_{L/S}\longrightarrow
\mathcal O_L(1)^{\oplus2}\longrightarrow\mathcal O_L(5)
\longrightarrow0,
\]
so \(N_{L/S}\cong\mathcal O_L(-3)\), and \(H^0(L,N_{L/S})=0\). Thus every Fano-scheme point is geometrically reduced. Together with finiteness (established by the next enumeration), this proves finite étaleness over the perfect field \(\mathbb F_2\).

**2. An exhaustive two-chart parametrization.** Represent each \(\mathbb F_{16}\)-line uniquely by a two-by-four reduced-row-echelon matrix. The only nonempty pivot charts are \((0,1)\) and \((0,2)\); for the latter and the former the matrices are respectively
\[
\begin{pmatrix}1&u&0&v\\0&0&1&w\end{pmatrix},
\qquad
\begin{pmatrix}1&0&u&v\\0&1&w&z\end{pmatrix}.
\]
The line-on-surface criterion of step 1 gives in the first chart
\[
1+u^5+v^5=0,\qquad 1+w^5=0,\qquad v^4w=0.
\]
Hence \(v=0\) and \(u^5=w^5=1\), yielding \(25\) lines. In the second chart it gives
\[
1+u^5+v^5=0,\quad 1+w^5+z^5=0,\quad u^4w+v^4z=0.
\]
There are \(60\) possible first pairs and exactly \(5\) normalized orthogonal second pairs for each; thus there are \(300\) lines. Indeed the fifth-power norm \(\mathbb F_{16}\to\mathbb F_4\) takes each nonzero value five times, and the norm-one orthogonal complement is a one-dimensional norm-one torsor. No chart with first pivot later than \(0\) occurs because the Hermitian plane section \(X_0=0\) contains no line; the remaining chart with pivots \((0,3)\) has a row with a single nonzero coordinate, violating isotropy. Thus there are exactly \(325\) geometric lines.

The three coordinate pairings and the five fifth roots of unity in \(\mathbb F_{16}\) yield \(3\cdot5^2=75\) distinct coordinate-pair lines. The other \(250\) are exceptional. The coordinate-pair property is preserved by Frobenius.

**3. Frobenius and incidence enumeration.** Set \(\mathbb F_{16}=\mathbb F_2[\alpha]/(\alpha^4+\alpha+1)\). The attached `verify.py` enumerates all \(70161\) RREF representatives of two-planes over this field, tests the three Hermitian isotropy equations, and constructs all \(325\) lines. It applies coefficientwise squaring, returns to RREF, and computes the Frobenius cycles. For any chart with fixed pivot columns, write the remaining two columns as a matrix \(B\). The line \(L\) meets \(\sigma^r L\), for \(r=1,2\), precisely if
\[
\det\bigl(B+B^{(2^r)}\bigr)=0.
\]
The verifier also checks this criterion independently by taking the rank of the stacked four-by-four row matrices. An orbit of four lines is determined up to the four graph types in the theorem by these two incidence tests, since squaring cyclically permutes the four vertices. Exhaustive pivot-chart counts are:

| Pivot chart | Fixed | Two-cycles | Empty | Matching | Four-cycles | Four-cliques |
|---|---:|---:|---:|---:|---:|---:|
| \((0,1)\) | \(2\) | \(1\) | \(44\) | \(14\) | \(12\) | \(4\) |
| \((0,2)\) | \(1\) | \(0\) | \(4\) | \(0\) | \(0\) | \(2\) |

Separating these entries into coordinate-pair and exceptional lines produces exactly the theorem's first table. Each count is asserted by the complete deterministic verifier, rather than inferred from sampling.

**4. Rational points and concurrency.** A line defined over \(\mathbb F_4\) must lie in the plane \(X_0+X_1+X_2+X_3=0\), since fifth powers of elements of \(\mathbb F_4\) are squares. On this plane the dot-product form becomes alternating with one-dimensional radical generated by \((1,1,1,1)\). Its totally isotropic two-planes are exactly the five planes containing this radical; hence the five \(\mathbb F_4\)-lines pass through \(P\). The verifier checks that exactly three are fixed by the \(\mathbb F_2\)-Frobenius. All seven \(\mathbb F_2\)-points of \(S\) are the nonzero even-parity binary quadruples; precisely six are not \(P\). Any four-clique of lines on a smooth Hermitian surface is concurrent, because its tangent-plane section at a pairwise intersection is a five-line star; Frobenius-invariance forces its center to lie in \(S(\mathbb F_2)\). The six four-cliques each have a distinct center away from \(P\), as also verified directly using RREF span tests, proving the last statement.

## Verification

Run `python3 verify.py` using the Python standard library. The code implements \(\mathbb F_{16}\) arithmetic, enumerates every one of the \(70161\) RREF two-planes, checks the line equations, both Frobenius incidences in two independent ways, the coordinate-pair split, all orbit-type counts, and the six rational centers. Its deterministic success line begins `VERIFY_OK`. The exhaustive search is finite and complete **because** step 1 independently proves that every geometric line is \(\mathbb F_{16}\)-rational. The derived finite étale scheme statement does not rely on computational extrapolation to arbitrary fields.

## Relationship to prior work

The Hermitian nature of this Fermat quintic, the general \((q^3+1)(q+1)\) line count, and the geometry of stars are established features of Hermitian and smooth extremal surfaces; they are not claimed as new. Homma–Kim describe Hermitian surfaces through finite-field rational point geometry. Blake–Murty–Usefi study diagonal and Hermitian surfaces principally via point counts and zeta functions. Brosowsky–Page–Ryan–Smith give the total line count, star geometry, automorphism groups, and general line incidence. The present calculation instead gives the **prime-field descent of the Fano scheme together with the four distinct graph types on each Frobenius quartet, separated between the 75 coordinate-pair and 250 exceptional lines**. No such joint arithmetic-incidence classification was located in the cited works or in the other checked records.

## Limitations

The classification is for this exact \(\mathbb F_2\)-model, not an arbitrary form of the Hermitian surface. It concerns lines and their pairwise geometric intersections, not every higher linear subsystem or intersection multiplicity. The computational certificate uses exhaustive arithmetic over the explicitly defined field; the algebraic field-of-definition and étaleness arguments are separate. While targeted literature comparisons revealed no equivalent prime-field incidence classification, older finite-polar-space literature, including Hirschfeld's monograph, has not been exhaustively checked for an equivalent formulation.

## References

1. M. Homma and S. J. Kim, *The characterization of Hermitian surfaces by the number of points*, arXiv:1304.0302 (first posted 2013-04-01), especially introduction and §3–4. https://arxiv.org/abs/1304.0302
2. I. Blake, V. K. Murty, and H. Usefi, *A note on diagonal and Hermitian surfaces*, arXiv:1411.3706 (first posted 2014-11-13), especially §§2–4. https://arxiv.org/abs/1411.3706
3. A. Brosowsky, J. Page, T. Ryan, and K. E. Smith, *Geometry of Smooth Extremal Surfaces*, arXiv:2110.15908 (first posted 2021-10-29), especially Theorem 3.2.1, Corollary 3.2.3, and Proposition 3.4.1. https://arxiv.org/abs/2110.15908
4. R. C. Bose and I. M. Chakravarti, *Hermitian varieties in a finite projective space \(\mathrm{PG}(n,q^2)\)*, Canad. J. Math. 18 (1966), 1161–1182.
5. J. W. P. Hirschfeld, *Finite Projective Spaces of Three Dimensions*, Oxford University Press (1985), chapter on Hermitian surfaces.
