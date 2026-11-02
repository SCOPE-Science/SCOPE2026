# Induced-matching vacancies and an isolated Curie response in the spin-one icosahedral antiferromagnet

## Finding
Consider the twelve-vertex icosahedral graph \(I\) and classical spins \(s_v\in\{-1,0,+1\}\). For \(J>0\), \(D\in\mathbb R\), and zero external field, the homogeneous antiferromagnetic spin-one Blume–Capel Hamiltonian is
\[
H(s)=J\sum_{\{u,v\}\in E(I)}s_us_v+D\sum_{v\in V(I)}s_v^2.
\]
With \(r=D/J\), its exact ground energy is
\[
\frac{E_0}{J}=\begin{cases}-10+12r,&r\le 1/2,\\-8+8r,&1/2\le r\le1,\\0,&r\ge1.\end{cases}
\]
The numbers of labeled spin configurations attaining the minimum in the successive regimes \(r<1/2\), \(r=1/2\), \(1/2<r<1\), \(r=1\), \(r>1\) are **72, 462, 150, 351, 1**, respectively. These are exact finite-cluster level crossings, not thermodynamic-limit phase transitions.

More structurally, in the open interval \(1/2<r<1\) every ground state has precisely eight occupied (nonzero) vertices. Its four vacant vertices induce **exactly two disjoint edges** (an induced \(2K_2\)) in \(I\). Conversely, each of the exactly **75** such four-vertex vacancy sets supports **exactly two** ground-state sign patterns, related by global inversion. Hence this phase has \(75\cdot2=150\) states, and the vacancy geometry is a complete characterization, not just a sufficient construction.

Let \(M=\sum_v s_v\). At \(r=1/2\), the \(462\) states split by the number \(m=\sum_v s_v^2\) of occupied vertices into \(72\) at \(m=12\), \(240\) at \(m=10\), and \(150\) at \(m=8\), all having \(M=0\). For the \(m=10\) sector, the vacancies form one of the \(30\) edges and there are eight allowed sign patterns per edge. At \(r=1\), the \(351\) states consist of the empty state, \(80\) states with \((m,M)=(6,0)\), \(60\) each with \((m,M)=(7,\pm1)\), and \(150\) with \((m,M)=(8,0)\).

For an infinitesimal uniform magnetic field coupled by \(-hM\), take the derivative at \(h=0\) before the zero-temperature limit. With \(k_B=1\), the equilibrium susceptibility \(\chi=\partial\langle M\rangle/\partial h\) obeys
\[
\lim_{\beta\to\infty}\frac{\chi(\beta)}{\beta}=\begin{cases}40/117,&D=J,\\0,&D\ne J.\end{cases}
\]
The nonzero response is isolated at the vacancy-collapse degeneracy: only the \(120\) seven-occupied critical states have \(|M|=1\), while all other ground states have zero magnetization.

## Assumptions and scope
The graph is the simple icosahedral vertex-edge graph, with \(12\) vertices, \(30\) edges, degree \(5\), and \(20\) triangular faces. The three spin values are discrete classical scalars, not quantum spin-one operators. Couplings are uniform, \(J>0\), and the occupancy penalty \(D\) can be any real number. All counts are labeled (vertex-distinct) configurations; configurations related by symmetries and by spin reversal are counted separately. No pair interactions beyond the graph edges are present.

A fully explicit labeling is used in the proof and checker: vertices \(0\) and \(11\) are opposite poles; \(1,\ldots,5\) and \(6,\ldots,10\) are two cyclic pentagonal belts. For each \(i=0,\ldots,4\), use edges from \(0\) to \(1+i\), from \(11\) to \(6+i\), the cyclic links on each belt, and links \(1+i\) to both \(6+i\) and \(6+((i-1)\bmod5)\). This uniquely specifies the \(30\) edges and requires no software graph library.

## Proof
Write \(m=\sum_v s_v^2\) and \(b=\sum_{\{u,v\}\in E(I)}s_us_v\), so \(H/J=b+rm\). Let \(A\) be the occupied set, \(P\) its positive-spin subset and \(N=A\setminus P\) its negative-spin subset. If \(e(U)\) is the number of graph edges induced by vertex set \(U\), then the exact identity
\[
b=2\bigl(e(P)+e(N)\bigr)-e(A)
\]
follows by distinguishing equal-sign bonds from opposite-sign bonds. Enumerating the \(2^{12}\) sets \(A\) and the \(2^{|A|}\) choices of \(P\) examines each of the \(3^{12}=531441\) physical spin assignments exactly once. Counting induced edges by integer bit masks gives the following complete minimum-bond certificate; the third column counts all assignments with that occupancy attaining the indicated minimum:

| \(m\) | \(\min b\) | Multiplicity |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 0 | 24 |
| 2 | -1 | 60 |
| 3 | -2 | 120 |
| 4 | -3 | 300 |
| 5 | -4 | 480 |
| 6 | -6 | 80 |
| 7 | -7 | 120 |
| 8 | -8 | 150 |
| 9 | -8 | 960 |
| 10 | -9 | 240 |
| 11 | -9 | 600 |
| 12 | -10 | 72 |

