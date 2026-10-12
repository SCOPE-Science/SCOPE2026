# Joint state–measurement likelihood in partial-information discrimination is not jointly concave

## Finding

Ježek's partial-information discrimination scheme maximizes a log-likelihood jointly over unknown states and a discrimination POVM. The paper states that convexity of the log-likelihood guarantees only one global maximum or a plateau. For the joint state-and-measurement problem, that convexity claim fails already on a two-parameter commuting-qubit slice.

Let
\[
\rho_1(p)=\operatorname{diag}(p,1-p),
\qquad
\rho_2=\frac{I}{2},
\qquad 0<p<1,
\]
and let the two-outcome discrimination POVM be
\[
\Pi_1(q)=\operatorname{diag}(q,1-q),
\qquad
\Pi_2(q)=I-\Pi_1(q),
\qquad 0<q<1.
\]
For the calibration of \(\rho_1\), take the fixed computational-basis measurement with normalized frequencies \(1/2,1/2\). Fix all calibration information for \(\rho_2\).

The source discrimination term for label \(1\) contains
\[
\ell_{11}(p,q)=\log s(p,q),
\qquad
s(p,q)=1-p-q+2pq.
\]
The label-\(2\) discrimination term is constant on this slice because
\[
\operatorname{tr}(\rho_2\Pi_2)=\frac12.
\]
The chosen calibration contribution for \(\rho_1\) is
\[
\ell_{\mathrm{cal}}(p)=\frac12\log p+\frac12\log(1-p).
\]
Therefore, at \(p=q=1/2\), the Hessian of the full restricted log-likelihood is
\[
H=\begin{pmatrix}-4&4\\4&0\end{pmatrix}.
\]
Its determinant is \(-16<0\), and its eigenvalues are \(-2-2\sqrt5\) and \(-2+2\sqrt5\). Hence the joint objective is neither concave nor convex.

The conclusion is structural: concavity available when a quantum state is optimized with a fixed measurement, or when a measurement is optimized with fixed states, does not extend to the simultaneous likelihood because \(\operatorname{tr}(\rho\Pi)\) is bilinear in the two unknowns. Consequently, convexity cannot by itself certify global uniqueness or global convergence of the source's simultaneous iteration.

## Assumptions and scope

The result concerns the likelihood and iteration introduced in Ježek's 2002 partial-information discrimination protocol. The state and POVM constraints are enforced directly by the parametrization above: both density matrices are positive and trace one, both POVM elements are positive, and \(\Pi_1+\Pi_2=I\).

The calibration measurement is fixed, as in the source protocol. Its two outcomes have strictly positive probabilities at \(p=1/2\), so the likelihood and Hessian are finite. The normalized calibration frequencies \(1/2,1/2\) are a valid data choice.

The theorem is a curvature obstruction. It does not claim that every data set has multiple optima, that the source iteration diverges, or that its numerical examples are wrong. It only rules out the stated joint-convexity route to a universal global-optimality guarantee.

## Proof

For the feasible slice,
\[
s(p,q)=\operatorname{tr}(\rho_1(p)\Pi_1(q))=pq+(1-p)(1-q)=1-p-q+2pq.
\]
At \(p=q=1/2\),
\[
s=\frac12,\qquad \partial_p s=\partial_q s=0,\qquad \partial_{pq}s=2.
\]
Thus
\[
\partial_{pp}\log s=0,\qquad \partial_{qq}\log s=0,\qquad \partial_{pq}\log s=4.
\]
For the calibration term,
\[
\ell_{\mathrm{cal}}(p)=\frac12\log p+\frac12\log(1-p),
\]
so \(\ell_{\mathrm{cal}}''(1/2)=-4\). It has no \(q\)-dependence. The second state's discrimination probability is constant:
\[
\operatorname{tr}(\rho_2\Pi_2(q))=\frac12\operatorname{tr}\Pi_2(q)=\frac12.
\]
All fixed calibration terms for \(\rho_2\) are also constant on this slice. Summing the second derivatives yields the displayed matrix \(H\).

Because \(\det H=-16\), the Hessian is indefinite at an interior feasible point. A twice differentiable concave function has negative-semidefinite Hessian at every interior point, while a twice differentiable convex function has positive-semidefinite Hessian. The source joint likelihood therefore has neither property in general.

## Verification

The standalone script `artifacts/verify.py` reconstructs the feasible qubit slice with exact rational arithmetic. It checks \(s(1/2,1/2)=1/2\), the mixed curvature \(\partial_{pq}\log s=4\), the calibration curvature \(-4\), and the full Hessian determinant \(-16\). The executed package path returned:

`VERIFY_OK H=[[-4,4],[4,0]] determinant=-16 trace=-4 eigenvalues=-2+-2sqrt(5)`

The script is supplementary; the proof is the exact derivative calculation above.

## Relationship to prior work

Ježek introduced the joint likelihood, derived the coupled extremal equations, proposed iteration, and stated that convexity guarantees a single global maximum or a plateau. The same article supplies the simultaneous state-and-POVM setting to which the counterexample applies.

Later maximum-likelihood quantum-state-estimation literature often invokes convexity when the measurement is fixed. That setting does not imply joint concavity here: fixing one factor removes the bilinearity in \(\operatorname{tr}(\rho\Pi)\), while the source protocol optimizes both factors simultaneously.

Modern self-calibrating tomography likewise treats state and device parameters jointly and emphasizes the additional structure of simultaneous estimation. Targeted searches did not locate a published statement applying the explicit Hessian obstruction above to Ježek's 2002 discrimination likelihood or correcting its convexity-based uniqueness sentence.

## Limitations

Indefinite curvature invalidates a universal convexity or concavity certificate; it does not, by itself, exhibit a spurious local maximum of the full iteration. A different argument could still establish convergence or global optimality under additional assumptions or for particular data sets.

The counterexample uses commuting qubit states and a diagonal POVM, so it does not rely on noncommutativity. It does not classify the global landscape of the full matrix problem.

A residual literature risk remains that a later optimization or tomography paper may note the same source-specific issue under different terminology.

## References

1. M. Ježek, “Discrimination between non perfectly known states,” arXiv:quant-ph/0202085, first submitted 15 February 2002; *Physics Letters A* 299 (2002), 441–446, DOI: 10.1016/S0375-9601(02)00775-2.
2. Z. Hradil, J. Řeháček, J. Fiurášek, and M. Ježek, “Maximum-Likelihood Methods in Quantum Mechanics,” in *Quantum State Estimation* (2004), DOI: 10.1007/978-3-540-44481-7_3.
3. J. Shang et al., “Proper error bars for self-calibrating quantum tomography,” *Physical Review A* 100 (2019), 022333, DOI: 10.1103/PhysRevA.100.022333.
