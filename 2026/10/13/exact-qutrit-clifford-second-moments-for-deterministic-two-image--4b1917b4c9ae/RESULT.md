# Exact qutrit-Clifford second moments for deterministic two-image classical channels

## Finding
Let \(F:\{0,1,2\}\to\{0,1,2\}\) have exactly two image points and define the deterministic classical qutrit channel
\[
\mathcal C_F(X)=\sum_{j=0}^{2}\langle j|X|j\rangle\,|F(j)\rangle\langle F(j)|.
\]
Let \(\mathcal C_3\) be the projective single-qutrit Clifford group, and let the superscript \(\mathcal C_3\) denote the randomized-benchmarking twirl used by Wallman and Flammia. Put
\[
r=|\{j:F(j)=j\}|.
\]
For the eighteen maps with \(|\operatorname{im}F|=2\), one has \(r\in\{0,1,2\}\), with six maps for each value. The complete spectrum of the Wallman--Flammia second-moment operator is
\[
\operatorname{spec}\!\left((\mathcal C_F^{\otimes2})^{\mathcal C_3}\right)=
\begin{cases}
\{1,(1/6)^{[4]},(1/24)^{[8]},(-1/8)^{[16]},0^{[52]}\},&r=0,\\
\{1,(1/6)^{[4]},(-1/12)^{[8]},0^{[68]}\},&r=1,\\
\{1,(1/6)^{[4]},(1/24)^{[8]},(1/8)^{[16]},0^{[52]}\},&r=2.
\end{cases}
\]
Here the bracketed exponents denote multiplicities. In particular every such channel is \(2\)-contractive with respect to the qutrit Clifford design, and the largest nontrivial eigenvalue modulus is exactly \(1/6\).

These channels are genuinely outside the higher-dimensional reduction used in the source for unital channels: each \(\mathcal C_F\) is nonunital, and its affine projection onto the unital part is not even positive.

## Assumptions and scope
The Hilbert space is exactly \(\mathbb C^3\), the computational basis is fixed, and \(F\) is a deterministic map with exactly two image points. The channel is completely positive and trace preserving because it has Kraus operators
\[
K_j=|F(j)\rangle\langle j|,
\qquad
\sum_{j=0}^2K_j^\dagger K_j=I.
\]
It is entanglement breaking because it first measures in the computational basis and then prepares a basis state.

The twirling set is the projective single-qutrit Clifford group. The result does not claim the same spectrum for an arbitrary qutrit unitary \(2\)-design, nor does it prove the Wallman--Flammia conjecture for all qutrit channels.

## Proof
Use the normalized nonidentity Weyl operators as a basis for the eight-dimensional traceless operator space. Write
\[
D_{a,b}=X^aZ^b,
\qquad
(a,b)\in\mathbb F_3^2\setminus\{(0,0)\},
\qquad
\omega=e^{2\pi i/3}.
\]
The traceless Liouville block \(\phi_F\) of \(\mathcal C_F\) annihilates every Weyl operator with \(a\ne0\). On the two diagonal Weyl operators it is given exactly by
\[
(\phi_F)_{(0,c),(0,b)}
=
\frac13\sum_{j=0}^2\omega^{bj-cF(j)},
\qquad b,c\in\{1,2\}.
\]
Thus \(\phi_F\) has rank one for every two-image map \(F\).

Let
\[
B_F=(\phi_F^{\otimes2})^{\mathcal C_3}.
\]
The qutrit Clifford group is generated projectively by the Fourier, quadratic-phase, and Weyl displacement generators. Their adjoint action permutes the eight nonidentity Weyl operators with phases in \(\{1,\omega,\omega^2\}\). Exact closure gives \(216\) projective elements. Averaging \(\phi_F^{\otimes2}\) over those elements can therefore be done entirely in the cyclotomic field \(\mathbb Q(\omega)\), with no floating-point step.

For all eighteen two-image maps the average is in fact rational. Exact enumeration gives
\[
\operatorname{rank}B_F=12.
\]
If \(r=1\), it also gives
\[
B_F\left(B_F-\frac16I\right)\left(B_F+\frac1{12}I\right)=0,
\qquad
\operatorname{Tr}B_F=0.
\]
The polynomial has distinct roots, so \(B_F\) is diagonalizable. Rank and trace then force multiplicities \(4\), \(8\), and \(52\) for \(1/6\), \(-1/12\), and \(0\), respectively.

If \(r\in\{0,2\}\), exact enumeration gives
\[
B_F\left(B_F-\frac16I\right)\left(B_F-\frac1{24}I\right)=0,
\qquad
\operatorname{Tr}B_F=1,
\]
so the multiplicities are \(4\), \(8\), and \(52\) for \(1/6\), \(1/24\), and \(0\).

