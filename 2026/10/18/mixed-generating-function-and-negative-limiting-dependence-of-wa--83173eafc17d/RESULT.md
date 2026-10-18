# Mixed generating function and negative limiting dependence of walk maxima and zero-return counts

## Finding

For independent symmetric steps taking values \(-1\) and \(+1\) with probability \(1/2\), put \(S_0=0\), \(S_j=\sum_{i=1}^{j}X_i\), and, for every integer \(n\ge0\), define
\[
 M_n=\max_{0\le j\le n}S_j,\qquad L_n=\sum_{j=1}^{n}\mathbf{1}_{\{S_j=0\}}.
\]
In particular, \(L_n\) counts returns after time zero, not the starting visit. Define, for \(|z|<1\),
\[
 u(z)=(1-z^2)^{-1/2},\qquad
 r(z)=\frac{1-\sqrt{1-z^2}}{z},\quad r(0)=0.
\]
The exact mixed-moment generating function is
\[
\boxed{\sum_{n=0}^{\infty}\mathbb E[M_nL_n]z^n
=\frac{1}{1-z}\left\{u(z)\left[
\frac{r(z)}{1-r(z)}+\frac{r(z)^2}{1-r(z)^2}-\frac{r(z)^3}{1-r(z)^3}
\right]-\frac{r(z)}{1-r(z)}\right\}.}
\tag{1}
\]
Consequently, the covariance and Pearson correlation have the limits
\[
\boxed{\lim_{n\to\infty}\frac{\operatorname{Cov}(M_n,L_n)}n
=\frac7{12}-\frac2\pi<0,}\qquad
\boxed{\lim_{n\to\infty}\operatorname{Corr}(M_n,L_n)
=\frac{\frac7{12}-\frac2\pi}{1-\frac2\pi}<0.}
\tag{2}
\]
Thus an increasingly large random-walk maximum and the number of returns to the origin have a strictly negative *limiting* normalized dependence, with an exact finite-time mixed-moment transform. This assertion does not require, and does not prove, a negative covariance for every finite \(n\).

## Assumptions and scope

Steps are independent and equiprobable \(\pm1\), time is discrete, the walk starts at zero, and the maximum includes time zero. Each \(L_n\) omits time zero. Formula (1) holds as an analytic identity on \(|z|<1\), interpreted through its power series near the origin. Formulas (2) concern \(n\to\infty\) over all integers, with both parities included. No claim is made for biased or non-nearest-neighbor walks, or for simultaneous nonzero spatial local times.

## Proof

Write \(\tau_a=\inf\{j\ge0:S_j=a\}\) for an integer level \(a\ge1\). The first-passage generating function and the return Green function are
\[
\mathbb E[z^{\tau_a}]=r(z)^a,\qquad
\sum_{j\ge0}z^j\Pr(S_j=k)=u(z)r(z)^{|k|}.
\tag{3}
\]
The first equality follows from the nearest-neighbor first-step recurrence, taking the solution with modulus below one; the second follows from the resolvent difference equation, with the boundary value \(u(z)=(1-z^2)^{-1/2}\). Both hold for \(0<z<1\), sufficient for coefficient identities and limits.

By reflection of paths up to their first visit to \(a\),
\[
\Pr(S_j=0,M_j\ge a)=\Pr(S_j=2a).
\]
It follows from (3), remembering that \(j=0\) must be excluded from the local-time count, that
\[
\sum_{j\ge1}z^j\Pr(S_j=0,M_j\ge a)=u(z)r(z)^{2a},
\quad
\sum_{j\ge1}z^j\Pr(S_j=0,M_j<a)=u(z)(1-r(z)^{2a})-1.
\tag{4}
\]
At any return time \(j\), the event \(M_n\ge a\) has already occurred if \(M_j\ge a\). Otherwise, conditional on \(S_j=0\) and \(M_j<a\), it occurs after \(j\) exactly when an independent future walk first hits \(a\) before \(n-j\). Summing (4) over \(j\) and remaining times therefore gives
\[
\sum_{n\ge0}z^n\mathbb E[L_n\mathbf{1}_{\{M_n\ge a\}}]
=\frac{u(z)r(z)^{2a}+[u(z)(1-r(z)^{2a})-1]r(z)^a}{1-z}.
\tag{5}
\]
Since \(M_n=\sum_{a\ge1}\mathbf{1}_{\{M_n\ge a\}}\), summing (5) for all \(a\ge1\) yields
\[
\frac{1}{1-z}\left\{u(z)\sum_{a\ge1}\left(r(z)^a+r(z)^{2a}-r(z)^{3a}\right)-\sum_{a\ge1}r(z)^a\right\},
\]
which sums geometrically to (1). All sums are nonnegative before the algebraic rearrangement for \(0<z<1\), so the interchanges are justified.

As \(z\uparrow1\), set \(\varepsilon=1-z\). Then
\[
 u(z)\sim(2\varepsilon)^{-1/2},\qquad
 1-r(z)\sim\sqrt{2\varepsilon},\qquad
 \frac{r(z)^k}{1-r(z)^k}\sim\frac{1}{k\sqrt{2\varepsilon}}
\]
for fixed \(k=1,2,3\). The coefficients \(1+1/2-1/3=7/6\) imply
\[
\sum_{n\ge0}z^n\mathbb E[M_nL_n]\sim\frac7{12}(1-z)^{-2}.
\]
The sequence \(\mathbb E[M_nL_n]\) is nonnegative and nondecreasing because both factors are pathwise nondecreasing. A monotone-density Tauberian theorem therefore yields
\[
\lim_{n\to\infty}\frac{\mathbb E[M_nL_n]}n=\frac7{12}.
\tag{6}
\]
(Equivalently, singularity analysis can treat the branch singularities at \(z=\pm1\) directly.)

