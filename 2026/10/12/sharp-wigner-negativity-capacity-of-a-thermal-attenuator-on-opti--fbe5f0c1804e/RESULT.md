# Sharp Wigner-negativity capacity of a thermal attenuator on optical single-rail qubits

## Finding

Consider any state supported on the vacuum and one-photon optical Fock levels, \(\{|0\rangle,|1\rangle\}\). Its density matrix in that basis is
\[\rho=\begin{pmatrix}1-p&c\\\overline c&p\end{pmatrix},\qquad 0\le p\le1,\quad |c|^2\le p(1-p).\]
Pass it through the single-mode, phase-insensitive thermal attenuator with transmissivity \(0\le\eta\le1\) and environmental mean photon number \(b\ge0\). Set \(A=\eta+(1-\eta)(2b+1)\), and define the integrated negative Wigner volume \(\mathcal N(\rho)=\int_{\mathbb C}[-W_\rho(z)]_+\,d^2z\), where \([t]_+=\max(t,0)\) and \(\int W\,d^2z=1\).

The exact maximum over **all** such mixed or pure optical single-rail inputs is
\[
\boxed{\sup_\rho\mathcal N(\mathcal E_{\eta,b}(\rho))=
\begin{cases}
0,&A\ge2\eta,\\
\dfrac{2\eta}{A}\exp\!\left(-1+\dfrac{A}{2\eta}\right)-1,&A<2\eta.
\end{cases}}
\]
For \(A<2\eta\), its unique maximizer is the single-photon Fock state \(|1\rangle\langle1|\). For any prescribed excitation population \(0<p<1\), the maximizers are **exactly** the pure superpositions \(\sqrt{1-p}|0\rangle+e^{i\phi}\sqrt p|1\rangle\), for arbitrary phases \(\phi\); every genuinely mixed state at that fixed population has strictly smaller negative volume.

For a fixed \(0<p\le1\) and \(A<2\eta\), the exact sharp fixed-population value is the following one-dimensional integral. Define
\[
R^2=\frac{A(2\eta-A)}{4\eta},\qquad s=\frac{A\sqrt{1-p}}{2\sqrt{\eta p}}.
\]
Then
\[
\boxed{\mathcal N_p^{\max}=\frac{16\eta p}{A^3}e^{-2s^2/A}\int_0^R(R^2-r^2)r\,e^{-2r^2/A}I_0\!\left(\frac{4rs}{A}\right)dr,}
\]
where \(I_0\) is the modified Bessel function. For \(p=0\) and for \(A\ge2\eta\), this value is zero. In the negative-volume regime the additional strict photon-budget bound holds:
\[
\boxed{0<\mathcal N(\mathcal E_{\eta,b}(\rho))\le p\,\mathcal N_1^{\max}}\quad\text{if the output Wigner function is negative},
\]
with equality only for \(p=1\); vacuum has \(p=0\) and zero volume. In particular, the universal loss threshold is \(\eta\le (b+1/2)/(b+1)\).

## Assumptions and scope

The bosonic mode has the usual canonical Wigner distribution on \(\mathbb C\). The attenuation channel mixes the input field with an independent thermal state of occupation \(b\) at a beamsplitter of intensity transmissivity \(\eta\). There is no squeezing, phase-dependent noise, heralding, postselection, additional modes, or allowance for input photon levels greater than one. The bound is on integrated Wigner-negative volume, not on nonclassical depth, negativity potential, Wigner minimum, or operational preparation probability. The single input mean photon number equals \(p\).

## Proof

**1. Channel profile.** The symmetrically ordered characteristic function of the input state is
\[
\chi_\rho(\xi)=e^{-|\xi|^2/2}\bigl[1-p|\xi|^2+c\,\xi-\overline c\,\overline\xi\bigr],
\]
for the phase convention in equation (1). Attenuation replaces \(\chi_\rho(\xi)\) by \(\chi_\rho(\sqrt\eta\,\xi)\exp[-(1-\eta)(2b+1)|\xi|^2/2]\). Gaussian Fourier inversion therefore gives, after choosing the phase-space orientation consistent with the matrix entry \(c\),
\[
W(z)=\frac{2}{\pi A}e^{-2|z|^2/A}\left[1-\frac{2\eta p}{A}+\frac{4\eta p|z|^2}{A^2}+\frac{4\sqrt\eta}{A}\operatorname{Re}(cz)\right].\tag{1}
\]
The expression integrates to one because every nonconstant correction has zero Gaussian mean. Direct substitution at \(\eta=1\) reproduces the Wigner functions of the vacuum, one-photon state, and their coherences.

**2. Exact negative disks.** If \(p>0\) and \(\eta>0\), completing the square in the bracket of (1) yields
\[
\frac{4\eta p}{A^2}|z-z_c|^2 + 1-\frac{2\eta p}{A}-\frac{|c|^2}{p},\qquad z_c=-\frac{A\overline c}{2\sqrt\eta\,p}.
\]
Hence the negative set is a nonempty open disk precisely when \(2\eta p/A+|c|^2/p>1\). Since \(|c|^2\le p(1-p)\), every input has nonnegative Wigner function when \(A\ge2\eta\). At \(\eta=0\) the output is thermal and is likewise Wigner-positive. For a pure input with \(0<p\le1\), \(|c|^2=p(1-p)\), the negative disk is \(|z-z_c|<R\) with the radius displayed above, and has strictly positive negative volume if \(A<2\eta\). Its center has modulus \(|z_c|=s\). Notice that the disk radius is independent of \(p\), while its displacement is not.

