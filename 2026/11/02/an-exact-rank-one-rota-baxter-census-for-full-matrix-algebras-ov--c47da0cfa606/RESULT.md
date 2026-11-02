# An exact rank-one Rota–Baxter census for full matrix algebras over finite fields

## Finding

For every prime power \(q\) and integer \(n\geq 3\), the number of nonzero rank-one weight-zero Rota–Baxter linear operators on \(M_n(\mathbb F_q)\) is the sum of two explicitly enumerated families, distinguished by whether the product on their one-dimensional images vanishes. The formulas below also hold at \(n=2\), where existing low-dimensional classifications provide prior partial coverage; the all-size finite-field census is the focus here.

Write \({m\brack r}_q\) for the Gaussian binomial coefficient and \(g_r(q)=|\operatorname{GL}_r(\mathbb F_q)|\). Define
\[
S_{n,q}=\sum_{r=1}^{\lfloor n/2\rfloor}
\frac{{n\brack r}_q{n-r\brack r}_q g_r(q)}{q-1}
\bigl(q^{(n-r)^2}-1\bigr),
\]
\[
I_{n,q}=2\sum_{r=1}^{n-1}{n\brack r}_q q^{r(n-r)}
\bigl(q^{r(n-r)}-1\bigr).
\]
Then the exact number is \(T_{n,q}=S_{n,q}+I_{n,q}\). The two summands count operators whose nonzero image matrices are, respectively, square-zero and scalar multiples of nontrivial idempotents. Each family is further rank-refined by the displayed summation index.

Every operator counted here satisfies \(R^2=0\) as a linear endomorphism, although the operators in the second family have images that are one-dimensional nonzero-product subalgebras. In particular, \(T_{3,2}=651\), partitioned as \(315+336\). For fixed \(n\geq3\), \(T_{n,q}\sim q^{n^2-2}\) as the field size tends to infinity through prime powers; the leading term comes only from the rank-one square-zero image matrices.

## Assumptions and scope

Let \(k\) be an arbitrary field and \(n\geq2\). A weight-zero Rota–Baxter operator on the associative algebra \(A=M_n(k)\) is a \(k\)-linear map \(R:A\to A\) such that
\[
 R(X)R(Y)=R\bigl(R(X)Y+XR(Y)\bigr)
 \quad\text{for all }X,Y\in A.
\]
Rank one means rank one **as a linear transformation on the \(n^2\)-dimensional space** \(A\), not rank one of each output matrix. There is no characteristic restriction. Put \(V=k^n\), and write \(\operatorname{tr}\) for the ordinary matrix trace, which gives a nondegenerate bilinear pairing even in positive characteristic.

The structural classification holds over every field. The enumerations require \(k=\mathbb F_q\). We count individual operators, not orbits under conjugation, transpose, or scalar equivalence.

## Proof

**1. Reduction to a tensor equation.** Every nonzero rank-one linear map has a presentation
\[
R(X)=\operatorname{tr}(BX)A_0,\qquad A_0,B\in M_n(k)\setminus\{0\},
\]
unique up to simultaneous rescaling \((A_0,B)\mapsto(cA_0,c^{-1}B)\), \(c\in k^\times\). Substitution of \(X,Y\) with nonzero trace pairings shows that \(A_0^2=\lambda A_0\) for a unique \(\lambda\in k\). The defining identity then reads
\[
\lambda\phi(X)\phi(Y)
=\phi(X)\phi(A_0Y)+\phi(Y)\phi(XA_0),
\qquad \phi(X)=\operatorname{tr}(BX).
\]
Choose \(X_0\) with \(\phi(X_0)=1\), and compare first with \(Y\in\ker\phi\), then with \(X=X_0,Y=X_0\). It follows that for some \(\mu\in k\),
\[
\phi(A_0Y)=\mu\phi(Y),\qquad
\phi(XA_0)=(\lambda-\mu)\phi(X).
\]
Trace nondegeneracy gives the **necessary and sufficient** equations
\[
A_0^2=\lambda A_0,\quad BA_0=\mu B,
\quad A_0B=(\lambda-\mu)B. \tag{1}
\]
Applying \(A_0^2=\lambda A_0\) to \(BA_0=\mu B\), with \(B\ne0\), yields \(\mu^2=\lambda\mu\). Hence \(\mu=0\) or \(\mu=\lambda\), including when \(\lambda=0\).

**2. Square-zero image family.** If \(\lambda=0\), then \(A_0^2=0\) and (1) reduces exactly to
\[
A_0B=BA_0=0.\tag{2}
\]
Fix the line \(kA_0\) and write \(r=\operatorname{rank}A_0\). Necessarily \(1\leq r\leq\lfloor n/2\rfloor\). Condition (2) means that \(B\) kills \(\operatorname{im}A_0\) and has image in \(\ker A_0\). Thus \(B\) is an arbitrary map \(V/\operatorname{im}A_0\to\ker A_0\), from a vector space of dimension \(n-r\) to one of the same dimension. Exactly \(q^{(n-r)^2}-1\) such nonzero \(B\) exist for a fixed representative \(A_0\) of its line.

