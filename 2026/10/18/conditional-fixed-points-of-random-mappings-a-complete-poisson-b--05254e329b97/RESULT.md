# Conditional fixed points of random mappings: a complete Poisson–Bernoulli limit classification

## Finding

Consider a self-map \(f:[n]\to[n]\), with loops allowed. Its image vector \((f(1),\ldots,f(n))\) is assumed exchangeable under permutations of its \(n\) **domain positions**; in particular, independent identically distributed choices of images satisfy this assumption, even with nonuniform image probabilities. Write
\[
D_i=\#\{j:f(j)=i\},\qquad F=\#\{i:f(i)=i\}.
\]
For a nonnegative integer vector \(d=(d_1,\ldots,d_n)\) with \(\sum_i d_i=n\) and positive probability, the conditional law of \(f\) given \(D=d\) is the uniform arrangement of the multiset containing \(d_i\) copies of label \(i\). Let \((a)_r=a(a-1)\cdots(a-r+1)\), let \((a)_0=1\), and let \(e_r(d)\) be the \(r\)-th elementary symmetric polynomial of the coordinates of \(d\), with \(e_0=1\).

**Exact conditional law.** For every \(n\ge1\), every such \(d\), and all \(0\le r\le n\),
\[
\mathbb E[(F)_r\mid D=d]=\frac{r!e_r(d)}{(n)_r},\qquad
\mathbb E[u^F\mid D=d]=\sum_{r=0}^n\frac{e_r(d)}{(n)_r}(u-1)^r.
\]
In particular, \(\mathbb E[F\mid D]=1\) for **every exchangeable random map**, so \(F\) is mean-independent of the complete labelled indegree vector and of every integrable function of it. For \(n\ge2\),
\[
\operatorname{Var}(F\mid D=d)=\frac{n^2-\sum_i d_i^2}{n(n-1)}.
\]
Moreover \(\mathbb E[(F)_r\mid D=d]\le1\) for all \(r\), including when the indegrees are highly concentrated.

**Complete limiting laws.** For each \(n\), fix a degree vector \(d^{(n)}\) with \(n\) entries summing to \(n\), and let its decreasing rearrangement, normalized by \(n\), be \(a_{n,1}\ge\cdots\ge a_{n,n}\ge0\) (pad with zeros beyond \(n\)). Suppose \(a_{n,j}\to p_j\) for every fixed \(j\ge1\). Then \(p_1\ge p_2\ge\cdots\ge0\) and \(\sum_{j\ge1}p_j\le1\). Put \(q=1-\sum_{j\ge1}p_j\). The conditional fixed-point law converges in **total variation**:
\[
\mathcal L(F\mid D=d^{(n)})\xrightarrow{\mathrm{TV}}
\mathcal L\!\left(Z+\sum_{j\ge1}B_j\right),
\quad Z\sim\operatorname{Poisson}(q),\quad
B_j\sim\operatorname{Bernoulli}(p_j),
\]
where all terms on the right are independent. The infinite Bernoulli sum is almost surely finite. Its mean is \(1\) and its variance is \(1-\sum_jp_j^2\).

Without any assumed coordinatewise profile convergence, \(\mathcal L(F\mid D=d^{(n)})\) converges to \(\operatorname{Poisson}(1)\) in total variation **if and only if**
\[
\frac{\max_i d_i^{(n)}}{n}\longrightarrow0.
\]
All possible subsequential limits have the displayed Poisson–Bernoulli form, and conversely every nonincreasing \((p_j)\) with nonnegative terms and sum at most \(1\) is realized by a deterministic sequence of integer indegree profiles. Thus the list is an exact classification, not merely a sufficient-condition theorem.

## Assumptions and scope

Exchangeability concerns the vector of image values under **permutation of input indices**, not arbitrary simultaneous relabelling of vertices. Conditional uniformity holds at each count vector with positive mass. For the deterministic-profile asymptotics one may equivalently sample a map uniformly from all maps with a given indegree vector; no underlying iid distribution is needed. A degree vector may contain zeros and components equal to \(n\). Every profile considered has exactly \(n\) coordinates with total \(n\); there are no unspecified regularity or bounded-degree hypotheses.

The conditional variance formula requires \(n\ge2\). For \(n=1\), \(F=1\) deterministically and the exact factorial-moment formula still holds. The total-variation statement concerns fixed integers of fixed points as \(n\to\infty\), not a joint graph-process limit.

