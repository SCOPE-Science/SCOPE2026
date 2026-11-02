# Affine-code entanglement in nondegenerate quadratic Boolean Cayley graph states

## Finding

Let \(d=2m\ge4\), let \(V=\mathbb F_2^d\), and let \(Q:V\to\mathbb F_2\) be a quadratic form with \(Q(0)=0\) and nondegenerate alternating polar form
\[
\beta(x,y)=Q(x+y)+Q(x)+Q(y).
\]
On the \(2^d\) points of \(V\), join distinct vertices \(x,y\) exactly when \(Q(x+y)=1\). Prepare the pure qubit graph state of this simple graph. For any nonempty proper affine flat \(A=a+U\) with \(k=\dim U\), the reduced state on the \(2^k\) qubits indexed by \(A\) has exactly \(2^{r(A)}\) nonzero eigenvalues, all equal to \(2^{-r(A)}\), where
\[
\boxed{
 r(A)=\begin{cases}
 k+1,&0\le k\le d-2,\quad\beta|_{U\times U}=0,\\
 k+2,&0\le k\le d-2,\quad\beta|_{U\times U}\ne0,\\
 d,&k=d-1.
 \end{cases}}
\]
Consequently all positive-order Rényi entropies and the von Neumann entropy are \(r(A)\) bits. The remaining \(2^{2^k}-2^{r(A)}\) eigenvalues vanish. Every affine offset gives the same spectrum. For a fixed nondegenerate polar form, all quadratic refinements, including refinements of different Arf type, give identical spectra on each affine-flat cut.

In the same ambient dimension and affine-flat dimension, a totally isotropic and a nonisotropic direction subspace (when both exist) differ by precisely one ebit. The entanglement grows only linearly in \(d\), although the graph has exponentially many qubits.

## Assumptions and scope

The graph has one qubit at each vertex of \(V\) and an unweighted controlled-phase edge interaction. Its state is
\[
|G_Q\rangle=\prod_{\{x,y\}:Q(x+y)=1}\mathrm{CZ}_{xy}|+\rangle^{\otimes 2^d}.
\]
The product is over unordered pairs of distinct vertices. There are no loops because \(Q(0)=0\). The bipartition is exactly \(A=a+U\) versus \(V\setminus A\); here \(a\in V\), \(U\le V\), and \(0\le k=\dim U\le d-1\). All ranks and scalar products below are over \(\mathbb F_2\); entropy is measured in bits. No assertion is made for arbitrary, non-affine vertex sets.

## Proof

