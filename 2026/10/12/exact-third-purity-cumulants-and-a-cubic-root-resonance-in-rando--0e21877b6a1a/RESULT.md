# Exact third purity cumulants and a cubic-root resonance in random Hadamard states

## Finding
For every pair of integers \(U,V\ge2\), consider the independent phase-flat bipartite state
\[
|\psi\rangle=\frac1{\sqrt{UV}}\sum_{i=1}^{U}\sum_{j=1}^{V}s_{ij}|i\rangle\otimes|j\rangle.
\]
Each \(s_{ij}\) is uniform on the \(q\)-th roots of unity, independently, with \(q\in\{2,3,4,\ldots\}\); alternatively \(q=\infty\) means independent Haar-uniform unit-circle phases. Let \(P=\operatorname{Tr}(\rho_A^2)\), where \(\rho_A=\operatorname{Tr}_B|\psi\rangle\langle\psi|\), and set
\[
N=UV,\quad R=\binom U2\binom V2,\quad T=\binom U2\binom V3+\binom U3\binom V2.
\]
We use the convention \(\binom ab=0\) for nonnegative integers \(b>a\). The mean and variance are the established quantities
\[
\mu=\mathbb E P=\frac{U+V-1}{N},\qquad
\operatorname{Var}(P)=\frac{16R}{N^4}\ \ (q=2),\qquad
\operatorname{Var}(P)=\frac{8R}{N^4}\ \ (q\ge3\text{ or }q=\infty).
\]
The **third central moment**, which is the third cumulant, is exactly
\[
\boxed{\mathbb E[(P-\mu)^3]=\frac{64}{N^6}\begin{cases}
6T,&q=2,\\
(6T+R)/4,&q=3,\\
3T/2,&q\ge4\text{ or }q=\infty.
\end{cases}}
\]
In particular, \(q=3\) has an extra positive contribution from the phase-cubic resonance of a single plaquette, not apparent in the first two cumulants. The exact standardized skewness is
\[
\gamma_1(P)=\begin{cases}
6T/R^{3/2},&q=2,\\
(6T+R)/(\sqrt2 R^{3/2}),&q=3,\\
3\sqrt2\,T/R^{3/2},&q\ge4\text{ or }q=\infty.
\end{cases}
\]
Consequently for square dimensions \(U=V=d\to\infty\), \(\gamma_1=8/d+O(d^{-2})\) for \(q=2\), and \(\gamma_1=4\sqrt2/d+O(d^{-2})\) for every fixed \(q\ge3\) or for continuous phases. These identities quantify the leading finite-size asymmetry of the Gaussian approximation.

## Assumptions and scope
All dimensions \(U,V\) are integers at least two. The independent phases have the same uniform distribution as above; correlations among phase choices or random coefficient magnitudes are not allowed. The conclusion concerns the purity of **one designated bipartition**, not the average of purities over a family of cuts. The qubit special case takes \(U=2^a\), \(V=2^b\), \(a,b\ge1\); the \(q=2\) ensemble is the uniform real-sign (hypergraph) ensemble, \(q\ge3\) finite are Hadamard–Butson phase ensembles, and \(q=\infty\) is the continuous flat-phase ensemble.

## Proof
Index the phase array by rows \(i\) and columns \(j\). The reduced-state matrix is \((\rho_A)_{ii'}=N^{-1}\sum_j s_{ij}\overline{s_{i'j}}\). Expanding the trace of its square gives
\[
P=\frac1{N^2}\sum_{i,i',j,j'}s_{ij}\overline{s_{i'j}}s_{i'j'}\overline{s_{ij'}}.
\]
The cases \(i=i'\) or \(j=j'\) contribute exactly \((U+V-1)/N\). For each unordered row pair \(i<i'\) and column pair \(j<j'\), define the oriented plaquette holonomy
\[
z_R=s_{ij}s_{i'j'}\overline{s_{ij'}s_{i'j}}.
\]
Its four ordered appearances contribute \(4\operatorname{Re}(z_R)/N^2\). Therefore
\[
P-\mu=\frac4{N^2}\sum_{R\in\mathcal R}\operatorname{Re}(z_R),\qquad |\mathcal R|=R.
\]
Every holonomy has expectation zero. Uniform root phases satisfy \(\mathbb E[s^k]=1\) if \(q\mid k\), and zero otherwise; for \(q=\infty\), only \(k=0\) survives. This identity also shows that any two distinct plaquettes have zero covariance: they cannot have identical four-cell supports. Moreover \(\mathbb E[(\operatorname{Re}z_R)^2]=1\) for \(q=2\) and \(1/2\) otherwise, yielding the stated variance.

Expand the centered third moment into ordered triples of rectangles. There are three cases.

**One repeated plaquette three times.** The moment \(\mathbb E[(\operatorname{Re}z_R)^3]\) equals \(1/4\) for \(q=3\) and zero for all other allowed \(q\). Indeed the expansion \((z+\bar z)^3/8\) has nonzero expectation only for \(z^3\) and \(\bar z^3\), and only cubic roots of unity make these averages nonzero. This contributes \(R/4\).

