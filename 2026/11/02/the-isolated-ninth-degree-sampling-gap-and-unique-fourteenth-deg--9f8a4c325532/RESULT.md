# The isolated ninth-degree sampling gap and unique fourteenth-degree conditioning spike of the rhombicuboctahedron

## Finding
For the twenty-four vertices of the regular rhombicuboctahedron, exact-degree real spherical-harmonic evaluation has full antipodal-parity-compatible rank in degrees \(6,7,8\), loses precisely two ranks at degree \(9\), and has full rank at **every** degree \(k\ge10\). The complete evaluation-rank sequence is
\[
\operatorname{rank}E_k=\begin{cases}
2k+1,&0\le k\le5,\\
10,&k=9,\\
12,&k=6,7,8\ \text{or}\ k\ge10.
\end{cases}
\]

Among all exact degrees having full rank twelve, the normalized twelve-by-twelve Legendre sampling Gram matrix has a **unique** maximum spectral condition number at \(k=14\). Put \(Q=9904578032905937\), and define
\[
L=\frac{1376426164832320-973165469028480\sqrt2}{Q},\qquad
U=\frac{10234852354708520+3606819450015600\sqrt2}{Q}.
\]
Then \(\lambda_{\min}(K_{14})=L>0\), \(\lambda_{\max}(K_{14})=U\), and
\[
\max_{\{k:\operatorname{rank}E_k=12\}}\kappa_2(K_k)
=\frac UL=94454.64388018355\ldots,
\]
attained **only** for \(k=14\). Every other full-rank degree has \(\kappa_2(K_k)<3600\); in particular, this extremum is isolated by a strict factor greater than \(25\).

## Assumptions and scope
Let \(r=1+\sqrt2\), and set
\[
X=\left\{\frac{(\varepsilon_1 b_1,\varepsilon_2 b_2,\varepsilon_3 b_3)}{\sqrt{5+2\sqrt2}}:\ (b_1,b_2,b_3)\text{ is a permutation of }(r,1,1),\ \varepsilon_j\in\{-1,1\}\right\}\subset S^2.
\]
Repeated permutations of the two equal entries are counted once; hence \(|X|=24\). Fix \(x_1,\ldots,x_{12}\) as the members of \(X\) with positive first coordinate, ordered first by the position of \(r\), and then by the signs of the second and third coordinates in lexicographic order with negative preceding positive. There are exactly twelve antipodal classes.

For every integer \(k\ge0\), \(\mathcal H_k(S^2)\) is the real harmonic space of exactly degree \(k\) (dimension \(2k+1\)), and \(E_k:\mathcal H_k(S^2)\to\mathbb R^X\) evaluates functions on \(X\). Define \(P_k\) by \(P_k(1)=1\) and
\[
K_k=(P_k(x_i\cdot x_j))_{i,j=1}^{12}.
\]
By the spherical-harmonic addition theorem, \(K_k\) is positive semidefinite, with rank equal to \(\operatorname{rank}E_k\), because the omitted antipodal rows only duplicate the selected ones up to the sign \((-1)^k\). The condition number is the spectral ratio \(\lambda_{\max}/\lambda_{\min}\), defined here only when \(K_k\) is positive definite. The results assert no interpolation of arbitrary independent values on all twenty-four vertices at a *single* degree: the parity restriction is unavoidable.

## Proof
**Step 1: Three signed distance relations.** Every off-diagonal inner product among the chosen representatives is one of \(\pm a,\pm b,\pm c\), where
\[
a=\frac{7+4\sqrt2}{17},\qquad
b=\frac{-3+8\sqrt2}{17},\qquad
c=\frac{5-2\sqrt2}{17}.
\]
The associated unordered pair counts are \(24,18,24\). For parity \(\epsilon\in\{0,1\}\) define three symmetric zero-diagonal integer matrices \(A_\epsilon,B_\epsilon,C_\epsilon\) by putting \(\operatorname{sgn}(x_i\cdot x_j)^\epsilon\) in the entry belonging respectively to absolute inner product \(a,b,c\), and zero elsewhere. Consequently, with \(u=P_k(a)\), \(v=P_k(b)\), \(w=P_k(c)\),
\[
K_k=I+uA_\epsilon+vB_\epsilon+wC_\epsilon,\qquad\epsilon\equiv k\pmod2.
\]
These three integer matrices are explicitly reconstructible from the twelve stated points, with no choices left implicit.

