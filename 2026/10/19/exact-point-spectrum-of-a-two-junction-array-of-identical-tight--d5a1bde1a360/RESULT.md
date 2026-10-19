# Exact point spectrum of a two-junction array of identical tight-binding wires

## Finding

Fix integers \(M\geq2\) and \(L\geq2\). Take \(M\) disjoint copies of the integer lattice \(\mathbb Z\), identify their respective vertices \(0\) into one vertex \(u\), and identify their respective vertices \(L\) into a second vertex \(v\); keep all other vertices distinct. Let \(H\) be the positive unit-hopping adjacency operator on this infinite simple graph.

**Complete classification.** The essential spectrum is \([-2,2]\). Every eigenvalue inside this band is
\[
E_k=2\cos\left(\frac{k\pi}{L}\right),\qquad k=1,\ldots,L-1,
\]
and each has multiplicity exactly \(M-1\). All such eigenvectors have finite support, confined to the \(M\) paths between the two junctions. There are no eigenvalues at the band edges.

For \(E>2\), write \(\kappa=\operatorname{arcosh}(E/2)\) and \(q=e^{-\kappa}\). Define the two real scalar functions
\[
F_s(E)=E-M\left(q+\frac{\sinh((L-1)\kappa)+s\sinh\kappa}{\sinh(L\kappa)}\right),\qquad s\in\{-1,+1\}.
\]
The equation \(F_{+1}(E)=0\) has exactly one root \(E_+>2\) for every admissible \(M,L\). The equation \(F_{-1}(E)=0\) has exactly one root \(E_->2\) except when \((M,L)=(2,2)\), in which case it has none. Whenever both roots exist, \(2<E_-<E_+\). Each root is a simple eigenvalue. Bipartite symmetry supplies their negative partners. Thus the entire point spectrum consists of the above embedded modes and exactly one pair \(\{\pm E_+\}\) if \((M,L)=(2,2)\), or exactly two pairs \(\{\pm E_+,\pm E_-\}\) otherwise.

At the exceptional pair \((M,L)=(2,2)\), the missing odd-junction channel instead produces a bounded, non-square-summable threshold solution at each of \(E=2\) and \(E=-2\). For fixed \(M\) and increasing \(L\), the two positive bound energies converge to the single-junction value
\[
\lim_{L\to\infty}E_\pm=\frac{2M}{\sqrt{2M-1}},
\]
with \(E_+\) strictly above that value and \(E_-\) strictly below it whenever the latter exists.

## Assumptions and scope

The Hilbert space is \(\ell^2(V)\), where the vertex set is
\[
V=\{u,v\}\ \cup\ \{(m,j):1\leq m\leq M,\ j\in\mathbb Z\setminus\{0,L\}\}.
\]
The edges connect consecutive integer labels within each copy; every occurrence of label \(0\) means the single shared vertex \(u\), and every occurrence of label \(L\) means the single shared vertex \(v\). All hopping matrix elements are \(+1\), all on-site terms are zero, and no other edges are present. The condition \(L\geq2\) prevents multiple edges directly between the junctions. The operator is bounded and self-adjoint because every vertex has degree at most \(2M\). This is a discrete adjacency Hamiltonian, not the differential Laplacian on a metric quantum graph.

## Proof

**1. Essential band.** Delete the finitely many edges incident to the two junctions. The remaining operator is the direct sum of \(2M\) standard half-line adjacency operators, \(M\) finite open paths of length \(L-1\), and two isolated junction vertices. The deleted-edge perturbation has finite rank. The half-lines have essential spectrum \([-2,2]\); Weyl's theorem yields \(\sigma_{\mathrm{ess}}(H)=[-2,2]\).

**2. Every embedded eigenvector is compact.** At an energy \(E\in[-2,2]\), a solution on an infinite exterior ray satisfies \(E\psi_j=\psi_{j-1}+\psi_{j+1}\). For \(|E|<2\), its nonzero solutions are oscillatory and not square-summable; at \(E=\pm2\), its nonzero solutions are affine sequences times an alternating sign and again not square-summable. Hence an \(\ell^2\) eigenvector vanishes on all exterior rays. The equations at the first exterior sites then force its two junction amplitudes to vanish.

