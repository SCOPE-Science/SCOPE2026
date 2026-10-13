# The unrooted three-qubit entropy product fails average LOCC monotonicity
## Finding
For a three-qubit pure state, let \(E_i=-\operatorname{Tr}(\rho_i\log_2\rho_i)\) be the one-qubit entropy and consider the unrooted product
\[
S_E=E_1E_2E_3.
\]
The state
\[
|\psi\rangle=\sqrt{\frac18}|000\rangle+\sqrt{\frac78}|111\rangle
\]
has \(E_1=E_2=E_3=h_2(1/8)\), so \(S_E(\psi)=h_2(1/8)^3\). A single local two-outcome measurement on the first qubit, with
\[
K_1=|0\rangle\langle0|+\frac1{\sqrt7}|1\rangle\langle1|,
\qquad
K_2=\sqrt{\frac67}|1\rangle\langle1|,
\]
raises the expected value of \(S_E\) strictly: the postmeasurement average is exactly \(1/4\), whereas the input value is smaller than \(125/512<1/4\). Thus this raw entropy product is not a strong, or average, LOCC entanglement monotone.

## Assumptions and scope
The claim concerns normalized pure states of three qubits and base-two von Neumann entropies of the one-qubit reductions. Strong LOCC monotonicity means that for every local instrument producing pure conditional states \(|\psi_j\rangle\) with probabilities \(q_j\), one must have \(\sum_j q_j S_E(\psi_j)\le S_E(\psi)\).

The claim is specifically about the unrooted product \(S_E=\prod_i E_i\) discussed as a good three-qubit entanglement measure in the motivating paper. It does not claim that the later geometric-mean multiple-entropy components \(S_i\) fail monotonicity.

## Proof
The measurement is valid because
\[
K_1^\dagger K_1+K_2^\dagger K_2=I.
\]
On \(|\psi\rangle\), the first outcome has unnormalized state
\[
\sqrt{\frac18}|000\rangle+\sqrt{\frac78}\frac1{\sqrt7}|111\rangle
=\sqrt{\frac18}(|000\rangle+|111\rangle),
\]
so its probability is \(q_1=1/4\) and its normalized state is the GHZ state \((|000\rangle+|111\rangle)/\sqrt2\). Every one-qubit reduction of that branch is maximally mixed, hence \(S_E=1\).

The second outcome has probability \(q_2=3/4\) and normalized state \(|111\rangle\), hence \(S_E=0\). Therefore
\[
\sum_j q_j S_E(\psi_j)=\frac14.
\]
For the input,
\[
h_2(1/8)=3-\frac78\log_2 7.
\]
The integer inequality \(2^{19}<7^7\) implies \(\log_2 7>19/7\), and consequently
\[
h_2(1/8)<3-\frac78\frac{19}7=\frac58.
\]
Thus
\[
S_E(\psi)=h_2(1/8)^3<\left(\frac58\right)^3=\frac{125}{512}<\frac14.
\]
This is a strict average increase under a local measurement.

## Verification
The standalone script `artifacts/verify.py` checks the Kraus completeness conditions through their exact squared diagonal entries, the two branch probabilities, the GHZ/product branch values, the exact integer witness \(2^{19}<7^7\), and the rational comparison \(125/512<1/4\). Its recorded output is `artifacts/verification_output.txt` and begins with `VERIFY_OK`.

No numerical approximation is needed for the proof. The reported floating-point input value is only a diagnostic.

## Relationship to prior work
Liu, Zhao, and Long list LOCC nonincrease among the basic requirements for an entanglement measure and state that the unrooted product of one-qubit entropies gives a good measure for a three-qubit pure system before introducing their geometric-mean multiple-entropy quantities. The counterexample above separates these two constructions: it invalidates strong monotonicity of the raw product, not of the geometric mean.

Later work on geometric means of bipartite entanglement monotones proves strong monotonicity by exploiting concavity of the geometric mean together with strong monotonicity of its factors. That mechanism is inapplicable to the raw product because the product itself is not concave on the relevant positive cube. No implication-equivalent published counterexample to this specific three-qubit entropy product was found in the checked literature.

## Limitations
This is a pure-state, three-qubit counterexample to average LOCC monotonicity. It does not classify all local instruments that increase the raw product, does not address mixed-state convex-roof constructions, and does not challenge the distinct geometric-mean MEMS quantities. The literature search cannot exclude an unindexed or differently phrased earlier observation.

## References
1. D. Liu, X. Zhao, and G.-L. Long, “Multiple Entropy Measures for Multipartite Quantum Entanglement,” arXiv:0705.3904, first public 2007-05-26; published as “Multiple entropy measures for multi-particle pure quantum state,” Communications in Theoretical Physics 54, 825–828, DOI:10.1088/0253-6102/54/5/09.
2. Y. Li and J. Shang, “Geometric mean of bipartite concurrences as a genuine multipartite entanglement measure,” Physical Review Research 4, 023059 (2022), DOI:10.1103/PhysRevResearch.4.023059.