## Proof

**Step 1: conditional mixed indicators.** Fix \(d\). Exchangeability of the image positions implies that, conditional on \(D=d\), every sequence with these multiplicities is equally likely. For distinct indices \(i_1,\ldots,i_r\), exposing images without replacement gives
\[
\Pr\{f(i_1)=i_1,\ldots,f(i_r)=i_r\mid D=d\}
=\frac{\prod_{h=1}^r d_{i_h}}{(n)_r}.
\]
Summing over ordered tuples proves the factorial-moment formula. The identity \(u^F=(1+(u-1))^F=\sum_r (F)_r(u-1)^r/r!\) proves the conditional probability-generating polynomial. Taking \(r=1\) yields \(\mathbb E[F\mid D=d]=(\sum_i d_i)/n=1\), which proves mean-independence. Taking \(r=2\) yields the displayed variance formula.

**Step 2: uniform moment control.** The integer \(e_r(d)\) counts ways to choose \(r\) balls from \(n\) balls with all chosen balls having different labels, where the multiplicities are \(d_i\). Therefore \(e_r(d)\le\binom nr\). Hence, for every fixed \(n\) and \(0\le r\le n\),
\[
0\le\mathbb E[(F)_r\mid D=d]\le 1.
\]
Consequently the entire function \(\mathbb E[(1+z)^F\mid D=d]\) has an absolutely convergent binomial-moment expansion uniformly dominated by \(e^{|z|}\), independently of \(n\) and \(d\). In particular, every positive exponential moment of \(F\) has a uniform bound.

**Step 3: normalized-degree product limit.** Put \(H_n(z)=\prod_{i=1}^n(1+a_{n,i}z)\). Its coefficient of \(z^r\) is \(e_r(d^{(n)})/n^r\). The monotone arrangement and sum \(\sum_i a_{n,i}=1\) imply \(a_{n,i}\le1/i\) and \(\sum_{i>K}a_{n,i}^2\le1/(K+1)\). For fixed complex \(z\), once \(K>2|z|\),
\[
\sum_{i>K}\bigl|\log(1+a_{n,i}z)-a_{n,i}z\bigr|
\le C_z\sum_{i>K}a_{n,i}^2\le\frac{C_z}{K+1}.
\]
For each fixed \(K\), the first \(K\) factors converge to \(\prod_{j\le K}(1+p_jz)\), while the tail mass tends to \(1-\sum_{j\le K}p_j\). Letting \(n\to\infty\), then \(K\to\infty\), gives locally uniform convergence of entire functions
\[
H_n(z)\longrightarrow H(z):=e^{qz}\prod_{j\ge1}(1+p_jz).
\]
The infinite product converges locally uniformly because \(\sum_jp_j\le1\). For each fixed \(r\), \(n^r/(n)_r\to1\); the exact formula and coefficient convergence therefore give
\[
\mathbb E[(F)_r\mid D=d^{(n)}]\longrightarrow r![z^r]H(z).
\]
The factorial-moment bound from Step 2 permits termwise convergence of \(\mathbb E[(1+z)^F\mid D=d^{(n)}]\) for every complex \(z\), locally uniformly. The limit is \(H(z)\), which is the binomial-moment generating function of an independent \(\operatorname{Poisson}(q)\) plus \(\operatorname{Bernoulli}(p_j)\) sum. Local uniform convergence of the ordinary probability-generating functions around the origin implies convergence of each atom probability. Since both discrete laws have total mass one, Scheffé's argument yields total-variation convergence. The Bernoulli sum is finite almost surely by \(\sum_jp_j<\infty\).

**Step 4: sharp Poisson criterion.** If \(\Delta_n=\max_i d_i^{(n)}\) satisfies \(\Delta_n/n\to0\), then \(\sum_i a_{n,i}^2\le\Delta_n/n\to0\). The same logarithmic product estimate gives \(H_n(z)\to e^z\), and Step 3 gives total-variation convergence to \(\operatorname{Poisson}(1)\). Conversely, if the conditional laws converge to \(\operatorname{Poisson}(1)\), the uniform exponential-moment bounds from Step 2 ensure convergence of the second moments, so the exact conditional variance converges to \(1\). Consequently
\[
\frac{\sum_i(d_i^{(n)})^2}{n^2}
=\frac1n+\frac{n-1}{n}\bigl(1-\operatorname{Var}(F\mid D=d^{(n)})\bigr)
\longrightarrow0.
\]
Thus \((\Delta_n/n)^2\le\sum_i(d_i^{(n)})^2/n^2\to0\). This proves necessity.

