# A unique conditioning reversal between fixed-norm sign and sphere probes in one-node log-determinant Lanczos quadrature

## Finding

For the positive definite two-by-two diagonal matrix \(A_\kappa=\operatorname{diag}(\kappa,1)\), with \(\kappa>1\), estimate \(\log\det A_\kappa=\log\kappa\) using one sample and exactly one Lanczos node. Two zero-mean, isotropic, identically normed probe distributions exchange their ranking in squared-error risk exactly once as the condition number increases. For independent Rademacher signs \(z_R=(\varepsilon_1,\varepsilon_2)\) and a uniform sphere probe \(z_S=\sqrt{2}(\cos\Theta,\sin\Theta)\), \(\Theta\sim\operatorname{Unif}[0,2\pi)\), write \(M_R(\kappa)=\mathbb E[(Q(z_R)-\log\kappa)^2]\) and \(M_S(\kappa)=\mathbb E[(Q(z_S)-\log\kappa)^2]\). For \(u=\tfrac12\log\kappa\) and \(x=\tanh^2(u/2)\),

\[
M_R=4\log^2\cosh u,\qquad
M_S=16\log^2\cosh(u/2)+8\operatorname{Li}_2(x).
\]

Here \(\operatorname{Li}_2(x)=\sum_{j=1}^\infty x^j/j^2\) for \(0\le x<1\). There is a unique \(x_*\in(0,1)\) satisfying

\[
-\log(1-x_*)\log(1+x_*)+\tfrac12\log^2(1+x_*)-\operatorname{Li}_2(x_*)=0.
\]

Let \(\kappa_*=((1+\sqrt{x_*})/(1-\sqrt{x_*}))^2\approx254.078784541\). Then \(M_R<M_S\) for \(1<\kappa<\kappa_*\), equality holds at \(\kappa_*\), and \(M_S<M_R\) for \(\kappa>\kappa_*\). At \(\kappa=1\) both are exact. In particular, the sign probe has zero sampling variance but greater squared error than the spherical probe at high condition number.

## Assumptions and scope

Fix any finite \(\kappa\ge1\), the real matrix \(A_\kappa=\operatorname{diag}(\kappa,1)\), the real principal matrix logarithm, and a single fixed-norm probe \(z\in\mathbb R^2\), \(\|z\|_2^2=2\). The **one-node Lanczos approximation** to \(z^\top\log(A_\kappa)z\) is

\[
Q(z)=\|z\|_2^2\log\left(\frac{z^\top A_\kappa z}{\|z\|_2^2}\right)=2\log\left(\frac{z^\top A_\kappa z}{2}\right).
\]

Both probe distributions have \(\mathbb E[zz^\top]=I_2\) and \(\|z\|_2^2=2\) samplewise; \(z_S\) is a normalized Gaussian direction, **not** an unnormalized Gaussian vector. In both cases the computational budget is one matrix-vector product and one Rayleigh quotient. The approximation \(Q(z)\) is generally biased, even though the underlying quadratic trace probe would be unbiased with an exact matrix-logarithm action.

## Proof

For \(z_R\), the Rayleigh quotient is the constant \((\kappa+1)/2\). Consequently the signed output has zero variance and bias

\[
2\log\frac{\kappa+1}{2}-\log\kappa=2\log\cosh u,
\]

which proves the asserted formula for \(M_R\).

For \(z_S\), set \(t=(\sqrt\kappa-1)/(\sqrt\kappa+1)\in[0,1)\) and \(c=((\sqrt\kappa+1)/2)^2\). Elementary trigonometry gives

\[
\kappa\cos^2\Theta+\sin^2\Theta=c\lvert1+t e^{2i\Theta}\rvert^2.
\]

Since \(|t|<1\), the logarithm has an absolutely convergent Fourier series

\[
\log(\kappa\cos^2\Theta+\sin^2\Theta)
=\log c+2\sum_{j\ge1}\frac{(-1)^{j+1}t^j}{j}\cos(2j\Theta).
\]

Orthogonality implies a mean of \(\log c\) and a variance of \(2\sum_{j\ge1}t^{2j}/j^2=2\operatorname{Li}_2(t^2)\). Multiplying by the factor two in \(Q\), its variance is \(8\operatorname{Li}_2(t^2)\). The bias is \(2\log c-\log\kappa=4\log\cosh(u/2)\), yielding the asserted \(M_S\).

