# Arithmetic obstruction to exact revival of odd-dimensional spin-coupled Grover harmonic walks

## Finding

Let \(d=2m+1\geq3\) be odd and let \(\widetilde W_{\mathbf s}\) be the spin-coupled Grover step on the \(d\)-dimensional Boolean hypercube as defined in [1]. Assume the spin field is constant, with value \(\varepsilon\in\{-1,1\}\), on the four central Hamming layers of weights \(m-1,m,m+1,m+2\); its values elsewhere are arbitrary. Let \(\mathcal H_{\mathrm{har}}^{\mathrm{odd}}\) denote the nonzero invariant central harmonic space constructed in [1]. Then, for every positive integer \(T\) and every unit scalar \(\xi\),

\[
\left(\widetilde W_{\mathbf s}\big|_{\mathcal H_{\mathrm{har}}^{\mathrm{odd}}}\right)^T\ne \xi I.
\]

In particular, the full spin-sector walk cannot have a scalar global revival. Within the harmonic subspace, the pure states having no exact projective revival at any positive integer time form an open dense set of full measure; the same is true among pure states of the full finite-dimensional spin-sector space. This statement does **not** say every state lacks recurrence: eigenstates recur projectively at each step.

For comparison, the even-dimensional central harmonic construction of [1] yields a nonzero subspace of exact fixed states. That fixed-state assertion is an established result, not a new claim. Thus the central harmonic dynamics has a dimension-parity distinction between a fixed sector in even dimension and nonperiodic full-sector dynamics in every odd dimension.

## Assumptions and scope

The graph is the Boolean hypercube \(Q_d\) with standard Grover coin; the spin-coupled walk, coin/shift convention and QBN central harmonic lifting are exactly those of [1, §2 and §4]. In odd dimension \(d=2m+1\), the harmonic lift provides an invertible intertwiner \(\mathfrak T_m\) from \(\mathscr H_m^-\otimes\mathbb C^8\) onto \(\mathcal H_{\mathrm{har}}^{\mathrm{odd}}\), satisfying

\[
\widetilde W_{\mathbf s}\,\mathfrak T_m=\mathfrak T_m(I\otimes \mathcal M_m^{(\varepsilon)}).
\]

Both this intertwiner and the reduced matrix \(\mathcal M_m^{(\varepsilon)}\) are from [1, Theorem 4.3, equation (4.20)]. Each matrix is diagonalizable because it is similar to a restriction of a unitary matrix. The theorem concerns integer-time exact global or projective revival, not approximate recurrence, local measurement return, mixing, or all spin choices outside the four central layers.

## Proof

**1. An explicit characteristic coefficient.** Set \(d=2m+1\) and \(\omega=\exp(-i\varepsilon\pi/d)\). Equation (4.20) of [1] gives the eight-by-eight matrix through

\[
\begin{aligned}
y_0&=\omega^m(-x_1+2(m+1)x_2+2x_3)/d, &y_1&=-\omega^{m-1}x_0,\\
y_2&=-\omega^{m+1}x_4,&y_3&=\omega^{m+1}(2x_4+x_5+2mx_6)/d,\\
y_4&=\omega^m(2mx_1+x_2+2x_3)/d,&y_5&=-\omega^m x_3,\\
y_6&=-\omega^{m+2}x_7,&y_7&=\omega^{m+1}(2x_4+2(m+1)x_5-x_6)/d.
\end{aligned}
\]

Its diagonal vanishes, hence \(\operatorname{tr}\mathcal M=0\). Enumerating the five unordered nonzero two-way coordinate couplings in these eight rows and columns gives

\[
\frac12\operatorname{tr}(\mathcal M^2)
=\frac{\omega^{2m-1}+\omega^{2m+3}-2\omega^{2m+1}}d
 +\frac{4\omega^{2m+1}}{d^2}
=\frac{4}{d}\sin^2\!\left(\frac\pi d\right)-\frac4{d^2}.
\]

Here \(\omega^{2m+1}=\omega^d=-1\). By Newton's identities, the coefficient of \(\lambda^6\) in \(\det(\lambda I-\mathcal M)\) is

\[
A_d=-\tfrac12\operatorname{tr}(\mathcal M^2)
=\frac4{d^2}\left(1-d\sin^2\!\frac\pi d\right).
\]

This agrees with [1, §4.4], but the matrix formula independently determines the needed coefficient. The same source gives \(\det\mathcal M=1\), also directly verifiable by the displayed matrix.

**2. The coefficient is not an algebraic integer.** Let \(\zeta=\exp(2\pi i/d)\) and \(\alpha=\zeta+\zeta^{-1}\). Then

\[
A_d=\frac{4-2d+d\alpha}{d^2}.
\]

