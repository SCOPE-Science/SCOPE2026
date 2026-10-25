# Two-axis Minkowski symmetrization: arithmetic resonance and a \(t^{1/3}\) area-deficit law

## Finding
Fix \(\sigma>0\), set \(\delta_\sigma=(1-e^{-\sigma})/4\), and let \(K_0\) be the strictly convex real-analytic planar body with support function
\[
h_\sigma(\theta)=1+\delta_\sigma\sum_{m=2}^{\infty}\frac{e^{-\sigma m}}{m^2}\cos(m\theta).
\]
Fix an angle \(0<\alpha<\pi\). Independently at each integer time, choose one of the two lines of angle \(0\) and \(\alpha\), each with probability \(1/2\), and perform Minkowski symmetrization with respect to that line. Write \(K_t\) for the resulting body and \(D_t=\pi-\operatorname{Area}(K_t)\), its isoperimetric area deficit (the perimeter stays \(2\pi\)). Then for **every** integer \(t\geq0\),
\[
\boxed{\mathbb E D_t=\frac{\pi\delta_\sigma^2}{2}\sum_{m=2}^{\infty}\frac{(m^2-1)e^{-2\sigma m}}{m^4}\left(1-\frac12\sin^2(m\alpha)\right)^t.}
\]
If \(\alpha/\pi=p/q\) is rational in lowest terms, \(\mathbb E D_t\) converges geometrically to the strictly positive quantity
\[
\frac{\pi\delta_\sigma^2}{2}\sum_{\substack{m\ge2\\q\mid m}}\frac{(m^2-1)e^{-2\sigma m}}{m^4}.
\]
If \(\alpha/\pi\) is irrational, \(\mathbb E D_t\to0\), but there is **no** upper bound \(\mathbb E D_t\le C\rho^t\) valid for all large \(t\), for any fixed \(C<\infty\) and \(0<\rho<1\). If, in addition, \(\alpha/\pi\) has bounded continued-fraction partial quotients, then there are positive constants \(c,C\) (depending on \(\sigma,\alpha\)) and \(t_0\) such that
\[
\boxed{e^{-Ct^{1/3}}\le\mathbb E D_t\le e^{-ct^{1/3}}\qquad(t\ge t_0).}
\]
In particular, this sharp stretched-exponential order holds for \(\alpha=\pi(\sqrt5-1)/2\).

## Assumptions and scope
A line angle \(\beta\) means the undirected line spanned by \((\cos\beta,\sin\beta)\). For a convex body \(K\), its Minkowski symmetral about the line is \((K+R_\beta K)/2\), where \(R_\beta\) is reflection in that line; Minkowski addition and positive scalar multiplication are in the usual geometric sense. The random line choices are independent, equiprobable, and independent of the initial body. The value \(\sigma>0\) is fixed. All expectations are with respect to these random choices only. The rational and irrational conclusions concern the same explicit body \(K_0\), not an arbitrary convex body.

The support series and its first two derivatives converge uniformly. Indeed
\[
h_\sigma+h_\sigma''=1-\delta_\sigma\sum_{m=2}^\infty (1-m^{-2})e^{-\sigma m}\cos(m\theta)
\ge1-\delta_\sigma\frac{e^{-2\sigma}}{1-e^{-\sigma}}>\frac34.
\]
Hence \(h_\sigma\) is the support function of a positively curved strictly convex body. Exponential Fourier decay also makes it real analytic. Its constant support coefficient is \(1\), so its perimeter is \(2\pi\), and every Minkowski symmetrization retains that perimeter.

## Proof
**Support-harmonic projection.** A reflection in a line at angle \(\beta\) sends \(\theta\mapsto2\beta-\theta\). Accordingly, Minkowski averaging sends the coefficient vector \((a_m,b_m)\) of \(a_m\cos m\theta+b_m\sin m\theta\) to its Euclidean orthogonal projection onto \(e_m(\beta)=(\cos m\beta,\sin m\beta)\). No frequency is mixed. Initially \((a_m,b_m)=(\delta_\sigma e^{-\sigma m}/m^2,0)\) for \(m\ge2\).

After any symmetrization, the nonzero coefficient vector of a fixed frequency lies on one of the two lines spanned by \(e_m(0)\) and \(e_m(\alpha)\). Conditional on its squared length, the next projection retains that length with probability \(1/2\) and multiplies it by \(\cos^2(m\alpha)\) with probability \(1/2\). Thus its conditional expected squared-length multiplier is always
\[\lambda_m=\tfrac12(1+\cos^2(m\alpha))=1-\tfrac12\sin^2(m\alpha).\]
The same multiplier holds for the first step because the initial vector is parallel to \(e_m(0)\). Consequently
\[\mathbb E(a_{m,t}^2+b_{m,t}^2)=\delta_\sigma^2e^{-2\sigma m}m^{-4}\lambda_m^t.\]

