# The complete distance spectrum and four-periodic quadratic embedding constant of folded cubes

## Finding
Let \(F_n\), for integer \(n\ge3\), be the graph obtained by identifying antipodal vertices in the binary \(n\)-cube. Its vertex group has \(2^{n-1}\) elements. The ordinary graph-distance matrix \(D_n\) is nonsingular, with a completely explicit signed Walsh spectrum. Its maximum Rayleigh quotient on the zero-sum subspace exhibits a sharp four-periodic change of extremizing harmonic.

Set \(r=\lfloor n/2\rfloor\), \(s=\lfloor(n-1)/2\rfloor\), and \(M_n=\binom{n-2}{\lfloor(n-2)/2\rfloor}\). The constant-function eigenvalue is
\[
\Lambda_0=n2^{n-2}-\frac n2\binom{n-1}{s}.
\]
For every integer \(1\le a\le r\), the eigenvalue on even Walsh weight \(j=2a\) is
\[
\boxed{\Lambda_{2a}=(-1)^a\frac{(2a-2)!(n-2a)!}{(a-1)!(r-a)!s!},\qquad \text{multiplicity }\binom n{2a}.}
\]
The constant weight has multiplicity one. These weights exhaust all characters of the quotient, and every displayed eigenvalue is nonzero. In particular,
\[
\boxed{\operatorname{In}(D_n)=\left(\sum_{j\equiv0\ (4)}\binom nj,\ 0,\ \sum_{j\equiv2\ (4)}\binom nj\right).}
\]
All binomial sums are over \(0\le j\le n\). The first component also equals \(2^{n-2}+2^{n/2-1}\cos(n\pi/4)\).

The quadratic embedding constant (maximum centered distance quadratic form) is exactly
\[
\boxed{Q_n=\max_{v\perp\mathbf1,\ \|v\|_2=1}v^TD_nv=
\begin{cases}
-1,&n=3,\\
M_n,&n\equiv0\pmod4,\\
M_n/(n-3),&n\equiv2\pmod4,\\
M_n/(n-2),&n\ge5\text{ odd}.
\end{cases}}
\]
For \(n\equiv0\pmod4\), the top nonconstant mode has full Walsh weight \(j=n\); for all odd \(n\ge5\), weight \(j=4\) attains the maximum (possibly tied); for \(n\equiv2\pmod4\), weight \(j=4\) also attains the maximum. The metric is conditionally negative semidefinite only for \(n=3\). The matrix \((e^{-t d(x,y)})_{x,y}\) is not positive semidefinite for all sufficiently small \(t>0\) when \(n\ge4\).

## Assumptions and scope
Write \(V=\mathbb F_2^n\), \(h=(1,\ldots,1)\), and \(G=V/\langle h\rangle\). The class of \(x\) is denoted \([x]\). Its Hamming weight is \(|x|\), and the graph on \(G\) has generators \([e_i]\), \(1\le i\le n\). Its shortest-path metric is
\[d([x],[y])=f(|x-y|),\quad f(k)=\min(k,n-k).\]
Indeed, the shortest representative of \([x-y]\) is either \(x-y\) or its complement. The \(2^{n-1}\) characters of \(G\) are precisely the restrictions \(\chi_a([x])=(-1)^{a\cdot x}\) with even \(|a|\). Euclidean norms and matrix eigenvalues use counting measure on \(G\), without dividing \(D_n\) by group order. Inertia counts strictly positive, zero, then strictly negative eigenvalues. The centered Rayleigh quotient is taken on the real zero-sum subspace.

## Proof
**Fourier reduction.** Translation invariance diagonalizes \(D_n\) on the quotient characters. For even \(j=|a|\), using the binary Krawtchouk coefficient \(K_j(k)=[z^k](1-z)^j(1+z)^{n-j}\),
\[
\Lambda_j=\frac12\sum_{k=0}^n f(k)K_j(k).
\]
The factor \(1/2\) corrects for the two representatives of each antipodal class. The character count at weight \(j\) is \(\binom nj\). For \(j=0\), the identity \(\sum_k\binom nk|k-n/2|=n\binom{n-1}{\lfloor(n-1)/2\rfloor}\) gives \(\Lambda_0=n2^{n-2}-(n/2)\binom{n-1}{s}>0\).

**Discrete curvature of the tent.** For \(j\ge2\), set \(R(z)=(1-z)^{j-2}(1+z)^{n-j}\). Multiplication of its coefficients by \((1-z)^2\) and summation by parts twice show that the only surviving terms are the two central finite second differences of \(f\). If \(n=2r\), the sole central curvature is \(-2\), giving
\[\Lambda_j=-[z^{r-1}]R(z).\]
If \(n=2r+1\), there are two adjacent curvatures \(-1\), giving
\[\Lambda_j=-\tfrac12([z^{r-1}]R(z)+[z^r]R(z)).\]
Because \(j\) is even, in the odd case \(R\) is reciprocal of degree \(2r-1\), so these two coefficients agree and \(\Lambda_j=-[z^{r-1}]R(z)\) there as well.

