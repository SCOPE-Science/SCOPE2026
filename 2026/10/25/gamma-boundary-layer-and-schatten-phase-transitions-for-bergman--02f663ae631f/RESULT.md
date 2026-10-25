# Gamma boundary layer and Schatten phase transitions for Bergman disk-cutoff commutators

## Finding

For every \(\alpha>-1\), let \(A^2_\alpha(\mathbb D)\) be the analytic Bergman space with probability measure \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\). Put \(\beta=\alpha+1>0\), \(0<\varepsilon<1\), and let \(P_\varepsilon\) be the Toeplitz compression of the indicator of \(\{|z|^2<1-\varepsilon\}\). Let \(M_z\) be multiplication by the coordinate function and \(C_\varepsilon=P_\varepsilon M_z-M_zP_\varepsilon\).

**Exact singular spectrum.** Apart from their ordering, all singular values of \(C_\varepsilon\), counted with multiplicity, are
\[
s_k(\varepsilon)=\varepsilon^\beta(1-\varepsilon)^{k+1}c_k(\beta),\qquad
c_k(\beta)=\frac{\Gamma(k+\beta+1)}{\Gamma(\beta)\Gamma(k+2)}\sqrt{\frac{k+1}{k+\beta+1}},\qquad k=0,1,2,\ldots.
\]
Every value in this indexed sequence is positive, and \(C_\varepsilon\) belongs to every Schatten class \(\mathcal S_p\), \(0<p<\infty\), at each fixed \(\varepsilon\).

**Gamma edge law.** The finite positive measures
\[
\nu_\varepsilon=\sum_{k\ge0}s_k(\varepsilon)\,\delta_{\varepsilon(k+1)}
\]
converge weakly on \([0,\infty)\) as \(\varepsilon\downarrow0\) to the probability measure with density \(t^{\beta-1}e^{-t}/\Gamma(\beta)\). In particular,
\[
\lim_{\varepsilon\downarrow0}\|C_\varepsilon\|_{\mathcal S_1}=1,
\qquad \lim_{\varepsilon\downarrow0}\|C_\varepsilon\|=0.
\]
At each fixed cutoff, \(0<\|C_\varepsilon\|_{\mathcal S_1}<1-\varepsilon^\beta\).

**Complete sharp Schatten asymptotics.** For any fixed \(p>0\), put \(a=p(\beta-1)\). With \(\|C\|_{\mathcal S_p}^p=\sum_k s_k(C)^p\), the following are exact leading-equivalent asymptotics:
\[
\|C_\varepsilon\|_{\mathcal S_p}^p\sim
\begin{cases}
\displaystyle \varepsilon^{p\beta}\sum_{k\ge0}c_k(\beta)^p,&a<-1,\\[3pt]
\displaystyle \frac{\varepsilon^{p-1}\log(1/\varepsilon)}{\Gamma(\beta)^p},&a=-1,\\[6pt]
\displaystyle \frac{\Gamma(a+1)}{p^{a+1}\Gamma(\beta)^p}\,\varepsilon^{p-1},&a>-1.
\end{cases}
\]
The convergent series in the first case is an explicit positive constant. The logarithmic boundary is possible exactly when \(p>1\) and \(\alpha=-1/p\). Consequently \(\|C_\varepsilon\|_{\mathcal S_p}\to0\) for \(p>1\), approaches \(1\) for \(p=1\), and diverges for \(0<p<1\), even though the operator norm vanishes.

**Sharp operator-norm scale and its three modal regimes.** Let \(K_\beta=\max_{k\ge0}c_k(\beta)\) for \(0<\beta<1\); this maximum is finite and attained. Then
\[
\|C_\varepsilon\|\sim
\begin{cases}
K_\beta\varepsilon^\beta,&0<\beta<1,\\
\varepsilon,&\beta=1,\\
\displaystyle\frac{(\beta-1)^{\beta-1}e^{-(\beta-1)}}{\Gamma(\beta)}\varepsilon,&\beta>1.
\end{cases}
\]
If \(k_\varepsilon\) is any maximizing index, it stays bounded as \(\varepsilon\downarrow0\) when \(\beta<1\); at \(\beta=1\) every maximizing index obeys \(k_\varepsilon\sqrt\varepsilon\to1/\sqrt2\); and for \(\beta>1\), \(\varepsilon k_\varepsilon\to\beta-1\).

