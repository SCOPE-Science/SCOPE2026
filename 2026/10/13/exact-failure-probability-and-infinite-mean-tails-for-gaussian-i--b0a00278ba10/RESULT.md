# Exact failure probability and infinite-mean tails for Gaussian indefinite Nyström Schur corrections

## Finding

A positive-definite exact Schur complement can acquire an indefinite randomized approximation through the signed Nyström correction of its inverse-diagonal residual. For the concrete two-dimensional double-saddle-point family defined below, a single standard Gaussian sketch has the exact strictly positive probability
\[
\Pr\{Q_{r,\gamma}\not\succ0\}=\frac2\pi\left[\arctan\sqrt{\frac{1-r}{1+r}}-\arctan\sqrt{\frac{c(\gamma-c)}{a(\gamma+a)}}\right],
\qquad a=\frac r{1-r},\quad c=\frac r{1+r}.
\]
Equivalently, the second arctangent's square-root argument is \(c(\gamma-c)/(a(\gamma+a))\). This probability never vanishes for \(0<r<1\) and \(\gamma>1\); its sharp supremum over these parameters is \(0.142154976126\ldots\), approached as \(\gamma\downarrow1\). Also,
\[
\lim_{z\to\infty}z\,\Pr\{\|Q_{r,\gamma}\|_2>z\}
=\frac{2r}{\pi\sqrt{1-r^2}},
\qquad \mathbb E\|Q_{r,\gamma}\|_2=+\infty.
\]
For **every fixed positive ridge** \(\varepsilon>0\) added to the signed scalar core, the corresponding regularized approximate Schur complement still fails positive definiteness with positive probability and has infinite expected spectral norm. These results concern the signed correction in exact arithmetic, not the stabilized indefinite-Nyström variants in the literature.

## Assumptions and scope

Fix \(0<r<1\) and \(\gamma>1\). Use real two-dimensional blocks
\[
A=I_2,\quad B=\sqrt{\gamma-1}\,I_2,\quad C=I_2,
\quad E=\begin{pmatrix}1&r\\r&1\end{pmatrix},\quad E_D=\operatorname{diag}(E)=I_2.
\]
Both \(A\) and \(E\) are symmetric positive definite and \(B,C\) have full row rank. The exact Schur complement \(S=BA^{-1}B^T+C^TE^{-1}C=(\gamma-1)I_2+E^{-1}\) is positive definite. Approximate the \(BA^{-1}B^T\) term **exactly**, the diagonal part of \(C^TE^{-1}C\) exactly, and its remainder by one signed rank-one Nyström correction. Define
\[
\Delta=C^T(E^{-1}-E_D^{-1})C=E^{-1}-I_2,\quad
Q_{r,\gamma}=\gamma I_2+
\Delta\omega(\omega^T\Delta\omega)^{\dagger}(\Delta\omega)^T,
\quad\omega\sim N(0,I_2).
\]
The scalar pseudoinverse agrees almost surely with the ordinary inverse: the null core event has probability zero. For fixed \(\varepsilon>0\), define the **ridge-core version**
\[
Q_{r,\gamma,\varepsilon}=\gamma I_2+
\frac{\Delta\omega(\Delta\omega)^T}{\omega^T\Delta\omega+\varepsilon}.
\]
All probabilities refer solely to the independent standard Gaussian sketch. No rounding, approximate linear solves, or adaptive choice of sketch is assumed. The dimension is \(n=m=p=2\), meeting the full-row-rank block assumptions in the motivating setting; computing the first Schur term exactly isolates the second term's mechanism.

## Proof

