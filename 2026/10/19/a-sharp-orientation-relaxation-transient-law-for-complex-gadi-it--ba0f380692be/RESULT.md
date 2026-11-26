# A sharp orientation–relaxation transient law for complex GADI iteration

## Finding

Let \(\alpha,\beta>0\) with \(\alpha\ne\beta\), let \(t\ge0\), and let \(v\in\mathbb R^2\) be a unit vector. Define
\[
W=\operatorname{diag}(\alpha,\beta),\qquad T=t vv^{\mathsf T},\qquad A=W+iT,\qquad
q=|v_2|^2,\qquad d=\frac{\alpha-\beta}{\alpha+\beta}.
\]
Use the complex generalized alternating-direction implicit (GADI) iteration below with shift \(\alpha\), relaxation \(0\le\omega<2\), and error propagator \(G_\omega\). Put \(\theta=\omega/2\) and \(H=G_0\). All norms are complex Euclidean operator norms.

**Exact orientation law.** The rank-one matrix \(H\) has nonzero eigenvalue \(\lambda\), and
\[
\lambda=d\frac{\alpha+it(1-2q)}{\alpha+it},\qquad
\|H\|_2^2=d^2\left(1+\frac{q(1-q)t^4}{\alpha^2(\alpha^2+t^2)}\right),\qquad
\rho(H)^2=d^2\frac{\alpha^2+(1-2q)^2t^2}{\alpha^2+t^2}.
\]
For each \(t>0\), the unique **overlap** \(q\) that maximizes the norm and minimizes the spectral radius is \(q=1/2\); both inequalities are strict against every other overlap. At the commuting overlaps \(q=0,1\), both quantities equal \(|d|\).

**Sharp unrelaxed stiff limit.** For \(q=1/2\) and every integer \(k\ge1\),
\[
\|H^k\|_2=\frac{|d|^k\alpha^{k-1}(2\alpha^2+t^2)}{2(\alpha^2+t^2)^{k/2}}.
\]
Consequently as \(t\to\infty\), \(\rho(H)\to0\), \(\|H\|_2/t\to|d|/(2\alpha)\), \(\|H^2\|_2\to d^2/2\), and \(\|H^k\|_2\to0\) for each \(k\ge3\). One-step amplification can diverge even as the spectral radius goes to zero. For \(q=1/2+\eta\alpha/t\) with fixed real \(\eta\),
\[
\lim_{t\to\infty}(t/\alpha)\rho(H)=|d|\sqrt{1+4\eta^2}.
\]
Thus the \(O(\alpha/t)\) spectral-radius scale requires overlap within \(O(\alpha/t)\) of balance. For every fixed \(q\ne1/2\), \(\rho(H)\to|d|\,|1-2q|>0\).

**Relaxed stiff limit at balanced overlap.** In the following assertions fix **\(q=1/2\)** and \(0\le\theta<1\) while taking \(t\to\infty\). For every fixed integer \(k\ge1\), with \(0^0=1\),
\[
\lim_{t\to\infty}\frac{\|G_\omega^k\|_2}{t}=\frac{|d|}{2\alpha}(1-\theta) k\theta^{k-1},\qquad
\lim_{t\to\infty}\rho(G_\omega)=\theta.
\]
The peak over all iteration counts also satisfies
\[
\lim_{t\to\infty}\frac{1}{t}\sup_{k\ge1}\|G_\omega^k\|_2
=\frac{|d|}{2\alpha}(1-\theta)\max_{k\ge1} k\theta^{k-1}.
\]
For \(0<\theta<1\), the leading coefficient peaks at \(\lceil\theta/(1-\theta)\rceil\); if \(\theta/(1-\theta)\) is a positive integer, the next index ties. This is a tie in the leading coefficient, not necessarily at finite \(t\). At \(\theta=0\) only the first power grows linearly with \(t\); at each fixed \(\theta>0\), every positive fixed power grows linearly. These formulas are not asserted for general fixed overlaps: for example, at \(q=0\), \(H=\operatorname{diag}(0,d)\) is independent of \(t\).

