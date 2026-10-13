# A strict dispersion ordering of the two Poisson extremes

## Finding
Let \(X\) and \(Y\) be independent \(\operatorname{Poisson}(\lambda)\) random variables with common parameter \(\lambda>0\). Write \(L=\min(X,Y)\), \(U=\max(X,Y)\), and define their dispersion indices \(D_L=\operatorname{Var}(L)/\mathbb EL\) and \(D_U=\operatorname{Var}(U)/\mathbb EU\). **For every positive intensity,**
\[
\boxed{D_L>D_U.}
\]
In contrast, their unnormalized variances have the opposite strict ordering:
\[
\boxed{\operatorname{Var}(U)-\operatorname{Var}(L)=2\lambda e^{-2\lambda}I_0(2\lambda)>0,}
\]
where \(I_j\) is the modified Bessel function of the first kind of integer order \(j\). Thus the maximum has the larger variance but the smaller variance-to-mean ratio, throughout the entire Poisson intensity range.

The dispersion gap is exactly
\[
\boxed{
D_L-D_U=\frac{2\bigl[b(\lambda)-\lambda c(\lambda)^3\bigr]}{1-c(\lambda)^2},\quad
b(\lambda)=e^{-2\lambda}I_1(2\lambda),\quad
c(\lambda)=e^{-2\lambda}\bigl[I_0(2\lambda)+I_1(2\lambda)\bigr].
}
\]
The numerator is **strictly positive** for all \(\lambda>0\); the main proof establishes the associated nontrivial Bessel inequality. The gap vanishes only in the limiting regimes:
\[
D_L-D_U=\lambda+O(\lambda^2)\quad(\lambda\downarrow0),\qquad
D_L-D_U=\frac{1-2/\pi}{\sqrt{\pi\lambda}}+O(\lambda^{-1})\quad(\lambda\to\infty).
\]

## Assumptions and scope
The parent variables are exactly two independent, identically distributed Poisson counts, with \(\lambda\) any finite positive real number. The ratios are well defined because \(\mathbb EL>0\). No assumption about integer-valued \(\lambda\), asymptotically large \(\lambda\), or a finite collection of tested intensities is made. The conclusion concerns the variance-to-mean ratio and does not assert a variance ordering in the same direction.

For the proof set \(a=e^{-2\lambda}I_0(2\lambda)\), \(b=e^{-2\lambda}I_1(2\lambda)\), and \(c=a+b\). The Bessel functions are normalized by the standard power series
\[
I_0(2\lambda)=\sum_{j=0}^{\infty}\frac{\lambda^{2j}}{(j!)^2},\qquad
I_1(2\lambda)=\sum_{j=0}^{\infty}\frac{\lambda^{2j+1}}{j!(j+1)!}.
\]
All these quantities are strictly positive and \(0<c<1\) when \(\lambda>0\).

## Proof
**1. Moment reduction.** Let \(T=X+Y\) and \(H=X-Y\). The Skellam identity \(\Pr(H=k)=e^{-2\lambda}I_{|k|}(2\lambda)\), together with the Bessel recurrence, gives \(\mathbb E|H|=2\lambda c\) and \(\Pr(H=0)=a\). Since \(U=(T+|H|)/2\) and \(L=(T-|H|)/2\),
\[
\mathbb EU=\lambda(1+c),\qquad \mathbb EL=\lambda(1-c).
\]
Poisson size bias and the integer identity \(|k+1|+|k-1|=2|k|+2\mathbf1_{\{k=0\}}\) imply
\[
\mathbb E[T|H|]=\lambda\mathbb E[|H+1|+|H-1|]=4\lambda^2c+2\lambda a.
\]
Using \(\mathbb ET^2=4\lambda^2+2\lambda\) and \(\mathbb EH^2=2\lambda\), direct expansion of the two squared extrema yields
\[
\operatorname{Var}(L)=\lambda(1-a-\lambda c^2),\qquad
\operatorname{Var}(U)=\lambda(1+a-\lambda c^2).
\]
Consequently,
\[
D_L-D_U=\frac{1-a-\lambda c^2}{1-c}-\frac{1+a-\lambda c^2}{1+c}
=\frac{2(b-\lambda c^3)}{1-c^2}.
\]
It remains to establish \(b>\lambda c^3\).

**2. A strict Laplace-transform bound.** The standard integral formula for \(I_0+I_1\) is
\[
c=\frac4\pi\int_0^{\pi/2}e^{-4\lambda\sin^2 t}\cos^2t\,dt
=\mathbb E[e^{-4\lambda S}],\qquad S\sim\operatorname{Beta}(1/2,3/2).
\]
Take independent \(G\sim\operatorname{Gamma}(1/2,1)\), \(J\sim\operatorname{Gamma}(3/2,1)\), parameterized by shape and unit rate, and write \(S=G/(G+J)\). By beta-gamma independence, \(G+J\) is independent of \(S\) and has mean \(2\). Therefore
\[
\mathbb E[2G\mid S]=4S.
\]
Strict conditional Jensen for \(e^{-\lambda x}\) gives, for every \(\lambda>0\),
\[
\boxed{c=\mathbb E e^{-\lambda\mathbb E(2G\mid S)}
<\mathbb E e^{-2\lambda G}=(1+2\lambda)^{-1/2}.}
\]
Strictness follows because the conditional distribution of \(2G=2S(G+J)\) is nondegenerate for almost every \(S\).

