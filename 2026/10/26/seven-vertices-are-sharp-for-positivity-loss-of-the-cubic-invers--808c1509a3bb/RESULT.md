# Seven vertices are sharp for positivity loss of the cubic inverse-Taylor heat step

## Finding
Let \(G\) be a finite, simple, connected, unweighted, undirected graph, let \(L_G\) be its combinatorial Laplacian, and let
\[
R_G(h)=\left(I+hL_G+\frac{h^2}{2}L_G^2+\frac{h^3}{6}L_G^3\right)^{-1},\qquad h\geq0.
\]
This is the \([0/3]\) Padé approximation of the heat evolution \(\exp(-hL_G)\). **Every such graph on at most six vertices has an entrywise strictly positive step matrix for every \(h>0\). Seven is the smallest graph order at which entrywise positivity can fail.** On the seven-vertex path \(P_7\), numbering vertices from one end, exact arithmetic gives
\[
(R_{P_7}(1))_{1,7}=-\frac{16229}{1505893633}<0.
\]
The same path is strictly positive at both \(h=1/2\) and \(h=2\), and is not entrywise nonnegative at \(h=3/4\) or \(h=1\). Thus the property reenters at larger step sizes for this fixed graph. For every graph and every \(h\geq0\), the step is symmetric, positive definite, has row sums one, and is a contraction in Euclidean norm.

## Assumptions and scope
Graphs are finite, simple, connected, loop-free, undirected, and **unweighted**. Edges have unit conductance. The timestep \(h\) is any nonnegative real number; there is no timestep restriction in the positive six-vertex statement. Positivity means entrywise positivity of the matrix, which is stronger than spectral stability. The minimum order is over this class of graphs. No assertion is made for arbitrary edge weights, directed generators, disconnected graphs, or all graphs with at least seven vertices. For the one-vertex graph, \(R_G(h)=I\).

## Proof
**Spectral properties.** For any \(h\geq0\), the real polynomial \(q_h(s)=1+hs+h^2s^2/2+h^3s^3/6\) is positive for \(s\geq0\). Since \(L_G\) is symmetric and positive semidefinite, \(Q_G(h)=q_h(L_G)\) is positive definite. Therefore its inverse exists, is symmetric positive definite, and has diagonal entries strictly positive. Since \(L_G\mathbf1=0\), also \(Q_G(h)\mathbf1=\mathbf1\), so \(R_G(h)\mathbf1=\mathbf1\). Eigenvalues of \(R_G(h)\) lie in \((0,1]\), proving Euclidean nonexpansiveness.

**Exact finite certificate for every order below seven.** Multiply \(Q_G(h)\) by six and write
\[
A_G(h)=6I+6hL_G+3h^2L_G^2+h^3L_G^3.
\]
Then \(R_G(h)=6A_G(h)^{-1}\). For distinct vertices \(i,j\), let \(C_{ij}(h)=(-1)^{i+j}\det A_G(h)_{\widehat j,\widehat i}\), the transposed cofactor appearing in \((A_G^{-1})_{ij}\). The diagonal entries of the inverse are already positive, and \(\det A_G(h)>0\) for all \(h\geq0\). It remains to certify \(C_{ij}(h)>0\) for \(h>0\).

The accompanying `verify.py` performs exhaustive **exact integer-polynomial arithmetic**, without a precompiled graph atlas. For each \(n=2,3,4,5,6\), it generates all \(2^{\binom n2}\) labeled simple graphs by edge bitmasks, reduces every labeled graph to a permutation orbit under all \(n!\) vertex permutations, and retains every connected isomorphism class. The resulting connected class counts are \(1,2,6,21,112\), respectively, totaling \(142\) classes. For every class, every unordered pair \(i<j\) is checked, totaling \(1933\) cofactor polynomials.

For \(1932\) of these cofactor polynomials all coefficients are nonnegative and at least one is positive. For the remaining polynomial, multiplying by \((1+h)^{32}\) gives a polynomial with all coefficients nonnegative and at least one positive. (The same multiplier works for every cofactor.) Thus, for all \(h>0\),
\[
(1+h)^{32}C_{ij}(h)>0,\qquad C_{ij}(h)>0.
\]
Every operation determining these signs is exact; there is no floating-point tolerance, timestep grid, probabilistic sampling, or unexamined graph class. The small-order statement follows.

