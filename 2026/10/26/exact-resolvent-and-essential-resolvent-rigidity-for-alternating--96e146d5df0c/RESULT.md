# Exact resolvent and essential-resolvent rigidity for alternating-adjoint block paths

## Finding
Let \(H\) be a nonzero complex Hilbert space, let \(m\ge2\) be an integer, and let \(a_1,\ldots,a_{m-1}>0\). Let \(J\) be the scalar \(m\)-by-\(m\) nilpotent weighted upper shift, whose only nonzero entries are \(J_{j,j+1}=a_j\). For \(T\in\mathcal B(H)\), form the block upper shift \(B_T\) on \(H^{\oplus m}\) with only nonzero blocks
\[
(B_T)_{j,j+1}=\begin{cases}a_jT,&j\text{ odd},\\a_jT^*,&j\text{ even}.\end{cases}
\]
Put \(L=\|T\|\) and, when \(H\) is infinite-dimensional, \(L_{\mathrm e}=\inf_{K\in\mathcal K(H)}\|T-K\|\). Set
\[
F_m(s)=\left\|\left(I_m-sJ\right)^{-1}\right\|_2,\qquad s\ge0.
\]
Here \(\|\cdot\|_2\) is the matrix operator norm induced by Euclidean norm, not the Hilbert--Schmidt norm.

**Exact global resolvent law.** For all complex \(z\), without any normality, injectivity, closed-range, compactness, or norm-attainment assumption on \(T\),
\[
\boxed{\ \big\|(I-zB_T)^{-1}\big\|=F_m(|z|L).\ }
\]
If \(H\) is infinite-dimensional, the Calkin essential norm satisfies the independently exact law
\[
\boxed{\ \big\|(I-zB_T)^{-1}\big\|_{\mathrm e}=F_m(|z|L_{\mathrm e}).\ }
\]
For \(z\ne0\) and \(T\ne0\), the first resolvent attains its operator norm on the unit sphere if and only if \(T\) does. The function \(F_m\) is continuous and strictly increasing on \([0,\infty)\), with \(F_m(0)=1\).

**Entire pseudospectral disks.** Using the strict convention \(\sigma_\varepsilon(B_T)=\sigma(B_T)\cup\{\lambda\notin\sigma(B_T):\|(\lambda I-B_T)^{-1}\|>1/\varepsilon\}\), for each \(\varepsilon>0\) there is a unique \(r_\varepsilon>0\) satisfying
\[
r_\varepsilon=\varepsilon F_m(L/r_\varepsilon),
\qquad \sigma_\varepsilon(B_T)=\{\lambda\in\mathbb C:|\lambda|<r_\varepsilon\}.
\]
For \(L>0\), as \(\varepsilon\downarrow0\),
\[
r_\varepsilon\sim\left(\varepsilon L^{m-1}\prod_{j=1}^{m-1}a_j\right)^{1/m}.
\]
For infinite-dimensional \(H\), replacing \(L\) by \(L_{\mathrm e}\) gives the same exact radial level sets for the essential-resolvent norm (and a radius \(\varepsilon\) when \(L_{\mathrm e}=0\)).

For the unweighted path \(a_j=1\) and any \(T\) of norm one, an explicit universal value is
\[
\boxed{\ \big\|(I-B_T)^{-1}\big\|=\frac{1}{2\sin(\pi/(4m+2))}.\ }
\]
If \(H\) is infinite-dimensional and \(\|T\|_{\mathrm e}=1\), the essential norm of this inverse is exactly the same constant.

## Assumptions and scope
All assertions concern bounded operators on complex Hilbert spaces, with arbitrary Hilbert-space dimension unless the essential norm is mentioned. The integer \(m\) is finite, the scalar edge weights are strictly positive, and the alternating use of \(T\) and \(T^*\) begins with \(T\) at the first superdiagonal block. The result is invariant under unimodular edge phases, removed by a diagonal scalar unitary. The zero operator is allowed in both norm identities; the norm-attainment equivalence is deliberately stated only for nonzero \(T\) and nonzero \(z\). With \(T=0\), the resolvent is the identity and the pseudospectral radius is \(\varepsilon\).

