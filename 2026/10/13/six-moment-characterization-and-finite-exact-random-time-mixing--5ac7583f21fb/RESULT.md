# Six-moment characterization and finite exact random-time mixing on the five-vertex path

## Finding
Let \(A\) be the adjacency matrix of the ordinary unweighted path \(P_5\), and let \(U(t)=\exp(itA)\). For any Borel probability distribution of a real observation time \(T\), define \(\mathcal M_T=(\mathbb E|U(T)_{ij}|^2)_{1\le i,j\le5}\). Then \(\mathcal M_T=J_5/5\) **if and only if** the following six cosine moments take their indicated values:
\[
\begin{aligned}
\mathbb E\cos(\sqrt3 T)&=-\tfrac15, &\mathbb E\cos T&=0,\\
\mathbb E\cos(2\sqrt3 T)&=-\tfrac15,&\mathbb E\cos(2T)&=-\tfrac15,\\
\mathbb E\cos((\sqrt3-1)T)&=0,&\mathbb E\cos((\sqrt3+1)T)&=0.
\end{aligned}
\]
Such distributions exist. More precisely, **for every real threshold \(L\)**, there exist \(1\le s\le7\), pairwise distinct \(t_1,\ldots,t_s>L\), and strictly positive \(w_1,\ldots,w_s\) summing to one, such that
\[
\sum_{r=1}^s w_r |U(t_r)_{ij}|^2=\tfrac15\quad(1\le i,j\le5).
\]
Thus one common randomized observation-time law produces an exactly uniform average from every starting vertex, and its entire support can be postponed past any prescribed deadline.

## Assumptions and scope
The graph is the simple five-vertex path with four edges of weight one, zero onsite potentials, and adjacency (not Laplacian) Hamiltonian. Time ranges over the real numbers. The uniformity assertion concerns the expectation of squared transition amplitudes, not an instantaneous uniform mixing matrix, nor a standard unweighted infinite-time average. The six-moment criterion applies to *every* Borel probability law on real time. The finite-support assertion allows arbitrary strictly later times and weights depending on the chosen threshold; it is existential and does not provide a closed-form schedule.

## Proof
The path adjacency matrix has five simple eigenvalues \(\sqrt3,1,0,-1,-\sqrt3\). Let \(E,F,Q\) be its orthogonal spectral projectors for \(\sqrt3,1,0\), respectively. They can be reconstructed without eigenvectors by spectral interpolation,
\[
P_\lambda=\prod_{\mu\ne\lambda}\frac{A-\mu I}{\lambda-\mu},
\qquad \lambda,\mu\in\{\sqrt3,1,0,-1,-\sqrt3\}.
\]
Let \(D=\operatorname{diag}(1,-1,1,-1,1)\). Bipartite symmetry gives \(P_{-\sqrt3}=DED\), \(P_{-1}=DFD\). Consequently the matrix entries of \(U(t)\), with \(\theta=\sqrt3t\) and \(\varphi=t\), are
\[
U(t)_{ij}=\begin{cases}
Q_{ij}+2E_{ij}\cos\theta+2F_{ij}\cos\varphi,&i-j\text{ even},\\
2i(E_{ij}\sin\theta+F_{ij}\sin\varphi),&i-j\text{ odd}.
\end{cases}
\]
Set the six real moments
\[
\begin{aligned}
x&=\mathbb E\cos\theta,&y&=\mathbb E\cos\varphi,\\
X&=\mathbb E\cos^2\theta,&Y&=\mathbb E\cos^2\varphi,\\
Z&=\mathbb E(\cos\theta\cos\varphi),&W&=\mathbb E(\sin\theta\sin\varphi).
\end{aligned}
\]
For same-parity vertex indices put \(a=Q_{ij}\), \(b=2E_{ij}\), \(c=2F_{ij}\). Then \(\mathcal M_{T,ij}=a^2+b^2X+c^2Y+2abx+2acy+2bcZ\). For opposite parity it equals \(b^2(1-X)+c^2(1-Y)+2bcW\). These identities are valid for any sampling law, without symmetry or independence assumptions.

Inserting the exactly computed projector entries, the six requirements \(\mathcal M_{T,ij}=1/5\) at \((i,j)=(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)\) reduce respectively to
\[
\begin{aligned}
5X+45Y+30Z+20x+60y&=16,\\
10\sqrt3W-5X-15Y&=-8,\\
5X-10x&=4,\\
10\sqrt3W+5X+15Y&=8,\\
5X+5Y+10Z&=4,\\
5X&=2.
\end{aligned}
\]
The determinant of this linear system in the variable order \((x,y,X,Y,Z,W)\), using coefficients of \(\mathcal M_{T,ij}-1/5\) rather than the rescaled display, is \(\sqrt3/972\ne0\). Its unique solution is
\[
(x,y,X,Y,Z,W)=(-\tfrac15,0,\tfrac25,\tfrac25,0,0).
\]
Substitution into the general entry formulas yields \(\mathcal M_{T,ij}=1/5\) also for the nine remaining upper-triangular entries. Finally, \(\cos(2\alpha)=2\cos^2\alpha-1\) and \(\cos(\theta\pm\varphi)=\cos\theta\cos\varphi\mp\sin\theta\sin\varphi\) translate this unique six-vector exactly into the six stated cosine moments. This proves necessity and sufficiency.

