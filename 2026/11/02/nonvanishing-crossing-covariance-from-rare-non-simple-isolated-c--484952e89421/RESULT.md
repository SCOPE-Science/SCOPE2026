# Nonvanishing crossing covariance from rare non-simple isolated chords

## Finding

A uniform chord diagram on \(2n\) labeled points is a uniformly chosen perfect matching of cyclically ordered points. Its **intersection graph** has one vertex per chord and one edge per crossing. Let \(C_n\) be its number of crossings. An **isolated chord** crosses no other chord. Write \(U_{n,s}\) for the number of isolated chords whose *shorter* open circular arc contains exactly \(2s\) other endpoints, where \(n\ge2\) and \(0\le s\le\lfloor(n-1)/2\rfloor\).

Every admissible stratum has strictly negative covariance:
\[
\boxed{\operatorname{Cov}(U_{n,s},C_n)=-\frac{(n-1)+s(n-1-s)}{3}\,\mathbb E U_{n,s}},
\]
with the exact mean
\[
\mathbb E U_{n,s} =M_{n,s}\frac{(2s-1)!!\,[2(n-1-s)-1]!!}{(2n-1)!!},\qquad
M_{n,s}=\begin{cases}2n,&2s<n-1,\\n,&2s=n-1.\end{cases}
\]
Here \((-1)!!=1\). The equality case in the definition of \(M_{n,s}\) corresponds to the antipodal short-arc tie.

The genuinely non-simple stratum \(s=1\) obeys, for every \(n\ge4\),
\[
\boxed{\mathbb E U_{n,1}=\frac{2n}{(2n-1)(2n-3)},\qquad
\operatorname{Cov}(U_{n,1},C_n)=-\frac{2n}{3(2n-1)}\longrightarrow-\frac13.}
\]
Let \(R_n=\sum_{s=1}^{\lfloor(n-1)/2\rfloor}U_{n,s}\), the total number of isolated chords that are **not** simple (whose endpoints are nonconsecutive). Then
\[
\boxed{\mathbb E R_n=\frac1{2n}+O(n^{-2}),\qquad
\operatorname{Cov}(R_n,C_n)=-\frac13+O(n^{-1}).}
\]
Thus \(R_n\to0\) in probability, yet its unscaled covariance with the number of crossings does not tend to zero. This is a rare-event covariance effect, not a contradiction: the crossing deficit conditional on an isolated non-simple chord grows with \(n\). The \(s=0\) simple-chord case is included in the general identity for comparison, **not asserted to be new**.

## Assumptions and scope

The endpoint labels are fixed, and every one of the \((2n-1)!!\) perfect matchings has equal probability. Crossings involve pairs of distinct chords with alternating endpoints on the circle. An isolated chord is a degree-zero vertex of the intersection graph; in particular, it is not merely a chord with small circular arc span. All covariances are ordinary, unnormalized covariances. The range is \(n\ge2\) and \(0\le s\le\lfloor(n-1)/2\rfloor\); for \(R_n\), empty sums are zero.

## Proof

**1. Crossing mean.** For each four-element subset of endpoints, there is exactly one way of pairing its four members to create a crossing. Any specified two disjoint chords occur in a uniform perfect matching with probability \(1/[(2n-1)(2n-3)]\). Linearity of expectation consequently gives
\[
\mathbb E C_n=\frac{\binom{2n}{4}}{(2n-1)(2n-3)}=\frac{n(n-1)}6.
\]

**2. Conditioning on an isolated chord.** Fix a candidate chord \(e\) whose shorter open arc contains \(2s\) endpoints and whose other arc contains \(2(n-1-s)\). The event \(A_e\) that \(e\) is present and isolated is *exactly* the event that its two groups of remaining endpoints are each paired internally. Therefore
\[
\mathbb P(A_e)=\frac{(2s-1)!!\,[2(n-1-s)-1]!!}{(2n-1)!!}.
\]
Given \(A_e\), the two induced internal matchings are independent and uniform. Chords from opposite arcs cannot cross one another, and no chord crosses \(e\). With the convention that an empty group contributes zero crossings,
\[
\mathbb E(C_n\mid A_e)=\frac{s(s-1)+(n-1-s)(n-2-s)}6.
\]
Subtracting the unconditional mean, with \(m=n-1\), gives the exact conditional deficit
\[
\mathbb E(C_n\mid A_e)-\mathbb E C_n
=-\frac{m+s(m-s)}3.
\]
Each admissible shorter-arc geometry has \(2n\) different candidate chords unless its two arcs contain equally many endpoints, in which case each candidate is double-counted under clockwise versus counterclockwise enumeration and there are \(n\) chords. Thus the number \(M_{n,s}\) above is exact.

Now write \(U_{n,s}=\sum_{e\in\mathcal E_{n,s}}\mathbf1_{A_e}\). For every candidate \(e\),
\[
\operatorname{Cov}(\mathbf1_{A_e},C_n)
=\mathbb P(A_e)\{\mathbb E(C_n\mid A_e)-\mathbb E C_n\}.
\]
Summation proves both the exact mean and covariance. All factors outside the leading minus sign are strictly positive on the stated range, so each stratum has strictly negative covariance.

