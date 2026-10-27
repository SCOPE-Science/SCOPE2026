# Critical chi and simplex laws for competing slow sites in a zero-range gas

## Finding

**Theorem.** Fix an integer \(r\ge2\), a rate contrast \(a>1\), a critical-window displacement \(\delta\in\mathbb R\), and a vector of site biases \(c=(c_1,\ldots,c_r)\in\mathbb R^r\). For each large integer \(M\), distribute
\[
N_M=\left\lfloor\frac{M}{a-1}+\delta\sqrt M\right\rfloor
\]
indistinguishable particles over \(r\) labelled slow sites and \(M\) ordinary sites. A nonempty ordinary site releases a particle at rate \(1\); nonempty slow site \(i\) releases one at total rate \([a\exp(c_i/\sqrt M)]^{-1}\). Each released particle goes to a uniformly selected *different* site. Let \(H_i\) be the stationary occupancy of slow site \(i\), and write \(S_M=\sum_{i=1}^r H_i\).

For sufficiently large \(M\), the chain is irreducible with unique stationary law. Put \(\sigma^2=a/(a-1)^2\). Then, jointly,
\[
\frac1{\sqrt M}(H_1,\ldots,H_r)\ \Longrightarrow\ X
\]
where \(X\) has the absolutely continuous probability density on \(\mathbb R_{\ge0}^r\)
\[
f_{\delta,c}(x)=\frac{\displaystyle\exp\!\left[-\frac{(\sum_{i=1}^r x_i-\delta)^2}{2\sigma^2}+\sum_{i=1}^r c_i x_i\right]}{\displaystyle I_{\delta,c}},\quad
I_{\delta,c}=\int_{\mathbb R_{\ge0}^r}\exp\!\left[-\frac{(\sum_i x_i-\delta)^2}{2\sigma^2}+\sum_i c_i x_i\right]dx.
\]
The integral is finite and positive. Convergence holds also for every mixed polynomial moment of the rescaled slow occupations.

In the tied-rate case \(c=0\), \(T=\sum_i X_i\) and \((X_1/T,\ldots,X_r/T)\) are independent: the latter has the uniform \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution on the simplex, while
\[
\mathbb P(T\in dt)=\frac{t^{r-1}e^{-(t-\delta)^2/(2\sigma^2)}\,dt}{\displaystyle\int_0^\infty u^{r-1}e^{-(u-\delta)^2/(2\sigma^2)}\,du},\quad t>0.
\]
In particular, at exact criticality \(\delta=0\),
\[
T\ \stackrel d=\ \sigma\chi_r.
\]
For two tied slow sites the total rescaled slow mass is Rayleigh distributed and the fraction on the first site is independent uniform on \([0,1]\). For general \(c\), the critical \(M^{-1/2}\) rate perturbation gives an exponential tilt of this simplex law, rather than a single-site winner-take-all limit.

**Exact finite-size law.** With \(s=\sum_i h_i\), the joint slow-site occupancy probability is
\[
\mathbb P(H=h)=\frac{a^s\exp(\sum_i c_i h_i/\sqrt M)\binom{N_M-s+M-1}{M-1}}{\displaystyle\sum_{\substack{g_i\ge0\\\sum_i g_i\le N_M}} a^{\sum_i g_i}\exp(\sum_i c_i g_i/\sqrt M)\binom{N_M-\sum_i g_i+M-1}{M-1}},
\quad h\in\mathbb Z_{\ge0}^r,\ \sum_i h_i\le N_M.
\]

## Assumptions and scope

All results concern the canonical stationary law, not a dynamical mixing-time or finite-time statement. The number \(r\) of slow sites is fixed while \(M\to\infty\); the constants \(a\), \(\delta\), and \(c\) do not vary with \(M\). The graph of permitted particle jumps is the complete graph on the \(M+r\) site labels, with uniform choices among the \(M+r-1\) other destinations. No exclusion constraint is imposed: each site permits arbitrarily many particles. For any fixed \(\delta\), \(N_M\ge0\) eventually. The empty state and finite exceptional small values of \(M\) are immaterial to the limit. The normalization of the Gaussian uses variance \(\sigma^2\), not \(1/\sigma^2\). We use the convention that a geometric random variable counts failures before one success.

