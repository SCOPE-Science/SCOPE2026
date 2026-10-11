# Harmonic eigenspace multiplicities for positive contraction semigroups

## Finding

**Theorem.** Let \(E\) be a complex Banach lattice that is monotonically complete and has the Fatou property. Let \((T_t)_{t\geq 0}\) be a positive, contractive, strongly continuous semigroup on \(E\), with generator \(A\). For every real number \(\beta\) and every integer \(k\),

\[
\dim\ker(A-i\beta I)\ \leq\ \dim\ker(A-ik\beta I).
\]

The dimensions here are finite nonnegative integers or \(\infty\); different infinite cardinalities are not distinguished. Thus, in particular, every imaginary generator eigenvalue propagates to all integer harmonics with no loss of **finite geometric multiplicity**. The inequality may be strict.

## Assumptions and scope

A complex Banach lattice is **monotonically complete** when each norm-bounded increasing net of positive real vectors has a supremum in the lattice; it has the **Fatou property** when the norm of any existing supremum of an increasing positive net is the supremum of its norms. Positivity means \(T_t(E_+)\subseteq E_+\), contractivity means \(\|T_t\|\leq 1\), and strong continuity means \(\lim_{t\downarrow0}T_t x=x\) in norm for each \(x\in E\). The generator has domain consisting of vectors for which \(\lim_{t\downarrow0}(T_t x-x)/t\) exists in norm.

The theorem concerns geometric eigenspaces, not generalized eigenspaces, approximate eigenvectors, or the full spectrum. In particular, the zero-dimensional case is included.

## Proof

If \(\beta=0\), both eigenspaces coincide. Fix \(\beta\neq 0\), and set \(\tau=2\pi/|\beta|\) and \(F=\ker(T_\tau-I)\). By Glück's fixed-space theorem [1, Theorem 3.1], \(F\), with its inherited norm and order, is a Dedekind-complete complex Banach lattice. This is important: \(F\) need not be a sublattice of the original \(E\); its lattice operations are those of the inherited order on \(F\).

Each \(T_s\) leaves \(F\) invariant because the semigroup is commutative. For \(0\leq s\leq\tau\), the restriction \(U_s=T_s|_F\) is positive and its inverse is \(T_{\tau-s}|_F\): both products equal \(T_\tau|_F=I_F\). The inverse is positive, so \(U_s\) is an order isomorphism and therefore a lattice automorphism. These operators form a strongly continuous group with period \(\tau\), when extended periodically to all real parameters.

Choose \(a\in(0,\tau)\) such that \(a/\tau\) is irrational. Write \(U=T_a|_F\) and \(\lambda=e^{i\beta a}\). For **every integer** \(j\), we claim the exact eigenspace identity

\[
\ker(U-\lambda^jI_F)=\ker(A-ij\beta I_E).
\]

The right-hand side is contained in \(F\), since \(T_t x=e^{ij\beta t}x\) for a generator eigenvector and \(e^{ij\beta\tau}=1\); such a vector is also an eigenvector of \(U\) with eigenvalue \(\lambda^j\).

Conversely, suppose \(x\in F\) and \(Ux=\lambda^j x\). Then for every nonnegative integer \(m\), \(T_{ma}x=e^{ij\beta ma}x\). The residues of \(ma\) modulo \(\tau\) are dense in the circle of circumference \(\tau\). Since \(T_{t+\tau}x=T_tx\) for \(x\in F\), strong continuity therefore gives \(T_tx=e^{ij\beta t}x\) for each \(0\leq t\leq\tau\), and hence for all \(t\geq0\). Taking the right derivative at zero proves that \(x\in D(A)\) and \(Ax=ij\beta x\), completing the eigenspace identity. The same argument covers \(j=0\) and negative \(j\).

The order-complete lattice \(F\) and the lattice homomorphism \(U\) satisfy the precise hypotheses of [2, Proposition 3.1(b)]. That result, whose dimension step is proved by normalized lattice powers and finite linear independence in [2, Appendix A, Lemma A.4], gives

\[
\dim\ker(U-\lambda I_F)\leq\dim\ker(U-\lambda^kI_F)
\qquad(k\in\mathbb Z).
\]

