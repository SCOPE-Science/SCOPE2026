# All-degree spherical-harmonic sampling spectrum of the 72 \(E_6\) roots

## Finding
Let \(X\subset S^5\) be the 72 unit vectors of the irreducible root system of type \(E_6\), and let
\(E_k:\mathcal H_k(S^5)\longrightarrow\mathbb R^X\) evaluate every real spherical harmonic of **exact** degree \(k\), for an arbitrary integer \(k\ge0\). Then
\[
\operatorname{rank}E_k=
\begin{cases}
1&k=0,\\
6&k=1,\\
20&k=2,\\
30&k=3,\\
35&k=4,\\
36&k\ge5.
\end{cases}
\]
This is an all-degree classification, not an extrapolation from finite-degree computations. Since \(X=-X\) consists of 36 antipodal pairs, 36 is the largest possible rank for any individual exact degree. The degree-five threshold is sharp. In fact, evaluation of the *direct sum* \(\mathcal H_k(S^5)\oplus\mathcal H_{k+1}(S^5)\) is surjective onto all 72 vertex values if and only if \(k\ge5\); the preceding pair of degrees four and five has rank 71.

The following formulas determine **every** eigenvalue and multiplicity of the 36-by-36 unit-diagonal Gegenbauer evaluation Gram matrix. Set
\[
B_k=\binom{k+3}{3},\quad p_k=\frac{C_k^{(2)}(1/2)}{B_k},\quad q_k=\frac{C_k^{(2)}(0)}{B_k},
\]
where \(C_k^{(2)}\) is the degree-\(k\) Gegenbauer polynomial (so \(C_k^{(2)}(1)=B_k\)). For even \(k\), the spectrum is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1+20p_k+15q_k&1\\
1+2p_k-3q_k&20\\
1-4p_k+3q_k&15
\end{array}.
\]
For odd \(k\), the spectrum is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1+10p_k&6\\
1-2p_k&30
\end{array}.
\]
All displayed eigenvalues are nonnegative, and all are strictly positive for \(k\ge5\). **The exact worst Gram condition number over every full-rank degree is**
\[\boxed{\sup_{k\ge5}\kappa_2(K_k)=25/3,}\]
**attained only at degree \(k=10\)**. Equivalently, after orthonormalizing the spherical harmonic domain and restricting the sample codomain to the appropriate antipodal parity subspace, the worst ratio of largest to smallest **nonzero** singular value of the evaluation map is \(5/\sqrt3\). This is a sharp uniform sampling-stability statement over infinitely many degrees. The unit-diagonal full 72-by-72 Gram matrix has 36 antipodal-parity zero eigenvalues and its remaining eigenvalues are twice the numbers above, with the same listed multiplicities.

## Assumptions and scope
Use the six-dimensional Euclidean subspace \(W\subset\mathbb R^9\) consisting of vectors whose coordinates sum to zero separately in each of three consecutive coordinate blocks of length three. Write \(e_1,e_2,e_3\) for coordinate vectors within a block, and put \(w_1=(2,-1,-1)\), \(w_2=(-1,2,-1)\), \(w_3=(-1,-1,2)\). Form 36 vectors with integer coordinates:

1. For each of the three blocks and each \(1\le i<j\le3\), the vector supported in that block and equal there to \(3(e_i-e_j)\), giving nine vectors.
2. All \((w_a,w_b,w_c)\) with \(a,b,c\in\{1,2,3\}\), giving 27 vectors.

Each has squared length 18. Divide by \(\sqrt{18}\) to obtain \(T=\{x_1,\ldots,x_{36}\}\subset S^5\), and set \(X=T\cup(-T)\). The 72 vectors are exactly a normalized type-\(E_6\) root system. One can check this directly from the Cartan matrix of the following six unnormalized roots (semicolon separates coordinate triples):
\[
\begin{gathered}
(0,0,0;0,0,0;0,3,-3),\ (0,0,0;0,0,0;3,-3,0),\\
(0,0,0;0,3,-3;0,0,0),\ (0,0,0;3,-3,0;0,0,0),\\
(0,3,-3;0,0,0;0,0,0),\ (1,-2,1;-2,1,1;-2,1,1).
\end{gathered}
\]
After dividing these integer vectors by three, their squared norms are two; their pairwise scalar products are \(-1\) precisely along the \(E_6\) Dynkin diagram with a central trivalent node and arm lengths \(2,2,1\), and zero otherwise. The explicit construction also avoids any dependence on choices of root-system coordinates.

The claimed ranks refer to **real** harmonic spaces, though the ranks are identical after complexification. The scalar product is Euclidean, the sphere has radius one, and the Gegenbauer normalization is explicitly \(C_k^{(2)}(1)=\binom{k+3}{3}\). Sampling uses no weights other than one per vertex. A change of orientation of any selected antipodal representative does not change the spectrum.