Any field conjugate of \(\alpha\) has the form \(2\cos(2\pi k/d)\) for an integer \(k\) coprime to \(d\), and lies in \([-2,2]\). Every conjugate \(A_d'\) therefore satisfies

\[
\frac{4(1-d)}{d^2}\leq A_d'\leq\frac4{d^2},
\qquad |A_d'|<1\quad(d\geq3).
\]

Moreover \(A_d\neq0\). Otherwise \(\alpha=2-4/d\) would be rational; since \(\alpha\) is an algebraic integer, it would be an integer, forcing \(d\) to divide \(4\), impossible for odd \(d\geq3\). If \(A_d\) were itself an algebraic integer, its field norm would be a nonzero rational integer, yet the product of the absolute values of all its conjugates is strictly less than one. This contradiction proves that \(A_d\) is not an algebraic integer.

**3. Excluding even projective finite order.** If \(\mathcal M^T=I\) for a positive integer \(T\), all eight eigenvalues of \(\mathcal M\) are roots of unity. Their second elementary symmetric sum, \(A_d\), must then be an algebraic integer; Step 2 rules this out. If instead \(\mathcal M^T=\xi I\), taking determinants gives \(\xi^8=(\det\mathcal M)^T=1\). Consequently \(\mathcal M^{8T}=I\), again impossible. The intertwiner transfers this conclusion to the full harmonic restriction. If the full walk had scalar finite order, so would its invariant harmonic restriction; therefore the full spin-sector walk also lacks scalar finite order.

**4. Generic pure states.** The eight eigenvalues are distinct and on the unit circle [1, §4.4]. A harmonic vector with nonzero projections onto every one of their eight eigenspaces cannot obey \(\widetilde W^T\psi=\xi\psi\) for any \(T>0\), because that would force the restriction to satisfy \(\mathcal M^T=\xi I\). The set with all eight spectral projections nonzero is the complement of a finite union of proper closed linear subspaces, hence open, dense and full measure on the unit sphere. The harmonic sector reduces the full unitary walk; imposing nonzero projections onto its eight eigenspaces defines the same type of open dense full-measure set in the full finite-dimensional spin-sector Hilbert space. This proves the generic statement.

## Verification

The included `verify.py` requires Python 3 and NumPy; run `python3 verify.py`. It independently constructs the displayed eight-by-eight matrix for eleven odd dimensions from \(3\) through \(101\), both spin signs, and checks the characteristic coefficients, second trace, determinant and unit-circle spectrum. For dimensions \(3,5,7\), it separately constructs the full hypercube Grover operator and the eight QBN lifts and tests the exact intertwining identity numerically. All 131 assertions pass with indicated floating-point tolerances. These finite computations corroborate the input identities, **not** the proof of nonperiodicity for unbounded odd dimensions; the latter is the algebraic-integer argument of Steps 2–3.

## Relationship to prior work

Wang [1] established the parity-dependent invariant harmonic spaces, their complete eight-dimensional odd reduction, its explicit characteristic polynomial, and the exact fixed even-dimensional subspace. None of these constructions, nor the spectrum formula, is claimed as new. The added conclusion here is an all-odd-dimension obstruction to every scalar revival time, including projective global revival, and its generic-state consequence. Kajiwara et al. [2] used cyclotomic arithmetic to exclude finite periods for a different three-state walk on finite cycles; that general arithmetic technique is prior art, but their theorem concerns a different operator and does not imply the spin-coupled hypercube claim. Jayakody and Nanayakkara [3] constructed exact revivals by special coin engineering on higher-dimensional lattices; those constructions neither provide nor contradict a finite period of the fixed model here.

## Limitations

The result does not exclude arbitrarily close recurrences (finite-dimensional unitary orbits have approximate returns), exact projective recurrence of eigenvectors, or recurrence of particular special states. The spin field need only be constant on the central four layers, but the statement does not automatically extend to arbitrary spins there. It is a discrete-time projective-period statement, not a classification of stationary distributions or transition-probability periodicity. Priority beyond the inspected literature is not independently established.

## References

[1] Ce Wang, *Harmonic Reduction of Spin-Coupled Grover Walks on Hypercubes via Quantum Bernoulli Noises*, arXiv:2610.14467v1 (10 October 2026), revised v2 (14 October 2026); https://arxiv.org/html/2610.14467v2 .

[2] T. Kajiwara, N. Konno, S. Koyama and K. Saito, *Periodicity for the 3-state quantum walk on cycles*, arXiv:1907.01725 (2019); https://arxiv.org/abs/1907.01725 .

[3] M. N. Jayakody and A. Nanayakkara, *Full state revivals in higher dimensional quantum walks*, arXiv:1806.07032 (2018); https://arxiv.org/abs/1806.07032 .
