# Two sharp mode thresholds and universal edge laws for three equispaced light-mass defects

## Finding
In an infinite nearest-neighbor monatomic harmonic chain with three identical lighter replacement masses at positions \(0,d,2d\), the number of normalizable vibrations above the host phonon band is exactly
\[
N(\delta,d)=1+\mathbf 1_{\{\delta>1/(4d)\}}+\mathbf 1_{\{\delta>3/(4d)\}}.
\]
Here \(d\ge1\) is an integer separation in lattice sites and \(0<\delta<1\) is the relative mass deficit. At either equality the new mode is not square summable. The two emergent eigenvalues obey independent, separation-universal quadratic laws:
\[
\lambda_{\rm odd}-4=16\left(\delta-\frac1{4d}\right)^2+O_d\!\left(\left(\delta-\frac1{4d}\right)^3\right),
\]
\[
\lambda_{\rm even,low}-4=144\left(\delta-\frac3{4d}\right)^2+O_d\!\left(\left(\delta-\frac3{4d}\right)^3\right).
\]
Both expansions are one-sided from above their corresponding threshold, at fixed \(d\). The ratio of their leading coefficients is \(9\), independent of the separation.

## Assumptions and scope
Let masses \(m_n=m\) except \(m_0=m_d=m_{2d}=m(1-\delta)\), with \(m>0\), fixed nearest-neighbor spring constant \(K>0\), and \(0<\delta<1\). For displacements \(u_n(t)=u_n e^{i\omega t}\), set \(\lambda=m\omega^2/K\), and let \(L\) be the discrete Laplacian \((Lu)_n=2u_n-u_{n-1}-u_{n+1}\). The generalized eigenvalue problem is \(Lu=\lambda Mu\), where \(M\) has diagonal entries \(1-\delta\) on the three defect sites and \(1\) otherwise. A localized normal mode means a nonzero solution in \(\ell^2(\mathbb Z)\). The essential spectrum is \([0,4]\) in squared-frequency units, with the upper edge corresponding to physical frequency \(2\sqrt{K/m}\).

## Proof
**1. Reduction to a positive three-site matrix.** Positivity of the quadratic spring energy excludes negative eigenvalues. The exterior constant-mass second-order recurrence excludes square-summable eigenvectors for \(\lambda\in[0,4]\), including its endpoints; if a solution vanishes on a half-line, the recurrence forces it to vanish everywhere. For \(\lambda>4\), write \(\lambda=2+q+q^{-1}\), \(0<q<1\). The free resolvent kernel is
\[
[(\lambda-L)^{-1}]_{mn}=\frac{(-q)^{|m-n|}}{\sqrt{\lambda(\lambda-4)}}.
\]
The equation \((\lambda-L)u=\lambda\delta\sum_{a\in\{0,d,2d\}}u_a e_a\) reduces, after a diagonal alternating-sign gauge on these three coordinates, to \(\delta B(q)v=v\), with
\[
B(q)=\frac{1+q}{1-q}
\begin{pmatrix}1&t&t^2\\t&1&t\\t^2&t&1\end{pmatrix},\qquad t=q^d.
\]
There are at most three isolated eigenvalues because this is a rank-three condition, and each root yields a unique decaying \(\ell^2\) mode.

**2. Spectral branches and exhaustive mode counts.** The three eigenvalues of the inner matrix, in strictly descending order for \(0<t<1\), are
\[
\mu_+(t)=\frac{2+t^2+t\sqrt{8+t^2}}2,\quad
\mu_{\rm odd}(t)=1-t^2,\quad
\mu_-(t)=\frac{2+t^2-t\sqrt{8+t^2}}2.
\]
The middle eigenvector is \((1,0,-1)\), and the last is reflection-even. The inequalities \(\mu_+>\mu_{\rm odd}>\mu_->0\) follow from \(\sqrt{8+t^2}>3t\) for \(0<t<1\). Each eigenvalue of \(B(q)\) is strictly increasing in \(q\): in terms of \(\lambda\), \(B\) is the restriction of \(\lambda(\lambda-L)^{-1}\), and its derivative is the strictly negative quadratic form \(-L(\lambda-L)^{-2}\) on nonzero finitely supported vectors. Hence every branch crosses the level \(1/\delta\) at most once. At \(q\downarrow0\) all three branch eigenvalues tend to \(1\), smaller than \(1/\delta\). At \(q\uparrow1\) the three limits, in order, are \(+\infty\), \(4d\), and \(4d/3\). This gives exactly the asserted strict threshold inequalities. At equality, the root can only occur at \(q=1\), corresponding to nondecaying exterior solutions and not to a localized eigenmode.

