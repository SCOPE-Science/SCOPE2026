# Reversal eigenspaces of squared-path cut-complex homology

## Finding
For every integer \(k\ge2\) and \(n\ge k+3\), write \(r=n-k\) and \(K=\Delta_k(P_n^2)\), the **ordinary cut complex** of the square of the path. Path reversal \(\rho(i)=n+1-i\) acts simplicially on \(K\). Its reduced rational homology vanishes outside degree \(r-1\), and its complete \(\mathbb Q[C_2]\)-module is determined by the following formula.

Set \(a=\lfloor n/2\rfloor\), \(f=n-2a\), and
\[
H_{n,r}=[t^r](1+t)^{a+f-1}(1-t)^a,
\qquad
B(j,A)=\sum_{\ell=0}^{\min(j-1,A-j)}\binom{j-1}{\ell}.
\]
Take \(B(j,A)=0\) when \(j<1\) or \(A<j\). Define
\[
C_{n,k}=\begin{cases}
0,&n\ \text{even},\ k\ \text{odd},\\
B((k-1)/2,a)+B((k-1)/2,a-1),&n,k\ \text{odd},\\
B(k/2,a),&k\ \text{even}.
\end{cases}
\]
Then the trace of \(\rho\) on \(\widetilde H_{r-1}(K;\mathbb Q)\) is
\[
\boxed{\chi_{n,k}=H_{n,r}-(-1)^{\lfloor r/2\rfloor}C_{n,k}
+(-1)^{\lfloor(r-1)/2\rfloor}\mathbf1_{\{r\ \mathrm{odd}\}}.}
\]
With the **previously known** top Betti number
\[
\beta(k,n)=\binom{n-1}{k-1}
-\sum_{j=0}^{\min(k-1,r)}\binom{k-1}{j}(r-j+1)+r,
\]
the \(\rho\)-invariant and anti-invariant dimensions are **exactly**
\[
\boxed{\dim \widetilde H_{r-1}(K;\mathbb Q)^{\rho=\pm1}
=\frac{\beta(k,n)\pm\chi_{n,k}}2.}
\]
Examples are \((n,k)=(8,4)\), with \(\beta=11\), \(\chi=1\), multiplicities \((6,5)\); \((9,4)\), with \(\beta=25\), \(\chi=-1\), multiplicities \((12,13)\); and \((10,5)\), with \(\beta=67\), \(\chi=-5\), multiplicities \((31,36)\). This assertion concerns the full rational involution representation, **not** a new nonequivariant homology calculation.

## Assumptions and scope
The vertices of \(P_n^2\) are \(\{1,\ldots,n\}\), with an edge between distinct vertices at distance at most two in the ordinary path order. The facets of \(\Delta_k(P_n^2)\) are the complements in \([n]\) of disconnected induced \(k\)-vertex subsets. Only integers \(k\ge2\), \(n\ge k+3\), hence \(r\ge3\), are asserted. Homology representations use rational coefficients, and \(\rho\) acts on oriented simplicial chains via the induced vertex permutation, including orientation signs. The previously established shellability and Betti-number formula are used as cited input.

## Proof
**1. The complete list of omitted faces.** A \(k\)-subset \(T=\{t_1<\cdots<t_k\}\subset[n]\) induces a connected subgraph of \(P_n^2\) if and only if consecutive gaps satisfy \(t_{j+1}-t_j\le2\). Indeed, a gap of three or more separates the induced graph, whereas gaps of one or two connect the ordered selected vertices. The complementary-face classification proved by Zhang and Yang says that, relative to the full \((r-1)\)-skeleton \(S\) of the \((n-1)\)-simplex, \(K\) lacks *precisely* two sets of faces: in cardinality \(r\), complements of connected \(k\)-subsets; and in cardinality \(r-1\), complements of the \(r\) intervals of \(k+1\) consecutive vertices. Every face of cardinality at most \(r-2\) is present. The two omitted layers do not overlap in cardinality and there are no other omissions.

**2. Rational equivariant Euler identity.** Write \(V_0=\mathbb Q^n/\langle(1,\ldots,1)\rangle\). The unique reduced homology group of the full skeleton \(S\) is \(\bigwedge^rV_0\) in degree \(r-1\). The reversal permutation has \(a\) eigenvalues \(-1\) and \(a+f-1\) eigenvalues \(+1\) on \(V_0\); hence its trace on this exterior power is \(H_{n,r}\). The established shellability result says that \(\widetilde H_i(K;\mathbb Q)=0\) for \(i\ne r-1\). Take the reduced, \(\rho\)-equivariant Euler characteristic of the *actual augmented chain complexes* of \(K\) and \(S\). Subtracting a missing \(r\)-element face subtracts its oriented-chain trace in degree \(r-1\). Subtracting a missing \((r-1)\)-element face adds its oriented-chain trace in degree \(r-1\), because it lies in degree \(r-2\). A face of \(p\) vertices invariant under reversal has oriented-chain sign \((-1)^{\lfloor p/2\rfloor}\): reversal acts on its sorted vertices by \(\lfloor p/2\rfloor\) transpositions. Only invariant faces contribute to a permutation trace. Therefore
\[
\chi_{n,k}=H_{n,r}
-(-1)^{\lfloor r/2\rfloor}\,C_{n,k}
+(-1)^{\lfloor(r-1)/2\rfloor}\,I_{n,k},
\]
where \(C_{n,k}\) counts reversal-invariant connected \(k\)-subsets and \(I_{n,k}\) counts reversal-invariant intervals of length \(k+1\). Exactly one interval is centered when \(n-(k+1)=r-1\) is even, and none otherwise. Thus \(I_{n,k}=\mathbf1_{\{r\ \mathrm{odd}\}}\).

