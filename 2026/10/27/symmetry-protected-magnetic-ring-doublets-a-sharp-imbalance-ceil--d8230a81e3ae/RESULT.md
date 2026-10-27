# Symmetry-protected magnetic-ring doublets, a sharp imbalance ceiling, and conical splitting

## Finding
Consider a one-dimensional quantum ring of circumference \(2\pi\), pierced by a magnetic flux with phase \(\theta\), with two repulsive point interactions at antipodal positions \(0\) and \(\pi\). Their derivative-jump strengths are \(\alpha,\beta>0\). Let \(E\) denote eigenenergy in units where the kinetic operator is \(-d^2/dx^2\).

**Exact half-flux spectrum and sharp bound.** At half flux \(\theta=\pi\), the entire spectrum, counting multiplicity, is the union of the two sequences \(E_n(\alpha)=k_n(\alpha)^2\) and \(E_n(\beta)=k_n(\beta)^2\), indexed by every integer \(n\ge0\), where \(k_n(q)\) is the unique root of
\[
2k\cot(\pi k)=-q,\qquad n+\tfrac12<k<n+1.
\]
For each \(n\), if \(\alpha\ne\beta\), the two levels are simple and have a strictly positive energy splitting obeying the **uniform, sharp ceiling**
\[
0<|E_n(\alpha)-E_n(\beta)|<\frac{|\alpha-\beta|}{\pi},
\qquad
\lim_{n\to\infty}|E_n(\alpha)-E_n(\beta)|=\frac{|\alpha-\beta|}{\pi}.
\]
When \(\alpha=\beta=q\), every eigenenergy \(E_n(q)\) has multiplicity exactly two at half flux.

**Conical opening under two independent imperfections.** Fix \(g>0\) and an integer \(n\ge0\). Put \(\alpha=g+d\), \(\beta=g-d\) with \(|d|<g\) and \(\theta=\pi+\varepsilon\). Let \(k_n=k_n(g)\) and
\[
D_n=2\pi k_n+\frac{g}{k_n}+\frac{\pi g^2}{2k_n}>0.
\]
The two eigenenergies emanating from the double level \(k_n^2\), in increasing order, obey as \(\rho=\sqrt{d^2+\varepsilon^2}\to0\),
\[
E_{n,+}-E_{n,-}
=\frac{4k_n}{D_n}\sqrt{d^2+\left(k_n^2+\frac{g^2}{4}\right)\varepsilon^2}
+O_{g,n}(\rho^2).
\]
The leading expression is strictly positive in every nonzero direction in the two-parameter plane; its two axes give the exact first-order sensitivities to barrier imbalance and flux detuning. For fixed \(g\), these sensitivities tend respectively to \(2/\pi\) and \(2k_n/\pi\) as \(n\to\infty\).

## Assumptions and scope
The operator is the self-adjoint realization of the one-dimensional free Schrödinger operator on a ring, with continuity of the wave function at each point interaction and derivative jumps \(u'(x_j+)-u'(x_j-)=q_j u(x_j)\), with \(x_j\in\{0,\pi\}\). In the zero-vector-potential gauge, the magnetic field is encoded by the quasi-periodic monodromy multiplier \(e^{i\theta}\); \(\theta\) is defined modulo \(2\pi\). Equivalently, use periodic form domain \(H^1(S^1)\), kinetic form \(\int_0^{2\pi}|(-i\partial_x-\theta/(2\pi))u|^2dx\), and point terms \(\alpha|u(0)|^2+\beta|u(\pi)|^2\). All point strengths are strictly positive. No claim is made about finite-width barriers, electron-electron interactions, many-body persistent currents, or barriers not placed antipodally. The conical remainder is local at each fixed \(g,n\), not uniform in growing \(n\).