**3. Exact edge coefficients.** Put \(\varepsilon=1-q\). Since \(t=(1-\varepsilon)^d\), direct Taylor expansion gives
\[
\mu_{\rm odd}=2d\varepsilon-d(2d-1)\varepsilon^2+O_d(\varepsilon^3),
\]
\[
\mu_-=\frac{2d}3\varepsilon+\frac{d(9-2d)}{27}\varepsilon^2+O_d(\varepsilon^3).
\]
Therefore the deficit needed for each eigenvalue branch is
\[
\delta_{\rm odd}(q)=\frac{1-q}{(1+q)\mu_{\rm odd}(q^d)}=\frac1{4d}+\frac\varepsilon4+O_d(\varepsilon^2),
\]
\[
\delta_{\rm even,low}(q)=\frac{1-q}{(1+q)\mu_-(q^d)}=\frac3{4d}+\frac\varepsilon{12}+O_d(\varepsilon^2).
\]
Finally \(\lambda-4=(1-q)^2/q=\varepsilon^2/(1-\varepsilon)\). Inverting the two expansions proves the coefficients \(16\) and \(144\), with the claimed cubic remainders for fixed \(d\). The other (largest) eigenvalue branch exists for every positive defect contrast.

## Verification
Run `python3 verify.py` with Python 3 and its standard library. The checker independently counts eigenvalues above \(4\) by Sylvester inertia of a finite Dirichlet mass-normalized chain with \(1201\) sites, compares all three predicted mode-count regimes for each \(d\in\{1,2,3,5,10\}\), and evaluates the two near-critical coefficients. These numerical finite-chain tests do not establish the infinite-chain statements; those follow from the exact resolvent and monotonicity proof above.

## Relationship to prior work
Montroll and Potts established lattice-defect Green-function methods and the general finite-rank determinant framework, including interactions among defects. Thus neither the resolvent technique nor the existence of localized impurity modes is claimed new. Theocharis et al. and Man et al. studied the frequencies of one and two impurities in physical granular chains, with bead-size changes also modifying the contacts; their analyzed models are not identical to the present mass-only, constant-spring infinite chain. The specifically assessed result here is the complete three-equispaced-defect count with two exact thresholds and the separation-independent coefficients of both distinct edge openings. The complete 1955 source could not be inspected, so priority over all specializations of its determinant framework remains an explicit risk.

## Limitations
The formulas assume an infinite linear conservative chain, identical three defect deficits, equal defect spacing, and unchanged nearest-neighbor stiffness. They do not describe damping, nonlinear Hertzian contacts, nonuniform inter-impurity spacing, finite-sample mode visibility, or measurement noise. The quadratic remainders are for fixed integer spacing; no uniform double-scaling assertion in \(d\) is made. A full-text priority comparison with Montroll and Potts (1955) was unavailable.

## References
1. Montroll and Potts, *Effect of Defects on Lattice Vibrations*, Physical Review 100 (1955), 525–543, doi:10.1103/PhysRev.100.525.
2. Theocharis et al., *Localized Breathing Modes in Granular Crystals with Defects*, arXiv:0906.4094 (2009); Physical Review E 80, 066601.
3. Man et al., *Defect Modes in One-Dimensional Granular Crystals*, arXiv:1103.2483 (2011); Physical Review E 85, 037601.
