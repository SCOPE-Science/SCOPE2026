# Independent beta contraction factors for Gaussian rank-one randomized CGLS on identity least squares

## Finding
Consider the randomized conjugate-gradient least-squares (RCGLS) iteration of Zeng–Cai–Han–Xie with independent rank-one Gaussian sketches, specialized to a real identity least-squares system of dimension \(d\). Although consecutive search directions are conjugate only to their immediate predecessors, the **entire sequence of normalized squared errors** has an exact product-beta law. In dimensions \(d\geq3\), the first squared-error ratio has law \(\operatorname{Beta}((d-1)/2,1/2)\), while all subsequent ratios are **mutually independent** with common law \(\operatorname{Beta}((d-2)/2,1/2)\). In dimension \(d=2\), the method terminates in exactly two steps almost surely from any nonoptimal initial point.

For \(d\geq3\), if \(E_k=\|x^k-b\|_2^2\) and \(E_0>0\), then for every integer \(k\geq1\),
\[
\frac{E_k}{E_0}\ \stackrel{\mathrm d}=\ B_0\prod_{j=1}^{k-1}B_j,
\qquad B_0\sim\operatorname{Beta}\!\left(\frac{d-1}{2},\frac12\right),\quad
B_j\stackrel{\mathrm{iid}}\sim\operatorname{Beta}\!\left(\frac{d-2}{2},\frac12\right),
\]
with every factor on the right independent. Consequently,
\[
\mathbb E E_k=E_0\frac{d-1}{d}\left(\frac{d-2}{d-1}\right)^{k-1},\qquad
\lim_{k\to\infty}\frac1k\log\frac{E_k}{E_0}
=\psi\!\left(\frac{d-2}{2}\right)-\psi\!\left(\frac{d-1}{2}\right)<0
\quad\text{almost surely}.
\]
Here \(\psi\) is the digamma function. In contrast, rank-one Gaussian randomized gradient descent with exact line search and no conjugacy correction has independent \(\operatorname{Beta}((d-1)/2,1/2)\) factors at **every** step, and expected error \(E_0((d-1)/d)^k\).

## Assumptions and scope
Let \(d\geq1\) be an integer, take \(A=I_d\), \(x^0,b\in\mathbb R^d\), \(x^0\neq b\), and use exact arithmetic. Independently draw \(s_k\sim N(0,I_d)\) for each integer \(k\geq0\). At step zero set \(g^0=(s_0^{\mathsf T}r^0)s_0\) and \(p^0=g^0\), where \(r^k=b-x^k\). At each later step \(k\geq1\), set
\[
g^k=(s_k^{\mathsf T}r^k)s_k,\qquad
p^k=g^k-\frac{\langle g^k,p^{k-1}\rangle}{\|p^{k-1}\|_2^2}p^{k-1}.
\]
The update at each step is the original exact-line-search RCGLS rule
\[
\mu_k=\frac{\langle r^k,p^k\rangle}{\|p^k\|_2^2},\qquad
x^{k+1}=x^k+\mu_kp^k,\qquad
r^{k+1}=r^k-\mu_kp^k.
\]
Denominators are nonzero almost surely up to exact termination. The source's alternative stepsize expression agrees with this expression because \(r^k\) is orthogonal to \(p^{k-1}\). This result applies to real, rank-one, independently Gaussian sketch columns, and the identity Hessian only; it neither asserts analogous independence for nonidentity Hessians nor describes the cost of any sparse implementation.

## Proof
**Algebraic identification.** Let \(u_0=s_0\); for \(k\geq1\), let \(u_k=P_{k-1}s_k\), where \(P_{k-1}=I_d-p^{k-1}(p^{k-1})^{\mathsf T}/\|p^{k-1}\|_2^2\) projects onto the preceding search direction's orthogonal complement. Exact line search yields \(r^k\perp p^{k-1}\) for all \(k\geq1\), so \(s_k^{\mathsf T}r^k=u_k^{\mathsf T}r^k\). Therefore the RCGLS correction takes the exact form
\[
p^k=(u_k^{\mathsf T}r^k)u_k,
\quad
\mu_k=\frac{1}{\|u_k\|_2^2},
\quad
r^{k+1}=r^k-\frac{u_k^{\mathsf T}r^k}{\|u_k\|_2^2}u_k
\]
for all nonterminal steps. The first formula holds also at \(k=0\) with \(u_0=s_0\).

