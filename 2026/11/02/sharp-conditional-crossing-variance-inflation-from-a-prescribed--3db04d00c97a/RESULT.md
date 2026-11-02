# Sharp conditional crossing-variance inflation from a prescribed chord

## Finding

For a uniformly random pairing of the \(2n\) cyclically ordered endpoints of a chord diagram, \(n\ge3\), let \(C\) be the number of unordered crossing pairs of chords. Fix an endpoint pair \(e\), and suppose its two complementary arcs contain \(a\) and \(b=2n-2-a\) other endpoints. Condition on \(e\) being a chord. Then

\[
\boxed{\operatorname{Var}(C\mid e\text{ present})=
\frac{(n-1)(n-2)(n+2)}{45}
+\frac{(2n+3)ab(a-1)(b-1)}{3(2n-5)(2n-3)^2}.}
\]

The second term is the **exact variance inflation relative to an independent uniform diagram with \(n-1\) chords**. It is nonnegative; it vanishes exactly if \(\min(a,b)\le1\), and is positive if \(a,b\ge2\). For fixed \(n\), it is symmetric in the arc sizes, grows strictly as the smaller arc size rises from \(1\) to \(n-1\), and is uniquely maximized when \(a=b=n-1\). At this maximum it is asymptotic to \(n^2/12\).

The structural identity behind the inflation is also exact. Write \(X\) for the number of crossings among the remaining \(n-1\) random chords, and \(Y\) for the number crossing the prescribed chord. Conditional on the prescribed chord,

\[
\boxed{\operatorname{Cov}(X,Y)=\frac{ab(a-1)(b-1)}{6(2n-5)(2n-3)}\ge0.}
\]

Thus the extra variability comes both from the randomness of the prescribed chord's degree and from a nonnegative *mixed covariance* with the crossings elsewhere. The associated first moment, included for context rather than claimed as a separate new contribution, is

\[
\mathbb E[C\mid e\text{ present}]=\frac{(n-1)(n-2)}6+\frac{ab}{2n-3}.
\]

## Assumptions and scope

Place \(2n\) distinct, labeled points in fixed cyclic order. Select uniformly from all \((2n-1)!!\) perfect matchings of these points, drawing each matched pair as a chord. Intersections are determined solely by alternating endpoints, not by sampling random Euclidean lines or random interior points. A prescribed endpoint pair occurs with probability \(1/(2n-1)\); conditioning on this event makes the pairing of the other \(M=2n-2\) points uniform. Here \(0\le a\le M\), \(b=M-a\), and \(n\ge3\) so that \(M\ge4\). The assertion covers every endpoint pair, including adjacent and opposite pairs.

## Proof

**1. Pairing probabilities and the chord's crossing count.** Conditional on \(e\), let \(A,B\) be its two arc sets of sizes \(a,b\). Let \(I_{uv}\) be the indicator that \(u\in A\) is matched to \(v\in B\). Then \(Y=\sum_{u\in A,v\in B}I_{uv}\). A specified pair is present with probability \(1/(M-1)\); two disjoint specified pairs are present with probability \(1/((M-1)(M-3))\). Hence

\[
\begin{aligned}
\mathbb EY&=\frac{ab}{M-1},\\
\mathbb E[Y(Y-1)]&=\frac{a(a-1)b(b-1)}{(M-1)(M-3)},\\
\operatorname{Var}(Y)&=\frac{2ab(a-1)(b-1)}{(M-3)(M-1)^2}.
\end{aligned}
\]

**2. Mixed covariance.** Regard the remaining \(M\) positions as \(1,\ldots,M\), with \(A=\{1,\ldots,a\}\) and \(B=\{a+1,\ldots,M\}\). The crossing count \(X\) of their uniform matching has expectation \(M(M-2)/24\), by summing over the \(\binom M4\) ordered quadruples and noting that a crossing on a particular quadruple has probability \(1/((M-1)(M-3))\).

For \(u\in A\), \(v\in B\), put \(t=v-u-1\). If \(uv\) is present, the remaining \(M-2\) endpoints are still uniformly paired; their internal crossing expectation is \((M-2)(M-4)/24\). The chord \(uv\) has \(t\) endpoints on one side and \(M-2-t\) on the other, so its expected number of crossings is \(t(M-2-t)/(M-3)\). Therefore

\[
\operatorname{Cov}(X,I_{uv})=
\frac{1}{M-1}\left(\frac{t(M-2-t)}{M-3}-\frac{M-2}{6}\right).
\]

The finite double sum evaluates by the standard first and second power sums:

\[
\sum_{u=1}^{a}\sum_{v=a+1}^{M}(v-u-1)(M-1-v+u)
=\frac{ab(M^2+ab-6M+7)}6.
\]

Summing the individual covariances and simplifying gives

