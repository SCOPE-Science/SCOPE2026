# Exact finite-atom \(L^4\) mean-reflection constants and the irrational attainment gap

## Finding
Let \(n\ge2\) be an integer, \(\mathbf 1=(1,\dots,1)\in\mathbb R^n\), and let
\[
R_n x=x-\frac{2}{n}\left(\sum_{j=1}^n x_j\right)\mathbf 1,
\qquad C_n=\sup_{x\in\mathbb R^n\setminus\{0\}}\frac{\|R_nx\|_4}{\|x\|_4}.
\]
Write \(\ell=n-k\), and for \(1\le k\le\lfloor n/2\rfloor\) set
\[
F_{n,k}(t)=\frac{k((n-2k)t-2\ell)^4+\ell(-2kt+2k-n)^4}
{n^4(kt^4+\ell)},\qquad t\in\mathbb R,
\]
with \(F_{n,k}(\infty)=\big(k(n-2k)^4+\ell(2k)^4\big)/(n^4 k)\). Set
\[
Q_{n,k}(t)=k(4k-n)t^4+4k(n-k)(t^3+t)+(n-k)(3n-4k).
\]
Then the **exact finite algebraic determination, for every dimension**, is
\[
\boxed{C_n^4=\max\bigg(\{1\}\cup
\bigcup_{k=1}^{\lfloor(n-1)/2\rfloor}
\{F_{n,k}(t):Q_{n,k}(t)=0,\ t\in\mathbb R\}
\cup\{F_{n,k}(\infty)\}\bigg).}
\]
Thus at most \(4\lfloor(n-1)/2\rfloor\) finite real algebraic candidates plus explicit endpoint candidates suffice; the formula is exact, not a sampling recipe. In particular, \(C_2=1\), \(C_4=\sqrt2\). For \(n=8\) let \(\tau\) be the unique negative real zero of
\[
q(t)=t^4-7t^3-7t-35.
\]
Then
\[
\boxed{C_8^4=\frac{11\tau^4-84\tau^3+378\tau^2-420\tau+371}
{32(\tau^4+7)},\quad C_8=1.5445210906900528884\ldots.}
\]
Every finite \(n\) obeys a strict universal bound, but the bound is asymptotically optimal:
\[
\boxed{C_n<\sqrt{1+\sqrt2}\quad(n\ge2),\qquad
\lim_{n\to\infty}C_n=\sqrt{1+\sqrt2}.}
\]
The strict inequality is forced by the irrational mass of every extremizing two-point probability distribution in the unrestricted moment problem.

## Assumptions and scope
All scalars and \(L^4\) norms here are **real**. Finite-dimensional \(\|x\|_4^4=\sum_j|x_j|^4\); normalized expectation \(\mathbb E\) below is either the uniform measure on \(n\) atoms or a general real probability law. There are no assumptions on signs, coordinate ordering, or the number of nonzero entries. The transformation \(R_n\) is an involution: its one-dimensional constant subspace has eigenvalue \(-1\), while its mean-zero hyperplane has eigenvalue \(+1\). When \(n\) is a power of two it is diagonally isometrically conjugate to a single nonconstant Haar-sign flip; this observation does **not** assert the complete finite-level Haar unconditional constant.

## Proof
**Two-level reduction.** For any real \(\lambda\),
\[
H_\lambda(x)=\lambda\sum_{j=1}^n x_j^4-\sum_{j=1}^n(R_nx)_j^4
\]
is a homogeneous symmetric quartic. By the half-degree principle for symmetric real polynomials (Riener, Theorem 1.3; Blekherman--Riener, Proposition 3.1), \(H_\lambda\ge0\) on all of \(\mathbb R^n\) if and only if it is nonnegative on vectors having at most two distinct coordinate values. Applying the equivalence with \(\lambda=C_n^4\) and compactness of the unit sphere proves that an exact maximizer can be taken two-valued. A nonzero two-valued vector can be scaled and permuted to have \(k\) coordinates \(t\), and \(n-k\) coordinates \(1\); the case in which the second value is zero is represented by \(t=\infty\). Swapping the blocks gives \(k\le n/2\). Evaluating the coordinates of \(R_nx\) gives \(F_{n,k}\) exactly. If \(2k=n\), \(F_{n,k}\equiv1\).