**3. Non-simple shortest stratum.** For \(n\ge4\) the class \(s=1\) is not antipodal, so its \(2n\) candidates have probability \((2n-5)!!/(2n-1)!!\). Substituting gives the displayed exact mean and covariance. The \(n=3\) antipodal case is already covered by the full formula (and is not used in this large-\(n\) limit).

**4. Control of all larger non-simple strata.** Set \(m=n-1\) and
\[
 r_{m,s}=\frac{\binom m s}{\binom{2m}{2s}},\qquad 0\le s\le\lfloor m/2\rfloor.
\]
The chord probability in step 2 is \(r_{m,s}/(2n-1)\). Direct cancellation shows
\[
 r_{m,1}=\frac1{2m-1},\quad
 r_{m,2}=\frac3{(2m-1)(2m-3)},\quad
\frac{r_{m,s+1}}{r_{m,s}}=\frac{2s+1}{2(m-s)-1}.
\]
Consequently \(r_{m,s}\) decreases for \(s\le\lfloor m/2\rfloor\), and for all sufficiently large \(m\), the ratios are at most \(1/2\) for \(2\le s<\lfloor m/4\rfloor\). For these \(s\),
\[
\sum_{s=2}^{\lfloor m/4\rfloor}
\big(m+s(m-s)\big)r_{m,s}
\le m r_{m,2}\sum_{j\ge0}(j+3)2^{-j}=O(m^{-1}).
\]
For \(s>\lfloor m/4\rfloor\), monotonicity and the preceding geometric decrease imply \(r_{m,s}\le r_{m,2}\,2^{-\lfloor m/4\rfloor+O(1)}\). At most \(m\) such terms occur, each with coefficient \(m+s(m-s)=O(m^2)\); their combined contribution is exponentially small times a polynomial and therefore \(O(m^{-1})\). The same argument without the coefficient yields
\[
\sum_{s=2}^{\lfloor m/2\rfloor}r_{m,s}=O(m^{-2}).
\]
The mean factor \(M_{n,s}/(2n-1)\) stays bounded above by \(2n/(2n-1)\), including the antipodal tie. It follows from the exact formulas that
\[
\sum_{s=2}^{\lfloor m/2\rfloor}\mathbb E U_{n,s}=O(n^{-2}),\qquad
\sum_{s=2}^{\lfloor m/2\rfloor}\operatorname{Cov}(U_{n,s},C_n)=O(n^{-1}).
\]
Adding the exact \(s=1\) formulas proves both asymptotic assertions for \(R_n\). Finally, Markov's inequality gives \(\mathbb P(R_n>0)\le\mathbb E R_n\to0\).

## Verification

The standalone `verify.py` uses exact fractions and independently enumerates every perfect matching on \(2n\) endpoints for \(2\le n\le7\) (\(146{,}598\) matchings in total). It counts crossings from endpoint alternation and isolated chords from their crossing degrees, not from the conditional formula. It matches empirical exact-rational means/covariances to every admissible stratum; additionally it checks normalization and the special formulas through \(n=150\). There were \(6{,}194\) assertions passed. These finite tests do **not** prove the infinite assertion, which follows from the four analytic steps above.

Reproduction: run `python verify.py` using the Python standard library, without network access.

## Relationship to prior work

Paguyo's 2021 work establishes quantitative limit theorems for the **marginal** crossing count and number of simple chords and discusses fixed-length chord counts, without asserting the above covariances for **non-simple isolated** chords. Acan's 2015 preprint studies the degree sequence of the random circle-intersection graph and its asymptotic isolated vertices. Flajolet and Noy's 2000 work separately gives the classical Gaussian crossing law and Poisson-type component behavior (its accessible full INRIA report was inspected). The \(s=0\) case of the displayed covariance identity is already covered by separate exact simple-chord/crossing calculations and is therefore only background here. The asserted contribution is the *isolation-conditioned positive-gap stratification* and especially the nonvanishing \(-1/3\) limit for a count vanishing in probability. No claim is made that generic chord-matching moment techniques are new.

## Limitations

The result assumes uniformly sampled matchings, not weighted matchings or conditioned diagrams. It concerns ordinary covariance, not independence, conditional independence, or scaled Pearson correlation. Published works with multivariate chord statistics could contain an equivalent calculation implicitly; historical priority remains subject to further independent checking. The simple-chord case is not a novel finding. The verification code is finite and not a formal proof; no independent audit has been performed.

## References

1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, first posted 2021-04-02, https://arxiv.org/abs/2104.01134 .
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, https://arxiv.org/abs/1501.01489 .
3. P. Flajolet and M. Noy, *Analytic combinatorics of chord diagrams*, Formal Power Series and Algebraic Combinatorics, 2000; open full report https://algo.inria.fr/flajolet/Publications/FlNo00.pdf .
