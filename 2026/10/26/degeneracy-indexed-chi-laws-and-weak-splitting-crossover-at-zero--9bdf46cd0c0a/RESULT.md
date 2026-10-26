# Degeneracy-indexed chi laws and weak-splitting crossover at zero-range condensation onset

## Finding
Consider a totally asymmetric, occupation-independent zero-range process on a directed periodic ring with \(L\) ordinary sites and a fixed number \(r\geq2\) of distinguished slow sites. The former have departure rate one whenever nonempty; the latter have departure rates \(q\exp(-\theta_j/\sqrt L)\), for fixed \(0<q<1\) and fixed real parameters \(\theta_1,\ldots,\theta_r\). A departure transfers one particle clockwise; the total particle number is conserved. Set
\[
\rho_c=\frac{q}{1-q},\qquad v=\frac{q}{(1-q)^2},\qquad
N_L=\left\lfloor\rho_c L+\lambda\sqrt L\right\rfloor,
\]
where \(\lambda\in\mathbb R\) is fixed. Let \(K_{j,L}\) denote the occupation of slow site \(j\) in the unique canonical stationary law. Then
\[
\left(K_{1,L},\ldots,K_{r,L}\right)/\sqrt L
\ \Longrightarrow\ (Y_1,\ldots,Y_r),
\]
where the limiting density on \(\mathbb R_+^r\) is
\[
 f_{\lambda,\boldsymbol\theta}(\mathbf y)
 =\frac{1}{Z_{\lambda,\boldsymbol\theta}}
 \exp\left\{\sum_{j=1}^r\theta_j y_j
 -\frac{(\lambda-\sum_{j=1}^r y_j)^2}{2v}\right\},\qquad
 Z_{\lambda,\boldsymbol\theta}=\int_{\mathbb R_+^r}\exp\left\{\sum_j\theta_j y_j-\frac{(\lambda-\sum_jy_j)^2}{2v}\right\}d\mathbf y.
\]
The normalizer is finite and positive for all stated parameters. Polynomial moments of the scaled occupations converge as well.

At exact criticality with equal defect rates (\(\lambda=0\), all \(\theta_j=0\)), the total scaled slow-site mass \(S=\sum_jY_j\) obeys
\[
 \frac{S}{\sqrt v}\sim\chi_r,
 \qquad
 f_S(s)=\frac{2^{1-r/2}}{\Gamma(r/2)v^{r/2}}
 s^{r-1}\exp\!\left(-\frac{s^2}{2v}\right),\quad s>0.
\]
Independently of \(S\), the shares \((Y_1/S,\ldots,Y_r/S)\) are \(\operatorname{Dirichlet}(1,\ldots,1)\). Thus for two distinguished sites \(S\) is Rayleigh with \(\mathbb P(S>s)=\exp[-s^2/(2v)]\), and the share of one site is uniform on \([0,1]\).

For \(r=2\), \(\lambda=0\), and \((\theta_1,\theta_2)=(0,\theta)\), define \(h_0(s)=s\) and \(h_\theta(s)=(e^{\theta s}-1)/\theta\) for \(\theta\ne0\). The total mass has density proportional to
\[
 h_\theta(s)\exp[-s^2/(2v)],\qquad s>0,
\]
and, conditional on \(S=s\), the second slow site's mass has density \(e^{\theta y}/h_\theta(s)\) on \(0<y<s\). This is the nontrivial competition profile on the \(L^{-1/2}\) relative-rate scale at the condensation onset.

## Assumptions and scope
For each sufficiently large integer \(L\), the state space is the set of nonnegative integer occupation vectors of length \(L+r\) summing to \(N_L\). The directed ring has one clockwise outgoing edge per site. All departure rates are strictly positive; a site departs at its specified rate whenever it contains at least one particle and at rate zero when empty. Distinguished sites can occupy any distinct positions, because the stationary law below depends on the site rates, not on their locations. Both \(r\) and all the parameters are fixed while \(L\to\infty\). The rate \(q\exp(-\theta_j/\sqrt L)\) is less than one for all sufficiently large \(L\). The result concerns canonical equilibrium occupations, not relaxation times or evolving particles.