It remains to include the one-copy diagonal blocks in the Wallman--Flammia second-moment operator. Their Eq. (89) shows that the full operator is block lower triangular with diagonal blocks
\[
1,
\qquad
f_F I_8,
\qquad
f_F I_8,
\qquad
B_F.
\]
The trace of the full superoperator \(\mathcal C_F\) is the number \(r\) of fixed computational-basis projectors, whereas the scalar identity block contributes \(1\). Therefore
\[
f_F=\frac{\operatorname{Tr}\phi_F}{8}=\frac{r-1}{8}.
\]
Combining this scalar with the spectrum of \(B_F\) gives the three displayed full spectra.

Finally, the unital projection cannot supply this result. If \(y\) is the output value with two preimages and \(z\) is the output value with no preimage, then
\[
\mathcal C_F(I)-I=|y\rangle\langle y|-|z\rangle\langle z|.
\]
Choose an input basis state whose image is the singleton output value. The projected-unital map
\[
\mathcal U_F(X)=\mathcal C_F(X)-\frac{\operatorname{Tr}X}{3}\bigl(\mathcal C_F(I)-I\bigr)
\]
has diagonal entry \(-1/3\) at \(|y\rangle\langle y|\) on that positive input. Hence \(\mathcal U_F\) is not positive.

## Verification
The included `verify.py` performs the finite part of the proof using exact rational arithmetic in \(\mathbb Q(\omega)\). It constructs the \(216\)-element projective qutrit Clifford adjoint action from generators, enumerates all eighteen functions with two image points, forms every twirled \(64\times64\) block exactly, proves rationality of every entry, checks the rank and annihilating polynomial stated above, and reconstructs the full \(81\)-dimensional spectra from Eq. (89). Running the packaged script produces `VERIFY_OK`; the accompanying `verification_output.txt` records the deterministic output.

The computation is exhaustive only for this finite qutrit family. No numerical sample or timeout is used as evidence for an infinite statement.

## Relationship to prior work
Wallman and Flammia define \(n\)-contractivity and conjecture that every nonunitary channel is \(2\)-contractive with respect to any unitary \(2\)-design. They prove the claim for unital channels and note that it then follows for qubits because a qubit channel's unital projection remains completely positive. They explicitly state that higher dimensions remain open. Their block formula for a general trace-preserving channel is the structural input used here.

The present family lies in the first unresolved dimension and is nonunital. More strongly, its unital projection is not positive, so Proposition 16 cannot simply be applied to these channels. The result is narrower than the published conjecture because it fixes the qutrit Clifford design, but it gives the exact second-moment spectrum and a uniform \(5/6\) spectral gap for the complete two-image deterministic classical family.

Graydon, Skanes-Norman, and Wallman record that the Clifford group is a unitary \(2\)-design in prime dimensions, which includes dimension three. Later qutrit experiments have explicitly used the qutrit Clifford group for randomized benchmarking, so this finite design is not merely a formal test case. Targeted searches for the exact two-image qutrit spectrum, deterministic classical channels with Wallman--Flammia \(2\)-contractivity, and later resolutions of the higher-dimensional conjecture did not locate an implication-equivalent result.

## Limitations
The theorem is restricted to deterministic measure-and-prepare qutrit channels with exactly two image points and to the projective qutrit Clifford design. It does not establish \(2\)-contractivity for arbitrary qutrit noise or for every unitary \(2\)-design. The originality search was targeted rather than mathematically exhaustive; an obscure note could contain the same finite classification under different terminology.

The exact enumeration is part of the proof because the classified family and design are both finite. It should not be extrapolated to an infinite class without an additional argument.

## References
1. J. J. Wallman and S. T. Flammia, *Randomized Benchmarking with Confidence*, arXiv:1404.6025v1 (first public 2014-04-24), New J. Phys. 16 (2014) 103032. See Definition 15, Proposition 16, and Eq. (89).
2. M. A. Graydon, J. Skanes-Norman, and J. J. Wallman, *Clifford groups are not always 2-designs*, arXiv:2108.04200. The paper records the prime-dimensional Clifford group as a unitary \(2\)-design.
3. M. Kononenko, M. A. Yurtalan, S. Ren, J. Shi, S. Ashhab, and A. Lupascu, *Characterization of Control in a Superconducting Qutrit Using Randomized Benchmarking*, arXiv:2009.00599; Phys. Rev. Research 3, L042007 (2021).
4. J. J. Wallman, *Randomized benchmarking with gate-dependent noise*, Quantum 2, 47 (2018), arXiv:1703.09835.
