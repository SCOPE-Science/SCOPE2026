# A sharp orientation–relaxation transient law for complex GADI iteration

## Finding
Consider the two-stage generalized alternating-direction implicit (GADI) iteration for complex symmetric linear systems introduced in the cited 2024 source. For a positive-definite real part and a rank-one nonnegative imaginary part, a two-dimensional family exhibits a sharp and quantified conflict between asymptotic convergence and finite-step Euclidean error amplification.

Let \(\alpha,\beta>0\) with \(\alpha\ne\beta\), \(t\ge0\), and \(v\in\mathbb R^2\) with \(\|v\|_2=1\). Define
\[
W=\begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix},\qquad
T=t vv^{\mathsf T},\qquad A=W+iT,\qquad q=|v_2|^2,\qquad d=\frac{\alpha-\beta}{\alpha+\beta}.
\]
For relaxation \(0\le\omega<2\), write \(\theta=\omega/2\) and denote its error propagator by \(G_\omega\). The following are exact conclusions in complex Euclidean norm.

**Exact orientation law.** The unrelaxed propagator \(H=G_0\) has rank one, with its only possibly nonzero eigenvalue and norm
\[
\lambda=d\frac{\alpha+it(1-2q)}{\alpha+it},\qquad
\|H\|_2^2=d^2\left(1+\frac{q(1-q)t^4}{\alpha^2(\alpha^2+t^2)}\right),
\]
\[
\rho(H)^2=d^2\frac{\alpha^2+(1-2q)^2t^2}{\alpha^2+t^2}.
\]
At every \(t>0\), the same and unique orientation \(q=1/2\) maximizes \(\|H\|_2\) and minimizes \(\rho(H)\). The inequalities are strict against every \(q\ne1/2\). The commuting orientations \(q=0,1\) instead have \(\|H\|_2=\rho(H)=|d|\).

**Sharp stiff limit.** At \(q=1/2\), for every positive integer \(k\),
\[
\|H^k\|_2=\frac{|d|^k\alpha^{k-1}(2\alpha^2+t^2)}{2(\alpha^2+t^2)^{k/2}}.
\]
In particular,
\[
\lim_{t\to\infty}\rho(H)=0,\quad
\lim_{t\to\infty}\frac{\|H\|_2}{t}=\frac{|d|}{2\alpha},\quad
\lim_{t\to\infty}\|H^2\|_2=\frac{d^2}{2},\quad
\lim_{t\to\infty}\|H^k\|_2=0\ (k\ge3).
\]
One-step error amplification can therefore diverge while the asymptotic spectral radius tends to zero. For \(q=1/2+\eta\alpha/t\) with fixed \(\eta\in\mathbb R\), the sharp angular-window law is
\[
\lim_{t\to\infty}\frac{t}{\alpha}\rho(H)=|d|\sqrt{1+4\eta^2}.
\]
For every fixed \(q\ne1/2\), by contrast, \(\rho(H)\to|d|\,|1-2q|>0\). Thus the fast spectral behavior requires tuning the overlap within order \(\alpha/t\).

**Relaxation changes the entire finite-horizon transient.** Set \(0\le\theta<1\). For every fixed integer \(k\ge1\), with \(0^0=1\),
\[
\lim_{t\to\infty}\frac{\|G_\omega^k\|_2}{t}
=\frac{|d|}{2\alpha}(1-\theta)k\theta^{k-1},\qquad
\lim_{t\to\infty}\rho(G_\omega)=\theta.
\]
The convergence also holds after taking the supremum over iteration counts:
\[
\boxed{\displaystyle
\lim_{t\to\infty}\frac{1}{t}\sup_{k\ge1}\|G_\omega^k\|_2
=\frac{|d|}{2\alpha}(1-\theta)\max_{k\ge1} k\theta^{k-1}.}
\]
If \(0<\theta<1\), the maximizing index of the leading coefficient is \(\lceil\theta/(1-\theta)\rceil\), with an additional tied maximizer at the next index when \(\theta/(1-\theta)\) is a positive integer. At \(\theta=0\) only the first power has nonzero linear-in-\(t\) growth. Every fixed \(\theta>0\) instead produces such growth at *every* positive fixed power.

