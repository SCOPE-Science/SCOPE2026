# Sharp dephasing-enhancement boundary for a four-site Wannier–Stark chain

## Finding

For a four-site open \(XX\) chain with a uniform linear field, local dephasing and oppositely biased boundary reservoirs, the **inverse stationary current is strictly convex in the dephasing strength for every nonzero field and every positive boundary coupling**. This yields a complete, nonperturbative classification of dephasing-assisted current, rather than just its initial derivative.

In units \(J=\hbar=1\), let \(G>0\) be the boundary coupling, \(g\geq0\) the local dephasing strength, and \(U\geq0\) the field step. Define \(z=U^2\) and

\[
\begin{aligned}
\Phi_G(z)={}&5308416z^5+(3538944+460800G^2)z^4\\
&+(9547776+513024G^2+14608G^4)z^3\\
&+(5603328+157696G^2+16128G^4+200G^6)z^2\\
&+(2293760+90112G^2-1536G^4+128G^6+G^8)z\\
&-49152G^2-6144G^4-192G^6.
\end{aligned}
\]

For every \(G>0\), this polynomial has exactly one strictly positive zero \(z_c(G)\). Put \(U_c(G)=\sqrt{z_c(G)}\). For every positive boundary bias, the exact stationary current obeys the following trichotomy:

- If \(0\leq U\leq U_c(G)\), the current is strictly decreasing in \(g\geq0\); zero dephasing is the unique maximizing choice.
- If \(U>U_c(G)\), the current first strictly increases and then strictly decreases as \(g\) runs from zero to infinity, with exactly one strictly positive global optimizer.
- At \(U=U_c(G)\), the one-sided derivative at zero dephasing vanishes, but every positive dephasing strength strictly reduces the current.

The sharp boundary is nonmonotone as a function of boundary coupling in the following rigorous sense: it is positive at every finite \(G>0\), while

\[
U_c(G)\sim\sqrt{\frac{3}{140}}\,G\quad(G\downarrow0),
\qquad
U_c(G)\sim\frac{8\sqrt3}{G}\quad(G\to\infty).
\]

In particular it must attain a positive interior maximum. At matched coherent and boundary rates, \(G=1\), the exact threshold is \(U_c(1)=0.1485390031\ldots\), below the three-site threshold \(1/4\) in the same units.

## Assumptions and scope

The four sites have Hamiltonian

\[
H=\sum_{j=1}^{3}(\sigma_j^x\sigma_{j+1}^x+\sigma_j^y\sigma_{j+1}^y)
-U\sum_{j=1}^{4}j\sigma_j^z.
\]

The boundary reservoirs have jump operators

\[
L_1^\pm=\sqrt{\frac{G(1\pm f)}2}\,\sigma_1^\pm,
\qquad L_4^\pm=\sqrt{\frac{G(1\mp f)}2}\,\sigma_4^\pm,
\]

and every site has \(L_j^d=\sqrt{g/2}\,\sigma_j^z\). Here \(G>0\), \(0<f\leq1\), \(g\geq0\), and \(U\geq0\). The dynamics is the standard Lindblad master equation. Denote by \(j(g,G,U)=\langle I\rangle_\infty/f\) the stationary current divided by the positive bias. The stationary current itself is exactly proportional to \(f\) in this quadratic-expectation sector. The results concern this stationary current, not an initial-state transport efficiency or a thermodynamic-limit conductivity.

## Proof

**1. Exact current reduction.** The stationary Pauli-string moment equations of the cited model close in \(4^2=16\) unknown real coefficients. Solving them with no coherence truncation gives a compact exact resistance \(R=1/j\). Define the following polynomials, all evaluated at \((G,g)\):

\[
\begin{aligned}
A={}&G^2+6Gg+8g^2+16,\\
B={}&G^3+18G^2g+80Gg^2+160G+96g^3+480g,\\
C={}&G^3g+10G^2g^2+8G^2+32Gg^3+80Gg+32g^4+160g^2,\\
D={}&25G^3+436G^2g+1840Gg^2+912G+2496g^3+576g,\\
E={}&25G^2g+136Gg^2+72G+208g^3+48g.
\end{aligned}
\]

Write

\[
\begin{aligned}
P&=AB+4zD+2304z^2(G+12g),\\
Q&=AC+4z(G+4g)E+2304z^2g(G+4g).
\end{aligned}
\]

The exact result is

\[
\boxed{R(g,G,U)=\frac{16+G^2+6Gg}{16G}+\frac{zP}{8Q}.}
\]

All coefficients in \(P,Q\) are nonnegative and \(Q>0\) throughout the stated parameter domain. At zero field the second term vanishes, recovering the known exact current \(j=16G/(16+G^2+6Gg)\). The accompanying checker reconstructs the full original \(16\)-equation system and proves this rational identity symbolically. It separately recovers the published two- and three-site currents, fixing the dephasing and hopping normalizations.

**2. Exact monotonicity and strict convexity certificate.** Put \(F=zP/(8Q)\) and define the explicit polynomial numerators

\[
\begin{aligned}
W_1&=P\,\partial_g Q-(\partial_g P)Q,\\
W_2&=(\partial_g^2P)Q^2-P(\partial_g^2Q)Q
-2(\partial_gP)(\partial_gQ)Q+2P(\partial_gQ)^2.
\end{aligned}
\]

