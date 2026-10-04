# Sharp condition-number frontier for objective descent in core LARS
## Finding

For the SPD quadratic
\[
f(x)=\frac12x^\top Hx,
\qquad
H=H^\top\succ0,
\qquad
\sigma(H)\subseteq[\mu,L],
\]
write
\[
\kappa=\frac{L}{\mu}.
\]
The zero-momentum, zero-weight-decay core LARS update is
\[
x^+
=
x-\rho\frac{\|x\|_2}{\|Hx\|_2}Hx.
\]

Define
\[
\rho_\star(\kappa)
=
\frac{3\sqrt{3}\,\kappa(\kappa+1)}
{(\kappa^2+\kappa+1)^{3/2}}.
\]
Then
\[
f(x^+)\le f(x)
\]
for every nonzero \(x\) and every admissible \(H\) if and only if
\[
0\le\rho\le\rho_\star(\kappa).
\]
Strict decrease for every nonzero state holds exactly for
\[
0<\rho<\rho_\star(\kappa).
\]

The frontier is sharp in two dimensions. With
\[
H=\operatorname{diag}(\mu,L)
\]
and, after scaling \(L=1\), squared mass
\[
p_\star
=
\frac{2\kappa+1}
{(\kappa+1)(\kappa^2+\kappa+1)}
\]
on the \(L\)-eigenvector, equality holds at \(\rho=\rho_\star(\kappa)\); every larger \(\rho\) makes the one-step objective increase.

The limiting laws are
\[
\rho_\star(1)=2,
\qquad
\rho_\star(\kappa)\sim\frac{3\sqrt{3}}{\kappa}.
\]
A crude state-independent argument that forces the induced gradient-descent step below \(2/L\) gives only
\[
\rho\le\frac{2}{\kappa}.
\]
Thus the exact LARS trust frontier is asymptotically larger by
\[
\frac{3\sqrt{3}}{2}.
\]

## Assumptions and scope

The theorem isolates the proportional LARS rule used in the direct convergence analysis of proportional updates and obtained from the original LARS rule by setting momentum and weight decay to zero.

It is a deterministic one-step objective-monotonicity theorem. Momentum, stochastic gradients, weight decay, warmup, and learning-rate schedules are outside the claim.

The minimizer is the origin, and the update is evaluated only at nonzero \(x\).

## Proof

Set
\[
s=\rho\frac{\|x\|_2}{\|Hx\|_2}.
\]
Since \(x^+=x-sHx\),
\[
f(x^+)-f(x)
=
-s\,x^\top H^2x
+
\frac{s^2}{2}x^\top H^3x.
\]
Let
\[
C=x^\top x,
\qquad
A=x^\top H^2x,
\qquad
B=x^\top H^3x.
\]
Then
\[
f(x^+)-f(x)
=
-\rho\sqrt{AC}
+
\frac{\rho^2BC}{2A}.
\]
Therefore a nonzero state decreases exactly when
\[
\rho<\frac{2A^{3/2}}{B\sqrt C}.
\]

Normalize \(C=1\) and scale \(L=1\). In an eigenbasis, let \(X\) equal an eigenvalue with probability given by the squared coordinate mass of \(x\). Then
\[
X\in[a,1],
\qquad
a=\frac1\kappa,
\]
and
\[
A=\mathbb E[X^2],
\qquad
B=\mathbb E[X^3].
\]
Thus the sharp universal threshold is
\[
2\left[
\sup
\frac{\mathbb E[X^3]}{\mathbb E[X^2]^{3/2}}
\right]^{-1}.
\]

Put \(Y=X^2\). Since \(Y\in[a^2,1]\) and \(y^{3/2}\) is convex, for fixed \(\mathbb E[Y]\) the quantity \(\mathbb E[Y^{3/2}]\) is maximized by an endpoint distribution. Hence it is enough to put probability \(p\) at \(X=1\) and \(1-p\) at \(X=a\).

Then
\[
A=a^2+p(1-a^2),
\qquad
B=a^3+p(1-a^3).
\]
Maximizing
\[
\frac{B}{A^{3/2}}
\]
gives
\[
p_\star
=
\frac{a^2(a+2)}
{(a+1)(a^2+a+1)}.
\]
At this point
\[
A_\star=\frac{3a^2}{a^2+a+1},
\qquad
B_\star=\frac{2a^2}{a+1}.
\]
Therefore
\[
\rho_\star
=
\frac{2A_\star^{3/2}}{B_\star}
=
\frac{3\sqrt{3}\,a(a+1)}
{(a^2+a+1)^{3/2}}.
\]
Substituting \(a=1/\kappa\) gives the stated formula, while the endpoint mixture gives the equality witness and proves sharpness.

## Verification

`verify.py` checks the closed form, the exact two-dimensional witness, immediate failure above the frontier, dense two-point scans, and random higher-dimensional spectra.

The numerical tests are only transcription guards. The continuum extremum follows from the convex-chord reduction and exact one-variable maximization above.

## Relationship to prior work

You, Gitman, and Ginsburg introduced LARS to control each layer's update relative to its weight norm, using a local rate proportional to
\[
\frac{\|w\|_2}{\|\nabla L(w)\|_2}
\]
and a trust coefficient. Their source explicitly links overly large relative updates to instability.

Gitman, Dilipkumar, and Parr then isolated the proportional update
\[
w_{k+1}
=
w_k-\lambda_k
\frac{\|w_k\|_2}{\|\nabla L(w_k)\|_2}
\nabla L(w_k)
\]
and analyzed one-dimensional quadratics and general convex objectives. The inspected theory does not give a sharp multidimensional SPD condition-number threshold.

Huo, Gu, and Huang later gave sufficient convergence bounds for layer-wise scaling and interpreted LARS as approximating inverse layer smoothness. Their bounds depend on smoothness and gradient variance and do not optimize the exact deterministic one-step condition over an SPD spectrum.

Focused published-record comparisons found exact objective frontiers for scaled Polyak, Barzilai–Borwein, and Cauchy trust-region steps, but those use different step constructions and do not imply the LARS formula above.

## Limitations

The theorem excludes momentum and weight decay, both present in practical LARS training.

It gives one-step objective monotonicity, not a new global convergence-rate theorem.

The sharp witness is an adversarial two-eigenvalue mixture and need not be typical of neural-network layers.

Mini-batch variance can impose stricter practical trust limits.

## References

1. Yang You, Igor Gitman, and Boris Ginsburg, “Large Batch Training of Convolutional Networks,” arXiv:1708.03888v1, 2017.
2. Igor Gitman, Deepak Dilipkumar, and Ben Parr, “Convergence Analysis of Gradient Descent Algorithms with Proportional Updates,” arXiv:1801.03137v1, 2018.
3. Zhouyuan Huo, Bin Gu, and Heng Huang, “Large Batch Optimization for Deep Learning Using New Complete Layer-Wise Adaptive Rate Scaling,” AAAI 2021, DOI `10.1609/aaai.v35i9.16962`.
