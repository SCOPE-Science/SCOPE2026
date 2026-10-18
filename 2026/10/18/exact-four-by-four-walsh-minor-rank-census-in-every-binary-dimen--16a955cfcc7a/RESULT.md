# Exact four-by-four Walsh minor rank census in every binary dimension

## Finding
Let \(d\ge3\), \(N=2^d\), and let \(H_d\) be the unnormalized Walsh--Fourier matrix indexed by \(x,y\in\mathbb F_2^d\), with entry \((-1)^{x\cdot y}\). Among all ordered pairs \((R,C)\) of four-element row and column *sets*, every \(4\)-by-\(4\) submatrix has complex rank in \(\{1,2,3,4\}\), and every nonzero determinant has modulus \(8\) or \(16\). The following formulas are **complete for all dimensions**.

Write \(P=N(N-1)(N-2)/24\), \(T=N(N-1)(N-2)(N-4)/24\), \(u=N/4\), and \(v=N/8\). Let \(A_j\) count submatrices of rank \(j\), with \(\binom{m}{k}=0\) for \(k>m\). Then
\[
\begin{aligned}
A_1&=4P\binom{u}{4}+8T\binom{v}{4},\\
A_2&=6P\bigl(2u\binom{u}{3}+\binom{u}{2}^2\bigr)+28T\bigl(2v\binom{v}{3}+\binom{v}{2}^2\bigr),\\
A_3&=12P\binom{u}{2}u^2+T\bigl(168\binom{v}{2}v^2+12v^4\bigr),\\
A_4&=Pu^4+58Tv^4.
\end{aligned}
\]
Moreover, the two nonzero absolute-determinant counts are
\[
\#\{|\det|=8\}=56Tv^4,\qquad
\#\{|\det|=16\}=Pu^4+2Tv^4.
\]
The counts sum to \(\binom{N}{4}^2\), and in particular the vanishing determinant count is \(A_1+A_2+A_3\).

A structural form of the result determines **each individual minor**, not just its global rank count. If \(R\) is an affine plane, the rank is the number of distinct projections of \(C\) into the four-character dual of the row-direction plane; rank four then has determinant modulus \(16\). If \(R\) is affine-independent, the relevant projection has eight values; with fewer than four distinct images the rank equals that number. With four distinct images, an affine-independent projected quadruple yields rank four and determinant modulus \(8\); an affine plane in the image yields rank four and modulus \(16\) exactly when it is one of the two cosets of the even-weight plane, and otherwise yields rank three.

For example, the complete rank multiplicities are \((0,84,1344,3472)\) at \(N=8\), and \((560,104160,1612800,1594880)\) at \(N=16\). The absolute-determinant multiplicities \((0,8,16)\) at \(N=16\) are respectively \((1717520,1505280,89600)\).

## Assumptions and scope
All ranks are over \(\mathbb C\) (equivalently over \(\mathbb Q\) for these integer matrices). The matrix is not divided by \(\sqrt N\). Row and column selections are unordered four-element sets; the pair \((R,C)\) is ordered, and exchanging row and column sets gives a transpose, not a new category. Multiplicities count such pairs once each. We study the full Fourier matrix on the elementary abelian binary group, **not** an arbitrary Hadamard matrix of the same order. The formulas hold for every integer \(d\ge3\).

Given an affine-independent row quadruple \(R=\{r_0,r_1,r_2,r_3\}\), define the projection \(\rho_R:\mathbb F_2^d\to\mathbb F_2^3\) by \(\rho_R(c)=((r_1+r_0)\cdot c,(r_2+r_0)\cdot c,(r_3+r_0)\cdot c)\). It is surjective and its fibers each have size \(v\). Changing the chosen first row and ordering changes coordinates but not rank or determinant modulus. The even-weight-plane test is to be applied in coordinates arising from this specified ordering.

## Proof
**1. Affine row orbits.** Every four-point set in a vector space over \(\mathbb F_2\) is either an affine two-plane, equivalently its four-point sum is zero, or an affine-independent three-simplex. To count planes, choose a base point and two independent directions, then divide by the \(4\) base choices and \(6\) ordered direction bases. This gives \(P=N(N-1)(N-2)/24\). Subtracting from \(\binom{N}{4}\) gives \(T=N(N-1)(N-2)(N-4)/24\). The affine group is transitive separately on both types.

**2. Dephasing and a local three-by-three problem.** Translate a chosen first row and first column to zero and multiply rows and columns by signs. These operations preserve ranks and absolute determinants. For an affine-independent row set, the normalized \(4\)-by-\(4\) matrix consists of a top row and a left column of ones; its lower-right entries are \((-1)^{z_i}\), where the three-bit labels \(z\) run over the projections of the selected columns. Subtracting the first row from the other three rows and the first column from the other columns shows that if the four projected columns are distinct, the determinant equals \(\pm8\det B\), where the \(3\)-by-\(3\) integer matrix \(B\) has as columns the three nonzero projected differences written in \(\{0,1\}^3\). In general, the original matrix rank is one plus the rank of \(B\). A repeated projected column gives a repeated normalized column, so the rank equals the number of distinct projected values when that number is at most three: any three different vertices of the cube are affinely independent over \(\mathbb R\).

**3. Complete local four-point classification.** There are \(\binom{8}{4}=70\) four-element subsets of the projection cube. Of these, \(56\) are affine-independent and \(14\) are affine planes. For an affine-independent set, the three difference columns form a basis over \(\mathbb F_2\), so \(\det B\) is odd. The determinant of a three-by-three zero-one matrix has absolute value at most two, hence \(|\det B|=1\) and \(|\det H_{R,C}|=8\).