**3. Dirichlet spectrum and multiplicity.** With both junction amplitudes zero, each of the \(M\) finite interior paths obeys the same open-chain Dirichlet eigenvalue equation. Its simple eigenvalues are precisely \(E_k=2\cos(k\pi/L)\), \(1\leq k<L\). At energy \(E_k\), the amplitude on the \(m\)-th interior path is \(c_m\sin(k\pi j/L)\) for \(1\leq j<L\). The two junction equations require
\[
\sum_{m=1}^M c_m\sin(k\pi/L)=0,\quad
\sum_{m=1}^M c_m\sin(k\pi(L-1)/L)=0.
\]
Since \(\sin(k\pi/L)\ne0\) and \(\sin(k\pi(L-1)/L)=(-1)^{k+1}\sin(k\pi/L)\), these are the single condition \(\sum_m c_m=0\). Its dimension is \(M-1\). No band-edge eigenvalue is possible because no interior Dirichlet eigenvalue equals \(\pm2\). This proves the complete embedded point-spectrum assertion, not merely existence of examples.

**4. Out-of-band secular equations.** Fix \(E>2\) and define \(\kappa\) and \(q\) as above. If the junction amplitudes are \(U,V\), square summability uniquely forces exterior amplitudes \(Uq^{-j}\) on the left rays \(j<0\) and \(Vq^{j-L}\) on the right rays \(j>L\). The same recurrence forces, on every interior path,
\[
\psi(m,j)=\frac{U\sinh((L-j)\kappa)+V\sinh(j\kappa)}{\sinh(L\kappa)}\qquad(1\leq j<L).
\]
Substitute these expressions into the two junction equations. With \(a=\sinh((L-1)\kappa)/\sinh(L\kappa)\) and \(b=\sinh\kappa/\sinh(L\kappa)>0\), they become
\[
\begin{pmatrix}E-M(q+a)&-Mb\\-Mb&E-M(q+a)\end{pmatrix}
\begin{pmatrix}U\\V\end{pmatrix}=0.
\]
The symmetric and antisymmetric vectors \((U,V)=(1,s)\) give precisely \(F_s(E)=0\). Conversely, a zero of either scalar function yields an exponentially decaying nonzero \(\ell^2\) eigenvector through the displayed formulas; its eigenspace is one-dimensional because \(b>0\).

**5. Monotonicity, root count, and threshold.** Let \(K\) denote the disconnected operator on all non-junction vertices and let \(B\) couple those vertices to the two junctions. For \(E>2\), its self-energy is \(\Sigma(E)=B^*(E-K)^{-1}B\). Differentiating the resolvent gives
\[
\frac{d}{dE}(EI_2-\Sigma(E))
=I_2+B^*(E-K)^{-2}B\succeq I_2.
\]
Consequently both fixed-parity eigenvalues \(F_s(E)\) are strictly increasing. Their band-edge limits are
\[
F_{+1}(2^+)=2-2M<0,\qquad
F_{-1}(2^+)=2-2M\left(1-\frac1L\right)\leq0.
\]
The second inequality is equality among admissible integers only for \((M,L)=(2,2)\). Moreover \(F_s(E)\to+\infty\) as \(E\to+\infty\), and \(F_{+1}(E)<F_{-1}(E)\) since \(b>0\). The intermediate value theorem, strict monotonicity, and the equal-endpoint exception give exactly the stated positive root count and ordering. At the exceptional endpoint the odd channel has \(U=-V\), constant (not square-summable) exterior-ray amplitudes and a linear interior interpolation; this is a genuine bounded generalized solution, not an eigenvector.

