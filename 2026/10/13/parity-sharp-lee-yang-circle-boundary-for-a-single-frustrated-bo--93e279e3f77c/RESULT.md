# Parity-sharp Lee–Yang circle boundary for a single frustrated bond in an Ising ring

## Finding

For every integer \(n\ge3\), every real \(K>0\), and every real defect coupling \(L\), define the finite Ising-ring partition function
\[
Z_n(K,L;h)=\sum_{\sigma\in\{-1,1\}^n}
\exp\!\left(K\sum_{j=1}^{n-1}\sigma_j\sigma_{j+1}+L\sigma_n\sigma_1+h\sum_{j=1}^n\sigma_j\right).
\]
The reduced polynomial is \(P_n(z)=e^{-nh}Z_n(K,L;h)\), where \(z=e^{-2h}\), so \(P_n\) has degree \(n\) and strictly positive coefficients. Its Lee–Yang circle property means that **all** \(n\) complex roots of \(P_n\), including multiplicities, have modulus one.

Put \(c^2=1-e^{-4K}\). The complete necessary and sufficient condition is
\[
\boxed{
\begin{aligned}
 n\ \mathrm{even}:\quad &L\ge -K,\\
 n\ \mathrm{odd}:\quad &L\ge -K-\tfrac12\log\left(1+\frac{1-e^{-4K}}{n-1}\right).
\end{aligned}}
\]
At equality, the first off-circle collision occurs at \(z=-1\): this zero has multiplicity exactly two when \(n\) is even and exactly three when \(n\) is odd. If the respective inequality is violated, a reciprocal pair of **negative real**, off-unit-circle Lee–Yang zeros exists. The odd-ring tolerance of a single negative bond exceeds the even-ring tolerance by a strictly positive, explicit finite-size amount that tends to zero as \(n\to\infty\).

## Assumptions and scope

The underlying graph is the simple cycle on \(n\ge3\) spins, with \(n-1\) equal positive real dimensionless pair couplings \(K\), one arbitrary real pair coupling \(L\), and a spatially uniform complex dimensionless field \(h\). The temperature has been absorbed into the couplings; no thermodynamic limit is taken. There are no other interactions. The theorem classifies the complete zero set's confinement to \(|z|=1\); it does not claim all individual zero angles are explicitly elementary.

## Proof

**1. Transfer matrix and exact polynomial.** Set
\[
T_J(h)=\begin{pmatrix}e^{J+h}&e^{-J}\\e^{-J}&e^{J-h}\end{pmatrix}.
\]
Its off-diagonal entries split the uniform field equally between neighboring bonds. Thus \(Z_n=\operatorname{tr}(T_K^{n-1}T_L)\). Let \(d=\sqrt{2\sinh 2K}=e^Kc>0\), \(x=\cosh h/c\), and let \(U_j\) be the second-kind Chebyshev polynomial, normalized by \(U_0=1\), \(U_1=2x\), \(U_{j+1}=2xU_j-U_{j-1}\). Cayley–Hamilton gives
\[
T_K^{n-1}=d^{n-2}U_{n-2}(x)T_K-d^{n-1}U_{n-3}(x)I.
\]
Taking the trace with \(T_L\) and using \(2\cosh^2h-1=\cosh2h\), one obtains the exact identity
\[
Z_n(K,L;h)=2e^{K+L}d^{n-2}c^2 Q_n(x),\qquad
Q_n(x)=xU_{n-1}(x)+\lambda U_{n-2}(x),
\]
with \(\lambda=(e^{-2(K+L)}-1)/c^2\). Notice \(\lambda>-1/c^2\) for every finite real \(L\), and \(\lambda=0\) exactly when \(L=-K\). Because \(Q_n\) has parity \(n\), the identity is a degree-\(n\) polynomial in \(z=e^{-2h}\) after multiplication by \(e^{-nh}\). Every root of \(Q_n\) in \([-1/c,1/c]\) yields field \(h=i\theta\) with \(\cos\theta=cx\), hence a unit-modulus fugacity; conversely, any root of \(Q_n\) outside this real interval yields a non-unit fugacity. The root counts agree, including multiplicity. Therefore the circle property is equivalent to all zeros of \(Q_n\) lying in \([-1/c,1/c]\).

