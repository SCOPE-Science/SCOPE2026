# One-sided initial opinions select extreme consensus in the incremental voter mean-field model

## Finding

**Theorem.** Fix an integer \(k\ge1\). In the Cao–Gong incremental voter mean-field system on \(\{-k,-k+1,\ldots,k\}\), suppose the initial probability distribution is supported on \(\{-k,\ldots,0\}\). If it assigns positive mass to at least one strictly negative opinion, then
\[
\lim_{t\to\infty}p_{-k}(t)=1.
\]
By reflection, initial support on \(\{0,\ldots,k\}\) with positive mass at a strictly positive opinion implies \(p_k(t)\to1\). The exclusion is necessary: initial concentration at opinion \(0\) evolves under the symmetric reflecting random walk and converges to the uniform distribution, not to either extreme. These are mean-field limits; no finite-population fixation-probability statement is made.

This settles the particular one-sided-support basin conjecture stated in the conclusion of Cao and Gong, arXiv:2605.28984v1, for **every** integer \(k\ge1\), without requiring an initial-mean threshold such as \(m(0)<1-k\).

## Assumptions and scope

Let \(p_x(t)\ge0\), \(\sum_{x=-k}^{k}p_x(t)=1\), and \(m(t)=\sum_{x=-k}^{k}x p_x(t)\). Put \(a(m)=(k+m)/(2k)\) and \(b(m)=(k-m)/(2k)\). The system is the reflecting nearest-neighbor nonlinear birth–death equation
\[
\dot p_x=a(m)p_{x-1}\mathbf1_{x>-k}+b(m)p_{x+1}\mathbf1_{x<k}
 -\big(a(m)\mathbf1_{x<k}+b(m)\mathbf1_{x>-k}\big)p_x.
\]
The indicators exclude nonexistent outside-boundary terms. This is equation (2.1) of the motivating source. The finite-dimensional vector field is polynomial and preserves the probability simplex, so solutions exist uniquely for all \(t\ge0\). Write \(\mu\preceq_{\rm st}\nu\) if the cumulative mass of \(\mu\) up to every interior opinion is **at least** that of \(\nu\).

## Proof

**1. Order comparison.** For \(-k\le j\le k-1\), write \(F_j(t)=\sum_{x=-k}^{j}p_x(t)\), set \(F_{-k-1}=0\), \(F_k=1\), and note \(m=k-\sum_{j=-k}^{k-1}F_j\). Summing the mass flux through the cut \(j\) gives
\[
\dot F_j=b(m)(F_{j+1}-F_j)-a(m)(F_j-F_{j-1}). \tag{1}
\]
At any distribution in the simplex, every off-diagonal partial derivative of the right side of (1) is nonnegative: for \(\ell\ne j\), it equals
\[
 b(m)\mathbf1_{\ell=j+1}+a(m)\mathbf1_{\ell=j-1}
 +\frac{p_j+p_{j+1}}{2k}\ge0. \tag{2}
\]
Thus the comparison principle for finite-dimensional cooperative systems applies; equivalently, it follows by the common-uniform coupling of reflecting nearest-neighbor update chains. Reflection of a distribution, \(p_x\mapsto p_{-x}\), commutes with the dynamics. Initial support on nonpositive states makes the initial law stochastically smaller than its reflection, so comparison implies \(m(t)\le0\) at every time.

Let \(p^{(0)}(t)\) solve the **linear**, reflecting, unbiased nearest-neighbor equation with the same initial distribution and fixed rates \(a=b=1/2\). Because \(m(t)\le0\), the nonlinear up rate never exceeds \(1/2\) and its down rate never falls below \(1/2\). Comparison therefore yields \(p(t)\preceq_{\rm st}p^{(0)}(t)\).

