# A state-dependent degradation cone for the two-vs-two qubit correlation tradeoff
## Finding
Let
\[
|\psi\rangle=\sqrt{\lambda}|00\rangle+\sqrt{1-\lambda}|11\rangle
\]
be a pure two-qubit state in Schmidt form, and let
\[
C=2\sqrt{\lambda(1-\lambda)},\qquad r=2\lambda-1,
\]
so that \(C^2+r^2=1\). Consider rank-one projective measurements with outcomes \(x,y\in\{+1,-1\}\). Assume Alice's measurement is Schmidt-unbiased, meaning its Bloch axis is \(a=(a_x,a_y,0)\), and write Bob's axis as \(b=(b_x,b_y,b_z)\). Define
\[
t=a_xb_x-a_yb_y,\qquad u=r b_z.
\]
Then Alice's outcome is uniform and the induced binary channel is
\[
W_C(y\mid x)=\frac12\bigl(1+y u+xyCt\bigr).
\]
For the maximally entangled state \(|\Phi^+\rangle\) in the same local frame, the same measurement pair gives
\[
W_1(y_0\mid x)=\frac12\bigl(1+xy_0t\bigr).
\]

If \(t=0\), then \(W_C\) is independent of \(x\), so it is trivially a stochastic post-processing of \(W_1\). If \(t\ne0\), then \(W_C\) is a stochastic post-processing of \(W_1\) if and only if
\[
|u|+C\le1.
\]
Since \(|r|=\sqrt{1-C^2}\), this condition is equivalently
\[
|b_z|\le\sqrt{\frac{1-C}{1+C}}.
\]
Therefore, throughout this exact degradation cone,
\[
I_{\psi}(A:B)\le I_{\Phi^+}(A:B).
\]

