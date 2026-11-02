# Flux-selected minimum-support states and equal-intensity resonance in a magnetic Lieb waveguide lattice

## Finding
For a uniform-flux nearest-neighbor Lieb waveguide lattice, the minimum number of occupied lattice sites of a nonzero finitely supported zero-eigenfrequency state is exactly \(4\) at zero flux, exactly \(6\) at half a flux quantum, and exactly \(7\) at any other flux. At generic flux all seven-site minimizers have the same two-adjacent-plaquette support topology, with six equal-modulus amplitudes and one amplitude whose modulus is \(|1+e^{i\phi}|\) times theirs. These modes have equal intensity on all seven sites precisely at \(\phi\equiv\pm2\pi/3\pmod{2\pi}\), where their inverse participation ratio is \(1/7\).

## Assumptions and scope
Take the infinite square graph with vertex set \(\mathbb Z^2\), and create one optical waveguide at every vertex and at the midpoint of every nearest-neighbor graph edge. Only a midpoint and its two incident vertices are coupled, with unit-magnitude hopping, no on-site potentials and no longer-range couplings. This defines a magnetic Lieb lattice. Write \(t=e^{i\phi}\) with \(|t|=1\), \(\phi\in\mathbb R\). A fixed gauge for the vertex--edge incidence operator \(B\) is: for each horizontal edge \((x,y)\to(x+1,y)\), its column has entries \(+1\) at \((x,y)\) and \(-1\) at \((x+1,y)\); for each vertical edge \((x,y)\to(x,y+1)\), its column has entries \(+1\) at \((x,y)\) and \(-t^x\) at \((x,y+1)\). Each elementary square has oriented holonomy \(t\), up to orientation conjugation. The Hermitian propagation Hamiltonian, acting on vertex and edge-midpoint amplitudes, is
\[
H=\begin{pmatrix}0&B\\B^\dagger&0\end{pmatrix}.
\]
Every statement concerns a nonzero exactly zero-eigenvalue state with finitely many nonzero amplitudes, on this **infinite** lattice. Support size counts occupied optical waveguides, not plaquettes or vertices of the underlying square graph.

For a nonzero state \(\psi\), write its inverse participation ratio as \(I(\psi)=\sum_j|\psi_j|^4/(\sum_j|\psi_j|^2)^2\). Claims of uniqueness are modulo translation and square-lattice symmetry, the required gauge equivalence when reflecting flux, and multiplication by a nonzero complex scalar. The flux \(t\) is fixed when assessing such equivalences.

## Proof
**1. All compact zero modes live on edge midpoints.** Write a zero mode as \((u,z)\), where \(u\) is supported on original square vertices and \(z\) on edge midpoints. The equations are \(Bz=0\) and \(B^\dagger u=0\). Each column equation of \(B^\dagger u=0\) relates its two incident values by a nonzero unit-phase factor. Because \(u\) has finite support on an infinite connected square graph, one vertex value vanishes; connectivity forces every vertex value to vanish. Thus \(u=0\).

**2. Support must contain cycles.** Associate to the nonzero edge amplitudes their occupied edges in the square graph. At each incident original vertex, the sum \(Bz\) vanishes. A vertex incident to exactly one occupied edge would have a nonzero single contribution, which is impossible; hence all occupied vertices have occupied degree at least two. Every finite occupied connected component therefore contains a cycle. A simple occupied cycle admits a nonzero solution of \(Bz=0\) if and only if its gain product equals one: solving successively around the cycle must return the initial amplitude. For a square-grid cycle encircling \(A\) unit faces, its gain is \(t^A\), up to inversion.

**3. Exact sharp support cutoffs.** The square grid has no cycles shorter than four. The only possible connected degree-at-least-two occupied subgraphs with at most six edges are simple cycles: a four-edge unit square or a six-edge perimeter of two edge-adjacent squares. Indeed, obtaining two independent square-grid cycles requires at least two four-sided bounded faces, and they share at most one edge, requiring at least seven occupied edges. The four-cycle consistency condition is \(t=1\); for the six-cycle it is \(t^2=1\). Hence four-edge modes occur exactly at \(t=1\), six-edge modes at \(t=-1\) (and also at \(t=1\), where they are not smallest), and no mode of at most six sites exists when \(t\ne\pm1\). For any flux the seven occupied edges of two edge-adjacent elementary plaquettes support an explicit solution below, completing sharpness in all cases.

**4. Explicit seven-edge state.** Use two horizontal unit squares \([0,1]\times[0,1]\) and \([1,2]\times[0,1]\). Denote horizontal-edge amplitudes by \(h_{x,y}\) and vertical-edge amplitudes by \(v_{x,0}\). Set
\[
(h_{0,0},h_{1,0},h_{0,1},h_{1,1})=(-t,1,t,-t^2),\qquad
(v_{0,0},v_{1,0},v_{2,0})=(t,-(1+t),1).
\]
The six vertex cancellation equations for this support, in the order bottom left/middle/right and top left/middle/right, reduce respectively to
\[
-t+t=0,\quad t+1-(1+t)=0,\quad -1+1=0,
\]
\[
t-t=0,\quad -t-t^2+t(1+t)=0,\quad t^2-t^2=0.
\]
For \(t\ne-1\) all seven amplitudes are nonzero. At \(t=-1\) the shared-middle-edge amplitude vanishes, leaving the six-edge perimeter. At \(t=1\) a four-edge one-square state is already available.

