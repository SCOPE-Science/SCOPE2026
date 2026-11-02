# Fifth-order phase-memory resonance in a cat-driven circle map

## Finding

Consider the cat-driven circle skew product of Chigarev, Kazakov, and Pikovsky [1], at its unforced Möbius boundary \(\varepsilon=0\). With the driving Anosov map
\[
(t_{j+1},s_{j+1})=(2t_j+s_j,t_j+s_j)\pmod 1,
\]
and lifted driven coordinate
\[
\widetilde x_{j+1}=\widetilde x_j+c+\mu\sin(2\pi t_j+\alpha),
\]
put \(X_j=\sin(2\pi t_j+\alpha)\) and \(S_N=\sum_{j=0}^{N-1}X_j\). Start the cat coordinates with normalized Haar measure on \(\mathbb T^2\). Then, for every \(\alpha\in\mathbb R\), all distinct \(X_i,X_j\) are independent and every joint polynomial moment in the \(X_j\) of total degree at most four agrees with that of independent uniform-phase sine variables. Nevertheless, their first nontrivial Fourier resonance has order five:
\[
\mathbb E[X_j X_{j+1}^{3} X_{j+2}]=\frac{\sin\alpha}{16},\qquad j\geq0.
\]
Every signed zero-frequency relation containing at most five terms is either a cancellation at matching time indices or, up to reversing all signs and shifting time, the length-five relation \(v_j-3v_{j+1}+v_{j+2}=0\) described below. In particular, for \(\sin\alpha\ne0\), degree five is the **first degree of departure** from the independent-sine joint-moment law.

For every integer \(N\geq1\), the first five moments are exactly
\[
\begin{aligned}
\mathbb E S_N&=0, & \mathbb E S_N^2&=\frac N2,
&\mathbb E S_N^3&=0,\\
\mathbb E S_N^4&=\frac{3N(2N-1)}8,
&\mathbb E S_N^5&=\frac54\max(N-2,0)\sin\alpha.
\end{aligned}
\]
Thus the first five cumulants are
\[
\kappa_1(S_N)=0,\quad\kappa_2(S_N)=N/2,\quad\kappa_3(S_N)=0,\quad
\kappa_4(S_N)=-3N/8,\quad
\kappa_5(S_N)=\frac54\max(N-2,0)\sin\alpha.
\]
The centered lifted phase increment equals \(\widetilde x_N-\widetilde x_0-Nc=\mu S_N\); its cumulant of order \(k\) is therefore \(\mu^k\kappa_k(S_N)\) for \(1\le k\le5\). In particular, a nonzero forcing phase \(\sin\alpha\) produces a fifth-order non-Gaussian asymmetry despite pairwise independent kicks and a zero third cumulant.

## Assumptions and scope

The driving coordinates are Haar-uniform on \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), and the observations are stationary because the integer matrix \(A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\) preserves Haar measure. The parameters \(c,\mu,\alpha\) are real; \(N\) is a positive integer. There is no arithmetic restriction on the parameters. The calculation concerns the natural lift of the phase variable and the **exact slice \(\varepsilon=0\)**, rather than nonlinear forcing \(\varepsilon>0\). The central claims about \(S_N\) remain valid when \(\mu=0\), but the phase-displacement effect is then trivial. The moments are expectations over the random initial cat coordinates, not time averages along one prescribed orbit.

## Proof

**1. Characters and two-point independence.** Set \(e_1=(1,0)\) and \(v_j=(A^T)^j e_1\in\mathbb Z^2\). Then \(t_j=v_j\cdot(t_0,s_0)\pmod1\). Because \(A^2-3A+I=0\),
\[
v_{j+2}=3v_{j+1}-v_j.\tag{1}
\]
For distinct indices \(i,j\), the vectors \(v_i,v_j\) are linearly independent over \(\mathbb R\). Indeed, the eigenvalues \(\lambda=(3+\sqrt5)/2\) and \(\lambda^{-1}\) of \(A\) are different positive numbers, and \(e_1\) has nonzero components in both eigenvectors, so proportionality would require \(\lambda^{j-i}=\lambda^{-(j-i)}\). The integer map \((t_0,s_0)\mapsto(v_i\cdot(t_0,s_0),v_j\cdot(t_0,s_0))\pmod1\) is a surjective torus homomorphism and pushes Haar probability to Haar probability on \(\mathbb T^2\). Therefore \(t_i,t_j\), hence \(X_i,X_j\), are independent. Each \(X_j\) has the centered arcsine distribution, \(\mathbb E X_j^2=1/2\), \(\mathbb E X_j^4=3/8\).