## Proof
**1. Exact root-pair identities.** For \(i\ne j\), direct block-coordinate calculation shows that \(\langle x_i,x_j\rangle\) belongs to \(\{0,\pm1/2\}\). Define the symmetric 36-by-36 matrices \(A\) and \(S\) by
\[
A_{ij}=\mathbf1_{\{i\ne j,\ |\langle x_i,x_j\rangle|=1/2\}},\qquad
S_{ij}=\begin{cases}2\langle x_i,x_j\rangle&i\ne j,\\0&i=j.\end{cases}
\]
Let \(I\) be the identity and \(J\) the all-ones matrix. Exact enumeration of the nine block differences and 27 three-block weights gives the finite combinatorial identities
\[
A\mathbf1=20\mathbf1,\qquad A^2=8I-2A+12J,\qquad S^2=20I+8S.
\]
They can be checked *exhaustively* from the 36 explicit vectors by integer dot products; `check_e6.py` is the standalone constructive verification, with no external dependencies and no floating-point arithmetic. Independently, the signed identity also follows because \(\sum_{x\in T}xx^{\mathsf T}=6I_W\), so the Gram matrix \(I+S/2\) has eigenvalues six (six times) and zero (thirty times). The unsigned identity identifies the nonorthogonality graph as strongly regular with parameters \((36,20,10,12)\).

The quadratic identities and traces show that \(A\) has eigenvalues \(20,2,-4\), with respective multiplicities \(1,20,15\), whereas \(S\) has eigenvalues \(10,-2\), with multiplicities \(6,30\). For \(A\), the constant eigenspace has dimension one, since its two other possible eigenvalues differ from 20; their multiplicities follow from \(\operatorname{tr}A=0\). The multiplicities for \(S\) follow from \(\operatorname{tr}S=0\).

**2. Addition theorem and parity.** The spherical harmonic addition theorem says that the unit-diagonal degree-\(k\) Gram kernel at unit points is \(P_k(\langle x,y\rangle)\), with \(P_k(t)=C_k^{(2)}(t)/B_k\). Its rank is the rank of the evaluation operator. Since \(P_k(-t)=(-1)^kP_k(t)\), selecting one point from each antipodal pair leaves the rank unchanged. If \(k\) is even, its 36-by-36 Gram matrix is
\[
K_k=(1-q_k)I+(p_k-q_k)A+q_kJ.
\]
If \(k\) is odd, it is \(K_k=I+p_kS\). Substitution of the spectra from Step 1 yields exactly the claimed eigenvalue formulas with multiplicities.

**3. Values in the exceptional degrees.** Direct Gegenbauer recurrence gives
\[
\begin{array}{c|c|c}
k&p_k&q_k\\\hline
0&1&1\\1&1/2&0\\2&1/10&-1/5\\3&-1/10&0\\
4&-4/35&3/35\\5&-1/28&0\\6&1/28&-1/21\\8&1/55&1/33
\end{array}.
\]
At \(k=0\), only the even constant-sector eigenvalue survives. At \(k=1\), only the six-dimensional signed sector survives. At \(k=2\), only the 20-dimensional even sector survives. At \(k=3\), exactly the 30-dimensional signed sector survives. At \(k=4\), the even 20- and 15-dimensional sectors survive. Thus the first five ranks are \(1,6,20,30,35\). The displayed degree-five, six and eight values give strictly positive eigenvalues; degree seven is covered by the odd-degree inequality below.

**4. Infinite-degree positivity.** The differentiation identity \(C_k^{(2)}(t)=\frac12\frac{d}{dt}U_{k+1}(t)\) for Chebyshev polynomials of the second kind gives the exact residue-class formula
\[
C_k^{(2)}(1/2)=
\begin{cases}
(k+3)/3&k\equiv0\pmod6,\\
2(k+2)/3&k\equiv1\pmod6,\\
(k+1)/3&k\equiv2\pmod6,\\
-(k+3)/3&k\equiv3\pmod6,\\
-2(k+2)/3&k\equiv4\pmod6,\\
-(k+1)/3&k\equiv5\pmod6.
\end{cases}
\]
Also \(C_k^{(2)}(0)=0\) for odd \(k\), while \(C_k^{(2)}(0)=(-1)^{k/2}(k+2)/2\) for even \(k\). In particular,
\[
|C_k^{(2)}(1/2)|\le(2k+5)/3,\qquad
|C_k^{(2)}(0)|\le(k+2)/2.
\]
For odd \(k\ge5\), the strict integer inequality
\[
(k+1)(k+2)(k+3)>40k+100
\]
ensures \(10|p_k|<1\), so both signed-sector eigenvalues are positive. It holds at \(k=5\) and its left-minus-right difference is increasing thereafter.

