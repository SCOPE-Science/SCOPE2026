# Exact parity dichotomy and uniquely optimal loss allocation for two absorbing lattice sites

## Finding
For a left-incident plane wave at the band centre of a one-dimensional nearest-neighbour tight-binding lattice, allocate a fixed positive total absorptive onsite strength between two sites separated by an integer distance \(d\ge1\). If \(d\) is even, the absorbed fraction is independent of that allocation. If \(d\) is odd, a uniquely optimal, strictly positive loss allocation exists for **every** total budget. At large budget, the odd-separation optimum becomes almost perfectly absorbing, even though the even-separation and single-absorber designs become almost perfectly reflecting.

In hopping-energy units of one, let \(\gamma_L,\gamma_R\ge0\) be the imaginary-potential magnitudes at sites \(0,d\), with \(\gamma_L+\gamma_R=2b\), \(b>0\), and put \(x=\gamma_L/2\), \(y=\gamma_R/2=b-x\). Define the left-incident absorbed flux fraction by \(\mathcal A=1-|r|^2-|t|^2\), with unit incident amplitude and equal left/right group velocities. The complete band-centre result is
\[
\mathcal A_b(x)=\begin{cases}
\dfrac{2b}{(1+b)^2}, & d\text{ even},\\[4pt]
1-\dfrac{1+[b-2(b+1)x+2x^2]^2}{[1+b+2x(b-x)]^2}, & d\text{ odd}.
\end{cases}
\]
For odd \(d\), the unique maximizer \(x_*(b)\in(0,b)\) is the unique root in that interval of
\[
P_b(x)=b^3(1-2x)+b^2(6x^2-6x+1)+b(-6x^3+9x^2-4x+1)+2x^4-4x^3+3x^2-2x=0.
\]
For every \(b>0\), \(\mathcal A_b(x_*)>2b/(1+b)^2\). Furthermore
\[
x_*(b)=\frac b2-\frac{b^2}{8}+O(b^3)\quad(b\downarrow0),
\qquad
x_*(b)=\frac12-\frac1{4b}+\frac1{4b^2}+O(b^{-3})\quad(b\to\infty),
\]
\[
1-\max_{0\le x\le b}\mathcal A_b(x)=\frac1{4b^2}+O(b^{-3})\quad(b\to\infty).
\]
Thus the optimal upstream physical loss tends to \(\gamma_L=1\), while the remaining downstream loss grows with the total budget. The absorption is strictly less than one at each finite \(b\), because transmitted flux is positive.

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb Z)\). The one-particle Hamiltonian acts by
\[
(H\psi)_n=-\psi_{n-1}-\psi_{n+1}-i\gamma_L\mathbf1_{\{n=0\}}\psi_n-i\gamma_R\mathbf1_{\{n=d\}}\psi_n.
\]
The incident stationary scattering solution has momentum \(k\in(0,\pi)\), energy \(E=-2\cos k\), incoming amplitude one from the left, outgoing amplitude \(r\) to the left and \(t\) to the right. The stated optimization fixes the band centre \(k=\pi/2\), fixed integer \(d\), and fixed \(b>0\); it does not optimize the incident momentum, separation, or frequency bandwidth. Zero loss at either defect is allowed as a competing allocation. No spatially extended absorbing leads, amplification, driving or nonlinearities are assumed.

## Proof
**Step 1: exact two-site scattering.** For arbitrary \(0<k<\pi\), put \(X=\gamma_L/(2\sin k)\), \(Y=\gamma_R/(2\sin k)\) and \(z=e^{2ikd}\). Matching the plane-wave amplitudes and the discrete Schrödinger equations at the two impurity sites, or composing the two rank-one scattering transfer maps, gives
\[
t=\frac1{(1+X)(1+Y)-XYz},\qquad
r=\frac{-X(1+Y)-Y(1-X)z}{(1+X)(1+Y)-XYz}.
\]
The same equations remain valid if one of the losses vanishes. Setting \(B=X+Y\) and \(h=1-\cos(2kd)\), direct expansion gives the nonnegative absorption formula
\[
\mathcal A(k,d,X,Y)=
\frac{2B+4XY(1+Y)h}{(1+B)^2+2XY(1+B+XY)h}.
\]
This establishes both the normalization and the directionality: interchanging the two loss strengths changes the numerator because incidence is from the left.

**Step 2: parity at band centre.** At \(k=\pi/2\), \(X=x\), \(Y=y\) and \(z=(-1)^d\). If \(d\) is even, \(h=0\), hence \(\mathcal A=2b/(1+b)^2\) regardless of \(x\). If \(d\) is odd, \(h=2\), and the scattering denominator is \(D=1+b+2x(b-x)>0\), while the real reflection numerator is \(R=b-2(b+1)x+2x^2\). Thus \(t=1/D\), \(r=-R/D\), and \(\mathcal A=1-(1+R^2)/D^2\), yielding the theorem's exact profile. In particular \(\mathcal A<1\) for every finite budget.

**Step 3: global uniqueness.** Differentiation yields the exact identity
\[
\frac{d\mathcal A_b}{dx}=\frac{8P_b(x)}{D(x)^3}.
\]
For \(0<x<b\) introduce the positive ratio \(z=x/(b-x)\). Direct polynomial algebra gives
\[
(1+z)^4P_b\!\left(\frac{bz}{1+z}\right)=bH_b(z),
\]
where
\[
H_b(z)=b^2+b+1+2(1-b^2-b^3)z-3b(b+1)z^2-2(b+1)z^3-z^4.
\]
Reading the coefficients in descending powers, the \(z^4,z^3,z^2\) terms are strictly negative, the \(z^1\) term may have either sign or vanish, and the constant term is strictly positive. Consequently the coefficient list has **exactly one sign change**, for every \(b>0\); Descartes' rule gives at most one positive zero (counted with multiplicity). Existence follows because \(H_b(0)=b^2+b+1>0\) and \(H_b(z)\to-\infty\) as \(z\to\infty\). Because the zero is unique and \(P_b(0)=b(b^2+b+1)>0\), \(P_b(b)=-b<0\), the profile rises before \(x_*\) and falls after \(x_*\), including its closed endpoints. This proves unique global optimality and strict interior allocation.