For existence, introduce auxiliary angles \((\theta,\varphi)\) on the two-dimensional torus with independent absolutely continuous distributions having respective densities
\[
f(\theta)=\frac{1-\tfrac25\cos\theta-\tfrac25\cos(2\theta)}{2\pi},
\qquad
 g(\varphi)=\frac{1-\tfrac25\cos(2\varphi)}{2\pi}.
\]
Both are normalized and strictly positive: \(f\ge1/(10\pi)\) and \(g\ge3/(10\pi)\). Fourier orthogonality gives \(\mathbb E\cos\theta=-1/5\), \(\mathbb E\cos\varphi=0\), both cosine-square means \(2/5\), and \(Z=W=0\). Therefore their torus-averaged mixing matrix is precisely \(J_5/5\).

The map \(\Phi:(\theta,\varphi)\mapsto(|(P_{\sqrt3}e^{i\theta}+P_1e^{i\varphi}+Q+P_{-1}e^{-i\varphi}+P_{-\sqrt3}e^{-i\theta})_{ij}|^2)_{ij}\) is continuous. Its affine image lies in a space of dimension at most six by the six-moment formulas. Because the auxiliary product density is everywhere strictly positive, its barycenter \(J_5/5\) is in the relative interior of \(\operatorname{conv}\Phi(\mathbb T^2)\): any supporting affine functional attaining equality at the barycenter would have to be constant throughout the torus.

Since \(\sqrt3\) is irrational, Kronecker's density theorem for a continuous two-frequency flow shows that \(\{(\sqrt3t\bmod2\pi,t\bmod2\pi):t>L\}\) is dense in \(\mathbb T^2\) for every real \(L\). The convex hull of the corresponding physical mixing matrices is dense in the torus convex hull, and a dense convex subset of a finite-dimensional convex set contains its relative interior. Hence the exact barycenter is a finite convex combination of physical mixing matrices at times greater than \(L\). Carathéodory's theorem in affine dimension at most six reduces the support to at most seven. Remove zero weights and merge any repeated times to obtain strictly positive weights at distinct times. This completes the proof.

## Verification
Run `python3 verify.py` with SymPy installed. The program independently constructs all five spectral projectors from the original adjacency matrix, checks their eigenrelations and bipartite conjugation, derives the 15 symbolic upper-triangular mixing equations, verifies the six-by-six determinant \(\sqrt3/972\), solves for the unique moment vector, and confirms exact uniformity in all entries. An auxiliary 64-node periodic quadrature checks the explicit positive torus law numerically to tolerance \(10^{-12}\). The infinite density/relative-interior/Kronecker/Carathéodory step is analytical, not certified by the finite quadrature.

## Relationship to prior work
Baptista, Coutinho and Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378 (first public preprint 2023-08-31), introduced arbitrary-time averaging and proved exact uniform averages for \(P_3\) and \(P_4\) (Sections 3.2 and 4.3); their Section 7 explicitly asks about larger paths. Coutinho and Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236 (Section 4.2), still identified the existence question for \(P_n\), \(n\ge5\), as open in 2024. The present result resolves the first of those instances with necessary *and sufficient* numerical moment data and strictly late finite support. Standard uniform-in-time averages, instantaneous uniform mixing, weighted-graph universal mixing, and Szegedy-walk averages are different requirements and do not supply this result.

## Limitations
This result does **not** settle arbitrary paths with more than five vertices, nor supply a constructive algorithm producing the exact real observation times and weights, nor prove that seven support points are needed. Its existential finite-time conclusion uses exact real arithmetic and a density/convexity argument. The literature comparison may miss a later or differently indexed equivalent theorem. No independent mathematical audit has been performed.

## References
1. P. Baptista, G. Coutinho and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378 (2023), Sections 3.2, 4.3, 7; https://arxiv.org/pdf/2308.16378 .
2. G. Coutinho and K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236 (2024), Section 4.2; https://arxiv.org/pdf/2404.02236 .
3. W. Carlson et al., *Universal Mixing of Quantum Walk on Graphs*, arXiv:quant-ph/0608044 (2006); https://arxiv.org/abs/quant-ph/0608044 (a distinct edge-weight variation model).
4. J. Sorci, *Average Mixing in Quantum Walks of Reversible Markov Chains*, arXiv:2211.02037 (2022); https://arxiv.org/abs/2211.02037 (a distinct discrete-time Szegedy-walk model).
