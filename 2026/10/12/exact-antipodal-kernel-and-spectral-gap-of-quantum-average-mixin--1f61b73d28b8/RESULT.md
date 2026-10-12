# Exact antipodal kernel and spectral gap of quantum average mixing on even halved cubes

## Finding
For each **even integer** \(d\ge6\), let \(H_d\) be the halved \(d\)-cube: its vertices are the even-weight vectors \(x\in\mathbb F_2^d\), with two vertices adjacent exactly when their Hamming distance is two. With the ordinary unweighted adjacency Hamiltonian \(A_d\), define
\[
\widehat M_d=\lim_{T\to\infty}\frac1T\int_0^T e^{itA_d}\circ e^{-itA_d}\,dt.
\]
Write \(s=(1,\ldots,1)\in\mathbb F_2^d\). Then the **complete kernel** is
\[
\ker\widehat M_d=\{f:\mathbb F_2^d\supseteq V(H_d)\to\mathbb R:\ f(x+s)=-f(x)\text{ for every }x\in V(H_d)\}.
\]
In particular,
\[
\operatorname{rank}\widehat M_d=2^{d-2},\qquad
\dim\ker\widehat M_d=2^{d-2}.
\]
The positive spectral sector consists exactly of functions symmetric under the antipodal map.

More precisely, index Fourier characters on \(V(H_d)\) by cosets \([z]\in\mathbb F_2^d/\langle s\rangle\), and let \(w=|z|\). Define for even nonnegative \(r\)
\[
\alpha_r=\frac{\binom{r}{r/2}}{2^r}.
\]
The eigenvalue of \(\widehat M_d\) on the character \(x\mapsto(-1)^{z\cdot x}\) is
\[
\boxed{\mu_{[z]}=
\begin{cases}
0,&w\text{ odd},\\
\alpha_w+\alpha_{d-w}-\alpha_w\alpha_{d-w},&w\text{ even}.
\end{cases}}
\]
This description includes every eigenvalue with its character-indexed multiplicity. Equivalently, for each even \(w<d/2\) the listed positive value occurs with multiplicity \(\binom dw\); if \(4\mid d\), the central even weight \(w=d/2\) occurs with multiplicity \(\frac12\binom d{d/2}\). Identical numerical eigenvalues, if any, have their listed multiplicities added. Zero has multiplicity \(2^{d-2}\).

The **smallest positive eigenvalue** is exact. Put \(m=d/2\), \(r=\lfloor m/2\rfloor\) and \(t=\lceil m/2\rceil\); then
\[
\boxed{\gamma_d=1-\left(1-\frac{\binom{2r}{r}}{4^r}\right)
\left(1-\frac{\binom{2t}{t}}{4^t}\right)>0},
\qquad \gamma_d\sim\frac4{\sqrt{\pi d}}\quad(d\to\infty\text{ through even integers}).
\]
For example, \(H_6\) has 32 vertices, rank 16 and gap \(11/16\); \(H_8\) has 128 vertices, rank 64 and gap \(39/64\).

## Assumptions and scope
The assertion concerns the simple undirected distance-two component on even binary words, the adjacency Hamiltonian with every edge weight one, and the infinite-time Cesàro average of entrywise transition probabilities. All statements hold for every even integer \(d\ge6\), without genericity or numerical assumptions. The same spectral computation also works at \(d=4\), where the graph is a complete multipartite graph; that low-dimensional case is not advanced as new. It does **not** assert a rank theorem for arbitrary cubelike or distance-regular graphs, nor a conclusion about instantaneous uniform mixing.

## Proof
Let \(G=\{x\in\mathbb F_2^d:|x|\equiv0\pmod2\}\), an additive group of order \(N=2^{d-1}\). The graph is the Cayley graph of \(G\) with generating set consisting of all binary vectors of weight two. Its characters are
\[
\chi_{[a]}(x)=(-1)^{a\cdot x},\qquad [a]\in\widehat G=\mathbb F_2^d/\langle s\rangle.
\]
Indeed \(\chi_a=\chi_{a+s}\) on \(G\), and these are the only identifications. If \(j=|a|\), the adjacency eigenvalue is
\[
\theta_{[a]}=\sum_{1\le i<j\le d}(-1)^{a_i+a_j}
=\frac{(d-2|a|)^2-d}{2}.
\]
The expression is invariant under replacing \(a\) by \(a+s\). Equality \(\theta_{[a]}=\theta_{[b]}\) holds exactly when \(|a|=|b|\) or \(|a|+|b|=d\); no other energies coincide.

For an energy \(\theta\), let \(B_\theta\) be its set of dual characters. Its real orthogonal spectral projector has the explicit kernel
\[
E_\theta(x,y)=\frac1N\sum_{[a]\in B_\theta}\chi_{[a]}(x+y).
\]
The finite spectral expansion of the unitary evolution and Cesàro averaging imply the standard identity \(\widehat M_d=\sum_\theta E_\theta\circ E_\theta\). Expanding the squares, grouping character products, and applying orthogonality shows that each \(\chi_{[z]}\) is an eigenvector of \(\widehat M_d\) with eigenvalue
\[
\mu_{[z]}=\frac1N\#\{[a]\in\widehat G:\theta_{[a]}=\theta_{[a+z]}\}.
\]
To count without choosing dual representatives, fix a lift \(z\in\mathbb F_2^d\) with \(|z|=w\), and let \(a\) range over all \(2^d\) binary words. Each dual coset is counted twice. Let \(t\) count the ones of \(a\) on the support of \(z\), and let \(u\) count its ones off that support. Then \(|a|=t+u\) and \(|a+z|=w-t+u\). Equality of the *squared* adjacency energy parameters is equivalent to
\[
|a|=|a+z|\ \Longleftrightarrow\ 2t=w,
\qquad |a|+|a+z|=d\ \Longleftrightarrow\ 2u=d-w.
\]
When \(w\) is odd and \(d\) is even, both conditions are impossible. When \(w\) is even, their respective numbers of solutions are
\[
2^{d-w}\binom{w}{w/2}
\quad\text{and}\quad
2^w\binom{d-w}{(d-w)/2}.
\]
Their intersection has \(\binom{w}{w/2}\binom{d-w}{(d-w)/2}\) solutions. Divide the inclusion–exclusion count by \(2^d\) (two lifts per character and \(N=2^{d-1}\)) to obtain the asserted exact eigenvalue formula. It depends only on the coset \([z]\), since \(w\) and \(d-w\) are interchanged by adding \(s\).