## Proof
**1. Exact polar reduction, including singular cores.** Write \(T=U|T|\) in its polar decomposition, and let \(M=(\ker T)^\perp\) and \(R=\overline{\operatorname{ran}T}\). The restriction \(U:M\to R\) is a unitary between these two Hilbert spaces. In the direct sum \(H^{\oplus m}\), take at odd-numbered sites the subspace \(R\), and at even-numbered sites \(M\). Their orthogonal direct sum \(\mathcal L\) reduces \(B_T\): each block \(T\) takes its even input in \(M\) to its odd output in \(R\); each block \(T^*\) takes its odd input in \(R\) to its even output in \(M\). On the orthogonal complement \(\mathcal L^\perp\), every block vanishes, because \(T\ker T=0\) and \(T^*R^\perp=0\). Conjugating the odd sites of \(\mathcal L\) by \(U^*\), and leaving the even sites unchanged, identifies its restriction with \(J\otimes A\), where \(A=|T||_M\ge0\). Hence, with the orthogonal complement interpreted as a possibly zero-dimensional space,
\[
B_T\ \simeq\ (J\otimes A)\oplus0_{\mathcal L^\perp}.
\]
This remains an honest unitary equivalence when \(T\) has unequal kernel and cokernel dimensions or nonclosed range; no artificial unitary extension of its polar factor is used. Furthermore \(\|A\|=L\).

**2. Scalar monotonicity.** Since \(J^m=0\),
\[
Q(s)=(I_m-sJ)^{-1}=\sum_{k=0}^{m-1}s^kJ^k.
\]
For real \(s\ge0\), all entries are nonnegative; those on and above the diagonal are strictly positive whenever \(s>0\). If \(0\le s\le t\), entrywise \(0\le Q(s)\le Q(t)\); for every complex vector \(v\), \(|Q(s)v|\le Q(t)|v|\), hence \(F_m(s)\le F_m(t)\). At \(s>0\), \(Q(s)^*Q(s)\) has strictly positive entries, so its leading Perron eigenvector is strictly positive. If \(0<s<t\), applying the latter vector to \(Q(t)^*Q(t)-Q(s)^*Q(s)\), which is nonnegative entrywise and nonzero, proves strict inequality of largest eigenvalues. Finally \(F_m(s)>1=F_m(0)\) for every \(s>0\), using the last standard basis vector. Continuity is immediate.

For complex \(\zeta\), a diagonal unitary with successive phase increments \(\arg\zeta\) conjugates \(\zeta J\) to \(|\zeta|J\). Thus \(\|(I_m-\zeta J)^{-1}\|_2=F_m(|\zeta|)\).

**3. Ordinary norm and norm attainment.** The spectral theorem and continuous matrix-valued functional calculus for the positive operator \(A\) give
\[
\big\|(I-zJ\otimes A)^{-1}\big\|
=\max_{s\in\sigma(A)}\big\|(I_m-zsJ)^{-1}\big\|_2
=\max_{s\in\sigma(A)}F_m(|z|s)=F_m(|z|L).
\]
The direct summand on \(\mathcal L^\perp\) contributes norm one and cannot increase this value. For \(z\ne0\) and \(L>0\), strict increase of \(F_m\) implies that any norming vector of the resolvent has its \(A\)-spectral measure supported on \(\{L\}\); hence \(L\) is an eigenvalue of \(A\), which is equivalent to norm attainment by \(T\). Conversely, an eigenvector of \(A\) at \(L\), tensored with a top singular vector of \((I_m-zLJ)^{-1}\), gives a norming vector.

**4. Essential norm.** Suppose \(H\) is infinite-dimensional. If \(M\) is finite-dimensional, \(T\) is finite rank, the resolvent differs from the identity by a finite-rank operator, and both sides of the claimed essential-norm formula equal one. If \(M\) is infinite-dimensional, apply the Calkin quotient \(\pi_M:\mathcal B(M)\to\mathcal B(M)/\mathcal K(M)\) entrywise to \(Q(zA)\). The continuous functional calculus in the Calkin algebra yields
\[
\big\|\pi_{M^{\oplus m}}(Q(zA))\big\|
=\max_{s\in\sigma(\pi_M(A))}F_m(|z|s)
=F_m(|z|\|\pi_M(A)\|).
\]
Because \(T\) is unitarily equivalent as a map between its support spaces to \(A\), with zero on the respective kernel/cokernel, \(\|\pi_M(A)\|=\|T\|_{\mathrm e}\). Any infinite-dimensional orthogonal complement contributes an identity summand of essential norm one, already bounded by \(F_m\). Finite-dimensional summands contribute zero to the quotient. This proves the essential formula.

