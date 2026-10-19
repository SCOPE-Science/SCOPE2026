# Exact Hamming-depth correction to percolated Grover absorption on hypercubes

## Finding
Let \(d\ge3\) be an integer. For the dynamically percolated flip-flop Grover walk on the Boolean hypercube \(Q_d\), with a sink at \(0^d\), start from a normalized directed-edge state \(\lvert x\to y\rangle\) with \(\lvert x\rvert=k\), \(\lvert y\rvert=k+1\), and \(1\le k\le d-1\). Here the vertical bars on binary vectors denote Hamming weight. All undirected edges are independently open with a fixed probability \(p\in(0,1)\) at each time step; the sink absorbs after every step. The exact probability \(q_{d,k}\) of eventual absorption is
\[
q_{d,k}=\frac{1+R_{d,k}}{2},
\]
where the following entirely explicit rational expression gives the unit-conductance effective resistance of the edge \(\{x,y\}\) in \(Q_d\setminus\{0^d\}\):
\[
\begin{aligned}
R_{d,k}&=\frac{2(1-2^{-d})}{d}
+\frac{d-1}{d-2+2^{1-d}}\biggl[
 k(B_{d,k}-B_{d,k+1})^2\\
&\qquad +4B_{d,k+1}^{2}
 +(d-k-1)(B_{d,k+1}-B_{d,k+2})^2\biggr],\\
B_{d,h}&=\frac{\sum_{j=h}^{d}\binom dj}{2^{d}d\binom{d-1}{h-1}}
=\int_0^{1/2}t^{h-1}(1-t)^{d-h}\,dt
\quad(1\le h\le d),\\
B_{d,d+1}&=0.
\end{aligned}
\]
The formula is independent of \(p\). The bracket is strictly positive; hence the single-vertex sink's removal from the cycle network produces an exact, positive, position-dependent correction to the intact-cube edge resistance. For each fixed \(k\ge1\), as \(d\to\infty\) through integers with \(d>k\),
\[
q_{d,k}=\frac12+\frac{1-2^{-d}}{d}
+\frac{k((k-1)!)^2}{2d^{2k}}\bigl(1+O_k(d^{-1})\bigr).
\]
Thus the leading sink-deletion correction to eventual absorption is of order \(d^{-2k}\): the farther the initially occupied edge lies from the sink, the more strongly that correction is suppressed. At \(d=3\), for example, \(q_{3,1}=17/20\) and \(q_{3,2}=4/5\).

## Assumptions and scope
The vertices of \(Q_d\) are bit strings of length \(d\). Every vertex has \(d\) outgoing arc states, indexed by flipped coordinate. The local coin is \(C_d=2\lvert s_d\rangle\langle s_d\rvert-I\), where \(\lvert s_d\rangle\) is the normalized uniform coin vector. For each open edge, the shift exchanges its two arcs; for a closed edge, the shift leaves both arcs fixed. The open/closed indicators have full support and are independently resampled after each step. After applying shift and coin, the entire sink-origin arc subspace is projected away. The initial state is a *single* outgoing arc on an edge of the indicated Hamming depths, neither endpoint being the sink. The limit defining eventual absorption exists as the decreasing limit of total surviving trace; no finite-time convergence rate is claimed.

All resistance computations refer to unweighted undirected graph edges interpreted as unit conductors. The punctured hypercube is connected for \(d\ge2\). The expression depends only on \(d,k\) by coordinate permutation symmetry. The sign/orientation of the initial directed arc does not affect the answer.

