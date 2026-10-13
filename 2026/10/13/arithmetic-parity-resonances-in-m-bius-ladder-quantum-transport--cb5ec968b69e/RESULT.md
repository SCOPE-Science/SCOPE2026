# Arithmetic parity resonances in Möbius-ladder quantum transport

## Finding
For each integer \(m\ge3\), let \(G_m=C_{2m}(1,m)\) be the cubic Möbius ladder with vertex set \(\mathbb Z/(2m)\), edges of cyclic displacement \(\pm1\) and of antipodal displacement \(m\). Let \(A_m\) be its adjacency matrix and let \(J\in\mathbb R\setminus\{0\}\). Define the mutually exclusive indicators
\[
 d_4(m)={\mathbf{1}}_{m\equiv2\pmod4},\qquad
 d_6(m)={\mathbf{1}}_{m\equiv3\pmod6},\qquad d(m)=d_4(m)+d_6(m)\in\{0,1\}.
\]
One positive-rate absorber at vertex \(0\) has a bright subspace of dimension \(m+1-d(m)\); two positive-rate absorbers at the antipodal pair \(\{0,m\}\) have bright dimension \(m+1\). For a maximally mixed initial state, their eventual absorption probabilities are, respectively,
\[
 P_1=\frac{m+1-d(m)}{2m},\qquad P_2=\frac{m+1}{2m}.
\]
In the absence of absorbers, define the infinite-time quantum transition averages
\[
 \chi_{s,0}=\lim_{T\to\infty}\frac1T\int_0^T
 |\langle s|e^{-itJA_m}|0\rangle|^2\,dt.
\]
Writing \(B_m=(2m-1)/(2m^2)\), the *same* arithmetic defect exactly controls antipodal asymmetry:
\[
 \chi_{0,0}=B_m+\frac{d_4(m)+2d_6(m)}{m^2},\qquad
 \chi_{m,0}=B_m-\frac{d_4(m)+2d_6(m)}{m^2},
\]
so \(\chi_{0,0}-\chi_{m,0}=2d_4(m)/m^2+4d_6(m)/m^2\). Thus return-versus-antipode asymmetry is present precisely when the second absorber restores one additional bright dimension. All three formulas hold for every \(m\ge3\), all nonzero real \(J\), and every fixed choice of strictly positive absorber strengths.

## Assumptions and scope
The one-walker Hilbert space is \(\mathcal H=\mathbb C^{2m}\), with standard orthonormal vertex vectors \(|j\rangle\). The absorbing no-jump generators are \(K_1=JA_m-i\gamma_0|0\rangle\langle0|\) and \(K_2=JA_m-i(\gamma_0|0\rangle\langle0|+\gamma_m|m\rangle\langle m|)\), where \(\gamma_0,\gamma_m>0\). The survival probability of any density matrix \(\rho\) is \(S_r(t;\rho)=\operatorname{tr}(e^{-itK_r}\rho e^{itK_r^*})\), and absorption is \(1-\lim_{t\to\infty}S_r(t;\rho)\). The stated values \(P_r\) use \(\rho=I/(2m)\). No claim is made for discrete-time coined dynamics, weighted rungs, additional onsite energies, or more general trap placements.

## Proof
**1. Fourier spectrum.** Define \(\zeta=e^{\pi i/m}\) and \(|k\rangle_F=(2m)^{-1/2}\sum_{j=0}^{2m-1}\zeta^{kj}|j\rangle\). For \(0\le k<2m\), direct multiplication gives
\[
 A_m|k\rangle_F=\lambda_k|k\rangle_F,\qquad
 \lambda_k=2\cos(\pi k/m)+(-1)^k.
\]
The equality \(\lambda_{2m-k}=\lambda_k\) identifies the ordinary reflection pairs. Among representatives \(0\le k\le m\), both even-indexed and odd-indexed sequences are strictly decreasing: an additional coincidence must have an odd index \(u\) and an even index \(v\) with \(u<v\) and
\[
 \cos(\pi u/m)-\cos(\pi v/m)=1. \tag{1}
\]