**Step 2: Complete Gram eigenvalues.** Exact rational row operations on the three relation matrices give orthogonal invariant subspaces of dimensions \(1,2,3,6\), both for even and odd parity. On the first three the respective eigenvalues and multiplicities are \((\ell_1,1)\), \((\ell_2,2)\), \((\ell_3,3)\), with
\[
(\ell_1,\ell_2,\ell_3)=
\begin{cases}
(1+4u+3v+4w,\ 1+u-2w,\ 1-u-2v+2w),&\epsilon=0,\\
(1-v-4w,\ 1-3u+2v+2w,\ 1-u-2w),&\epsilon=1.
\end{cases}
\]
On the six-dimensional complement the other eigenvalues are the two real roots \(\rho_\pm\) of \(z^2-Sz+R=0\), **each with multiplicity three**, where
\[
\begin{aligned}
S&=\frac{12-\ell_1-2\ell_2-3\ell_3}{3},\\
T&=\frac{12+48u^2+36v^2+48w^2-\ell_1^2-2\ell_2^2-3\ell_3^2}{3},\\
R&=\frac{S^2-T}{2}.
\end{aligned}
\]
For completeness, the supplied exact checker constructs explicit rational bases of the dimension-\(1,2,3\) subspaces, and on their common orthogonal complement verifies \(K^2-SK+RI=0\) as a **polynomial identity in three independent variables** \(u,v,w\). Ten unisolvent evaluations establish every coefficient of this total-degree-at-most-two identity, so this is not merely a numerical test at sample degrees. The trace and the quadratic identity force each distinct root to have multiplicity three (at a double root the full six-dimensional eigenvalue has multiplicity six). Thus the formulas give the entire spectrum for every integer \(k\).

**Step 3: Exact low-degree classification and bounds.** The recurrence
\[
P_0(t)=1,\quad P_1(t)=t,\quad kP_k(t)=(2k-1)tP_{k-1}(t)-(k-1)P_{k-2}(t)
\]
is evaluated without approximation inside \(\mathbb Q(\sqrt2)\) for every \(0\le k\le199\). Signs of quadratic field elements are decided exactly by rational-square comparisons. The enclosed standalone checker verifies each rank and the following strict inequalities:
\[
\begin{aligned}
&\lambda_{\min}(K_k)>\frac1{50}&& (6\le k\le199,\ k\notin\{9,13,14\}),\\
&\lambda_{\min}(K_{13})>\frac1{300},\\
&\lambda_{\min}(K_{14})=L,\quad\lambda_{\max}(K_{14})=U,\quad U>90000L.
\end{aligned}
\]
At \(k=9\) the degree-nine parity matrix has exactly its multiplicity-two sector \(\ell_2=0\), with all remaining eigenvalues strictly positive. Two independent annihilating coefficient vectors, in the representative ordering above, are
\[
(-1,1,1,-1,1,-1,-1,1,0,0,0,0),\qquad
(-1,1,1,-1,0,0,0,0,1,-1,-1,1).
\]
All statements in this step are finite identities or strict rational-quadratic comparisons, not floating-point extrapolations. The source file contains the complete finite certificate and executes under Python 3.10 or later without dependencies.