**Spherical law and conditional independence.** At the first step, \(u_0\) is isotropic in a \(d\)-dimensional space. At every subsequent step, conditional on the complete past, \(u_k\) is a standard isotropic Gaussian vector in the \((d-1)\)-dimensional hyperplane \((p^{k-1})^\perp\), and \(r^k\) is a fixed nonzero vector in the same hyperplane. The square of the cosine between a fixed vector and an isotropic Gaussian direction in dimension \(h\) has distribution \(\operatorname{Beta}(1/2,(h-1)/2)\), by splitting the \(\chi^2_1\) component from the independent \(\chi^2_{h-1}\) orthogonal squared length. Orthogonal projection subtracts this squared cosine from one, hence
\[
\frac{\|r^{k+1}\|_2^2}{\|r^k\|_2^2}
\sim\operatorname{Beta}\!\left(\frac{h-1}{2},\frac12\right),
\]
with \(h=d\) at step zero and \(h=d-1\) thereafter. In particular, the later conditional law **does not depend on the past**. Each ratio is thus independent of all preceding sigma-fields and of the other ratios, proving the asserted independent product representation.

**Dimension boundary and rates.** When \(d=1\), the first line spans the whole space and the initial residual vanishes. When \(d=2\), after the first nonzero step the error lies in the one-dimensional orthogonal complement of \(p^0\); the next Gaussian direction projected there spans it almost surely, giving \(r^2=0\). When \(d\geq3\), both beta parameters are positive, so every finite-step ratio lies strictly between zero and one almost surely; finite termination therefore has probability zero. The means of the beta factors are \((d-1)/d\) and \((d-2)/(d-1)\), respectively, giving the exact expected error. Moreover, \(\mathbb E|\log B_1|<\infty\), and the strong law of large numbers gives the logarithmic limit with the standard beta identity \(\mathbb E\log B_1=\psi((d-2)/2)-\psi((d-1)/2)\). Strict negativity follows from strict monotonicity of the digamma function. Repeating the first-step spherical argument independently at every step establishes the comparison with uncorrected Gaussian line-search descent.

## Verification
Run `python verify.py` (Python standard library only). It checks 1,386 exact-rational projected-direction identities, including the two-dimensional two-step termination, and compares empirical first-/later-step means, second moments, and consecutive-factor moments against the independent beta laws across 216,000 simulated Gaussian steps in dimensions three, five, and nine. It prints `VERIFY_OK` on success. These finite computations test the implementation and explicit identities but do not prove the probability laws or almost-sure limits; those follow from the arguments above.

## Relationship to prior work
Zeng, Cai, Han, and Xie (2026), arXiv:2605.25034v1, introduced RCGLS, its predecessor-direction correction, and a general expected-error upper bound (Algorithm 1 and Theorem 2.4). For \(A=I_d\), their rank-one Gaussian-sketch bound using the uniform \(\gamma_k=1\) yields at most \(1-1/d\), not the exact later-step ratio \((d-2)/(d-1)\); their work does not give the joint independent beta-factor distribution or almost-sure rate of this specialization. Stich, Müller, and Gärtner (2012), arXiv:1111.0194, analyzed independent spherical random-pursuit directions and exact line searches; those directions are not corrected to be orthogonal to the **previous** direction. Gower and Richtárik (2015), arXiv:1506.03296, developed sketch-and-project methods using independent sketches with no matching one-step conjugacy correction. Standard spherical beta projections are classical and are not claimed as novel in isolation. The distinctive claim concerns the complete exact error law of this *specific* RCGLS specialization and its sharp acceleration over uncorrected directions.

## Limitations
The theorem does not imply conjugacy to all earlier directions, finite termination in dimensions three or larger, increased practical speed, numerical stability under rounding, or extension to nonidentity least-squares matrices, structured sketch distributions, or inexact line searches. The expected-error comparison counts iterations, not floating-point operations. Independent external audit and complete global literature verification have not been performed; an equivalent earlier analysis of one-step-memory spherical projections remains a residual originality risk.

## References
1. Y. Zeng, J.-F. Cai, D. Han, J. Xie, *Randomized conjugate gradient least squares*, arXiv:2605.25034v1 (first posted 24 May 2026), §§2.2–2.3, Algorithm 1, Theorem 2.4. https://arxiv.org/abs/2605.25034
2. S. U. Stich, C. L. Müller, B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194v2 (2012), §§1–2, 4–6. https://arxiv.org/abs/1111.0194
3. R. M. Gower, P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015), especially the independent-sketch framework. https://arxiv.org/abs/1506.03296
