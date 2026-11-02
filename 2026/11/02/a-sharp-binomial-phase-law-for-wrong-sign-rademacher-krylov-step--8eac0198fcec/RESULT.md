# A sharp binomial phase law for wrong-sign Rademacher Krylov steps

## Finding
Fix integers \(k\ge1\), real \(a>0\) and \(\kappa\ge1\), and the two-mode SPD system \(A=\operatorname{diag}(a,\kappa a)\). Let \(b\ne0\). With an independent symmetric sign sketch \(S\in\{-1,+1\}^{k\times2}\), the one-dimensional sketched minimal-residual coefficient is the minimum-magnitude minimizer of \(\|S(b-tAb)\|_2\). Put
\[\chi_\kappa=\frac{2\sqrt\kappa}{1+\kappa}.\]
Then the following is the *exact attained worst-case probability* over initial residual directions:
\[
\boxed{\sup_{b\ne0}\Pr(t_S<0)=\frac1{2^k}\sum_{j=0}^{k}\binom{k}{j}\mathbf1\!\left\{\frac{2j-k}{k}<-\chi_\kappa\right\}.}
\]
For \(\kappa>1\), the extremizer is \(b=(\sqrt\kappa,1)^\mathsf T\), up to nonzero scale, and a sign change of one component also attains the same probability. For \(\kappa=1\), the probability is zero. For \(\kappa>1\), the maximal probability is at least \(2^{-k}\), no matter how near \(\kappa\) is to one. It is a binomial staircase in \(\kappa\) whose jumps occur when \(\chi_\kappa\) passes a positive value \((k-2j)/k\); at equality the corresponding binomial term is excluded.

At \(k=3\) the first nontrivial jump has a fully explicit threshold:
\[
\sup_{b\ne0}\Pr(t_S<0)=
\begin{cases}
0,&\kappa=1,\\
1/8,&1<\kappa\le (3+2\sqrt2)^2,\\
1/2,&\kappa>(3+2\sqrt2)^2.
\end{cases}
\]
A negative coefficient has an immediate operational interpretation: since \(b^\mathsf TAb>0\), the actual residual \(b-t_SAb\) has strictly greater Euclidean norm than \(b\).

## Assumptions and scope
All arithmetic is exact; all sketch entries are mutually independent fair signs. The first iterate belongs to the initial Krylov space \(\operatorname{span}\{b\}\); the minimal-norm convention assigns \(t_S=0\) when \(SAb=0\). The probability is for the sketch alone, with \(A\) and \(b\) fixed beforehand. The maximization is over all nonzero real two-component initial residuals for fixed \(A\). Scale \(1/\sqrt{k}\) on every sketch entry does not change the coefficient. The same law holds for a larger diagonal SPD matrix when only two diagonal modes of ratios \(\kappa\) are excited; unused sign-sketch columns are irrelevant.

## Proof
Write \(b=(x,y)^\mathsf T\), and for the \(i\)-th sketch row let \(\epsilon_i=S_{i1}S_{i2}\). These are independent uniform signs. Define \(B=\sum_{i=1}^k\epsilon_i\). The normal equations give
\[
t_S=\frac{(Sb)^\mathsf T(SAb)}{\|SAb\|_2^2}
=\frac{k(a x^2+\kappa a y^2)+a(1+\kappa)Bxy}{\|SAb\|_2^2}
\]
when the denominator is nonzero. If the denominator vanishes then the numerator vanishes as well and the coefficient convention gives zero, so the sign criterion is unchanged. For \(xy=0\) the coefficient is nonnegative. Otherwise, negativity requires \(Bxy<0\) and
\[
\left|\frac Bk\right|>
\frac{x^2+\kappa y^2}{(1+\kappa)|xy|}
\ge\frac{2\sqrt\kappa}{1+\kappa}=\chi_\kappa.
\]
The inequality is arithmetic–geometric mean, with equality precisely for \(|x/y|=\sqrt\kappa\). By symmetry of \(B\), any fixed residual direction therefore has negative-coefficient probability at most the stated one-sided binomial tail; taking \(x=\sqrt\kappa\), \(y=1\) attains this bound for *every* sketch outcome at once. Since \(B=2J-k\) for \(J\sim\operatorname{Bin}(k,1/2)\), this proves the formula including the strict endpoints.