A rank-\(r\) square-zero matrix is obtained uniquely by choosing \(U=\operatorname{im}A_0\), then \(K=\ker A_0\supset U\), and then an isomorphism \(V/K\to U\). This yields
\[
{n\brack r}_q{n-r\brack r}_q g_r(q)
\]
matrices. Their nonzero scalar multiples form \((q-1)\)-element lines. Multiplying their number of lines by the preceding \(B\)-fiber count yields the summand of \(S_{n,q}\) at \(r\).

**3. Idempotent-image family.** If \(\lambda\ne0\), the line \(kA_0\) contains the unique nonzero idempotent \(E=\lambda^{-1}A_0\), and \(1\leq r=\operatorname{rank}E\leq n-1\), since (1) excludes \(E=1\). Normalize \(R(X)=\operatorname{tr}(CX)E\). Equations (1) become either
\[
CE=0,\quad EC=C,
\qquad\text{or}\qquad
CE=C,\quad EC=0. \tag{3}
\]
Relative to \(V=\operatorname{im}E\oplus\ker E\), these are exactly the nonzero upper-right and lower-left rectangular blocks, each with \(r(n-r)\) independent entries. Their only intersection is zero, so they give \(2(q^{r(n-r)}-1)\) choices of \(C\). The number of rank-\(r\) idempotents is \({n\brack r}_q q^{r(n-r)}\): choose the image and a complementary kernel. Summing gives \(I_{n,q}\).

Each rank-one operator has a unique image line. A square-zero line cannot be an idempotent line, and the idempotent within a nonzero-product line is unique; therefore no overcount occurs. This proves the full formula.

**4. Linear square-zero property and asymptotic.** In (2), \(BA_0=0\) implies \(\operatorname{tr}(BA_0)=0\). In (3), at least one of \(CE=0\) or \(EC=0\) holds; trace cyclicity gives \(\operatorname{tr}(CE)=0\) in both cases. Consequently \(R^2=0\). The square-zero rank-\(r\) term has degree \(n^2-r^2-1\) in \(q\), while the idempotent rank-\(r\) term has degree \(3r(n-r)\). For each fixed \(n\ge3\), the unique highest degree is \(n^2-2\), from square-zero rank \(r=1\), with leading coefficient one. This proves the stated asymptotic.

## Verification

The standalone `verify.py` performs direct finite-field matrix multiplication and independently checks the Rota–Baxter equation on every ordered pair of matrix units for complete small-field configurations. It exhaustively enumerates normalized output-matrix lines and nonzero trace functionals and compares their resulting counts with both rank-refined formulas. The test suite includes \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2)\); the degree-two extension field is represented by a polynomial quotient. Results for the five configurations are respectively \(15,56,135,264,651\), with square-zero versus idempotent partitions \((3,12),(8,48),(15,120),(24,240),(315,336)\). Exhaustive **direct identity evaluation** is carried out for all candidate normalized pairs in the first three configurations, and for all admitted pairs in the remaining two. The program prints `RANK_ONE_MATRIX_RB_EXACT_CENSUS_OK 5 9055`. The general statement is proved symbolically above; finite tests are not an infinite proof.

To reproduce: run `python3 verify.py` with a Python 3 standard-library interpreter. No external packages or network are required.

## Relationship to prior work

Guo, Rosenkranz, and Zheng (arXiv:1407.5306v1, 20 July 2014, particularly Sections 1–3) study Rota–Baxter operators on polynomial algebras; their monomial/injective classification concerns a different algebra and does not imply these finite matrix counts. Gubarev (arXiv:1805.00723v3, Sections 3.3, 5.1, 5.4) proves the general matrix correspondence with the associative Yang–Baxter equation, gives constructions, and reproduces the established classification for \(M_2\) over algebraically closed fields up to equivalences. This is partial prior coverage of the dimension-two boundary, not an exact \(\mathbb F_q\)-census over arbitrary size. Its matrix examples are not asserted to be new here. The present result is a rank-one, all-size, characteristic-independent finite-field census, rather than a classification of all Rota–Baxter operators of higher linear rank.

Searches found related algebraic classifications but did not establish a published all-size count identical to \(T_{n,q}\). This is a best-knowledge originality assessment, not a priority guarantee.

## Limitations

Only nonzero **linear-rank-one**, weight-zero operators are classified. The proof does not count operators of higher linear rank, their conjugacy classes, scheme multiplicities, or arbitrary associative algebras. Earlier classifications already cover aspects of \(M_2\) up to equivalence. The exact finite-field census does not imply an orbit classification. Bibliographic completeness and independent validation remain open.

## References

1. Li Guo, Markus Rosenkranz, and Shanghua Zheng, *Rota-Baxter operators on the polynomial algebras, integration and averaging operators*, arXiv:1407.5306v1 (2014), first submitted 20 July 2014, https://arxiv.org/abs/1407.5306.
2. Vsevolod Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723v3 (2019), original submission 2 May 2018, https://arxiv.org/abs/1805.00723.
3. G. Baxter, *An analytic problem whose solution follows from a simple algebraic identity*, Pacific J. Math. 10 (1960), 731–742 (background definition).
