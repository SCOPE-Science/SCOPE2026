# Exact randomized-time uniform quantum mixing on the ten-cycle

## Finding
Let \(C_{10}\) be the unweighted simple cycle on \(\mathbb Z/10\mathbb Z\), and let \(A\) be its adjacency matrix. Write
\[
M(t)_{uv}=\left|\bigl(e^{\mathrm{i}tA}\bigr)_{uv}\right|^2.
\]
**Theorem.** For every real \(T\geq0\), there are an integer \(1\leq k\leq6\), distinct real observation times \(t_1,\ldots,t_k>T\), and strictly positive probabilities \(w_1,\ldots,w_k\) summing to one such that
\[
\sum_{j=1}^{k}w_jM(t_j)=\frac1{10}J_{10}.
\]
Thus a single common random observation time produces exactly uniform expected transition probabilities from every initial vertex. This does not assert instantaneous uniform mixing, prescribe closed-form physical times, or prove that six is the smallest possible support.

## Assumptions and scope
The Hamiltonian is the ordinary real, unweighted adjacency matrix with no onsite potential, magnetic phases or decoherence. Sampling times are positive and are shared among all starting vertices. The statement concerns the full mixing matrix, not one initial-state row. The probability law may depend on the cutoff \(T\). The proof works with \(e^{\mathrm{i}tA}\); changing the sign of the Hamiltonian gives the same mixing matrix.

Set \(\varphi=(1+\sqrt5)/2\). The adjacency eigenvalues in Fourier-index order \(j=0,1,\ldots,9\) have the exact form \(\lambda_j=a_j+b_j\varphi\), where
\[
((a_j,b_j))_{j=0}^{9}=((2,0),(0,1),(-1,1),(1,-1),(0,-1),(-2,0),(0,-1),(1,-1),(-1,1),(0,1)).
\]
The identity follows from \(\lambda_j=2\cos(2\pi j/10)\), \(2\cos(\pi/5)=\varphi\) and \(2\cos(2\pi/5)=\varphi-1\).

## Proof
**1. Phase-torus Fourier reduction.** For \(x,y\) modulo \(2\pi\), define \(\theta_j=a_jx+b_jy\), and, for every \(d\in\mathbb Z/10\mathbb Z\), set
\[
p_d(x,y)=\left|\frac1{10}\sum_{j=0}^{9}\exp\bigl(\mathrm{i}(\theta_j+2\pi jd/10)\bigr)\right|^2.
\]
These ten nonnegative numbers sum to one. By Fourier diagonalization of the cycle, the transition probability for any two vertices at cyclic displacement \(d\) equals \(p_d(t,\varphi t)\). Define the discrete Fourier transform
\[
F_k(x,y)=\sum_{d=0}^{9}p_d(x,y)e^{-2\pi\mathrm{i}kd/10}
=\frac1{10}\sum_{j=0}^{9}e^{\mathrm{i}(\theta_j-\theta_{j-k})},
\]
where each index is modulo ten. The last equality is orthogonality of tenth roots of unity.

**2. A single-harmonic, nonnegative phase law.** Put a probability measure on the two-dimensional torus with density
\[
f(x,y)=\frac{1-\cos(x-2y)}{4\pi^2}
\]
relative to \(dx\,dy\) on \([0,2\pi)^2\). It is nonnegative and has full topological support: its zero set is a finite union of curves and has no interior. For integer pairs \((a,b)\), its Fourier character moment is
\[
\int e^{\mathrm{i}(ax+by)}f(x,y)\,dx\,dy=
\begin{cases}
1,&(a,b)=(0,0),\\
-1/2,&(a,b)=(1,-2)\text{ or }(-1,2),\\
0,&\text{otherwise}.
\end{cases}
\]
Count the ten differences \((a_j-a_{j-k},b_j-b_{j-k})\), for each \(k=1,\ldots,9\). If \(k\) is odd, none of them is \((0,0)\), \((1,-2)\) or \((-1,2)\). If \(k\) is even, precisely two are \((0,0)\), two are \((1,-2)\), and two are \((-1,2)\). Consequently,
\[
\mathbb E[F_k]=0\quad(1\leq k\leq9),\qquad \mathbb E[F_0]=1.
\]
By inverse discrete Fourier transform, \(\mathbb E[p_d]=1/10\) for all ten displacements. In particular the phase-averaged mixing matrix is \(J_{10}/10\).

