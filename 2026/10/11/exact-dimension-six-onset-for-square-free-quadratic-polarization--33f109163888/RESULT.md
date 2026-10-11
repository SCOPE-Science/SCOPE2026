# Exact dimension-six onset for square-free quadratic polarization on \(\ell_\infty^n\)

## Finding

For an integer \(n\ge2\), let \(\mathcal Z_n\) be the space of real symmetric \(n\times n\) matrices with zero diagonal. For \(A\in\mathcal Z_n\), define the associated quadratic polynomial and symmetric bilinear form by
\[
P_A(x)=x^{\mathsf T}Ax,\qquad B_A(x,y)=x^{\mathsf T}Ay
\]
on the real space \(\ell_\infty^n\). Write \(\|P_A\|=\sup_{\|x\|_\infty\le1}|P_A(x)|\), \(\|B_A\|=\sup_{\|x\|_\infty,\|y\|_\infty\le1}|B_A(x,y)|\), and define the square-free quadratic polarization constant
\[
c_n^{\mathrm{sf}}=\sup_{0\ne A\in\mathcal Z_n}\frac{\|B_A\|}{\|P_A\|}.
\]
Then
\[
\boxed{c_n^{\mathrm{sf}}=1\quad(2\le n\le5),\qquad c_6^{\mathrm{sf}}=\frac32.}
\]
For every \(n\ge6\), moreover, \(c_n^{\mathrm{sf}}\ge3/2\) by zero-padding the six-dimensional extremizer. Thus dimension six is the first dimension at which the square-free quadratic and symmetric bilinear supremum norms can differ; the optimal loss there is exactly fifty percent.

## Assumptions and scope

All spaces and coefficients are **real**. The matrix is arbitrary apart from symmetry and the vanishing diagonal. Equivalently, the homogeneous polynomial is tetrahedral (square-free): no monomial has a repeated coordinate. The bilinear form is the unique symmetric polarization of its polynomial. The operator and polynomial norms are over closed unit cubes, with no restriction on matrix signs, rank, or sparsity. This theorem does **not** determine \(c_n^{\mathrm{sf}}\) for \(n\ge7\).

## Proof

**1. Reduction to signs.** Because the diagonal of \(A\) vanishes, \(P_A(x)=2\sum_{i<j}a_{ij}x_ix_j\) is affine in each coordinate separately. Thus the maximum of its absolute value over the unit cube occurs at a sign vector. The bilinear function \(B_A(x,y)\) is separately affine in all \(2n\) coordinates, so its absolute maximum also occurs at two sign vectors. Consequently it suffices to prove the asserted inequalities for \(x,y\in\{-1,1\}^n\).

**2. Cut cancellation and a block bound.** Conjugating \(A\) by the diagonal sign matrix determined by \(x\) preserves both norms and converts \(x\) to the all-ones vector. Let \(U=\{i:y_i=1\}\) and \(V=\{i:y_i=-1\}\), and put
\[
a=\sum_{i,j\in U}a_{ij},\qquad b=\sum_{i,j\in V}a_{ij}.
\]
The two cross-block sums in \(B_A(\mathbf1,y)\) cancel because \(A\) is symmetric, and therefore \(B_A(\mathbf1,y)=a-b\). For arbitrary signs \(u\) on \(U\) and \(v\) on \(V\), write \(q_U(u)=\sum_{i,j\in U}a_{ij}u_iu_j\) and similarly \(q_V(v)\). Since the cross terms change sign upon replacing \(v\) by \(-v\),
\[
\frac12\big(P_A(u,v)+P_A(u,-v)\big)=q_U(u)+q_V(v).
\]
Hence, for \(M=\|P_A\|\),
\[
M\ge\left|q_U(u)+q_V(v)\right|\tag{1}
\]
for every within-block pair of sign assignments (including empty blocks).

**3. A block of size at most two.** On a block of size zero or one, the quadratic form vanishes. On a two-element block, changing just one sign reverses its quadratic value. Thus whenever \(\min\{|U|,|V|\}\le2\), there is a sign assignment on the smaller block yielding the negative of its all-ones value; keep all signs positive on the larger block. Equation (1) then gives \(M\ge|a-b|\). This covers every cut in dimensions \(2\le n\le5\), and every unbalanced cut in dimension six. Thus \(\|B_A\|\le\|P_A\|\) in dimensions two through five. The reverse inequality \(\|B_A\|\ge\|P_A\|\) holds because \(B_A(x,x)=P_A(x)\).

