# A sharp \(5/6\) Haar-fidelity ceiling for single-beamsplitter realistic teleportation
## Finding
For the realistic qubit-teleportation protocol of Trump, Bruß, and Lewenstein in which Alice sends the maximum-posterior Bell label inferred from photon-number detection after one polarization-preserving beamsplitter, with an ideal maximally entangled resource and a Haar-uniform unknown pure qubit, the exact maximal average teleportation fidelity is \(\bar F_{\max}=5/6\), attained by the standard 50:50 analyzer. The two Bell states \(\lvert\phi^+\rangle\) and \(\lvert\phi^-\rangle\) induce identical photon-count distributions for every such beamsplitter, so the maximum-a-posteriori Bell-label success probability is at most \(3/4\); a 50:50 analyzer attains this by perfectly distinguishing \(\lvert\psi^+\rangle\) and \(\lvert\psi^-\rangle\) and guessing within the unresolved \(\phi\)-pair. A correct Bell label gives fidelity one, while any wrong Pauli correction has Haar-average pure-state fidelity \(1/3\), hence \(\bar F=(1+2p_{\mathrm{MAP}})/3\le 5/6\). Therefore the source's reported numerical maximum \(\bar F_{\max}\approx0.88\) is not the Haar-uniform average over pure input states; the corrected value remains above the classical \(2/3\) benchmark and does not challenge the source's qualitative conclusion that incomplete linear-optical Bell analysis can still demonstrate nonclassical teleportation.

The bound is sharp. At a standard 50:50 beamsplitter, the two \(\psi\)-states have disjoint photon-count signatures, while the two \(\phi\)-states remain indistinguishable. The resulting Bell-label decision accuracy is exactly \(3/4\), and therefore the Haar-averaged teleportation fidelity is exactly
\[
\bar F_{\max}=\frac34+\frac14\cdot\frac13=\frac56.
\]

## Assumptions and scope
The input is an arbitrary pure qubit distributed with normalized Haar measure on the Bloch sphere. Alice and Bob share an ideal maximally entangled qubit pair. Alice performs the source's single polarization-preserving beamsplitter transformation followed by ideal photon-number-resolving detection of the two-photon output modes, chooses a Bell label of maximal posterior probability, and tells Bob to apply the Pauli correction associated with that label.

The result is restricted to that source protocol. It does not bound Bell measurements using nonvacuum ancillas, active optical elements, extra entanglement, adaptive networks beyond the stated analyzer, or nonlinear interactions.

## Proof
Let the four equiprobable Bell states be \(\lvert\psi^+\rangle,\lvert\psi^-\rangle,\lvert\phi^+\rangle,\lvert\phi^-\rangle\). For a detector outcome \(j\), write the joint probabilities of the two \(\psi\)-states as \(a_j\) and \(b_j\), and write the joint probability of either \(\phi\)-state as \(c_j\). The equality of the two \(\phi\)-probabilities follows directly from the source beamsplitter: it acts independently on horizontal and vertical polarization, so the all-horizontal and all-vertical sectors never interfere in a number-resolving detection event. The only distinction between \(\lvert\phi^+\rangle\) and \(\lvert\phi^-\rangle\) is the relative phase between those orthogonal sectors, which photon counting cannot observe. Thus for every \(j\),
\[
\Pr(j,\phi^+)=\Pr(j,\phi^-)=c_j.
\]
The maximum-posterior decision success is therefore
\[
p_{\mathrm{MAP}}=\sum_j\max\{a_j,b_j,c_j,c_j\}
\le\sum_j(a_j+b_j+c_j)=\frac14+\frac14+\frac14=\frac34.
\]

A conventional 50:50 analyzer attains equality: \(\lvert\psi^-\rangle\) produces the coincidence class with one photon in each output port and opposite polarizations, \(\lvert\psi^+\rangle\) produces the complementary opposite-polarization bunching class, and the two \(\phi\)-states occupy a common same-polarization class. Hence both \(\psi\)-labels are recovered perfectly, while one can do no better than a tie-break inside the \(\phi\)-pair, giving \(p_{\mathrm{MAP}}=3/4\).