## Proof
**Step 1 — trapping is a cycle-space projection.** The common-eigenstate characterization of the dynamically percolated Grover walk with a sink, proved by Mareš, Novotný, Štefaňák, and Jex, identifies its sink-resistant trapped states with arc assignments having equal values on the two orientations of every undirected edge and a zero sum at every vertex. The common \(+1\) uniform state is excluded by the sink. For the bipartite graph \(H=Q_d\setminus\{0^d\}\), multiply the vertex-sum constraint by \(-1\) on one bipartition to obtain the usual signed-incidence conservation law. Let \(D\) be a signed incidence matrix of \(H\). The trapped subspace is therefore isometric to \(\ker D\) except that each edge coordinate appears twice in the arc Hilbert space. Consequently, for a unit arc supported on an edge \(e\), the squared norm of its projection onto the trapped subspace equals \(\frac12(P_{\ker D})_{ee}\). As \(P_{\ker D}=I-D^{\mathsf T}(DD^{\mathsf T})^+D\), the well-known electrical identity gives \((P_{\ker D})_{ee}=1-R_H(e)\). The probability absorbed is \(1-\frac12(1-R_H(e))\), yielding \(q_{d,k}=(1+R_H(e))/2\). This step relies on the complete asymptotic-attractor theorem for the specified percolated walk; the subsequent resistance evaluation is elementary and self-contained.

**Step 2 — delete one hypercube vertex by a rank-\(d-1\) update.** Write the full hypercube Laplacian in the block form
\[
L_{Q_d}=\begin{pmatrix}d&-c^{\mathsf T}\\-c&L_{RR}\end{pmatrix},
\]
with \(c\) the indicator of the \(d\) neighbors of \(0^d\), and \(R=V(Q_d)\setminus\{0^d\}\). Eliminating the sink by a Schur complement gives \(L_K=L_{RR}-cc^{\mathsf T}/d\), whereas the deleted-vertex Laplacian is \(L_H=L_{RR}-\operatorname{diag}(c)=L_K-P\), where \(P=\operatorname{diag}(c)-cc^{\mathsf T}/d\) is the orthogonal projector onto the zero-sum space supported by the sink's neighbors. All inverses below are on mean-zero vectors. By the full symmetry permuting the \(d\) coordinates, the restriction of \(L_K^+\) to \(\operatorname{ran}P\) is scalar: \(PL_K^+P=\kappa P\). Applying a unit current between two distinct neighbors of the sink gives \(\kappa=\frac12R_{Q_d}(\mathrm{distance}\ 2)=B_{d,1}+B_{d,2}=(1-2^{1-d})/(d-1)<1\). The rank-update identity therefore yields, for any two surviving vertices \(x,y\), with \(b=\mathbf e_x-\mathbf e_y\),
\[
R_H(x,y)=R_{Q_d}(x,y)
+\frac{\lVert PL_K^+b\rVert^2}{1-\kappa}.
\]
The first term for adjacent vertices is \(R_{Q_d}(x,y)=2(1-2^{-d})/d=2B_{d,1}\).

**Step 3 — compute the update from the Boolean heat kernel.** Let \(g(h)\) be the mean-zero Green kernel of the full cube Laplacian at Hamming distance \(h\). Spectral calculus with the product heat kernel gives
\[
g(h-1)-g(h)=2^{-d}\int_0^1(1+z)^{d-h}(1-z)^{h-1}\,dz=B_{d,h}.
\]
The second equality uses \(t=(1-z)/2\), and direct binomial integration gives the stated rational form. Choose coordinates with \(x=1^k0^{d-k}\) and \(y=1^{k+1}0^{d-k-1}\). The potential \(u=L_K^+b\), evaluated at the \(d\) neighbors of the sink, differs by a common constant from \(g(\operatorname{dist}(\cdot,x))-g(\operatorname{dist}(\cdot,y))\). Those \(d\) values are \(B_{d,k}\) with multiplicity \(k\), \(-B_{d,k+1}\) with multiplicity one, and \(B_{d,k+2}\) with multiplicity \(d-k-1\). Their mean is \(B_{d,k+1}\): the potential is harmonic at the sink, because \(x,y\ne0^d\). It follows that
\[
\lVert Pu\rVert^2=k(B_{d,k}-B_{d,k+1})^2+4B_{d,k+1}^2
+(d-k-1)(B_{d,k+1}-B_{d,k+2})^2.
\]
Since \((1-\kappa)^{-1}=(d-1)/(d-2+2^{1-d})\), substitution proves the exact formula. For \(k=d-1\), the last multiplicity is zero; the definition \(B_{d,d+1}=0\) makes the expression unambiguous. The strictly positive middle square proves strict positivity of the correction.