**4. The balanced cut in dimension six.** The only remaining case has \(|U|=|V|=3\). For a three-point, zero-diagonal quadratic form whose all-ones value is \(b\), the three sign patterns with exactly one negative coordinate have mean value \(-b/3\). Indeed, each off-diagonal pair contributes \(-1\) in the sum of its three sign products, compared to \(+3\) for all ones. Average (1) over these three assignments on \(V\), keeping all signs positive on \(U\), to obtain \(M\ge|a-b/3|\). Reversing the roles of the blocks gives \(M\ge|b-a/3|\). Therefore
\[
\frac43|a-b|=\left|(a-b/3)-(b-a/3)\right|\le2M,
\]
and consequently \(\|B_A\|\le(3/2)\|P_A\|\) for every real zero-diagonal symmetric six-by-six matrix.

**5. Sharpness and dimensional onset.** Split six coordinates into two triples. Set \(a_{ij}=1\) for distinct indices in the first triple, \(a_{ij}=-1\) for distinct indices in the second, and zero otherwise. On one triple, \(2(s_1s_2+s_1s_3+s_2s_3)\) takes precisely the two values \(6\) and \(-2\); the second block takes values \(-6\) and \(2\). The quadratic polynomial therefore has norm \(8\). Yet \(x=\mathbf1\) and \(y=(1,1,1,-1,-1,-1)\) give \(B_A(x,y)=12\). The ratio is \(12/8=3/2\), proving optimality in dimension six. For any larger dimension, adjoining zero rows and columns preserves these two norms and the ratio. This also demonstrates the strict onset exactly at dimension six.

## Verification

The standalone `CHECK.py` uses exact rational coefficients and exhaustively checks every one of the \(2^{2n}\) pairs of sign vectors for every \(2\le n\le6\). For each pair it constructs an **exact formal coefficient identity** expressing the bilinear matrix evaluation as a signed combination of quadratic sign evaluations, with total absolute coefficient mass at most \(1\) in dimensions two through five and at most \(3/2\) in dimension six. Those identities apply to **every real matrix**, not just tested numerical coefficients. The program checks all \(5456\) vertex pairs and verifies the six-dimensional extremizer has respective norms \(8\) and \(12\). Run `python CHECK.py` with Python 3 standard library. The preceding analytic proof is self-contained and does not depend on the executable.

## Relationship to prior work

Classical polarization compares the norm of a symmetric multilinear form with the supremum norm of its diagonal polynomial, over **all** homogeneous polynomials. Dimant, Galicer and Rodríguez [1] discuss this unrestricted constant and the symmetric operator norm property; Chatzakou and Sarantopoulos [2] establish broader estimates for polynomial norms. Their conditions allow diagonal monomials, whereas the present invariant restricts to vanishing diagonal and quantifies a new dimension threshold. The distinction is real: on \(\ell_\infty^2\), the diagonal matrix \(\mathrm{diag}(1,-1)\) has bilinear norm \(2\) and quadratic norm \(1\), while every **zero-diagonal** symmetric matrix in that dimension has equal norms.

Marceca [3, Chapter 6] compares a non-symmetric polarization of scalar polynomials and establishes dimension-dependent general bounds, rather than the symmetric square-free dimension-six constant. Alon, Makarychev, Makarychev and Naor [4] compare graph quadratic forms with vector-valued semidefinite relaxations; the numerator there is a different optimization over vectors, not the bilinear sign norm in this theorem. The present proof uses a local two-block sign geometry unavailable from these unrestricted bounds alone.

## Limitations

The conclusion is for real scalars; a complex analogue is not asserted. No sharp value for \(n\ge7\) is claimed, only the inherited \(3/2\) lower bound. Absence of a covering theorem from the cited comparisons is not a proof of absolute novelty; an equivalent formulation under matrix sign-norm or Boolean chaos terminology could exist. The verification program certifies exact coefficient identities in dimensions at most six but is not a calculation of higher-dimensional constants.

## References

[1] V. Dimant, D. Galicer, and J. T. Rodríguez, *The polarization constant of finite dimensional complex spaces is one*, arXiv:1908.08107, first public 2019-08-21. https://arxiv.org/abs/1908.08107

[2] M. Chatzakou and Y. Sarantopoulos, *Estimates for polynomial norms on Banach spaces*, arXiv:2107.05993, first public 2021-07-13. https://arxiv.org/abs/2107.05993

[3] F. Marceca, *Polinomios aleatorios en espacios de Banach y aplicaciones a series de Dirichlet*, doctoral thesis (2020), Chapter 6, especially Theorem 6.1.4. https://bibliotecadigital.exactas.uba.ar/download/tesis/tesis_n7019_Marceca.pdf

[4] N. Alon, K. Makarychev, Y. Makarychev, and A. Naor, *Quadratic Forms on Graphs*, Inventiones Mathematicae (2006). https://web.math.princeton.edu/~naor/homepage%20files/AM%5E2N.pdf