**Exactly two identical plaquettes.** Every term vanishes: the third, distinct plaquette includes a cell not contained in the repeated one, giving a unit phase exponent that averages to zero.

**Three pairwise distinct plaquettes.** For a term to survive, each cell of their union must appear in at least two of the three plaquettes; otherwise that cell has exponent \(\pm1\). Two distinct grid rectangles share at most two cells. If their intersection has fewer than two cells, their symmetric difference contains more than four cells and cannot be contained in the third rectangle. Thus a surviving triple has pairwise intersections of size exactly two, with each cell appearing exactly twice, and the third rectangle is the symmetric difference of the first two. These are precisely the triples of rectangles formed by fixing two rows and choosing three columns, or fixing two columns and choosing three rows. Their number as unordered triples is
\[
T=\binom U2\binom V3+\binom U3\binom V2.
\]
For each such unordered triangle, all \(3!=6\) orderings occur. When \(q=2\), each of the eight orientations in the expansion of three real parts survives because the two appearances at each cell give even exponents, so the expectation is \(1\). For \(q\ge3\), exactly two orientations survive (the two globally consistent opposite circulations), giving expectation \(2/8=1/4\). Hence all distinct-triple terms contribute \(6T\) for \(q=2\) and \(6T/4\) otherwise. Adding the one-plaquette contribution and multiplying by \((4/N^2)^3\) proves the formula.

Finally, the stated square-dimensional skewness follows from \(R=d^4/4+O(d^3)\), \(T=d^5/6+O(d^4)\), together with the exactly evaluated variances and third moments.

## Verification
The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py`. It exhaustively checks the phase-monomial expectation criterion for all rectangle triples on six rectangular grids \((U,V)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), with alphabets \(q=2,3,4,5,6\), giving 30 exact monomial comparisons. It also exhaustively enumerates 72,706 phase arrays on the specified small grids and checks their first three moment identities with exact rational arithmetic; the phase-to-purity rectangle identity is separately compared with the reduced Gram-matrix purity on all small arrays or a stated deterministic sample. The recorded successful run returned `VERIFY_OK 30 exact monomial tests; 72706 complete phase-array state comparisons`. The general theorem is proved by the preceding combinatorial argument; no finite test is used as a substitute for that proof.

## Relationship to prior work
Trotta et al., *Multipartite entanglement of random states of qubits* (arXiv:2605.10314v1), define exactly these independent Hadamard–Butson phase ensembles, derive the fixed-cut purity expansion (their Eq. 23), the mean (Eq. 24), the variance (Eq. 26), and the corresponding first two cumulants for average purity. Their Section V compares numerical fixed-cut distributions with Gaussian approximations. The formula above keeps these established quantities unchanged but evaluates the **third central moment at one fixed cut** through the additional rectangle-triangle and cubic-root phase combinatorics. Scarafile et al., *Statistical mechanics of multipartite entanglement in hypergraph states* (arXiv:2609.24508v1), investigate a different ensemble statistic, purity averaged across balanced cuts in an effective classical energy landscape, and exact low-qubit counts. The latter work's full text was not accessible for complete comparison, so possible implicit finite-size overlap remains a limitation. Mirsohi's *Exact Haar Statistics of Planar k-Purity in Multipartite Quantum Systems* (arXiv:2608.28914v1) treats a Haar ensemble and a different purity functional; it is not the same discrete fixed-cut random-phase model. No absolute priority is claimed.

## Limitations
The result does not supply the third cumulant of purity **averaged over multiple cuts**, nor the full distribution or a Berry–Esseen bound. A skewness tending to zero is not by itself a proof of a central limit theorem. The proof uses independent uniform phases and does not cover correlated hypergraph ensembles, nonuniform amplitudes, or Haar-typical complex coefficients. Relevant later literature can contain an equivalent calculation not identified in accessible sources; the closest September manuscript could only be read at abstract level.

## References
1. G. Trotta, P. Scarafile, P. Facchi, G. Magnifico, A. Mariano, G. Parisi, S. Pascazio, K. Życzkowski, *Multipartite entanglement of random states of qubits*, arXiv:2605.10314v1 (first posted 2026-05-11). https://arxiv.org/abs/2605.10314
2. P. Scarafile, G. Trotta, P. Facchi, G. Magnifico, G. Parisi, S. Pascazio, K. Życzkowski, *Statistical mechanics of multipartite entanglement in hypergraph states*, arXiv:2609.24508v1 (first posted 2026-09-21). https://arxiv.org/abs/2609.24508
3. Mirsohi, *Exact Haar Statistics of Planar k-Purity in Multipartite Quantum Systems*, arXiv:2608.28914v1 (first posted 2026-08-28). https://arxiv.org/abs/2608.28914