## Proof
**Step 1: exact canonical weights.** Write \(a_i\) for the departure rate at site \(i\). The finite irreducible zero-range chain has stationary distribution
\[
 \pi_L(\boldsymbol\eta)=\frac{1}{\mathcal Z_L}
 \mathbf1_{\{\sum_i\eta_i=N_L\}}\prod_{i=1}^{L+r}a_i^{-\eta_i}.
\]
Indeed, for any configuration \(\boldsymbol\eta\), an incoming jump from site \(i-1\) to site \(i\) has a predecessor only when \(\eta_i\ge1\). Its weighted incoming flux divided by \(\pi_L(\boldsymbol\eta)\) is then \(a_i\), equal to the corresponding contribution to the total outgoing flux. Summing around the ring proves global balance; irreducibility gives uniqueness.

**Step 2: exact negative-binomial conditioning.** Let \(B_L\) be a sum of \(L\) independent geometric random variables with \(\mathbb P(G=k)=(1-q)q^k\), \(k\ge0\). Then
\[
 \mathbb P(B_L=b)=\binom{L+b-1}{b}(1-q)^Lq^b,
 \quad\mathbb EB_L=\rho_cL,
 \quad\operatorname{Var}(B_L)=vL.
\]
Write \(\mathbf k=(k_1,\ldots,k_r)\) and \(|\mathbf k|=\sum_jk_j\). By multiplying all canonical weights by the same \(q^{N_L}(1-q)^L\) factor, the exact slow-site distribution is
\[
 \mathbb P(\mathbf K_L=\mathbf k)
 =\frac{\mathbf1_{\{|\mathbf k|\le N_L\}}
 \exp(\boldsymbol\theta\cdot\mathbf k/\sqrt L)
 \mathbb P(B_L=N_L-|\mathbf k|)}{H_L},
\]
with \(H_L\) the sum of the numerator over all \(\mathbf k\in\mathbb Z_+^r\). This identity is not an approximation.

**Step 3: critical local limit and uniform integrability.** The lattice local central limit theorem for the geometric sum gives, uniformly when \(\mathbf k/\sqrt L\) ranges in a compact subset of the positive orthant,
\[
 \sqrt L\,\mathbb P(B_L=N_L-|\mathbf k|)
 \longrightarrow\frac{1}{\sqrt{2\pi v}}
 \exp\left[-\frac{(\lambda-|\mathbf k|/\sqrt L)^2}{2v}\right].
\]
To justify the unbounded Riemann sums, use the exact negative-binomial mass formula and its log-concavity: for fixed \(q,\lambda\), uniformly for \(0\le b\le N_L\), there exist constants \(C,c>0\) such that
\[
 \mathbb P(B_L=b)\le\frac{C}{\sqrt L}
 \exp\left[-c\frac{((\rho_cL-b)_+)^2}{L}\right].
\]
This follows by Stirling's formula near the mode and summing the logarithms of the decreasing mass ratios \(\mathbb P(B_L=b-1)/\mathbb P(B_L=b)=b/[q(L+b-1)]\) below the mode, with exponentially small bounds below half the mode. Because the number of \(r\)-tuples with sum \(s\) equals \(\binom{s+r-1}{r-1}\), the displayed bound, multiplied by \(\exp(\|\boldsymbol\theta\|_\infty s/\sqrt L)\), gives a polynomial times a Gaussian tail in \(s/\sqrt L\). The same bound permits every fixed polynomial moment. Riemann summation therefore gives
\[
 L^{-(r-1)/2}H_L\longrightarrow
 (2\pi v)^{-1/2}Z_{\lambda,\boldsymbol\theta},
\]
and proves convergence of the joint distribution and all polynomial moments.