For \(\kappa=1\), the numerator is \(\|Sb\|_2^2\ge0\); thus the probability vanishes. For \(\kappa>1\), \(\chi_\kappa<1\), so the event \(B=-k\) enters the binomial sum and has probability \(2^{-k}\). For \(k=3\), the negative values of \(B\) are \(-3\) and \(-1\), with respective probabilities \(1/8\) and \(3/8\). The second enters exactly when \(\chi_\kappa<1/3\), equivalent to \(\kappa>(3+2\sqrt2)^2\).

Finally, on \(B=-k\), all sign rows probe \(x-y\). At \(b=(\sqrt\kappa,1)^\mathsf T\), the minimizer is
\[
t_S=\frac{\sqrt\kappa-1}{a(\sqrt\kappa-\kappa)}=-\frac1{a\sqrt\kappa}.
\]
Consequently \(b-t_SAb=(1+\sqrt\kappa)(1,1)^\mathsf T\), so
\[\frac{\|b-t_SAb\|_2^2}{\|b\|_2^2}=\frac{2(1+\sqrt\kappa)^2}{1+\kappa}\longrightarrow4\quad(\kappa\downarrow1).\]
For every negative coefficient, \(\|b-t_SAb\|_2^2=\|b\|_2^2-2t_Sb^\mathsf TAb+t_S^2\|Ab\|_2^2>\|b\|_2^2\). This proves the residual claim. In higher-dimensional diagonal systems with initial residual supported on these two coordinate axes, all projected quantities involve only the same two sign columns, proving the embedding statement.

## Verification
Run `python verify.py` with Python 3 and no extra packages. It enumerates all row-product-sign sequences for \(1\le k\le8\), compares 352 exact rational cases against the sharp binomial probability, verifies the strict \(k=3\) phase boundary and the nonvanishing floor at 16 sketch dimensions. The exact algebra above proves the theorem for all integer \(k\) and all real \(\kappa\); finite tests do not prove the universal quantifiers.

## Relationship to prior work
Yuan and Wu's October 26, 2026 preprint [1] studies randomized Krylov methods for shifted systems and explicitly includes Rademacher sketches among standard oblivious embeddings, with sketched minimal-residual objective in its Section 2.2. Güttel and Pearson [2], and Nakatsukasa and Tropp [3], provide algorithms and embedding/error frameworks rather than this exact one-step wrong-sign probability. Prior Gaussian sketch-and-solve results, including [4], analyze continuous Gaussian ensembles; their distributional results do not yield the discrete binomial staircase for independent sign sketches. The contribution claimed here is the sharp two-mode finite-sketch failure probability and its near-identity discontinuity, not the generic normal-equation formula or the elementary binomial distribution.

## Limitations
The event classified is a negative coefficient, which is sufficient but not necessary for actual residual amplification; the theorem **does not** give the probability of every possible residual increase. The two-mode diagonal alignment and exact sign ensemble are essential; neither arbitrary SPD orientations nor other sketch laws are covered. Sketches with deficient action on the relevant vector are handled by an explicit coefficient convention. Numerical floating-point effects, restarted multi-step methods, and conditional acceptance of only certified subspace embeddings are not addressed. Historical priority has not been exhaustively established, and there is no independent mathematical audit.

## References
[1] X. Yuan and G. Wu, *Randomized Krylov Subspace Methods for Shifted Linear Systems*, arXiv:2610.34964v1, publicly submitted 2026-10-26. https://arxiv.org/html/2610.34964v1

[2] S. Güttel and J. W. Pearson, *Stabilizing randomized GMRES through flexible GMRES*, arXiv:2506.18408v2. https://arxiv.org/html/2506.18408v2

[3] Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113. https://arxiv.org/abs/2111.00113

[4] E. N. W. Epperly, *Note to Self: Sketch-and-Solve with a Gaussian Embedding*, 2024-11-19. https://www.ethanepperly.com/index.php/2024/11/19/note-to-self-sketch-and-solve-with-a-gaussian-embedding/