## Assumptions and scope

The measure \(dA\) denotes ordinary Euclidean planar area, and the Bergman probability measure is normalized exactly as above. The disk indicator uses strict inequality, immaterial on the boundary circle of measure zero. The parameters \(\alpha,p\) are fixed as \(\varepsilon\to0\); the theorem makes no uniform claim while they vary with \(\varepsilon\). For \(0<p<1\), the Schatten expression is a quasi-norm. The singular-value sequence is indexed by the orthonormal monomial modes, not asserted to be decreasing in that index. Weak convergence refers to finite measures tested against bounded continuous functions.

## Proof

**Diagonalization and normalization.** Write \(m_k=\int_{\mathbb D}|z|^{2k}\,d\mu_\alpha(z)=\beta B(k+1,\beta)\) and \(e_k=z^k/\sqrt{m_k}\). Rotational invariance gives \(P_\varepsilon e_k=\lambda_ke_k\), where \(\lambda_k=I_{1-\varepsilon}(k+1,\beta)\) is a regularized incomplete beta integral. Furthermore, \(M_ze_k=\sqrt{(k+1)/(k+\beta+1)}\,e_{k+1}\). Integration by parts (equivalently the elementary beta recurrence) gives, with \(x=1-\varepsilon\),
\[
I_x(k+1,\beta)-I_x(k+2,\beta)
=\frac{x^{k+1}(1-x)^\beta}{(k+1)B(k+1,\beta)}.
\]
Therefore \(C_\varepsilon e_k=-s_k(\varepsilon)e_{k+1}\). As the images of distinct basis vectors are orthogonal, the displayed positive weights are **exactly** the nonzero singular values with their index multiplicities; no truncation or finite-matrix approximation is used. Their exponential decay proves membership in every \(\mathcal S_p\) at fixed \(\varepsilon\). Since each shift weight is strictly smaller than one,
\[
\sum_{k\ge0}s_k(\varepsilon)
<\sum_{k\ge0}(\lambda_k-\lambda_{k+1})=\lambda_0=1-\varepsilon^\beta.
\]
The limit \(\lambda_k\to0\) follows from the fixed-cutoff beta integral.

**Gamma boundary layer.** Stirling's gamma-ratio formula gives
\[
c_k(\beta)\sim \frac{(k+1)^{\beta-1}}{\Gamma(\beta)},
\qquad c_k(\beta)\le C_\beta(k+1)^{\beta-1}
\quad(k\ge0),
\]
for some finite constant \(C_\beta\). For every \(0<u<v<\infty\), uniformly for modes with \(u\le\varepsilon(k+1)\le v\),
\[
\frac{s_k(\varepsilon)}{\varepsilon}
-\frac{(\varepsilon(k+1))^{\beta-1}e^{-\varepsilon(k+1)}}{\Gamma(\beta)}\longrightarrow0.
\]
Thus the measures converge against continuous functions supported in any compact subinterval of \((0,\infty)\) by ordinary Riemann summation. The bound above and \((1-\varepsilon)^{k+1}\le e^{-\varepsilon(k+1)}\) bound the total masses in \((0,\delta]\) by \(O_\beta(\delta^\beta+\varepsilon^\beta)\), and those in \([R,\infty)\) by a decaying gamma-tail majorant. Taking \(\delta\downarrow0\), \(R\uparrow\infty\) upgrades this to weak convergence of the full finite measures. The limiting gamma density integrates to one, proving the trace-norm limit.

**All Schatten regimes.** Raising the exact formula to power \(p\) yields
\[
\|C_\varepsilon\|_{\mathcal S_p}^p=
\varepsilon^{p\beta}\sum_{k\ge0}(1-\varepsilon)^{p(k+1)}c_k(\beta)^p.
\]
If \(a<-1\), the sum of \(c_k^p\) converges, and dominated convergence after division by \(\varepsilon^{p\beta}\) proves the first line. If \(a=-1\), the summand \(c_k^p\) is asymptotic to \(1/(\Gamma(\beta)^p(k+1))\). Splitting the sum at a fixed large index and then at \(1/\varepsilon\), and bounding the exponential tail, gives \(\Gamma(\beta)^{-p}\log(1/\varepsilon)(1+o(1))\). If \(a>-1\), the Riemann-sum and near-zero/tail domination used above apply with the exponent \(a\), producing
\[
\int_0^\infty e^{-pt}t^a\,dt=\frac{\Gamma(a+1)}{p^{a+1}}.
\]
The three limits follow, including the special case \(p=1\), where the constant is identically one and no logarithmic boundary is admissible.

