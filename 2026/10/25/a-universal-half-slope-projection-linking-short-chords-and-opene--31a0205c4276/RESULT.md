# A universal half-slope projection linking short chords and opener–closer peaks in random matchings

## Finding

Let \(M\) be a uniformly random perfect matching of the linearly ordered set \(\{1,\ldots,2n\}\), with integer \(n\ge 2\). A pair \(\{a,b\}\), \(a<b\), is a chord; \(a\) is its opener and \(b\) its closer. Define \(S\) as the number of short chords \(\{i,i+1\}\), and \(L\) as the number of positions \(i\in\{1,\ldots,2n-1\}\) at which \(i\) is an opener and \(i+1\) is a closer. In particular every short chord contributes one to \(L\). Put \(A=L-S\); this counts such adjacent opener–closer pairs on **distinct** chords.

The following finite-size joint second-moment identities hold:

\[
\begin{aligned}
\mathbb E S&=1,&\operatorname{Var}(S)&=\frac{2(n-1)}{2n-1},\\
\mathbb E L&=\frac{n+2}{3},&\operatorname{Var}(L)&=\frac{2(n^2-1)}{9(2n-1)},\\
\operatorname{Cov}(S,L)&=\frac{n-1}{2n-1},&
\operatorname{Cov}(S,A)&=-\frac{n-1}{2n-1}.
\end{aligned}
\]

Thus short chords correlate **positively** with all adjacent opener–closer pairs but **negatively** with the nontrivial pairs formed by different chords, and these covariances have equal magnitudes. For every \(n\ge2\), the unique least-squares affine predictor of \(L\) from \(S\) is

\[
\widehat L=\frac{n+2}{3}+\frac{S-1}{2},
\qquad
\operatorname{Corr}(S,L)=\frac{3}{2\sqrt{n+1}}.
\]

Its residual variance is \(\operatorname{Var}(L-\widehat L)=(n-1)(4n-5)/[18(2n-1)]\), so the fraction of \(L\)-variance explained by the one-dimensional affine projection is precisely \(9/[4(n+1)]\).

There is also a position-resolved deletion identity. Let \(B_i\) be the event that \(\{i,i+1\}\) is a chord. For \(n\ge3\) and \(2\le i\le2n-2\),

\[
\mathbb E[A\mid B_i]=\frac{n-2}{3}-\frac{(i-2)(2n-i-2)}{(2n-3)(2n-5)}.
\]

At the two boundary positions \(i=1,2n-1\), the conditional expectation is \((n-2)/3\). For \(n=2\), it is zero at all three positions.

## Assumptions and scope

Every perfect matching of \(2n\) **linearly** ordered, labeled endpoints has probability \(1/(2n-1)!!\). An LR pair is counted whenever an opener is immediately followed by a closer, whether or not those two endpoints belong to the same chord. No planar, noncrossing, or nonnesting restriction is imposed. The claims concern exact second moments and the least-squares **affine** predictor, not a nonlinear conditional expectation or independence.

## Proof

**1. Single positions and short chords.** For each \(i\), the event \(B_i\) has probability \(1/(2n-1)\), giving \(\mathbb E S=1\). Two distinct short-chord events at positions separated by at least two have joint probability \(1/[(2n-1)(2n-3)]\); overlapping events are incompatible. There are \((2n-2)(2n-3)\) ordered pairs of nonoverlapping short-chord positions. Therefore

\[
\mathbb E[S(S-1)]=\frac{2n-2}{2n-1},\qquad
\operatorname{Var}(S)=\frac{2n-2}{2n-1}.
\]

At position \(j\), an opener immediately followed by a closer belonging to another chord must pair \(j\) to some endpoint beyond \(j+1\) and \(j+1\) to some endpoint before \(j\). There are \(2n-j-1\) and \(j-1\) choices, respectively. Hence

\[
\Pr(j\text{ contributes to }A)=
\frac{(j-1)(2n-j-1)}{(2n-1)(2n-3)}.
\]

Summing from \(j=1\) through \(2n-1\) gives \(\mathbb E A=(n-1)/3\) and \(\mathbb E L=1+(n-1)/3=(n+2)/3\).

**2. The deletion seam and mixed moment.** Condition on a short chord \(B_i\) and delete both its endpoints. The remaining matching, with its inherited order, is uniform on \(2n-2\) points. Its different-chord adjacent opener–closer count has mean \((n-2)/3\). All original different-chord adjacent pairs survive this deletion exactly, except that the deletion *creates* one potentially new adjacent pair between the former points \(i-1\) and \(i+2\), if both exist. In the reduced matching this is the seam at position \(i-1\). For \(n\ge3\), the probability that it is a different-chord opener–closer pair is

\[
q_i=\frac{(i-2)(2n-i-2)}{(2n-3)(2n-5)}
\quad (2\le i\le2n-2),
\]

with \(q_1=q_{2n-1}=0\). This proves the position-resolved identity. As