Finally, the graph is bipartite, so multiplication by \(+1\) on one bipartition and \(-1\) on the other conjugates \(H\) to \(-H\). This proves the negative spectrum claims. For fixed \(E>2\) as \(L\to\infty\), \(a\to q\) and \(b\to0\), uniformly on compact subsets of \((2,\infty)\). Both scalar equations converge to \(E=2Mq\), whose unique solution is \(2M/\sqrt{2M-1}\). The identities
\[
a-q=-\frac{q^{2L-1}(1-q^2)}{1-q^{2L}},\qquad
b=\frac{q^{L-1}(1-q^2)}{1-q^{2L}}
\]
imply \(a-q+b>0\) and \(a-q-b<0\), which locate the positive finite-separation roots strictly on opposite sides of the single-junction energy. The monotone-root argument also supplies their convergence.

## Verification

Run \(\texttt{python3 verify.py}\) with Python, NumPy, and SciPy. The standalone script constructs truncated adjacency matrices independently of the secular formulas, verifies exact compact-mode residuals, compares the predicted exterior eigenvalues to sparse matrix eigenvalues on length-\(80\) exterior rays, and stress-tests the monotonicity equations. Its execution completed successfully with **182 checks**. These numerical truncations support the algebra but are not used as an infinite-volume proof; the exhaustive spectral classification rests on the arguments above.

## Relationship to prior work

He and Ganesh [1] solve localization at a *single* kinetic junction formed by intersecting tight-binding wires, obtaining the associated exterior-band bound energy. Röntgen and collaborators [2] establish the general mechanism of compact localized states through local symmetries in discrete networks. Wang and collaborators [3] study symmetry-induced bound states in the continuum for a distinct *metric Helmholtz* network with leads. These results make individual ingredients of the present analysis familiar, rather than novel by themselves. The present contribution is the complete discrete two-junction infinite-wire spectral classification: all embedded eigenvalues and their exact multiplicities, all exterior bound pairs, and the exceptional finite-separation band-edge resonance, in one family with no on-site potentials.

Exner [5, Sec. 7.5.1] also treats a loop with two leads and embedded modes in a continuous metric graph; that related two-junction mechanism is established prior art, but the Hamiltonian is an edgewise second derivative and does not provide the present discrete exterior bound-pair threshold. Pinto, Molina and Orellana [4] study BICs in continuous-wave crossbar-junction arrays. Their accessible abstract addresses different waveguide differential equations and geometry but is relevant enough that a full-text comparison remains a priority risk; the complete article was not available for this check. No novelty claim is made for BICs, local-symmetry protection, or the existence of a bound state at a single junction in general.

## Limitations

This theorem requires exactly identical positive unit hopping strengths, simultaneous identification at two lattice labels, infinite rays on both sides, and no on-site or magnetic terms. It is not a theorem for irregular bond weights, metric/Kirchhoff quantum graphs, larger networks of junctions, or nonlinear interactions. The spectral theorem is mathematical; finite experiments do not establish it. Prior-art equivalence in general graph spectral theory cannot be completely excluded by the sources inspected, and an independently conducted mathematical priority review has not been performed.

## References

[1] E. He and R. Ganesh, *Bound states without potentials: localization at singularities*, arXiv:2302.03065 (first public version 6 February 2023), https://arxiv.org/abs/2302.03065.

[2] M. Röntgen, C. V. Morfonios, I. Brouzos, F. K. Diakonos and P. Schmelcher, *Quantum network transfer and storage with compact localized states induced by local symmetries*, arXiv:1811.02950 (2018), https://arxiv.org/abs/1811.02950.

[3] C. Wang, U. Kuhl, J. P. Dowling, H. Schanz and T. Kottos, *Bound states in the continuum induced via local symmetries in complex structures*, arXiv:2310.09682 (2023), https://arxiv.org/abs/2310.09682.

[4] S. Pinto, R. A. Molina and P. A. Orellana, *Bound states in the continuum in asymmetric crossbar junctions in one-dimensional waveguides*, Phys. Rev. A **110**, 013501 (2024), https://doi.org/10.1103/PhysRevA.110.013501.

[5] P. Exner, *Solvable models of resonances and decays*, arXiv:1205.0512 (2012), Sec. 7.5.1, https://arxiv.org/abs/1205.0512.