**3. Strict optimization at fixed excitation.** For each fixed \(0<p<1\), rotate the phase convention so that \(c=r\) is real and \(0\le r\le r_{\max}:=\sqrt{p(1-p)}\). The two pure input states with coherences \(\pm r_{\max}\) have the same negative volume, because a phase rotation of \(\pi\) exchanges them. Every state with \(r<r_{\max}\) is their strictly nontrivial convex combination with weights \((1\pm r/r_{\max})/2\). Negative volume is convex in the density matrix because \(t\mapsto[-t]_+\) is convex. The inequality is **strict**: the two pure output Wigner functions have distinct nonempty negative disks centered at opposite nonzero positions, so on the positive-area symmetric difference of those disks one function is negative while the other is positive. Pointwise convexity is strict there for weights strictly between zero and one. Thus the fixed-\(p\) maximizers are exactly the pure phase family. For \(p=0,1\), there is only one possible input density matrix.

**4. Sharp integral and photon-budget bound.** For a pure state, equation (1) reduces exactly to
\[
-W(z)=\frac{8\eta p}{\pi A^3}e^{-2|z|^2/A}(R^2-|z-z_c|^2)\quad\text{inside }|z-z_c|<R.
\]
Shift to disk-centered polar coordinates \(u=z-z_c\). Angular integration gives \(\int_0^{2\pi}e^{-4rs\cos\vartheta/A}d\vartheta=2\pi I_0(4rs/A)\), proving the displayed fixed-population integral. For fixed \(R>0\), the convolution
\[
J(s)=\int_{|u|<R}(R^2-|u|^2)e^{-2|u+s|^2/A}\,d^2u
\]
is strictly maximized at \(s=0\): express the radial paraboloid by integrating indicators of nested centered disks, then express the strictly radially decreasing Gaussian by its positive layer-cake of concentric disks. The intersection area of two disks is maximized when their centers agree, and for each \(s>0\) a positive set of pairs of radii gives strict inequality. Consequently, for each \(0<p<1\), \(\mathcal N_p^{\max}<p\mathcal N_1^{\max}\), and by step 3 this also bounds every mixed state with that same \(p\). At \(p=1\), the negative disk is centered and the Gaussian integral evaluates to \(\mathcal N_1^{\max}=k\exp(-1+1/k)-1\), with \(k=2\eta/A>1\). The pure Fock state is therefore the unique global maximizer when \(A<2\eta\), and the claimed universal threshold follows from \(A\ge2\eta\).

## Verification

The accompanying `verify.py` numerically evaluates the disk integral using an exponentially scaled modified Bessel function, compares it with direct two-dimensional midpoint quadrature of (1), checks the Fock closed form and photon-population upper bound over physical mixed inputs, and tests the Wigner-positive boundary. Run `python verify.py` with the versions declared in `requirements.txt`. The command previously executed successfully and reported `VERIFY_OK all_checks=112`. Finite grid checks corroborate but do not establish the strict convexity or Gaussian rearrangement arguments, which are proved above.

## Relationship to prior work

Kenfack and Życzkowski [2] define the negative Wigner volume and calculate the single-photon value in the lossless case. Özdemir and coauthors [1] analyze Wigner profiles for experimentally generated vacuum–one-photon superpositions. Miranowicz and coauthors [3] numerically study negative Wigner volume for coherent superpositions in finite-dimensional optical spaces, including the two-dimensional family. Those works establish the objects and important special cases; the lossless single-photon volume, the qualitative presence of superposition negativity, and Wigner-positivity criteria are not claimed as new. Miranowicz and coauthors [4] derive nonclassical-depth and beam-splitter entanglement-potential comparisons for arbitrary mixed single-rail qubits; these are different quantities and can rank mixed and pure inputs differently. The additional result assessed here is the exact **thermal-channel negative-volume optimization over the entire mixed input Bloch disk at each fixed excitation population**, its strict equality classification, and the resulting closed all-input capacity bound.

## Limitations

The optimization applies only to the physical optical subspace spanned by vacuum and one photon. It does not extend the bound to higher photon numbers, multimode states, squeezed Gaussian channels, or non-Gaussian heralded operations. The Bessel integral is an exact one-dimensional representation, not generally an elementary closed form. The strictness statements require \(A<2\eta\); at or below threshold all inputs have zero negative volume and there is no unique maximizer. The bound measures negative volume, not an operational distillation yield. Exact publication priority beyond the literature inspected is not independently established.

## References

1. Ş. K. Özdemir, A. Miranowicz, M. Koashi and N. Imoto, *Quantum-scissors device for optical state truncation: A proposal for practical realization*, arXiv:quant-ph/0107048 (first posted 9 July 2001).
2. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015 (first posted 2 June 2004).
3. A. Miranowicz, M. Paprzycka, A. Pathak and F. Nori, *Phase-space interference of states optically truncated by quantum scissors*, arXiv:1307.6950 (first posted 26 July 2013).
4. A. Miranowicz et al., *Statistical mixtures of states can be more quantum than their superpositions*, arXiv:1502.04523 (first posted 16 February 2015).