## Proof

**1. Stationary measure and exact marginal.** Write \(w_i=a e^{c_i/\sqrt M}\) at slow site \(i\) and \(w_i=1\) elsewhere. The departure rate from a nonempty site is \(1/w_i\). For configurations differing by transfer of one particle from \(i\) to \(j\), the product weights \(\prod_\ell w_\ell^{n_\ell}\) satisfy detailed balance because the destination-selection factor \(1/(M+r-1)\) cancels and
\[
\left(\prod_\ell w_\ell^{n_\ell}\right)w_i^{-1}=\left(\prod_\ell w_\ell^{n_\ell-\mathbf1_{\ell=i}+\mathbf1_{\ell=j}}\right)w_j^{-1}.
\]
Every canonical configuration communicates with every other, so normalization yields the unique stationary probability. Given slow occupancies \(h\) with total \(s\), the remaining \(N_M-s\) particles occupy \(M\) ordinary sites in \(\binom{N_M-s+M-1}{M-1}\) compositions. This gives the exact formula.

**2. Reduction to a one-dimensional local limit.** Let \(B_M\) be the sum of \(M\) independent geometric random variables with probability \(\mathbb P(G=k)=(1-a^{-1})a^{-k}\) for \(k=0,1,\ldots\). Then \(\mathbb EB_M=M/(a-1)\), \(\operatorname{Var}B_M=M\sigma^2\), and
\[
\mathbb P(B_M=k)=\binom{k+M-1}{M-1}(1-a^{-1})^M a^{-k}.
\]
Multiplying the exact stationary numerator by the common \(h\)-independent constant \(a^{-N_M}(1-a^{-1})^M\) shows that the slow-occupation measure is proportional to
\[
\exp\!\left(\sum_i c_i h_i/\sqrt M\right)\mathbb P(B_M=N_M-\sum_i h_i).
\]
The lattice local central limit theorem for the geometric law (finite variance, span one) gives, uniformly for \(h_i/\sqrt M\) in any fixed compact subset of the positive orthant,
\[
\sqrt M\,\mathbb P(B_M=N_M-\sum_i h_i)
\longrightarrow \frac1{\sigma\sqrt{2\pi}}\exp\!\left[-\frac{(\delta-\sum_i h_i/\sqrt M)^2}{2\sigma^2}\right]
\]
in the sense of uniform convergence of the corresponding lattice-point densities.

**3. Uniform tail control.** This is needed to justify normalizing the local limit and taking moments. For \(p_M(k)=\mathbb P(B_M=k)\), the exact successive-mass ratio is
\[
\frac{p_M(k+1)}{p_M(k)}=\frac{k+M}{a(k+1)}.
\]
Its logarithm is strictly decreasing in \(k\) for \(M>1\), and it vanishes at \(k=(M-a)/(a-1)\). Summing the logarithms between an integer mode and \(k\le\mathrm{mode}\), and bounding the derivative
\[
-\frac{d}{dk}\log\frac{k+M}{a(k+1)}=\frac{M-1}{(k+M)(k+1)}
\]
from below by a constant multiple of \(M^{-1}\) throughout \(0\le k\le N_M\), gives constants \(C,\eta>0\), depending only on \(a,\delta\), with
\[
p_M(N_M-s)\le\frac C{\sqrt M}\exp\!\left[-\eta\left(\frac{s}{\sqrt M}-|\delta|-1\right)_+^2\right],\qquad0\le s\le N_M
\]
for all large \(M\); Stirling's bound \(\max_k p_M(k)\le C/\sqrt M\) controls the mode and any value above it. Here \(y_+=\max(y,0)\). Summing over the \(\binom{s+r-1}{r-1}\) slow-site compositions of \(s\), any degree-\(d\) polynomial in \(h/\sqrt M\), multiplied by the weak bias \(e^{\sum c_i h_i/\sqrt M}\), is dominated after Riemann rescaling by an integrable function proportional to
\[
(1+t)^{r+d-1}\exp[-\eta(t-|\delta|-1)_+^2+\|c\|_\infty t],\quad t\ge0.
\]
Thus local convergence on compacts extends to total mass, tightness, and all polynomial moments. The \(r\)-dimensional lattice Riemann sums converge to the stated orthant density, with the common factor \((\sigma\sqrt{2\pi})^{-1}\) cancelling on normalization.

