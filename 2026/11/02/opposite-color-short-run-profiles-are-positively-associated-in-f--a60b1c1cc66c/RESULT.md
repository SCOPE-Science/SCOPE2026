# Opposite-color short-run profiles are positively associated in fixed-content random circles

## Finding

Consider a uniformly sampled binary word on \(n=a+b\) cyclically indexed positions, containing exactly \(a\ge2\) zeros and \(b\ge2\) ones. A *run* is a maximal nonempty circular block of one symbol. For \(s\in\{0,1\}\) and a positive integer \(t\), let \(C^{(s)}_t\) count the runs of symbol \(s\) whose lengths are **at most** \(t\). Write \(\mathbf C^{(0)}=(C^{(0)}_1,\ldots,C^{(0)}_a)\) and \(\mathbf C^{(1)}=(C^{(1)}_1,\ldots,C^{(1)}_b)\).

**Two-color short-run positive association.** For every pair of coordinatewise nondecreasing real functions \(F\colon\mathbb Z_{\ge0}^a\to\mathbb R\) and \(G\colon\mathbb Z_{\ge0}^b\to\mathbb R\),
\[
\operatorname{Cov}\!\left(F(\mathbf C^{(0)}),G(\mathbf C^{(1)})\right)\ge0.
\]
If both functions are strictly increasing whenever their coordinate vectors increase strictly in the product order, the inequality is strict. Thus any pair of increasing events, one determined by each color's short-run profile, is positively correlated. The statement also holds for bounded monotone statistics of arbitrary collections of these coordinates.

For the especially natural singleton-run counts \(P=C^{(1)}_1\) (the number of circular occurrences of \(010\)) and \(Q=C^{(0)}_1\) (the number of occurrences of \(101\)), the covariance has an exact factorization. Let \(R\) be the number of cyclic \(01\) transitions, also the number of runs of either color. Then
\[
\boxed{\operatorname{Cov}(P,Q)=
\frac{\operatorname{Var}(R(R-1))}{(a-1)(b-1)}>0.}
\]
For a fully explicit finite formula, let \((x)_{\underline{k}}=x(x-1)\cdots(x-k+1)\), and define
\[
M_k=\begin{cases}
\dfrac{(a)_{\underline{k}}(b)_{\underline{k}}}{(n-1)_{\underline{k}}},&k\le\min(a,b),\\[3pt]
0,&k>\min(a,b).
\end{cases}
\]
Then
\[
\boxed{\operatorname{Cov}(P,Q)=
\frac{M_4+4M_3+2M_2-M_2^2}{(a-1)(b-1)}.}
\]
These formulas apply at every \(a,b\ge2\), including the small cases where some \(M_k=0\). If one color has only one occurrence, the corresponding short-run profile is deterministic and all stated cross-color covariances are zero.

## Assumptions and scope

The sample space is the \(\binom{n}{a}\) distinct position-labeled words of the specified composition, each equally likely. Positions are labeled even when the circular pattern has a nontrivial period; no quotient by rotations is taken. Adjacent positions include the last and first. Both colors appear. Every run length is a positive integer; the sum of all zero-run lengths is \(a\), and that of all one-run lengths is \(b\). The test functions are real-valued on finite sets, so all moments exist. No limit theorem or independence of the original cyclic letters is assumed.

## Proof

**1. Conditional composition factorization.** A binary cyclic word with both symbols has the same number \(R=r\) of zero-runs and one-runs. The possible values are \(1\le r\le\min(a,b)\). Let \(\mathcal P_{m,r}\) be the set of ordered positive integer compositions of \(m\) into \(r\) parts; its size is \(\binom{m-1}{r-1}\).

Fix a zero-run start and list the alternating zero-run and one-run lengths in circular order. This yields an element of \(\mathcal P_{a,r}\times\mathcal P_{b,r}\). Conversely, a pair of such compositions and a selected starting position determines a cyclic word. Each position-labeled cyclic word with \(r\) zero-runs has exactly \(r\) possible choices of zero-run start. Consequently
\[
\Pr(R=r)=\frac{n}{r\binom na}\binom{a-1}{r-1}\binom{b-1}{r-1}.
\]
Moreover, conditional on \(R=r\), the ordered zero-run and one-run compositions are **independent and each uniform** on its respective composition space. This statement accounts correctly for rotationally periodic words, because the number of marked zero-run starts is exactly \(r\) for every position-labeled word.

**2. Simultaneous refinement coupling.** A positive composition of \(m\) into \(r\) parts corresponds bijectively to a subset of \(r-1\) of the \(m-1\) internal gaps of an ordered string of \(m\) symbols. Choose a uniformly random ordering of those \(m-1\) gaps and use its first \(r-1\) elements as cuts. The resulting composition is uniform on \(\mathcal P_{m,r}\) for each \(r\), and the compositions are nested by refinement as \(r\) increases.

Splitting a part of length \(L\) into two positive parts cannot reduce the number of parts of length at most \(t\): if \(L\le t\), one counted part becomes two counted parts; if \(L>t\), an uncounted part becomes zero, one, or two counted parts. Therefore every coordinate of the vector of cumulative short-run counts increases weakly along the coupling.

