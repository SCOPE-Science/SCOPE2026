# Infinitely many sharp gradient cusps for biased lattice heat flow

## Finding

For positive jump rates \(a,b\), let \(T_t=\exp(tQ_{a,b})\) on bounded real sequences indexed by \(\mathbb Z\), where
\[
(Q_{a,b}f)(j)=a(f(j+1)-f(j))+b(f(j-1)-f(j)).
\]
Let \(\operatorname{Lip}(g)=\sup_{j\in\mathbb Z}|g(j+1)-g(j)|\) and \(G_{a,b}(t)=\sup_{\|f\|_\infty\le1}\operatorname{Lip}(T_tf)\), for \(t>0\). Set \(L=a+b\), \(\delta=a-b\), and
\[
p_t(k)=e^{-Lt}(a/b)^{k/2}I_{|k|}(2t\sqrt{ab})\quad(k\in\mathbb Z).
\]
Then the exact sharp gradient norm is
\[
\boxed{G_{a,b}(t)=2\max_{k\in\mathbb Z}p_t(k).}
\]
For \(a=b\), the unique mode is zero and the norm is analytic for positive time:
\[
G_{a,a}(t)=2e^{-2at}I_0(2at).
\]
For \(a>b\), there exist unique, strictly increasing transition times \(0<t_0<t_1<\cdots\), with \(t_k\to\infty\), characterized by
\[
\sqrt{a/b}\,\frac{I_{k+1}(2t_k\sqrt{ab})}{I_k(2t_k\sqrt{ab})}=1\qquad(k\ge0).
\]
Put \(t_{-1}=0\). For every \(k\ge0\), the sole mode of \(p_t\) is \(k\) for \(t_{k-1}<t<t_k\); at \(t=t_k\) the only modes are \(k,k+1\). Consequently the norm has an upward jump of its time derivative at every transition,
\[
\boxed{G'_{a,b,+}(t_k)-G'_{a,b,-}(t_k)=4a\,p_{t_k}(k)\left.\frac{d}{dz}\frac{I_{k+1}(z)}{I_k(z)}\right|_{z=2t_k\sqrt{ab}}>0.}
\]
These infinitely many corners obey the sharp location asymptotic
\[
\boxed{t_k=\frac{k+1/2}{a-b}+\frac1{2(a+b)}+O_{a,b}(k^{-1})\quad(k\to\infty).}
\]
For \(a<b\), the same statements hold after reflecting integer indices and exchanging \(a,b\); the transition locations depend on \(|a-b|\). In all cases every sharp norm is attained by a bounded sign sequence. Thus nonzero drift creates an infinite sequence of nonsmoothness times in the **sharp norm**, although every individual heat-kernel coefficient is analytic in time.

## Assumptions and scope

The rates \(a,b\) are strictly positive and fixed, the underlying space is the entire two-sided integer lattice, and the generator is the bounded nearest-neighbor operator displayed above; no boundary condition or finite-period truncation is used. All norms use counting measure and the unweighted nearest-neighbor edge difference; no factor of mesh length is included. Real-valued inputs suffice. The formula for \(G\) is for all positive times, and the transition asymptotic concerns \(k\to\infty\) with \(a,b\) fixed. The degeneracy \(a=b\) is treated separately. The theorem makes no claim of differentiability at the transition times or of a uniform asymptotic as the drift tends to zero.

## Proof

**Kernel and sharp norm.** Independent Poisson random variables of respective means \(at\) and \(bt\) show that the convolution kernel of \(T_t\) is the strictly positive mass function \(p_t\). The modified-Bessel series gives the displayed formula. Translation invariance yields
\[
(T_tf)(j+1)-(T_tf)(j)=\sum_{k\in\mathbb Z}[p_t(k-1)-p_t(k)]f(j+k).
\]
Therefore the sharp norm is exactly \(\sum_k|p_t(k-1)-p_t(k)|\); the sign of each coefficient is a single bounded extremizing input. The sum converges absolutely. For each \(z>0\), the strict Turán inequality \(I_j(z)^2>I_{j-1}(z)I_{j+1}(z)\) for integers \(j\ge1\) follows from the positive Neumann product integral
\[
I_j(z)^2-I_{j-1}(z)I_{j+1}(z)=\frac4\pi\int_0^{\pi/2} I_{2j}(2z\cos u)\sin^2u\,du>0.
\]
At the index zero, \(I_0(z)>I_1(z)\) follows from the positive integral of \(e^{z\cos u}(1-\cos u)\). These identities show strict log-concavity of the full two-sided sequence \(p_t(k)\). It rises to one mode or two adjacent tied modes and then falls, and its variation telescopes to twice the maximal mass. In particular, this proves the first boxed identity without approximation.

