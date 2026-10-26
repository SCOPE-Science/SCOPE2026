# Quadratic unfolding of the dark phonon band in a two-resonator acoustic chain

## Finding

A local dark resonance becomes a narrow but genuine propagating Bloch band when two attached oscillators are detuned. Although their **squared-frequency mismatch is linear** in the tuning parameter, the band's **squared-frequency width is quadratic** in that mismatch. The exact coefficient measures how efficiently the dark resonator motion couples back to the host chain.

Consider a host mass \(M>0\), connected to neighboring hosts by springs \(K>0\), with two uncoupled attached masses \(m_1=aM\), \(m_2=bM\), where \(a,b>0\). The attached spring constants are \(\kappa_1=m_1r_1\), \(\kappa_2=m_2r_2\), with squared resonance frequencies \(r_1,r_2>0\).

Write \(z(\theta)=2(K/M)(1-\cos\theta)\), \(c=4K/M\), and let \(\lambda_{\mathrm{mid}}(z)\) be the middle of the three squared-frequency eigenvalues. If \(0<r_1<r_2\), the branch is strictly increasing, lies between the local frequencies, and satisfies

\[
0<\frac{d\lambda_{\mathrm{mid}}}{dz}
=|u_0|^2
\le \left[1+\frac{\big((ar_1^2)^{1/3}+(br_2^2)^{1/3}\big)^3}{(r_2-r_1)^2}\right]^{-1},
\]

where \(|u_0|^2\) is the host component's squared modulus in the **mass-normalized unit Bloch eigenvector**. In particular the band width is at most \(c\) times the displayed bound.

For \(r_1=r-\varepsilon\), \(r_2=r+\varepsilon\), where \(r>0\) is fixed and \(\varepsilon\downarrow0\), the entire middle branch has the uniform expansion

\[
\lambda_{\mathrm{mid}}(z,\varepsilon)=
r+\frac{a-b}{a+b}\varepsilon+
\frac{4ab\,[z-r(1+a+b)]}{r^2(a+b)^3}\varepsilon^2
+O(\varepsilon^3),\qquad 0\le z\le c.
\]

The **sharp leading bandwidth law** and uniform host-energy law are

\[
W_\lambda(\varepsilon)
:=\lambda_{\mathrm{mid}}(c,\varepsilon)-\lambda_{\mathrm{mid}}(0,\varepsilon)
=\frac{4cab}{r^2(a+b)^3}\varepsilon^2+O(\varepsilon^3),
\]

\[
|u_0(z,\varepsilon)|^2=
\frac{4ab}{r^2(a+b)^3}\varepsilon^2+O(\varepsilon^3)
\quad\text{uniformly in } z\in[0,c].
\]

Since the coefficient is positive, the unfolding exponent two is optimal. The ordinary-frequency band width is \(W_\omega=W_\lambda/(2\sqrt r)+O(\varepsilon^3)\). At fixed total attached mass fraction \(a+b\), the leading bandwidth coefficient is largest when \(a=b\).

## Assumptions and scope

An infinite periodic one-dimensional harmonic mass-and-spring lattice is considered; every mass and spring is strictly positive. The host has one scalar displacement per cell; each of the two attached oscillators couples only to its own host and not directly to the other resonator or adjacent cells. No damping, nonlinearities, disorder, external driving, or finite-chain boundary is included. Frequencies are real, nonnegative, and squared frequencies carry physical units of inverse-time squared. The near-degenerate expansion fixes \(a,b,r,c>0\) and lets \(\varepsilon\to0^+\); its remainder constants can depend on those four fixed parameters but not on \(z\in[0,c]\).

In mass-normalized coordinates the Bloch dynamic matrix is the real symmetric matrix

\[
H(z)=\begin{pmatrix}
z+ar_1+br_2&-\sqrt a\,r_1&-\sqrt b\,r_2\\
-\sqrt a\,r_1&r_1&0\\
-\sqrt b\,r_2&0&r_2
\end{pmatrix}.
\]

At \(r_1=r_2=r\), its eigenvalue \(r\) is a simple flat band for every bounded \(z\) and the corresponding normalized eigenvector has zero host amplitude.

## Proof

**1. Strict eigenvalue interlacing.** Eliminating the two attached displacements in \((H-\lambda I)u=0\) gives the scalar equation

\[
z=F(\lambda):=\lambda\left[1+\frac{ar_1}{r_1-\lambda}+\frac{br_2}{r_2-\lambda}\right].
\]

For \(\lambda\in(r_1,r_2)\),

\[
F'(\lambda)=1+\frac{ar_1^2}{(\lambda-r_1)^2}+\frac{br_2^2}{(r_2-\lambda)^2}>0.
\]

