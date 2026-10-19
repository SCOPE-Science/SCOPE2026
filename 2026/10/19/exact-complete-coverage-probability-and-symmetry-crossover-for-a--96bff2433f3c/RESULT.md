# Exact complete-coverage probability and symmetry crossover for alternating-rate dimer deposition on cycles

## Finding
On an even cycle, irreversible deposition of nearest-neighbor dimers with two alternating positive bond rates has an exact probability of *perfect* (vacancy-free) terminal coverage and a two-branch exponential asymptotic. The two branches exchange dominance at equal rates; tuning the rate contrast on the scale \(1/n\) gives an explicit hyperbolic-cosine crossover.

Write \(\alpha=a/(a+b)\), \(\beta=b/(a+b)\), where \(a,b>0\). For \(m\ge1\), define
\[
p_0(\alpha)=1,\qquad p_m(\alpha)=\frac{\alpha}{m-1+\alpha}\sum_{j=0}^{m-1}p_j(\alpha)p_{m-1-j}(\alpha).
\]
Then the complete-coverage probability on \(C_{2n}\) is, for every \(n\ge2\),
\[
Q_n(\alpha)=\alpha p_{n-1}(\alpha)+\beta p_{n-1}(\beta),\quad
\sum_{m\ge0}p_m(\alpha)z^m=\frac{{}_0F_1(;\alpha;\alpha\beta z)}{{}_0F_1(;\alpha-1;\alpha\beta z)}.
\]
For \(0<\alpha<1\), denote by \(R(\alpha)\) the smallest-modulus zero of \({}_0F_1(;\alpha-1;\alpha\beta z)\). It is real, positive, simple, unique on its modulus circle, and **strictly decreasing** in \(\alpha\). At fixed contrast,
\[
Q_n(\alpha)=R(\alpha)^{-n}+R(\beta)^{-n}
       +O(r_\alpha^{-n}+r_\beta^{-n}),\qquad
 r_\alpha>R(\alpha),\quad r_\beta>R(\beta).
\]
In particular, for \(\alpha\ne1/2\), the branch with the *larger* normalized rate uniquely dominates. At exact symmetry, \(Q_n(1/2)\sim2R_0^{-n}\), where \(R_0=s^2\approx1.4392288398906452\) and \(s\tanh s=1\), \(s>0\). For any fixed \(t\in\mathbb R\) and \(\alpha_n=1/2+t/n\),
\[
\lim_{n\to\infty}\frac{Q_n(\alpha_n)}{2R_0^{-n}}=\cosh(\kappa t),\qquad
\kappa=-\frac{R'(1/2)}{R_0}\approx1.0936467545844>0.
\]
The probability is of *zero terminal vacancies*, not the expected jamming coverage or a random choice of perfect matching.

## Assumptions and scope
The graph is the **simple** cycle \(C_{2n}\) with \(n\ge2\), hence at least four vertices. Each edge has an independent Poisson deposition-attempt clock with rate \(a\) or \(b\) according to edge parity. An attempted dimer is accepted only when both endpoint vertices are vacant; accepted dimers remain forever. Rejected attempts are discarded. Time is continued until no edge has two vacant endpoints. The event of interest is that every vertex is occupied by the time the process jams. Multiplying both rates by a common factor changes physical time but not the terminal event. All asymptotic statements let \(n\to\infty\) along integer ring half-sizes. The crossover statement requires \(n\) large enough that \(0<\alpha_n<1\).

## Proof
**1. First-event path recurrence and the cyclic cut.** On an open path of \(2m\) vacant vertices with bond rates \(a,b,a,\ldots,a\), exactly \(m\) bonds have rate \(a\) and \(m-1\) have rate \(b\). The first successful dimer has rate-weighted probability \(\alpha/(m-1+\alpha)\) at each odd-index (rate-\(a\)) bond. Choosing an even-index bond leaves two odd-length open components and makes perfect coverage impossible. Choosing bond \(2j+1\) splits the remaining sites into independent even-length components of sizes \(2j\) and \(2(m-j-1)\), each with alternating bonds beginning and ending at the same rate \(a\). Conditioning on the first accepted event therefore proves the displayed recurrence for \(p_m\) with \(p_0=1\). A first accepted bond on the even cycle has rate \(a\) with total probability \(\alpha\), or rate \(b\) with total probability \(\beta\). The remaining \(2(n-1)\) vertices form a path whose boundary bond type equals the selected cycle-bond type. This proves \(Q_n=\alpha p_{n-1}(\alpha)+\beta p_{n-1}(\beta)\).

**2. Hypergeometric generating function.** Let \(P(z)=\sum_{m\ge0}p_m(\alpha)z^m\). The recurrence gives the formal Riccati equation
\[
zP'(z)=\beta(P(z)-1)+\alpha z P(z)^2,\qquad P(0)=1.
\]
Set \(P(z)=-u'(z)/(\alpha u(z))\), with \(u(0)=1\), \(u'(0)=-\alpha\). Substitution gives \(zu''=\beta u'+\alpha\beta u\). Its unique analytic solution is \(u(z)={}_0F_1(;\alpha-1;\alpha\beta z)\), because the coefficient of \(z^m\) is \((\alpha\beta)^m/[m!(\alpha-1)_m]\); its derivative is \(u'(z)=-\alpha\,{}_0F_1(;\alpha;\alpha\beta z)\). This establishes the quotient formula as a formal identity and, wherever the denominator is nonzero, an analytic one.

**3. Dominant zero, residue, and exponential law.** Since \(0<\beta<1\), write \(u(z)=1-\sum_{m\ge1}d_m z^m\), where \(d_m=-(\alpha\beta)^m/[m!(\alpha-1)_m]>0\). The entire positive-coefficient sum increases strictly from zero to infinity on the positive real axis, giving a unique simple positive zero \(R\). If \(|z|\le R\) and \(u(z)=0\), triangle inequality forces \(|z|=R\); equality with all nonzero powers, especially consecutive powers \(1\) and \(2\), forces \(z=R\). Therefore \(R\) is the unique zero of least modulus. Entire-function zero isolation gives a disk of radius \(r>R\) containing no other denominator zero. The numerator is \(-u'(z)/\alpha\), so \(P\) has residue exactly \(-1/\alpha\) at \(z=R\). Subtracting its principal part and applying Cauchy's coefficient estimate gives \(p_m(\alpha)=\alpha^{-1}R(\alpha)^{-m-1}+O(r^{-m})\) for any such \(r\), yielding the two-branch formula for \(Q_n\).

**4. Strict monotonicity in rate contrast.** For \(0<\alpha_1<\alpha_2<1\), the path recurrence factor \(f_m(\alpha)=\alpha/(m-1+\alpha)\) obeys, for every \(m\ge2\),
\[
\frac{f_m(\alpha_2)}{f_m(\alpha_1)}\ge c:=\frac{\alpha_2(1+\alpha_1)}{\alpha_1(1+\alpha_2)}>1.
\]
Put \(d=\sqrt c>1\). Induction on the convolution recurrence, using \(p_0=1\), \(p_1=1\), and the fact that the two subinterval exponents sum to at least \(m-3\), proves \(p_m(\alpha_2)\ge d^{m-1}p_m(\alpha_1)\) for every \(m\ge1\). Cauchy–Hadamard then yields \(R(\alpha_2)\le R(\alpha_1)/d<R(\alpha_1)\), as claimed.

**5. Symmetric point and the crossover.** At \(\alpha=\beta=1/2\), the denominator simplifies to \(u(z)=\cosh\sqrt z-\sqrt z\sinh\sqrt z\); its least positive zero is \(R_0=s^2\) where \(s\tanh s=1\). All other zeros are separated from it. Since this simple zero depends analytically on \(\alpha\) in a neighborhood of \(1/2\), define \(\kappa=-R'(1/2)/R_0\). The derivative is strictly negative: at \(\alpha=1/2\), \(d_1'=1\), \(d_2'=0\), and for \(m\ge3\), \(-m d_m<d_m'<0\), by differentiating the Pochhammer product. Consequently
\[
\frac{\partial}{\partial\alpha}\left[\sum_{m\ge1}d_m(\alpha)R_0^m\right]_{\alpha=1/2}
>R_0-\sum_{m\ge3}m d_m(1/2)R_0^m
>R_0-\frac{R_0\cosh s}{2}>0.
\]
The last inequality uses \(s<5/4\) and \(\cosh(5/4)<2\); thus \(\partial_\alpha u(R_0)<0\), while \(\partial_z u(R_0)<0\), so \(R'(1/2)<0\). The uniform isolation of the simple leading pole in a neighborhood of \(1/2\) makes the coefficient asymptotics uniform there. For \(\alpha_n=1/2+t/n\), analyticity gives \(R(\alpha_n)=R_0[1-\kappa t/n+O(n^{-2})]\) and \(R(1-\alpha_n)=R_0[1+\kappa t/n+O(n^{-2})]\). Inserting them into the two-branch formula proves the stated \(\cosh(\kappa t)\) limit.

## Verification
The accompanying standalone `verify.py` independently enumerates the exact absorbing outcomes from every reachable vacancy mask on the cycle, without using the path decomposition, and compares these probabilities against the recurrence. All 35 combinations of ring half-sizes \(2\le n\le8\) and rate pairs \((1,1),(2,3),(3,1),(1,5),(5,1)\) agree as exact rational numbers. An independent formal division checks 21 coefficients of the hypergeometric ratio. Additional high-precision checks evaluate the symmetric root and derivative and verify two large-order coefficient asymptotics. Run `python verify.py` with Python 3 and `mpmath` installed. Exact tests do not depend on floating-point numerical results; the all-size proof is the five steps above.

## Relationship to prior work
Page's 1959 analysis of vacancies in homogeneous line deposition concerns the distribution of residual vacancies and may already imply the equal-rate specialization via its full moment sequence; **equal rates alone are not claimed new**. Pippenger's 1989 treatment of random sequential adsorption on graphs includes occupied-edge variants and marginal jamming-time/occupancy calculations; its accessible abstract does not imply the alternating-weight probability or symmetry window. De Oliveira and Tomé (1994) studied spatially inhomogeneous deposition and computed sublattice mean coverages on a line, a distinct observable from zero terminal vacancies on alternating-rate bonds. Purvis, Reeve, Wattis, and Mao (2015) studied scaling between availability and coverage close to jamming in random sequential adsorption; their accessible full manuscript does not derive the finite-cycle two-branch full-coverage law. The new mathematical information is the all-parameter *inhomogeneous* full-coverage law, its dominant spectral zero, and the sharp \(1/n\)-contrast crossover, not the homogeneous first-event method by itself.

## Limitations
The theorem addresses only nearest-neighbor irreversible dimers on simple even cycles, with strictly positive alternating rates, and the event of complete coverage. It does not describe the full terminal vacancy-count distribution or jamming time. The high-precision constants are numerical evaluations of exact characterizations, not numerical proofs. A complete full-text check of Page (1959), Pippenger (1989), and de Oliveira–Tomé (1994) was unavailable through the consulted access routes; these sources remain bibliographic overlap risks, especially for related inhomogeneous extensions not visible from abstracts. The result has not received independent scientific validation.

## References
- E. S. Page, “The Distribution of Vacancies on a Line,” *J. R. Statist. Soc. B* **21** (1959), 364–374. DOI: `10.1111/j.2517-6161.1959.tb00343.x`.
- N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM J. Discrete Math.* **2** (1989), 393–401. DOI: `10.1137/0402034`.
- M. J. de Oliveira and T. Tomé, “Inhomogeneous random sequential adsorption on bipartite lattices,” *Phys. Rev. E* **50** (1994), 4523–4527. DOI: `10.1103/PhysRevE.50.4523`.
- B. E. Purvis, L. Reeve, J. A. D. Wattis, and Y. Mao, “Scaling behavior near jamming in random sequential adsorption,” *Phys. Rev. E* **91** (2015), 022118, published February 17, 2015. DOI: `10.1103/PhysRevE.91.022118`.
- MSC2020 82C23, “Exactly solvable dynamic models in time-dependent statistical mechanics.”
