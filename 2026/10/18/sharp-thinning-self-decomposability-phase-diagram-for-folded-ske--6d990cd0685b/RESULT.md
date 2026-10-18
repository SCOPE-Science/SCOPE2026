# Sharp thinning self-decomposability phase diagram for folded skew discrete Laplace laws

## Finding

The absolute difference of independent geometric counts has an explicitly positive compound-Poisson jump measure for every pair of parameters. Nevertheless, binomial-thinning self-decomposability holds in exactly one sharp parameter region, while ordinary mass-function log-concavity holds only on the symmetry line.

**Theorem.** Let \(0<q,r<1\), let \(X,Y\) be independent nonnegative-integer random variables with \(\Pr(X=j)=(1-q)q^j\) and \(\Pr(Y=j)=(1-r)r^j\) for all integers \(j\ge0\), and let \(W=|X-Y|\). Then:

1. \(W\) is infinitely divisible with respect to convolution on the nonnegative integers for all \((q,r)\). Its compound-Poisson jump intensities are
   \[
   \nu_{2m-1}=\frac{q^{2m-1}+r^{2m-1}}{2m-1},\qquad
   \nu_{2m}=\frac{(q^m-r^m)^2}{2m},\qquad m\ge1.
   \]
2. \(W\) is **discrete self-decomposable under independent Bernoulli thinning** if and only if
   \[
   \boxed{(q-r)^2\ge q^3+r^3.}
   \]
   Equality is included. This is a complete classification over the open unit parameter square, not merely a sufficient criterion.
3. Its probability mass sequence is log-concave if and only if \(q=r\). Consequently the two properties in items 2 and 3 are mutually exclusive in this family. The log-concavity observation on the symmetry line is included as context rather than claimed as an independent novelty result.

## Assumptions and scope

The geometric distributions are **zero-based**, with positive success complements \(1-q\) and \(1-r\). Both shape parameters lie strictly between zero and one. Infinite divisibility is ordinary additive divisibility of probability distributions on \(\mathbb Z_{\ge0}\). The thinning operator \(\alpha\odot Z\), for \(0<\alpha<1\), means a sum of \(Z\) independent \(\operatorname{Bernoulli}(\alpha)\) variables, independent of \(Z\). Discrete self-decomposability means that for every such \(\alpha\) there is a nonnegative-integer random variable \(U_\alpha\), independent of the thinned copy, such that \(W\overset d=\alpha\odot W'+U_\alpha\), where \(W'\overset d=W\). Log-concavity means \(p_k^2\ge p_{k-1}p_{k+1}\) for every integer \(k\ge1\), with \(p_k=\Pr(W=k)\).

## Proof

**1. Folded probability law.** Set \(c=(1-q)(1-r)/(1-qr)>0\). Summing the mutually exclusive events \(X=Y+k\) and \(Y=X+k\) gives, for each integer \(k\ge1\),
\[
\Pr(W=k)=\sum_{j\ge0}(1-q)q^{j+k}(1-r)r^j+\sum_{j\ge0}(1-q)q^j(1-r)r^{j+k}=c(q^k+r^k).
\]
For \(k=0\), only the common diagonal contributes, so \(\Pr(W=0)=c\). Therefore, for \(|z|\le1\), the probability-generating function is
\[
G(z)=c\left(1+\frac{qz}{1-qz}+\frac{rz}{1-rz}\right)=\frac{c(1-qr z^2)}{(1-qz)(1-rz)}.
\]
The expression satisfies \(G(1)=1\), since \(c\) was chosen by normalization.

**2. Positive compound-Poisson representation.** The logarithmic power series is absolutely convergent for \(|z|\le1\), since all three quantities \(q,r,qr\) are strictly less than one. It yields
\[
\log G(z)=\log c+\sum_{k\ge1}\frac{q^k+r^k}{k}z^k-\sum_{m\ge1}\frac{(qr)^m}{m}z^{2m}
             =\log c+\sum_{k\ge1}\nu_k z^k.
\]
For odd \(k=2m-1\), the last series has no contribution. For even \(k=2m\), the coefficient is
\[
\frac{q^{2m}+r^{2m}-2(qr)^m}{2m}=\frac{(q^m-r^m)^2}{2m}\ge0.
\]
All \(\nu_k\) are nonnegative, the odd coefficients are strictly positive, and \(\Lambda=\sum_{k\ge1}\nu_k=-\log c\) lies in \((0,\infty)\) by \(G(1)=1\) and \(0<c<1\). Hence
\[
G(z)=\exp\left\{\sum_{k\ge1}\nu_k(z^k-1)\right\}
\]
is the generating function of a compound-Poisson sum with Poisson rate \(\Lambda\) and jump probabilities \(\nu_k/\Lambda\). This proves infinite divisibility, including at \(q=r\), when the even jump intensities vanish.

**3. Exact self-decomposability boundary.** Bouzar's Proposition 1 (citing Steutel and van Harn) states that a nondegenerate infinitely divisible law on \(\mathbb Z_{\ge0}\) is binomial-thinning self-decomposable precisely when its canonical sequence \(a_k=k\nu_k\), for integers \(k\ge1\), is nonincreasing. The stated characterization applies because \(G(0)=c>0\) and the compound-Poisson form has already been proved.