Consequently, take two measurement pairs \((A^{(1)},B^{(1)})\) and \((A^{(2)},B^{(2)})\). If both Alice bases are Schmidt-unbiased and, for each \(j\), either \(t_j=0\) or Bob's Schmidt-axis component obeys
\[
|b_{j,z}|\le\sqrt{\frac{1-C}{1+C}},
\]
then the two-vs-two conjectured inequality of Grudka et al. is valid for the state \(|\psi\rangle\):
\[
I(A^{(1)}:B^{(1)})+I(A^{(2)}:B^{(2)})\le 2+\log_2 c'.
\]
Here \(c'\) is exactly the basis-overlap parameter appearing in that source. The statement is symmetric under interchanging Alice and Bob. At \(C=1\), the source's maximally-entangled theorem already gives the inequality without any cone restriction.

## Assumptions and scope
All mutual informations are Shannon mutual informations in bits. The state is pure and two-dimensional on each side. Measurements are binary rank-one projective measurements. A Schmidt-unbiased basis means that both basis vectors have squared overlap \(1/2\) with each vector of the chosen local Schmidt basis, equivalently that the measurement Bloch axis has zero Schmidt-\(z\) component.

For a nonmaximally entangled state the Schmidt axis is fixed up to signs and phases. The condition is sufficient for the two-vs-two inequality and is exact only for the stated same-measurement binary-degradation mechanism when \(t\ne0\). It is not claimed to characterize all measurement pairs for which the mutual-information inequality happens to hold.

## Proof
The Schmidt-form correlation tensor of \(|\psi\rangle\) in the Pauli frame is
\[
T=\operatorname{diag}(C,-C,1),
\]
and each reduced Bloch vector is \((0,0,r)\). Hence the joint law of projective outcomes is
\[
p_C(x,y)=\frac14\left(1+xr a_z+yr b_z+xy\,a^{\mathsf T}Tb\right).
\]
Because \(a_z=0\), Alice is uniform and \(a^{\mathsf T}Tb=C(a_xb_x-a_yb_y)=Ct\). Dividing by \(p_C(x)=1/2\) gives
\[
W_C(y\mid x)=\frac12(1+yu+xyCt).
\]
For \(|\Phi^+\rangle\), the local Bloch vectors vanish and the correlation tensor is \(\operatorname{diag}(1,-1,1)\), so the same Alice axis gives
\[
W_1(y_0\mid x)=\frac12(1+xy_0t).
\]

Assume first that \(t\ne0\). Any binary stochastic post-processing from \(y_0\) to \(y\) can be written in expectation form
\[
\mathbb E[y\mid y_0]=\alpha+\beta y_0,
\]
with stochasticity equivalent to \(|\alpha+\beta|\le1\) and \(|\alpha-\beta|\le1\). If it maps \(W_1\) to \(W_C\), comparison of the two conditional means for \(x=\pm1\) forces
\[
\alpha=u,\qquad \beta=C.
\]
Thus such a post-processing exists if and only if \(|u|+C\le1\). When this holds, it is explicitly
\[
K(y\mid y_0)=\frac12\bigl(1+y(u+Cy_0)\bigr).
\]
A direct summation gives
\[
\sum_{y_0}K(y\mid y_0)W_1(y_0\mid x)
=\frac12(1+yu+xyCt)=W_C(y\mid x).
\]
If \(t=0\), both conditional rows of \(W_C\) coincide, so an input-forgetting post-processing exists regardless of \(b_z\).

Finally,
\[
|u|+C=|r b_z|+C\le1
\]
is, for \(C<1\), equivalent to
\[
|b_z|\le\frac{1-C}{\sqrt{1-C^2}}=\sqrt{\frac{1-C}{1+C}}.
\]
The data-processing inequality for classical mutual information now gives the pointwise comparison with the same measurement pair on \(|\Phi^+\rangle\).

Grudka et al. prove their two-vs-two bound for every maximally entangled state. Applying the pointwise comparison separately to the two measurement pairs and then their theorem yields the displayed two-vs-two inequality for the stated cone. Swapping the parties gives the symmetric version.

## Verification
The proof is algebraic and does not rely on finite sampling. The accompanying `artifacts/verify.py` independently checks the Schmidt-form joint probabilities against direct amplitudes, verifies the stochastic-kernel identity on a deterministic parameter grid, checks the cone equivalence, and confirms the mutual-information data-processing inequality numerically as a supplementary stress test. These computations are not used to replace the analytic proof.

The only external theorem used in the final step is the maximally-entangled two-vs-two inequality proved as Theorem 3 in the 2013 source. Its relevant theorem and the subsequent discussion of the nonmaximally entangled open case were inspected directly.

## Relationship to prior work
Grudka, Horodecki, Horodecki, Horodecki, Kłobus, and Pankowski introduced the two-vs-two complementary-correlation inequality, reported numerical tests in dimensions two and three, and proved it for maximally entangled states. Immediately after that theorem they asked about nonmaximally entangled states and showed that the most direct unrestricted comparison with the corresponding maximally entangled state can fail for tilted measurements.

Seiler, Strohm, and Schleich later gave an explicit Bloch-sphere formula for projective-measurement mutual information of a pure two-qubit state and identified the Schmidt correlation tensor \(\operatorname{diag}(C,-C,1)\). Their optimization concerns the best opposing measurement for a fixed uniform measurement; it does not state the same-measurement degradation cone above or transfer the 2013 two-vs-two theorem to this state-dependent sector.

The present result identifies an exact Blackwell/degradation boundary for the failed same-measurement proof strategy when one side is Schmidt-unbiased. It therefore gives a continuous nonmaximally-entangled sector in which the stronger pointwise route is valid, while making no claim outside that sector.

## Limitations
The theorem does not prove the full 2013 conjecture for arbitrary nonmaximally entangled states or arbitrary measurement bases. The cone is exact for existence of the stated binary post-processing when \(t\ne0\), not for the truth of the mutual-information inequality itself. The result is restricted to pure two-qubit states and rank-one projective measurements. No mixed-state, POVM, higher-dimensional, or multipartite extension is asserted.

## References
1. A. Grudka, M. Horodecki, P. Horodecki, R. Horodecki, W. Kłobus, and Ł. Pankowski, *Conjectured strong complementary-correlations tradeoff*, arXiv:1210.8317v1; Phys. Rev. A 88, 032106 (2013), DOI:10.1103/PhysRevA.88.032106.
2. J. Seiler, T. Strohm, and W. P. Schleich, *Estimating the privacy of quantum-random numbers*, arXiv:2005.05675; New J. Phys. 22, 093063 (2020), DOI:10.1088/1367-2630/abac73.
3. MSC2020 81P40, Quantum coherence, entanglement, quantum correlations.