**5. Radial level sets and small-noise law.** Since \(B_T^m=0\), the spectrum is \(\{0\}\). For \(r=|\lambda|>0\),
\[
\|(\lambda I-B_T)^{-1}\|=r^{-1}F_m(L/r).
\]
This is continuous and strictly decreasing from infinity to zero as \(r\) increases from zero to infinity; the same remains true when \(L=0\), because the expression reduces to \(1/r\). Thus each pseudospectral threshold has the stated unique circular radius. For \(L>0\), the highest power in the finite inverse expansion is \(s^{m-1}J^{m-1}\), and \(\|J^{m-1}\|_2=\prod_j a_j\). Therefore \(F_m(s)\sim s^{m-1}\prod_j a_j\) as \(s\to\infty\), giving the radius asymptotic. The essential version follows by replacing \(L\) by \(L_{\mathrm e}\).

**6. Closed benchmark.** For \(a_j=1\), the inverse of \(Q(1)\) is \(I_m-J\). Its positive Gram matrix is tridiagonal, with diagonal \((1,2,\ldots,2)\) and neighboring entries \(-1\). The eigenvalue equation is the discrete second-difference equation with ghost boundary \(u_0=u_1\) and terminal boundary \(u_{m+1}=0\). The eigenangles are \((2k-1)\pi/(2m+1)\), \(k=1,\ldots,m\), so the smallest squared singular value is \(4\sin^2(\pi/(4m+2))\). Taking its reciprocal square root gives the benchmark.

## Verification
The provided standalone `checker.py` constructs alternating block shifts from independently generated complex matrices, including singular and nonnormal examples, and directly compares singular-value norms of the full matrix inverse with those of the scalar weighted path at \(\|T\|\). It also compares powers and checks the closed discrete-Volterra constant across path lengths. Its deterministic finite assertions test the formulas but do not replace the spectral and Calkin arguments needed for arbitrary Hilbert spaces. The exact reduction and monotonicity proof above establish the infinite-dimensional claims without numerical extrapolation.

## Relationship to prior work
Audeh, Kittaneh, and Moradi's 2026 paper computes the numerical radius of the unweighted alternating-adjoint path as \(\|T\|\cos(\pi/(m+1))\), and its proof exhibits alternating near-singular vectors. It does not calculate its full resolvent norm, essential-resolvent norm, norm-attainment locus, or pseudospectral disks. The present theorem concerns these distinct nonlinear invariants and permits arbitrary positive path weights. Buchała's 2024 paper develops unitary-equivalence theory for *bilateral* weighted shifts with quasi-invertible operator weights; its hypotheses and stated results do not give the present finite nilpotent, possibly singular-core reduction or exact Calkin-resolvent law. Classical pseudospectrum theory provides the general terminology and nilpotent asymptotic context, not this two-parameter collapse for alternating operator blocks.

The alternating-adjoint assumption is structural rather than decorative. For example, if two adjacent links both equal the same nonzero square-zero operator \(T\), the three-block shift has square zero; the corresponding alternating-adjoint shift has nonzero square. Thus a same-orientation family cannot share the universal profile at fixed \(\|T\|\).

## Limitations
This result concerns finite paths with a single common core \(T\), its adjoint on alternating edges, and positive scalar weights. It does not classify paths with arbitrary unrelated operator weights, infinite paths, other Banach norms, or full perturbation structure beyond norm-defined pseudospectra. The exact formulas do not imply that the usual resolvent norm is attained when \(T\) is not norm attaining. Historical priority against older operator-valued shift or pseudospectral literature requires independent verification; absence of matching search results is not a proof of novelty.

## References
1. W. Audeh, F. Kittaneh, H. R. Moradi, *Integral Representations and Sharp Numerical Radius Inequalities for Hilbert Space Operators*, arXiv:2610.15242v1 (first submitted 2026-10-11), especially Corollary 2.1. https://arxiv.org/html/2610.15242v1
2. M. Buchała, *Unitarily equivalent bilateral weighted shifts with operator weights*, Opuscula Math. 44 (2024), 651–672, especially Theorem 3.8. https://doi.org/10.7494/OpMath.2024.44.5.651
3. A. Böttcher, M. Lindner, *Pseudospectrum*, Scholarpedia 3(3):2680 (2008). https://var.scholarpedia.org/article/Pseudospectrum
4. L. N. Trefethen, M. Embree, *Spectra and Pseudospectra*, Princeton University Press (2005).