The endpoint limits of \(F\) are \(-\infty\) at \(r_1^+\) and \(+\infty\) at \(r_2^-\), because the residues are nonzero. Thus there is exactly one middle eigenvalue between the resonator frequencies for every real \(z\), and \(d\lambda_{\mathrm{mid}}/dz=1/F'(\lambda_{\mathrm{mid}})>0\). The other two eigenvalues interlace below \(r_1\) and above \(r_2\).

**2. Exact kinetic-energy identity and global flattening bound.** The attached coordinates in a mass-normalized eigenvector satisfy

\[
u_1=\frac{\sqrt a\,r_1}{r_1-\lambda}u_0,\qquad
u_2=\frac{\sqrt b\,r_2}{r_2-\lambda}u_0.
\]

Unit normalization gives \(|u_0|^2=1/F'(\lambda)\), proving the equality in the finding. For \(\Delta=r_2-r_1>0\), set \(t=\lambda-r_1\), \(A=(ar_1^2)^{1/3}\), \(B=(br_2^2)^{1/3}\). Minimizing \(A^3/t^2+B^3/(\Delta-t)^2\) over \(0<t<\Delta\) gives the minimum \((A+B)^3/\Delta^2\), attained at \(t=A\Delta/(A+B)\). Substitution proves the global upper bound; integrating over \(0\le z\le c\) proves the width upper bound. The inequality is optimal as a one-variable estimate but equality need not occur within a given physical Brillouin interval.

**3. Uniform dark-band perturbation.** At \(r_1=r_2=r\), the middle eigenvalue \(r\) has host-free eigenvector \((0,\sqrt b,-\sqrt a)/\sqrt{a+b}\). The two remaining eigenvalues are the roots of

\[
\lambda^2-[z+r(1+a+b)]\lambda+zr=0.
\]

The value of this quadratic at \(\lambda=r\) is \(-r^2(a+b)<0\). Consequently the flat eigenvalue is simple and uniformly separated from both other eigenvalues for \(z\in[0,c]\). Analytic perturbation for symmetric finite matrices therefore yields a Taylor expansion in \(\varepsilon\) with a remainder uniform in that compact interval.

Write \(\lambda=r+t\varepsilon+u(z)\varepsilon^2+O(\varepsilon^3)\) and substitute into the scalar dispersion identity with \(r_1=r-\varepsilon\), \(r_2=r+\varepsilon\). Cancellation of its order \(\varepsilon^{-1}\) term gives \(t=(a-b)/(a+b)\). The remaining constant-order equation is

\[
z=r(1+a+b)+\frac{r^2(a+b)^3}{4ab}u(z),
\]

so \(u(z)=4ab[z-r(1+a+b)]/[r^2(a+b)^3]\). This proves the stated uniform expansion. Subtracting the endpoint values yields the bandwidth law. Finally the exact normalized-energy identity and the uniform eigenvalue expansion give

\[
\frac1{F'(\lambda_{\mathrm{mid}})}=
\frac{4ab}{r^2(a+b)^3}\varepsilon^2+O(\varepsilon^3),
\]

uniformly in \(z\in[0,c]\). Since \(\sqrt{\lambda}\) is smooth near \(r>0\), the frequency conversion follows. At fixed \(a+b\), the inequality \(4ab\le(a+b)^2\) proves the final mass-allocation observation.

## Verification

The accompanying standalone `CHECK.py` constructs the independently mass-normalized three-by-three Bloch matrix and uses symmetric eigenvalue computations to compare both the quadratic prediction and eigenvector host weight. It checks 20 parameter/detuning combinations drawn from five positive physical parameter sets, verifies monotonicity, strict interlacing, the asymptotic coefficient, and the nonasymptotic slope upper bound. It also compares the host weight with centered finite-difference derivatives. Run `python CHECK.py` after installing `numpy`. These finite numerical checks corroborate the formulas; global statements are proved analytically above.

## Relationship to prior work

Bonanomi, Theocharis and Daraio (arXiv:1403.1052v1; first posted 2014-03-05) analyze a locally resonant granular chain and motivate the underlying mass-in-mass propagation structure. Jones, Movchan and Gei (2011) analyze multi-scale resonators in structured solids. Stein, Nouh and Singh (arXiv:2107.08431v1, sections 2.1.1–2.1.3) explicitly derive multi-resonator dispersion, characterize the exactly flat bands at identical attached frequencies, and display narrow dispersive passbands separating gaps when resonators are distinct. Those known forward dispersion results are not claimed here as new. The present result quantifies the near-degenerate dispersive unfolding by an exact positive quadratic coefficient valid for unequal attached masses, an exact kinetic-energy/slope identity, and a global finite-detuning flattening inequality. No formal completeness or priority theorem is asserted over all specialized literature.

## Limitations

The theorem is confined to the conservative, scalar, nearest-neighbor chain with two independent local resonators and positive fixed parameters. The quadratic asymptotic is for **squared natural frequencies**, not raw spring-constant differences with masses varying independently. The Brillouin interval is finite and fixed before taking the detuning limit. Inferences about finite dissipative transmission amplitudes, experimental resolution, general periodic elastic continua, nonlinear response, or random imperfections are not proved. Generic perturbation theory establishes analyticity, but the model-specific coefficient and physically quantified leakage law require the explicit calculation. Specialized earlier perturbation analyses may contain an equivalent coefficient not identified in the material inspected.

## References

1. L. Bonanomi, G. Theocharis, C. Daraio, *Locally Resonant Granular Chain*, arXiv:1403.1052v1 (posted 2014-03-05), https://arxiv.org/abs/1403.1052.
2. A. Stein, M. Nouh, T. Singh, *Widening, Transition and Coalescence of Local Resonance Band Gaps in Multi-resonator Acoustic Metamaterials: From Unit Cells to Finite Chains*, arXiv:2107.08431v1 (posted 2021-07-18), https://arxiv.org/abs/2107.08431, notably Sections 2.1.1–2.1.3; article DOI 10.1016/j.jsv.2021.116716.
3. I. S. Jones, A. B. Movchan, M. Gei, *Waves and damage in structured solids with multi-scale resonators*, Proceedings of the Royal Society A 467 (2011), 964–984, DOI 10.1098/rspa.2010.0319.
