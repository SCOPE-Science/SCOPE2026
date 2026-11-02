# Exact harmonic-sampling spectra and the last interpolation gap of the regular dodecahedron

## Finding
Let \(X\subset S^2\) be the twenty vertices of a regular dodecahedron centered at the origin. For each integer \(k\ge0\), let \(E_k:\mathcal H_k(S^2)\longrightarrow\mathbb R^X\) evaluate real spherical harmonics of **exact** degree \(k\). Then
\[
\operatorname{rank}E_k=\begin{cases}
1,&k=0,\\
3,&k=1,\\
5,&k=2,\\
7,&k=3,\\
9,&k=4,\\
6,&k=5,\\
9,&k\in\{8,14\},\\
10,&\text{all remaining }k\ge6.
\end{cases}
\]
All evaluation data obey antipodal parity. Every compatible array of ten sample values is attainable at exact degree \(k\) precisely for \(k\in\{6,7,9,10,11,12,13\}\) or \(k\ge15\). Thus \(15\) is the **sharp permanent-surjectivity degree**, despite earlier full interpolation at degree \(6\) and the exceptional drop at degrees \(8\) and \(14\). In particular, the degree-five image has dimension \(6\), strictly below the degree-four image dimension \(9\).

The theorem also supplies the complete spectrum of the normalized Legendre sampling Gram matrix at **every** degree. Put \(a_k=P_k(1/3)\), \(b_k=P_k(\sqrt5/3)\), where \(P_k(1)=1\). Besides ten eigenvalues zero due to antipodal parity, the Gram matrix has the following ten eigenvalues (further zero values are allowed):

* At even \(k\): \(2(1+6a_k+3b_k)\) once, \(2(1-2a_k+b_k)\) five times, and \(2(1+a_k-2b_k)\) four times.
* At odd \(k\): \(2(1-3a_k)\) four times and \(2(1+2a_k\pm\sqrt5 b_k)\) three times for each sign.

These are exact spectral formulas; no numerical diagonalization is required. As a consequence, the uniform vertex sum annihilates every spherical harmonic in the even degrees \(2,4,8,14\), and in no other positive even degree; the odd-degree sums vanish by antipodality.

## Assumptions and scope
The vertex set is the rotation and scaling of the twenty vectors
\[
(\pm1,\pm1,\pm1),\quad (0,\pm\varphi^{-1},\pm\varphi),\quad
(\pm\varphi^{-1},\pm\varphi,0),\quad (\pm\varphi,0,\pm\varphi^{-1}),
\qquad\varphi=(1+\sqrt5)/2,
\]
all divided by \(\sqrt3\), with every independent sign choice shown. The first block has eight vectors and the other three blocks have four each. The indexing set contains no repeated points. The statement covers every integer harmonic degree, including degree zero, but not sums of several degrees, weighted sampling, or conditioning of nonzero singular values.

The Gram normalization is \(K_k(x,y)=P_k(x\cdot y)\). By the spherical-harmonic addition formula,
\[
K_k(x,y)=\frac{4\pi}{2k+1}\sum_{m=-k}^kY_{km}(x)\overline{Y_{km}(y)}
\]
for any orthonormal harmonic basis. Consequently \(K_k\) is positive semidefinite and \(\operatorname{rank}K_k=\operatorname{rank}E_k\).

## Proof
**1. Antipodal reduction.** Choose one vertex from each antipodal pair, giving ten representatives \(v_i\). Between distinct representatives the inner products lie in \(\{\pm1/3,\pm\sqrt5/3\}\). For even degrees the ten-by-ten parity-reduced Gram matrix \(G_k\) has entries \(P_k(v_i\cdot v_j)\) and only the absolute value matters. Define the zero-diagonal matrix \(C\) by \(C_{ij}=1\) when \(|v_i\cdot v_j|=\sqrt5/3\), and zero otherwise. Direct substitution of the displayed vertex coordinates gives
\[
C\mathbf1=3\mathbf1,\qquad C^2=2I-C+J,
\]
where \(J\) is the all-ones matrix. Hence \(C\) has eigenvalues \(3,1,-2\) with multiplicities \(1,5,4\), respectively. The reduced even Gram matrix is
\[
G_k=(1-a_k)I+(b_k-a_k)C+a_kJ.
\]
Its three claimed even-degree eigenvalues, before the factor \(2\), follow immediately.