Let \(v_+=(1,-1)^T/\sqrt2\), \(v_-=(1,1)^T/\sqrt2\). In this orthogonal eigenbasis,
\[
\Delta=\operatorname{diag}(a,-c),\qquad
a=\frac r{1-r}>0,\quad c=\frac r{1+r}\in(0,1).
\]
Write \(\omega=u v_+ +v v_-\) with independent standard normal \(u,v\), and put \(d=a u^2-c v^2\), \(h=a^2u^2+c^2v^2\). Except on \(d=0\), the rank-one correction has eigenvalues \(0\) and \(h/d\), so \(Q_{r,\gamma}\) has eigenvalues
\[
\gamma,\qquad \gamma+\frac{h}{d}.
\]
Here \(h>0\) almost surely. Set \(t=|u/v|\). Since \(u/v\) is a standard Cauchy variable, \(t\) has density \(2/[\pi(1+t^2)]\) for \(t>0\). When \(d<0\), the second eigenvalue is negative exactly when \(\gamma d+h>0\), since division by \(d\) reverses the inequality. When \(d>0\), the second eigenvalue is positive. Consequently,
\[
\gamma+\frac{h}{d}<0
\iff
\frac{c(\gamma-c)}{a(\gamma+a)}<t^2<\frac ca.
\]
Indeed \(\gamma d+h=a(\gamma+a)u^2-c(\gamma-c)v^2\), with \(\gamma>1>c\). The Cauchy integral on this interval gives
\[
\Pr(Q_{r,\gamma}\not\succ0)=
\frac2\pi\left(\arctan t_0-\arctan t_1\right),\quad
t_0=\sqrt{c/a},\quad t_1=\sqrt{\frac{c(\gamma-c)}{a(\gamma+a)}}.
\]
The threshold is strict because \(t_1<t_0\) (as \(\gamma-c<\gamma+a\)), and equality events have probability zero.

For fixed \(r\), \(t_1^2\) is strictly increasing in \(\gamma\), hence the probability decreases strictly in \(\gamma\). At the boundary \(\gamma\downarrow1\), set \(x=\sqrt{(1-r)/(1+r)}\in(0,1)\): then \(t_0=x\) and \(t_1=x^2\). The sharp supremum reduces to maximizing \(2[\arctan x-\arctan(x^2)]/\pi\). Its derivative has the sign of \(x^4-2x^3-2x+1\); this polynomial decreases strictly on \((0,1)\), is positive at zero and negative at one, and has a unique root \(x_*=0.435420544682\ldots\). Thus the supremum is \(0.142154976126\ldots\), at limiting \(r_*=(1-x_*^2)/(1+x_*^2)=0.681250038633\ldots\). Because \(\gamma>1\), this is a supremum, not an attained maximum.

For tails define \(R(t)=(a^2t^2+c^2)/(a t^2-c)\). Its simple pole at \(t_0=\sqrt{c/a}\) has residue \((a+c)t_0/2\). The density of \(t\) is continuous and positive at \(t_0\). Its two sides therefore yield
\[
\lim_{z\to\infty}z\Pr(|R(t)|>z)=
2\frac{2}{\pi(1+t_0^2)}\frac{(a+c)t_0}{2}
=\frac{2\sqrt{ac}}\pi
=\frac{2r}{\pi\sqrt{1-r^2}}.
\]
Since \(\|Q_{r,\gamma}\|_2=\max\{\gamma,|\gamma+R(t)|\}\), fixed \(\gamma\) does not change the limit. The strict positive limit implies \(\int_0^\infty\Pr(\|Q\|_2>z)\,dz=\infty\).

For arbitrary fixed \(\varepsilon>0\), the ridge denominator is \(d_\varepsilon=a u^2-c v^2+\varepsilon\). At \((u,v)=(0,\sqrt{\varepsilon/c})\), it vanishes, its gradient is nonzero and \(h=c\varepsilon>0\). The Gaussian density is strictly positive there. In a sufficiently small neighborhood use \(d_\varepsilon\) as one smooth coordinate transverse to its zero curve. In that neighborhood \(h\) and the Jacobian/density have positive lower bounds; on the negative side \(\gamma+h/d_\varepsilon<0\) close enough to the curve. This has positive probability. Integrating the norm lower bound proportional to \(1/|d_\varepsilon|\) across both sides diverges logarithmically. This proves both assertions for every fixed ridge \(\varepsilon>0\), without claiming the same *exact failure-probability formula* for ridge corrections.

