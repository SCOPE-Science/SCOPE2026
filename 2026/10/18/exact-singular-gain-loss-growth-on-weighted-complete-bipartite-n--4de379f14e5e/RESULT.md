# Exact singular gain–loss growth on weighted complete bipartite networks

## Finding

Fix integers \(a\ge3\) and \(b\ge1\), and put \(c=a-2\). Divide the vertices of \(K_{a,b}\) into a part \(A\) with two distinguished vertices \(u,v\) and \(c\) otherwise equivalent vertices, and a part \(B\) with \(b\) vertices. Give every edge from \(u\) or \(v\) to \(B\) hopping weight \(1\), and every edge from the other \(A\)-vertices to \(B\) weight \(\eta\ge0\). Put balanced imaginary on-site potentials \(+i\gamma\) and \(-i\gamma\) at \(u\) and \(v\), respectively, where \(\gamma\ge0\). Let \(H\) be the resulting complex symmetric hopping Hamiltonian.

For \(\gamma>0\) and \(\eta>0\), set
\[
A_0=b(2+c\eta^2)-\gamma^2,\qquad C_0=\gamma^2bc\eta^2,\qquad \Delta=\sqrt{A_0^2+4C_0}.
\]
The complete spectrum consists of \(a+b-4\) zero modes together with four simple nonzero eigenvalues
\[
\pm\omega,\quad\pm i\mu,\qquad
\omega=\sqrt{\frac{\Delta+A_0}{2}},\quad
\mu=\sqrt{\frac{\Delta-A_0}{2}}>0.
\]
The zero eigenvalues are semisimple, the matrix is diagonalizable, and its propagator has exact exponential growth exponent
\[
\lim_{t\to\infty}\frac1t\log\|e^{-itH}\|_2=\mu,
\qquad \|e^{-itH}\|_2=\Theta(e^{\mu t}).
\]
Thus any strictly positive coupling to the additional passive vertices destroys the entire-real-spectrum interval of the isolated gain–loss trimer, however weak the gain–loss potential.

The quantitative singular onset is different below and at the isolated trimer's exceptional point:
\[
\mu=\gamma\sqrt{\frac{bc}{2b-\gamma^2}}\,\eta+O(\eta^3)
\quad (0<\gamma<\sqrt{2b},\ \eta\downarrow0),
\]
\[
\mu=\sqrt b\,(2c)^{1/4}\sqrt\eta\,[1+O(\eta)]
\quad(\gamma=\sqrt{2b},\ \eta\downarrow0).
\]
Their joint transition has an exact crossover: for any fixed real \(\kappa\), if \(\gamma(\eta)^2=2b+\kappa\eta\), then
\[
\lim_{\eta\downarrow0}\frac{\mu(\gamma(\eta),\eta)}{\sqrt\eta}
=\sqrt{\frac{\sqrt{\kappa^2+8b^2c}+\kappa}{2}}.
\]
At \(\eta=0\) the spectrum is real and the propagator is uniformly bounded when \(0\le\gamma<\sqrt{2b}\); at \(\gamma=\sqrt{2b}\) there is one Jordan block of size three at zero, yielding \(\Theta(t^2)\) propagator growth; beyond it the growth exponent is \(\sqrt{\gamma^2-2b}\). The isolated trimer threshold and ordinary third-order exceptional point are established background; the claimed contribution is the exact all-size passive-coupling instability and its singular quantitative crossover.

## Assumptions and scope

All parameters and all graph sizes are finite. The matrix entries between opposite parts are symmetric real hopping weights. No edges connect vertices within a part. The time convention is \(\psi(t)=e^{-itH}\psi(0)\), and \(\|\cdot\|_2\) is the Euclidean operator norm. At \(\eta=0\), the weighted network becomes a trimer plus isolated vertices. The \(\gamma>0,\eta>0\) spectral formula and its zero-mode count require \(a\ge3\), \(b\ge1\), and \(c=a-2\ge1\). In this setting the interchange \(u\leftrightarrow v\), followed by conjugation, is a parity–time symmetry.