Direct expansion in the three nonnegative indeterminates \((G,g,z)\) gives **85 nonzero, strictly positive integer coefficients** in \(W_1\), and **224 nonzero, strictly positive integer coefficients** in \(W_2\). Their respective smallest coefficients are \(1\) and \(2\). The complete finite coefficient tests are implemented using exact integer polynomial arithmetic in `checker.py`, without interpolation, sampling or numerical positivity assumptions. Therefore

\[
\partial_gF=-\frac{zW_1}{8Q^2}<0,
\qquad
\partial_g^2F=\frac{zW_2}{8Q^3}>0
\quad\text{for }U>0.
\]

It follows that \(\partial_g^2R>0\) strictly for \(U>0\). Moreover \(F=O(g^{-1})\) as \(g\to\infty\), so \(\partial_gR\to3/8>0\). Strict convexity ensures at most one positive critical point of \(R\) and determines the entire global current profile from the derivative at zero.

**3. Exact onset and uniqueness of the threshold.** Let \(Q_0=Q(G,0,z)>0\). Expanding the derivative at zero and collecting yields the exact polynomial identity

\[
\boxed{\left.\partial_gR\right|_{g=0}=-\frac{G^2\Phi_G(z)}{8Q_0^2}.}
\]

The constant coefficient of \(\Phi_G\) is \(-192G^2(G^4+32G^2+256)<0\). Each nonconstant coefficient is strictly positive for \(G>0\); the only coefficient not manifestly positive in its original expanded form, that of \(z\), equals

\[
G^8+128G^2\bigl((G^2-6)^2+668\bigr)+2293760>0.
\]

Thus \(\Phi_G(z)\) is strictly increasing on \([0,\infty)\), starts below zero and tends to infinity. Its unique positive root is \(z_c(G)\). If \(\Phi_G(z)\leq0\), strict convexity of \(R\) proves that \(j=1/R\) strictly decreases on every positive dephasing interval; otherwise, strict convexity and the positive limiting slope prove exactly one interior maximum of \(j\).

**4. Two singular-coupling asymptotics.** With \(y=G^2\), the unique-root polynomial begins at small \((y,z)\) as \(2293760z-49152y+O(z^2+yz+y^2)\). Hence \(z_c\sim(3/140)G^2\). For \(G\to\infty\), substituting \(z=\beta/G^2\) and dividing by \(G^6\) gives \(\beta-192+o(1)\); uniqueness of the positive root yields \(z_c\sim192/G^2\). These imply the two displayed asymptotic laws.

## Verification

Run `python checker.py` with Python, SymPy and NumPy. This recomputes the stationary current from the full exact Pauli-string recurrence for chains of two, three and four sites; proves the compact resistance formula, checks all 85 and 224 integer-coefficient positivity certificates, checks the exact onset identity and compares against 150 independently constructed Hermitian covariance linear-system solutions. All these checks completed successfully using the embedded program.

The numerical value \(U_c(1)=0.1485390031\ldots\) is obtained by selecting the unique positive root of \(\Phi_1(U^2)\), not by inferring uniqueness from root-search experiments.

## Relationship to prior work

Jacob, Bettmann, Lacerda, Zawadzki, Clark, Goold and Mendoza-Arenas (arXiv:2407.21715) supply the Lindblad model, exact stationary recurrence and exact current optimization for two and three sites. For larger chains they give a nearest-coherence tridiagonal approximation and explicitly state that a compact exact current and optimal dephasing are not displayed. Their approximation does not imply the exact four-site strict-convexity certificate or the universal-in-\(G\) onset polynomial established here.

Žnidarič and Horvat (arXiv:1207.5952) study disordered boundary-driven chains and bulk conductivity. Their periodically diluted random disorder can display two maxima as a function of dephasing; it is a different potential pattern and parameter regime from the exact four-site *linear* potential. The theorem here neither contradicts nor extends their two-maximum result to other disorder patterns. The general finite-dimensional moment-solving method is established mathematics and is not claimed to be new.

## Limitations

The classification is exact only for four sites, a uniform linear tilt, the specified symmetric boundary baths and homogeneous local dephasing. It does not imply unimodality for arbitrary chain length, nonuniform disorder, interaction terms or nonlinear bath models. The threshold is a crossover in stationary transport optimization, not a thermodynamic phase transition. The exact polynomial and strict-convexity conclusion have undergone internal algebraic reproduction, but independent publication-priority verification and independent scientific audit have not been performed. The global number or location of the positive interior maxima of \(U_c(G)\) as a function of \(G\) is not determined.

## References

- S. L. Jacob, L. P. Bettmann, A. M. Lacerda, K. Zawadzki, S. R. Clark, J. Goold and J. J. Mendoza-Arenas, *Dephasing-assisted transport in a tight-binding chain with a linear potential*, arXiv:2407.21715v1, first public July 31, 2024. https://arxiv.org/abs/2407.21715 ; full lawful text https://arxiv.org/html/2407.21715v3 .
- M. Žnidarič and M. Horvat, *Transport in a disordered tight-binding chain with dephasing*, arXiv:1207.5952, first public July 25, 2012. https://arxiv.org/abs/1207.5952 .