**2. Signed odd-degree reduction.** Define zero-diagonal signed matrices \(A,B\) by
\[
A_{ij}=\begin{cases}\operatorname{sgn}(v_i\cdot v_j),&|v_i\cdot v_j|=1/3,\\0,&\text{otherwise},\end{cases}
\qquad
B_{ij}=\begin{cases}\operatorname{sgn}(v_i\cdot v_j),&|v_i\cdot v_j|=\sqrt5/3,\\0,&\text{otherwise}.\end{cases}
\]
The same explicit ten-point calculation gives \(B^2=A+3I\) and \(B^3=5B\). In particular, \(B\) is symmetric with eigenvalues \(0,\sqrt5,-\sqrt5\). Its zero diagonal gives \(\operatorname{tr}B=0\), and each row of \(B\) has three nonzero entries, giving \(\operatorname{tr}B^2=30\). Therefore their multiplicities are \(4,3,3\). Since \(A=B^2-3I\), the odd reduced Gram matrix \(G_k=I+a_kA+b_kB\) has eigenvalues \(1-3a_k\) (multiplicity four) and \(1+2a_k\pm\sqrt5 b_k\) (multiplicity three each).

**3. Complete Gram spectrum.** Since \(P_k(-t)=(-1)^kP_k(t)\), ordering the full twenty vertices as \(v_1,\ldots,v_{10},-v_1,\ldots,-v_{10}\) gives
\[
K_k=\begin{pmatrix}G_k&(-1)^kG_k\\(-1)^kG_k&G_k\end{pmatrix}.
\]
The ten eigenvalues of \(G_k\) are therefore doubled, and ten additional eigenvalues are zero. The addition formula turns their nonzero count into the evaluation rank.

**4. Exact finite portion.** Set
\[
A_k=3^kP_k(1/3),\qquad
B_k=\frac{3^kP_k(\sqrt5/3)}{(\sqrt5)^{k\bmod2}},\qquad A_0=A_1=B_0=B_1=1.
\]
The Legendre recurrence yields, for every \(k\ge1\),
\[
(k+1)A_{k+1}=(2k+1)A_k-9kA_{k-1},
\]
\[
(k+1)B_{k+1}=(2k+1)c_kB_k-9kB_{k-1},
\quad c_k=\begin{cases}5,&k\text{ odd},\\1,&k\text{ even}.
\end{cases}
\]
Multiplying the ten reduced eigenvalues by the positive factor \(3^k\) produces the exact rational triples
\[
\begin{array}{ll}
(3^k+6A_k+3B_k,\ 3^k-2A_k+B_k,\ 3^k+A_k-2B_k),&k\text{ even};\\
(3^k-3A_k,\ 3^k+2A_k+5B_k,\ 3^k+2A_k-5B_k),&k\text{ odd}.
\end{array}
\]
Their multiplicities are respectively \((1,5,4)\) and \((4,3,3)\). The self-contained exact-rational checker `verify_dodecahedron.py` constructs the coordinates and signed matrices, verifies all three matrix identities, then checks every triple for \(0\le k\le185\). Every entry is nonnegative; the only degrees with zero entries are \(0,1,2,3,4,5,8,14\), with ranks \(1,3,5,7,9,6,9,9\), in this order. No floating-point tolerance or partial numerical rank decision enters this step.