To classify all crossings put \(x=t^2\). The hyperbolic identities \(\cosh(u/2)=(1-x)^{-1/2}\) and \(\cosh u=(1+x)/(1-x)\) give

\[
\frac{M_R-M_S}{8}=H(x):=-\log(1-x)\log(1+x)+\tfrac12\log^2(1+x)-\operatorname{Li}_2(x).
\]

Differentiation of its absolutely convergent series gives

\[
H'(x)=\frac{N(x)}{1-x^2},\quad
N(x)=2\log(1+x)+\frac{1-x}{x}\log(1-x),\qquad
N'(x)=\frac{-\log(1-x)-x(1-x)/(1+x)}{x^2}>0
\]

for every \(0<x<1\): indeed \(-\log(1-x)>x>x(1-x)/(1+x)\). Moreover \(N(0+)=-1\) and \(N(1-)=2\log2>0\). Thus \(H\) decreases strictly and then increases strictly, with just one minimum. Since \(H(0)=0\), \(H\) is strictly negative after leaving zero and eventually positive because \(H(x)\to+\infty\) as \(x\uparrow1\); the dilogarithm stays bounded by \(\pi^2/6\). Therefore exactly one interior zero exists. The map \(\kappa\mapsto x=((\sqrt\kappa-1)/(\sqrt\kappa+1))^2\) is a strictly increasing bijection from \((1,\infty)\) to \((0,1)\). This proves the sharp, global, unique reversal. The rational Taylor bounds in the accompanying verifier additionally certify \(0.7778<x_*<0.7779\), which is consistent with the numerical value of \(\kappa_*\).

## Verification

Run `python3 verify.py` using Python 3.10 or later, without third-party packages. The checker evaluates exact rational enclosures for \(H(0.7778)\) and \(H(0.7779)\), including rigorous geometric-series tail bounds, and tests the risk identities at nine positive condition numbers by deterministic angular quadrature. It also compares the computed sign bias and the risk difference. These numerical quadrature tests are diagnostic, **not** a proof for all \(\kappa\); universality and uniqueness are established analytically above.

## Relationship to prior work

Cortinovis and Kressner [1] study randomized trace estimates and Lanczos-based determinant estimation, primarily deriving tail and resource bounds for Rademacher and **unnormalized Gaussian** probes. Chen, Trogdon, and Ubaru [2] develop a unified matrix-free quadrature framework and explicitly treat uniform sphere sampling in their concentration analysis. Li, Huang, and Zhu [3] revisit stochastic Lanczos quadrature with Rademacher and Gaussian sampling and optimize the allocation between sampling and quadrature error. These works motivate the comparison but their inspected results do not state this exact two-dimensional **fixed-norm sphere versus sign**, one-node mean-squared risk crossover or its uniqueness proof. The base Lanczos estimator, sphere distribution, Fourier expansion, and dilogarithm are standard mathematical tools, not claimed as inventions.

## Limitations

The entire finding is confined to a single one-node logarithmic spectral quadrature evaluation of aligned two-dimensional diagonal positive matrices. Its statement is **not** about Hutchinson evaluation of an exact matrix logarithm (which is exact for this diagonal family under a sign probe); not about unnormalized Gaussian probes, multidimensional matrices, arbitrary rotations, multiple probes, or two-or-more-node Lanczos. In dimension two, two Lanczos nodes make the probe quadratic form exact, changing the comparison completely. Both one-node estimates can have large errors for ill-conditioned inputs; the crossover does not imply that sphere probes are globally superior. The exact specialized priority claim has not been independently reviewed; a previous calculation may exist outside the inspected sources.

## References

1. A. Cortinovis and D. Kressner, *On randomized trace estimates for indefinite matrices with an application to determinants*, arXiv:2005.10009 (first posted 2020-05-20), https://arxiv.org/abs/2005.10009; full text https://arxiv.org/html/2005.10009v2.
2. T. Chen, T. Trogdon and S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, arXiv:2204.01941 (first posted 2022-04-05), https://arxiv.org/html/2204.01941v3.
3. W. Li, Y. Huang and S. Zhu, *An analysis on stochastic Lanczos quadrature with asymmetric quadrature nodes*, arXiv:2307.00847 (first posted 2023-07-03), https://arxiv.org/html/2307.00847v5.