**Step 4 — fixed-depth asymptotics.** For each fixed positive integer \(h\), the beta integral implies \(B_{d,h}=(h-1)!d^{-h}(1+O_h(d^{-1}))\). In the square bracket the first term is \(k((k-1)!)^2d^{-2k}(1+O_k(d^{-1}))\); the other two terms are smaller by at least one power of \(d\). Moreover \((1-\kappa)^{-1}=1+O(d^{-1})\). Combining these estimates and dividing the resistance correction by two proves the asserted absorption asymptotic.

## Verification
The bundled `verify.py` independently builds each punctured-cube Laplacian and solves a sparse grounded resistance system for every \(3\le d\le8\) and \(1\le k<d\). All \(27\) numerical electrical resistances agree with the exact rational formula to absolute error at most \(5.56\times10^{-16}\). It also simulates the actual averaged percolated Grover density channel on \(Q_3\), including projection onto the nonsink subspace after every time step, for \(600\) steps for each \(k\in\{1,2\}\) and \(p\in\{0.4,0.7\}\). All four survival probabilities agree with \((1-R_{3,k})/2\) to within \(6.83\times10^{-15}\). These finite computations corroborate the proof and do not themselves establish an infinite-time limit or all-dimensional truth. Run using Python with NumPy and SciPy: `python verify.py`.

## Relationship to prior work
Mareš–Novotný–Jex (2018 preprint; 2019 journal) gave the trapped-state method and treated single-sink transport on the ordinary three-dimensional cube, including the dependence on coherent initial coin states. Mareš–Novotný–Štefaňák–Jex (2022 preprint) proved a general theorem for arbitrary finite simple graphs and provided structural transport examples. Both are essential antecedents; the general projection rule is **not** claimed as new. Ambainis–Prūsis–Vihrovs–Wong (2016) established a related electrical-circuit method for oscillatory localization of a different, unpercolated walk. The finding here is the explicit all-dimensional *punctured-hypercube*, Hamming-shell edge-resistance formula and its sharp fixed-depth \(d^{-2k}\) transport correction, rather than a reformulation of the general trapping theorem or the three-cube case.

## Limitations
The result assumes independent dynamical edge percolation with full-support probability, a flip-flop shift, an exactly Grover coin, a single fully absorbing sink vertex, and a single initially occupied directed edge with neither endpoint at the sink. It does not apply verbatim to static percolation, arbitrary coherent edge superpositions, incomplete absorption, or finite-time mixing. The asymptotic statement keeps the Hamming depth fixed as dimension grows and makes no uniform claim when depth grows with dimension. Priority remains open to an undiscovered earlier implicit electrical-network calculation.

## References
1. J. Mareš, J. Novotný and I. Jex, *Percolated quantum walks with a general shift operator: From trapping to transport*, arXiv:1812.02519v1 (public 6 December 2018), later Phys. Rev. A **99**, 042129 (2019). https://arxiv.org/abs/1812.02519
2. J. Mareš, J. Novotný, M. Štefaňák and I. Jex, *Key graph properties affecting transport efficiency of flip-flop Grover percolated quantum walks*, arXiv:2202.09582v1 (public 19 February 2022), later Phys. Rev. A **105**, 062417 (2022). https://arxiv.org/abs/2202.09582
3. A. Ambainis, K. Prūsis, J. Vihrovs and T. G. Wong, *Oscillatory Localization of Quantum Walks Analyzed by Classical Electric Circuits*, arXiv:1606.02136v1 (2016). https://arxiv.org/abs/1606.02136