For every \(m\ge1\),
\[
  a_{2m-1}=q^{2m-1}+r^{2m-1},\qquad a_{2m}=(q^m-r^m)^2.
\]
Since \(0<q,r<1\), \(a_{2m-1}>a_{2m}\) without any restriction. The remaining adjacent inequalities are
\[
(q^m-r^m)^2\ge q^{2m+1}+r^{2m+1},\qquad m\ge1.
\]
By symmetry, assume \(q\ge r\), set \(t=r/q\in(0,1]\), and divide by \(q^{2m}>0\). The family becomes
\[
(1-t^m)^2\ge q(1+t^{2m+1}),\qquad m\ge1.
\]
The left side increases weakly in \(m\), while the right side decreases weakly in \(m\). Thus **the inequality at \(m=1\) is necessary and sufficient for every inequality in the infinite family**. Multiplying the first inequality by \(q^2\) gives exactly \((q-r)^2\ge q^3+r^3\). This also covers \(q=r\), for which the criterion fails. The known canonical-sequence characterization completes the proof of the sharp boundary.

**4. Log-concavity and structural separation.** With \(p_k=\Pr(W=k)\), the boundary comparison is
\[
 p_1^2-p_0p_2=2c^2qr>0.
\]
For each \(k\ge2\), direct cancellation gives
\[
 p_{k-1}p_{k+1}-p_k^2=c^2(qr)^{k-1}(q-r)^2.
\]
Therefore \(p_k^2\ge p_{k-1}p_{k+1}\) holds for all \(k\ge1\) if and only if \(q=r\). This symmetry condition is incompatible with the self-decomposability criterion because \((q-r)^2=0<2q^3\) when \(q=r>0\). All statements follow.

## Verification

The file `check_folded_geometric.py` is a standalone Python standard-library exact-arithmetic checker. Run it from this directory with `python3 check_folded_geometric.py`. It tests normalization with an exact geometric-tail remainder, the canonical logarithmic coefficient recurrence, exact even/odd intensity formulas, the adjacent coefficient transition for many rational parameters, the log-concavity minors, and the folded two-sided geometric summation with explicit tails. It reports `PASS exact rational checks: 3921` upon success. These finitely many computations are checks only; universal quantifiers and the parameter boundary are proved analytically in the preceding section using the monotonicity of two exact expressions.

For illustration, \((q,r)=(9/10,1/100)\) satisfies \((q-r)^2>q^3+r^3\), giving a self-decomposable but non-log-concave folded law. On the symmetry line \(q=r=1/2\), log-concavity holds while discrete self-decomposability does not.

## Relationship to prior work

Kozubowski and Inusah (2006), especially Definition 2.1, Proposition 3.1, and Proposition 4.1, supply the signed skew discrete-Laplace law, its difference-of-geometric construction, and a compound-Poisson representation **on the entire integer line**. Their signed Lévy measure is not the nonnegative jump measure of its folded absolute value; applying absolute value to a compound-Poisson sum does not commute with independent summation. Their mass formula is the natural starting point, not the asserted structural classification.

Bouzar (2008), Proposition 1, supplies the general canonical-sequence criterion for thinning self-decomposability. The present calculation applies that criterion to the *folded* skew model, derives an exact parity-dependent jump measure, and reduces infinitely many inequalities to one sharp cubic parameter boundary. The general criterion itself is not claimed as new.

Karlis and Mamode Khan's 2022 advance review of models on the integers provides the motivating statistical setting of signed count differences and thinning; Pakes (2022) surveys infinite divisibility and discrete self-decomposability. These overviews give general context, not an identified explicit folded-skew phase diagram. A later treatment by Arnold and Arvanitis (2025) studies asymmetric signed discrete-Laplace laws and processes, rather than this fold and its thinning criterion.

In the symmetric case, \(W\) is also the range of two identically distributed geometric observations and its generating function is a Bernoulli–geometric factorization \(c(1+qz)/(1-qz)\). That stronger factorization makes the symmetric log-concavity consequence unsurprising. The log-concavity contrast is presented as a diagnostic consequence, not as a separately novel theorem.

## Limitations

The parameters \(q,r\) must satisfy \(0<q,r<1\); endpoint limit distributions are outside the theorem. Self-decomposability is specifically **binomial-thinning** self-decomposability of the nonnegative folded law, not multiplication-based self-decomposability of the signed random variable. Infinite divisibility does not imply thinning self-decomposability, and self-decomposability does not imply log-concavity here. The analysis does not characterize other forms of decomposability or nongeometric parents. It does not claim absolute uniqueness against unindexed classical treatments, nor independent mathematical certification.

## References

1. D. Karlis and N. Mamode Khan, “Models for Integer Data,” *Annual Review of Statistics and Its Application* **10** (2023), 297–323; first available as Review in Advance 18 November 2022. DOI: `10.1146/annurev-statistics-032921-022516`.
2. T. J. Kozubowski and S. Inusah, “A skew Laplace distribution on integers,” *Annals of the Institute of Statistical Mathematics* **58** (2006), 555–571. DOI: `10.1007/s10463-005-0029-1`.
3. N. Bouzar, “Semi-self-decomposable distributions on \(\mathbb Z_+\),” *Annals of the Institute of Statistical Mathematics* **60** (2008), 901–917, especially Proposition 1. DOI: `10.1007/s10463-007-0124-6`.
4. A. G. Pakes, “Mutant Number Laws and Infinite Divisibility,” *Axioms* **11** (2022), article 584. DOI: `10.3390/axioms11110584`.
5. B. C. Arnold and S. Arvanitis, “On Asymmetric Discrete Laplace Distributions and Processes,” (2025). DOI: `10.1007/s13171-025-00395-9`.