**2. The unbiased comparison eventually lies strictly below uniform.** Put \(n=2k+1\) and \(c=1/n\). The unbiased reflecting generator has orthogonal eigenfunctions
\[
 h_s(x)=\cos\!\left(\frac{s\pi(x+k+1/2)}{n}\right),\qquad
 s=0,1,\ldots,n-1,
\]
with eigenvalues \(-[1-\cos(s\pi/n)]\). In particular, \(h_1(x)>0\) for \(x<0\), \(h_1(0)=0\), and \(h_1(x)<0\) for \(x>0\). Our initial-data hypothesis gives \(A=\sum_xp_x(0)h_1(x)>0\). Hence the spectral expansion at large \(t\) is
\[
 p^{(0)}_x(t)-c=\frac{2A}{n}\,e^{-[1-\cos(\pi/n)]t}h_1(x)
 +O\!\left(e^{-[1-\cos(2\pi/n)]t}\right).
\]
For each interior cut \(j\), the first-mode prefix sum is
\[
 \sum_{x=-k}^{j}h_1(x)
 =\frac{\sin((j+k+1)\pi/n)}{2\sin(\pi/(2n))}>0.
\]
There are only finitely many cuts. Therefore some finite \(T\) satisfies \(F_j^{(0)}(T)> (j+k+1)c\) **for every** \(j=-k,\ldots,k-1\), and comparison gives the same strict inequality for \(F_j(T)\).

**3. Strict stochastic sub-uniformity cannot decay back to uniform.** Define \(D_j=F_j-(j+k+1)c\), with \(D_{-k-1}=D_k=0\), and \(S=\sum_{j=-k}^{k-1}D_j=-m\). Equation (1) becomes
\[
 \dot D_j=b(-S)D_{j+1}+a(-S)D_{j-1}-D_j+\frac{c}{k}S. \tag{3}
\]
Choose the strictly positive discrete parabola \(u_j=(j+k+1)(k-j)\) for the interior cuts, and \(u_{-k-1}=u_k=0\). Direct finite-difference calculation yields
\[
 \frac{u_{j-1}+u_{j+1}}2-u_j=-1,\qquad
 U:=\sum_j u_j=\frac{(2k+1)\,2k(k+1)}3.
\]
Consequently the linearization of the right side of (3) at \(D=0\), applied to \(u\), has all coordinates equal to
\[
 -1+\frac{cU}{k}=\frac{2k-1}{3}>0. \tag{4}
\]
For sufficiently small \(\varepsilon>0\), \(D=\varepsilon u\) corresponds to a legitimate probability vector and has **strictly positive** vector field in every coordinate: the correction to (4) is of order \(\varepsilon^2\). At time \(T\) every \(D_j(T)>0\), so we may also impose \(D_j(T)\ge\varepsilon u_j\). By cooperativity and the stationary-subsolution comparison applied to (3),
\[
 D_j(t)\ge\varepsilon u_j\quad(t\ge T),\qquad
 m(t)\le-\varepsilon U<0. \tag{5}
\]
This argument uses a finite-dimensional comparison principle, not an inference from a linear instability alone.