**Step 4: degeneracy and asymmetry.** For zero detuning and zero critical displacement, change coordinates from \(\mathbf y\) to \(s=\sum_jy_j\) and shares \(u_j=y_j/s\). The Jacobian contributes \(s^{r-1}\), and the uniform simplex volume is \(1/(r-1)!\). The distribution of \(s\) is therefore proportional to \(s^{r-1}e^{-s^2/(2v)}\), giving the stated chi normalization; the simplex fractions are uniform Dirichlet and independent of \(s\). For two slow sites with detuning only at the second site, integration over its occupancy from zero to \(s\) produces exactly \(h_\theta(s)\); conditioning on \(s\) leaves the displayed truncated-exponential law.

## Verification
The included standalone Python program reconstructs finite canonical weights both by direct composition enumeration and by negative-binomial coefficients; checks the exact stationary flux balance on small directed rings; compares critical finite-volume moments against the chi-family integrals for multiple sizes and parameters; and tests nonzero weak-rate detuning against the limiting integral. The recorded run completed 134 combinatorial and scaling checks, 24 detuning checks, and 631 generator-balance checks. The finite checks corroborate, but do not establish, the local-limit or infinite-volume arguments. To reproduce, run `python critical_defects_verify.py` with Python, NumPy and SciPy installed.

## Relationship to prior work
The factorized zero-range stationary law and single-defect canonical analysis are classical; Angel, Evans and Mukamel (2004) analyze a single defective site and finite-size density effects. Godrèche and Luck (2012), especially Appendix A, compute the weak-asymmetry profile of a **two-site system with a fixed total mass**; its tilt scale is the inverse of that mass. The present theorem instead retains an extensive fluctuating ordinary-site background, tunes total density within \(O(L^{-1/2})\) of its critical value, and resolves the complete **joint law on a fixed set of at least two slow sites**, including the chi-degeneracy hierarchy and rate splittings of order \(L^{-1/2}\). Armendáriz, Grosskinsky and Loulakis (2009) treat critical condensation generated by occupation-dependent decreasing rates in a homogeneous system, a different mechanism. Kocharovsky and Kocharovsky (2015), Section IX, give cut-off negative-binomial formulas for a two-energy-level ideal Bose trap with a single ground level and arbitrary degeneracy of the **excited** level. These precedents supply important ingredients but do not explicitly state this multi-slow-site joint critical distribution with independent weak splittings. This relationship assessment is based on inspected accessible material, not a claim of exhaustive priority.

## Limitations
The theorem assumes a fixed number of slow sites, occupation-independent departure rates, homogeneous ordinary-site rates, an exactly conserved particle number, and the stated Gaussian critical window. It does not cover a growing defect count, interacting zero-range rates that depend on occupation, disorder in the ordinary sites, the mixing time, or the complete supercritical crossover. A more general canonical Bose-gas theorem might imply a specialization; historical priority is not proven. Neither numerical comparisons nor the citations constitute independent scientific validation.

## References
- A. G. Angel, M. R. Evans and D. Mukamel, *Condensation Transitions in a One-Dimensional Zero-Range Process with a Single Defect Site*, first posted January 15, 2004; arXiv:cond-mat/0401262, DOI:10.1088/1742-5468/2004/04/P04001.
- C. Godrèche and J. M. Luck, *Condensation in the inhomogeneous zero-range process: an interplay between interaction and diffusion disorder*, first posted September 21, 2012; arXiv:1209.4749, especially Sections 2 and Appendix A.
- I. Armendáriz, S. Grosskinsky and M. Loulakis, *Zero Range Condensation at Criticality*, first posted December 9, 2009; arXiv:0912.1793.
- V. V. Kocharovsky and Vl. V. Kocharovsky, *Analytical theory of mesoscopic Bose-Einstein condensation in ideal gas*, first posted November 5, 2015; arXiv:1511.01610, especially Section IX.
- R. F. Zeng, *Research on Thermal Balance with Critical Density in the Zero-Range Process with many Defect Sites*, 2014, DOI:10.4028/www.scientific.net/AMR.977.191; only its publicly accessible abstract was examined.