For \(\alpha=1,\beta=3,q=1/2\) and \(\omega=3/2\), the normalized worst transient tends to \(27/256\), with a leading tie at \(k=3,4\). At the same curvature ratio and overlap with \(\omega=0\), the first Euclidean step is expansive precisely when \(t/\alpha>\sqrt{6+4\sqrt3}\), even though the iteration converges for every fixed \(t\).

## Assumptions and scope

The original complex GADI iteration is used with exact subproblem solves, fixed positive shift \(\alpha\) equal to the first diagonal entry of \(W\), and the two stages
\[
(\alpha I+W)x^{(k+1/2)}=(\alpha I-iT)x^{(k)}+b,
\]
\[
(\alpha I+iT)x^{(k+1)}=[iT-(1-\omega)\alpha I]x^{(k)}+(2-\omega)\alpha x^{(k+1/2)}.
\]
Here \(W\) is real positive definite, \(T\) is real positive semidefinite, and \(b\) and the initial iterate may be arbitrary complex vectors. The solution is well defined since the Hermitian part of \(A\) is positive definite. The error is the numerical iterate minus this solution. An operator norm is the supremum of amplification over nonzero initial errors. The supremum over powers is over positive integers.

## Proof

**Propagator.** Set \(C=\alpha I+iT\), \(B=\alpha I-iT\), and \(e=(0,1)^{\mathsf T}\). The solution is a fixed point of both stages. Subtract it and eliminate the half step. Using \(iT-(1-\omega)\alpha I=\theta C-(1-\theta)B\) yields
\[
G_\omega=\theta I+(1-\theta)H,\qquad H=C^{-1}DB,\qquad
D=(\alpha I-W)(\alpha I+W)^{-1}=d ee^{\mathsf T}.
\]
Thus \(H=d(C^{-1}e)(e^{\mathsf T}B)\) has rank one: \(B,C\) are invertible and \(d\ne0\).

**Singular and eigenvalue data.** With \(P=vv^{\mathsf T}\),
\[
C^{-1}=\frac{I-P}{\alpha}+\frac{P}{\alpha+it},\qquad
BC^{-1}=(I-P)+\frac{\alpha-it}{\alpha+it}P.
\]
The trace of the rank-one matrix is \(d e^{\mathsf T}BC^{-1}e=\lambda\); the numerator of the claimed \(\lambda/d\) has real part \(\alpha>0\). The squared operator norm is
\[
d^2\|C^{-1}e\|_2^2\|e^{\mathsf T}B\|_2^2
=d^2\left(\frac{1-q}{\alpha^2}+\frac{q}{\alpha^2+t^2}\right)(\alpha^2+qt^2).
\]
Multiplication yields the norm formula and taking \(|\lambda|^2\) gives the spectral-radius formula. At \(t>0\) the squared norm strictly increases and the squared radius strictly decreases with \(q(1-q)\); that product has its unique maximum at \(q=1/2\).

**Stiff powers and angular window.** Rank one gives \(H^k=\lambda^{k-1}H\) for \(k\ge1\). At balance, \(|\lambda|=|d|\alpha/\sqrt{\alpha^2+t^2}\) and \(\|H\|_2=|d|(2\alpha^2+t^2)/(2\alpha\sqrt{\alpha^2+t^2})\). Their product gives the power formula and limits. In the exact spectral formula, substituting \(q=1/2+\eta\alpha/t\) gives the angular-window limit. More generally the formula shows that if \((t/\alpha)\rho(H)\) remains bounded at large \(t\), so does \((t/\alpha)|1-2q|\); the converse also holds.