For even \(d\), the parity of \(|z|\) is also well-defined on the coset. Every even-weight coset has strictly positive eigenvalue, because each \(\alpha_r>0\) and the displayed expression is \(1-(1-\alpha_w)(1-\alpha_{d-w})>0\). Every odd-weight coset has eigenvalue zero. Precisely half the \(2^{d-1}\) dual cosets are of odd weight. Moreover \(\chi_{[z]}(x+s)=(-1)^{|z|}\chi_{[z]}(x)\), and the characters form a real orthogonal basis. Thus the odd-weight sector is **exactly** the antipodally antisymmetric kernel, of dimension \(2^{d-2}\); the even sector is positive definite and has the same dimension.

For the sharp positive gap, write \(d=2m\) and \(w=2j\), and put \(c_j=\binom{2j}{j}/4^j\) and \(b_j=1-c_j\) for \(0\le j\le m\). The positive eigenvalue at weight \(2j\) is \(1-b_jb_{m-j}\). A direct ratio gives
\[
c_{j+1}=\frac{2j+1}{2j+2}c_j,
\qquad b_{j+1}-b_j=\frac{c_j}{2j+2}>0.
\]
These increments strictly decrease with \(j\); therefore \(b_j\) is nonnegative, increasing, and discretely concave. As a consequence its positive terms are log-concave (the arithmetic mean bounds the geometric mean). Hence the symmetric product \(b_jb_{m-j}\) is maximized at \(j=\lfloor m/2\rfloor\) or \(j=\lceil m/2\rceil\), giving the exact formula for \(\gamma_d\). Finally the central-binomial asymptotic \(\binom{2j}{j}/4^j\sim1/\sqrt{\pi j}\) proves \(\gamma_d\sim4/\sqrt{\pi d}\).

## Verification
Run `python3 verify.py` with Python 3 and its standard library. The checker constructs the distance-two halved-cube adjacency action directly, verifies all Fourier adjacency eigenvector identities, constructs the exact Schur-square mixing kernel from its spectral projectors, and checks each predicted mixing eigenvalue by a second exact Fourier transform for dimensions 3 through 10. It also checks binomial intersection counts in even dimensions 4 through 24, antipodal symmetry, the kernel rank, and the claimed sharp gap. The reported check output is in `VERIFICATION.md`. All finite checks supplement rather than establish the unrestricted proof.

## Relationship to prior work
Godsil (2013; arXiv:1103.2578) established the spectral-projector formula and basic positivity properties of average mixing. Coutinho, Godsil, Guo, and Zhan (2018; arXiv:1709.03591) related its kernel to strong cospectrality. Ada Chan (2020; arXiv:1305.5811, Section 5) established halved-cube adjacency eigenvalues and characterized **instantaneous** uniform mixing; her results also identify perfect state transfer in even halved cubes. These give a reason to expect antipodal null directions, but not the reverse kernel inclusion, full Cesàro spectrum, or sharp positive gap proved here. Coutinho, Baptista, Godsil, Spier, and Werner (2022; arXiv:2208.08971) provide general exact-computation methods for average mixing. Coutinho and Guo (2024; arXiv:2404.02236) discuss average-mixing rank problems more broadly. Their primitive distance-regular graph problem is **not** claimed to be settled here: the even halved cubes have antipodal structure.

For odd dimensions the halved cube has the same character-projector partition, under an appropriate group identification, as the corresponding folded cube; those odd-dimensional spectral consequences are not claimed as a separate contribution. The dimension-four halved cube is complete multipartite and likewise lies within known simpler results. The contribution is the dimension-uniform even case with \(d\ge6\), including exact positivity on the antipodally symmetric sector.

## Limitations
The kernel and positive spectrum concern adjacency-generated **infinite-time** mixing, not finite-time probability distributions, arbitrary couplings, graph Laplacians, or resistance to perturbations. Although the closed forms follow from standard harmonic analysis, a logically equivalent formulation may occur in a broader source not located during the literature comparison. No independent validation has yet occurred. Numerical checks through dimension ten do not prove the infinite-family statement; the unrestricted result follows from character orthogonality and inclusion–exclusion.

## References
- C. Godsil, *Average Mixing of Continuous Quantum Walks*, Journal of Combinatorial Theory A **120** (2013), 1649–1662; arXiv:1103.2578.
- A. Chan, *Complex Hadamard Matrices, Instantaneous Uniform Mixing and Cubes*, Algebraic Combinatorics **3** (2020), 757–774; arXiv:1305.5811, especially Section 5.
- G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, Electronic Journal of Combinatorics **25** (2018), P4.14; arXiv:1709.03591.
- G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational Quantum Walks*, SIAM Journal on Applied Algebra and Geometry (2023); first public preprint 2022-08-18, arXiv:2208.08971.
- G. Coutinho, K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, 2024 preprint, arXiv:2404.02236.
