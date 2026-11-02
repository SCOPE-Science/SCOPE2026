# Exact graph-Laplacian spectral support from binary ecological Turing-instability probes

## Finding
Fix the two-species reaction kinetics specified below, at their positive homogeneous equilibrium. For a finite connected undirected graph \(G\), let \(\mathcal I_G(d_1,d_2)\) be one if the linearization at that equilibrium has an eigenvalue with positive real part, and zero otherwise, for positive diffusion rates \(d_1,d_2\). Then for any two such graphs \(G,H\), potentially of different orders,
\[
\mathcal I_G(d_1,d_2)=\mathcal I_H(d_1,d_2)\quad\text{for all }d_1,d_2>0
\]
holds **if and only if** the sets of their distinct strictly positive combinatorial Laplacian eigenvalues agree (multiplicity is not recoverable from this yes/no response). Every prescribed positive wavenumber can be isolated in an arbitrarily narrow open instability band by suitable positive diffusion rates. Moreover, six vertices is the least order at which two connected regular graphs of the same degree can be separated in *both directions* by changing only the two diffusion rates: the triangular prism and \(K_{3,3}\), each cubic, exhibit explicitly verified reversed stability verdicts.

## Assumptions and scope
The ecological network follows the local reactions from Ye and Zhou's 2023 hyperbolic-mortality predator–prey model, with undirected combinatorial-Laplacian diffusion:
\[
\dot u_i=f(u_i,v_i)-d_1(Q_Gu)_i,\qquad
\dot v_i=g(u_i,v_i)-d_2(Q_Gv)_i,
\]
\[
f(u,v)=\alpha\left(\frac{u^2(1-u)}{u+A}-\frac{uv}{1+\beta u}\right),\qquad
g(u,v)=\frac{\beta uv}{1+\beta u}-\frac{\gamma v^2}{e+\eta v}.
\]
Here \(G\) is any finite connected simple undirected graph with at least two vertices, \(Q_G=\operatorname{diag}(\deg G)-\operatorname{Adj}(G)\), and \(d_1,d_2>0\). Fix \(\alpha=2/3\), \(A=1/50\), \(\beta=6\), \(\gamma=\eta=1/2\), and \(e=1\). The homogeneous coexistence equilibrium is \((u_*,v_*)=(1/10,6/5)\), and its reaction Jacobian is
\[
J=\begin{pmatrix}31/144&-1/24\\45/16&-15/64\end{pmatrix},\quad
\operatorname{tr}J=-11/576<0,\quad \Delta=\det J=205/3072>0.
\]
The theorem refers to **strict linear instability of the homogeneous equilibrium**, not to existence, stability, or amplitude of a patterned nonlinear attractor. A zero eigenvalue at a band endpoint counts as no *strict* linear instability.

## Proof
**1. Exact linear modal criterion.** By differentiating the displayed reactions at \((u_*,v_*)\), we obtain the stated rational Jacobian (the standalone exact-rational checker independently verifies its four entries and stationarity). Write \(a=31/144>0\), \(b=-1/24<0\), \(c=45/16>0\), \(d=-15/64<0\). The graph Laplacian is real symmetric and has a nonnegative spectrum containing zero. Along an eigenmode with eigenvalue \(q\ge0\), the two-by-two linearization is \(J-q\operatorname{diag}(d_1,d_2)\), with trace \(\operatorname{tr}J-(d_1+d_2)q<0\) and determinant
\[
P(q)=\Delta-(ad_2+dd_1)q+d_1d_2q^2.
\]
A real two-by-two matrix with strictly negative trace has an eigenvalue with positive real part exactly when its determinant is negative. Therefore \(\mathcal I_G(d_1,d_2)=1\) exactly when \(P(q)<0\) at at least one Laplacian eigenvalue of \(G\); \(q=0\) is always stable because \(P(0)=\Delta>0\).

**2. An arbitrarily narrow instability window centered on an arbitrary target.** This step also works for any two-by-two reaction Jacobian with \(a>0\), \(d<0\), \(bc<0\), \(\operatorname{tr}J<0\), and \(\Delta>0\). Set \(r=d_2/d_1\), \(h(r)=ar+d\), and
\[
r_c=\left(\frac{\sqrt\Delta+\sqrt{-bc}}a\right)^2>0.
\]
For \(r>r_c\), choose a desired \(q_0>0\) and prescribe
\[
d_1=\frac{h(r)}{2rq_0},\qquad d_2=rd_1.
\]
These rates are positive because \(r>r_c>-d/a\). Completing the square yields
\[
P(q)=d_1d_2\bigl((q-q_0)^2-q_0^2\varepsilon(r)^2\bigr),\qquad
\varepsilon(r)=\sqrt{1-\frac{4r\Delta}{h(r)^2}}.
\]
The defining equation for \(r_c\) makes \(h(r_c)=2\sqrt{r_c\Delta}\); thus \(\varepsilon(r)>0\) for \(r>r_c\) and \(\varepsilon(r)\to0\) as \(r\downarrow r_c\). Consequently the entire continuous unstable band is exactly \((q_0(1-\varepsilon),q_0(1+\varepsilon))\), whose width tends to zero. This is an explicit mode-selective diffusion construction, not an appeal to a continuous-wavenumber approximation.

