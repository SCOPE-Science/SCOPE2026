# A sharp dephasing threshold and a one-sided coherence correction in a four-site quantum wire

## Finding

A four-site linearly tilted, boundary-driven quantum wire has a **unique transition between dephasing-suppressed and dephasing-assisted steady current**. In the normalization below the transition occurs at a nearest-neighbor energy tilt
\[
 u_c=\sqrt{t_c}=0.303236990165122\ldots,
\]
where \(t_c\) is the unique positive zero of
\[
 P(t)=20736t^5+21024t^4+46225t^3+25410t^2+10305t-1200.
\]
For \(0\leq |u|\leq u_c\), current is strictly decreasing with the dephasing rate on \((0,\infty)\), and its global maximum is at zero dephasing. For \(|u|>u_c\), current strictly increases to a **unique positive-dephasing global maximum**, then strictly decreases. The positive optimum is the sole positive zero of the explicitly certified degree-twelve derivative numerator below.

A further part of the same four-site transport classification compares the exact current with the familiar nearest-neighbor-correlation (tridiagonal) closure. For **every nonzero tilt and every finite nonnegative dephasing rate**, that closure *strictly underestimates* the steady current. This gives a direction-of-error theorem at the first chain length where the closure is not exact.

## Assumptions and scope

There are four fermionic modes \(c_j\), \(j=1,2,3,4\), with Hamiltonian (\(\hbar=1\))
\[
 H=\sum_{j=1}^{3}(c_j^\dagger c_{j+1}+c_{j+1}^\dagger c_j)
       +u\sum_{j=1}^4(j-1)c_j^\dagger c_j.
\]
The Lindblad jump operators are \(c_1^\dagger\) (unit-rate injection), \(c_4\) (unit-rate extraction), and \(\sqrt\gamma\,c_j^\dagger c_j\) at all four sites (independent dephasing), with \(u\in\mathbb R\) and \(\gamma\geq0\). The dissipator convention is
\(\mathcal D[L]\rho=L\rho L^\dagger-\{L^\dagger L,\rho\}/2\).
The stationary particle current \(I(u,\gamma)\) is the extraction flux \(\langle c_4^\dagger c_4\rangle\), equivalently the conserved interior particle current. This is the infinite-bias, matched hopping/injection/extraction-rate specialization of the boundary-driven tilted-chain setting, with a dephasing normalization fixed by the stated jump operators.

Write \(t=u^2\), \(g=\gamma\). Define \(N(g,t)\) and \(D(g,t)\) by
\[
\begin{aligned}
N(g,t)=2[&8g^6+28g^5+(104t+94)g^4+(188t+157)g^3\\
&+(288t^2+142t+196)g^2+(144t^2+109t+117)g+36t+20],\\
D(g,t)={}&24g^7+124g^6+(336t+422)g^5+(1160t+941)g^4\\
&+(1176t^2+1624t+1373)g^3+(2332t^2+1426t+1331)g^2\\
&+(864t^3+1010t^2+1121t+645)g+144t^3+253t^2+385t+100.
\end{aligned}
\]
All coefficients of \(D\) are positive. In particular the following formula is well-defined on the complete stated domain:
\[
\boxed{\ I(u,\gamma)=\frac{N(\gamma,u^2)}{D(\gamma,u^2)}.\ }
\]

For \(t>0\), let \(I_{\mathrm{tri}}\) be the stationary current obtained by setting all correlations \(\langle c_i^\dagger c_j\rangle\) with \(|i-j|>1\) to zero within the retained stationary correlation equations. The resulting tridiagonal closure is
\[
I_{\mathrm{tri}}(g,t)=\frac{2g(2g+1)}{B(g,t)},\qquad
B(g,t)=6g^3+13g^2+(6t+5)g+t.
\]
At \(t=0\), this expression is extended by continuity wherever its displayed form is indeterminate.

## Proof