**Finite stationary calculation.** Put \(U=k((n-2k)t-2(n-k))^4+(n-k)(-2kt+2k-n)^4\) and \(V=kt^4+n-k\). Direct binomial multiplication, without division by a potentially zero stationary factor, gives
\[
U'(t)V(t)-U(t)V'(t)
=-8kn(k-n)(2k-n)(t-1)^2 Q_{n,k}(t).
\]
For \(k<n/2\), the stationary candidates of \(F_{n,k}=U/(n^4V)\) are \(t=1\) (where \(F=1\)) and the real roots of \(Q_{n,k}\). The only remaining projective point is \(t=\infty\). This proves the boxed all-dimensional formula, including when the quartic leading coefficient vanishes. For \(n=2\) the only block size is \(k=n/2\), giving \(C_2=1\).

**The four-atom and eight-atom exact values.** For \(n=4\) only \(k=1\) matters, with
\[
F_{4,1}(t)=\frac{t^4+18t^2-24t+21}{4(t^4+3)},\qquad
4-F_{4,1}(t)=\frac{3(t+1)^2(5t^2-10t+9)}{4(t^4+3)}\ge0.
\]
Equality at \(t=-1\) proves \(C_4^4=4\). For \(n=8\), the branches \(k=2\) and \(k=4\) are bounded by \(4\) and \(1\), respectively. The \(k=3\) branch is
\[
F_{8,3}(t)=\frac{51t^4+60t^3+90t^2-180t+235}{32(3t^4+5)}.
\]
Its gap from \(4\) has numerator \(333t^4-60t^3-90t^2+180t+405\), which is bounded below by \(303t^4-210t^2+315>0\): use \(-60t^3\ge-30t^4-30t^2\), \(180t\ge-90t^2-90\), and positivity of the remaining quadratic in \(t^2\). The remaining branch is
\[
F_{8,1}(t)=\frac{11t^4-84t^3+378t^2-420t+371}{32(t^4+7)},\quad
F'_{8,1}(t)=\frac{21(t-1)^2q(t)}{8(t^4+7)^2}.
\]
The polynomial \(q(-u)=u^4+7u^3+7u-35\) is strictly increasing on \(u>0\), so \(q\) has exactly one negative root \(\tau\); Descartes' sign rule gives exactly one positive root. The derivative therefore changes from positive to negative at \(\tau\), from negative to positive at the positive root, and is otherwise nonzero apart from a horizontal stationary point at \(1\). Since \(F_{8,1}(-1)=79/16>4\), whereas \(F_{8,1}(\pm\infty)=11/32\), the unique global maximum occurs at \(\tau\). This also strictly exceeds all other \(k\)-branches, proving the eight-atom claim.

**Universal bound and arithmetic obstruction.** Let \(X\) be any nonconstant real random variable with finite fourth moment. Set \(\mu=\mathbb EX\), \(Y=X-\mu\), \(v=\mathbb EY^2>0\), \(z=\mu/\sqrt v\), \(\gamma=\mathbb EY^3/v^{3/2}\), and \(\kappa=\mathbb EY^4/v^2\). Cauchy--Schwarz for \(Y^2-v\) and \(Y\) gives Pearson's moment inequality \(\kappa\ge1+\gamma^2\). Expanding the fourth moments yields
\[
\frac{\mathbb E|X-2\mathbb EX|^4}{\mathbb E|X|^4}
=\frac{\kappa-4z\gamma+6z^2+z^4}{\kappa+4z\gamma+6z^2+z^4}.
\]
When \(z\gamma\ge0\), this ratio is at most \(1\). Otherwise put \(\eta=4|z\gamma|/(\kappa+6z^2+z^4)\). Elementary maximization of \(g/(g^2+B)\), with \(B=1+6z^2+z^4\), implies
\[
\eta\le\frac{2|z|}{\sqrt{1+6z^2+z^4}}\le\frac1{\sqrt2},
\qquad \frac{1+\eta}{1-\eta}\le3+2\sqrt2.
\]
The second inequality is equivalent to \((z^2-1)^2\ge0\). Equality forces \(z^2=1\), \(\gamma^2=8\), \(\kappa=9\), \(z\gamma<0\), and equality in Pearson's inequality. The latter forces \(Y\) to lie almost surely in the two roots of a quadratic; its nonzero atom masses must be \(\alpha_\ast=(3-\sqrt6)/6\) and \(1-\alpha_\ast\) (obtained from \(\gamma^2=(1-2\alpha)^2/(\alpha(1-\alpha))=8\)). These masses are irrational. Conversely this two-point law with appropriate nonzero mean and sign satisfies all equality conditions, so \(3+2\sqrt2\) is the unrestricted sharp fourth-power constant. Every two-valued law on a **uniform** finite \(n\)-point space has rational masses \(k/n\), hence cannot attain equality. The compactness of its unit sphere implies the strict upper bound for \(C_n\). Finally choose \(k_n/n\to\alpha_\ast\), approximate the two-point equality law by vectors with \(k_n\) coordinates at its first value and \(n-k_n\) at the second; continuity of the fourth-moment ratio gives the asserted limit.