**2. Arithmetic collision lemma.** If \(0\le\theta<\phi\le\pi\) are rational multiples of \(\pi\) with \(\cos\theta-\cos\phi=1\), then
\[
 (\theta,\phi)\in\{(0,\pi/2),(\pi/3,2\pi/3),(\pi/2,\pi)\}. \tag{2}
\]
Indeed, \(2\cos\theta\) and \(2\cos\phi\) are algebraic integers, so if either cosine is rational then both are rational and belong to \(\{-1,-1/2,0,1/2,1\}\), giving the three pairs. If neither is rational, reflection of obtuse angles reduces their relation to a minimal rational linear combination of two cosines of angles strictly between \(0\) and \(\pi/2\), with coefficients of magnitude \(1\). The two-term case of Conway–Jones, Theorem 7 (1976), permits only the exceptional irrational relation \(\cos(\pi/5)-\cos(2\pi/5)=1/2\), up to signs and interchanging terms. Its rational right side has magnitude \(1/2\), not \(1\). Hence no irrational case is possible. This use of Theorem 7 is precisely the non-elementary arithmetic ingredient.

The first pair in (2) would force \(u=0\), impossible because \(u\) is odd. The second pair forces \((u,v)=(m/3,2m/3)\), valid exactly for \(m\equiv3\pmod6\). The third forces \((u,v)=(m/2,m)\), valid exactly for \(m\equiv2\pmod4\). These cases cannot occur simultaneously because the former requires odd \(m\) and the latter even \(m\). Therefore there is exactly one additional cross-parity eigenvalue collision if \(d(m)=1\), and none otherwise. The number of distinct eigenvalues is \(m+1-d(m)\). At a collision the two Fourier parity sectors have multiplicities \((2,2)\) if \(d_6=1\) and \((2,1)\) if \(d_4=1\); the reversed ordering is immaterial.

**3. Exact absorbing ranks.** For any Hermitian \(H\) and any positive diagonal loss operator supported on a set \(E\), the maximal loss-free invariant space is the direct sum, over distinct eigenvalues \(\lambda\) of \(H\), of \(\ker(H-\lambda I)\cap\ker P_E\). Its orthogonal complement is reducing for the no-jump generator. Any eigenvector on that complement with generator eigenvalue of zero imaginary part would satisfy \(\langle x,P_Ex\rangle=0\), hence give a forbidden loss-free eigenvector. All remaining eigenvalues have strictly negative imaginary part; finite dimensionality gives exponential decay on the bright complement. Thus the limiting survival of any initial \(\rho\) equals \(\operatorname{tr}(Q_E\rho)\), with \(Q_E\) the projection onto the loss-free invariant space.

For \(E=\{0\}\), every Fourier vector has nonzero amplitude \((2m)^{-1/2}\) at \(0\). Consequently the detector restriction has rank one on each distinct eigenspace, so the bright dimension equals the distinct-eigenvalue count \(m+1-d(m)\). For \(E=\{0,m\}\), the two detector amplitudes of the \(k\)-th Fourier mode are proportional to \((1,(-1)^k)\). Every unmixed eigenspace contributes rank one, and the sole possible mixed-parity eigenspace contributes rank two. Hence the two-detector bright dimension is \(m+1-d(m)+d(m)=m+1\). The absorption probabilities follow by dividing bright dimensions by \(2m\).