The return probabilities are \(p_{2j}=\binom{2j}{j}/4^j\) and \(p_{2j+1}=0\). Hence
\[
\mathbb E[L_n]=\sum_{j=1}^{n}p_j\sim\sqrt{\frac{2n}{\pi}}.
\tag{7}
\]
By the reflection principle or Donsker's theorem with Doob's maximal \(L^4\) inequality,
\[
\frac{\mathbb E[M_n]}{\sqrt n}\longrightarrow\sqrt{\frac2\pi},\qquad
\frac{\operatorname{Var}(M_n)}{n}\longrightarrow1-\frac2\pi.
\tag{8}
\]
For the return count, the Markov property at two distinct return times gives the exact second-moment transform
\[
\sum_{n\ge0}\mathbb E[L_n^2]z^n
=\frac{(u(z)-1)(2u(z)-1)}{1-z}.
\tag{9}
\]
Its leading singular behavior is \((1-z)^{-2}\), and \(\mathbb E[L_n^2]\) is nondecreasing. Therefore
\[
\frac{\mathbb E[L_n^2]}n\longrightarrow1,\qquad
\frac{\operatorname{Var}(L_n)}n\longrightarrow1-\frac2\pi.
\tag{10}
\]
Combining (6)--(8) proves the covariance limit in (2); (8) and (10) then give its correlation limit. Since \(7/12<2/\pi\), both constants are strictly negative.

## Verification

The standalone file `verify.py` implements two genuinely separate exact-rational procedures. One expands (1), the first-moment return Green function, and (9) through degree 16 using binomial/Catalan coefficients and truncated rational-series products. The other exhaustively propagates weighted states \((S_n,M_n,L_n)\) under the two equiprobable transitions, calculating the three moments independently from the walk definition. Executing `python verify.py` prints matching rational values for selected indices and checks **every** coefficient from \(n=0\) through \(n=16\). These finite checks do not prove the infinite identities; the analytic proof above does.

## Relationship to prior work

The classical reflection principle, random-walk Green functions, and first-passage transforms are known; these ingredients are not claimed as discoveries. Kirschenhofer and Prodinger (1996), a particularly close primary source, develop generating functions for the return count and separately for the *number of visits to the path maximum*, including conditioned bridges. Its Sections 2 and 3 give marginal moment transforms of those counts rather than the mixed moment between the *maximum height* and zero-return count in an unconditioned walk. Pitman's 1998 discussion of Lévy identities and bridge local times identifies important distributional correspondences, but those correspondences concern transformed processes or conditional bridges, not the simultaneous same-walk maximum–zero-return product of (1). Denisov and Wachtel (2014) address local times of killed and reflected walks and local-time fields, not this mixed statistic. Csáki, Földes and Salminen (1987) study the maximum, its location and a spatial maximum of a Brownian local-time process, rather than the fixed-origin local time jointly with the running maximum of one walk.

A published finite-path symmetry result gives a half-variance covariance between the running maximum and the *endpoint* and includes an odd-endpoint-transform family. That does not cover (1), since the accumulated return count is neither the endpoint nor its odd transform. Exact complete joint transforms for a maximum and a local-time statistic, if present in other literature, could imply the result even without the displayed form; the novelty assertion is limited by this residual risk.

## Limitations

The exact ordinary generating function has been proved only for the symmetric nearest-neighbor walk with the specified return-count normalization. The covariance result is an asymptotic statement, not a classification of every finite-time sign. The argument does not provide a full bivariate joint law or prove independence of either statistic. Existing general path-functionals or excursion-theoretic transforms may subsume its special case without matching the same wording; no universal novelty guarantee is asserted. Independent validation has not been performed.

## References

1. Jim Pitman, “The distribution of local times of a Brownian bridge,” University of California, Berkeley Statistics Technical Report 539, publicly dated November 1, 1998: https://live-statistics.pantheon.berkeley.edu/tech-reports/539 .
2. Denis Denisov and Vitali Wachtel, “Universality of local times of killed and reflected random walks,” arXiv:1412.6184v1, submitted December 18, 2014: https://arxiv.org/abs/1412.6184 .
3. Endre Csáki, Antónia Földes and Paavo Salminen, “On the joint distribution of the maximum and its location for a linear diffusion,” Annales de l'I.H.P., Probabilités et statistiques 23 (1987), 179–194: https://www.numdam.org/article/AIHPB_1987__23_2_179_0.pdf .
4. Peter Kirschenhofer and Helmut Prodinger, “Return statistics of simple random walks,” Journal of Statistical Planning and Inference 54 (1996), 67–74, https://www.math.tugraz.at/~prodinger/inference.pdf .
5. “Reversal and sign symmetry force a half-variance maximum–endpoint law,” published result, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-reversal-and-sign-symmetry-force-a-half-variance-maximum-endpoin--5e8da51794ea/RESULT.md .