As an exact witness, take \(r=1/2\), \(\gamma=2\), eigen-coordinates \((u,v)=(1/2,1)\). In the \((v_+,v_-)\) basis,
\[
Q_{1/2,2}=\begin{pmatrix}-1&2\\2&2/3\end{pmatrix},
\quad \operatorname{spec}(Q_{1/2,2})=\{-7/3,2\}.
\]
The exact Schur complement is nevertheless positive definite, with eigenvalues \(3\) and \(5/3\). The open event around this witness gives positive probability, independently of the Gaussian measure-zero exact point.

## Verification

Run `python3 verify.py` using Python's standard library, without external dependencies. The program performs exact-fraction determinant/eigenvalue checks on the rational witness and a positive-ridge witness, multiple exact rank-one eigen-identities, deterministic-seed Gaussian trials for the four stated probability regimes, numerical asymptotic pole calculations at ten parameter/tail pairs, and a bisection check of the supremum. Expected last line:

`VERIFY_OK exact_fraction_identity=true gaussian_trials=480000 tail_formula_cases=10 global_supremum_verified=true`

The simulations are finite corroborations; the proof above is what establishes the universal probability, expectation, and ridge statements.

## Relationship to prior work

Liang and Huang (2026), Section 3 and Algorithm 1, introduce the hybrid diagonal-plus-signed-Nyström Schur construction and a positive ridge in the core. Their equation (3.3) reduces exactly to the signed correction used above; their conditional high-probability approximation-error analysis does not state the exact two-dimensional Gaussian positivity-loss law, its global probability supremum, or its infinite unconditional mean-norm conclusion. Their spectral analysis explicitly assumes an SPD Schur approximant.

Nakatsukasa and Park (2023), Section 1.1, already prove by a two-dimensional example that plain indefinite Nyström approximations may be unboundedly inaccurate. The present finding **does not claim that phenomenon as new**. Instead it computes the Gaussian probability and norm tail in an SPD-Schur preconditioning family and proves that even fixed positive ridge-core regularization does not ensure positivity or an integrable norm.

Chen, Nakatsukasa, Narendran and Park (2026) study an alternative two-sided sketched least-squares construction for indefinite Nyström approximation. Its accessible abstract motivates the broader problem, but a complete full-text comparison could not be made; it remains a literature risk. The construction here is the original signed core inverse, not their alternative.

## Limitations

Only a specific two-dimensional, rank-one, real Gaussian, exactly evaluated block family is classified. The failure probability is not a general failure rate for larger systems, sparse sketches, empirical incomplete Cholesky solves, multiple landmarks or an alternative stable indefinite approximation. The ridge result is qualitative rather than a closed probability expression. The exact threshold does not guarantee that practical solvers using other safeguards fail. An unavailable plausible newer source remains an explicit originality risk, so independent literature assessment has not occurred.

## References

1. S. Liang and N. Huang, *Randomized inexact block triangular preconditioners for double saddle-point systems in PDE-constrained optimization*, arXiv:2609.01031v1 (first public September 1, 2026), especially Section 2 (SPD hypotheses), Section 3, Algorithm 1 and equation (3.3). https://arxiv.org/html/2609.01031v1
2. Y. Nakatsukasa and T. Park, *Randomized low-rank approximation for symmetric indefinite matrices*, SIAM J. Matrix Anal. Appl. 44 (2023), 1370–1392; arXiv:2212.01127, Section 1.1. https://arxiv.org/pdf/2212.01127
3. Y. Chen, Y. Nakatsukasa, A. Narendran and T. Park, *Nyström method for symmetric indefinite matrices*, arXiv:2608.20531 (2026); accessible abstract only. https://arxiv.org/abs/2608.20531