\[
\sum_{i=1}^{2n-1}q_i=
\frac{\sum_{r=0}^{2n-4}r(2n-4-r)}{(2n-3)(2n-5)}
=\frac{n-2}{3},
\]

linearity, the identity \(S=\sum_i\mathbf1_{B_i}\), and \(\Pr(B_i)=1/(2n-1)\) give

\[
\mathbb E[SA]=\frac1{2n-1}\left((2n-1)\frac{n-2}{3}-\frac{n-2}{3}\right)
=\frac{2(n-1)(n-2)}{3(2n-1)}.
\]

Consequently \(\operatorname{Cov}(S,A)=-(n-1)/(2n-1)\) and \(\operatorname{Cov}(S,L)=(n-1)/(2n-1)\). For \(n=2\), each conditional \(A\)-mean given \(B_i\) is zero, so the same mixed-moment identity holds directly.

**3. The LR-count variance.** The classical second-order Eulerian recurrence for LR pairs [1] admits this probabilistic reading. Start with a uniform matching on \(2n-2\) positions having \(k\) LR pairs; insert the new chord with its opener to the left of all old endpoints and its closer in one of the \(2n-1\) available insertion positions. Exactly \(n-k\) positions increase the LR count by one, while \(n-1+k\) preserve it. This insertion is a bijection between uniformly chosen old matchings plus uniformly chosen slots and uniformly chosen new matchings. Thus, writing \(L_n\) for the LR count at size \(n\),

\[
\Pr(L_n=k+1\mid L_{n-1}=k)=\frac{n-k}{2n-1},
\quad L_1=1.
\]

In particular,

\[
\begin{aligned}
\mathbb E[L_n\mid k]&=k+\frac{n-k}{2n-1},\\
\mathbb E[L_n^2\mid k]&=k^2+\frac{(2k+1)(n-k)}{2n-1}.
\end{aligned}
\]

Induction with \(L_1=1\) yields \(\mathbb E L_n=(n+2)/3\) and \(\operatorname{Var}(L_n)=2(n^2-1)/[9(2n-1)]\).

**4. Regression.** Because \(\operatorname{Var}(S)>0\) for \(n\ge2\), the unique optimal affine slope is

\[
\frac{\operatorname{Cov}(S,L)}{\operatorname{Var}(S)}=\frac12.
\]

The correlation, explained-variance fraction, and residual-variance identities follow by direct substitution of the proved moments. This completes the proof.

## Verification

The independent-of-the-proof enumeration in the accompanying `verify.py` generates all \(146598\) perfect matchings with \(2n\) endpoints for \(2\le n\le7\). It computes the statistics from chord endpoints, checks all the stated exact moments and position-conditioned deletion identities, and validates the Eulerian conditional-moment recurrence through \(n=200\), using exact rational arithmetic. Run `python verify.py`; it prints `VERIFY_OK` on success. The finite checks are diagnostic, not the proof for arbitrary \(n\).

## Relationship to prior work

Cameron and Killpatrick [1] introduce and study both short-chord counts (a generalized Narayana triangle) and LR-pair counts (the row-reversed second-order Eulerian triangle) as **separate marginal distributions**. Their recurrence for the second statistic is credited above. The present statement connects these statistics through their exact *mixed* moment, a deletion-seam identity, an invariant one-half projection slope, and a sign reversal upon excluding same-chord pairs. The inspected text of [1], including its results and concluding discussion, does not state these mixed identities. Krasko and Omelchenko [2] analyze loops and parallel chords; Young [3] studies short-chord marginal laws and their extensions; Marmor [4] studies short-chord Schur positivity and refinements. These results do not visibly imply the new LR-pair joint covariance from the specific material inspected. The possibility of an earlier implicit expression or an uninspected equivalent formula remains.

## Limitations

The regression is affine least squares; it need not equal \(\mathbb E[L\mid S]\). The calculation is for unconstrained uniformly random perfect matchings on a line, not for noncrossing matchings, imperfect matchings, or alternative probability weights. The claimed originality is based on identified comparisons rather than a proof of historical priority. Independent validation has not been performed.

## References

[1] Naiomi T. Cameron and Kendra Killpatrick, “Statistics on Linear Chord Diagrams,” *Discrete Mathematics & Theoretical Computer Science* 21(2), article 11 (2020), arXiv:1902.09021, first posted 2019-02-24. https://dmtcs.episciences.org/en/articles/5211/download

[2] Evgeniy Krasko and Alexander Omelchenko, “Enumeration of Chord Diagrams without Loops and Parallel Chords,” *Electronic Journal of Combinatorics* 24(3), P3.43 (2017), arXiv:1601.05073. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p43/pdf/

[3] Donovan Young, “Linear \(k\)-Chord Diagrams,” *Journal of Integer Sequences* 23, article 20.9.1 (2020), arXiv:2004.06921. https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.pdf

[4] Avichai Marmor, “Schur-Positivity of Short Chords in Matchings,” *Algebraic Combinatorics* 7 (2024), 887–914, arXiv:2307.09894. https://arxiv.org/pdf/2307.09894