For even \(k\ge10\), the inequality
\[
(k+1)(k+2)(k+3)>125k+290
\]
ensures \(20|p_k|+15|q_k|<1\), hence strict positivity of all three even-sector eigenvalues (the other two require smaller coefficient sums). It holds at \(k=10\) and its left-minus-right difference is increasing thereafter. The two remaining even degrees \(k=6,8\) were evaluated in Step 3. Hence every eigenvalue is positive at every degree \(k\ge5\), proving the rank classification in the infinite range.

**5. Sharp condition number across all degrees.** For degree ten, direct recurrence gives
\[
(p_{10},q_{10})=(-4/143,-3/143),\qquad
\operatorname{spec}K_{10}=\{(18/143)^1,(144/143)^{20},(150/143)^{15}\}.
\]
Its condition number is therefore exactly \(150/18=25/3\). Degrees five, six, seven, eight and nine have smaller condition numbers by their explicit rational eigenvalues; their values are respectively \(5/3,17/10,5/3,25/13,19/15\) (degree nine has \(p_9=-1/55\)). At every odd degree \(k\ge11\), and indeed already for \(k\ge7\), we have
\[
10|p_k|\le\frac{40k+100}{(k+1)(k+2)(k+3)}\le\frac{19}{36},
\]
so all signed-sector eigenvalues lie between \(1-19/36\) and \(1+19/36\), giving condition number at most \(55/17<25/3\). At even degrees \(k\ge12\), similarly,
\[
20|p_k|+15|q_k|\le\frac{125k+290}{(k+1)(k+2)(k+3)}\le\frac{179}{273},
\]
so every eigenvalue lies between \(1-179/273\) and \(1+179/273\); their condition number is at most \(226/47<25/3\). Both bounding rational functions are decreasing in the indicated integer ranges. Every degree except ten has a strict smaller condition number, proving the unique sharp worst-case degree. This demonstrates that full rank alone does not predict the strongest interpolation instability.

**6. Consecutive degrees.** Even- and odd-degree harmonic evaluations lie in complementary antipodal parity subspaces of \(\mathbb R^{72}\), each of dimension 36. Their ranks therefore add. The first two adjacent full-parity ranks occur at degrees five and six, giving 72; all later adjacent pairs are also full. For degrees below five, at least one constituent has rank less than 36, proving the sharpness.

## Verification
Run `python3 check_e6.py` in the directory containing this result. The checker constructs all 36 representatives using exact integers, verifies all root dot products and the full 36-by-36 matrix identities, computes normalized Gegenbauer coefficients by the independent three-term recurrence, compares them to the closed residue-class formula, and checks the claimed rank, positivity and condition numbers at forty initial degrees with exact rational arithmetic. It also checks sample instances of the elementary high-degree inequalities. Exhaustive finite root-pair identities and the infinite-degree inequalities are separate proof components; the forty-degree numerical range is a consistency check, not an assertion that computation exhausts the infinite range. A separate numerical linear-algebra cross-check gave adjacency eigenvalues \(20^1,2^{20},(-4)^{15}\) and signed eigenvalues \(10^6,(-2)^{30}\).

## Relationship to prior work
Bannai, Okuda and Tagami (2013) introduced the harmonic-index-design viewpoint and its Fisher-type bounds. Zhu, Bannai, Bannai, Kim and Yu (2015) developed tight harmonic-index design theory. Borodachov (2022), §9, explicitly describes the normalized 72-root \(E_6\) configuration and establishes its spherical five-design and potential-minimization properties. Those facts explain the constant-sector cancellations at degrees two and four. The classification here concerns a different operator: restriction of **every harmonic of one exact degree** to all 72 roots, including its nonconstant spectral sectors for every degree and its permanent interpolation threshold. Known results for the larger \(E_7\) and \(E_8\) root configurations do not imply this intrinsic six-dimensional restriction statement. A finite-dimensional association-scheme reinterpretation could produce an equivalent earlier result, so originality is assessed only against the literature actually inspected.

## Limitations
The theorem concerns the canonical 72-root configuration only; it does not assert the same ranks for deformations or for arbitrary spherical five-designs. It gives no general error bound for noisy sampling beyond the exact positive eigenvalues above. Its all-degree correctness and uniform sampling-stability bound follow from the stated proof and finite root identities; independent external mathematical validation has not been performed. Historical novelty cannot be certified solely from database search, and unlocated equivalent formulations remain a risk.

## References
1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index \(t\)*, arXiv:1308.5101, first public 2013-08-23; journal version, *Journal of Approximation Theory* 195 (2015), 1–18.
2. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index \(t\)*, arXiv:1507.05373, first public 2015-07-20.
3. S. Borodachov, *Absolute Minima of Potentials of a Certain Class of Spherical Designs*, arXiv:2212.04594, first public 2022-12-08, §9 (the normalized \(E_6\) root configuration and its five-design properties).