**4. Time-averaged transition probabilities.** Spectral averaging removes oscillatory cross terms with unequal eigenvalues. If an eigenspace contains \(e_\lambda\) even Fourier modes and \(o_\lambda\) odd modes, then
\[
 \chi_{0,0}=\frac1{4m^2}\sum_\lambda(e_\lambda+o_\lambda)^2,
 \qquad\chi_{m,0}=\frac1{4m^2}\sum_\lambda(e_\lambda-o_\lambda)^2.
\]
Without mixed-parity collisions, modes \(0,m\) contribute \(1\) each and each of the other \(m-1\) reflection pairs contributes \(4\), giving \(B_m=(2+4(m-1))/(4m^2)\). Merging one even block of size \(e\) with one odd block of size \(o\) increases \(\chi_{0,0}\) by \(2eo/(4m^2)\) and decreases \(\chi_{m,0}\) by the same amount. Substitution of \((e,o)=(1,2)\) or \((2,2)\) proves both formulas.

## Verification
The standalone program `verify.py` reconstructs the \(2m\)-vertex adjacency operators, checks their numerical spectra against the Fourier formula, computes *exact* cyclotomic remainders for the characteristic Fourier values for \(3\le m\le30\), verifies all predicted collision pairs and exact rational return/antipode averages, computes detector spectral ranks for \(3\le m\le14\), and tests the no-jump asymptotics by matrix exponentials in four small cases. Command: `python verify.py`; dependencies are listed in `requirements.txt`. Its observed completed output is `VERIFY_OK graph_numeric=28 exact_cyclotomic=28 asymmetry_rational=28 detector_rank_cases=24 long_time_cases=4`. These checks are finite; the theorem for all integers \(m\ge3\) follows from the analytical argument above and the cited Conway–Jones result.

## Relationship to prior work
The standard Möbius-ladder Fourier eigenvalue formula occurs in Norman Biggs, *Algebraic Graph Theory*, and in the accessible spectral-graph textbook *Teoria Espectral de Grafos*, Example 2.9. That input is prior work, not claimed as new. Conway and Jones (1976) classify the required two-cosine rational relation. Xu (arXiv:0812.3452v1) analyzes long-range interacting cycles and their quantum trapping and time-averaged transport, using a four-neighbor family and numerical trapping results; in the antipodal case its \(j\pm m\) indices coincide, unlike the cubic Möbius ladder's single rung. Agliari, Mülken and Blumen (arXiv:0903.3288v1) investigate trap configurations on ordinary rings. The assertion here is the *combined exact arithmetic classification* of parity collisions, the two-detector recovery effect, and the corresponding limiting quantum return asymmetry and absorption statistics for cubic Möbius ladders. None of those three papers or the inspected textbook section states this combined classification.

## Limitations
This is an exact finite-graph theorem, not a bound on finite-time absorption or mixing rates. It does not apply to a rung of arbitrary weight, additional onsite disorder, multiple excitations, or distinguishable-particle transport. The spectral formula and the general trapped-walk mechanism predate this result; an unlocated equivalent specialized classification could exist. The spectral book of Biggs was accessible through excerpts, not fully downloaded, so complete coverage by it is a residual literature risk.

## References
1. X.-P. Xu, *Coherent exciton transport and trapping on long-range interacting cycles*, arXiv:0812.3452v1 (first public 2008-12-18), later Phys. Rev. E 79, 011117 (2009), DOI 10.1103/PhysRevE.79.011117.
2. E. Agliari, O. Mülken and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, arXiv:0903.3288v1 (2009-03-19).
3. J. H. Conway and A. J. Jones, *Trigonometric diophantine equations (On vanishing sums of roots of unity)*, Acta Arithmetica 30 (1976), 229–240, DOI 10.4064/aa-30-3-229-240, Theorem 7.
4. N. Biggs, *Algebraic Graph Theory*, Cambridge University Press, 1974, §3e, Möbius ladder eigenvalue formula.
5. N. Abreu, R. Del-Vecchio, V. Trevisan and C. Vinagre, *Teoria Espectral de Grafos — Uma Introdução*, III Colóquio de Matemática da Região Sul (2014), Example 2.9, explicit Möbius-ladder eigenvalue formula (public text: https://livrozilla.com/doc/752670/).