**3. Inverse equivalence.** If \(G\) and \(H\) have equal sets of positive Laplacian eigenvalues, the criterion in part 1 gives equal binary signatures for every pair of positive rates. Conversely, if some positive Laplacian eigenvalue \(q_0\) belongs to \(G\) but not to \(H\), the latter's finite spectrum has positive distance from \(q_0\). Apply part 2 with \(\varepsilon\) sufficiently small that the resulting open band contains \(q_0\) but no eigenvalue of \(H\). Then \(\mathcal I_G=1\) and \(\mathcal I_H=0\). Interchange the graphs if the set difference is reversed. This proves both directions. Multiplicities are absent from this criterion and therefore cannot be determined by it.

**4. Sharp regular-graph witness.** The six-vertex triangular prism \(K_3\square K_2\) and the complete bipartite graph \(K_{3,3}\) are both connected and three-regular. Their exact Laplacian spectra, including multiplicity, are respectively
\[
\{0,2,3,3,5,5\},\qquad \{0,3,3,3,3,6\}.
\]
For \((d_1,d_2)=(1/20,9/20)\), the polynomial satisfies
\[
P(2)=-1043/76800<0,\quad P(3)=1057/76800>0,\quad
P(5)=625/3072>0,\quad P(6)=28093/76800>0.
\]
Hence the prism is linearly unstable, but \(K_{3,3}\) is Hurwitz stable in every mode. Reversing the outcome, for \((d_1,d_2)=(1/60,261/2000)\),
\[
P(2)=51949/1920000>0,\quad P(3)=26389/1920000>0,\quad
P(5)=13/76800>0,\quad P(6)=-179/1920000<0.
\]
Now the prism is Hurwitz stable and \(K_{3,3}\) is unstable. In both cases \(P(0)=205/3072>0\) and every modal trace is negative. All fractions are exact.

For each order up to five, every admissible connected simple regular graph of a fixed degree is unique up to isomorphism (degrees one and maximal give \(K_2\) and complete graphs, degree two gives the cycle, and the remaining choices fail parity or connectivity). At order six, connected cubic graphs correspond under complementation to two-regular graphs that are either \(C_6\) or \(C_3\sqcup C_3\); their complements are respectively the triangular prism and \(K_{3,3}\). Thus order six is the first possible equal-order, equal-degree separation, and the displayed two choices give separation in both directions.

## Verification
Run `python3 verify.py` with Python 3 standard library. It checks the exact biological equilibrium and Jacobian, computes the six-by-six graph Laplacian characteristic polynomials independently from power traces and Newton identities, and verifies every displayed rational mode determinant, modal trace, and both opposite verdicts. This is finite verification of the concrete witness. The arbitrary-graph and arbitrary-wavenumber statements rely on the exact algebraic proof above, not on finite enumeration.

## Relationship to prior work
Ye and Zhou (2023, arXiv:2306.11818v1) supply the source predator–prey kinetics and standard network Turing dispersion criterion, with an emphasis on network degree and pattern formation. Mimar and collaborators (2019, arXiv:1903.03845) study how network topology and Laplacian spectral support mediate the presence or absence of Turing modes. These results make the modal criterion known; **that criterion alone is not claimed as new here**. The added statement is the exact inverse equivalence for the entire *binary two-diffusivity response function*, together with a constructive arbitrarily-narrow spectral selector and a sharp bidirectional equal-degree graph-order witness. Hütt, Armbruster, and Lesne's *Predictable topological sensitivity of Turing patterns on graphs* (2022, DOI:10.1103/PhysRevE.105.014304) is another relevant work; its abstract was accessible, but the full text was not available for complete comparison. The available evidence does not establish that the inverse characterization or sharp witness is previously proved; undiscovered equivalent formulations remain possible.

## Limitations
This statement detects *distinct positive Laplacian eigenvalues* but cannot infer their multiplicities, graph isomorphism, topology uniquely, or nonlinear pattern stability. The exact six-node example is specific to one admissible positive-parameter predator–prey equilibrium; no quantitative robustness to noisy observations is asserted. The inverse direction assumes freedom to vary both positive diffusion rates over a continuum and to query strict linear instability. A fully independent literature audit has not been performed.

## References
- Yong Ye and Jiaying Zhou, *Pattern formation in a predator-prey model with Allee effect and hyperbolic mortality on networked and non-networked environments* (2023), arXiv:2306.11818v1, https://arxiv.org/abs/2306.11818 .
- Sayat Mimar et al., *Turing patterns mediated by network topology in homogeneous active systems* (2019), arXiv:1903.03845, https://arxiv.org/abs/1903.03845 .
- Alexander Hütt, Dieter Armbruster and Annick Lesne, *Predictable topological sensitivity of Turing patterns on graphs* (2022), https://doi.org/10.1103/PhysRevE.105.014304 .
