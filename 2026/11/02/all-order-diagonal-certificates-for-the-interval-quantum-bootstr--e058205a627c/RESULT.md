# All-order diagonal certificates for the interval quantum bootstrap

## Finding

Let \(w(z)=z(1-z)\), \(S=i\,d/dz\), and \(H=S w(Z) S=-d(w(z)\,d/dz)/dz\) on \(L^2(0,1)\) with the no-flux endpoint condition. Consider the alternatively ordered, \(K\times K\) two-operator bootstrap matrix \(\widetilde B_K(E)\) of Sword and Vegh [1], associated with the operator family \(S^j w(Z)^j\), \(0\le j<K\), and normalized by \(\langle1\rangle_E=1\). Its entries are the formal rational energy-dependent moments determined by the eigenstate bootstrap recursions, away from their poles.

**All-order diagonal identity.** For every integer \(j\ge1\), the rational diagonal entry has the closed form

\[
\boxed{\widetilde B_{jj}(E)=\frac{\binom{2j}{j}}{4^j}\frac{\prod_{k=0}^{j-1}(E-k(k+1))^2}{\prod_{m=1}^{j}(4E-(4m^2-1))}.}
\]

Also \(\widetilde B_{00}(E)=1\). Thus the numerator zeros are doubled at exactly the first \(j\) physical levels, and its poles are exactly \(E=m^2-1/4\) for \(1\le m\le j\), without cancellations.

**Complete low-energy positivity classification at every size.** For every integer \(K\ge2\), and every real trial energy \(E\) with \(0\le E<(K-1)^2-1/4\) at which the formal matrix is defined,

\[
\boxed{\widetilde B_K(E)\succeq0\quad\Longleftrightarrow\quad E=n(n+1)\text{ for some }n\in\{0,\ldots,K-2\}.}
\]

At any pole \(E=m^2-1/4\), \(1\le m\le K-2\), the formal matrix is undefined and is **not** assigned a positivity status. No assertion is made above or at the final threshold \(E=(K-1)^2-1/4\). The result is an arbitrary-size proof of the precise low-energy behavior observed at finite sizes in [1].

## Assumptions and scope