**Relaxed powers and peak at balance.** Here \(q=1/2\), so \(\lambda\to0\). The eigenvalues of \(G_\omega\) are \(\theta\) and \(\theta+(1-\theta)\lambda\), implying the asserted spectral limit. The binomial expansion gives
\[
G_\omega^k=\theta^k I+p_k(\lambda)H,\qquad
p_k(z)=\sum_{j=1}^k\binom{k}{j}\theta^{k-j}(1-\theta)^j z^{j-1}.
\]
At fixed \(k\), \(p_k(\lambda)\to(1-\theta)k\theta^{k-1}\). The two-sided reverse-triangle estimate bounds the difference between \(\|G_\omega^k\|_2/t\) and \(|p_k(\lambda)|\|H\|_2/t\) by \(\theta^k/t\), proving the fixed-power formula. For a uniform tail bound, \(\binom{k}{j}\le k\binom{k-1}{j-1}\) yields
\[
|p_k(\lambda)|\le k(1-\theta)[\theta+(1-\theta)|\lambda|]^{k-1}.
\]
For all sufficiently large \(t\), the bracket is at most a fixed \(r<1\) and \(\|H\|_2/t\) is bounded. The terms \(kr^{k-1}\) tend uniformly to zero beyond a growing cutoff, and \(\sup_k\theta^k/t\to0\). Thus the fixed-power limit passes to the supremum over \(k\). At \(0<\theta<1\) the ratio of consecutive leading factors is \(\theta(k+1)/k\), giving the stated peak and tie. At \(\theta=0\), the convention \(0^0=1\) gives the first power only. At \(\theta=3/4\), \(\alpha=1\), \(d=-1/2\), the peak value is \((1/4)(1/4)3(3/4)^2=27/256\). At \(\theta=0\), \(|d|=1/2\), set \(y=(t/\alpha)^2\); \(\|H\|_2>1\) is equivalent to \((2+y)^2>16(1+y)\), or \(y>6+4\sqrt3\).

**Weighted contraction.** The matrix \(BC^{-1}\) is unitary by its projector representation, so \(CHC^{-1}=DBC^{-1}\) has norm \(|d|\). Thus \(\|CG_\omega C^{-1}\|_2\le\theta+(1-\theta)|d|<1\). At every fixed \(t\) the Euclidean powers tend to zero, notwithstanding the large finite-step amplification as \(t\) varies.

## Verification

The accompanying `verify.py` uses SymPy to reconstruct the two GADI stages and compare rank-one eigenvalue, norm and finite-power expressions at selected exact parameters. It also checks the balanced example's threshold and leading peak coefficient. The analytic identities and uniform tail estimate, not finite sampling, establish the universal claims. Run `python verify.py` with SymPy installed.

## Relationship to prior work

Zhang and Xun (2024, equation (7) and Theorem 2) define complex GADI, identify the affine relaxation of the HSS map, and give asymptotic convergence under positivity assumptions. HSS error maps, transformed-norm contraction and the qualitative role of nonnormality are prior work; see also Bertaccini et al. The factor \(k\theta^{k-1}\) is the usual derivative of the scalar power, as in nearly coalescent eigenvalues and Jordan powers. The contribution here is the exact Euclidean orientation law, the tuned spectral window and stiff power limits, and the uniform peak law with its exact coefficient for this balanced GADI family. This does not establish global priority for equivalent earlier specializations.

## Limitations

The result is planar, with rank-one imaginary part for \(t>0\), fixed positive curvature ratio, and exact subproblem solves. In the relaxed stiff limit the overlap stays balanced and \(\theta\) stays fixed below one. No claim is made for joint scaling \(\theta\to1\), other fixed overlaps in those peak formulas, finite precision, or higher-dimensional systems. The result concerns Euclidean amplification and does not contradict contraction in the transformed norm.

## References

1. J. Zhang and W. Xun, *A general alternating direction implicit iteration method for solving complex symmetric linear systems*, arXiv:2404.12160 (2024). https://arxiv.org/abs/2404.12160
2. D. Bertaccini, G. H. Golub, S. Serra-Capizzano, and C. Tablino-Possio, *Preconditioned HSS methods for the solution of non-Hermitian positive definite linear systems and applications to the discrete convection-diffusion equation*, Numerische Mathematik 99 (2005), 441–484. https://doi.org/10.1007/s00211-004-0574-1
