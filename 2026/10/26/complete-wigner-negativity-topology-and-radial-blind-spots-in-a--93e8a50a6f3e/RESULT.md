# Complete Wigner-negativity topology and radial blind spots in a stationary qutrit oscillator

## Finding

For the stationary qutrit state of the single quantum Arosh oscillator, the conventional continuous-variable Wigner function has **exactly three possible negativity topologies**: no negative points, two opposite connected negative lobes, or one annular connected negative region. All transition surfaces, including tangencies, have elementary sharp formulas in the two dissipation rates.

Let \(a=\gamma_1>0\) denote single-photon pumping, \(b=\gamma_2>0\) the nonlinear loss coefficient, and set
\[
S=\sqrt{(a+3b)^2+16},\quad c=2\sqrt{a(2a+b)},\quad q_\pm=4a-b\pm\frac{8ab}{S}.
\]
The Wigner-negative set \(\mathcal N=\{\alpha\in\mathbb C:W(\alpha)<0\}\) is **empty** exactly when \(q_+\le c\); it comprises **one annular connected component** exactly when \(q_->c\); and it comprises **two opposite connected components** exactly when \(q_-\le c<q_+\). These cases are mutually exclusive and exhaustive.

The angularly integrated Wigner function \(\overline W(r)=(2\pi)^{-1}\int_0^{2\pi} W(re^{i\theta})\,d\theta\) has a negative value for some \(r\) exactly when
\[
\frac ab>\frac{3+\sqrt7}{4}.
\]
Consequently the angular average can be everywhere nonnegative even though the full Wigner function has negative lobes. Two explicit parameter paths display distinct transitions:

* If \(a=b=t>0\), negativity first appears as **two lobes** at the exact threshold
\[
t_\mathrm{birth}=\frac{2\sqrt3-3}{\sqrt{4-(2\sqrt3-3)^2}}=0.238562694451\ldots.
\]
At \(t\le t_\mathrm{birth}\) there is no negative region; at \(t>t_\mathrm{birth}\) there are two lobes, but \(\overline W(r)\ge0\) for every \(r\ge0\).

* If \(a=2t,\ b=t\), the negative region is **annular** for \(0<t<t_\mathrm{split}\) and consists of **two lobes** for \(t\ge t_\mathrm{split}\), where
\[
t_\mathrm{split}=\frac{4(7-2\sqrt{10})}{\sqrt{256-25(7-2\sqrt{10})^2}}=0.172753380808\ldots.
\]
The angular average has a negative region for every \(t>0\) on this second path. At the splitting threshold, two radial directions are excluded by zeros of the Wigner function and the strict negative set has two components.

## Assumptions and scope

Work on \(\mathcal H_3=\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle\}\), with annihilation operator \(a_0|n\rangle=\sqrt n|n-1\rangle\) (and \(a_0|0\rangle=0\)), number operator \(n=a_0^\dagger a_0\), and \(x=(a_0+a_0^\dagger)/\sqrt2\). The dynamics is
\[
\dot\rho=-i[n,\rho]+a\,\mathcal D[a_0^\dagger](\rho)+b\,\mathcal D[xa_0](\rho),\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}.
\]
Rates \(a,b\) are dimensionless in oscillator-frequency units, and are strictly positive. The stationary state is the following explicit qutrit density matrix, already derived by Chattopadhyay–Pendse–Gupta:
\[
\rho_*=
\begin{pmatrix}
2b/d&0&R e^{i\phi}\\
0&b/d&0\\
R e^{-i\phi}&0&2a/d
\end{pmatrix},\quad
d=2a+3b,\quad
R=\frac{4\sqrt2 ab}{dS},\quad
\phi=\arctan\frac4{a+3b}.
\]
The Wigner function here is the **ordinary oscillator Wigner function of this density operator embedded in the full Fock space**. It is not a discrete qutrit Wigner function and it is not asserted to describe the stationary Wigner function of the untruncated oscillator. Coordinates are \(\alpha=re^{i\theta}\), \(r\ge0\), with \(z=r^2\).

## Proof

**1. Independent stationary-state check.** In the qutrit basis, the two jump matrices are \(a_0^\dagger\) and
\[
xa_0=\begin{pmatrix}0&0&1\\0&1/\sqrt2&0\\0&0&\sqrt2\end{pmatrix}.
\]
Substitution of \(\rho_*\) into the Lindblad generator gives zero. Its populations sum to one; the only possibly nontrivial positivity condition is \(R^2\le (2b/d)(2a/d)\). In fact, their ratio is
\[
\frac{R^2}{(2b/d)(2a/d)}=\frac{8ab}{(a+3b)^2+16}<\frac23,
\]
so \(\rho_*\) is a strictly positive density matrix for all assumed rates.

**2. Exact sign polynomial.** Using the Fock-state displaced-parity identity (or directly the \(0\)-, \(1\)-, \(2\)-level oscillator Wigner matrix elements),
\[
W(re^{i\theta})=\frac{2e^{-2z}}{\pi d}P(z,\theta),\quad
P=16az^2-4q(\theta)z+(2a+b),
\]
where
\[
q(\theta)=4a-b-\frac{8ab}{S}\cos(2\theta+\phi).
\]
The prefactor is everywhere strictly positive. The values of \(q\) range exactly from \(q_-\) to \(q_+\).

