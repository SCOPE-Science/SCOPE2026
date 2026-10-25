# Checkerboard cosine diffusion couplings and the sharp Neumann-grid positivity boundary

## Finding

Let \(N\ge1\), \(L>0\), and let \(C\) be the orthogonal, cell-centered discrete cosine transform with
\[
 C_{i0}=N^{-1/2},\qquad
 C_{ip}=\sqrt{2/N}\cos\!\left(\frac{p\pi(i-1/2)}{N}\right),
 \quad 1\le i\le N,\quad 1\le p\le N-1.
\]
Set
\[
 Q=C\operatorname{diag}\left(-\frac{\pi^2p^2}{L^2}:0\le p\le N-1\right)C^{\mathsf T},
 \qquad H(t)=e^{tQ}\quad(t\ge0).
\]
These are exactly the nodal diffusion generator and heat step of the cosine spectral method with homogeneous Neumann conditions described by Kim, Kwak, Lee, Hwang, and Ham [1, equations (2.1)–(2.6)].

**Full off-diagonal sign law.** For every pair \(1\le i<j\le N\), put \(d=j-i\) and \(s=i+j-1\). Then
\[
 \boxed{\displaystyle
 Q_{ij}=\frac{\pi^2}{2L^2}(-1)^{d+1}
 \left[\cot^2\!\left(\frac{d\pi}{2N}\right)
       -\cot^2\!\left(\frac{s\pi}{2N}\right)\right].}
\]
The difference in brackets is **strictly positive**. Hence
\[
 \boxed{\operatorname{sgn}(Q_{ij})=(-1)^{j-i+1}\qquad(i\ne j).}
\]
The number of strictly negative unordered off-diagonal pairs is exactly
\[
 \boxed{\left\lfloor\frac{(N-1)^2}{4}\right\rfloor.}
\]
Consequently the cosine spectral heat step preserves the entire nonnegative nodal cone, or equivalently every nodal maximum/minimum interval, **at every time \(t\ge0\) if and only if \(N\le2\)**. For each \(N\ge3\), every even-distance off-diagonal entry \(H_{ij}(t)\) is strictly negative for all sufficiently small positive times. The first such failure already occurs between nodes \(1\) and \(3\).

**Eventual positivity and the smallest-grid exact transition.** Nevertheless, for every \(N\) the heat step is strictly entrywise positive at every time satisfying
\[
 \frac{\pi^2t}{L^2}>\log(N-1)\qquad(N\ge2).
\]
For the first nontrivial case \(N=3\), define \(r\) as the unique root in \((0,1)\) of
\[
 r^3+r^2+r-2=0,
 \qquad r=0.810535713766\ldots,
\]
and put \(t_*=-(L/\pi)^2\log r\). The **complete** set of times when \(H(t)\) is entrywise nonnegative is
\[
 \boxed{\{0\}\cup[t_*,\infty),\qquad
 \frac{\pi^2t_*}{L^2}=0.2100598749078\ldots.}
\]
The exact three-node time evaluation is a specialized illustration; the primary structural finding is the complete alternating sign law and grid-size classification for all \(N\).

## Assumptions and scope

The discrete nodes are \(x_i=(i-\tfrac12)L/N\). The source method evolves the cosine modes exactly, with eigenvalues \(-(p\pi/L)^2\). The full, unfiltered mode range \(p=0,\dots,N-1\), **not** a finite-difference approximation to the Laplacian or a truncated periodic Fourier grid, is required. Time is continuous and nonnegative. Nodal positivity refers to the map from arbitrary nonnegative **nodal data** to the new nodal vector. There is no assumption of smooth, consistently interpolated initial data.

Because \(C\) is orthogonal, \(Q\) is symmetric, \(Q\mathbf1=0\), and \(H(t)\mathbf1=\mathbf1\). Thus \(H(t)\) has unit row sums. For a unit-row-sum real matrix, preservation of \([a,b]^N\) for every real \(a\le b\) is equivalent to entrywise nonnegativity. Indeed, negative entries are witnessed by a nonnegative coordinate vector; conversely, each row is a convex combination when all entries are nonnegative.

## Proof