**2. The entire \(\lambda\le0\) region is stable.** The Chebyshev recurrence gives
\[
2Q_n(x)=U_n(x)+(1+2\lambda)U_{n-2}(x).
\]
For \(\lambda\le0\), this is, up to a positive constant, the characteristic polynomial of the real symmetric \(n\)-site Jacobi matrix with zero diagonal, edges \(1/2\) except the last edge \(\sqrt{-\lambda/2}\). Indeed the last principal-minor recurrence gives precisely the coefficient \(1+2\lambda\). Hence all \(n\) zeros are real, including at \(\lambda=0\), where the last edge vanishes.

At \(\lambda=0\), the zeros of \(xU_{n-1}(x)\) all lie in \((-1,1)\). They vary continuously with \(\lambda\). No zero can cross the boundaries \(\pm1/c\) while \(-1/c^2<\lambda\le0\), since, for \(u=1/c\ge1\),
\[
Q_n(u)\ge uU_{n-1}(u)-u^2U_{n-2}(u)
=u^2U_{n-2}(u)-uU_{n-3}(u)>0,
\]
where the first inequality uses \(\lambda\ge-u^2\), the equality uses the Chebyshev recurrence, and the strict inequality follows from \(U_{n-2}(u)\ge U_{n-3}(u)>0\). By parity, \(Q_n(-u)\ne0\) as well. Thus all roots remain in the required closed interval throughout \(\lambda\le0\).

**3. Even \(n\), any \(\lambda>0\) fails.** Write \(n=2m\). Then \(Q_n(iy)\) is real for real \(y\), and at \(y=0\) its sign is \((-1)^{m-1}\) because \(Q_n(0)=\lambda U_{2m-2}(0)=\lambda(-1)^{m-1}\). Its leading term as \(y\to+\infty\) has the opposite sign \((-1)^m\). By continuity \(Q_n(iy)=0\) for some \(y>0\), which produces non-unit negative real fugacity zeros. At \(\lambda=0\), \(Q_n=xU_{n-1}\) has a zero of multiplicity exactly two at \(x=0\), corresponding to \(z=-1\).

**4. Odd \(n\), a finite additional stable interval.** Write \(n=2m+1\), \(m\ge1\). Since \(U_{2m-1}(x)\) is divisible by \(x\), set
\[
Q_n(x)=x F_m(x),\qquad F_m(x)=U_{2m}(x)+\lambda\frac{U_{2m-1}(x)}x.
\]
The two even polynomials in this formula have strictly interlacing positive roots: the \(m\) positive roots of \(U_{2m}\) are \(a_j=\cos(j\pi/(2m+1))\), and the \(m-1\) positive roots of \(U_{2m-1}/x\) are \(b_j=\cos(j\pi/(2m))\), with \(a_1>b_1>a_2>\cdots>b_{m-1}>a_m>0\). For every \(\lambda>0\), the values of \(F_m\) at successive \(a_j\) have alternating signs, so there are at least \(m-1\) distinct positive roots between consecutive \(a_j\). At the origin
\[
F_m(0)=(-1)^m[1-2m\lambda],
\]
whereas \(F_m(a_m)\) has sign \((-1)^{m-1}\). If \(0<\lambda<1/(2m)\), there is one additional positive root between zero and \(a_m\). Its \(m\) positive roots and their negatives exhaust the degree \(2m\), so every root of \(Q_n\) lies in \((-1,1)\) apart from its zero at the origin. If \(\lambda=1/(2m)\), the last pair reaches zero, and the factor \(x\) makes a triple root. It is exactly triple because the coefficient of \(x^2\) in \(F_m\) at that value is \((-1)^{m-1}(m+1)(4m+2)/3\ne0\). The remaining roots stay in \((-1,1)\).

If \(\lambda>1/(2m)\), evaluate \(F_m(iy)\) for real \(y\ge0\). At \(y=0\) its sign is \((-1)^{m-1}\), whereas its leading term at infinity has sign \((-1)^m\); hence it has an imaginary root \(iy\) with \(y>0\), again producing a negative real reciprocal off-circle pair. Thus the exact odd threshold is \(\lambda=1/(n-1)\).