**3. Angular/radial classification, including boundary cases.** Put \(c=2\sqrt{a(2a+b)}\). For \(z\ge0\), the quadratic \(P\) is negative for some \(z\) if and only if \(q(\theta)>c\). For each such angle, the full radial negative interval is
\[
z_-(\theta)<z<z_+(\theta),\qquad
z_\pm(\theta)=\frac{q(\theta)\pm\sqrt{q(\theta)^2-c^2}}{8a}.
\]
If \(q_+\le c\), no angle is admissible. If \(q_->c\), every angle is admissible and the two positive continuous bounding radii enclose one annulus. If \(q_-\le c<q_+\), the admissible angular set is a disjoint union of two open antipodal arcs (each one centered where \(\cos(2\theta+\phi)=-1\)); over each arc the negative radial band is connected, giving exactly two components. Equality \(q_-=c\) still excludes two angles and hence gives two components, whereas equality \(q_+=c\) has no strictly negative points. These arguments classify the topology globally, not merely a finite grid.

**4. Angular averaging and hidden negativity.** Angular integration removes the cosine term. Its sign polynomial is
\[
\overline P(z)=16az^2-4(4a-b)z+(2a+b).
\]
It has a negative value at a nonnegative \(z\) exactly when \(4a-b>c\). For \(r=a/b>0\), this inequality is equivalent to \(r>(3+\sqrt7)/4\). Indeed, it requires \(r>1/4\); squaring the positive sides then yields \(8r^2-12r+1>0\), whose only admissible branch is the displayed one.

**5. Exact one-parameter transitions.** On \(a=b=t\), \(q_+/t=3+2t/\sqrt{t^2+1}\), \(q_-/t=3-2t/\sqrt{t^2+1}\), and \(c/t=2\sqrt3\). The first ratio crosses \(2\sqrt3\) exactly at \(t_\mathrm{birth}\); the second is always strictly less. Also \(a/b=1<(3+\sqrt7)/4\), proving the claimed radial blind spot. On \(a=2t, b=t\), \(q_+/t=7+16t/\sqrt{25t^2+16}>2\sqrt{10}=c/t\); \(q_-/t=7-16t/\sqrt{25t^2+16}\) decreases strictly from \(7\) to \(7-16/5\), crossing \(2\sqrt{10}\) exactly once at \(t_\mathrm{split}\). The radial criterion holds since \(2>(3+\sqrt7)/4\). This finishes the classification.

## Verification

Run `python verify.py` with NumPy installed. The program independently assembles the nine-dimensional Lindblad superoperator from the jump matrices, evaluates the stated stationary density and positivity, compares the Wigner sign polynomial against a separate Fock-element expression, checks representative parameter regions and both exact transition constants. Its execution returned **521 passed finite checks**. These are reproducibility checks; the all-parameter and topological assertions follow from the algebraic proof above, not from grid sampling. An arbitrarily thin negativity region near a boundary may be missed by a finite grid.

## Relationship to prior work

Chattopadhyay, Pendse and Gupta (arXiv:2610.19904v1, first public 2026-10-14), Sections III.2–III.3, derive the stationary qutrit density and its anisotropic Wigner function and demonstrate numerical negative regions at selected parameters. Those identities and that observation are prior knowledge. The present result classifies **all positive rate pairs**, the number and shape of connected negative components, the exact topological transitions, and an explicit regime where angular averaging entirely hides the negativity. It does not claim a new Lindblad stationary-state formula. The earlier Arosh–Cross–Lifshitz oscillator study (arXiv:2011.02706) treats distinct untruncated quantum Rayleigh–van der Pol models; its qualitative discussion of nonnegative limit-cycle Wigner functions does not address this qutrit stationary parameter classification. Kenfack–Życzkowski (arXiv:quant-ph/0406015) motivates Wigner negativity as a nonclassicality witness, without claiming this model-specific phase diagram.

## Limitations

The conclusion concerns strictly positive loss and pumping rates in the specified three-level truncation. No claim is made at a vanishing rate, where stationary-state uniqueness can change, nor for the untruncated physical oscillator, modified jump operators, or discrete finite-dimensional Wigner representations. An ordinary Wigner-positive state can still be nonclassical according to different criteria; positivity is only a statement about this quasiprobability witness. Priority beyond the checked literature has not been independently certified.

## References

1. R. Chattopadhyay, V. Pendse, S. Gupta, *Single and coupled quantum van der Pol oscillators: Wigner-function dynamics, exact qutrit solutions, and synchronization*, arXiv:2610.19904v1 (2026-10-14), Sections III.2–III.3, https://arxiv.org/abs/2610.19904.
2. L. Ben Arosh, M. C. Cross, R. Lifshitz, *Quantum limit-cycles and the Rayleigh and van der Pol oscillators*, arXiv:2011.02706 (2020), https://arxiv.org/abs/2011.02706; *Physical Review Research* **3**, 013130 (2021).
3. A. Kenfack, K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015 (2004), https://arxiv.org/abs/quant-ph/0406015.
