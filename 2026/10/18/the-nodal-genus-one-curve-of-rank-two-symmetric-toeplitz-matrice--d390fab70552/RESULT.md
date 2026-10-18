# The nodal genus-one curve of rank-two symmetric Toeplitz matrices

## Finding
For every integer \(n\ge 4\) over an algebraically closed field \(k\) of characteristic zero, let \(D_n\subset\mathbb P^{n-1}_k\) be the **reduced** projective locus of nonzero symmetric Toeplitz matrices
\[
A_n(t)=(t_{|i-j|})_{0\le i,j<n},\qquad
[t_0:\cdots:t_{n-1}]\in\mathbb P^{n-1},\qquad \operatorname{rank}A_n(t)\le2.
\]
Then \(D_n=C_n\cup L_n\), with exactly two irreducible components:

1. \(C_n\) is the rational normal curve of degree \(n-1\), with projective parametrization
\[
[s:v]\longmapsto
\big[s^{n-1}T_0(v/s):s^{n-1}T_1(v/s):\cdots:s^{n-1}T_{n-1}(v/s)\big],
\]
where each homogeneous expression is interpreted by polynomial continuation at \(s=0\), and the Chebyshev polynomials satisfy \(T_0=1\), \(T_1(u)=u\), \(T_{j+1}(u)=2uT_j(u)-T_{j-1}(u)\). In particular \([s:v]=[0:1]\) maps to \([0:\cdots:0:1]\).
2. \(L_n\) is the projective line \(\{[a:b:a:b:\cdots]\}\) of two-periodic Toeplitz diagonals.

The two components meet in precisely the two reduced, transverse rank-one points \([1:1:\cdots:1]\) and \([1:-1:1:-1:\cdots]\). Thus \(D_n\) is connected, is nodal at exactly these two points, and has no other singularities as a **reduced curve**. It has projective degree \(n\), Hilbert polynomial \(P_{D_n}(d)=nd\), and arithmetic genus \(1\). Its normalization is \(\mathbb P^1\sqcup\mathbb P^1\).

## Assumptions and scope
The field is algebraically closed of characteristic zero, and \(n\ge4\). The geometric assertions concern the **reduced support** of the determinantal locus defined set-theoretically by the \(3\times3\) minors. No assertion is made that the unsaturated minor ideal is radical or that it has no embedded components. Homogeneous coordinates and ranks are taken in the indicated projective symmetric Toeplitz linear space, not the unrestricted matrix space. The index of the first diagonal is \(0\).

## Proof
**Step 1: the two families have rank at most two.** For \(L_n\), write \(e=(1,-1,1,-1,\ldots)^\top\) and \(\mathbf1=(1,\ldots,1)^\top\). Then a two-periodic matrix is
\[
\frac{a+b}{2}\mathbf1\mathbf1^\top+\frac{a-b}{2}ee^\top.
\]
For finite \(u\), choose \(z\in k^\times\) with \(u=(z+z^{-1})/2\). The identity \(T_j(u)=(z^j+z^{-j})/2\) implies
\[
T_{|i-j|}(u)=\frac12\big(z^iz^{-j}+z^{-i}z^j\big),
\]
a sum of two rank-one matrices. At \(s=0\), only \(t_{n-1}\) is nonzero, so the matrix has exactly its two corner entries nonzero and has rank two. As rank conditions are closed, this also follows by specialization.

**Step 2: the first principal minor separates the alternatives.** Write the first three Toeplitz coefficients as \(t_0,t_1,t_2\). Rank at most two forces
\[
0=\det A_n(t)_{\{0,1,2\},\{0,1,2\}}
=(t_0-t_2)\bigl(t_0(t_0+t_2)-2t_1^2\bigr).
\]
Suppose \(t_0^2-t_1^2\ne0\) and \(t_2=t_0\). The upper-left \(2\times2\) block is invertible and columns \(0\) and \(2\) have identical first two entries. As the entire matrix has rank at most two, these columns coincide, forcing \(t_j=t_{j-2}\) for every \(j\ge2\), hence membership in \(L_n\).

If \(t_0\ne0\) and \(t_0^2=t_1^2\) with \(t_2=t_0\), put \(\varepsilon=t_1/t_0\in\{\pm1\}\). The principal \(3\times3\) minor on indices \(\{0,1,j\}\), for \(j\ge2\), is \(-t_0(t_j-\varepsilon t_{j-1})^2\). Its vanishing inductively gives \(t_j=\varepsilon^jt_0\), one of the two rank-one points in \(L_n\cap C_n\). The subcase \(t_0=0\) and \(t_1\ne0\) has \(t_2=0\) from the displayed determinant and satisfies the invertible \(2\times2\) case, so also lies in \(L_n\).

Finally, if \(t_0\ne0\) and \(t_2\ne t_0\), the factorization yields \(t_2=2t_1^2/t_0-t_0\), and the leading \(2\times2\) determinant \(t_0^2-t_1^2=t_0(t_0-t_2)/2\) is nonzero. Put \(u=t_1/t_0\). The first two entries of column \(2\) equal those of \(2u\) times column \(1\) minus column \(0\); the full columns must agree by the rank bound. Consequently \(t_j=2ut_{j-1}-t_{j-2}\) for all \(j\ge2\), whence \(t_j=t_0T_j(u)\). This is in \(C_n\).