**1. A second-moment identity for the Dirichlet kernel.** Define
\[
 F_N(\theta)=\frac12+\sum_{p=1}^{N-1}\cos(p\theta)
 =\frac{\sin((N-\tfrac12)\theta)}{2\sin(\theta/2)}.
\]
For any integer \(m\in\{1,\ldots,2N-1\}\), differentiate twice and evaluate at \(\theta_m=m\pi/N\). The substitutions
\[
 \sin((N-\tfrac12)\theta_m)=(-1)^{m+1}\sin(\theta_m/2),\qquad
 \cos((N-\tfrac12)\theta_m)=(-1)^m\cos(\theta_m/2)
\]
give exactly
\[
 F_N''(\theta_m)=\frac{(-1)^mN}{2}
 \left[(N-1)-\cot^2\!\left(\frac{m\pi}{2N}\right)\right].
\]
Since \(F_N''(\theta)=-\sum_{p=1}^{N-1}p^2\cos(p\theta)\), this is a closed identity for all cosine second moments on the required integer frequencies. All denominators are nonzero because \(1\le m\le2N-1\).

**2. Exact generator and signs.** For \(i<j\), the product-to-sum formula gives
\[
 Q_{ij}=-\frac{\pi^2}{NL^2}\sum_{p=1}^{N-1}p^2
 \left[\cos\!\left(\frac{pd\pi}{N}\right)
       +\cos\!\left(\frac{ps\pi}{N}\right)\right],
 \quad d=j-i,\ s=i+j-1.
\]
The integers \(d\) and \(s\) have **opposite parities**. Substitute the identity from step 1; its two constant \(N-1\) contributions cancel, leaving the boxed formula.

To establish the strict sign of the cotangent-square difference, write
\[
 a=\frac{d\pi}{2N},\qquad b=\frac{s\pi}{2N}.
\]
Both \(a,b\) lie in \((0,\pi)\), with \(a<b\), and
\[
 \cot^2a-\cot^2b
 =\frac{\sin^2b-\sin^2a}{\sin^2a\sin^2b}
 =\frac{\sin(a+b)\sin(b-a)}{\sin^2a\sin^2b}.
\]
But \(a+b=(j-\tfrac12)\pi/N\) and \(b-a=(i-\tfrac12)\pi/N\), both strictly between \(0\) and \(\pi\). Thus the difference is strictly positive, proving the alternating signs. The negative pairs are exactly pairs of indices having the same parity; their count is
\[
 \binom{\lceil N/2\rceil}{2}+\binom{\lfloor N/2\rfloor}{2}
 =\left\lfloor\frac{(N-1)^2}{4}\right\rfloor.
\]
The transpose symmetry of \(Q\) completes all off-diagonal entries.

**3. Unconditional positivity boundary.** If \(N=1\), \(H(t)=I\). If \(N=2\), direct cosine diagonalization gives
\[
 H(t)=\frac12
 \begin{pmatrix}1+e^{-\pi^2t/L^2}&1-e^{-\pi^2t/L^2}\\
 1-e^{-\pi^2t/L^2}&1+e^{-\pi^2t/L^2}\end{pmatrix}\ge0.
\]
If \(N\ge3\), the sign law shows \(Q_{13}<0\). Analyticity yields
\[
 H_{13}(t)=tQ_{13}+O(t^2)<0
\]
for all sufficiently small \(t>0\). More generally the same argument applies to every off-diagonal pair with even index separation. The initial coordinate vector at node \(3\) produces a negative value at node \(1\), so the nodal positivity and corresponding nodal maximum principle fail. This proves the necessary-and-sufficient \(N\le2\) classification.

**4. Eventual positivity at every grid size.** The zero-mode projector is \(\mathbf1\mathbf1^{\mathsf T}/N\), and all other mode exponents are at most \(e^{-\pi^2t/L^2}\). By Cauchy–Schwarz, for every \(i,j\),
\[
 \left|H_{ij}(t)-\frac1N\right|
 \le e^{-\pi^2t/L^2}\sum_{p=1}^{N-1}|C_{ip}C_{jp}|
 \le \frac{N-1}{N}e^{-\pi^2t/L^2}.
\]
This proves entrywise strict positivity whenever the quoted logarithmic inequality holds. This is a **sufficient** time estimate, not a claimed sharp threshold for \(N>3\).

