# A coherence-driven zero-probability counterexample for arbitrary multiphoton input
## Finding
For the four-mode passive interferometer
\[
U=\begin{pmatrix}
1/2&1/2&1/2&1/2\\
1/(2\sqrt3)&1/(2\sqrt3)&1/(2\sqrt3)&-\sqrt3/2\\
1/\sqrt2&-1/\sqrt2&0&0\\
1/\sqrt6&1/\sqrt6&-2/\sqrt6&0
\end{pmatrix},
\]
which is real orthogonal, let the internal two-level degree of freedom \(q\in\{0,1\}\) be unaffected by the network and use the convention \(a^\dagger_{k,q}=\sum_l U_{kl}b^\dagger_{l,q}\). With fixed spatial input occupation \((2,1,0,0)\), define the normalized pure input
\[
|\Psi_\phi\rangle=
\sqrt{\frac23}\,\frac{(a^\dagger_{1,0})^2}{\sqrt2}a^\dagger_{2,1}|0\rangle
+\frac{e^{i\phi}}{\sqrt3}a^\dagger_{1,0}a^\dagger_{1,1}a^\dagger_{2,0}|0\rangle.
\]
For ideal number-resolving detectors insensitive to \(q\), the probability of spatial output occupation \((1,1,1,0)\) is exactly
\[
P_{1110}(\phi)=\frac{1+\cos\phi}{24}.
\]
Hence \(P_{1110}(\pi)=0\), whereas \(P_{1110}(0)=1/12\), and erasing the coherence between the two displayed orthogonal input components gives \(P_{1110}=1/24\). The zero at \(\phi=\pi\) is therefore created by internal-state coherence. Moreover every completely indistinguishable one-, two-, or three-photon transition relevant to this event is nonsuppressed: for outputs among \(1,2,3\), the two-photon amplitudes are \(\sqrt2/4\) for two photons from input 1 and \(1/(2\sqrt3)\) for one photon from each of inputs 1 and 2, while the fully indistinguishable three-photon amplitude from spatial input \((2,1,0,0)\) to \((1,1,1,0)\) is \(\sqrt6/8\neq0\). Thus the zero-probability conjecture of arXiv:1410.1506, when applied to the arbitrary fixed-occupation input class of its Eq. (1), is false as stated: exact suppression need not be inherited from a completely indistinguishable subset and can depend on coherence between internal configurations. This does not address a narrower conjecture restricted to product internal states from independent sources.

## Assumptions and scope
The network acts only on the spatial mode and leaves the internal label \(q\) unchanged. Detectors resolve spatial occupation but not \(q\). The input has exactly two photons in spatial input 1 and one in spatial input 2; its two displayed Fock components are orthogonal and their squared weights are \(2/3\) and \(1/3\). This is within the arbitrary fixed-occupation multiphoton input class used in Eq. (1) of arXiv:1410.1506. The conclusion concerns that literal arbitrary-input scope. It does not claim a counterexample for the narrower product-state model of independent photon sources.

## Proof
The three internal-resolved states contributing to spatial output \((1,1,1,0)\) are distinguished by the output \(i\in\{1,2,3\}\) occupied by the unique \(q=1\) photon. Call them \(|f_i\rangle\). They are mutually orthogonal.

For the first component of \(|\Psi_\phi\rangle\), the \(q=1\) photon comes from spatial input 2 and the two \(q=0\) photons both come from spatial input 1. If \(\{i,j,k\}=\{1,2,3\}\), its amplitude at \(|f_i\rangle\) is
\[
\sqrt{\frac23}\,U_{2i}\,\sqrt2\,U_{1j}U_{1k}=\frac1{12}.
\]
For the second component, the \(q=1\) photon comes from spatial input 1. The two \(q=0\) photons, from spatial inputs 1 and 2, have bosonic amplitude \(U_{1j}U_{2k}+U_{1k}U_{2j}=1/(2\sqrt3)\). Thus
\[
\frac{e^{i\phi}}{\sqrt3}U_{1i}\left(U_{1j}U_{2k}+U_{1k}U_{2j}\right)=\frac{e^{i\phi}}{12}.
\]
Therefore
\[
\langle f_i|U|\Psi_\phi\rangle=\frac{1+e^{i\phi}}{12}
\]
for all three values of \(i\). Summing the three orthogonal internal outcomes gives
\[
P_{1110}(\phi)=3\left|\frac{1+e^{i\phi}}{12}\right|^2=\frac{1+\cos\phi}{24}.
\]
The incoherent mixture of the two input components removes the cross term and gives \(1/24\).

It remains to rule out the mechanism asserted by the conjecture for this event. For distinct target outputs among \(1,2,3\), all relevant matrix entries in rows 1 and 2 are nonzero. Two completely indistinguishable photons both from input 1 have normalized transition amplitude \(\sqrt2 U_{1j}U_{1k}=\sqrt2/4\). One photon from each of inputs 1 and 2 has amplitude \(U_{1j}U_{2k}+U_{1k}U_{2j}=1/(2\sqrt3)\). If all three photons are made completely indistinguishable, the normalized permanent for \((2,1,0,0)\to(1,1,1,0)\) is \(\sqrt6/8\). None is zero. The exact suppression at \(\phi=\pi\) therefore comes from interference between the two orthogonal internal configurations, not from a suppressed fully indistinguishable subset.

## Verification
The accompanying `verify.py` checks orthogonality of \(U\), expands the normalized bosonic creation operators in an output Fock basis, verifies \(P_{1110}(\phi)=(1+\cos\phi)/24\) at several benchmark phases, verifies the zero at \(\phi=\pi\), and checks that the relevant two- and three-photon fully indistinguishable amplitudes are nonzero. Its expected terminal line is `VERIFY_OK phase_zero=passed coherence_dependence=passed no_subset_suppression=passed`.

## Relationship to prior work
Shchesnovich, arXiv:1410.1506, develops the arbitrary fixed-occupation input state in Eq. (1) and conjectures that every exact zero for arbitrary multiphoton input comes from cancellation among completely indistinguishable photons and is independent of coherence among partially distinguishable photons. Bezerra and Shchesnovich, arXiv:2301.02192, still describe this as a conjecture and illustrate it for product inputs prepared from independent sources, including one partially distinguishable photon. Khalid et al., DOI:10.1103/PhysRevA.97.063802, allow arbitrary spatial occupations but explicitly assume a product input with distinguishability encoded by arrival times. Those settings do not imply the coherent internally entangled construction above.

## Limitations
The counterexample relies on coherent superposition between orthogonal internal occupation patterns at fixed spatial occupation. It does not refute a reformulated statement restricted to product internal states from independent sources, nor does it classify all zeros for correlated internal states. A residual literature risk is that an equivalent example may appear under representation-theoretic, immanant, or hidden-label terminology without citing the 2014 conjecture.

## References
1. V. S. Shchesnovich, “Partial indistinguishability theory for multi-photon experiments in multiport devices,” arXiv:1410.1506; Phys. Rev. A 91, 013844 (2015).
2. M. E. O. Bezerra and V. S. Shchesnovich, “Families of bosonic suppression laws beyond the permutation symmetry principle,” arXiv:2301.02192.
3. A. Khalid, D. Spivak, B. C. Sanders, and H. de Guise, “Permutational symmetries for coincidence rates in multimode multiphotonic interferometry,” Phys. Rev. A 97, 063802 (2018), DOI:10.1103/PhysRevA.97.063802.