As a concrete example, with \(\alpha=1\), \(\beta=3\), balanced \(v\), and \(\omega=3/2\), the normalized worst transient tends to \(27/256\); iteration counts \(3\) and \(4\) tie for the leading peak. With \(\omega=0\), the first Euclidean step is expansive precisely when
\[
\frac{t}{\alpha}>\sqrt{6+4\sqrt3}
\]
for this curvature ratio, even though every fixed such iteration is asymptotically convergent.

## Assumptions and scope
The original complex GADI iteration is used with exact subproblem solves, fixed \(\alpha>0\), \(0\le\omega<2\), and the source's equations
\[
(\alpha I+W)x^{(k+1/2)}=(\alpha I-iT)x^{(k)}+b,
\]
\[
(\alpha I+iT)x^{(k+1)}=[iT-(1-\omega)\alpha I]x^{(k)}
 +(2-\omega)\alpha x^{(k+1/2)}.
\]
The right-hand side \(b\in\mathbb C^2\) and initial iterate are arbitrary. The real matrix \(W\) is strictly positive definite, and \(T\) is positive semidefinite. These ensure that \(A=W+iT\) is nonsingular. The error is the numerical iterate minus the exact solution, measured using the Euclidean norm on \(\mathbb C^2\). All supremums are over initial nonzero errors and, where indicated, positive integer iteration counts.

## Proof
**1. Reconstruct the propagator.** Set \(C=\alpha I+iT\), \(B=\alpha I-iT\), and \(e=(0,1)^{\mathsf T}\). Eliminating the half step yields
\[
G_\omega=\theta I+(1-\theta)H,\qquad
H=C^{-1}DB,\qquad
D=(\alpha I-W)(\alpha I+W)^{-1}=d ee^{\mathsf T}.
\]
Consequently \(H=d(C^{-1}e)(e^{\mathsf T}B)\) is rank one. Because \(B\) and \(C\) are polynomials in the same symmetric matrix, they commute.

**2. Exact singular and eigen data.** The orthogonal projector \(P=vv^{\mathsf T}\) gives
\[
C^{-1}=\frac{I-P}{\alpha}+\frac{P}{\alpha+it},\qquad
BC^{-1}=(I-P)+\frac{\alpha-it}{\alpha+it}P.
\]
Thus the nonzero eigenvalue equals \(\lambda=d e^{\mathsf T}BC^{-1}e\), producing the stated complex fraction. Since a rank-one matrix has operator norm equal to the product of its generating vector norms,
\[
\|H\|_2^2=d^2\|C^{-1}e\|_2^2\|e^{\mathsf T}B\|_2^2
=d^2\left(\frac{1-q}{\alpha^2}+\frac{q}{\alpha^2+t^2}\right)(\alpha^2+qt^2).
\]
Multiplication gives the claimed formula. The squared eigenvalue modulus gives \(\rho(H)^2\). For \(t>0\) both depend strictly monotonically, in opposite directions, on \(q(1-q)\); its unique maximizer on \([0,1]\) is \(q=1/2\).

**3. The finite powers and angular boundary.** As a rank-one matrix \(H^2=\lambda H\), hence \(H^k=\lambda^{k-1}H\) for all integers \(k\ge1\). At balanced orientation, substitution yields the exact power-norm expression, and taking the indicated limits proves the stiff laws. Replacing \(q\) by \(1/2+\eta\alpha/t\) in the exact spectral formula establishes the angular-window limit. The parameter stays admissible for sufficiently large \(t\).

