# Two-adic perfect capture and exact dark-state weights on a quantum figure-eight

## Finding

Let \(G_{m,n}\) be the simple *figure-eight* graph made by identifying the vertex labelled \(0\) of a cycle of length \(m\ge3\) and the vertex labelled \(0\) of a cycle of length \(n\ge3\), with no other identifications. Label the nonjunction vertices of the first cycle \(1,\ldots,m-1\) in cyclic order, and those of the second cycle \(1,\ldots,n-1\) separately. Set \(d=\gcd(m,n)\) and
\[
\epsilon=\mathbf1_{\{m/d\ \mathrm{odd},\ n/d\ \mathrm{odd}\}}=\mathbf1_{\{v_2(m)=v_2(n)\}}.
\]
For adjacency-matrix hopping with a positive-rate irreversible sink at the common vertex, the subspace of wavefunctions permanently invisible to the sink has exact dimension
\[
\boxed{\dim\mathcal D=\left\lfloor\frac{m-1}{2}\right\rfloor+\left\lfloor\frac{n-1}{2}\right\rfloor+\epsilon\left\lfloor\frac d2\right\rfloor.}
\]
The exact probability of *never being absorbed* in the infinite-time limit from first-cycle vertex \(x\in\{1,\ldots,m-1\}\) is
\[
\boxed{S_{m\mid n}(x)=\frac12\mathbf1_{\{m\text{ odd or }x\ne m/2\}}+\frac{2\epsilon}{m+n}\,R_d(x),\qquad R_d(x)=\sum_{\substack{1\le q<d\\q\text{ odd}}}\sin^2\!\left(\frac{\pi qx}{d}\right).}
\]
For the second cycle exchange \(m\) and \(n\). If \(d=1\), the sum is empty. For \(d\ge2\), it has the closed form
\[
R_d(x)=\begin{cases}0,&d\mid x,\\d/2,&d\text{ even and }x\equiv d/2\pmod d,\\d/4,&\text{otherwise}.\end{cases}
\]
Thus a nonjunction vertex is absorbed with probability **one** precisely when it is the opposite vertex \(x=m/2\) on an even first cycle and \(v_2(m)\ne v_2(n)\) (or the analogous condition on the second cycle). A walker at the junction is absorbed with probability one. In particular the first-cycle antipode survives with probability \(0\) for cycle lengths \((m,n)=(4,6)\), but with probability \(1/2\) for \((4,4)\). For two equal-length cycles, a nonjunction non-antipodal site has survival \(3/4\); an even-cycle antipode has survival \(1/2\). The total absorbed fraction of a maximally mixed initial state is \(1-\dim\mathcal D/(m+n-1)\).

## Assumptions and scope

The Hilbert space has one orthonormal state per vertex. Let \(A\) be the unweighted simple-graph adjacency matrix, \(h\in\mathbb R\setminus\{0\}\) the homogeneous hopping amplitude, \(\kappa>0\) the absorber rate, and \(P_0=|0\rangle\langle0|\). The surviving no-jump amplitude from a unit vector \(|\psi\rangle\) evolves under
\[
K=hA-\frac{i\kappa}{2}P_0,\qquad |\psi_t\rangle=e^{-itK}|\psi\rangle.
\]
The survival probability is \(\lim_{t\to\infty}\|\psi_t\|^2\), and the absorption probability is one minus that number. Equivalently, this is the unabsorbed sector of a Markovian one-way sink \(\sqrt\kappa\,|\mathrm{sink}\rangle\langle0|\). There is no added dephasing, site potential, magnetic flux, or other loss. The oriented index \(x\) on a cycle is not necessarily the graph's shortest-path distance from the junction.

## Proof

**1. Sink-invisible spectral subspace.** Let
\[
\mathcal D=\bigoplus_{\lambda\in\sigma(A)}\{u:Au=\lambda u,\ u(0)=0\}.
\]
It is an orthogonal, reducing subspace for both \(A\) and \(P_0\), and \(K|_{\mathcal D}=hA|_{\mathcal D}\). On its orthogonal complement, every eigenvalue \(z\) of \(K\) has strictly negative imaginary part: for an eigenvector \(u\),
\[
\operatorname{Im}z=-\frac\kappa2\frac{|u(0)|^2}{\|u\|^2}\le0.
\]
Equality implies \(u(0)=0\) and \(Au=(z/h)u\), contradicting orthogonality to \(\mathcal D\). Since the bright subspace is finite dimensional, its time propagator decays to zero (possible Jordan factors are harmless). Therefore for every initial state, the eventual survival is exactly its squared orthogonal projection onto \(\mathcal D\). This also proves rate independence and includes degenerate adjacency eigenvalues.

