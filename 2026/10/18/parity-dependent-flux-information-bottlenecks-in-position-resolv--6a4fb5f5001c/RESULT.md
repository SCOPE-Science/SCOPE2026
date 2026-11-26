# Parity-dependent flux-information bottlenecks in position-resolved quantum ring walks

## Finding

On a simple \(n\)-cycle with \(n\ge3\), let \(S|j\rangle=|j+1\rangle\) and \(H_\phi=J(e^{i\phi/n}S+e^{-i\phi/n}S^\dagger)\), with \(J>0\) and total flux \(\phi\). From the localized input \(|0\rangle\), set \(\psi_j=\langle j|e^{-itH_\phi}|0\rangle\) and \(p_j=|\psi_j|^2\). The ordinary single-shot position Fisher information is \(\mathcal I_n=\sum_{j:p_j>0}(\partial_\phi p_j)^2/p_j\); the pointwise value at a support zero need not equal the nearby limit.

The set of fluxes where all position scores vanish for **every** observation time is \(\pi\mathbb Z\) for even \(n\) and \(\pi/2+\pi\mathbb Z\) for odd \(n\). At each fixed flux outside its exceptional set, writing \(x=Jt\),
\[
\begin{aligned}
\mathcal I_{2r}(\phi,t)&=\frac{4\sin^2(\phi/2)}{(r!)^2}x^{2r}+O(x^{2r+2}) &&(r\ge2),\\
\mathcal I_{2r+1}(\phi,t)&=\frac{8\cos^2\phi}{((r+1)!)^2}x^{2r+2}+O(x^{2r+4}) &&(r\ge1).
\end{aligned}
\]
The leading information is from the antipode in the even case and from the two farthest sites in the odd case. In the fixed uniform Peierls-phase encoding and fixed site basis above, the pure-state QFI is \(8J^2t^2/n^2\). Thus the ratio of position FI to QFI decays at generic fixed flux as \(x^{n-2}\) for even \(n\) and \(x^{n-1}\) for odd \(n\), with positive leading constants.

## Proof

The Bessel generating function gives the winding expansion
\[
\psi_j=\sum_{q\equiv j\ ({\rm mod}\ n)}(-i)^q J_q(2x)e^{iq\phi/n}.
\]
Its factorial tails justify termwise differentiation in \(\phi\) at fixed time. The frequency-\(\ell\) coefficient of \(p_j\) is \((-i)^{n\ell}\) times a real number. Pairing positive and negative frequencies, for even \(n\) the probabilities contain only cosine harmonics, while for odd \(n\) they contain cosine harmonics of even frequency and sine harmonics of odd frequency. Their derivatives vanish at the stated exceptional fluxes, including all zero-probability outcomes. On an even ring the antipode has \(p_r(\pi,t)=0\) at all times: the terms at \(q\) and \(-q\) have equal coefficients before the flux phases, and their phase sum is zero when \(q\equiv r\pmod{2r}\).

For any site at distance \(d<n/2\) the shortest route is unique and yields \(p_j=x^{2d}/(d!)^2+O(x^{2d+1})\). A nonconstant flux term pairs distinct windings \(q,q'\), so \(|q|+|q'|\ge|q-q'|\ge n\), and \(\partial_\phi p_j=O(x^n)\). Its FI contribution is \(O(x^{2n-2d})\). These estimates follow from \(J_s(2x)=x^s/s!+O(x^{s+2})\) for nonnegative \(s\) and \(J_{-s}=(-1)^sJ_s\).

On the even ring the two shortest routes to \(r\) give \(\psi_r=2(-i)^r x^r\cos(\phi/2)/r!+O(x^{r+2})\). Hence \(p_r=2(1+\cos\phi)x^{2r}/(r!)^2+O(x^{2r+2})\), and \(\partial_\phi p_r=-2\sin\phi\, x^{2r}/(r!)^2+O(x^{2r+2})\). The quotient gives the even coefficient at a fixed nonexceptional flux. Every other site has \(d\le r-1\) and contributes at most \(O(x^{2r+2})\).

On the odd ring, the farthest sites \(r,r+1\) have interfering routes of lengths \(r,r+1\). The two leading expansions are
\[
 p_r=\frac{x^{2r}}{(r!)^2}-\frac{2x^{2r+1}\sin\phi}{r!(r+1)!}+O(x^{2r+2}),\qquad
 p_{r+1}=\frac{x^{2r}}{(r!)^2}+\frac{2x^{2r+1}\sin\phi}{r!(r+1)!}+O(x^{2r+2}).
\]
Differentiating and dividing gives \(4\cos^2\phi\,x^{2r+2}/((r+1)!)^2+O(x^{2r+3})\) per site. To sharpen the error, complex conjugation in the site basis gives \(p_j(\phi,-t)=p_j(-\phi,t)\), while reflection gives \(p_j(-\phi,t)=p_{-j}(\phi,t)\). The first and last expressions are equal as functions of \(\phi\), so their derivatives at fixed \(\phi\) are also equal. The two farthest-site FI terms thus exchange under \(x\mapsto-x\) and their sum is even. Each quotient extends real analytically through \(x=0\): the probability has the factor \(x^{2r}\) times a nonvanishing analytic function, while the squared derivative has the factor \(x^{4r+2}\). Evenness removes the entire order-\(2r+3\) term. This argument does not require the even part of a site's probability to be flux independent. The remaining sites contribute \(O(x^{2r+4})\) or smaller. Both leading coefficients are positive outside their respective exceptional sets, so a nonexceptional flux has nonzero information for sufficiently small positive time.

Finally, \(H_\phi\) and \(\partial_\phi H_\phi\) commute, so the QFI is \(4t^2\operatorname{Var}_0(\partial_\phi H_\phi)\). In the localized state the expectations of \(S,S^2\) and their adjoints vanish for \(n\ge3\); hence the derivative has mean zero and second moment \(2J^2/n^2\), giving the stated QFI.

## Verification and scope

The accompanying `verify.py` compares the probability and derivative calculations using direct matrix evolution and spectral evolution and reports 784 finite checks including small-time coefficients, blind fluxes, and QFI. The analytic proof, not the finite checks, covers all stated sizes, fluxes and times. The short-time statements are at fixed nonexceptional flux. Ordinary first-order position blindness does not rule out singular or second-order inference. Site probabilities are invariant under a diagonal phase gauge, but the state QFI is not invariant under arbitrary parameter-dependent changes of the encoding reference. No noisy setting or general measurement protocol is claimed.

## Relationship to prior work

Zanoli, Ragazzi, Bordone, and Paris, [Quantum walks on a ring as a versatile single-parameter sensor](https://doi.org/10.3389/frqst.2026.1894991), treat ground-state preparation schemes; their vanishing magnetic-only QFI is not for the localized input here. Luppi, [Flux control of measurement back-action and Leggett–Garg correlations in chiral quantum walks](https://arxiv.org/abs/2608.12519v1), §§VI.A–B, gives the rooted return winding expansion and a different even/odd onset for sequential readout based on returns, and explicitly leaves localized flux estimation open in the conclusion. The winding method and a parity effect are thus prior; the resolved position scores and their sharp farthest-site information terms are the distinct claim. Amorim et al., [Absorption-based qubit estimation in discrete-time quantum walks](https://doi.org/10.1103/zns5-vzyy), estimates a coin state, and Seveso, Benedetti, and Paris, [The walker speaks its graph](https://arxiv.org/abs/1809.09211), treats the tunnelling amplitude, not magnetic flux. This comparison is not a certification of bibliographic priority.