**Central binomial evaluation.** Put \(j=2a\), \(u=a-1\), and \(v=r-a\), so \(u+v=r-1\). In the even case
\[R(z)=(1-z)^{2u}(1+z)^{2v},\quad [z^{u+v}]R(z)=(-1)^u\frac{(2u)!(2v)!}{u!v!(u+v)!}.\]
This central coefficient follows, for example, by integrating \((2i\sin\theta)^{2u}(2\cos\theta)^{2v}\) on a circle and applying the elementary beta integral. In the odd case \(R\) is the even-case polynomial multiplied by \((1+z)\). If \(C_k=[z^k](1-z)^{2u}(1+z)^{2v}\), the derivative identity
\[(1-z^2)R_{\rm even}'(z)=(2(v-u)-2(u+v)z)R_{\rm even}(z)\]
and reciprocal symmetry give \(C_{u+v-1}=(v-u)C_{u+v}/(u+v+1)\). Hence the odd-case coefficient is \(C_{u+v}(2v+1)/(u+v+1)\). Both parity cases simplify to the stated factorial eigenvalue, whose sign is exactly \((-1)^a\).

**Inertia and nonsingularity.** The constant eigenvalue is positive and nonzero; every nonconstant factorial quotient is nonzero. Positive weights are those with \(j\equiv0\pmod4\); negative weights are those with \(j\equiv2\pmod4\). Fourfold root-of-unity filtering supplies the cosine closed form for the positive count. There is no kernel.

**Sharp centered extremum.** Write \(B_a=|\Lambda_{2a}|\). Exact cancellation of factorials yields
\[
\frac{B_{a+1}}{B_a}=\frac{2a-1}{2(r-a)-1}\quad(n=2r),\qquad
\frac{B_{a+1}}{B_a}=\frac{2a-1}{2(r-a)+1}\quad(n=2r+1).
\]
These ratios increase strictly with \(a\) wherever defined, so \(B_a\) is log-convex. Among the positive nonconstant modes (even \(a\)), the maximum must occur at the first or last admissible even index. Direct endpoint evaluation gives \(B_1=M_n\), \(B_2=M_n/(n-3)\) for even \(n\), \(B_2=M_n/(n-2)\) for odd \(n\), and \(B_r=M_n\) for even \(n\), or \(B_r=M_n/(n-2)\) for odd \(n\). For even \(n\), the identity \(B_a=B_{r+1-a}\) controls the last even index. For odd \(n\), log-convexity and \(B_r=B_2\) bound the final even index. This proves the four cases for \(Q_n\). At \(n=3\) the only nonconstant eigenvalue is \(-1\).

**Negative type and Gaussian obstruction.** A real finite metric is of conditional negative type if and only if its distance matrix is nonpositive on zero-sum vectors. By the sharp formula \(Q_3=-1\) and \(Q_n>0\) for \(n\ge4\). For a zero-sum eigenvector of positive eigenvalue, the first-order expansion of \(\exp(-tD_n)\) entrywise gives a negative quadratic form for all sufficiently small \(t>0\), proving the stated kernel failure. This does not assert failure for every positive \(t\).

## Verification
The accompanying standalone program `CHECK.py` uses only the Python standard library. It independently computes Fourier coefficients by Krawtchouk binomial convolution for every admissible weight in dimensions \(3\le n\le70\); it checks all analytic eigenvalues, multiplicities, zero trace, inertia and sharp centered extrema. It also recomputes the actual graph-distance Walsh transform directly for all even weights in \(3\le n\le10\), using the unique quotient representatives with final coordinate zero. The run produced `EXACT_FOLDED_CUBE_SPECTRA_OK 1596`. Finite tests corroborate, but do not establish, the infinite theorem.

## Relationship to prior work
The folded-cube distance-regular structure is classical; Ma and Koolen discuss folded cubes among twice \(Q\)-polynomial graphs (2014). Liu, Pan, Wang and Cao (2014) compute Kirchhoff indices using **Laplacian** eigenvalues and resistance distances, which are different from ordinary shortest-path distance matrices. Aalipour and coauthors (2015) study ordinary distance spectra of halved cubes, double odd graphs and Doob graphs, but their inspected full text does not list folded-cube distance spectra. The classical binary Krawtchouk diagonalization is acknowledged; the claim here is its exact all-dimension evaluation, nonsingularity, full inertia, and especially the four-periodic sharp quadratic embedding constant. A related earlier calculation of one top folded-cube Walsh mode for odd dimensions is not a general all-weight spectrum or sharp extremal classification.

## Limitations
The theorem concerns the unweighted shortest-path metric on antipodal quotients of binary cubes only, not effective resistance, the full Hamming cube, halved cubes, arbitrary radial kernels, or the exact maximum positive-definite power exponent. For \(n\ge4\), failure of \(e^{-td}\) is shown only for all sufficiently small positive \(t\), not every \(t\). An equivalent formulation in older association-scheme literature has not been categorically excluded; novelty is a bounded literature assessment, not independent certification.

## References
- Jianmin Ma and Jack Koolen, *Twice Q-polynomial distance-regular graphs of diameter 4*, arXiv:1405.2546 (first posted 2014-05-11), https://arxiv.org/abs/1405.2546 .
- G. Aalipour, A. Abiad, et al., *On the distance spectra of graphs*, arXiv:1509.01196 (first posted 2015-09-03), https://arxiv.org/html/1509.01196v2 .
- Jiabao Liu, Xiang-Feng Pan, Yi Wang, Jinde Cao, *The Kirchhoff Index of Folded Hypercubes and Some Variant Networks*, Mathematical Problems in Engineering (2014), DOI 10.1155/2014/380874, https://onlinelibrary.wiley.com/doi/10.1155/2014/380874 .
