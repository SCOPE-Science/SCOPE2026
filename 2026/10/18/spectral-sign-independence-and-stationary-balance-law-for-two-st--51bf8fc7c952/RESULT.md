# Spectral-sign independence and stationary-balance law for two-state Dirichlet Markov matrices

## Finding

Let \(\alpha>0\) and let \(U,V\) be independent \(\operatorname{Beta}(\alpha,\alpha)\) random variables. Define the stochastic matrix
\[
P=\begin{pmatrix}1-U&U\\V&1-V\end{pmatrix},\quad
\Pi=\frac{V}{U+V},\quad \Lambda=1-U-V.
\]
Here \(\Pi\) is the stationary mass of state one (first matrix coordinate), and \(\Lambda\) is the nontrivial transition eigenvalue. The event \(\Lambda\ge0\) has positive probability for every \(\alpha>0\).

**Classification.** Conditional on \(\Lambda\ge0\), the random variables \(\Pi\) and \(\Lambda\) are independent if and only if \(\alpha=1\). In that exceptional case the conditional law of \(\Pi\) is uniform on \((0,1)\). For every \(\alpha>0\), conditional independence on \(\Lambda<0\) is impossible because the conditional support of \(\Pi\) depends nontrivially on \(\Lambda\).

**Complete exceptional joint law.** At \(\alpha=1\), the joint Lebesgue density of \((\Pi,\Lambda)\) is
\[
f_{\Pi,\Lambda}(r,\ell)=(1-\ell)\mathbf1_{\mathcal D}(r,\ell),
\]
where the support \(\mathcal D\) is the union of
\[
0<\ell<1,\quad 0<r<1,
\]
and
\[
-1<\ell<0,\quad \frac{-\ell}{1-\ell}<r<\frac1{1-\ell}.
\]
The eigenvalue density is \(f_\Lambda(\ell)=1-|\ell|\) for \(-1<\ell<1\), and
\[
\operatorname{Var}(\Pi\mid\Lambda=\ell)=
\begin{cases}
1/12,&0<\ell<1,\\
(1+\ell)^2/[12(1-\ell)^2],&-1<\ell<0.
\end{cases}
\]
In addition, \(\mathbb E\Pi=1/2\), \(\operatorname{Var}\Pi=3/4-\log2\), \(\operatorname{Cov}(\Pi,\Lambda)=0\), while
\[
\operatorname{Cov}\big((\Pi-1/2)^2,\Lambda\big)=\frac76-\frac53\log2>0.
\]
Thus ordinary uncorrelatedness conceals a strict stationary-balance/eigenvalue dependence.

## Assumptions and scope

The two states are fixed and labeled. Both rows of \(P\) are independently symmetric Dirichlet with shape parameter \(\alpha>0\). All assertions concern the exact probability law, without a large-matrix limit or a requirement of aperiodicity beyond the almost-sure positivity of the entries. The matrices are irreducible and aperiodic almost surely. Conditioning at the single event \(\Lambda=0\) is irrelevant because it has probability zero. Formulae involving \(\alpha=1\) refer precisely to the uniform measure on the square of off-diagonal probabilities, equivalently the uniform Dirichlet Markov ensemble of order two.

## Proof

Write \(S=U+V=1-\Lambda\) and \(R=V/S=\Pi\). Their inverse transformation is \(U=S(1-R)\) and \(V=SR\). Its absolute Jacobian is \(S\). Since \(U,V\) lie in \((0,1)\), the transformed support is
\[
0<s<2,\qquad \max(0,1-1/s)<r<\min(1,1/s).
\]
Writing \(B(\alpha,\alpha)\) for the beta integral, the joint density is
\[
f_{S,R}(s,r)=\frac{s^{2\alpha-1}}{B(\alpha,\alpha)^2}
[r(1-r)(1-sr)(1-s+sr)]^{\alpha-1}
\]
on this support, and zero elsewhere. This establishes all scope restrictions, including the support contraction when \(1<s<2\) (equivalently \(\Lambda<0\)). Since the conditional support for \(R\) varies with \(s\) in this regime and every conditional density is positive in its interior, independence there is impossible.