**5. Infinite tail.** For \(|x|<1\), the Laplace integral representation of the Legendre polynomial is
\[
P_k(x)=\frac1\pi\int_0^\pi\bigl(x+i\sqrt{1-x^2}\cos t\bigr)^k\,dt.
\]
It follows, for \(k\ge1\), from \(1-u\le e^{-u}\) and \(\sin t\ge2t/\pi\) for \(0\le t\le\pi/2\) that
\[
|P_k(x)|\le\frac1\pi\int_0^\pi
\exp\!\left(-\frac{k(1-x^2)\sin^2t}{2}\right)dt
\le\sqrt{\frac{\pi}{2k(1-x^2)}}.
\]
Thus \(|a_k|\le3\sqrt\pi/(4\sqrt k)\) and \(|b_k|\le3\sqrt\pi/(2\sqrt{2k})\). In particular,
\[
6|a_k|+3|b_k|\le \frac{9\sqrt\pi}{2\sqrt k}\left(1+\frac1{\sqrt2}\right)<1
\quad\text{for every integer }k\ge186.
\]
The last strict inequality follows from \(\frac{81\pi}{4}(1+1/\sqrt2)^2<186\); the checker verifies a rational upper bound using \(\pi<22/7\) and \(1/\sqrt2<7072/10000\). Each even eigenvalue is at least \(1-6|a_k|-3|b_k|\), and each odd eigenvalue is at least this bound as well because \(\sqrt5<3\). Therefore every reduced eigenvalue is strictly positive at every degree \(k\ge186\). Together with the finite check, this proves the classification for all integers \(k\ge0\). \(\square\)

## Verification
Run `python3 verify_dodecahedron.py` from the directory containing this document. It uses only the Python standard library and reconstructs all twenty vertices as exact elements of \(\mathbb Q(\sqrt5)^3\), checks the signed Petersen-type identities, evaluates all scalar Legendre recurrences exactly through degree \(185\), and verifies the rational tail-bound comparison. The expected leading output is `DODECAHEDRAL_SAMPLING_EXACT_CHECK_OK`. The finite checker alone is not a proof of the infinite tail: that part uses the displayed Laplace-integral estimate.

## Relationship to prior work
Hitchin's 2007 study of cubic spherical harmonics and the icosahedron treats nodal sets of degree-three harmonics on the dual icosahedral geometry, not all-degree evaluation on the twenty dodecahedral vertices. Cohan's 1958 paper expands harmonics in representations of the icosahedral group through degree fourteen; it is relevant to low-degree symmetry but an all-degree dodecahedral sampling-rank theorem was not verifiable from the accessible extract. Ye and collaborators' 2012 diffusion-MRI sampling work explicitly considers the dodecahedron as a candidate directional grid but does not derive these exact-degree ranks. The earlier thirty-two-direction icosahedral-union rank statement implies surjectivity on its dodecahedral subset whenever the larger union is surjective, notably for degrees \(k\ge45\), but does not give the complete dodecahedral rank sequence, the sharp permanent threshold \(15\), or the three-block exact Gram spectra.

## Limitations
This is a self-contained mathematical proof and exact finite certificate, not an independent external audit. The result concerns unweighted exact-degree evaluation, not combined frequency bands or noise-optimal sample design. A full-text comparison with Cohan's historical article was blocked by access limitations; equivalence hidden in older icosahedral representation or interpolation literature remains a residual originality risk. Classical nonvanishing bounds establish only a sufficient large-degree tail; the sharp value \(15\) comes from the combined exact finite computation and analytic bound.

## References
- Nigel Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088v1 (first posted 2007-06-01), especially Sections 1–3. https://arxiv.org/abs/0706.0088
- Wenxing Ye, Sharon Portnoy, Alireza Entezari, Stephen J. Blackband, and Baba C. Vemuri, *An Efficient Interlaced Multi-shell Sampling Scheme for Reconstruction of Diffusion Propagators*, IEEE Transactions on Medical Imaging **31** (2012), 1043–1050. DOI:10.1109/TMI.2012.2184551; public full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3343185/.
- Norah V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Proc. Cambridge Philos. Soc. **54** (1958), 28–38, DOI:10.1017/S0305004100033156 (only extract accessible).
- Yibin Zheng and Peter C. Doerschuk, *Explicit Computation of Orthonormal Symmetrized Harmonics with Application to the Identity Representation of the Icosahedral Group*, SIAM Journal on Mathematical Analysis **32** (2000), 538–554, DOI:10.1137/S0036141098341770 (abstract inspected).