In ideal teleportation the four Bell outcomes occur with probability \(1/4\), independent of the unknown input. If the inferred Bell label is correct, Bob's correction recovers the input exactly. If the inferred label is wrong, the residual operation is a nonidentity Pauli operator \(P\). Writing the input pure state by its unit Bloch vector \(r\), one has \(\lvert\langle\tau\rvert P\lvert\tau\rangle\rvert^2=r_k^2\) for one Cartesian component. Haar symmetry gives
\[
\int r_k^2\,d\mu(r)=\frac13.
\]
Consequently
\[
\bar F=p_{\mathrm{MAP}}+\frac{1-p_{\mathrm{MAP}}}3
=\frac{1+2p_{\mathrm{MAP}}}3\le\frac56,
\]
and the 50:50 analyzer attains the upper bound.

## Verification
The analytic proof uses only the polarization block structure of the source beamsplitter, equiprobability of ideal Bell outcomes, and the rotational identity \(\mathbb E_{\mathrm{Haar}}[r_k^2]=1/3\). The accompanying `verify.py` replays the exact rational decision and fidelity arithmetic and returns `VERIFY_OK`, including \(p_{\mathrm{MAP}}=3/4\) and \(\bar F=5/6\).

As a diagnostic only, a uniform weighting of the polar angle rather than Haar area would give \(\mathbb E[\cos^2\theta]=1/2\) and hence \(7/8=0.875\), numerically close to the source's \(0.88\). No claim is made that this was the source's implementation, because its numerical integration code is unavailable.

## Relationship to prior work
Trump, Bruß, and Lewenstein explicitly define a maximum-posterior lookup-table strategy, define an input-averaged fidelity, and report a numerical maximum \(\bar F_{\max}\approx0.88\) at 50% transmission. Their beamsplitter is polarization preserving.

Lütkenhaus, Calsamiglia, and Suominen proved that complete Bell analysis is impossible with the relevant linear-optical resources. Calsamiglia and Lütkenhaus later proved the sharp 50% ceiling for *unambiguous* discrimination of four equiprobable Bell states in a broader passive-linear-optics model with vacuum ancillas. Those results concern failure-allowed unambiguous discrimination, not the source's always-guess maximum-posterior rule and not its Haar-averaged teleportation fidelity; they therefore do not supply the \(3/4\) MAP label accuracy or the source-specific \(5/6\) correction proved here.

## Limitations
The statement corrects the Haar-uniform interpretation of the source's averaged pure-state fidelity. The source does not publish its numerical integration code, so the precise coordinate weighting that produced approximately \(0.88\) cannot be reconstructed from the paper alone. The nearby value \(7/8\) under uniform polar-angle weighting is therefore only an explanatory diagnostic, not evidence about the implementation.

The result assumes ideal detectors and the source's single polarization-preserving beamsplitter model. Additional optical resources can increase Bell-measurement performance and lie outside the claim. The correction changes the quantitative optimum from approximately \(0.88\) to \(5/6\approx0.8333\), but the corrected value still exceeds the classical qubit measure-and-prepare benchmark \(2/3\).

## References
1. C. Trump, D. Bruß, and M. Lewenstein, “Realistic teleportation with linear optical elements,” arXiv:quant-ph/0010113v1, first public 31 October 2000; *Physics Letters A* 279 (2001), 7–11, DOI: 10.1016/S0375-9601(00)00784-2.
2. J. Calsamiglia and N. Lütkenhaus, “Maximum efficiency of a linear-optical Bell-state analyzer,” arXiv:quant-ph/0007058v1; *Applied Physics B* 72 (2001), 67–71, DOI: 10.1007/s003400000484.
3. N. Lütkenhaus, J. Calsamiglia, and K.-A. Suominen, “Bell measurements for teleportation,” *Physical Review A* 59 (1999), 3295–3300, DOI: 10.1103/PhysRevA.59.3295.