Let \(u(r)=\mathbb E[F(\mathbf C^{(0)})\mid R=r]\) and \(v(r)=\mathbb E[G(\mathbf C^{(1)})\mid R=r]\). The refinement coupling proves that both are nondecreasing in \(r\). Conditional independence of the two colors' run compositions gives
\[
\operatorname{Cov}\!\left(F(\mathbf C^{(0)}),G(\mathbf C^{(1)})\right)
=\operatorname{Cov}(u(R),v(R)).
\]
Using an independent copy \(R'\) of \(R\), twice this last covariance is
\[
\mathbb E[(u(R)-u(R'))(v(R)-v(R'))]\ge0.
\]
Since \(a,b\ge2\), both \(R=1\) and \(R=2\) have positive probabilities. Under a strict product-order increase, each of \(u,v\) increases strictly from \(r=1\) to \(r=2\): the latter has two parts instead of one in each color, and the cumulative count at the maximal threshold goes from one to two. Thus the covariance is strict when both functions are strictly increasing in the stated sense.

**3. The exact singleton covariance.** For a uniform positive composition of \(m\ge2\) into \(r\) parts, the probability that any specified part has length one is \((r-1)/(m-1)\); hence its expected number of singleton parts is \(r(r-1)/(m-1)\), including \(r=1\). The conditional means are therefore
\[
\mathbb E[P\mid R=r]=\frac{r(r-1)}{b-1},\qquad
\mathbb E[Q\mid R=r]=\frac{r(r-1)}{a-1}.
\]
Conditional independence and the total covariance identity now yield the variance factorization.

For completeness, consider \((R)_{\underline{k}}\), the number of ordered \(k\)-tuples of distinct cyclic \(01\) transitions. If \(k\le\min(a,b)\), their \(2k\) endpoints must be disjoint, and the number of ordered possible placements is \(\frac{n}{n-k}\binom{n-k}{k}k!\). The probability that the specified placements all have pattern \(01\) is \(\frac{(a)_{\underline{k}}(b)_{\underline{k}}}{(n)_{\underline{2k}}}\). Cancellation gives
\[
\mathbb E[(R)_{\underline{k}}]
=\frac{(a)_{\underline{k}}(b)_{\underline{k}}}{(n-1)_{\underline{k}}}=M_k.
\]
If \(k>\min(a,b)\), this expectation is zero. Finally,
\[
\bigl((R)_{\underline{2}}\bigr)^2
=(R)_{\underline{4}}+4(R)_{\underline{3}}+2(R)_{\underline{2}},
\]
which proves the explicit formula. Strict positivity also follows because \(R(R-1)\) differs between the positive-probability events \(R=1\) and \(R=2\).

## Verification

The accompanying standalone `verify.py` enumerates the position-labeled binary words for every \(a,b\ge2\) with \(a+b\le14\). It independently tests the exact run-count distribution, factorization of the conditional two-color singleton-count table, each conditional mean, the falling-factorial covariance expression, and positive quadrant dependence for every possible pair of singleton thresholds, and positive quadrant dependence and strict positive covariance for every pair of cross-color cumulative short-run coordinates. All 66 parameter pairs passed; the enumeration covered 584 distinct \((R,P,Q)\) categories. For finite short-run profile thresholds, the general monotonicity proof is analytic and does not depend on exhaustive enumeration. Run `python3 verify.py` in the extracted package.

## Relationship to prior work

Run distributions under Bernoulli and Pólya urn schemes are classical. Makri, Philippou and Psillakis (2007), DOI 10.1080/03610920601033942, derive circular distributions for **one color's** overlapping success runs; their publicly dated online appearance is March 22, 2007. Inoue and Aki (2005) study joint counts of multiple success-run lengths. Eryilmaz (2008), DOI 10.1239/jap/1231340230, gives broad **joint run-statistic distributions** for multiple colors in a linear exchangeable-urn model, including exact-length run counts. These are substantial antecedents: the present formulas are not claimed as a new general joint enumerator.

The assessed additional statement is the **circular, fixed-content, all-threshold positive-association theorem** established through conditional independence and a common refinement coupling, together with the exact singleton covariance factorization and its strict-sign boundary. A general joint distribution may permit these facts to be recovered after further reasoning; its mere existence is not evidence that the refinement-based stochastic ordering or its strictness has previously been stated. These priority distinctions require independent literature review.

## Limitations

Positive association is **cross-color**, between isotone functions of cumulative short-run profiles; it is not asserted for all functions of raw run lengths, nor for arbitrary pairs of statistics of one color. The model fixes both symbol counts and uses the uniform distribution; no claim is made for nonuniform permutations, arbitrary dependent sequences, or three or more colors. No result is asserted about temporal or spatial correlations under a stochastic process with replacement. Independent verification of historical novelty has not been performed.

## References

1. F. S. Makri, A. N. Philippou, and Z. M. Psillakis, *Pólya, Inverse Pólya, and Circular Pólya Distributions of Order k for l-Overlapping Success Runs*, Communications in Statistics—Theory and Methods 36 (2007), 657–668, DOI: 10.1080/03610920601033942. https://doi.org/10.1080/03610920601033942
2. S. Eryilmaz, *Run Statistics Defined on the Multicolor Urn Model*, Journal of Applied Probability 45 (2008), 1007–1023, DOI: 10.1239/jap/1231340230. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F863F78C31086D3F9C4D80477BBE1291/S0021900200004940a.pdf/run-statistics-defined-on-the-multicolor-urn-model.pdf
3. K. Inoue and S. Aki, *Joint distributions of numbers of success runs of specified lengths in linear and circular sequences*, Annals of the Institute of Statistical Mathematics 57 (2005), 353–368. https://www.ism.ac.jp/editsec/aism/pdf/057_2_0353.pdf
