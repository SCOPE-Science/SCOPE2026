# Exact transparency-count transition for two on-site defects in a tight-binding chain

## Finding
Consider an infinite one-dimensional uniform tight-binding lattice with precisely two real on-site impurities, separated by any integer number \(L\ge 1\) of lattice steps. For nonzero impurity amplitudes, perfect transmission at a propagating energy exists **only if their absolute amplitudes are equal**. With equal and opposite amplitudes, there are exactly \(L-1\) perfectly transmitting energies independent of the amplitudes. With equal signed amplitudes \(U\ne0\), the number is \(L\) when \(0<|U|<2t/L\) and \(L-1\) when \(|U|\ge2t/L\), where \(t>0\) is the uniform hopping amplitude. The missing mode exits through a band edge at the exact threshold and has square-root band-edge approach. No band-edge point is counted as a propagating scattering resonance.

## Assumptions and scope
For all \(t>0\), integers \(L\ge1\), and real \(U,V\), let \(H\) act on \(\ell^2(\mathbb Z)\) by
\[
(H\psi)_n=t(\psi_{n-1}+\psi_{n+1})+U\mathbf 1_{\{n=0\}}\psi_n+V\mathbf 1_{\{n=L\}}\psi_n.
\]
At each wave number \(k\in(0,\pi)\), the energy is \(E=2t\cos k\) and a left-incident scattering solution has asymptotics \(e^{ikn}+r(k)e^{-ikn}\) on the left and \(\tau(k)e^{ikn}\) on the right. A perfect-transmission energy means \(r(k)=0\), equivalent to \(|\tau(k)|=1\) by flux conservation. We count distinct energies in the open band \((-2t,2t)\), not resonant poles, local transmittance maxima, or nonpropagating endpoints.

When \(U=V=0\), the entire open band is transparent. Otherwise the complete classification is:

1. If \(|U|\ne|V|\), no open-band wave number has perfect transmission (this includes exactly one vanishing impurity).
2. If \(V=-U\ne0\), precisely \(k_m=m\pi/L\), \(1\le m\le L-1\), are transparent, with energies \(E_m=2t\cos(m\pi/L)\).
3. If \(V=U\ne0\), the transparent energies are precisely \(E=2t x\), \(x\in(-1,1)\), satisfying
\[
2tT_L(x)-U\mathcal U_{L-1}(x)=0,
\]
where \(T_L\) and \(\mathcal U_{L-1}\) are Chebyshev polynomials of the first and second kind. Every transparent energy is distinct, and their number is
\[
N_{\mathrm{trans}}(U,L)=\begin{cases}L,&0<|U|<2t/L,\\L-1,&|U|\ge 2t/L.\end{cases}
\]
For \(U>0\), the extra branch approaching the upper edge as \(\varepsilon=2t/L-U\downarrow0\) has
\[
k_{\mathrm{edge}}=\sqrt{\frac{3L}{t(2L^2+1)}}\,\sqrt\varepsilon+O(\varepsilon^{3/2}).
\]
For \(U<0\), the corresponding statement holds for \(\pi-k_{\mathrm{edge}}\) approaching the lower edge after reflection \(k\mapsto\pi-k\). The critical equality places a root at an excluded band edge, leaving exactly \(L-1\) interior energies.

## Proof
**1. Exact reflection-zero equation.** Write \(s=\sin k>0\) and \(g_k=( -2it s)^{-1}=i/(2ts)\). The outgoing free lattice Green kernel at energy \(2t\cos k\) is \(G_k(n)=g_ke^{ik|n|}\). The Lippmann--Schwinger equations for the two impurity-site amplitudes are
\[
\psi_0=1+g_k(U\psi_0+V e^{ikL}\psi_L),\qquad
\psi_L=e^{ikL}+g_k(Ue^{ikL}\psi_0+V\psi_L).
\]
On the left the reflection coefficient is \(r=g_k(U\psi_0+Ve^{ikL}\psi_L)\), and \(\psi_0=1+r\). If \(V\ne0\), then \(r=0\) forces \(\psi_0=1\) and \(\psi_L=-Ue^{-ikL}/V\); substitution into the second equation yields the necessary and sufficient condition
\[
e^{2ikL}=-\frac UV\frac{1-g_kV}{1+g_kU}.\tag{1}
\]
The denominator never vanishes for real \(U\) and \(k\in(0,\pi)\). For real finite impurities, the outgoing solution is unique: a nontrivial purely outgoing solution at real propagating energy would have outward nonzero conserved discrete probability flux at both ends, contradicting flux conservation. Consequently the algebraic condition also constructs the unique reflectionless state. If exactly one impurity vanishes, the single-site scattering equation gives nonzero reflection, and if both vanish the medium is homogeneous.

Taking moduli in (1) gives
\[
U^2\left(1+\frac{V^2}{4t^2s^2}\right)=V^2\left(1+\frac{U^2}{4t^2s^2}\right),
\]
hence \(U^2=V^2\). Thus there is no perfect transmission for unequal absolute strengths.

**2. Opposite signs.** If \(V=-U\ne0\), (1) simplifies identically to \(e^{2ikL}=1\). Exactly the \(L-1\) values \(k_m=m\pi/L\) with \(m=1,\ldots,L-1\) lie in the open band. Their energies are pairwise distinct since cosine is strictly decreasing on \((0,\pi)\).