**2. Exhaustive short Fourier relations.** We classify a signed vector relation \(\sum_{\ell=1}^{m}\sigma_\ell v_{j_\ell}=0\) with \(1\le m\le5\), \(\sigma_\ell\in\{-1,1\}\), and repeated indices allowed. The two eigenprojections of \(e_1\) are nonzero, so the relation is equivalent to *both* scalar identities
\[
\sum_{\ell=1}^{m}\sigma_\ell\lambda^{j_\ell}=0,
\qquad
\sum_{\ell=1}^{m}\sigma_\ell\lambda^{-j_\ell}=0.\tag{2}
\]
Cancel equal indices with opposite signs first. Suppose \(m>0\) remains. The positive and negative signs must both occur. A side containing only one term cannot equal a side containing at least two terms: if \(\lambda^a=\sum_{r=1}^k\lambda^{b_r}\) and \(\lambda^{-a}=\sum_{r=1}^k\lambda^{-b_r}\), then Cauchy–Schwarz makes the product of the right-hand sums at least \(k^2>1\), whereas the left-hand product is \(1\).

For \(m\le4\), this leaves only a two-plus/two-minus relation. The values \(\lambda^a+\lambda^b\) and \(\lambda^{-a}+\lambda^{-b}\) determine the unordered pair \(\{\lambda^a,\lambda^b\}\): their ratio determines the product \(\lambda^{a+b}\), after which the sum determines both roots of a quadratic. The pairs on either side therefore have identical indices. Hence **every relation of length at most four consists solely of cancelling pairs**.