**Step 3: no exceptional projective coordinates are omitted.** It remains to consider \(t_0=t_1=0\). Let \(r\ge2\) be the least index with \(t_r\ne0\). If \(r\le n-3\), the submatrix in rows \(0,1,2\) and columns \(r,r+1,r+2\) is upper triangular with all three diagonal entries \(t_r\), contradicting rank at most two. If \(r=n-2\), the principal \(4\times4\) submatrix on indices \(0,1,n-2,n-1\) has determinant \(t_r^4\), also a contradiction. Therefore \(r=n-1\), giving precisely the Chebyshev point at infinity. This exhausts all projective rank-at-most-two Toeplitz matrices.

**Step 4: components, nodes and genus.** The coordinate polynomials \(s^{n-1}T_j(v/s)\), for \(0\le j<n\), constitute an invertible triangular linear transformation of the complete homogeneous monomial basis of degree \(n-1\). Thus \(C_n\) is a smooth rational normal curve of degree \(n-1\). The family \(L_n\) is a distinct smooth degree-one curve. On the affine chart \(t_0=1\), \(C_n\cap L_n\) requires \(T_2(u)=1\); since \(T_2(u)=2u^2-1\), the only solutions are \(u=\pm1\), both rank-one points. The curve \(C_n\) has tangent derivative \(dT_2/du=4u\), nonzero at both values, whereas \(L_n\) has constant coordinate \(t_2=1\) there. Hence their tangents are different. Their scheme-theoretic intersections are two reduced points and the reduced union has precisely two ordinary nodes.

Using the standard exact sequence
\[
0\to\mathcal O_{D_n}\to\mathcal O_{C_n}\oplus\mathcal O_{L_n}
\to\mathcal O_{C_n\cap L_n}\to0,
\]
we obtain \(P_{D_n}(d)=((n-1)d+1)+(d+1)-2=nd\). Hence \(\deg D_n=n\) and \(p_a(D_n)=1\). Since its two smooth components meet transversely, the disjoint union of their normalizations is \(\mathbb P^1\sqcup\mathbb P^1\).

## Verification
The standalone `CHECK.py` uses only the Python standard library. It verifies the exact integral polynomial identity \(T_{|i-j|}(u)=T_i(u)T_j(u)+(1-u^2)U_{i-1}(u)U_{j-1}(u)\) for \(0\le i,j<10\), where \(U_j\) are Chebyshev polynomials of the second kind, and enumerates all projective Toeplitz matrices for \(n\in\{4,5,6\}\) over \(\mathbb F_3\) and \(\mathbb F_5\). In each tested case, the computed rank-at-most-two set equals the Chebyshev points union the two-periodic line, with intersection consisting of two points. The checker returns `VERIFY_OK`. These finite tests are corroboration; the characteristic-zero proof is the exact argument above.

## Relationship to prior work
Chu, Funderlic and Plemmons studied structured low-rank approximation and rank-constrained Toeplitz matrices. Chu's dated 2004 lecture explicitly analyzes the factorization of the \(3\times3\) symmetric Toeplitz determinant as the union of a conic and a line, and gives eigenvector equations for the \(4\times4\) rank-two problem. This three-by-three case is existing work, not new here. The proposed result is the **uniform all-size projective classification for \(n\ge4\)** and its nodal intersection and arithmetic-genus description. Ottaviani, Spaenlehauer and Sturmfels give general methods for exact structured low-rank approximation, but their inspected article treats other structures rather than this two-component symmetric Toeplitz rank-two locus. The Chebyshev recurrence, rational-normal curves, and nodal-curve Hilbert polynomial are established mathematical tools and are not themselves claimed to be new.

## Limitations
This classification concerns only rank at most two, the symmetric Toeplitz linear space, and the reduced determinantal locus in characteristic zero. It does not identify the full scheme defined by all minors, prove radicality of that possibly nonreduced ideal, solve nearest-point approximation, or classify higher-rank Toeplitz strata. Previously unlocated equivalent formulations in the Toeplitz recurrence or algebraic-statistics literature remain a potential priority risk. Independent audit has not been performed.

## References
- M. T. Chu, R. E. Funderlic, R. J. Plemmons, *Structured Low Rank Approximation*, 2003, author-hosted text: https://mtchu.math.ncsu.edu/Research/Papers/ranklow.pdf .
- M. T. Chu, *Structured Low Rank Approximation, Lecture II: General Approach*, presented September 14, 2004, author-hosted slides: https://mtchu.math.ncsu.edu/Research/Lectures/Italy_2004/talk2a.pdf . See especially the slides on rank-one Toeplitz matrices, four-by-four rank-two equations, and the three-by-three conic/line example.
- G. Ottaviani, P.-J. Spaenlehauer, B. Sturmfels, *Exact Solutions in Structured Low-Rank Approximation*, accessible author copy: https://members.loria.fr/PJSpaenlehauer/data/papers/OttSpaStu14.pdf .