## Proof

**Invariant decomposition.** Let \(e_-=(e_u-e_v)/\sqrt2\) and \(e_+=(e_u+e_v)/\sqrt2\). Let \(e_C\) be the normalized sum of the \(c\) passive vertices in \(A\), and \(e_B\) the normalized sum of the \(b\) vertices in \(B\). In the ordered orthonormal basis \((e_-,e_+,e_C,e_B)\), the invariant active block is
\[
H_{\mathrm{act}}=
\begin{pmatrix}
0&i\gamma&0&0\\
i\gamma&0&0&\sqrt{2b}\\
0&0&0&\eta\sqrt{bc}\\
0&\sqrt{2b}&\eta\sqrt{bc}&0
\end{pmatrix}.
\]
The orthogonal complements of \(e_C\) in the passive-vertex subspace and \(e_B\) in the \(B\)-subspace are pointwise annihilated by \(H\). Their total dimension is \((c-1)+(b-1)=a+b-4\). No other matrix entries couple to these complements, giving an exact direct sum, rather than a mere characteristic-polynomial identity.

**Characteristic polynomial and spectral growth.** A direct determinant expansion gives
\[
\det(zI_4-H_{\mathrm{act}})=
 z^4+[\gamma^2-b(2+c\eta^2)]z^2-\gamma^2bc\eta^2.
\]
For positive \(\eta,\gamma\), the constant coefficient is strictly negative. The two roots of the quadratic in \(z^2\) therefore have opposite signs and are nonzero. Writing them \(\omega^2\) and \(-\mu^2\) gives the displayed explicit formulas. The four roots are distinct. The invariant dark subspace and active invertibility show that the entire matrix is diagonalizable with exactly the indicated semisimple zeros. A diagonalization bounds its propagator above by a constant times \(e^{\mu t}\). An eigenvector for \(+i\mu\) gives the matching lower bound \(e^{\mu t}\). This also proves the logarithmic growth limit.

**Decoupled boundary and Jordan order.** Setting \(\eta=0\) makes \(e_C\) another zero mode. The remaining trimer on \((e_-,e_+,e_B)\) has characteristic polynomial \(z(z^2+\gamma^2-2b)\). For \(\gamma<\sqrt{2b}\), its three eigenvalues are distinct, and all other modes are stationary. At equality, the trimer has characteristic polynomial \(z^3\), is not the zero matrix, and has nonzero square: for instance, the \((e_-,e_B)\)-entry of its square is \(i\gamma\sqrt{2b}\). Cayley–Hamilton gives its cube zero. Hence its only Jordan block has size three, and its exponential contains a nonzero quadratic term \(-t^2H_{\mathrm{trim}}^2/2\), proving \(\Theta(t^2)\). Above the threshold its imaginary eigenvalues have magnitudes \(\sqrt{\gamma^2-2b}\).

**Asymptotic crossover.** Denote \(x=\mu^2\). The negative \(z^2\)-root satisfies
\[
x^2+A_0x-C_0=0,
\qquad x=\frac{\sqrt{A_0^2+4C_0}-A_0}{2}.
\]
For fixed \(0<\gamma<\sqrt{2b}\), \(A_0=2b-\gamma^2+bc\eta^2\) has a positive limit and \(C_0=\gamma^2bc\eta^2\); the positive root is analytic in \(\eta^2\), with leading term \(C_0/(2b-\gamma^2)\). Taking its positive square root yields the first expansion, including the \(O(\eta^3)\) remainder. At \(\gamma^2=2b\), \(A_0=bc\eta^2\) and \(C_0=2b^2c\eta^2\). Hence \(x/\eta\to\sqrt2 b\sqrt c\) and \(\mu/\sqrt\eta\to\sqrt b(2c)^{1/4}\), with a relative \(O(\eta)\) expansion. Finally substitute \(\gamma^2=2b+\kappa\eta\), divide the radical expression for \(x\) by \(\eta\), and take \(\eta\downarrow0\); the stated positive crossover follows for every fixed \(\kappa\in\mathbb R\).