When \(0<s<1\), the conditional support of \(R\) is all of \((0,1)\). At \(\alpha=1\) the joint density reduces to \(s\), so the conditional law of \(R\) is uniform and does not depend on \(s\). Conversely, for \(\alpha\ne1\), the ratio between the conditional densities at \(r=1/2\) and \(r=1/4\) equals
\[
\left[\frac{4(1-s/2)^2}{3(1-s/4)(1-3s/4)}\right]^{\alpha-1}.
\]
The expression inside brackets is not constant on \((0,1)\): its limits as \(s\downarrow0\) and \(s\uparrow1\) are \(4/3\) and \(16/9\). Independence would make this conditional-density ratio constant in \(s\). Hence it fails for every \(\alpha\ne1\), proving the if-and-only-if classification.

At \(\alpha=1\), the support and Jacobian give \(f_{S,R}(s,r)=s\). Replacing \(s\) by \(1-\ell\) proves the joint density in the finding. Integrating over \(r\) gives \(f_S(s)=s\) for \(0<s<1\) and \(f_S(s)=2-s\) for \(1<s<2\); this is equivalent to the stated triangular eigenvalue law. Conditional on \(S=s\), \(R\) is uniform on a centered interval of width one for \(s<1\), or width \((2-s)/s\) for \(s>1\). Thus conditional expectation is always \(1/2\), and the variance formula follows from the variance of a uniform interval.

For the remaining unconditional assertions, integration over \(s\) yields
\[
f_\Pi(r)=\begin{cases}
[2(1-r)^2]^{-1},&0<r<1/2,\\
(2r^2)^{-1},&1/2<r<1.
\end{cases}
\]
Symmetry under \(U\leftrightarrow V\) gives \(\mathbb E\Pi=1/2\) and \(\operatorname{Cov}(\Pi,\Lambda)=0\). By the law of total variance and elementary integration,
\[
\begin{aligned}
\operatorname{Var}\Pi&=\int_0^1\frac{s}{12}\,ds+
\int_1^2\frac{(2-s)^3}{12s^2}\,ds=\frac34-\log2,\\
\mathbb E[(\Pi-1/2)^2\Lambda]&=
\int_0^1\frac{(1-s)s}{12}\,ds+
\int_1^2\frac{(1-s)(2-s)^3}{12s^2}\,ds
=\frac76-\frac53\log2.
\end{aligned}
\]
As \(\mathbb E\Lambda=0\), the latter is the claimed covariance. It is strictly positive, for example because the variance of \(R\) is nondecreasing in \(\Lambda\), and strictly increasing on \((-1,0)\); Chebyshev's covariance identity gives strict positivity. This completes the proof.

## Verification

The standalone `verify.py` checks the exact inverse Jacobian, marginal normalizations, two moment integrals, nonconstant conditional odds, and 1,444 rational parameter pairs. Execute `python verify.py` with SymPy installed. The finite grid and symbolic replay are checks; the general theorem follows from the analytic density transformation and its support, not numerical sampling.

## Relationship to prior work

Chafaï introduced the uniform Dirichlet Markov ensemble and proved that its rows are independent uniform simplex vectors [1, Theorem 1.1], a fact used as the starting premise here. That paper addresses matrix structure and large-dimensional singular/eigenvalue laws; its inspected introduction, results, and discussion do not give this stationary-mass/nontrivial-eigenvalue joint law or the conditional independence classification across symmetric Dirichlet shape parameters. Bordenave, Caputo, and Chafaï subsequently proved high-dimensional circular-law results for random Markov matrices [2], also without the present finite two-state paired-invariant classification. The stationary mass \(V/(U+V)\) and eigenvalue \(1-U-V\) themselves are elementary standard facts and are not claimed as new. Novelty is restricted to their stated exact joint-law/conditional-independence synthesis and the sharp shape-parameter exception, subject to residual priority risk.

## Limitations

The theorem concerns only two-state independently generated symmetric Dirichlet rows. For larger matrices, the stationary measure and nontrivial eigenvalues are not represented by the same two scalar variables. No universality claim for general priors is made. The exact formulas use a short change of variables, so previous implicit publication or treatment as an elementary consequence of known matrix densities is an important unresolved historical-priority risk. Independent literature-priority and scientific reviews have not been performed.

## References

[1] D. Chafaï, *The Dirichlet Markov Ensemble*, arXiv:0709.4678 (first publicly submitted 2007-09-28), especially Theorem 1.1 and the discussion of eigenvalues, https://arxiv.org/abs/0709.4678.

[2] C. Bordenave, P. Caputo, D. Chafaï, *Circular Law Theorem for Random Markov Matrices*, arXiv:0808.1502 (first submitted 2008-08-11), especially Section 1.1, https://arxiv.org/abs/0808.1502.
