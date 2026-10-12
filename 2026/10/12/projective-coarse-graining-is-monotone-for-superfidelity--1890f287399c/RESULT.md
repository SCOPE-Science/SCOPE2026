# Projective coarse-graining is monotone for superfidelity
## Finding
For finite-dimensional density matrices \(\rho\) and \(\sigma\), define the superfidelity
\[
G(\rho,\sigma)=\operatorname{Tr}(\rho\sigma)+\sqrt{1-\operatorname{Tr}(\rho^2)}\sqrt{1-\operatorname{Tr}(\sigma^2)}.
\]
Let \(\mathcal E\) be a trace-preserving, state-preserving Hilbert--Schmidt orthogonal projection on the real Hilbert space of Hermitian matrices. Then
\[
G(\mathcal E\rho,\mathcal E\sigma)\ge G(\rho,\sigma).
\]
This includes every nonselective projective measurement (pinching)
\[
\mathcal E(X)=\sum_i P_iXP_i
\]
for a complete family of mutually orthogonal projectors. Hence the projective-measurement monotonicity question posed in Eq. (29) of Mendonça et al. is affirmative even when neither state commutes with the projectors.

More precisely, set
\[
R=(I-\mathcal E)\rho,\qquad S=(I-\mathcal E)\sigma,
\]
and
\[
a=\sqrt{1-\operatorname{Tr}(\rho^2)},\qquad b=\sqrt{1-\operatorname{Tr}(\sigma^2)}.
\]
Then
\[
G(\mathcal E\rho,\mathcal E\sigma)-G(\rho,\sigma)
=\sqrt{a^2+\lVert R\rVert_2^2}\sqrt{b^2+\lVert S\rVert_2^2}-ab-\operatorname{Tr}(RS).
\]
The right-hand side is the Cauchy--Schwarz deficit between the direct-sum Hilbert-space vectors \((a,R)\) and \((b,S)\). Equality holds exactly when those vectors are positively linearly dependent, with a zero vector allowed.

## Assumptions and scope
All Hilbert spaces are finite dimensional. Density matrices are positive semidefinite with unit trace. The Hilbert--Schmidt inner product on Hermitian matrices is \(\langle X,Y\rangle_2=\operatorname{Tr}(XY)\), with norm \(\lVert X\rVert_2=\sqrt{\operatorname{Tr}(X^2)}\).

The map \(\mathcal E\) is assumed to be an orthogonal projection for this inner product, to preserve trace, and to map density matrices to density matrices. These assumptions include projective pinching and, more generally, finite-dimensional trace-preserving Hilbert--Schmidt conditional expectations. The statement does not claim monotonicity of superfidelity under arbitrary completely positive trace-preserving maps; Mendonça et al. give counterexamples to such unrestricted monotonicity.

## Proof
Because \(\mathcal E\) is an orthogonal projection, write
\[
\rho=\mathcal E\rho+R,\qquad \sigma=\mathcal E\sigma+S,
\]
with \(R,S\) orthogonal to the range of \(\mathcal E\). Orthogonality gives
\[
\operatorname{Tr}(\rho^2)=\operatorname{Tr}((\mathcal E\rho)^2)+\lVert R\rVert_2^2,
\]
\[
\operatorname{Tr}(\sigma^2)=\operatorname{Tr}((\mathcal E\sigma)^2)+\lVert S\rVert_2^2,
\]
and
\[
\operatorname{Tr}(\rho\sigma)=\operatorname{Tr}((\mathcal E\rho)(\mathcal E\sigma))+\operatorname{Tr}(RS).
\]
Therefore
\[
1-\operatorname{Tr}((\mathcal E\rho)^2)=a^2+\lVert R\rVert_2^2,
\qquad
1-\operatorname{Tr}((\mathcal E\sigma)^2)=b^2+\lVert S\rVert_2^2.
\]
Substitution into the definition of \(G\) yields the exact difference formula in the finding.

Now work in the real Hilbert direct sum \(\mathbb R\oplus\mathsf H_{\mathrm{HS}}\). Its inner product gives
\[
\langle (a,R),(b,S)\rangle=ab+\operatorname{Tr}(RS),
\]
while the norms are
\[
\lVert(a,R)\rVert=\sqrt{a^2+\lVert R\rVert_2^2},\qquad
\lVert(b,S)\rVert=\sqrt{b^2+\lVert S\rVert_2^2}.
\]
Cauchy--Schwarz therefore gives the required nonnegativity. Equality in Cauchy--Schwarz at the upper bound occurs exactly when the two direct-sum vectors are positively linearly dependent, allowing either vector to vanish.

For a projective measurement, \(\mathcal E(X)=\sum_iP_iXP_i\) is trace preserving, state preserving, idempotent, and self-adjoint for the Hilbert--Schmidt inner product, hence it is an orthogonal projection and the theorem applies.

## Verification
The proof uses no finite enumeration or numerical approximation. The critical checks are: (i) the pinching map is a Hilbert--Schmidt orthogonal projection; (ii) the Pythagorean identities for purity and overlap follow from the range/kernel orthogonality; and (iii) the resulting difference is exactly one Cauchy--Schwarz deficit in a direct-sum real Hilbert space. These steps cover arbitrary finite dimension and arbitrary noncommuting input states.

The equality statement was checked against the same direct-sum reduction: no additional equality condition is hidden because the proof contains only identities followed by a single Cauchy--Schwarz inequality.

## Relationship to prior work
Miszczak et al. introduced superfidelity as an easily computed upper bound on the Uhlmann--Jozsa fidelity and established its basic structural properties. Mendonça et al. independently studied the same quantity, showed that it is not monotone under arbitrary quantum operations, and then explicitly asked whether arbitrary nonselective projective measurements nevertheless always increase it. Their Eq. (29) states exactly that inequality, notes the commuting special case, and reports numerical evidence for the general noncommuting case.

The present result supplies a dimension-independent analytic proof of that stated projective-measurement inequality and strengthens it from projective pinching to every state-preserving Hilbert--Schmidt orthogonal projection. The checked literature did not reveal a later source proving this exact statement. A 2015 paper on preservers of fidelity and superfidelity was located, but only its abstract was available in the bounded literature check; that abstract concerns maps that preserve the quantities exactly, not monotonicity under pinching. This remains a residual literature risk rather than evidence of coverage.

## Limitations
The theorem concerns orthogonal coarse-grainings. It does not restore monotonicity of superfidelity under arbitrary quantum channels, which is false. No claim is made about selective measurements with outcomes retained or averaged branchwise, nor about infinite-dimensional extensions where Hilbert--Schmidt and domain issues require separate hypotheses.

## References
1. J. A. Miszczak, Z. Puchała, P. Horodecki, A. Uhlmann, and K. Życzkowski, “Sub- and super-fidelity as bounds for quantum fidelity,” arXiv:0805.2037; Quantum Information and Computation 9 (2009), 103--130, DOI:10.26421/QIC9.1-2-7.
2. P. E. M. F. Mendonça, R. d. J. Napolitano, M. A. Marchiolli, C. J. Foster, and Y.-C. Liang, “Alternative fidelity measure between quantum states,” arXiv:0806.1150; Physical Review A 78 (2008), 052330, DOI:10.1103/PhysRevA.78.052330.
3. L. Wang, J. Hou, and K. He, “Fidelity, sub-fidelity, super-fidelity and their preservers,” International Journal of Quantum Information 13 (2015), 1550027, DOI:10.1142/S0219749915500276.