**5. Exact three-node threshold.** Put \(s=\pi^2t/L^2\) and \(y=e^{-s}\). For \(N=3\), the spectral projectors are
\[
 P_0=\tfrac13\mathbf1\mathbf1^{\mathsf T},\quad
 P_1=\tfrac12\begin{pmatrix}1&0&-1\\0&0&0\\-1&0&1\end{pmatrix},\quad
 P_2=\tfrac16\begin{pmatrix}1&-2&1\\-2&4&-2\\1&-2&1\end{pmatrix}.
\]
Therefore \(H(t)=P_0+yP_1+y^4P_2\). Its diagonal entries are strictly positive; \(H_{12}=H_{23}=(1-y^4)/3>0\) for \(t>0\); and
\[
 6H_{13}=2-3y+y^4
 =(y-1)(y^3+y^2+y-2).
\]
The cubic \(g(y)=y^3+y^2+y-2\) is strictly increasing on \([0,1]\), with \(g(0)<0<g(1)\), so it has a unique root \(r\in(0,1)\). For \(0<t<t_*\) one has \(r<y<1\) and \(H_{13}<0\); at \(t=t_*\) it vanishes; for \(t>t_*\), it is strictly positive. At \(t=0\), \(H(0)=I\). This is the claimed complete time classification.

## Verification

`CHECK.py` is a standalone Python 3 program using only the standard library. It independently assembles the DCT-II generator from its mode sum, compares every off-diagonal entry to the proposed formula for \(2\le N\le36\), checks its parity and pair count, verifies exact rational spectral projectors and generator in dimension three, brackets the cubic root with exact fractions, and samples strict late-time positivity. It passed 19,645 finite deterministic checks. The proof above, not the finite tests, establishes all-dimension and continuous-time statements.

## Relationship to prior work

Kim, Kwak, Lee, Hwang, and Ham [1] supply precisely the DCT-II Neumann heat step used here and computationally exhibit discrete maximum-principle violations for certain initial conditions and grids. Their fully inspected equations and numerical section do not provide the off-diagonal signed generator formula, its complete parity census, or the smallest permissible grid threshold. The present result converts those numerical violations into an all-dimensions, data-independent structural classification.

Li [2] analyzes effective maximum principles for periodic Fourier projection/collocation, with nonlinear and time-discrete applications; its inspected setup and principal statements do not present the cell-centered Neumann cosine heat generator. The classical DCT treatment of Strang [3] supplies the orthogonal cosine basis and its relation to a finite-difference operator, which has different eigenvalues from the exact \(-p^2\) spectral generator here. Strang and MacNamara [4] consider matrix functions of second-difference operators, also a different underlying generator. Classical trigonometric differentiation weights make the present calculation approachable, and related unpublished or less searchable cosine formulas may contain equivalent identities; publication priority is not certified. General self-adjoint-semigroup eventual positivity results can already explain the qualitative three-spectral-level recovery pattern, so the three-node time computation is **not** asserted to be an independent general semigroup theorem.

## Limitations

The claim treats exact cosine spectral heat evolution on a one-dimensional, cell-centered Neumann grid, without filtering, time discretization error, variable diffusion coefficients, or nonlinear reaction terms. It concerns arbitrary nodal vectors; a maximum principle relative to the supremum of the **continuous cosine interpolant** is a different statement. The displayed global strict-positivity time bound is not sharp for general \(N\). The exact sharp three-node recovery calculation is a specialized case of broader three-spectral-level positivity phenomena.

## References

[1] J. Kim, S. Kwak, H. G. Lee, Y. Hwang, and S. Ham, *A maximum principle of the Fourier spectral method for diffusion equations*, Electronic Research Archive 31 (2023), 5396–5405. DOI: 10.3934/era.2023273. Public full text: https://aimspress.com/aimspress-data/era/2023/9/PDF/era-31-09-273.pdf .

[2] D. Li, *Effective Maximum Principles for Spectral Methods*, Annals of Applied Mathematics 37 (2021), 131–290. DOI: 10.4208/aam.OA-2021-0003. Public manuscript: https://arxiv.org/pdf/2107.09438 .

[3] G. Strang, *The Discrete Cosine Transform*, SIAM Review 41 (1999), 135–147. DOI: 10.1137/S0036144598336745.

[4] G. Strang and S. MacNamara, *Functions of Difference Matrices Are Toeplitz Plus Hankel*, SIAM Review 56 (2014), 525–546. DOI: 10.1137/120897572.