**1. Graph-state character sum.** Let \(M\) denote the rectangular binary cross-adjacency matrix of the cut, with rows indexed by \(x\in A\), columns indexed by \(z\in V\setminus A\), and entries \(M_{xz}=Q(x+z)\). Writing the graph-state amplitudes in the two computational bit bases and collecting phases on each side gives
\[
\rho_A(\xi,\xi')=2^{-|A|}(-1)^{\phi(\xi)+\phi(\xi')}
\mathbf1_{\{M^{\mathsf T}(\xi+\xi')=0\}}.
\]
Conjugating by the diagonal phase unitary removes \(\phi\). The kernel of \(M^{\mathsf T}\) has dimension \(|A|-r\), where \(r=\operatorname{rank}M\), so the remaining matrix is \(2^{-|A|}\) times the convolution matrix of this kernel. Its Fourier characters yield \(2^r\) equal positive eigenvalues \(2^{-r}\) and all other eigenvalues zero. It remains to calculate the binary rank of \(M\).

**2. Two elementary rank facts.** Because \(\beta\) is nondegenerate, each nonzero \(u\in V\) defines a nonconstant linear functional \(z\mapsto\beta(u,z)\). If \(k\le d-2\), the complement of \(A\) has \(2^d-2^k>2^{d-1}\) points. Since any proper affine hyperplane has exactly \(2^{d-1}\) points, that complement affinely spans \(V\). Consequently restricted affine-linear functions on the complement are uniquely determined by their global affine-linear functions.

For every affine-linear \(L:V\to\mathbb F_2\), the nondegenerate quadratic function \(Q+L\) has weight
\[
\#\{z:Q(z)+L(z)=1\}=2^{d-1}\pm2^{d/2-1}.
\]
Indeed, the squared Walsh sum \(W=\sum_z(-1)^{Q(z)+L(z)}\) equals
\[
W^2=\sum_{t,z}(-1)^{Q(z+t)+Q(z)+L(t)}
=\sum_t(-1)^{Q(t)+L(t)}\sum_z(-1)^{\beta(t,z)}=2^d,
\]
using nondegeneracy to eliminate all \(t\ne0\). Thus the minimum possible weight is \(2^{d-1}-2^{d/2-1}>2^{d-2}\) for \(d\ge4\).

**3. All flats of codimension at least two.** Index the rows by \(x=a+u\), \(u\in U\). The row corresponding to \(u=0\) is \(F(z)=Q(a+z)\). Subtracting it from the row at \(u\) gives the function
\[
D_u(z)=\beta(u,z)+Q(u)+\beta(u,a),\qquad z\notin A.
\]
The span of these differences modulo the constant function has dimension \(k\), by nondegeneracy of \(\beta\) and affine spanning of the complement. Also,
\[
D_u+D_v+D_{u+v}=\beta(u,v)\,\mathbf1.
\]
If \(U\) is totally isotropic, the map \(u\mapsto D_u\) is linear and its image has dimension \(k\), without the constant function. If \(U\) is not totally isotropic, the displayed identity supplies the constant function, so the difference-row span has dimension \(k+1\).

In either case \(F\) lies outside the affine-linear functions restricted to the complement. Otherwise, after an affine change of variables, a nondegenerate quadratic plus an affine-linear function would vanish outside \(A\), forcing its support to have at most \(2^k\le2^{d-2}\) points. This contradicts the preceding quadratic-weight bound. The full row span therefore has dimension \(k+1\) for isotropic \(U\), or \(k+2\) otherwise.

**4. Hyperplanes.** If \(k=d-1\), choose \(w\notin U\) and index the two sides as \(a+u\), \(a+w+v\) with \(u,v\in U\). Translation invariance gives
\[
M_{u,v}=Q(w+u+v).
\]
The row at \(u=0\) is \(F(v)=Q(w+v)\), whose quadratic polar is the restriction \(\beta|_U\). A hyperplane in a \(d\)-dimensional nondegenerate symplectic space has \(\dim\operatorname{rad}(\beta|_U)=1\), hence \(\operatorname{rank}(\beta|_U)=d-2\ge2\). Thus \(F\) is not affine-linear on \(U\).

The difference rows are \(D_u(v)=Q(u)+\beta(u,w)+\beta(u,v)\). Their linear parts span a space of dimension \(d-2\); the constant \(\mathbf1\) also belongs to their span because \(D_u+D_v+D_{u+v}=\beta(u,v)\mathbf1\) and the restricted form has a nonzero pairing. Therefore the difference-row span is exactly the \((d-1)\)-dimensional space of affine-linear functions on \(U\) generated by those linear parts and the constant. The non-affine row \(F\) contributes one further dimension. Hence \(\operatorname{rank}M=d\).

The three cases prove the asserted rank and, by Step 1, the full reduced-state spectrum.

**5. Two graph types with the same cut spectra.** In dimension four take
\[
Q_+(x)=x_1x_2+x_3x_4,\qquad Q_-(x)=Q_+(x)+x_1+x_2.
\]
These quadratic forms have the same nondegenerate polar form, but their Cayley graphs have degrees \(6\) and \(10\), respectively. Since graph degree is an isomorphism invariant, the graphs are nonisomorphic. Nevertheless every affine-flat cut has the same exact entanglement spectrum for both. In particular, affine two-plane cuts have entropy \(3\) bits for isotropic directions and \(4\) bits for nonisotropic directions; all affine-hyperplane cuts have entropy \(4\) bits.

## Verification

The accompanying standalone `verify_quadratic_cuts.py` uses exact binary row reduction on the cross-adjacency matrix and an independently implemented prediction from isotropy. Its recorded execution passed \(6336\) comparisons in ambient dimension four (exhaustive subspace directions and all offsets for sampled nondegenerate forms), \(2520\) sampled comparisons in dimension six, and \(96\) in dimension eight: \(8952\) exact rank comparisons in total. Eight direct reduced-density-matrix calculations for explicit sixteen-qubit states, spanning both quadratic types and several cut dimensions, agreed with the predicted spectra with maximum absolute eigenvalue error \(4.1633\times10^{-17}\).

Run `python verify_quadratic_cuts.py` with Python 3.9 or later and NumPy available. The finite checks corroborate the proof; they are not a proof of the universal quantifiers. The above rank argument proves the theorem for every even \(d\ge4\).

## Relationship to prior work

Hein, Eisert and Briegel gave the general graph-state cut-adjacency rank characterization. The present statement specializes their mechanism to a uniform all-dimension formula for nondegenerate quadratic Cayley graphs on every affine-flat vertex cut. Leopardi's account of bent-function Cayley graphs and the older Bernasconi–Codenotti connection establish the relevant strongly regular graph setting, not this quantum cut-spectrum formula. Brouwer and van Eijl studied whole-graph modular adjacency ranks of strongly regular graphs; a whole-graph rank does not determine arbitrary rectangular cut ranks. Grassl, Klappenecker and Rötteler studied connections between graphs, quadratic forms and quantum codes, but the inspected material did not give the affine-cut dichotomy. These observations are comparisons of examined statements, not claims of exhaustive historical priority.

## Limitations

Only pure, unit-weight qubit graph states, nondegenerate quadratic Boolean Cayley graphs of even ambient dimension at least four, and affine-flat-versus-complement cuts are covered. General vertex subsets, degenerate quadratic forms, weighted or composite-dimensional graph states, and noisy or thermal dynamics are outside the theorem. Prior specialized modular cross-rank results might imply part or all of the classification; independent literature assessment has not been performed.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multiparty entanglement in graph states*, arXiv:quant-ph/0307130 (public 18 July 2003), https://arxiv.org/abs/quant-ph/0307130.
2. P. Leopardi, *Classifying bent functions by their Cayley graphs*, arXiv:1705.04507 (2017), https://arxiv.org/abs/1705.04507.
3. A. E. Brouwer and C. A. van Eijl, *On the p-Rank of the Adjacency Matrices of Strongly Regular Graphs*, J. Algebraic Combinatorics **1** (1992), https://emis.muni.cz/journals/JACO/Volume1_4/q1ur742gt117v044.fulltext.pdf.
4. M. Grassl, A. Klappenecker and M. Rötteler, *Graphs, Quadratic Forms, and Quantum Codes*, https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/Graphs-Quadratic-Forms-and-Quantum-Codes.pdf.
5. A. Bernasconi and B. Codenotti, *Spectral Analysis of Boolean Functions as a Graph Eigenvalue Problem* (1999), https://arpi.unipi.it/handle/11568/167433 (abstract/metadata inspected; complete text not obtained).