**Operator norm and maximizing modes.** For \(0<\beta<1\), the asymptotic \(c_k\to0\) implies \(K_\beta\) is attained at finite index and that all maximizing modes remain in a fixed finite set for sufficiently small \(\varepsilon\). For \(\beta>1\), after scaling \(t=\varepsilon(k+1)\), the previous local limit, the vanishing bound near zero (because \(\beta-1>0\)), and the decaying upper bound in the tail show that all maximizing modes converge to the unique maximum of \(t^{\beta-1}e^{-t}\), at \(t=\beta-1\); its height gives the third norm constant. When \(\beta=1\), the exact formula reduces to \(s_k=\varepsilon(1-\varepsilon)^{k+1}\sqrt{(k+1)/(k+2)}\). The successive ratio satisfies
\[
\frac{s_{k+1}^2}{s_k^2}=
(1-\varepsilon)^2\frac{(k+2)^2}{(k+1)(k+3)}.
\]
It is at least one exactly when \((2\varepsilon-\varepsilon^2)(k+2)^2\le1\). Hence all maximum indices differ by at most two from \((2\varepsilon-\varepsilon^2)^{-1/2}\) and satisfy the stated square-root scale. Substitution into \(s_k\) gives the middle norm constant, closing the proof.

## Verification

The included `checker.py` reconstructs the beta-integral spectral weights independently using incomplete beta functions, diagonalizes finite-dimensional compressed commutator matrices, checks spectral identities for fractional and integer weights, and records finite-parameter comparisons with the asymptotic constants. Its finite computations are illustrative: the gamma limit, logarithmic boundary, and global optimizing-mode claims are proved analytically above. Execute with `python checker.py` in an environment containing NumPy and SciPy. An execution transcript is supplied in `checker_output.txt`.

## Relationship to prior work

The orthogonality of weighted Bergman monomials and radial Toeplitz eigenvalue formulas are classical, not asserted novel. Le and Simanek (2020) study hyponormality of weighted shifts plus radial diagonals, including commutator coefficients in their operator analysis. Bendaoud and collaborators (2020) study Schatten criteria for radial Toeplitz operators; Barrera-Castelán, Maximenko and Ramos-Vazquez (2020) give radial operator decompositions in polyanalytic weighted Bergman spaces. These are distinct from an exact **disk-cutoff/multiplier commutator** singular-value edge distribution with simultaneous sharp Schatten phase constants and modal boundary layers. This comparison does not constitute a proof of absolute novelty; a general abstract spectral theorem or an unlocated older computation might cover the special case.

## Limitations

Only the analytic weighted disk, a sharp radial indicator, and the single coordinate multiplier are treated. No smooth-symbol, higher-dimensional, polyanalytic, or uniform-in-parameter extension is claimed. At \(\beta<1\), the finite maximizing coefficient \(K_\beta\) is characterized by an explicit sequence, not generally simplified to a closed elementary formula. The results do not establish which prior authors first obtained any of the component formulas. Independent literature review has not been performed.

## References

1. Trieu Le and Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330, first submitted March 16, 2020; Sections 2–3.
2. Z. Bendaoud, S. Kupin, K. Toumache, B. Touré and R. Zarouf, *Toeplitz Operators with Radial Symbols on Bergman Space and Schatten-von Neumann Classes*, Journal of Mathematical Physics, Analysis, Geometry 16 (2020), 3–26, DOI:10.15407/mag16.01.003.
3. R. M. Barrera-Castelán, E. A. Maximenko and G. Ramos-Vazquez, *Radial Operators on Polyanalytic Weighted Bergman Spaces*, arXiv:2009.14301, first submitted September 29, 2020.
4. Euler beta-function recurrence and Stirling gamma-ratio asymptotics (standard special-function identities, used with full derivations of their applications above).