**3. A zero-crossing argument.** Standard modified-Bessel differentiation identities yield
\[
c'=-\frac b\lambda,\qquad
b'=2c-\left(4+\frac1\lambda\right)b.
\]
Set \(F=b-\lambda c^3\). Power-series expansion at the origin gives \(F(\lambda)=\lambda^2+O(\lambda^3)\), so \(F>0\) for sufficiently small positive \(\lambda\). If \(F\) had a first zero \(\lambda_0>0\), differentiating and substituting \(b(\lambda_0)=\lambda_0c(\lambda_0)^3\) would give
\[
F'(\lambda_0)=c(\lambda_0)Q_{\lambda_0}\bigl(c(\lambda_0)^2\bigr),\quad
Q_\lambda(u)=2-(2+4\lambda)u+3\lambda u^2.
\]
The preceding strict Laplace bound gives \(0<c^2<(1+2\lambda)^{-1}\). For \(0\le u\le (1+2\lambda)^{-1}\),
\[
Q_\lambda'(u)=-(2+4\lambda)+6\lambda u<0,
\quad Q_\lambda\bigl((1+2\lambda)^{-1}\bigr)
=\frac{3\lambda}{(1+2\lambda)^2}>0.
\]
Hence \(F'(\lambda_0)>0\), contradicting that a differentiable function positive immediately to the left of its first zero must have nonpositive derivative there. Thus \(F>0\) everywhere on \((0,\infty)\), proving the strict dispersion ordering.

**4. Endpoint rates.** At zero, the defining series give \(b=\lambda-2\lambda^2+O(\lambda^3)\), \(c=1-\lambda+\lambda^2+O(\lambda^3)\), and therefore \(F=\lambda^2+O(\lambda^3)\). At infinity, standard Bessel expansions give \(a\sim(4\pi\lambda)^{-1/2}\), \(b\sim(4\pi\lambda)^{-1/2}\), and \(c\sim(\pi\lambda)^{-1/2}\). Substitution into the exact gap yields the two stated asymptotics, with the displayed remainder following from the next standard Bessel terms. The variance difference follows directly from step 1.

## Verification
Run `python3 verify.py` in the directory containing the supplied standalone script. It uses only the Python standard library. For seventeen intensities from \(0.01\) through \(100\), the script independently constructs the Poisson probability mass function, derives the minimum and maximum distributions from their cumulative distributions, compares the resulting moments to the Bessel/Skellam formulas, and checks the strict inequalities and exact gap. It prints `VERIFIED 17 intensity points` upon success. Symbolic series and Bessel differential identities were separately checked algebraically in deriving the proof. These numerical computations do not establish the theorem for untested real intensities; the analytic steps above do.

## Relationship to prior work
Badiella, del Castillo, and Puig (available online June 26, 2023) prove that discrete order statistics preserve ultra-log-concavity, implying individual Poisson-order-statistic underdispersion. This does not order the two different dispersion indices. The exact moments for two Poisson order statistics were already obtained by Steutel and Thiemann (1989), as reproduced by Lederman and Schein (2025). The latter analyze Poisson order-statistic dispersion and its asymptotic symmetry and display the two-branch curves; their statements do not give a strict all-intensity comparison between minimum and maximum. Their known limiting equality does not imply the present strict finite-intensity ordering. The additional strict cubic Bessel inequality and its beta-gamma proof supply the missing all-parameter sign.

## Limitations
No result is claimed for three or more Poisson observations, nonidentical intensities, other parent distributions, or a stronger stochastic/convex order between the extremes. The variance-to-mean comparison is not a claim that the maximum is less variable in absolute variance. Independent literature-wide priority confirmation remains outstanding. The original 1989 technical report was identified through an institutional record but its full text could not be retrieved during this comparison; its moment formulas were confirmed through the inspectable 2025 primary treatment. Earlier equivalent inequalities for modified Bessel functions remain a residual bibliographic risk.

## References
- L. Badiella, J. del Castillo, and P. Puig (2023), *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters **201**, 109900, DOI:10.1016/j.spl.2023.109900, available online June 26, 2023. OA PDF: https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf.
- J. Lederman and A. Schein (2025), *Modeling Latent Underdispersion with Discrete Order Statistics*, arXiv:2507.09032, especially Section 3, Figure 4 and Proposition 3.1.
- F. W. Steutel and J. G. F. Thiemann (1989), *The gamma process and the Poisson distribution*, Eindhoven University of Technology, COSOR report 89-24. Bibliographic record: https://research.tue.nl/en/publications/the-gamma-process-and-the-poisson-distribution-2.
- NIST Digital Library of Mathematical Functions, Chapter 10, sections 10.29 and 10.40 (modified Bessel recurrences and large-argument asymptotics).