**2. Dirichlet modes and the junction equation.** Delete the common vertex. The remaining graph is the disjoint union of paths with \(m-1\) and \(n-1\) vertices. The normalized Dirichlet modes on the first path are
\[
\phi_{m,k}(x)=\sqrt{\frac2m}\sin\!\left(\frac{\pi kx}{m}\right),\quad 1\le k<m,
\]
with eigenvalue \(2\cos(\pi k/m)\), and similarly for the second path. The sum of endpoint amplitudes entering the junction is
\[
c_{m,k}=\phi_{m,k}(1)+\phi_{m,k}(m-1)=\sqrt{\frac2m}\sin\!\left(\frac{\pi k}{m}\right)[1+(-1)^{k+1}].
\]
The same formula holds with \(n\). Thus every even-index mode is automatically dark and every odd-index mode has nonzero junction coupling. Distinct indices within the same path have distinct eigenvalues. A common eigenvalue across both paths requires \(k/m=\ell/n\) because cosine is strictly decreasing on \((0,\pi)\). Consequently
\[
k=(m/d)q,\quad \ell=(n/d)q,\quad 1\le q<d.
\]
The junction is a single scalar constraint \(c_{m,k}\alpha+c_{n,\ell}\beta=0\). At a common energy, any even-index modes are already among the individual dark modes. There is **one additional** mixed dark mode if and only if both indices are odd, i.e. \(m/d\) and \(n/d\) are odd and \(q\) is odd. Counting these gives the displayed dimension formula. The two quotients \(m/d,n/d\) are coprime, and both odd precisely when the original lengths have equal 2-adic valuations.

**3. Exact site projector.** The span of even-index Dirichlet modes on one path is the \(-1\) eigenspace of reflection \(x\mapsto m-x\). Its projector has diagonal entry \(1/2\) at every vertex except an even cycle's antipode \(x=m/2\), which is fixed by reflection and has entry \(0\). For a mixed mode corresponding to odd \(q\), the two nonzero junction couplings are
\[
c_{m,k}=2\sqrt{2/m}\sin(\pi q/d),\quad c_{n,\ell}=2\sqrt{2/n}\sin(\pi q/d).
\]
The normalized dark combination is proportional to \(c_{n,\ell}\phi_{m,k}-c_{m,k}\phi_{n,\ell}\). The squared fraction of its norm on the first path equals
\[
\frac{c_{n,\ell}^{2}}{c_{m,k}^{2}+c_{n,\ell}^{2}}=\frac{m}{m+n}.
\]
Its probability weight at first-cycle vertex \(x\) is therefore \(2\sin^2(\pi qx/d)/(m+n)\). Modes from distinct \(q\) have distinct eigenvalues, and these mixed odd modes are orthogonal to the even-index modes. Summing their diagonal projectors proves the exact survival formula.

**4. Trigonometric and perfect-capture consequences.** Write \(\sin^2 y=(1-\cos 2y)/2\) and sum the odd-index roots of unity. If \(d\) is odd the sum is \(0\) when \(d\mid x\) and \(d/4\) otherwise; if \(d\) is even it is \(0\), \(d/2\), or \(d/4\) according as \(x\equiv0\), \(d/2\), or neither modulo \(d\). Because both summands in the survival formula are nonnegative, zero survival from a nonjunction site requires an even-cycle antipode and zero mixed contribution. At \(x=m/2\), if \(\epsilon=1\) then \(d\) is even and \(m/d\) odd, giving \(x\equiv d/2\pmod d\) and mixed survival \(d/(m+n)>0\). When \(\epsilon=0\), the mixed contribution vanishes. The criterion follows. The maximally mixed assertion follows by taking the trace of the dark projector, whose rank is the dimension above.

## Verification

Execute `python verify.py` with the dependencies in `requirements.txt` from the same directory. The checker constructs the actual unweighted figure-eight adjacency matrices, independently extracts the dark projector through dense Hermitian eigenspaces and their overlap with the junction, compares its diagonal weights and rank with the formulas on a grid of distinct cycle sizes, and evaluates selected finite-time non-Hermitian propagators. Numerical checks are corroboration; the proof above establishes every integer pair and all admissible physical parameters.

## Relationship to prior work

Krovi and Brun, *Quantum walks with infinite hitting times* (first public arXiv version 10 June 2006), establish the general role of invariant subspaces and symmetries in quantum-walk detection. Varbanov, Krovi and Brun (2008) develop a Poisson-measurement hitting-time framework, including graph examples; their Hamiltonian uses the graph Laplacian and their measurement scheme differs from the continuous sink used here. Caruso and collaborators (2009) describe interference-protected trapping in exciton networks and solve fully connected examples. Pemberton-Ross, Kay and Schirmer (2010) characterize dark-state accessibility in spin networks. Those general principles are prior knowledge, not part of the originality claim here. The contribution assessed here is the explicit all-length adjacency-figure-eight arithmetic projection, exact sitewise surviving weights, and the two-adic necessary-and-sufficient condition for perfect absorption at an antipodal vertex. No blanket uniqueness claim follows from a literature search.

## Limitations

The two cycles are simple, have homogeneous edge hopping, and meet at exactly one vertex carrying a single irreversible sink. Moving the detector, changing edge weights or fluxes, adding dephasing, or taking a metric (continuum-edge) quantum graph changes the boundary equations and is not covered. The result determines infinite-time absorption fractions, not finite-time relaxation rates or absorption-time moments. Independent publication-priority assessment has not been performed.

## References

1. H. Krovi and T. A. Brun, *Quantum walks with infinite hitting times*, arXiv:quant-ph/0606094 (first submitted 10 June 2006), Phys. Rev. A **74**, 042334 (2006).
2. M. Varbanov, H. Krovi, and T. A. Brun, *Hitting time for the continuous quantum walk*, arXiv:0803.3446 (24 March 2008), Phys. Rev. A **78**, 022324 (2008).
3. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, and M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454 (28 January 2009), J. Chem. Phys. **131**, 105106 (2009).
4. P. J. Pemberton-Ross, A. Kay, and S. G. Schirmer, *Quantum control theory for state transformations: Dark states and their enlightenment*, arXiv:1003.4290 (22 March 2010), Phys. Rev. A **82**, 042322 (2010).
