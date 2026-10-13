# Degeneracy breaks the claimed one-magnon Meyer–Wallach value

## Finding

For the four-site periodic isotropic Heisenberg Hamiltonian
\[
H_4=\sum_{j=1}^4\left(X_jX_{j+1}+Y_jY_{j+1}+Z_jZ_{j+1}\right),
\]
with indices modulo four, the one-excitation energy-zero eigenspace does not have a single Meyer–Wallach value. Let \(|j\rangle\), \(j\in\{0,1,2,3\}\), denote the computational basis state whose only \(1\) occurs at site \(j\), and define
\[
|\phi_+\rangle=\frac12\sum_{j=0}^3 i^j|j\rangle,
\qquad
|\phi_-\rangle=\frac12\sum_{j=0}^3 (-i)^j|j\rangle.
\]
These are the momentum \(\pm\pi/2\) one-magnon states. For every normalized
\[
|\psi\rangle=a|\phi_+\rangle+b|\phi_-\rangle,
\qquad |a|^2+|b|^2=1,
\]
one has
\[
\boxed{Q(\psi)=\frac34-\bigl[\operatorname{Re}(a\overline b)\bigr]^2.}
\]
Consequently the exact range on this single degenerate energy eigenspace is
\[
\boxed{\frac12\le Q\le\frac34.}
\]
The standing wave
\[
|\psi_*\rangle=\frac{|1000\rangle-|0010\rangle}{\sqrt2}
\]
is an exact zero-energy eigenstate with \(Q(\psi_*)=1/2\). Meyer and Wallach give \(Q=4(n-1)/n^2\) for one-excitation eigenstates, which equals \(3/4\) at \(n=4\). Thus that value is correct for their momentum eigenstates but not for arbitrary eigenvectors inside a degenerate energy eigenspace.

## Assumptions and scope

The Hamiltonian is exactly the periodic isotropic four-qubit Heisenberg Hamiltonian used by Meyer and Wallach, with the same Pauli normalization. The claim concerns the one-excitation sector and specifically its zero-energy two-dimensional eigenspace. It does not challenge the definition of the Meyer–Wallach measure, its local-unitary invariance, or the source calculation for an individual plane wave. It corrects only the extension from a translation-eigenbasis to all energy eigenvectors when the energy is degenerate.

The Meyer–Wallach measure is evaluated in the equivalent average-purity form
\[
Q(\psi)=2\left(1-\frac14\sum_{j=0}^3\operatorname{tr}\rho_j^2\right),
\]
where \(\rho_j\) is the one-qubit reduced state. Brennen proved this expression equivalent to the original polynomial definition.

## Proof

In the one-excitation basis, direct Pauli action gives
\[
H_4|j\rangle=2|j-1\rangle+2|j+1\rangle,
\]
where indices are modulo four. Therefore
\[
H_4|\phi_+\rangle=H_4|\phi_-\rangle=0.
\]
Because the two momentum states are orthonormal, every normalized \(|\psi\rangle=a|\phi_+\rangle+b|\phi_-\rangle\) is also a zero-energy eigenstate.

Let \(p_j\) be the probability that the excitation is at site \(j\). Expanding the two momentum amplitudes gives
\[
p_j=\frac14\left(1+2(-1)^j\operatorname{Re}(a\overline b)\right).
\]
A fixed-one-excitation state has no one-site coherence between \(|0\rangle\) and \(|1\rangle\), so
\[
\rho_j=\operatorname{diag}(1-p_j,p_j).
\]
For four qubits the average-purity formula reduces to
\[
Q=1-\sum_{j=0}^3p_j^2.
\]
Writing \(r=\operatorname{Re}(a\overline b)\), one obtains
\[
\sum_{j=0}^3p_j^2=\frac14+r^2,
\qquad
Q=\frac34-r^2.
\]
Cauchy gives \(|r|\le |a||b|\le1/2\), so \(1/2\le Q\le3/4\). Every value of \(r\) in \([-1/2,1/2]\) occurs, for example by taking real \(a=\cos\theta\) and \(b=\sin\theta\) with a suitable \(\theta\). Thus the interval is exact.

At \(a=b=1/\sqrt2\), the state reduces to \(|\psi_*\rangle\) above and \(Q=1/2\). At \(a=1,b=0\), it is a plane wave and \(Q=3/4\). Hence degeneracy, not any change of Hamiltonian or entanglement definition, is responsible for the discrepancy.

## Verification

The accompanying `verify_counterexample.py` uses only the Python standard library. It represents the one-excitation Hamiltonian exactly by its integer hopping action, checks that both momentum vectors and the standing-wave vector have zero energy, and evaluates the plane-wave and standing-wave Meyer–Wallach values as exact rational numbers. Its captured output is in `verification_output.txt`.

The infinite-looking part of the statement is only the continuous two-dimensional eigenspace formula; it is proved algebraically above. The finite checker verifies the two endpoint witnesses and the source value but is not used as a substitute for that proof.

## Relationship to prior work

Meyer and Wallach define \(Q\), then state that translation invariance makes the one-excitation eigenstates plane waves and report
\[
Q=\frac{4(n-1)}{n^2}.
\]
For higher excitation number they similarly write a value depending only on total \(S_z\). The four-site example isolates the missing qualification: a translation-invariant Hamiltonian admits a translation-eigenbasis, but an arbitrary vector in a degenerate energy eigenspace need not itself be a translation eigenvector.

Brennen later showed that \(Q\) is exactly the average one-qubit linear entropy, which makes the degeneracy dependence transparent through the site occupations. Ichikawa, Sasaki, and Tsutsui later analyze Meyer–Wallach values for symmetric \(W_k\)/Dicke states, but that symmetric-state calculation does not cover interference within the degenerate one-magnon energy eigenspace considered here.

Targeted searches for the source identifier, the claimed Heisenberg eigenstate formula, one-magnon degeneracy, standing-wave superpositions, and the exact four-site values did not locate a published correction or an implication-equivalent statement. The remaining originality risk is an obscure erratum, note, or unindexed discussion of the same degeneracy caveat.

## Limitations

The result does not classify all four-site energy eigenspaces, all excitation sectors, or all chain lengths. It gives a complete range only for the four-site zero-energy one-excitation eigenspace. It also does not claim that the Meyer–Wallach measure is defective as an entanglement monotone; the correction concerns the source's spectral evaluation under degeneracy.

## References

1. D. A. Meyer and N. R. Wallach, “Global entanglement in multiparticle systems,” arXiv:quant-ph/0108104; DOI: 10.1063/1.1497700.
2. G. K. Brennen, “An observable measure of entanglement for pure states of multi-qubit systems,” arXiv:quant-ph/0305094; DOI: 10.26421/QIC3.6-5.
3. T. Ichikawa, T. Sasaki, and I. Tsutsui, “Entanglement Measures for Intermediate Separability of Quantum States,” arXiv:0809.1932; DOI: 10.1103/PhysRevA.79.052307.