## Verification
The accompanying standard-library script `CHECK.py` checks the exact rational-polynomial expansions, the derivative factorization for numerous integer dimension/count pairs as a diagnostic, the four-atom sharp inequality, all eight-atom branch identities, and a rational interval enclosing the unique negative root. Its finite checks do not prove the theorem for all dimensions; that universal quantifier rests on the half-degree principle and the displayed binomial identity, and the strict universal gap rests on the analytic moment proof. Run from this directory with `python CHECK.py`. Expected final line: `EXACT_IDENTITIES_OK`.

## Relationship to prior work
Riener's half-degree principle (first public preprint January 2010, Theorem 1.3) supplies the substantive symmetry reduction, **not** the displayed induced-operator norm profile, its eight-atom value, or its uniform-atom rigidity. Blekherman--Riener independently states the applicable criterion for symmetric quartic forms (Proposition 3.1). Osękowski's 2013 paper treats sharp restricted weak-type Haar projection and martingale-transform inequalities over nonatomic spaces, rather than the sharp finite uniform-atom fourth-norm of one sign reflection. Shargorodsky--Sharia (first published December 2022), Section 1 and Section 2, explicitly compute and discuss the different operator \(I-E\) (centering, with coefficient \(1\)) and its finite-atomic constant using Franchetti and Lewicki--Skrzypek. The present transformation is \(I-2E\), whose invariant and optimizer are different; the cited \(I-E\) formula does not imply the claimed values. The close 2016 hyperplane-projection article is only partly accessible here, and historical coverage remains possible.

## Limitations
The result concerns real scalars, the constant expectation on **uniform** atoms, and one fixed reflection only. It does not compute complex \(\ell_4\) norms, arbitrary weighted-atom spectra, all Haar sign patterns, or the full unconditional Haar constant. The degree-four reduction relies on an established external theorem; the checker is finite and does not replace that theorem. The claim's originality has a residual risk from historical projection/reflection literature not fully retrieved, notably Lewicki--Skrzypek (2016) and Franchetti (1990). No independent validation has been performed.

## References
1. C. Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464v1 (25 January 2010); Journal of Pure and Applied Algebra 216 (2012), 850–856. https://arxiv.org/abs/1001.4464 (Theorem 1.3, original preprint and full-text HTML examined).
2. G. Blekherman and C. Riener, *Symmetric Non-Negative Forms and Sums of Squares*, arXiv:1205.3102v1 (14 May 2012); Discrete & Computational Geometry 65 (2021), 764–799; DOI 10.1007/s00454-020-00208-w (Proposition 3.1, full text examined).
3. A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces (2013), article 646012; DOI 10.1155/2013/646012 (published 5 December 2013, full text examined).
4. E. Shargorodsky and T. Sharia, *Sharp estimates for conditionally centered moments and for compact operators on \(L^p\) spaces*, Mathematische Nachrichten 296 (2023), 368–381; DOI 10.1002/mana.202100217 (first published 18 December 2022, full text examined).
5. G. Lewicki and L. Skrzypek, *Minimal projections onto hyperplanes in \(\ell_p^n\)*, Journal of Approximation Theory 202 (2016), 42–63; DOI 10.1016/j.jat.2015.11.005 (bibliographic and abstract evidence only).
6. C. Franchetti, *The norm of the minimal projection onto hyperplanes in \(L^p[0,1]\) and the radial constant*, Boll. Unione Mat. Ital. B (7) 4 (1990), 803–821 (identified through references in source 4; full text not inspected).