**3. Exact physical-time realizability, not merely approximation.** Since \(\varphi\) is irrational, Kronecker density for a two-frequency continuous flow implies that for any cutoff \(T\),
\[
\{(t\bmod2\pi,\varphi t\bmod2\pi):t>T\}
\]
is dense in the phase torus. Let \(P(x,y)=(p_0(x,y),\ldots,p_9(x,y))\), and let \(K=\operatorname{conv}(P(\mathbb T^2))\). The barycenter \(u=(1/10,\ldots,1/10)\) belongs to the relative interior of \(K\): otherwise a proper supporting affine functional at \(u\) would be nonnegative on the image, vanish in expectation, and hence vanish throughout the image by continuity and full support, contradicting propriety. The convex hull of a dense subset of a compact set contains the relative interior of the compact convex hull. Therefore \(u\) belongs to the actual convex hull of \(\{P(t,\varphi t):t>T\}\), not only its closure.

**4. Six-point support bound.** By reflection symmetry \(p_d=p_{10-d}\), the mixing vectors are determined by \(p_0,\ldots,p_5\), which satisfy the affine normalization
\[
p_0+p_5+2\sum_{d=1}^{4}p_d=1.
\]
Their affine dimension is at most five. Carathéodory's theorem therefore gives a combination of at most six actual times. Discard zero-weight terms and combine repeated times; the remaining weights are strictly positive and their times can be taken distinct, all beyond \(T\). Translation symmetry propagates the uniform displacement law to all one hundred matrix entries. This proves the theorem.

## Verification
The accompanying standard-library script `verify.py` checks all ten exact spectral labels, all nine nontrivial Fourier difference counts, a weighted \(32\times32\) phase-grid integration independently using complex amplitudes, and the ordinary Cesàro averages. Execute `python3 verify.py`; the first output line is

`VERIFY_OK algebraic_spectrum=10 nontrivial_Fourier_modes=9 torus_points=1024 offsets=10 cesaro_profiles=10`

The infinite statement uses the exact Fourier count, the full-support relative-interior argument, irrational phase density, and Carathéodory's theorem. The numerical grid check is supplementary and is not used to infer exactness.

## Relationship to prior work
Baptista, Coutinho, and Marques [1] introduce averaging mixing matrices over arbitrary observation-time laws and construct exact examples on short paths. Their accessible full 2023 preprint treats characteristic functions, Cartesian products and open questions but does not present a randomized-time ten-cycle construction. Godsil, Mullin, and Roy [2] prove that the only even cycle with **instantaneous** uniform mixing is the four-cycle; this is a different assertion from a convex combination of mixing matrices. Adamczak and coauthors [3] rule out uniformity of the **ordinary infinite-time Cesàro average** on circulants; their assertion also uses a different sampling law. Indeed the conventional average for \(C_{10}\) has entries \(9/50\) at displacements zero and five, and \(2/25\) at each other displacement, whereas the specially weighted law constructed here has all entries \(1/10\). The 2024 survey by Coutinho and Guo [4] describes randomized average mixing as a developing spectral-graph-theoretic direction. No blanket claim of novelty beyond the inspected sources is made.

## Limitations
The theorem does not give closed-form actual observation times or prove an optimal support size. It covers the ten-cycle only and makes no assertion about other composite cycle orders. A full-scope independent literature audit has not been conducted; an equivalent result under another description of cyclic quantum interference remains possible. The proof is an analytical existence proof; the finite computations in `verify.py` are supporting checks. No independent validation is represented.

## References
[1] Pedro Baptista, Gabriel Coutinho and Vitor Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1, first submitted 2023-08-31, https://arxiv.org/pdf/2308.16378.

[2] Chris Godsil, Natalie Mullin and Aidan Roy, *Uniform Mixing and Association Schemes*, arXiv:1301.5889; *Electronic Journal of Combinatorics* 24 (2017), P3.22, https://arxiv.org/pdf/1301.5889.

[3] William Adamczak, Kevin Andrew, Leon Bergen, Dillon Ethier, Peter Hernberg, Jennifer Lin and Christino Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096, https://arxiv.org/pdf/0708.2096.

[4] Gabriel Coutinho and Krystal Guo, *Selected open problems in continuous-time quantum walks*, *Special Matrices* 12 (2024), article 20240025, https://doi.org/10.1515/spma-2024-0025.