**4. Relaxation and uniform peak.** For all \(k\ge1\), the binomial identity and \(H^j=\lambda^{j-1}H\) give
\[
G_\omega^k=\theta^kI+P_k(\lambda)H,\qquad
P_k(\lambda)=\sum_{j=1}^k\binom kj\theta^{k-j}(1-\theta)^j\lambda^{j-1}.
\]
At fixed \(k\), as \(t\to\infty\), \(\lambda\to0\) and \(P_k(\lambda)\to k\theta^{k-1}(1-\theta)\). Combining this with \(\|H\|_2/t\to|d|/(2\alpha)\) proves the fixed-power limit. For uniformity in \(k\), note
\[
|P_k(\lambda)|\le k(1-\theta)[\theta+(1-\theta)|\lambda|]^{k-1}.
\]
For large enough \(t\), the bracket is bounded by a fixed \(r<1\). Hence the tails of \(k r^{k-1}\) vanish uniformly, and \(\sup_k\theta^k/t\le1/t\to0\). This justifies exchanging the stiff limit and supremum over all positive integers. Finally, the ratio of consecutive positive coefficients \(k\theta^{k-1}\) is \(\theta(k+1)/k\), giving the asserted exact peak indices and ties.

**5. Compatibility with weighted contraction.** The pre-existing HSS analysis applies in the transformed norm. Indeed, \(CHC^{-1}=D BC^{-1}\), and \(BC^{-1}\) is unitary, so \(\|CHC^{-1}\|_2=|d|<1\). Therefore \(\|CG_\omega C^{-1}\|_2\le\theta+(1-\theta)|d|<1\). This proves convergence for every fixed admissible parameter, and explains why no weighted-norm contraction result is contradicted by the Euclidean transient. For fixed \(t\), \(\|G_\omega^k\|_2\to0\) as \(k\to\infty\).

## Verification
The accompanying standalone `verify.py` reconstructs the two source stages and confirms the propagator identity, rank-one relation, complex eigenvalue, exact Euclidean norm, and finite-power formula using exact symbolic arithmetic. It also verifies the closed-form amplification threshold and the relaxation peak coefficient in a rational example. The actual checker ran successfully. Infinite stiff-limit and all-integer peak assertions are proved by the foregoing identities and uniform geometric-tail argument; finite tests are not used as substitutes for those proofs.

## Relationship to prior work
Zhang and Xun (2024, equation (7), Theorem 2) define the complex GADI iteration and prove asymptotic convergence under positive-definiteness assumptions. The case \(\omega=0\) recovers the classical HSS error map. Bertaccini, Golub, Serra-Capizzano, and Tablino-Possio (published online in 2004) give this HSS matrix formula, its Cayley similarity transform, contraction in the transformed norm, and a general account of nonnormal spectral mixing. Those identities and qualitative effects are **prior work**, not new claims here. The additional exact contribution is the opposite strict orientation extrema for the *Euclidean* one-step norm and spectral radius, its singular angular window, and the uniformly sharp relaxation-dependent finite-horizon amplification law including delayed peak indices. The compared source material does not state these formulas or their joint stiff-limit classification. Equivalent prior specialized calculations remain a bibliographic possibility.

## Limitations
The result is a planar, rank-one-imaginary-part, exact-arithmetic analysis; it is not an unconditional Euclidean-norm divergence theorem, nor a failure of convergence. It does not quantify floating-point rounding, inexact subproblem solves, higher-dimensional preconditioners, or implementation runtime. Large initial transients may be accompanied by a growing equivalence constant between Euclidean and transformed error norms; the latter remains contractive. The theorem does not assert independently verified bibliographic priority.

## References
1. J. Zhang and W. Xun, “A general alternating direction implicit iteration method for solving complex symmetric linear systems” (2024), arXiv:2404.12160, first posted 2024-04-18. https://arxiv.org/abs/2404.12160
2. D. Bertaccini, G. H. Golub, S. Serra-Capizzano, and C. Tablino-Possio, “Preconditioned HSS methods for the solution of non-Hermitian positive definite linear systems and applications to the discrete convection-diffusion equation,” *Numerische Mathematik* 99 (2005), 441–484, published online 2004-12-14, doi:10.1007/s00211-004-0574-1. https://doi.org/10.1007/s00211-004-0574-1