**4. Every persistent negative mean approaches the left endpoint.** For any frozen \(v\in(-k,0)\), the linear reflecting chain with up/down rates \(a(v),b(v)\) has the unique geometric stationary law
\[
 \pi_v(-k+j)=\frac{r^j}{Z(r)},\quad
 r=\frac{k+v}{k-v}\in(0,1),\quad
 Z(r)=\sum_{j=0}^{2k}r^j.
\]
Write its mean as \(f(v)=-k+rZ'(r)/Z(r)\). In fact, \(f(v)<v\) **strictly** for every \(-k<v<0\). To verify this for all integers \(k\ge1\), use the exact identity
\[
 (1+r)rZ'(r)-2krZ(r)=r(r-1)
 \sum_{j=0}^{2k-2}(j+1)(2k-1-j)r^j<0,\qquad 0<r<1. \tag{6}
\]
Every coefficient in the last sum is positive, and \(v=-k+2kr/(1+r)\), proving the inequality.

Let \(L=\limsup_{t\to\infty}m(t)\). Equation (5) gives \(-k\le L<0\). Whenever \(L<v<0\), eventually \(m(t)\le v\); from that time onward the nonlinear law is stochastically below the fixed-\(v\) reflecting chain started at the same distribution. This irreducible finite-state linear chain converges to \(\pi_v\), so \(L\le f(v)\). Letting \(v\downarrow L\), if \(L>-k\) we get \(L\le f(L)<L\), a contradiction. Hence \(L=-k\). Since \(m(t)\ge-k\), it follows that \(m(t)\to-k\). Nonnegativity gives \(1-p_{-k}(t)\le m(t)+k\to0\), as required.

Reflection proves the right-hand statement. Finally, when \(p_0(0)=1\), reflection symmetry forces \(m(t)=0\) and the linear unbiased reflecting chain relaxes to uniform, proving the exception.

## Verification

The standalone file `verify.py` reconstructs the polynomial factorization (6) with integer coefficients for \(1\le k\le40\), checks the exact discrete-parabola linearization (4), tests the stationary-mean inequality with rational arithmetic, checks signs of neutral eigenmode prefix sums, and integrates one-sided examples for \(1\le k\le6\). Run from the directory containing the file with `python3 verify.py`; it uses only the Python standard library. The general argument is the preceding proof, not the finite experiments. Exact spectral formulas and the sign factorization admit direct independent hand checks.

## Relationship to prior work

Cao and Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium* (arXiv:2605.28984v1, May 27, 2026), derive the governing ODE, prove the finite-agent extreme-consensus absorption statement, establish mean-field equilibria, and give sufficient attraction conditions based on means lying near either endpoint. Their Section 4 explicitly proposes one-sided-support convergence as an expectation from simulations, rather than as a proved all-\(k\) result. The present claim proves precisely that expectation on the stated support classes.

Berenbrink et al., *Discrete Incremental Voting* (arXiv:2606.06381, June 2026), study a distinct process in which the listener moves one step **toward** the sampled neighbor's actual opinion. Here the direction is instead sampled from the neighbor's absolute opinion through \((k+y)/(2k)\); the mean-field equations and possible equilibria differ. Cao and Reed's *Iterative Persuasion-Polarization Opinion Dynamics and Its Mean-Field Analysis* (arXiv:2408.00148; SIAM J. Appl. Math.) treats a persuasion/repulsion model with a distinct microscopic rule.

Stochastic-order comparison and the reflecting-walk spectrum are classical tools and are not claimed as new. The identified contribution is their combination with the explicit all-\(k\) positive subsolution and the frozen-chain geometric drift to settle the source's proposed basin assertion. Prior analyses of this same model's linearized uniform instability and relaxation rates *conditional on convergence* do not themselves imply the one-sided basin inclusion.

## Limitations

The result does not provide the full basin boundary for arbitrary initial distributions containing both positive and negative opinions. It does not quantify a uniform relaxation rate or finite-population fixation probability. The source's general unrestricted basin problem remains open. Historical priority beyond the inspected sources is provisional, including the possibility of coverage by broader monotone McKean–Vlasov birth–death theory. No independent external audit has been performed.

## References

1. F. Cao and X. Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984v1 (first posted May 27, 2026), especially equation (2.1), Section 3.2, and Section 4. https://arxiv.org/html/2605.28984
2. P. Berenbrink, C. Cooper, T. Götte, L. Hintze, and T. Radzik, *Discrete Incremental Voting*, arXiv:2606.06381 (June 2026), Sections 1–2. https://arxiv.org/abs/2606.06381
3. F. Cao and S. Reed, *The Iterative Persuasion-Polarization Opinion Dynamics and Its Mean-Field Analysis*, SIAM J. Appl. Math., doi:10.1137/24M1700661 (arXiv:2408.00148).