At length five without a cancelling pair, there must be two indices \(a\le b\) on one side and three \(c\le d\le e\) on the other. Put \(h=b-a\), \(p=d-c\), \(q=e-d\), \(m'=p+q\). Write \(L_r=\lambda^r+\lambda^{-r}\), so \(L_0=2\), \(L_1=3\), \(L_2=7\), \(L_3=18\) and \(L_{r+2}=3L_{r+1}-L_r\). Multiplying the two scalar sum equalities in (2) gives the necessary identity
\[
L_h-1=L_p+L_q+L_{p+q}.\tag{3}
\]
Since the right side is at least six, \(h\ge2\). If \(h=2\), both \(p,q\) must be zero, and the scalar equalities now read \(\lambda^a+\lambda^{a+2}=3\lambda^c\), forcing \(c=a+1\). This is precisely the three-site relation in (1).

There are no solutions with \(h\ge3\). Indeed, if \(m'\ge h\), the right side of (3) is at least \(L_h+4\). If \(m'\le h-1\), use
\[
L_p+L_q\le L_{p+q}+2,
\]
which follows by expanding \((\lambda^p-1)(\lambda^q-1)+(\lambda^{-p}-1)(\lambda^{-q}-1)\ge0\). Then the right side is at most \(2L_{m'}+2\). For \(m'\ge2\), recurrence and \(L_{r+1}-2L_r-3=L_r-L_{r-1}-3>0\) for \(r\ge2\) yield \(L_h-1\ge L_{m'+1}-1>2L_{m'}+2\), a contradiction. For \(m'=0,1\), the right side is at most eight, whereas \(L_h-1\ge L_3-1=17\). Thus (1), shifted and sign-reversed, is the **unique noncancelling five-term relation**.

**3. Fourier moments and cumulants.** Expanding
\[
X_j=\sum_{\sigma=\pm1}\frac{\sigma e^{i\sigma\alpha}}{2i}
\exp\bigl(2\pi i\sigma v_j\cdot(t_0,s_0)\bigr)
\]
and integrating Haar characters gives zero unless the signed frequencies sum to zero. Through degree four, only pairwise cancellations are possible, exactly as for independent uniform-phase sines; this proves the assertion for **every joint polynomial moment** of total degree at most four. The two noncancelling sign assignments in \(X_jX_{j+1}^3X_{j+2}\) contribute
\[
\frac{e^{i\alpha}-e^{-i\alpha}}{32i}=\frac{\sin\alpha}{16}.\tag{4}
\]
They are the only anomalous order-five assignments. In \(S_N^5\), each consecutive triple contributes with multinomial multiplicity \(5!/3!=20\), and there are \(\max(N-2,0)\) such triples, giving \(\mathbb E S_N^5=20\max(N-2,0)\sin\alpha/16\). No purely independent odd-moment term survives. The other stated moments follow from \(\mathbb E X_j=0\), \(\mathbb E X_j^2=1/2\), and \(\mathbb E X_j^4=3/8\). The cumulants follow from the standard moment–cumulant formulas; because the mean and third moment vanish, the fifth cumulant equals the fifth moment. Scaling by \(\mu\) proves the lifted-phase statement.

## Verification

The standalone Python 3 program `checks/verify_fifth_resonance.py` performs exact-integer Fourier-frequency enumeration through degree five at 17 consecutive cat iterates. It verifies that every degree-two and degree-four relation is a pair cancellation, that exactly the expected consecutive three-site resonances occur at degree five, and that no degree-one or degree-three relation exists. It then computes exact rational moments of the cosine-phase case \(\alpha=\pi/2\) for \(1\le N\le10\), and checks 58 exact integer vector recurrences. Run with `python3 checks/verify_fifth_resonance.py` from the directory containing this file. These finite checks verify the algebra and selected instances; the all-time statement rests on the preceding analytical classification of (2) and (3).

## Relationship to prior work

Chigarev, Kazakov and Pikovsky [1] introduce exactly this three-torus map, interpret \(\mu\) as phase diffusion and \(\alpha\) as a phase shift, and investigate attractor–repeller collision, periodic-orbit bifurcations and Lyapunov statistics. Equation (1c) in their Section II gives the present forcing, and setting their \(\varepsilon=0\) yields the circle-shift slice studied here. Their inspected Section II–VII and appendix do not give the degree-five Fourier-resonance classification or these all-horizon phase cumulants. The lacunary-sum survey by Aistleitner, Berkes and Tichy [2], especially its Diophantine-frequency discussion, explains the general Fourier-relation method and the role of arithmetic dependencies in limit laws. That general machinery does not state the present exact minimal resonance nor the coefficients in (4). These results are an explicit map-specific complement, not a claim to have invented lacunary moment analysis. Dana and Chernov [3] concern a distinct perturbed cat map on a cylinder and a diffusion coefficient, not the present unperturbed cat-driven phase increment. An earlier unindexed computation of the same fifth-order statistic remains possible.

## Limitations

The theorem applies to the boundary \(\varepsilon=0\), not the nonlinear Möbius-fiber regime \(\varepsilon>0\). It establishes exact moments only through order five and does not classify higher-order resonances, give a central limit theorem, or characterize the complete law of \(S_N\). For \(\sin\alpha=0\) the fifth-order anomaly vanishes; degree five is the **first possible arithmetic resonance**, while no assertion is made about the first nonvanishing dependent moment in those special phases. Pairwise independence and agreement through fourth-order moments do **not** imply full joint independence. No independent mathematical audit has been performed.

## References

[1] V. Chigarev, A. Kazakov, A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1, first posted 2023-05-29. https://arxiv.org/html/2305.18172v1 ; https://arxiv.org/abs/2305.18172 .

[2] C. Aistleitner, I. Berkes, R. Tichy, *Lacunary sequences in analysis, probability and number theory*, arXiv:2301.05561v3, sections on Diophantine equations and probabilistic limit behavior. https://arxiv.org/html/2301.05561v3 .

[3] I. Dana, V. E. Chernov, *Chaotic diffusion on periodic orbits: The perturbed Arnold cat map*, Physical Review E **67** (2003), 046203. Abstract checked: https://doi.org/10.1103/PhysRevE.67.046203 .
