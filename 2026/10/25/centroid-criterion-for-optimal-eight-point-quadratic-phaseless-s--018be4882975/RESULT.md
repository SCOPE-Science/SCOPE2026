# Centroid criterion for optimal eight-point quadratic phaseless sampling on parallel lines

## Finding

Let \(h\in\mathbb R\setminus\{0\}\), let \(r_1,r_2,r_3,r_4\) be distinct real numbers, and let \(s_1,s_2,s_3,s_4\) be distinct real numbers. Form the eight-point sample set
\[
\Omega=\{r_1,r_2,r_3,r_4\}\cup\{s_1+ih,s_2+ih,s_3+ih,s_4+ih\}.
\]
Then the following are equivalent:

1. Every pair of complex polynomials \(p,q\) of degree at most two satisfying \(|p(z)|=|q(z)|\) for every \(z\in\Omega\) obeys \(p=\tau q\) for some \(|\tau|=1\).
2. The longitudinal centroids of the two rows are different:
\[
\boxed{\sum_{j=1}^{4} r_j\ne\sum_{j=1}^{4}s_j.}
\]

The assertion holds for all coefficient choices, including vanishing leading coefficients and the zero polynomial. Rigid motions and complex-affine changes of the sampling coordinate preserve the criterion after expressing both rows in a common longitudinal coordinate. Eight samples are the smallest possible number for universal complex phase retrieval of a three-dimensional coefficient vector, even without any restriction on measurement vectors (the known dimension-three lower bound).

For example, the rows \(\{0,1,2,3\}\) and \(\{i,1+i,2+i,4+i\}\) recover every quadratic polynomial up to phase. Replacing the second row by \(\{i,1+i,2+i,3+i\}\) destroys this universality.

## Assumptions and scope

All coefficient vectors belong to \(\mathbb C^3\), all sample nodes are known exactly, the four positions *within each row* are pairwise distinct, and the lines are distinct and parallel. Measurements consist solely of the eight magnitudes (or their squares) of the polynomial evaluations. No genericity assumption, coefficient nonvanishing assumption, random measurement model, or numerical reconstruction algorithm is used. The theorem concerns injectivity and makes no claim of a uniform noise-stability bound.

## Proof

**Step 1: Lift intensity comparisons.** Let \(v(z)=(1,z,z^2)^T\). For any Hermitian \(3\times3\) matrix \(K\), let \(Q_K(z)=v(z)^*Kv(z)\). The eight intensity measurements are injective up to global phase if and only if their real-linear kernel contains no nonzero Hermitian matrix of rank at most two. Indeed, equality of the intensities of polynomials \(p\) and \(q\) gives a kernel matrix equal to the difference of their two rank-one coefficient Gram matrices; conversely, a nonzero indefinite rank-two kernel matrix admits such a positive-minus-negative spectral decomposition. A nonzero semidefinite matrix cannot lie in the kernel because three distinct evaluations already span \(\mathbb C^3\) by Vandermonde interpolation. Thus every nonzero singular Hermitian kernel element, if present, has rank exactly two and indefinite signature. This also follows from the standard Hermitian-lifting criterion for complex phase retrieval.

**Step 2: Compute the restrictions to parallel lines.** Write
\[
K=\begin{pmatrix}
a&u+iv&s+it\\
u-iv&b&w+ik\\
s-it&w-ik&c
\end{pmatrix}
\]
with all nine displayed variables real. Expanding at \(z=x+iy\) yields the exact identity
\[
\begin{aligned}
Q_K(x+iy)={}&a+b(x^2+y^2)+c(x^2+y^2)^2\\
&+2(ux-vy)+2\bigl(s(x^2-y^2)-2txy\bigr)\\
&+2(wx-ky)(x^2+y^2).
\end{aligned}
\]
On every horizontal line the coefficient of \(x^4\) is \(c\) and that of \(x^3\) is \(2w\), independent of the line height. Suppose \(K\) vanishes at all eight sample nodes. The two restricted polynomials, each of degree at most four, vanish at four distinct real values. Therefore, with
\[
A(x)=\prod_{j=1}^{4}(x-r_j),\qquad B(x)=\prod_{j=1}^{4}(x-s_j),
\]
one has the polynomial identities
\[
Q_K(x)=cA(x),\qquad Q_K(x+ih)=cB(x)
\]
for every real \(x\). In particular, the equal cubic coefficients imply
\[
\boxed{c\left(\sum_jr_j-\sum_js_j\right)=0.}
\]