**Ordered changes of mode.** Suppose \(a>b\). The identity \(p_t(-k)=(b/a)^k p_t(k)\) for positive \(k\), together with strict log-concavity, excludes all negative modes. For nonnegative \(k\), define
\[
r_k(t)=\frac{p_t(k+1)}{p_t(k)}=\sqrt{a/b}\,R_k(2t\sqrt{ab}),\qquad R_k(z)=\frac{I_{k+1}(z)}{I_k(z)}.
\]
The recurrence and derivative identities for modified Bessel functions give
\[
R_k'(z)=1-\frac{2k+1}{z}R_k(z)-R_k(z)^2.
\]
Let \(c=k+1/2\) and \(q(z)=z/[c+\sqrt{c^2+z^2}]\). This is the increasing positive root of the quadratic equation on the right; \(R_k(z)\sim z/[2(k+1)]<q(z)\sim z/(2k+1)\) at zero. A hypothetical first contact would have \(R_k'=0<q'\) and is impossible. Thus \(R_k(z)<q(z)\), giving \(R'_k(z)>0\) for every positive \(z\). Moreover \(R_k(z)\to1\) as \(z\to\infty\), by the integral Laplace asymptotic for \(I_k\). As \(t\downarrow0\), \(r_k(t)\to0\), whereas \(r_k(t)\to\sqrt{a/b}>1\) at infinity. Each \(r_k\) therefore crosses one exactly once. Strict Turán inequalities imply \(r_{k+1}(t)<r_k(t)\), so the crossing times increase strictly; at fixed positive time, \(r_k(t)\to0\) as \(k\to\infty\), hence the crossings escape to infinity. The mode classification follows by comparing adjacent ratios. For symmetric rates \(r_k(t)<1\) for all \(k\ge0\) and the maximal mass is \(p_t(0)\).

**Exact corner size.** Between transitions \(G_{a,b}(t)=2p_t(k)\) on the cell with mode \(k\), an analytic function. At a crossing, \(p_{t_k}(k)=p_{t_k}(k+1)\), but \(r_k'(t_k)=2aR_k'(2t_k\sqrt{ab})>0\). Thus the right derivative minus the left derivative is \(2p_{t_k}(k)r_k'(t_k)\), which is the claimed strictly positive jump. There are no other corners. Reflection gives the case \(a<b\).

**Sharp transition asymptotic.** Write \(y=k-\delta t\), where \(\delta>0\), and consider \(|y|\le M\) for fixed \(M\). Fourier inversion yields
\[
p_t(k+1)-p_t(k)=\frac1{2\pi}\int_{-\pi}^{\pi}(e^{-i\theta}-1)
\exp\{Lt(\cos\theta-1)-iy\theta+i\delta t(\sin\theta-\theta)\}\,d\theta.
\]
Splitting the integral at \(|\theta|=t^{-2/5}\), the complementary region is exponentially small, since \(\cos\theta-1\le-c\theta^2\) near zero and is strictly negative off zero. Within that region, use \(\theta=u/\sqrt t\) and the Taylor expansions of the sine, cosine, and difference factor, retaining terms through relative order \(t^{-1}\) after integrating; odd Gaussian moments vanish. The three contributions at order \(t^{-3/2}\) are respectively \(-y/(Lt)\), \(-1/(2Lt)\), and \(-\delta/(2L^2t)\), relative to the Gaussian mass \((2\pi Lt)^{-1/2}\). Bounded Gaussian moments control all remaining even terms uniformly for \(|y|\le M\), giving
\[
p_t(k+1)-p_t(k)=
-\frac1{\sqrt{2\pi Lt}}\frac{y+1/2+\delta/(2L)+O_{a,b,M}(t^{-1})}{Lt}.
\]
For any fixed sufficiently large \(C>0\), evaluate the last formula at \(t=(k-C)/\delta\) and \(t=(k+C)/\delta\). Their signs differ for all sufficiently large \(k\). Uniqueness of the crossing proves \(t_k=k/\delta+O_{a,b}(1)\), and inserting \(y=k-\delta t_k\) into the uniform expansion gives \(k-\delta t_k=-1/2-\delta/(2L)+O_{a,b}(k^{-1})\). Rearranging yields the stated asymptotic. This argument controls the infinite \(k\) limit analytically and is not based on numerical extrapolation.

## Verification

The accompanying standalone checker independently evaluates Skellam masses and adjacent differences, verifies the total-variation equality at finite times, solves sample Bessel-ratio crossing equations, checks strict ordering and adjacent ties, and compares transition locations with the asymptotic expression for increasing indices. It reports 240 passed finite assertions with SciPy. For rates \(a=0.8,b=0.2\), the first crossing is near \(1.449149900938\) and the crossing at index \(100\) near \(168.000955773336\); the two-term asymptotic predicts \(168\). These tests corroborate computations but do not certify the general proof.

## Relationship to prior work

The Skellam representation and Bessel-ratio framework are classical. Balachandran, Viles and Kolaczyk (arXiv:1311.1450v1, 2013) derive bounds on modified-Bessel ratios, Skellam masses and related concentration functionals. Koopman, Lit and Lucas (2014) analyze time-varying Skellam models for integer-valued data. The present theorem concerns a different operator invariant: the exact bounded-input-to-spatial-gradient norm of an *asymmetric* heat semigroup and its full sequence of nonsmooth times. Its unique ratio-threshold classification, strict cusp sizes and second-order transition locations do not follow as stated from the inspected source conclusions; common Bessel and Skellam identities are used explicitly, not claimed as new.

## Limitations

The findings concern homogeneous two-sided nearest-neighbor generators with both rates positive; reflecting boundaries, nonconstant rates, higher dimensions and discontinuous limits as a rate vanishes are not covered. The O-term in the transition expansion holds for fixed rates and need not be uniform near zero drift. A literature search cannot prove historical uniqueness: earlier results on modes of Skellam laws, discrete birth–death heat flows, or modified-Bessel ratios might imply some or all of the phase classification. Independent scientific and bibliographic audit has not been performed.

## References

- P. Balachandran, W. Viles and E. D. Kolaczyk, *Exponential-type Inequalities Involving Ratios of the Modified Bessel Function of the First Kind and their Applications*, arXiv:1311.1450v1 (first posted 2013-11-06), https://arxiv.org/abs/1311.1450 .
- S. J. Koopman, R. Lit and A. Lucas, *The Dynamic Skellam Model with Applications*, public preprint dated 2014-03-06, https://www2.gwu.edu/~forcpgm/OxMetrics2014_files/KoopmanLitLucas-OxM14-NaisSkellamPaper.pdf .