**Step 4: Rigorous infinite tail.** The largest absolute off-diagonal inner product is \(a<3/4\), so its corresponding \(\sin\theta\) exceeds \(3/5\), and the same holds at \(b,c\). Bernstein's classical Legendre inequality (recorded in Gautschi–Giordano, §5.3) gives, for every \(k\ge1\) and every such inner product,
\[
|P_k(\cos\theta)|<\sqrt{\frac{2}{\pi k\sin\theta}}
<\sqrt{\frac{10}{9k}},
\]
using \(\pi>3\). Thus by Gershgorin every eigenvalue of \(K_k\) satisfies
\[
1-11\sqrt{\frac{10}{9k}}<\lambda<1+11\sqrt{\frac{10}{9k}}.
\]
For \(k\ge200\), the lower bound is strictly larger than \(1/50\), proving all such Gram matrices positive definite. Every \(K_k\) has trace \(12\); hence \(\lambda_{\max}<12\), so the finite and tail bounds give \(\kappa_2(K_k)<600\) outside \(k=13,14\) among full-rank degrees, and \(\kappa_2(K_{13})<3600\). Since \(\kappa_2(K_{14})>90000\), degree fourteen is the unique global maximizer. This completes all infinite-degree and uniqueness assertions.

## Verification
Execute \(\texttt{python3 rhombicuboctahedron_harmonic_certificate.py}\) from a directory containing the embedded checker. The success sentinel is \(\texttt{RHOMBICUBOCTAHEDRON\_SAMPLING\_CERTIFICATE\_OK 200 exact degrees}\). The checker enumerates the twelve points and their three pair relations; verifies the invariant-sector eigenvectors and a symbolic quadratic identity; reconstructs every Legendre coefficient in \(\mathbb Q(\sqrt2)\) for \(0\le k\le199\); checks ranks and sharp endpoint eigenvalues; and tests the rational lower bounds used in the last step. The proof above independently supplies the necessary infinite tail. The checker does **not** constitute independent validation, and no numerical eigensolver is used for the exact assertions.

## Relationship to prior work
An–Chen–Sloan–Womersley (2010) develop well-conditioned spherical designs for cumulative-degree integration and interpolation with point count related to \((t+1)^2\). Their setting does not determine an all-degree spectrum of one fixed 24-point Archimedean orbit. Bannai–Okuda–Tagami (2013) and Zhu et al. (2015) develop harmonic-index design and moment-annihilation theory, but the material inspected does not supply this configuration's degree-nine two-dimensional annihilator or its sharp all-degree spectral condition-number extremum. The Legendre tail uses the classical Bernstein bound recorded by Gautschi–Giordano (2008).

The exact-degree rank question is not the same as ordinary spherical-design strength or cumulative-degree polynomial interpolation. The theorem is also not implied by analogous rank/conditioning classifications on the **truncated octahedron**, the **icosidodecahedron**, or root-system point configurations: those involve different vertex sets and different Gram spectra. No directly covering result was located in the bounded searches; this does not establish historical priority.

## Limitations
The result concerns the specifically normalized regular rhombicuboctahedron, not arbitrary deformations or all Archimedean solids. It analyzes individual harmonic degrees, not sums of degrees, arbitrary weighted cubature, or noisy interpolation beyond the stated spectral ratios. A relevant 1975 paper of Lebedev on octahedrally invariant cubature was identified by its publication record, but its full text could not be retrieved for direct comparison; equivalent earlier association-scheme or cubature computations remain an originality risk. The exact certificate is a same-author reproducibility aid; independent audit has not been performed.

## References
1. W. Gautschi and C. Giordano, “Luigi Gatteschi's work on asymptotics of special functions and their zeros,” *Numerical Algorithms* 49 (2008), 11–31, DOI 10.1007/s11075-008-9208-5. First published online 2008-05-20. See §5.3 for the classical Legendre Bernstein inequality.
2. C. An, X. Chen, I. H. Sloan, R. S. Womersley, “Well Conditioned Spherical Designs for Integration and Interpolation on the Two-Sphere,” *SIAM Journal on Numerical Analysis* 48 (2010), 2135–2157, DOI 10.1137/100795140, published electronically 2010-12-14.
3. E. Bannai, T. Okuda, M. Tagami, “Spherical designs of harmonic index t,” arXiv:1308.5101, first version 2013-08-23.
4. Y. Zhu and collaborators, “More on Spherical Designs of Harmonic Index t,” arXiv:1507.05373, first version 2015-07-20.