## Proof
**1. Exact transfer relation.** Across a free arc of length \(\pi\), a state column \((u,u')^T\) propagates by
\[
P(k)=\begin{pmatrix}\cos(\pi k)&\sin(\pi k)/k\\-k\sin(\pi k)&\cos(\pi k)\end{pmatrix},
\]
and across a repulsive delta of strength \(q\) by \(J(q)=\begin{pmatrix}1&0\\q&1\end{pmatrix}\). Both have determinant one. The monodromy is \(T(k)=J(\beta)P(k)J(\alpha)P(k)\). A quasi-periodic eigenstate of phase \(\theta\) exists exactly when \(\operatorname{tr}T(k)/2=\cos\theta\), because \(\det T=1\). Multiplication gives the exact secular equation
\[
\cos\theta=\cos(2\pi k)+\frac{\alpha+\beta}{2k}\sin(2\pi k)
+\frac{\alpha\beta}{2k^2}\sin^2(\pi k).
\tag{1}
\]
The operator is strictly positive, so all eigenvalues have \(k>0\). At half flux no integer \(k\) satisfies (1): its right side would be \(1\), not \(-1\).

**2. Factorization, classification, and multiplicity.** Write \(g=(\alpha+\beta)/2\), \(d=(\alpha-\beta)/2\), and \(R(k)=2k\cot(\pi k)\). Using \(\sin(\pi k)\ne0\), equation (1) is equivalent to the exact identity
\[
\bigl(R(k)+g\bigr)^2=d^2+
\left(\frac{2k\cos(\theta/2)}{\sin(\pi k)}\right)^2.
\tag{2}
\]
At \(\theta=\pi\), (2) factors into \((R(k)+\alpha)(R(k)+\beta)=0\). On every interval \((n+1/2,n+1)\), \(R(k)\) decreases strictly from \(0\) to \(-\infty\), since
\[
R'(k)=\frac{\sin(2\pi k)-2\pi k}{\sin^2(\pi k)}<0
\quad(k>0,\ \sin\pi k\ne0).
\]
It is positive on \((n,n+1/2)\). Therefore every strictly positive barrier gives exactly one root in each displayed half-interval and no others. For \(\alpha\ne\beta\) the two roots in each half-interval are distinct, and the secular zeros are simple, implying simple eigenvalues. For \(\alpha=\beta=q\), at a common root the one-arc transfer matrix \(A=J(q)P(k)\) has trace \(2\cos(\pi k)+q\sin(\pi k)/k=0\) and determinant one. Cayley--Hamilton yields \(A^2=-I\); hence \(T=-I\), so **every** initial state obeys half-flux monodromy and the eigenvalue has geometric multiplicity two.

**3. Uniform upper bound and sharpness.** Differentiate \(R(k_n(q))=-q\) with respect to \(q>0\):
\[
\frac{dE_n(q)}{dq}=\frac{2k_n(q)}{D_n(q)},\quad
D_n(q)=2\pi k_n(q)+\frac q{k_n(q)}+\frac{\pi q^2}{2k_n(q)}.
\tag{3}
\]
In particular, \(0<dE_n/dq<1/\pi\). Integrating (3) from the smaller to the larger coupling proves the strict level-splitting inequality. For \(n\to\infty\) with \(q\) in any fixed compact positive interval, \(k_n(q)\in(n+1/2,n+1)\) and (3) tends to \(1/\pi\) uniformly. Integrating again proves the sharp limiting value. These are exact inequalities for every \(n\), not finite-sample inferences.

**4. Conical opening.** Fix \(n,g\), let \(k_n=k_n(g)\), and define \(\rho=\sqrt{d^2+\varepsilon^2}\). Equation (2), together with \(\cos((\pi+\varepsilon)/2)=-\sin(\varepsilon/2)\), gives locally
\[
(R(k)+g)^2=d^2+\left(k_n^2+\frac{g^2}{4}\right)\varepsilon^2+O_{g,n}(\rho^3)
\]
for roots with \(k-k_n=O(\rho)\), since \(k_n^2/\sin^2(\pi k_n)=k_n^2+g^2/4\). The implicit function theorem applied to the two signed square-root branches (or strict monotonicity of \(R\) on the relevant interval) produces exactly two roots
\[
k_{n,\pm}=k_n\pm\frac{\sqrt{d^2+(k_n^2+g^2/4)\varepsilon^2}}{D_n}+O_{g,n}(\rho^2).
\]
Squaring and subtracting yields the asserted conical energy splitting. Because the closed operator has compact resolvent, the isolated double eigenvalue yields exactly two local levels; the transfer equation exhausts them.

## Verification
The standalone file `verify.py` evaluates the trace directly from the independent product of four \(2\times2\) transfer matrices and compares it to (1). It independently brackets the scalar roots, verifies their half-flux secular identities and global gap inequalities on 500 random positive coupling pairs, tests large-index approach to the sharp coefficient, and checks the two-parameter conical slope at several levels and couplings. Run `python3 verify.py` with Python 3 and no third-party dependencies; the expected completion marker is `VERIFY_OK`. These tests are reproducibility checks, not the proof of infinitely many spectral assertions.

## Relationship to prior work
Krive and Sandström (arXiv:cond-mat/9704151, first public 1997-04-17) study persistent-current resonances of a one-dimensional ring with two tunnel barriers, the closest physical setup found. Their accessible abstract describes off-resonance, resonance, and semiresonance currents, but does not state the all-level sharp imbalance ceiling or the two-parameter conical coefficients; their complete original manuscript was not accessible for a decisive full-text priority comparison.

Viefers, Koskinen, Singha Deo, and Manninen (arXiv:cond-mat/0310064, first public 2003-10-03; journal 2004), in their accessible 35-page review, discuss magnetic flux, impurity-induced spectral gaps, and finite lattice rings, but do not give this antipodal continuum two-delta doublet theorem. Exner (arXiv:1906.01229) treats optimization of identical repulsive delta positions in a **zero-flux** periodic loop, a different optimization and spectral level; an accessible later proof of its all-coupling equidistant claim likewise does not imply (2)--(3) or the flux cone. The present result does not assert a new general transfer-matrix method or novelty of the Aharonov--Bohm effect itself.

## Limitations
This is an exact noninteracting one-dimensional delta-barrier model with antipodal positions. The bound concerns gaps **within the indexed half-flux doublets**, not all consecutive spectral gaps or transport resonances. The high-level limit fixes \(\alpha,\beta\), and the conical expansion fixes \(g,n\); neither is a joint uniform large-energy/small-imperfection theorem. Historical-priority uncertainty remains because the complete 1997 two-barrier manuscript could not be inspected. The result does not imply a device-scale experimental tolerance without validating the delta approximation, coherence, and other physical effects.

## References
1. I. V. Krive and P. Sandström, *Resonant Tunneling and Persistent Current of a Non-interacting and Weakly Interacting One-dimensional Electron Gas*, arXiv:cond-mat/9704151, v1 submitted 1997-04-17; related journal work Phys. Rev. B **56** (1997), 9255, DOI 10.1103/PhysRevB.56.9255.
2. S. Viefers, P. Koskinen, P. Singha Deo, M. Manninen, *Quantum rings for beginners: Energy spectra and persistent currents*, arXiv:cond-mat/0310064 (2003-10-03), Physica E **21** (2004), 1--35; DOI 10.1016/j.physe.2003.08.076. Open full text: https://users.jyu.fi/~pekkosk/resources/pdf/viefers_physicae_04.pdf.
3. P. Exner, *An optimization problem for finite point interaction families*, arXiv:1906.01229, v1 2019-06-04; J. Phys. A **52** (2019), 405302; DOI 10.1088/1751-8121/ab3d82.
4. *All-coupling equidistant maximizer for repulsive point interactions on a loop*, public mathematical note, 2026, published-finding corpus repository: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-all-coupling-equidistant-maximizer-for-repulsive-point-interacti--e80ea5c2ae33.