\[
\operatorname{Cov}(X,Y)=\frac{ab(a-1)(b-1)}{6(M-3)(M-1)}.
\]

**3. Total conditional variance.** The cyclic order of the remaining endpoints is inherited from the original diagram, so \(X\) is the ordinary crossing count for a uniform diagram with \(n-1\) chords. The classical variance identity is

\[
\operatorname{Var}(X)=\frac{(n-1)(n-2)(n+2)}{45}.
\]

This baseline can also be checked without a generating function: when a uniform \(m\)-chord diagram is exposed by the chord incident to the first point, its partner produces an arc gap uniformly distributed over \(0,\ldots,2m-2\). Applying the two formulas above to the remaining \(2m-2\) endpoints, then using total variance and finite power sums, yields, for \(m\ge3\),

\[
\operatorname{Var}(C_m)-\operatorname{Var}(C_{m-1})
=\frac{(m-1)(3m+4)}{45}.
\]

The initial cases have variances \(0\) for \(m=1\) and \(2/9\) for \(m=2\) (one crossing with probability \(1/3\)); telescoping gives \(m(m-1)(m+3)/45\). To see the finite-sum step explicitly, with \(M=2m-2\) and a uniform arc gap \(a\), the mean conditional increment is \(ab/(M-1)\), and the average conditional variance increment and variance of this mean are respectively

\[
\frac{M(M-2)(M+5)}{90(M-1)},\qquad
\frac{M(M+2)(M+3)}{180(M-1)}.
\]

Finally \(C=X+Y\); combining \(\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)\) gives

\[
\operatorname{Var}(C\mid e\text{ present})-\operatorname{Var}(X)
=\frac{ab(a-1)(b-1)(M+5)}{3(M-3)(M-1)^2},
\]

which is the claimed formula after \(M=2n-2\).

**4. Sharpness and shape.** The factor \(ab(a-1)(b-1)\) is zero exactly for \(\min(a,b)\le1\); otherwise it is positive. At fixed even \(M\), the product is symmetric under \(a\leftrightarrow M-a\). For \(2\le a<M/2\), its ratio on increasing \(a\) by one is \((a+1)(b-2)/((a-1)b)>1\), because \(b>a+1\). The case \(a=1\) is a strict increase to \(a=2\); the step from \(a=0\) to \(a=1\) is an equality at zero. The unique maximal integer value is thus at \(a=b=M/2=n-1\). Substitution gives \(n^2/12+O(n)\) for the variance increment.

## Verification

The standalone `verify.py` uses only the Python standard library. It exhaustively enumerates uniform perfect matchings conditioned on every possible arc gap for \(3\le n\le7\), and also enumerates unconditional diagrams of sizes \(1\le m\le7\). Using exact rational arithmetic, it compares the two moments, the mixed covariance, and the chord-crossing variance against the formulas. Its recorded run passed 194 assertions across 293,194 enumerated matching instances. The enumeration is a finite check, **not** the proof for all \(n\); the argument above supplies the infinite family.

## Relationship to prior work

Flajolet and Noy (2000, Theorem 3, section 2) give exact mean and variance formulas for the *unconditioned* total crossing count. Acan (2015, section 2) computes first and second moments of the crossing degree of a distinguished chord, conditional on chord length. Thus the first-moment formula for \(C\) is already obtainable by combining known elementary components and is not treated as novel here. Neither inspected calculation determines the mixed covariance between crossings of remaining chords and the distinguished chord's degree, which is required for the conditional *total* crossing variance. Pilaud and Rué (2013) treat generating functions for configurations with a fixed crossing count, rather than the fixed-edge conditional variance under uniform unrestricted matchings; only its available abstract was inspected, so an indirect specialization remains possible. The precise historical priority of the conditional variance formula is not established by these comparisons.

## Limitations

The result concerns a uniform perfect matching of fixed cyclic endpoints and conditioning on one prescribed chord; it makes no assertion for nonuniform matching weights, independently generated continuous geometric chords, multiple forced chords, or the conditional **full distribution** of crossing counts. A full historical novelty determination would require further targeted study of refined crossing enumerators. No independent audit or external certification of the formulas has been performed.

## References

1. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA research report RR-3914, dated March 4, 2000, section 2, Theorem 3. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first posted January 7, 2015, section 2. https://arxiv.org/abs/1501.01489
3. V. Pilaud and J. Rué, *Analytic combinatorics of chord and hyperchord diagrams with \(k\) crossings*, arXiv:1307.6440, first posted July 24, 2013. https://arxiv.org/abs/1307.6440
4. J. Riordan, *The distribution of crossings of chords joining pairs of \(2n\) points on a circle*, Mathematics of Computation 29 (1975), 215–222, DOI:10.1090/S0025-5718-1975-0366686-9.