**Seven-vertex witness and reentry.** For \(P_7\), compute its exact rational inverse \(R_{P_7}(h)\) at rational timesteps. The endpoint entry is
\[
\begin{aligned}
(R_{P_7}(1/2))_{1,7}&=\frac{1036685}{130532396219}>0,\\
(R_{P_7}(3/4))_{1,7}&=-\frac{529900671519}{16012967110980391}<0,\\
(R_{P_7}(1))_{1,7}&=-\frac{16229}{1505893633}<0,\\
(R_{P_7}(2))_{1,7}&=\frac{96462616}{19528273141}>0.
\end{aligned}
\]
At \(h=1/2\) and \(h=2\), that endpoint entry is the smallest of all \(49\) matrix entries; the complete matrices are therefore strictly positive. These exact rational identities, together with the preceding exhaustive proof, establish sharpness and the asserted nonmonotonicity in timestep.

## Verification
Run `python verify.py` with Python 3.10 or later and SymPy 1.12 or later. The program rebuilds graph permutation orbits from scratch, computes every necessary minor over \(\mathbb Z[h]\), multiplies coefficient vectors by \((1+h)\) at most 32 times, and tests coefficientwise positivity. It also builds the path Laplacian independently and checks the four exact rational inverse matrices and their row sums. The actual output is included in `verification_output.txt`: \(142\) connected isomorphism classes, \(1933\) off-diagonal tests, multiplier-degree distribution \(1932\) at zero and one at 32, and `VERIFICATION_OK`. An independent program need only reproduce these deterministic integer/rational computations; no stored numerical log substitutes for the cofactor identities.

## Relationship to prior work
Gottlieb, Shu, and Tadmor (2001) develop strong-stability-preserving time integration and discuss obstructions for general higher-order methods. Their general stability conditions do not imply this sharp graph-order statement for one fixed rational approximation. Blanes, Iserles, and Macnamara (2022) examine positivity-preserving graph-Laplacian integrators and construct different exponential/Patankar-based schemes; their accessible full text does not state the \([0/3]\) six-versus-seven cutoff. Previously recorded related calculations concern \([2/2]\) Gauss Padé, \([0/2]\) Padé, or two-stage Radau IIA stability functions: none of those rational maps equals the \([0/3]\) map studied here, so their numerical thresholds do not imply this result.

Masood and Yousuf (2010) consider positivity-preserving Padé schemes for inverse heat problems, making that paper an important possible historical overlap. Its abstract was examined, but its complete text was inaccessible in this comparison. We therefore **do not claim** that it excludes the present method or threshold. No general method-level originality is asserted for Padé approximation, positivity testing, graph orbit enumeration, or cofactor arithmetic.

## Limitations
The sharp minimal order is proved only for simple **unweighted** connected undirected graphs, not for all reversible Markov generators or all weighted graphs. The proof below seven is a computer-assisted *finite exhaustive* proof using exact symbolic arithmetic, rather than a graph-independent closed-form inequality. It does not classify every seven-vertex graph or determine the full interval structure of positivity for the path. Possible specialized prior coverage, particularly the inaccessible 2010 Padé article, remains a literature risk. Independent external validation has not been undertaken.

## References
1. S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112. First electronically published 2001-02-02. DOI: 10.1137/S003614450036757X. Open full text: https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download.
2. S. Blanes, A. Iserles, and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, ESAIM: M2AN 56 (2022), 1843–1870. DOI: 10.1051/m2an/2022042. Open full text: https://personales.upv.es/serblaza/2022_M2AN.pdf.
3. K. Masood and M. Yousuf, *Solution of the Initial Inverse Problems in the Heat Equation Using the Finite Difference Method with Positivity-Preserving Padé Schemes*, Numerical Heat Transfer Part A 57 (2010), 691–708. DOI: 10.1080/10407781003744763. Abstract available; complete text not inspected.