**1. Exact stationary linear system and uniqueness.** Put \(C_{ij}=\langle c_j^\dagger c_i\rangle\), \(h_{jj}=u(j-1)\), \(h_{j,j+1}=h_{j+1,j}=1\), \(R=\operatorname{diag}(1/2,0,0,1/2)\), and \(S=\operatorname{diag}(1,0,0,0)\). Taking the Lindblad adjoint on the quadratic observables gives the exact, closed covariance equation
\[
 \dot C=-i[h,C]-RC-CR+S-\gamma(C-\operatorname{diag}C).
\]
It holds even though the complete density matrix need not be Gaussian. For the difference \(X\) of two Hermitian stationary solutions, take the Hilbert-Schmidt inner product with \(X\). The commutator contributes zero, while the other terms yield
\[
0=-2\operatorname{tr}(RX^2)-\gamma\sum_{i\ne j}|X_{ij}|^2.
\]
Thus the first and fourth rows of \(X\) vanish. At stationarity the first-row commutator equation then forces the second row to vanish; induction along the connected chain forces the third row to vanish. Therefore the homogeneous system has only its zero solution for every \(u\in\mathbb R\), \(\gamma\geq0\). A stationary density matrix exists in finite dimension; hence every stationary state has the same covariance and current.

Write the four real diagonal entries and the six complex off-diagonal entries as sixteen real unknowns, ordered as \(\Re C_{ij}\) and then \(\Im C_{ij}\) for \(i<j\). The coefficient matrix of the above equation has determinant
\[
\det A=\frac{(2g+1)(4g^2+4g+16t+5)D(g,t)}{16}>0.
\]
Cramer's rule for \(C_{44}\), using the replacement-column minor, gives \(N/D\) as displayed. Both determinant and minor identities follow by finite polynomial expansion from the explicitly stated system and are verified by the standalone script.

**2. Exact one-sided closure error.** Restrict the same sixteen equations to diagonal and nearest-neighbor variables, replacing longer-range entries by zero. Solving this smaller linear system gives \(I_{\mathrm{tri}}\). Exact subtraction yields
\[
\boxed{
I(u,g)-I_{\mathrm{tri}}(g,u^2)=
\frac{8t\bigl[2g^3+5g^2+(18t+8)g+9t+5\bigr]}{B(g,t)D(g,t)}.}
\]
For \(t>0\) and \(g\geq0\) every factor in the fraction is positive; for \(t=0\), the two expressions coincide by continuity. This establishes strict, global underestimation, not merely a numerical comparison at a few parameter values.

**3. Sharp optimization.** Differentiate \(I=N/D\):
\[
\frac{\partial I}{\partial g}=\frac{Q(g,t)}{D(g,t)^2},\qquad
Q=(\partial_gN)D-N(\partial_gD).
\]
The coefficients \(q_k(t)=[g^k]Q(g,t)\) satisfy \(q_k(t)<0\) for every \(t\geq0\) and \(4\leq k\leq12\). The remaining four are
\[
\begin{aligned}
q_0&=2P(t),\\
q_1&=8(20736t^5+46656t^4+45539t^3+17541t^2+6612t-3510),\\
q_2&=2(248832t^5+158976t^4+259588t^3+13311t^2-8604t-64587),\\
q_3&=8(11520t^4+21592t^3-49439t^2-31690t-39108).
\end{aligned}
\]
For each \(k=0,1,2,3\), the polynomial \(q_k(t)\) has exactly one positive zero by Descartes' rule (its nonzero coefficients, ordered by descending powers of \(t\), have one sign change). Their zeros lie, respectively, in the **disjoint rational intervals**
\[
 (9/100,1/10),\quad (1/5,1/4),\quad(1/2,3/5),\quad(9/5,2).
\]
The endpoint signs are exact integer inequalities. Thus the zeros increase strictly with \(k\).