**Area identity.** For a smooth planar support function \(h\), \(\operatorname{Area}(K)=\tfrac12\int_0^{2\pi}(h^2-(h')^2)\,d\theta\). Fourier orthogonality yields
\[\operatorname{Area}(K)=\pi a_0^2-\frac\pi2\sum_{m\ge2}(m^2-1)(a_m^2+b_m^2)\]
when the translation harmonic is absent. Here \(a_0=1\) and the first harmonic is initially zero and stays zero. Substitution and monotone convergence of the positive series prove the exact formula for every \(t\ge0\).

**Rational resonance.** If \(\alpha/\pi=p/q\) in lowest terms, \(\lambda_m=1\) exactly for multiples of \(q\), and the remaining multipliers belong to finitely many residue classes with a common upper bound strictly below \(1\). Splitting the uniformly summable series therefore gives the stated positive limit and a geometric error bound. The positive limit reflects modes invariant under both reflections.

**Irrational decay without a geometric rate.** If \(\alpha/\pi\notin\mathbb Q\), then \(\lambda_m<1\) for every integer \(m\ge2\), so dominated convergence shows \(\mathbb E D_t\to0\). Density of the irrational rotation \(m\alpha\) modulo \(\pi\) implies \(\sup_{m\ge2}\lambda_m=1\). Since every coefficient weight in the exact series is strictly positive, for any \(\rho<1\) one can select a fixed \(m\) with \(\lambda_m>\rho\), and its single summand precludes an eventual bound by \(C\rho^t\).

**Sharp exponent for bounded-type angles.** Put \(x=\alpha/\pi\), and let \(\|y\|\) denote distance to the nearest integer. Bounded continued-fraction partial quotients give \(\|mx\|\ge\kappa/m\) for some \(\kappa>0\) and all positive integers \(m\). Since \(|\sin(\pi y)|\ge2\|y\|\),
\[\lambda_m^t\le\exp(-2\kappa^2t/m^2).\]
Consequently the exact sum is bounded by a constant times
\[\sum_{m\ge2}m^{-2}\exp(-2\sigma m-2\kappa^2t/m^2).\]
Minimizing \(\sigma m+2\kappa^2t/m^2\) over positive real \(m\) gives a positive multiple of \(t^{1/3}\); retain the other factor \(e^{-\sigma m}\) to sum a convergent geometric tail. This proves \(\mathbb E D_t\le C_1e^{-c_1t^{1/3}}\), whose prefactor can be absorbed into the exponent by increasing \(t_0\).

For the lower bound, let \(q_j\) be the continued-fraction convergent denominators of \(x\). Bounded partial quotients imply \(q_{j+1}\le Bq_j\) for some \(B<\infty\), while \(\|q_jx\|<1/q_{j+1}<1/q_j\). For every large \(t\) select \(j\) with \(q_j\le t^{1/3}<q_{j+1}\); thus \(t^{1/3}/B<q_j\le t^{1/3}\). Since \(|\sin(q_j\alpha)|\le\pi/q_j\) and \(\log(1-v/2)\ge-v\) for \(0\le v\le1\),
\[\lambda_{q_j}^t\ge\exp(-\pi^2t/q_j^2).\]
Keeping just the positive \(m=q_j\) summand gives \(\mathbb E D_t\ge c_2t^{-2/3}e^{-C_2t^{1/3}}\), and the polynomial factor can be absorbed by increasing the exponential constant. This proves the matching lower bound. The golden-ratio conjugate has bounded partial quotients, establishing the stated example.

## Verification
The standalone Python program `check_two_axis_symmetry.py` calculates the harmonic projections directly for every one of the \(2^t\) axis sequences for \(0\le t\le8\), independently computes areas from discretized support-function boundary curves, checks the rational nonzero area-deficit limit, and evaluates the log-defect trend for large iteration counts for a golden-ratio angle. Run it with `python check_two_axis_symmetry.py` using a standard Python 3 installation. The finite checks corroborate the proof; they do not prove the universal infinite-series or asymptotic statements.

## Relationship to prior work
Klartag's 2003 paper develops harmonic methods for choosing rapidly rounding Minkowski symmetrization directions, not random repeated choices between two fixed lines. Klain's 2011 paper proves convergence with finite direction sets for Steiner symmetrization. Coupier and Davydov's 2012 work proves almost-sure exponential rounding under an absolute-continuity assumption on random Minkowski directions, which excludes this two-atom distribution. Bianchi, Gardner and Gronchi (2019) extend finite-direction convergence results to Minkowski symmetrization and explicitly leave corresponding rate questions to further investigation. A related 2026 result treats uniform random axes and the covariance and typical rate of area deficits, whereas the present theorem isolates rational resonances and irrational small-divisor effects from two atomic angles. The projection formalism overlaps these works; the precise two-axis expected-area law and the bounded-type exponent are not asserted as consequences of their published statements. Historical priority beyond the inspected sources is not certified.

## Limitations
This theorem concerns **expected isoperimetric area deficit** for the displayed real-analytic body and iid equiprobable choices of **exactly two** mirror lines. It does not give a sample-path rate, a Hausdorff-distance rate, a universal rate for all convex bodies, or a leading stretched-exponential constant. The \(t^{1/3}\) assertion assumes bounded continued-fraction coefficients; for general irrational angles only convergence and the obstruction to a uniform exponential rate are proved. Definitive historical priority beyond the inspected sources has not been established.

## References
1. B. Klartag, *Rate of convergence of geometric symmetrizations*, first public 2 December 2003, arXiv:math/0312064, https://arxiv.org/abs/math/0312064.
2. D. A. Klain, *Steiner symmetrization using a finite set of directions*, first public 4 May 2011, arXiv:1105.0868, https://arxiv.org/abs/1105.0868.
3. D. Coupier and Yu. Davydov, *Random symmetrizations of convex bodies*, first public 8 November 2012, arXiv:1211.1785, https://arxiv.org/abs/1211.1785.
4. G. Bianchi, R. J. Gardner and P. Gronchi, *Convergence of symmetrization processes*, first public 8 August 2019, arXiv:1908.03259, https://arxiv.org/abs/1908.03259.