For an affine plane, after translating one vertex to zero its other vertices have binary labels \(a,b,a+b\) (addition in \(\mathbb F_2^3\)). Regarding these labels as integer columns, \(a\oplus b=a+b-2(a\odot b)\), and hence \(\det[a,b,a\oplus b]=-2\det[a,b,a\odot b]\). This vanishes except when the supports of \(a,b\) overlap in one coordinate and each has one additional, different coordinate. Thus the only nonzero case is the two cosets of the three-bit even-weight plane; there \(|\det B|=2\), giving \(|\det H_{R,C}|=16\). The other twelve affine planes yield rank three, since their three nonzero labels still give three independent columns of the four-row Walsh restriction.

**4. The affine-plane row case.** If \(R\) is an affine two-plane, each character column is determined up to a scalar sign by its restriction to the two-dimensional row-direction subspace. The four distinct restrictions are the four columns of the order-four Walsh matrix, which are orthogonal. Each restriction type has exactly \(u=N/4\) lifts. Hence rank is exactly the number of different types represented, and selection of one of each type produces a four-by-four Hadamard determinant of modulus \(16\).

**5. Exact multiplicities.** For \(s\) projection types, each with \(m\) lifts, four-column subsets with precisely one, two, or three distinct types number respectively
\[
 s\binom{m}{4},\qquad
 \binom{s}{2}\left(2m\binom{m}{3}+\binom{m}{2}^2\right),\qquad
 3\binom{s}{3}\binom{m}{2}m^2.
\]
The three-type formula follows because exactly one represented type is used twice. Apply these with \((s,m)=(4,u)\) for each of the \(P\) plane row sets, and \((s,m)=(8,v)\) for each of the \(T\) independent row sets. For four distinct types, the plane-row case has \(u^4\) choices, all determinant modulus \(16\). The independent-row case has \(70v^4\) choices, of which \(56v^4\) have modulus \(8\), \(2v^4\) have modulus \(16\), and \(12v^4\) have rank three. Collecting terms proves the four rank formulas and both determinant formulas. Every column set belongs to exactly one of these disjoint cases, proving exhaustiveness in every dimension.

## Verification
The standalone `CHECK.cpp` separately constructs every four-row and four-column subset of the actual binary Walsh matrix in dimensions three and four. It computes the exact integer rank and determinant of each four-by-four minor by dephased integer elimination and compares the exhaustive results against the closed multiplicity formulas, including the affine row-type counts. Compile with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic CHECK.cpp -o check` and execute `./check`. The completed verification returned, respectively, the rank vectors \((0,84,1344,3472)\) and \((560,104160,1612800,1594880)\), and the determinant-modulus counts listed in the finding. This is exact finite corroboration; the proof above is uniform over all \(d\ge3\).

## Relationship to prior work
Krahmer, Pfander, and Rashkov [1, Section 3, Table 1 and Proposition 3.6] connect finite Fourier minor ranks to support uncertainty and tabulate small cyclic examples; this establishes the relevance of minor ranks, but not the all-dimensional binary rank histogram here. Brent and Osborn [2, Sections 4--5 and the appendix] tabulate determinant spectra of maximal-determinant matrices through order twenty-one. In particular, one of their order-sixteen Hadamard classes has \(1{,}717{,}520\) vanishing four-by-four minors, consistent with the present order-sixteen computation. Their order-limited tables do not assert the rank-one/rank-two/rank-three subdivision or an all-power-of-two classification; the universal Hadamard statements in [2] concern minors of orders two and three, not four.

A published classification of simultaneous orthogonal four-character Walsh spectra [3] implies the characterization and count of the \(|\det|=16\) submatrices, which is **not** presented as a separate new theorem. A published four-sparse Walsh support-spectrum classification [4] concerns nonzero Fourier support for arbitrary four-sparse coefficient vectors; it does not supply the exact incidence of all rank-two, rank-three, and determinant-eight four-by-four Fourier restrictions. The distinguishing contribution here is the complete rank-by-affine-type incidence law and all singular rank strata, not either aggregate determinant count in isolation. Indeed, the determinant-eight total follows from the known orthogonal count, the possible determinant moduli, and Cauchy--Binet.

## Limitations
The result does not classify larger minors, arbitrary Hadamard equivalence classes, or nonbinary finite fields. Existing order-eight and order-sixteen numerical observations are known; their re-enumeration is not by itself a novelty claim. The proof uses a dimension-independent, three-coordinate reduction and a closed combinatorial count, not a numerical extrapolation. Historical small-minor statistics in sources not inspected here could contain an equivalent all-dimension formula. Independent external validation has not been performed.

## References
1. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first posted 2006-11-16, https://arxiv.org/pdf/math/0611493.
2. R. P. Brent and J.-a. H. Osborn, *On minors of maximal determinant matrices*, arXiv:1208.3819, first posted 2012-08-19, https://arxiv.org/pdf/1208.3819.
3. *Linearization and exact multiplicity of simultaneous four-point Walsh spectra*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-linearization-and-exact-multiplicity-of-simultaneous-four-point--171a2694aaac.
4. *Four-sparse Walsh spectra are controlled by affine dimension on binary vector groups*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-four-sparse-walsh-spectra-are-controlled-by-affine-dimension-on--1491c27461f4.