This certificate immediately gives two sharp inequalities, valid for **every** ternary spin assignment:
\[
b+\frac12m\ge-4,\qquad b+m\ge0.
\]
For \(r\le1/2\), because \(0\le m\le12\),
\[
b+rm=(b+m/2)+(r-1/2)m\ge-4+12(r-1/2)=-10+12r.
\]
For \(1/2\le r\le1\), using nonnegative interpolation weights,
\[
b+rm=2(1-r)(b+m/2)+(2r-1)(b+m)\ge-8+8r.
\]
For \(r\ge1\), \(b+rm=(b+m)+(r-1)m\ge0\). At the open-interval equality cases, the certificate respectively forces \((m,b)=(12,-10)\), \((8,-8)\), or \((0,0)\). At the two boundary values, its listed equality sectors give the claimed degeneracies and magnetizations. Thus every stated phase and boundary is globally exact for all real \(D\).

The same exhaustive integer certificate verifies the geometric strengthening: the \(150\) states with \((m,b)=(8,-8)\) have \(75\) distinct vacancy sets, each admitting exactly two minimizing sign assignments. Their vacancy sets are **exactly** the \(75\) four-element sets on which the induced graph is \(2K_2\). This is checked in both directions by enumerating all \({12\choose4}=495\) vacancy sets. Similarly, at \((m,b)=(10,-9)\), the \(30\) vacancy sets are precisely graph edges and each supports eight sign patterns. The checker includes these finite combinatorial conclusions as assertions rather than extrapolating from examples.

Finally, in finite volume at zero field, the limiting Gibbs state is the uniform mixture over the minimizing configurations. Because global spin reversal makes \(\langle M\rangle=0\), the fluctuation-dissipation identity gives \(\chi/\beta=\langle M^2\rangle\). The preceding magnetization counts make this exactly \(120/351=40/117\) at \(r=1\) and zero elsewhere.

## Verification
Run `python3 check_icosahedron.py` with Python 3.10 or later. It uses only standard-library modules, constructs the explicit graph, and performs two independently organized complete integer enumerations: direct ternary spin products, and occupied/positive-set bit masks using induced-edge counts. Both cover \(531441\) assignments; their occupancy minima and multiplicities must agree exactly. The script also verifies both sharp inequalities configuration by configuration, the critical magnetization sectors, the induced-\(2K_2\) vacancy characterization, the adjacent-vacancy characterization at the first threshold, and the exact Curie fraction. A successful run prints four `PASS` lines and raises an error on any failed assertion.

## Relationship to prior work
The 2005 icosahedral Heisenberg study [1] establishes a physically relevant twelve-vertex frustrated geometry for **quantum Heisenberg** spins, not the three-valued classical occupation-penalized Hamiltonian here. The 2013 triangular-lattice Blume–Capel work [2] analyzes spin-one occupancy physics using a periodic triangular lattice and Monte Carlo, rather than the finite icosahedral graph or this induced-matching ground-state classification. The 2015 regular Ising polyhedra study [3] establishes magnetic-field plateaux for **two-valued Ising** spins, which accounts for the fully occupied \(72\)-state limit but has no vacant-spin degrees of freedom. The 2020 exact-enumeration study [4] considers only a three-spin triangle and a seven-spin pair of corner-sharing tetrahedra, not the icosahedron. None of these results, in the material examined, supplies the \(75\)-template phase or the isolated \(40/117\) zero-temperature Curie coefficient.

The icosahedron cannot be properly vertex-three-colored: the five neighbors of any fixed vertex form a five-cycle, which cannot be colored by the two colors remaining after coloring that vertex. This geometric obstruction motivates finding the precise vacancies that release triangular frustration. Prior results for spin-one systems on line graphs of properly three-edge-colorable cubic graphs do not apply to this five-regular graph, and pure \(\pm1\) models cannot recover the occupancy transitions. These distinctions concern mathematical implication, not merely title or terminology.

## Limitations
This is an exact statement for one finite graph, not an assertion of a bulk phase transition. Its computational certificate is a **complete finite exhaustive proof** because the physical state space has exactly \(3^{12}\) elements; it is not an extrapolation to arbitrary graphs or to continuous spins. Finite-temperature susceptibility away from the scaled low-temperature limit, nonzero magnetic fields, nonuniform bonds, exchange anisotropy, quantum dynamics, and thermodynamic scaling are unproved. The cited 2015 Ising-polyhedra full text was not accessible for complete inspection; its abstract and accessible descriptions specify two-valued spins, but historical-priority review of all older literature remains a residual limitation. Historical priority has not been independently established.

## References
1. N. P. Konstantinidis, *The Antiferromagnetic Heisenberg Model on Clusters with Icosahedral Symmetry*, arXiv:cond-mat/0503658 (first public 2005-03-29), https://arxiv.org/abs/cond-mat/0503658 .
2. M. Žukovič and A. Bobák, *Magnetocaloric properties of a frustrated Blume-Capel antiferromagnet*, arXiv:1309.3593 (first public 2013-09-13), https://arxiv.org/abs/1309.3593 .
3. J. Strečka, K. Karľová, and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449 (first public 2015-02-16), https://arxiv.org/abs/1502.04449 .
4. M. Mohylna and M. Žukovič, *Effect of Single-Ion Anisotropy on Magnetocaloric Properties of Frustrated Spin-s Ising Nanoclusters*, arXiv:2010.16287 (first public 2020-10-30), https://arxiv.org/abs/2010.16287 .