**4. Tied-site radial and simplex laws.** When \(c=0\), the density depends only on \(t=\sum_i x_i\). The change of variables \(x_i=t p_i\), \(p_i\ge0\), \(\sum_i p_i=1\), has Jacobian proportional to \(t^{r-1}\). Its conditional angular density is constant on the simplex, hence Dirichlet with all parameters one, independently of \(t\). The stated radial density follows; for \(\delta=0\), it is exactly the density of \(\sigma\chi_r\). When \(c\ne0\), the extra factor \(e^{t\sum_i c_i p_i}\) yields the stated conditional exponential tilt. This completes the proof.

## Verification

The accompanying standard-library program `verify_stationary.py` independently solves the finite-state stationary master equations with exact rational arithmetic for four small systems (\(80\) labelled states in total) and compares them with the product weights. It also performs \(16\) independent exact hub-marginal identities. Direct finite canonical sums at \(M=100,400,1600,6400\) are compared against the chi-law mean for \(r=1,2,3\) (the one-site case is a boundary check), and against two independently integrated critical two-site biased expectations. All included assertions passed when executed. These finite and numerical checks support the proof but are not substitutes for the general lattice local-limit and uniform-tail arguments.

## Relationship to prior work

Stationary product measures and the canonical finite defect formula are classical zero-range methodology. Angel–Evans–Mukamel (2004) analyze a single site with occupation-dependent defect rates. Evans–Hanney (2005), especially the single-defect treatment in §5.2, explicitly calculate the single constant-rate defect partition function and thermodynamic critical density. Both cover premises and aspects of the one-defect object, not the stated finite-multiple-site joint critical-window law. Armendáriz–Grosskinsky–Loulakis (2009/2013) establish critical condensation scalings for **homogeneous** systems with occupancy-dependent decreasing rates, a different single-condensate mechanism. Mailler–Mörters–Ueltschi (2015) establish supercritical weak-disorder localization with randomized site weights and explicitly flag critical-window analysis as a separate issue; this theorem treats fixed deterministic near-tied sites instead, and does not resolve that random-disorder problem. These comparisons distinguish objects and exact implications, not merely titles. No absolute priority claim is made.

The distinguishing conclusion is the full joint stationary critical window for finitely many **constant-rate** defects, including the \(\chi_r\)-to-Dirichlet factorization at exact degeneracy and the \(M^{-1/2}\) rate-splitting tilt. The product-measure framework itself is not new.

## Limitations

This concerns a finite **fixed** number of defect sites on complete-graph dynamics. It says nothing about growing numbers of defects, disorder-averaged ensembles, occupation-dependent defect rates, non-complete routing, mixing times, dynamical metastability, or supercritical mass linear in \(M\). The result is not a claim that the entire infinite-volume gas condenses into a single site at criticality: each slow occupation is only order \(\sqrt M\). Prior broader product-measure theory can imply the finite stationary formula, and the novel asymptotic evaluation may yet occur in specialized work not located by the comparison.

## References

1. A. G. Angel, M. R. Evans, and D. Mukamel, *Condensation Transitions in a One-Dimensional Zero-Range Process with a Single Defect Site*, arXiv:cond-mat/0401262v1 (15 January 2004), https://arxiv.org/abs/cond-mat/0401262.
2. M. R. Evans and T. Hanney, *Nonequilibrium Statistical Mechanics of the Zero-Range Process and Related Models*, arXiv:cond-mat/0501338v1 (14 January 2005), https://arxiv.org/abs/cond-mat/0501338.
3. I. Armendáriz, S. Grosskinsky, and M. Loulakis, *Zero-range condensation at criticality*, arXiv:0912.1793v1 (9 December 2009), https://arxiv.org/abs/0912.1793.
4. C. Mailler, P. Mörters, and D. Ueltschi, *Condensation and symmetry-breaking in the zero-range process with weak site disorder*, arXiv:1509.07672v1 (25 September 2015), https://arxiv.org/abs/1509.07672.