Substitute the two exact eigenspace identities, for \(j=1\) and \(j=k\), to obtain the theorem.

**Strictness example.** On \(E=L_1(\mathbb T;\mathbb C)\oplus_1 L_1(\mathbb T;\mathbb C)\), use normalized Haar measure and the positive isometric strongly continuous semigroup

\[
T_t(f,g)(\theta)=(f(\theta+t),g(\theta+2t)).
\]

The generator has Fourier eigenvectors of frequencies \(in\) on the first summand and \(2in\) on the second, where \(n\in\mathbb Z\). Every such Fourier eigenspace on one summand is one-dimensional. Consequently, \(\dim\ker(A-iI)=1\) whereas \(\dim\ker(A-2iI)=2\). The space \(E\) is a \(KB\)-lattice, hence it meets both hypotheses [1, Examples 2.2]. By taking just one translation summand, equality holds at every harmonic.

## Verification

The argument is entirely analytic; no finite computation substitutes for an infinite-dimensional implication. The critical verifications are: (i) [1, Theorem 3.1] supplies **Dedekind completeness of the fixed space with inherited norm**, (ii) positive inverses make the restricted operators lattice automorphisms, (iii) irrational sampling and strong continuity give equality of the **whole** eigenspaces, not just inclusion, and (iv) [2, Proposition 3.1(b)] applies to the resulting lattice homomorphism. Its proof and supporting finite-dimension Lemma A.4 were checked in the full open text. The two-speed translation example verifies strictness by Fourier eigenfunction identities, without a numerical approximation.

## Relationship to prior work

Glück [1, Corollary 3.5] establishes qualitative cyclicity of the imaginary point spectrum for the same positive contractive semigroups, but does **not** assert a multiplicity bound; the paragraph immediately after that corollary explicitly suggests such a bound and identifies the absence of a convenient semigroup analogue of [2, Proposition 3.1] as an obstacle. The present proof bypasses that obstacle by sampling an irrational time in the periodic lattice fixed space, thereby importing the **discrete** estimate without assuming a general multiplicity theorem for lattice-homomorphism semigroups.

The discrete lattice-homomorphism estimate [2, Proposition 3.1(b)] alone does not state the generator result; the fixed-space and irrational-sampling reductions above connect its hypotheses to generator eigenspaces. The 2021 article *Spectrum and convergence of eventually positive operator semigroups* [3] focuses on cyclic spectral sets and a distinct finite-rank spectral-space bound for certain individual operators. The 2025 article *Eventually positive semigroups: spectral and asymptotic analysis* [4, Theorem 4.7] proves cyclicity of a **spectrum** under asymptotic positivity and does not establish the present comparison of generator eigenspace dimensions. These are implication comparisons, not claims of exhaustive historical priority.

## Limitations

This is a geometric multiplicity inequality with all infinite dimensions identified as \(\infty\); it does not compare different infinite cardinals. No assertion is made about algebraic multiplicity, continuous or approximate spectrum, noncontractive semigroups, or arbitrary Banach lattices. It does not settle the separate non-root-of-unity question for a **single** positive contraction formulated as [1, Open Problem 3.4]. A related 1986 semigroup monograph cited by [1] was not accessible in full, and mathematically equivalent formulations could occur in unindexed literature; the claim of priority is therefore qualified.

## References

[1] J. Glück, *A note on the fixed space of positive contractions*, arXiv:2108.05174v1, initially public 2021-08-11; Theorem 3.1, Corollaries 3.3 and 3.5, remark following Corollary 3.5. https://arxiv.org/html/2108.05174v1

[2] J. Glück, *On the Peripheral Spectrum of Positive Operators*, arXiv:1503.02430v2 (2015), Proposition 3.1(b), Definition A.2, and Lemma A.4. https://arxiv.org/html/1503.02430v2

[3] *Spectrum and convergence of eventually positive operator semigroups*, *Semigroup Forum* (2021), Sections 2 and 4. https://doi.org/10.1007/s00233-021-10204-y

[4] *Eventually positive semigroups: spectral and asymptotic analysis*, *Semigroup Forum* (2025), Section 4 and Theorem 4.7. https://doi.org/10.1007/s00233-025-10519-0