## Verification

Run `python verify.py` with dependencies in `requirements.txt`. The verification recomputes the active-block determinant symbolically, checks its decoupled specialization, compares full-graph eigenvalues against the predicted growth rate over \(720\) parameter tuples, checks \(21\) small-coupling limits, and checks \(3\) critical trimer Jordan-block propagators. These tests were run successfully on the included code. They are finite corroborations; the all-size and asymptotic statements rest on the proof above.

## Relationship to prior work

Duanmu, Li, Horne, Kevrekidis, and Whitaker (2012, arXiv:1210.3871) treat linear and nonlinear parity–time-symmetric dimers and trimers, including the conventional finite-gain trimer transition. Ge and Stone (2014, arXiv:1402.0428) explain that symmetry-coupled degeneracies can yield thresholdless parity–time breaking; the *qualitative phenomenon* of thresholdless breaking is therefore not claimed as novel. Teimourpour and colleagues (2014, arXiv:1408.1561) study hidden symmetries and higher-order exceptional points in finite photonic arrays. Moreno-Rodríguez and colleagues (2022, arXiv:2212.13642) study a different bipartite gain/loss distribution, with gain and loss on entire opposite parts, and give a different four-site spectrum. Teimourpour, Özdemir, and El-Ganainy (2017, DOI:10.1209/0295-5075/119/34003) investigate passive-dimer bridges between gain and loss sites and reverse transitions near exceptional points; the available first-page preview and figures depict passive-bridge arrays, not the star-shaped four-mode block here. That highly relevant paper could not be checked beyond the supplied preview and remains a specific originality risk.

The present specific graph has just one balanced pair in the **same** bipartition, plus an arbitrary number of identically weak passive pathways. Its exact all-size quartic, growth exponent, and singular \(\eta\)-dependent crossover were not established in the inspected passages of those works. That limited comparison is not proof of global novelty; a more general spectral perturbation theorem or earlier network calculation could imply the exact expressions.

## Limitations

The result concerns linear, finite-dimensional, complex-symmetric tight-binding Hamiltonians, uniform couplings within each of three vertex classes, and exactly one balanced gain–loss pair. It does not cover disorder, nonlinear optics, general graph weights, scattering boundary conditions, or the simultaneous limit of growing graph size and vanishing coupling. At \(\gamma=0\) the Hamiltonian is Hermitian, so the positive-growth statements do not apply. The effective four-mode reduction is highly symmetric; generic perturbations could change its exact polynomial. Only mathematical self-review has been performed, not independent scientific validation.

## References

1. M. Duanmu, K. Li, R. L. Horne, P. G. Kevrekidis, N. Whitaker, *Linear and Nonlinear PT-symmetric Oligomers: A Dynamical Systems Analysis*, arXiv:1210.3871 (first posted 2012-10-15), https://arxiv.org/abs/1210.3871 .
2. L. Ge and A. D. Stone, *Parity-Time Symmetry Breaking beyond One Dimension: The Role of Degeneracy*, arXiv:1402.0428 (first posted 2014-02-03), https://arxiv.org/abs/1402.0428 .
3. M. H. Teimourpour et al., *Light transport in PT-invariant photonic structures with hidden symmetries*, arXiv:1408.1561 (first posted 2014-08-07), https://arxiv.org/abs/1408.1561 .
4. M. H. Teimourpour, Ş. K. Özdemir, R. El-Ganainy, *Reverse PT phase transition across exceptional points of any order*, EPL 119 (2017) 34003, DOI:10.1209/0295-5075/119/34003 .
5. L. A. Moreno-Rodríguez, C. T. Martínez-Martínez, J. A. Méndez-Bermúdez, H. Benisty, *Stability mapping of bipartite tight-binding graphs with losses and gain: PT-symmetry and beyond*, arXiv:2212.13642 (first posted 2022-12-27), https://arxiv.org/abs/2212.13642 .