**Step 3: Unequal centroids are sufficient.** If the two sums differ, the last identity forces \(c=0\). Since both restricted polynomials have degree at most three and vanish at four distinct locations, they are identically zero. Comparing coefficients in \(Q_K(x)=0\) forces \(w=u=a=0\) and \(b=-2s\). Comparing \(Q_K(x+ih)=0\) subsequently yields \(k=t=0\) and \(v=-2hs\). Thus the entire measurement kernel is the one-dimensional real span of
\[
H_h=\begin{pmatrix}
0&-2ih&1\\
2ih&-2&0\\
1&0&0
\end{pmatrix},\qquad Q_{H_h}(x+iy)=4y(h-y).
\]
A direct determinant calculation gives \(\det H_h=2\), regardless of \(h\). Every nonzero kernel matrix consequently has full rank three; by Step 1 the intensity map is injective up to global phase.

**Step 4: Equal centroids are necessary.** Suppose the two sums are equal. The real kernel contains \(H_h\) as above. It also contains a matrix \(K_1\) with \(c=1\): take the desired restrictions \(Q_{K_1}(x)=A(x)\) and \(Q_{K_1}(x+ih)=B(x)\). Their coefficients of \(x^4\) and \(x^3\) agree; choose \(c=1\) and \(w\) to match them. The four coefficients on the first line determine \(a,u,b+2s\), leaving \(s\) free. On the second line the remaining \(x^2\), \(x\), and constant coefficients are matched successively by choosing \(k\), \(t\), and \(v\), respectively; their coefficients are \(-2h\), \(-4h\), and \(-2h\), all nonzero. Hence \(K_1\) exists and is independent of \(H_h\).

Now consider the real cubic \(F(t)=\det(K_1+tH_h)\). Its leading coefficient is \(\det H_h=2\), so \(F\) has at least one real zero. At such a zero, \(K_1+tH_h\) is a nonzero singular Hermitian kernel element because its bottom-right entry remains \(1\). By Step 1 it has rank two and opposite-sign nonzero eigenvalues. Splitting it into its positive and negative rank-one parts produces two quadratic polynomials that are not unimodular multiples but have identical magnitudes at every sample node. Therefore equal centroids always fail universal phase retrieval.

This proves both directions. Since rigid motions reduce arbitrary distinct parallel lines to the displayed normal form without changing polynomial degree or phase equivalence, it also proves the geometric formulation. The known lower bound of eight general complex intensity measurements in dimension three shows that the sample count is globally optimal.

## Verification

The accompanying `checker.py` uses exact SymPy polynomial and matrix arithmetic to verify the Hermitian expansion's leading terms, the universal full-rank null direction, and six representative eight-node linear-system ranks (both success and failure geometries). The recorded output is in `checker_output.txt`. These finitely many tests are supplementary; the determinant and interpolation arguments above prove the unrestricted all-node theorem.

## Relationship to prior work

Conca, Edidin, Hering and Vinzant analyze general complex phase retrieval and state the Hermitian rank-two obstruction and the dimension-three minimal count of eight measurements. These general criteria do not themselves give a complete injectivity classification for point evaluations lying four per parallel line. Przybyłek and Siedlecki establish nonadaptive phaseless polynomial reconstruction from a larger polar sampling grid and discuss insufficiency of poorly chosen sample locations; their explicit general grid uses \((2n+1)^2\) measurements at degree \(n\), or twenty-five for degree two. Wellershoff characterizes equal-magnitude finite-order entire functions on two *complete* parallel lines; the present question uses only four evaluations on each and gives a necessary-and-sufficient centroid test. Liehr considers uniqueness on collections of entire parallel lines for function classes containing exponentials, rather than finite samples on the degree-two polynomial subspace.

## Limitations

The result assumes exactly four distinct sites per row, and no analogous criterion is proved for uneven allocations or degree at least three. Global injectivity should not be confused with numerical conditioning: as the two row centroids approach equality, stability may deteriorate, but no optimal stability estimate is asserted. General phase-retrieval lower bounds and existing infinite-line uniqueness theorems are not claimed as new. Published-literature searches cannot exclude all obscure equivalent formulations, so bibliographic priority remains subject to independent confirmation.

## References

- A. Conca, D. Edidin, M. Hering and C. Vinzant, *An algebraic characterization of injectivity in phase retrieval*, arXiv:1312.0158, especially Proposition 3.1 and §2.1. https://arxiv.org/abs/1312.0158
- M. R. Przybyłek and P. Siedlecki, *A note on complexity of a phaseless polynomial interpolation*, arXiv:1907.09371, especially §4 and Theorem 4.2. https://arxiv.org/abs/1907.09371
- M. Wellershoff, *Phase retrieval of entire functions and its implications for Gabor phase retrieval*, arXiv:2202.03733, especially §3.2 and Theorem 10. https://arxiv.org/abs/2202.03733
- L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, Bull. Lond. Math. Soc. 56 (2024), 3316–3330, especially Theorem 1.1. https://doi.org/10.1112/blms.13134