**5. Translate back to the defect.** The inequality \(\lambda\le0\) is equivalent to \(L\ge-K\). For odd \(n\), \(\lambda\le1/(n-1)\) is equivalent to \(e^{-2(K+L)}\le1+c^2/(n-1)\), or to the displayed odd-ring lower bound. This completes the necessary-and-sufficient classification, including the collision multiplicities and the direction of failure.

## Verification

A standalone checker, `verify.py`, independently enumerates the real positive-coefficient Ising partition polynomial for \(3\le n\le11\) at three positive couplings and five defect choices straddling each predicted threshold. It checks numerical unit-circle roots, exact transfer-matrix/Chebyshev evaluation identities at five complex-field points per parameter set, and the boundary-zero multiplicity at 27 parameter pairs. Run `python verify.py` with NumPy installed. These finite numerical tests are supplementary; the argument above proves the all-\(n\), all-real-parameter statement.

## Relationship to prior work

The classical Lee–Yang circle theorem guarantees the circle property for purely ferromagnetic couplings, so its standard hypothesis covers \(L\ge0\) but does not decide negative \(L\). Matveev and Shrock examined extensions of circle behavior for complexified uniform couplings on higher-dimensional regular lattices; their focus is neither a single real antiferromagnetic defect in a finite ring nor an exact length-parity threshold. Peters and Regts characterized zero-free regions for graph families with uniform ferromagnetic or antiferromagnetic edge weights. Bencs, Buys, Guerini and Peters treated uniform antiferromagnetic weights with tree-based dynamical methods. Those general settings do not directly determine the present mixed-sign, single-defect all-zero threshold. Most directly, Tonchev and Dantchev (2026), Theorem 1, Equation (23), already derive the full Chebyshev representation of the defective-ring partition function, algebraically equivalent to our formula for \(Q_n\). That expression, and the method of deriving it, are **prior work and not claimed as original**. Their investigation explicitly assumes real magnetic field, and the inspected theorem, ensuing magnetization sections, and conclusion do not classify all complex-field Lee–Yang zeros or give the parity-dependent sharp bound. The contribution assessed here is solely this global root-confinement classification, its sharp defect threshold, and boundary multiplicities. A closed-form partition function does not by itself assert a root-location theorem. This close antecedent presents a genuine risk of a different derivation in uninspected specialized literature. A specialized antecedent not found in the consulted literature remains possible.

## Limitations

No claim is made about zero angles beyond confinement, observables at nonzero complex field, several defects, nonuniform remaining bonds, or infinite-dimensional systems. Publication priority has not been independently established. The zero at \(z=-1\) can have multiplicity two or three at the boundary; other degeneracies are not classified. Numerical verification is limited to finite instances, not a substitute for the proof.

## References

1. V. Matveev and R. Shrock, *Some New Results on Yang–Lee Zeros of the Ising Model Partition Function*, arXiv:cond-mat/9512149v2 (public preprint, 22 December 1995), https://arxiv.org/html/cond-mat/9512149v2.
2. H. Peters and G. Regts, *Location of zeros for the partition function of the Ising model on bounded degree graphs*, arXiv:1810.01699v3 (first posted 3 October 2018), https://arxiv.org/html/1810.01699v3.
3. F. Bencs, P. Buys, L. Guerini and H. Peters, *Lee–Yang Zeros of the antiferromagnetic Ising Model*, arXiv:1907.07479v1 (17 July 2019), https://arxiv.org/html/1907.07479v1.
4. N. S. Tonchev and D. Dantchev, *The Algebra of Chebyshev Polynomials and the Transfer-Matrix Approach for the One-Dimensional Ising Model with a Defect*, Mathematics 14 (2026), 741, Theorem 1, Eq. (23), https://doi.org/10.3390/math14040741; corresponding public preprint posted 2 February 2026, https://www.preprints.org/manuscript/202601.2419.
5. T. D. Lee and C. N. Yang, *Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model*, Physical Review 87 (1952), 410–419, DOI:10.1103/PhysRev.87.410.