**5. Uniqueness of minimal support topology at generic flux.** Every seven-edge component with no occupied degree-one vertices and at least two independent cycles must realize equality in the elementary two-face planar square-grid edge bound. Thus its bounded faces are two unit squares sharing one edge, giving the same seven-edge theta graph as above. A seven-edge simple cycle cannot exist because the square grid is bipartite. Disconnected supports of total size seven are impossible at generic flux because each nonzero component would itself need at least seven edges. On the connected six-vertex, seven-edge theta, \(B\) has full row rank six when \(t\ne1\): a left-null vector would satisfy \(B^\dagger u=0\) and nontrivial holonomy around its four-cycle, forcing \(u=0\). Therefore its kernel is one-dimensional, and the displayed vector is the unique solution up to scalar.

**6. Uniform intensity and sharp participation bound.** Six displayed amplitudes have squared modulus one, while the remaining amplitude has squared modulus \(q=|1+t|^2=2+2\cos\phi\). Therefore
\[
I(\phi)=\frac{6+q^2}{(6+q)^2}=\frac{6+(2+2\cos\phi)^2}{(8+2\cos\phi)^2}.
\]
The seven-site Cauchy--Schwarz inequality gives \(I\ge1/7\), with equality precisely for seven equal intensities; alternatively \(\frac{dI}{dq}=12(q-1)/(6+q)^3\). Equality is equivalent to \(q=1\), or \(\cos\phi=-1/2\). Hence it occurs precisely when \(\phi\equiv\pm 2\pi/3\pmod{2\pi}\); these are generic, not exceptional, fluxes.

## Verification
The accompanying `checker.py` defines the incidence matrix directly from the stated gauge, evaluates the seven amplitudes, checks all six cancellations, compares the closed participation expression over \(399\) nontrivial phase samples, and compares minimum support within a \(3\)-by-\(2\)-plaquette finite patch for six representative phases. In that patch it examines \(41,225\) nonempty edge subsets of cardinality at most seven per phase, tests absence of degree-one occupied vertices and the elementary cycle holonomy condition, and confirms the \(4/6/7\) cutoff examples. The program reports \(1,225\) assertions passed. These finite checks are **not** the proof of the global minimality or topological classification: those are established in steps 1--6.

To reproduce: run `python3 checker.py` with Python 3.9 or newer; no external packages are needed.

## Relationship to prior work
Gouveia, Maceira and Dias (arXiv:1607.04326v1, 2016) establish the persistence of compact Lieb-lattice states at nonzero flux and state that their supports require at least two plaquettes. Their exhibited two-plaquette state uses a different geometry, and their examined text does not give the three sharp support sizes or the seven-site intensity-equalization flux. The present work does **not** claim the Lieb flat band, magnetic robustness, or the concept of two-plaquette localization as new.

Mukherjee et al. (arXiv:1412.6342, 2014) experimentally and theoretically study four-site zero-flux optical Lieb states; the examined text does not characterize minimal magnetic-flux support. Tanigawa (arXiv:1207.3601, 2012), building on earlier gain-graph matroid theory, gives a general dependence criterion in terms of balanced cycles and unbalanced theta graphs. That general theory *already explains the dependency mechanism underlying the support classification*, so the graph-circuit principle is not claimed as novel. The evaluated, all-flux Lieb-lattice cutoff and especially its exact, uniquely equal-intensity seven-site design are the claims compared for originality.

Niţă, Ostahie and Aldea (Phys. Rev. B 87, 125428, 2013) investigate magnetic Lieb-lattice spectra and edge modes. Only their abstract and bibliographic material were accessible for substantive comparison, not the complete original manuscript. The possibility of equivalent earlier formulas in that paper or broader flat-band optics literature remains a genuine historical-priority risk.

## Limitations
The gauge-fixed theorem assumes exactly equal-magnitude, nearest-neighbor bipartite hopping on an infinite uniform-flux lattice. It does not cover finite-boundary extra zero modes, onsite detuning, losses, longer-range hopping, nonlinear propagation, magnetic disorder, or experimental realizability of the phase gauge. The intensity statement concerns **all minimum-support seven-site modes** for generic flux only; larger-supported compact modes can have smaller inverse participation ratio and no global spatial-localization optimum is asserted. Priority has not been independently certified; one closely relevant 2013 full paper was inaccessible.

## References
1. J. D. Gouveia, I. A. Maceira and R. G. Dias, *Time evolution of localized states in Lieb lattices*, arXiv:1607.04326v1 (14 July 2016), https://arxiv.org/abs/1607.04326 and https://arxiv.org/html/1607.04326v1.
2. S. Mukherjee et al., *Observation of a localized flat-band state in a photonic Lieb lattice*, arXiv:1412.6342 (19 December 2014), https://arxiv.org/pdf/1412.6342.
3. S. Tanigawa, *Matroids of Gain Graphs in Applied Discrete Geometry*, arXiv:1207.3601 (2012), https://arxiv.org/pdf/1207.3601, especially section 4.1.
4. M. Niţă, B. Ostahie and A. Aldea, *Spectral and transport properties of the two-dimensional Lieb lattice*, Physical Review B 87, 125428 (2013), https://doi.org/10.1103/PhysRevB.87.125428 (abstract inspected only).