**Step 4: strict gain over one-site/even-separation designs.** Holding \(B=b\) and \(X=x\in(0,b)\) fixed, differentiate the absorption expression from Step 1 with respect to \(h\). Its sign equals that of
\[
(1+b)[1+y(1+b)]-bxy=(1+b)+y[(1+b)^2-bx]>0,
\]
since \(0<x<b\) and \((1+b)^2-bx\ge1+2b\). Thus \(h=2\) strictly outperforms \(h=0\) for interior allocations. At \(x=0\) or \(b\), both are the single-site baseline \(2b/(1+b)^2\). In particular the odd-separation maximum is strictly higher than the even-separation absorption for each \(b>0\).

**Step 5: limiting allocation.** Expanding the polynomial zero condition at \(b\downarrow0\) with \(x=b/2+cb^2+O(b^3)\), the \(b^2\) coefficient is \(-2c-1/4\), hence \(c=-1/8\). The derivative of the scaled equation at the leading solution is nonzero, giving the stated expansion by the implicit-function theorem. At \(b\to\infty\), put \(x=1/2+c/b+d/b^2+O(b^{-3})\): the successive highest coefficients of \(P_b\) force \(c=-1/4\), \(d=1/4\), again with a nonzero limiting derivative. Substituting in \((1+R^2)/D^2\) gives \(1-\mathcal A_b(x_*)=1/(4b^2)+O(b^{-3})\). Therefore \(\max\mathcal A_b\to1\), while \(2b/(1+b)^2\to0\). These expansions apply to the unique roots already established, not to unrelated formal branches.

## Verification
The included standalone `checker.py` independently solves the four complex linear matching equations for the scattering amplitudes rather than using the closed scattering formula as its computational premise. It compares 500 random physical configurations against the exact amplitudes and absorption fractions, scans 180 logarithmically spaced fixed budgets against sampled competitors, verifies the positive phase benefit, and checks both singular-budget asymptotics. The exact derivative and polynomial-transformation identities were separately checked by symbolic expansion. These finite tests corroborate but do not replace Steps 1–5, which prove the claims for all admissible parameters.

## Relationship to prior work
Miroshnichenko and Kivshar [1] treat resonant wave transmission in conservative discrete networks decorated with side defects. Merkel and coauthors [2] demonstrate near-perfect **one-sided** acoustic absorption in asymmetric resonator structures; near-perfect one-sided absorption is therefore **not claimed to be a new physical phenomenon**. Guilarte and Muñoz-Castañeda [3] derive two-centre scattering formulas for predominantly real delta interactions in the continuum, without this lattice parity-constrained loss-budget optimization. Burke, Wiersig and Haque [4] analyze the single imaginary onsite impurity on a tight-binding lattice, including the decrease of absorption at strong loss. Longhi [5] investigates dissipative sites near the boundary of a finite or semi-infinite lattice, transient algebraic decay and coherent perfect absorption under prepared excitation; that is not the present two-port infinite-line fixed-sum optimization. The asserted mathematical contribution is the **combined** sharp parity dichotomy, all-budget uniqueness of the optimal two-loss split, and its singular high-budget absorption law for this specific two-impurity model, not the generic scattering formula, interference, quantum Zeno suppression, or near-perfect absorption alone.

## Limitations
This is an exact single-energy stationary scattering theorem in an ideal infinite uniform lattice. It does not quantify bandwidth, disorder, noise, decoherence, finite wave packets, or stability of the optimum to detuning. The optimality statement assumes a fixed total of **onsite imaginary-potential magnitudes**, not a constraint on actual dissipated power. It does not extend automatically to asymmetric hopping or other losses. Exact priority among all earlier specialized two-defect scattering studies cannot be guaranteed; any equivalent pre-existing fixed-budget classification would supersede the novelty assessment.

## References
[1] A. E. Miroshnichenko and Y. S. Kivshar, *Engineering Fano resonances in discrete networks*, arXiv:cond-mat/0505023, first submitted 2005-05-02. https://arxiv.org/abs/cond-mat/0505023

[2] A. Merkel, G. Theocharis, O. Richoux, V. Romero-García, and V. Pagneux, *Control of acoustic absorption in 1D scattering by indirect coupled resonant scatterers*, arXiv:1509.01443, first submitted 2015-09-04. https://arxiv.org/abs/1509.01443

[3] J. M. Guilarte and J. M. Muñoz-Castañeda, *Double-delta potentials: one dimensional scattering. The Casimir effect and kink fluctuations*, arXiv:1010.3116, first submitted 2010-10-15. https://arxiv.org/abs/1010.3116

[4] P. C. Burke, J. Wiersig, and M. Haque, *Non-Hermitian scattering on a tight-binding lattice*, arXiv:1910.07439, first submitted 2019-10-16. https://arxiv.org/abs/1910.07439

[5] S. Longhi, *Algebraic Absorption in Non-Hermitian Photonic Lattices*, *Photonics* **13** (2026), 574, DOI:10.3390/photonics13060574. https://doi.org/10.3390/photonics13060574