**Step 5: completeness and realization.** Any sequence of decreasing profiles admits a coordinatewise convergent subsequence by diagonal compactness, and its limit has sum at most \(1\). Step 3 describes every subsequential law. Conversely, given an admissible \((p_j)\), choose \(K_n=\lfloor\sqrt n\rfloor\) and set \(d_i^{(n)}=\lfloor np_i\rfloor\) for \(1\le i\le K_n\). Distribute the remaining \(n-\sum_{i\le K_n}\lfloor np_i\rfloor\) balls as evenly as possible among the other \(n-K_n\) labels. Each added multiplicity is at most \(2\) for all sufficiently large \(n\), and for every fixed \(j\) the \(j\)-th largest normalized multiplicity tends to \(p_j\). Thus every member of the stated family occurs.

## Verification

The accompanying standard-library script `verify_fixedpoint_profiles.py` exhaustively enumerates all \(50{,}069\) maps with \(1\le n\le6\), groups them into \(637\) distinct labelled indegree profiles, and compares the complete exact conditional distribution against the polynomial formula. It independently checks mean, variance, factorial moments and the bound \(\mathbb E[(F)_r\mid D]\le1\). It also compares finite factorial moments with the claimed limiting families for diffuse, one-hub, two-hub and concentrated profiles. These finite calculations are corroboration; Steps 1–5 establish the infinite assertions.

Run `python verify_fixedpoint_profiles.py` in a directory containing the script; no third-party dependencies or downloaded data are required. Successful execution prints a single PASS line with the enumerated mapping and profile counts.

## Relationship to prior work

Classical fixed-point limit theory for uniform permutations, such as Diaconis, Fulman and Guralnick (arXiv:0708.2643, first submitted 2007-08-20), gives the Poisson limit in the special profile with one copy of every image. Diaconis, Evans and Graham (Berkeley Technical Report 822, 2013-08-01), develops exact fixed-point and adjacent-pair statistics for **permutations**, not fixed-point counts of random functions conditional on arbitrary complete indegree vectors. Flajolet and Odlyzko's *Random Mapping Statistics* (EUROCRYPT 1989 / LNCS 1990) provides the classical random-function setting, with studies of mapping-graph parameters; a full comparison with its preprint was not possible.

Stark's 2026 preprint arXiv:2608.00710 concerns fixed points of permutations of a multiset relative to a reference word containing the same multiplicities, where the reported expected count is \(\sum_i d_i^2/n\). Here there is exactly **one distinguished domain position per possible label**, yielding conditional mean \(1\) for every degree profile. Thus that expectation and its Poisson-approximation regime do not directly supply the present conditional Poisson–Bernoulli classification; its full text was not accessible for a definitive section-by-section overlap check.

The claim concerns the exact conditional law and exhaustive limiting family, not the classical Poisson approximation for unconditioned iid maps or an isolated fixed-point expectation. Equivalent results might exist under *sampling without replacement*, *matching coincidences*, or *multiset diagonal hits* terminology; this possibility remains a residual originality risk.

## Limitations

The theorem does not establish novelty beyond the documented comparisons, does not treat nonexchangeable image vectors, and does not give a rate of total-variation convergence for arbitrary degree profiles. The conditional profile theorem is deterministic in the indegree counts and should not be confused with a law for graph degrees generated by nonexchangeable mechanisms. Possible uninspected historical statements about diagonal coincidences in prescribed-content words remain outside the verified literature coverage.

## References

1. P. Diaconis, J. Fulman and R. Guralnick, *On fixed points of permutations*, arXiv:0708.2643 (posted 2007-08-20), https://arxiv.org/abs/0708.2643 .
2. P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822 (2013-08-01), https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf .
3. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, EUROCRYPT 1989; Lecture Notes in Computer Science 434 (1990), 329–354, https://doi.org/10.1007/3-540-46885-4_34 .
4. D. Stark, *Poisson approximations of the number of fixed points in random multiset permutations*, arXiv:2608.00710 (posted 2026-08-01), https://arxiv.org/abs/2608.00710 .
5. V. N. Sachkov, *Random mappings of sets with restrictions on parameters. II*, Mathematical Aspects of Cryptography 3(2) (2012), 97–116, https://doi.org/10.4213/mvk56 .