**3. Equal signs and complete count.** For \(V=U\ne0\), put \(\alpha(k)=\arctan(U/(2t\sin k))\in(-\pi/2,\pi/2)\). Condition (1) becomes
\[
Lk+\alpha(k)=\bigl(m+\tfrac12\bigr)\pi,\qquad m\in\mathbb Z.\tag{2}
\]
Taking the cosine of (2) and using \(\cos\alpha=2t\sin k/\sqrt{4t^2\sin^2k+U^2}\) proves the equivalent real equation \(2t\sin k\cos(Lk)-U\sin(Lk)=0\). Dividing by \(\sin k\) and using \(\cos(Lk)=T_L(\cos k)\), \(\sin(Lk)/\sin k=\mathcal U_{L-1}(\cos k)\) gives the asserted Chebyshev polynomial.

It suffices first to take \(U>0\). Define \(f(k)=Lk+\alpha(k)\). Then \(f(0+)=\pi/2\), \(f(\pi-)=L\pi+\pi/2\), and
\[
f'(k)=L-\frac{2tU\cos k}{4t^2\sin^2k+U^2}.
\]
For \(0<k<\pi/2\) the subtracted positive fraction strictly decreases with \(k\), and for \(\pi/2\le k<\pi\) the derivative is positive. If \(U\ge2t/L\), the derivative is strictly positive throughout the open interval (it may tend to zero only at the excluded endpoint at equality). Equation (2) therefore has exactly one solution for each \(m=1,\ldots,L-1\), and none for any other integer. If \(0<U<2t/L\), \(f'(0+)=L-2t/U<0\), so \(f\) decreases to exactly one strict interior minimum below \(\pi/2\), then increases to \(L\pi+\pi/2\). In addition to the preceding \(L-1\) solutions it crosses the \(m=0\) level once on its increasing branch; no other levels are reached. This proves exactly \(L\) solutions. Under \(k\mapsto\pi-k\) and \(U\mapsto-U\), the polynomial equation changes by an overall nonzero sign, so the count and root simplicity are identical for negative \(U\).

**4. Sharp threshold asymptotics.** At \(U_c=2t/L\), \(2tT_L(1)-U_c\mathcal U_{L-1}(1)=0\). The Chebyshev derivatives \(T_L'(1)=L^2\) and \(\mathcal U_{L-1}'(1)=L(L^2-1)/3\) imply that the derivative of the polynomial with respect to \(x\) at \((x,U)=(1,U_c)\) equals \(2t(2L^2+1)/3>0\). The implicit-function theorem gives the nearby root
\[
x=1-\frac{3L\varepsilon}{2t(2L^2+1)}+O(\varepsilon^2),\quad \varepsilon=U_c-U\downarrow0.
\]
Since \(\arccos(1-z)=\sqrt{2z}+O(z^{3/2})\), the square-root asymptotic follows. Negative \(U\) reflects the calculation to \(x=-1\). All statements are uniform in the exact quantifiers given above; none infer infinite-lattice conclusions from a finite numerical scan.

## Verification
A standalone Python checker is supplied as `checker.py`, using direct complex transfer-matrix scattering, independent of the outgoing-Green-function proof. It runs 2,714 finite numerical checks across spacings \(1\le L\le17\), positive and negative impurity amplitudes, equal and opposite signs, unequal amplitudes, and the square-root edge regime. The maximum computed reflected amplitude at a predicted transparency point was \(5.32\times10^{-13}\). Execute `python3 checker.py`. Numerical checks corroborate the theorem, while the argument in the Proof section establishes its exact all-spacing classification.

For an exact illustrative case, at \(L=2\) and \(U=t\), the polynomial is \(4t x^2-2t x-2t=2t(2x+1)(x-1)\): only \(x=-1/2\) is propagating, while \(x=1\) is the excluded threshold. At \(U=t/2\), both polynomial roots lie strictly inside \((-1,1)\), making two transparent energies.

## Relationship to prior work
Mišković, English, Davison and Goodman (1996) investigate two impurities in a monatomic tight-binding chain and derive transmission probabilities for adjacent and separated defects. The generic two-impurity scattering method and interference mechanism are established prior art, and are not claimed here. Its complete paper was not accessible for comparison; overlap in the exact spectral count and boundary law remains possible. Chakrabarti (2006) treats two substitutional backbone impurities together with an additional side-coupled finite Fano–Anderson chain. Sections 2–4, including its explicit transfer matrices, show how an additional energy-dependent effective potential changes the resonance structure; the present two-impurity-only sharp count and band-edge transition do not follow directly from those stated side-chain classifications. Longhi (2006) treats a time-driven single defect, not two static real on-site defects. The contribution assessed here is the complete fixed-separation classification and its precise critical transparency loss, rather than the standard transfer-matrix or scattering formulas.

## Limitations
The result assumes an infinite one-channel nearest-neighbor chain with uniform real hopping and only two real on-site potentials; no longer-range hopping, absorption, many-body interaction, time-dependent drive, or changed bond hopping is permitted. It classifies exact open-band transmission zeros of reflection, not resonant width, approximate peak heights, or finite-size spectra. The available search and full-text comparisons do not certify historical priority, particularly given the inaccessible 1996 same mathematical model article. Independent scientific review has not been performed.

## References
1. Z. L. Mišković, R. A. English, S. G. Davison, F. O. Goodman, *Transmission of double-impurity atomic switches*, Physical Review B **54**, 255–260 (1996). DOI: https://doi.org/10.1103/PhysRevB.54.255 (publication date 1996-07-01; abstract accessible, full text restricted).
2. A. Chakrabarti, *Fano resonance in discrete lattice models: controlling lineshapes with impurities*, arXiv:cond-mat/0611211, first submitted 2006-11-08. Full-text manuscript: https://arxiv.org/abs/cond-mat/0611211.
3. S. Longhi, *Transmission and localization control by ac fields in tight-binding lattices with an impurity*, Physical Review B **73**, 193305 (2006). DOI: https://doi.org/10.1103/PhysRevB.73.193305 (single driven defect, contextual contrast).