If \(0\leq t\leq t_c\), all coefficients of \(Q(g,t)\) are nonpositive and those at positive powers are strictly negative: \(\partial_g I<0\) for every \(g>0\). If \(t>t_c\), the coefficient sequence \((q_{12},\ldots,q_0)\) has **exactly one** sign change. Since \(Q(0,t)=2P(t)>0\) and the leading coefficient of \(Q\) is negative, Descartes' rule and continuity imply exactly one positive zero \(g_*(t)\). It is simple and \(Q\) changes from positive to negative there. Because \(I(g,t)\to0\) as \(g\to\infty\), this zero is the unique global maximum. The polynomial \(P\) is strictly increasing for \(t\geq0\), has a negative value at zero, and tends to infinity: \(t_c\) is unique. The complete classification follows.

## Verification

Execute `python reproduce.py` from the extracted directory. The script independently reconstructs the sixteen real stationary covariance equations, checks the full determinant, exact current, tridiagonal-closure error, derivative-coefficient signs and rational root brackets. It also compares five parameter points against **the original sixteen-dimensional fermionic Fock-space Lindblad evolution**, solved as a \(256\times256\) stationary linear system using NumPy. All checks passed with SymPy, NumPy and SciPy installed. These finite checks support, but do not replace, the algebraic and sign proof.

For example, at \(u=0.4\) the exact dephasing optimum is approximately \(\gamma_*=0.0894560\), whereas at \(u=0.2\) the current decreases from zero dephasing onward. The threshold refers to the stated rate normalization; other bath-rate normalizations require conversion.

## Relationship to prior work

Jacob, Bettmann, Lacerda, Zawadzki, Clark, Goold and Mendoza-Arenas (2024), *Dephasing-assisted transport in a tight-binding chain with a linear potential*, present exact small-chain results for sizes two and three, a correlation-matrix linear system for general size, and a useful tridiagonal approximation. Their Secs. 3.1–3.3 explicitly do not display the exact size-four current or its optimal-dephasing criterion. These underlying equations and the physical phenomenon are prior work. The claim here is the sharp **four-site threshold, one-maximum theorem, and one-sided closure-error inequality**, which do not follow just from the published approximation.

Coates, Lovett and Gauger (2021) explore optimal noise versus localization on chains, but their readout/reinjection model is different (extraction followed by distributed reinjection). Contreras-Pulido, Bruderer, Huelga and Plenio (2014) analyze dephasing-assisted transport in a three-dot configuration, not the four-site tilted infinite-bias wire. These studies motivate the optimization question but do not state the present exact finite-chain classification. A generic algorithm for solving the stationary covariance system is not itself asserted to be new.

## Limitations

All statements are exact for four sites with hopping strength and both boundary jump rates normalized to one, perfect left-to-right bias, an exactly linear tilt, and local Markovian dephasing in the specified convention. No global shape claim is made for arbitrary chain length or unequal bath rates, nor does the result establish a many-body interacting extension, phase transition in the thermodynamic limit, or universality across different dephasing mechanisms. The search and literature comparison may miss an independently derived equivalent four-site formula or theorem; independent priority review is still needed.

## References

1. S. L. Jacob et al., *Dephasing-assisted transport in a tight-binding chain with a linear potential*, arXiv:2407.21715 (initially public 2024-07-31); *Frontiers in Physics* **12**, 1474018 (2024), DOI: 10.3389/fphy.2024.1474018. Full text: https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2024.1474018/full
2. A. R. Coates, B. W. Lovett and E. M. Gauger, *Localisation determines the optimal noise rate for quantum transport*, arXiv:2106.12567; *New Journal of Physics* **23**, 123014 (2021), DOI: 10.1088/1367-2630/ac3b2c.
3. L. D. Contreras-Pulido, M. Bruderer, S. F. Huelga and M. B. Plenio, *Dephasing-assisted transport in linear triple quantum dots*, arXiv:1407.0924; *New Journal of Physics* **16**, 113061 (2014).
