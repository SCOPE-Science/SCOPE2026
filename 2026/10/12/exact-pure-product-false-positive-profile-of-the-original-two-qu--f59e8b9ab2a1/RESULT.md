# Exact pure-product false-positive profile of the original two-qubit Kitagawa–Ueda squeezing parameters
## Finding
For every pure two-qubit product state \(|a\rangle\otimes|b\rangle\) with unit Bloch vectors \(\mathbf a,\mathbf b\in S^2\), suppose \(\mathbf a+\mathbf b\ne0\) and write
\[
\gamma=\arccos(\mathbf a\cdot\mathbf b)\in[0,\pi).
\]
For the original collective Kitagawa–Ueda and Wineland squeezing parameters used in the cited source,
\[
\xi_1=\cos(\gamma/2),\qquad \xi_2=1.
\]
Consequently every nonidentical nonantipodal product state, \(0<\gamma<\pi\), satisfies \(\xi_1<1\) although it is unentangled. Moreover \(\xi_1\) can be arbitrarily close to zero as \(\gamma\to\pi\). The Wineland parameter remains exactly on the unsqueezed boundary, \(\xi_2=1\), throughout this pure-product family.

## Assumptions and scope
There are exactly two qubits, \(N=2\), and the state is a pure product. Let \(\boldsymbol\sigma^{(1)}\) and \(\boldsymbol\sigma^{(2)}\) be the Pauli vectors and
\[
\mathbf J=\frac12\left(\boldsymbol\sigma^{(1)}+\boldsymbol\sigma^{(2)}\right).
\]
The parameters are the original collective definitions
\[
\xi_1=\frac{2(\Delta J_\perp)_{\min}}{\sqrt N},\qquad
\xi_2=\frac{\sqrt N(\Delta J_\perp)_{\min}}{|\langle\mathbf J\rangle|},
\]
where the variance is minimized over directions perpendicular to the collective mean. The antipodal case \(\mathbf a+\mathbf b=0\) is excluded because the collective mean direction and \(\xi_2\) are undefined there. No claim is made for mixed states, more than two qubits, or locally invariant replacements for these original collective parameters.

## Proof
Put \(c=\mathbf a\cdot\mathbf b\). Product-state factorization gives
\[
\langle\mathbf J\rangle=\frac{\mathbf a+\mathbf b}{2},
\qquad
|\langle\mathbf J\rangle|=\sqrt{\frac{1+c}{2}}.
\]
For any unit vector \(\mathbf n\perp(\mathbf a+\mathbf b)\), the variance has no inter-qubit covariance term, so
\[
(\Delta J_{\mathbf n})^2
=\frac14\left(1-(\mathbf a\cdot\mathbf n)^2\right)
 +\frac14\left(1-(\mathbf b\cdot\mathbf n)^2\right).
\]
Transversality implies \(\mathbf b\cdot\mathbf n=-\mathbf a\cdot\mathbf n\). The vector \(\mathbf a-\mathbf b\) is perpendicular to \(\mathbf a+\mathbf b\), and for \(c<1\) its normalized direction maximizes the transverse projection, with
\[
\max_{\mathbf n\perp(\mathbf a+\mathbf b)}(\mathbf a\cdot\mathbf n)^2=\frac{1-c}{2}.
\]
(The case \(c=1\) follows directly because either transverse direction has zero projection.) Therefore
\[
(\Delta J_\perp)^2_{\min}
=\frac12-\frac{1-c}{4}
=\frac{1+c}{4}.
\]
Substitution at \(N=2\) yields
\[
\xi_1=\sqrt{\frac{1+c}{2}},
\qquad
\xi_2=1.
\]
Since \(c=\cos\gamma\) and \(\gamma\in[0,\pi)\), the half-angle identity gives \(\xi_1=\cos(\gamma/2)\). Thus \(0<\gamma<\pi\) is exactly the false-positive region for the original condition \(\xi_1<1\), and \(\xi_1\to0\) as \(\gamma\to\pi\).

## Verification
The accompanying `verify.py` independently evaluates the variance minimizer in a canonical Bloch-plane parametrization over representative values of \(c\), checks the closed forms for \(\xi_1\), \(\xi_2\), and the minimum variance, reproduces the source's explicit product example, and probes the approach to the antipodal endpoint. Its recorded output is `VERIFY_OK`.

The source's explicit product example has Bloch-vector inner product \(c=-1/2\), hence \(\gamma=2\pi/3\). The formula gives \(\xi_1=1/2\) and \(\xi_2=1\), agreeing with the value discussed in the source and later review.

## Relationship to prior work
The 2003 source introduced a locally invariant spin-squeezing criterion after observing that the original Kitagawa–Ueda parameter can label a nonsymmetric product state as squeezed. It gives a concrete two-qubit product example but does not state the complete angular profile above. A later review repeats that example and the qualitative warning that nonsymmetric product states can exhibit original spin squeezing. The present result sharpens that warning into an exact classification: every nonidentical nonantipodal pure product state is a false positive for \(\xi_1<1\), the false-positive value ranges down arbitrarily close to zero, and \(\xi_2\) is identically one on the entire nonantipodal pure-product family.

## Limitations
This result is specific to pure two-qubit product states and to the original collective parameters. It does not challenge the source's locally invariant criterion, does not classify mixed separable states, and does not extend the formula to \(N>2\). The endpoint \(\gamma=\pi\) is a limiting statement only because the collective mean vanishes there.

## References
A. R. Usha Devi, X. Wang, and B. C. Sanders, “Spin squeezing criterion with local unitary invariance,” arXiv:quant-ph/0304051; DOI:10.1023/B:QINP.0000004125.12489.F4.

A. R. Usha Devi and Sudha, “Spin Squeezing and Quantum Correlations,” arXiv:1101.0308.
