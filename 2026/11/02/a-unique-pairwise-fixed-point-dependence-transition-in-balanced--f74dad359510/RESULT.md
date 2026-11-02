# A unique pairwise fixed-point dependence transition in balanced two-block Gibbs permutations

## Finding

For each integer \(m\ge 2\), divide \(\{1,\ldots,2m\}\) into equal blocks \(A\) and \(B\), and sample a permutation \(\sigma\) with probability proportional to \(\theta^{K(\sigma)}\), where \(\theta>0\) and \(K(\sigma)=\#\{i\in A:\sigma(i)\in A\}\). For two distinct labels \(i,j\in B\), let \(I_i=\mathbf 1_{\{\sigma(i)=i\}}\) and \(I_j=\mathbf 1_{\{\sigma(j)=j\}}\).

Define the strictly positive polynomial on \(\theta>0\)
\[
Z_m(\theta)=\sum_{k=0}^{m}\binom{m}{k}^{2}\theta^k,
\]
and
\[
H_m(\theta)=m^2 Z_m(\theta)Z_m''(\theta)
 -(m-1)^2\bigl(Z_m'(\theta)\bigr)^2.
\]
Then the covariance is **exactly**
\[
\operatorname{Cov}(I_i,I_j)
 =\frac{\theta^2 H_m(\theta)}{m^4(m-1)^2 Z_m(\theta)^2}.
\]
There exists a **unique** \(\theta_m\in(0,1)\) for which \(H_m(\theta_m)=0\). The covariance is strictly negative for \(0<\theta<\theta_m\), zero at \(\theta_m\), and strictly positive for \(\theta>\theta_m\). This holds for every pair of different labels within either block. Moreover,
\[
\boxed{\lim_{m\to\infty}\theta_m=\frac14.}
\]
For each fixed \(\theta>0\), setting \(x=\sqrt\theta/(1+\sqrt\theta)\), the asymptotic dependence strength is
\[
\boxed{\lim_{m\to\infty}m^3\operatorname{Cov}(I_i,I_j)
 =\frac{x(3x-1)}{2}.}
\]
For \(m=2\), the exact transition is \(\theta_2=\sqrt 6-2\).

## Assumptions and scope

The blocks have exactly \(m\) *distinguishable* labels each, \(m\ge2\), and the measure on the \((2m)!\) bijections is the normalized Gibbs weight specified above. A block-to-block match counts an image in the same block; an individual fixed point requires the image to equal its original label. There are no assumptions of independence among fixed-point indicators. Every \(\theta\) is strictly positive. The theorem concerns two *distinct fixed points in the same block*, not pairs from different blocks, and is independent of the labels chosen within that block. The asymptotic formulas keep \(\theta\) fixed as \(m\) grows, except for the separately stated convergence of the threshold itself.

## Proof

**1. Exact conditional matching law.** To construct a permutation with \(K=k\), first choose which \(k\) values of block \(A\) and which \(m-k\) values of block \(B\) are images of the \(m\) rows of \(A\), and then biject the two row blocks onto their allocated output sets. This gives exactly \((m!)^2\binom{m}{k}^2\) permutations. Hence
\[
\Pr(K=k)=\frac{\binom{m}{k}^2\theta^k}{Z_m(\theta)}
\quad (0\le k\le m).
\]
By the equal block sizes, exactly \(k\) rows in \(B\) also map into \(B\). Conditional on \(K=k\), the induced partial matching of these rows and columns is uniform. Therefore, for distinct \(i,j\in B\),
\[
\Pr(I_i=1\mid K=k)=\frac{k}{m^2},\qquad
\Pr(I_i=I_j=1\mid K=k)=\frac{k(k-1)}{m^2(m-1)^2}.
\]
As \(\mathbb E(K)=\theta Z_m'/Z_m\) and \(\mathbb E(K(K-1))=\theta^2 Z_m''/Z_m\), subtracting the product of marginal probabilities proves the displayed exact covariance identity. Identical block symmetry gives the assertion for \(A\).

**2. A unique covariance sign switch.** The Legendre polynomial identity (also used for this block-uniform normalizer by Ottolini and Starr [1])
\[
Z_m(\theta)=(1-\theta)^m
 P_m\!\left(\frac{1+\theta}{1-\theta}\right)
\]
holds first for \(\theta\ne1\), then polynomially at \(\theta=1\). It follows either from the binomial expression for Legendre polynomials or from the recurrence
\[
(m+1)Z_{m+1}=(2m+1)(1+\theta)Z_m-m(1-\theta)^2Z_{m-1}
\]
with \(Z_0=1\), \(Z_1=1+\theta\). The standard Rodrigues formula and orthogonality of \(P_m\) to every polynomial of degree below \(m\) show that \(P_m\) has exactly \(m\) distinct roots in \((-1,1)\): otherwise multiply its sign-changing factors to obtain a polynomial of degree less than \(m\) whose product with \(P_m\) has constant nonzero sign, contradicting orthogonality. The Möbius substitution maps these roots to \(m\) distinct negative roots of \(Z_m\). Thus, for some distinct \(\rho_1,\dots,\rho_m>0\),
\[
Z_m(\theta)=\prod_{a=1}^m(\theta+\rho_a).
\]
Put \(S_r(\theta)=\sum_{a=1}^m(\theta+\rho_a)^{-r}\). Then \(Z_m'/Z_m=S_1\), \(Z_m''/Z_m=S_1^2-S_2\), and
\[
\frac{H_m}{Z_m^2}=(2m-1)S_1^2-m^2S_2.
\]
The ratio \(R=S_1^2/S_2\) has strictly positive derivative
\[
R'=\frac{2S_1(S_1S_3-S_2^2)}{S_2^2}>0.
\]
Indeed Cauchy--Schwarz gives \(S_1S_3>S_2^2\) since the \(\rho_a\) are distinct and \(m\ge2\). Consequently the sign of \(H_m\) changes **at most once**, from negative to positive. At zero,
\[
H_m(0)=-\frac{m^4(m-1)^2}{2}<0.
\]
At \(\theta=1\), the permutation is uniform, so two distinct fixed-point events have covariance \(1/[4m^2(2m-1)]>0\). Continuity and strict monotonicity of \(R\) imply one and only one root, lying in \((0,1)\), with the claimed signs. For \(m=2\), \(H_2=4(\theta^2+4\theta-2)\), proving \(\theta_2=\sqrt6-2\).

**3. Large-block limit.** The binomial-square polynomial has the exact integral representation
\[
Z_m(\theta)=\frac1{2\pi}\int_{-\pi}^{\pi}
 (1+\theta+2\sqrt\theta\cos t)^m\,dt.
\]
For each fixed \(\theta>0\), the integrand has a unique maximal point at \(t=0\), and its logarithm has quadratic term \(-m\sqrt\theta\,t^2/(1+\sqrt\theta)^2\). Splitting into a shrinking Gaussian window and its exponentially smaller complement gives the classical, differentiable Laplace estimate, uniformly on compact positive \(\theta\)-intervals,
\[
Z_m(\theta)=\frac{(1+\sqrt\theta)^{2m+1}}
 {2\sqrt{\pi m\sqrt\theta}}\bigl(1+O(m^{-1})\bigr).
\]
The first two logarithmic derivatives with respect to \(\log\theta\) have matching differentiated expansions: local Taylor expansion after the change \(t=v/\sqrt m\), together with Gaussian domination, justifies differentiating under the integral and the uniform error estimates. Therefore
\[
\mathbb E K=m x+O(1),\qquad
\operatorname{Var}(K)=\frac{m}{2}x(1-x)+O(1),
\quad x=\frac{\sqrt\theta}{1+\sqrt\theta}.
\]
The exact covariance formula in Step 1 can equivalently be written
\[
\operatorname{Cov}(I_i,I_j)=
\frac{m^2\operatorname{Var}(K)+(2m-1)(\mathbb E K)^2-m^2\mathbb E K}
 {m^4(m-1)^2}.
\]
Substitution yields \(m^3\operatorname{Cov}(I_i,I_j)\to x(3x-1)/2\). Since the limiting expression is negative for \(0<\theta<1/4\) and positive for \(\theta>1/4\), while the finite-size covariance has exactly one sign switch, every fixed \(\theta\) below or above \(1/4\) eventually lies on the corresponding side of \(\theta_m\). Hence \(\theta_m\to1/4\), completing the proof.

## Verification

The standalone standard-library file `verify.py` enumerates every permutation for block sizes \(m=2,3,4\), independently counts the conditioning classes and each pair of fixed-point events, and compares their rational probabilities with the formula at five positive rational parameter values. It separately reproduces the Legendre recurrence coefficients through size 18, checks polynomial boundary identities through size 17, and produces rational threshold brackets for sizes 2 through 13. Its actual execution returned **633 passed exact-integer/rational assertions**. The finite checks are supplementary: the preceding analytical proof establishes the statements for every \(m\ge2\) and every \(\theta>0\). Run with `python3 verify.py` from a directory containing the extracted file; no third-party packages are required.

## Relationship to prior work

Ottolini and Starr (2026), arXiv:2605.25274, Section 2 and Appendix A, explicitly enumerate **the same two-block permutation partition function** and its transformed Legendre polynomial form, and establish block-uniform permanent asymptotics. The polynomial and its basic large-size asymptotics are therefore prior results, not claimed discoveries. The new assertion here is the exact joint covariance of two individually tagged diagonal fixed points, its **unique sign transition for every finite block size**, and the limiting threshold 1/4. Ottolini--Starr do not state this event-level covariance sign diagram in their inspected text. Duan, Lyu and Powell (2026), arXiv:2610.14616, equations (1.10)--(1.12), establish the general Gibbs-permutation/Poisson-contingency correspondence; their Theorem 2.10 concerns macroscopic linear-statistic fluctuations rather than microscopic tagged fixed points. Classical Fisher noncentral hypergeometric probabilities give the block count \(K\), while Johnson, Leader and Long (2019), arXiv:1909.03770, prove association for Bruhat-order up-sets under different permutation-measure hypotheses. These comparisons distinguish exact statements and implications rather than rebranding the known partition function, Legendre representation, or saddle-point asymptotics.

## Limitations

No statement is made for marked pairs in different blocks, uneven block sizes, zero or infinite parameter values, general non-block weights, or parameter sequences tending to zero or infinity with the block size. The covariance tends to zero at each fixed positive parameter; its rescaled sign is the information identified here. A search of the accessible sources and mathematical records did not identify the same threshold theorem, but it cannot establish definitive historical priority. The result has not undergone independent mathematical validation.

## References

1. A. Ottolini and S. Starr (2026), *Pal’s permanent conjecture: proof for block uniform matrices*, arXiv:2605.25274 (first posted 2026-05-24), https://arxiv.org/abs/2605.25274 .
2. D. Duan, H. Lyu and W. Powell (2026), *Poisson contingency tables, Gibbs permutations, and entropic optimal transport*, arXiv:2610.14616 (first posted 2026-10-10), https://arxiv.org/abs/2610.14616 .
3. J. R. Johnson, I. Leader and E. Long (2019), *Correlation for permutations*, arXiv:1909.03770, https://arxiv.org/abs/1909.03770 .
4. Fisher's noncentral hypergeometric distribution, SciPy statistical reference (mass law), https://scipy.github.io/devdocs/tutorial/stats/discrete_nchypergeom_fisher.html .
5. Standard Legendre Rodrigues formula, orthogonality, and Laplace's method; the required versions and their applications are reconstructed above.