The underlying differential expression is \(H\psi=-(w\psi')'\) with no-flux boundary \(w\psi'\to0\) at both ends. Its normalized eigenfunctions and eigenvalues are

\[
\psi_n(z)=\sqrt{2n+1}\,P_n(2z-1),\qquad E_n=n(n+1),\qquad n=0,1,2,\ldots.
\]

Here \(P_n\) is the ordinary Legendre polynomial. Formal off-spectrum entries of \(\widetilde B_K(E)\) are defined by the rational bootstrap moment identities of [1], not by postulating an off-spectrum normalizable eigenfunction. The normalization \(f_0(E)=1\), \(f_1(E)=1/2\) and the following recurrence, equivalent to [1, equation (3.10)], determine the one-variable moments rationally at generic energy:

\[
(m-1)^3 f_{m-2}+(2m-1)(2E-m^2+m) f_{m-1}+m(m^2-4E-1)f_m=0\quad(m\ge2).
\]

At physical energies where a recursion coefficient may vanish, identities are interpreted through direct eigenstate expectations; rational functional identities are obtained by matching at arbitrarily large physical energies, avoiding such exceptional divisions. The source's alternative ordering is essential: the formula is not asserted for its ordinarily ordered bootstrap matrix or its distinct higher-power subfamily.

## Proof

**1. A weighted derivative identity for all Legendre levels.** Fix \(n\ge0\) and \(j\ge0\), set \(E=E_n\), \(u=\psi_n^{(j)}\), and \(\Lambda=E-j(j+1)\). Differentiating \((w\psi_n')'+E\psi_n=0\) exactly \(j\) times and multiplying by \(w^j\) gives

\[
(w^{j+1}u')'+\Lambda w^j u=0.
\]

Define three finite, nonnegative integrals

\[
I_j=\int_0^1w^{2j}u^2\,dz,\quad J_j=\int_0^1w^{2j+1}u^2\,dz,\quad I_{j+1}=\int_0^1w^{2j+2}(u')^2\,dz.
\]

The endpoints contribute no boundary terms: \(u\) is a polynomial and the weights vanish to positive orders. With \(w'=1-2z\), \((w')^2=1-4w\), and \(w''=-2\), direct integration by parts gives

\[
T_j:=\int_0^1w^{2j+1}w'uu'\,dz=-\frac{2j+1}{2}I_j+(4j+3)J_j.
\]

Multiplying the differentiated equation by \(w^{j+1}u\), integrating by parts, and separately integrating the derivative of \(w^{2j+2}w'(u')^2\), yields the two exact relations

\[
I_{j+1}=\Lambda J_j-(j+1)T_j,\qquad I_{j+1}=-\Lambda T_j.
\]

The second relation follows because the two terms containing \((u')^2(w')^2\) cancel after substituting \(u''=-(j+1)(w'/w)u'-(\Lambda/w)u\). Eliminating \(T_j\) and \(J_j\) gives, without dividing by a potentially vanishing \(I_j\),

\[
\boxed{I_{j+1}=\frac{2j+1}{2(j+1)}\frac{[E-j(j+1)]^2}{4E-(2j+1)(2j+3)}I_j.}
\]

The denominator cannot vanish for \(E=E_n\), because \(4E_n\) is divisible by four whereas \((2j+1)(2j+3)\) is odd. The relation therefore holds also for \(j>n\), when both derivative norms vanish. Since \(I_0=1\), iteration gives

\[
I_j(E_n)=\frac{(2j)!}{4^j(j!)^2}\frac{\prod_{k=0}^{j-1}(E_n-k(k+1))^2}{\prod_{m=1}^j(4E_n-(4m^2-1))}.
\]

**2. From physical norms to the formal bootstrap rational functions.** The alternative matrix of [1, equations (3.39)–(3.42)] has diagonal

\[
\widetilde B_{jj}(E)=\big\langle S^j w^{2j}S^j\big\rangle_E.
\]

At every actual eigenstate \(\psi_n\), this equals \(\int_0^1w^{2j}|\psi_n^{(j)}|^2dz=I_j(E_n)\). To justify interpolation of the *off-spectrum* formal expression, fix \(j\). Repeated substitution of \(\psi''=-(w'/w)\psi'-(E/w)\psi\) into \((-1)^j\partial_z^j(w^{2j}\partial_z^j\psi)\) produces \(A_j(z,E)\psi'+B_j(z,E)\psi\), with polynomial coefficients and \(A_j(0,E)=A_j(1,E)=0\): each differentiation can remove at most one factor of \(w\), while the initial \(w^{2j}\) cancels all denominators arising from the first \(j\) derivatives and the following \(j\) derivatives. The associated formal expectation, after one integration by parts, is thus the expectation of the polynomial \(B_j-\tfrac12\partial_zA_j\). Consequently it is a finite linear combination of \(f_0(E),\ldots,f_{M_j}(E)\), hence is a rational function of \(E\) by the displayed moment recursion. The same factor-counting argument works for arbitrary matrix indices \(j,k\), with initial weight \(w^{j+k}\). For \(k\ge1\), reducing \(D^k\psi\) leaves at least \(j+1\) powers of \(w\), enough to absorb the following \(j\) differentiations. For \(k=0\), the coefficient of \(\psi\prime\) still retains a factor of \(w\), as one differentiation must act on \(\psi\) rather than on \(w^j\). Therefore every matrix entry has a rational representation in the same normalized moments. There is no assumption that such a formal expectation is a positive measure off the spectrum.

For every fixed \(j\), infinitely many physical levels \(n\) are sufficiently high that none of the finitely many moment recursions needed to evaluate this diagonal degenerates at \(E_n\). At those levels the formal moment recursion agrees with the genuine integrals, by its integration-by-parts derivation and initial conditions. Thus the formal diagonal and the right side of the boxed product are rational functions agreeing at infinitely many distinct values \(E_n\). They coincide identically. The all-order diagonal formula follows.

To justify the **converse at every low physical energy**, rather than merely at sufficiently large ones, note the parity symmetry \(\psi_n(1-z)^2=\psi_n(z)^2\). For each odd integer \(m\), it gives the physical identity

\[
2f_m=\sum_{k=0}^{m-1}(-1)^k\binom{m}{k}f_k.
\]

This identity holds rationally in \(E\): it holds at infinitely many high nonresonant physical levels, and both sides are rational. Hence every *odd* moment \(f_m(E)\) is determined from lower moments without division by the potentially vanishing odd-step coefficient \(m^2-4E-1\). At even steps \(m=2\ell\), that coefficient can vanish only at \(E=\ell^2-1/4\), never at a nonnegative integer physical level \(E_n=n(n+1)\). Induction therefore proves that all rational moments needed for each fixed matrix entry are regular at every \(E_n\), and their values equal those of the actual normalized Legendre state. Consequently the **whole** formal matrix at \(E_n\), not merely its diagonal, equals the physical Gram matrix. This removes any concern from the formally resonant odd steps in the original moment recurrence.

**3. A single negative diagonal excludes each nonphysical low energy.** Put \(\lambda_j=j^2-1/4\), so \(\lambda_0=-1/4\). For every \(1\le j\le K-1\) and any \(E\in(\lambda_{j-1},\lambda_j)\), exactly one denominator factor in \(\widetilde B_{jj}(E)\)—the \(m=j\) factor—is negative. The other \(j-1\) factors are positive. The squared numerator is strictly positive except at the single physical energy \(E_{j-1}=j(j-1)\) lying in this interval. Hence \(\widetilde B_{jj}(E)<0\) at every nonphysical energy in that interval. A Hermitian positive-semidefinite matrix cannot have a negative diagonal. These intervals cover \(0\le E<\lambda_{K-1}\) after removing their pole boundaries.

At a physical level \(E_n\), \(0\le n\le K-2\), all entries of the formal matrix agree with the genuine Gram products of \(w^j S^j\psi_n\), so \(\widetilde B_K(E_n)\succeq0\). This establishes both directions. At each excluded interior pole \(\lambda_m\), the diagonal \(\widetilde B_{mm}\) has a genuine simple pole (its squared numerator is nonzero), so the original formal matrix is not finite there.

## Verification

The accompanying standalone \(verify.py\) independently constructs formal diagonal entries using differential-operator reduction and the normalized polynomial-moment recursion; checks the exact product for \(1\le j\le6\); compares selected actual Legendre polynomial weighted derivative norms against the formula by exact integration; checks the explicit \(K=3\) diagonal of [1, equation (3.42)]; and evaluates rational sign witnesses within successive pole gaps. Execute \(python3 verify.py\) with SymPy installed. The universal theorem is proved in the preceding section; finite symbolic tests do not establish the arbitrary-\(K\) quantifier.

## Relationship to prior work

Sword and Vegh [1] introduced both alternative bootstrap orderings and showed finite-size exact low-energy isolation numerically, checking the determinant to \(K=12\) and positivity directly to \(K=5\). Their section 4.4 explicitly identifies an **arbitrary-\(K\)** proof as outstanding. The present claim does not originate the model, its spectrum, its bootstrap formalism, the first finite-size matrices, or the physical positivity principle; its contribution is the all-order explicit diagonal factorization and an analytic single-diagonal certificate that proves the observed low-energy classification at every size. General quantum-bootstrap and finite-moment positivity literature uses related methods but was not found to state this diagonal identity for these exact operators and ordering.

## Limitations

The result applies to the no-flux Legendre realization and the specific \(\zeta=\sigma\) alternatively ordered matrix. It does not prove an analogous classification for the other ordering, other boundary conditions, the \(\zeta=2\sigma\) subfamily, or energies at/above the last pole. The formal bootstrap matrix is a rational extension of moment recursions, not a Hilbert-space Gram matrix at arbitrary trial energies. Pole points are excluded, not assigned a limiting positivity status. Mathematical priority has not been independently audited; broader unpublished derivations or later literature may exist.

## References

[1] Lewis Sword and David Vegh, *Quantum mechanical bootstrap on the interval: obtaining the exact spectrum*, arXiv:2402.03434v1 (5 February 2024), *Physical Review D* **109**, 126002 (6 June 2024), https://arxiv.org/html/2402.03434v1 , https://doi.org/10.1103/PhysRevD.109.126002 . Particularly §§2.2–2.3, 3.1, 3.4.3 and 4.4, Appendix C.

[2] Xihe Hu, *Different Bootstrap Matrices in Many QM Systems*, arXiv:2206.00767 (2022), https://arxiv.org/abs/2206.00767 . Background on matrix choices; no claim of the present all-order formula is attributed to this reference.