**3. Enumerating the symmetric connected subsets.** A symmetric subset pairs its sites about the center, with a possible central site if \(n\) is odd. If \(n\) is even and \(k\) is odd, symmetry is impossible. For even \(k=2j\), there are \(j\) chosen sites in the left half. Connectivity across the center forces the rightmost such site to be site \(a\), whether the path length is even or odd. Read the remaining sites backward: the \(j-1\) gaps are each one or two; selecting exactly \(\ell\) gaps of size two gives leftmost site \(a-(j-1)-\ell\ge1\). This gives \(B(j,a)\). For odd \(n\) and odd \(k=2j+1\), the central site is selected, and connectivity forces the rightmost chosen left site to be \(a\) or \(a-1\); counting the permitted preceding gaps gives \(B(j,a)+B(j,a-1)\). All cases exhaust the possible parities.

**4. Identifying the full module.** Over \(\mathbb Q\), an involution has only the simple characters \(+1\) and \(-1\). The known top Betti number gives the total dimension \(\beta\); the independently computed trace gives the difference of multiplicities. Solving these two linear equations proves the displayed pair of eigenspace dimensions. This also proves integral nonnegativity of the expressions, without relying on a numerical test. The proof applies simultaneously to every pair in the stated infinite range.

## Verification
The standalone dependency-free script `verify_squared_path_reversal.py` enumerates ordinary cut-complex faces **independently from disconnected induced subsets**, rather than generating faces from the cited missing-face formula. It computes signed reversal traces of oriented faces and compares them with the new symbolic formula for every \(5\le n\le13\) and \(2\le k\le n-3\) (45 pairs); it separately enumerates centered connected subsets. For all 21 cases with \(n\le10\), exact binary Gaussian elimination of every boundary matrix reconstructs reduced mod-two homology and compares ranks with the prior formula. The recorded output `verification_output.txt` reports all checks passing. Finite experiments are checks only: all-parameter validity rests on Steps 1–4.

## Relationship to prior work
Zhang and Yang, *Betti Numbers of Cut Complexes of Squared Paths and a Recurrence Conjecture* (first available May 21, 2026), established the full complementary-face profile, the nonequivariant Betti formula and a recurrence; the present proof uses those facts and extracts the **previously unreported involution representation**, including both eigenspace dimensions. Bayer, Denker, Jelić Milutinović, Sundaram and Xue's *Topology of Cut Complexes II* (2024 preprint; later publication) proved shellability of squared-path cut complexes. It also investigates symmetry representations for other cut-complex families, including ordinary paths, but not the squared-path reversal character determined here. Their foundational *Topology of Cut Complexes of Graphs* develops general graph-cut-complex machinery. A result limited to ranks or to path powers with different edge sets does not imply the new eigenspace splitting without the centered connected-subset count and signed face correction. Candidate-specific literature and research-index searches did not identify a published equivalent; this is not a proof of global novelty.

## Limitations
The nonequivariant top Betti number, shellability and missing-face characterization are imported from the cited primary literature and not rediscovered here. The new claim covers only the path-reversal subgroup \(C_2\), rational homology representations, and the indicated \(n,k\) range; it makes no assertion of a new integral equivariant decomposition, of a new homotopy type, or of analogous formulas for higher path powers. The literature comparison cannot exclude unindexed or independently derived equivalent statements; in particular general equivariant Euler-character methods are known, though the explicit squared-path character formula was not found in the inspected sources. The included finite checks do not constitute an infinite proof.

## References
1. Y. Zhang and Y. Yang, *Betti Numbers of Cut Complexes of Squared Paths and a Recurrence Conjecture*, arXiv:2605.22808 (first public version May 21, 2026), https://arxiv.org/abs/2605.22808. Used: §§2–3 and the layerwise face characterization.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public version July 11, 2024), https://arxiv.org/abs/2407.08158. Used: squared-path shellability and comparison with other equivariant cut-complex results.
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, https://arxiv.org/abs/2304.13675. Background definitions and scope.
