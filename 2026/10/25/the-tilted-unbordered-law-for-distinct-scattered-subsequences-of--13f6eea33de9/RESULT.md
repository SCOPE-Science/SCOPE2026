# The tilted unbordered law for distinct scattered subsequences of an independent source

## Finding

Fix a finite alphabet \(\Sigma\) with \(q\ge2\) letters and strictly positive source probabilities \(p_a\) summing to one. In an independent random length-\(n\) word \(W_n\), let \(B_n\) count **distinct nonempty unbordered strings appearing as scattered subsequences**, counting each string once regardless of its number of embeddings. Let \(D_n\) count all distinct nonempty scattered subsequence strings.

Define
\[
g_a(z)=\frac{p_a z}{1-(1-p_a)z},\qquad S(z)=\sum_{a\in\Sigma}g_a(z),
\]
and the multivariate unbordered-language series
\[
\mathcal U(\mathbf x)=\sum_{u\in\Sigma^+\text{ unbordered}}\prod_{j=1}^{|u|}x_{u_j}.
\]
It is uniquely determined as a formal series with zero constant term by
\[
\bigl(1-\textstyle\sum_a x_a\bigr)\mathcal U(\mathbf x)
=\sum_a x_a-\mathcal U\bigl((x_a^2)_a\bigr).
\]
The exact expectation generating functions, for \(n\ge0\), are
\[
\sum_{n\ge0}\mathbb E B_n z^n=\frac{\mathcal U((g_a(z))_a)}{1-z},\qquad
\sum_{n\ge0}\mathbb E D_n z^n=\frac{S(z)}{(1-z)(1-S(z))}.
\]
Let \(r\in(0,1)\) be the unique solution of \(S(r)=1\) and let \(v_a=g_a(r)\). Then \(\mathbf v\) is a strictly positive probability vector. Define the classical unbordered-word density under this **tilted** source by
\[
\theta(\mathbf v)=1-\mathcal U((v_a^2)_a)
=\lim_{m\to\infty}\Pr_{\mathbf v}\{\text{a random length-}m\text{ word is unbordered}\}.
\]
This density is strictly positive, and the following asymptotics hold for every fixed source with \(q\ge2\) and \(p_a>0\):
\[
\mathbb E B_n\sim
\frac{\theta(\mathbf v)}{(1-r)rS'(r)}r^{-n},\qquad
\mathbb E D_n\sim\frac{1}{(1-r)rS'(r)}r^{-n},
\qquad
\boxed{\lim_{n\to\infty}\frac{\mathbb E B_n}{\mathbb E D_n}=\theta(\mathbf v)>0.}
\]
Both individual asymptotics have exponentially smaller additive errors. For a uniform \(q\)-symbol source, \(\mathbf v\) is also uniform and
\[
\mathbb E B_n\sim\frac{q}{q-1}\theta_q\left(2-\frac1q\right)^n,
\]
where \(\theta_q\) is the previously studied limiting proportion of unbordered uniform \(q\)-ary words. For a biased binary source with probabilities \(p,1-p\),
\[
r=(1+\sqrt{p(1-p)})^{-1},\qquad
\mathbf v=\frac{(\sqrt p,\sqrt{1-p})}{\sqrt p+\sqrt{1-p}}.
\]
Thus the limiting expected fraction is governed by the *square-root tilt* of the source, not generally the source itself.

## Assumptions and scope

A word is *unbordered* when it has no nonempty proper prefix identical to a suffix of the same length. The border is defined in the **pattern word**; the occurrence in \(W_n\) is as a possibly noncontiguous, order-preserving subsequence. A length-zero word is not counted. All source letters have positive probability, and the alphabet contains at least two symbols. The limits keep the probability vector fixed as \(n\to\infty\). The result concerns expectations and their ratio, not a typical-word concentration or an almost-sure density statement.

## Proof

**1. Exact occurrence transform.** For a fixed pattern \(u=u_1\cdots u_k\), greedy left-to-right matching in the independent source has independent waiting times \(T_j\), each geometric on \(\{1,2,\dots\}\) with success probability \(p_{u_j}\). The pattern occurs as a scattered subsequence of \(W_n\) if and only if \(T_1+\cdots+T_k\le n\). Consequently,
\[
\sum_{n\ge0}\Pr\{u\preceq W_n\}z^n
=\frac1{1-z}\prod_{j=1}^k\frac{p_{u_j}z}{1-(1-p_{u_j})z}.
\]
Sum this nonnegative identity over distinct pattern strings in the unbordered language, or in the entire nonempty free monoid, respectively. The first yields \(\mathcal U(\mathbf g(z))/(1-z)\); summing all patterns yields \(S(z)/((1-z)(1-S(z)))\). Equality holds formally coefficientwise since a length-\(n\) word cannot contain a subsequence longer than \(n\).

**2. The weighted border recurrence.** Every nonempty bordered string \(w\) has a unique shortest nonempty border \(b\). This \(b\) is unbordered: any proper border of \(b\) would give a shorter border of \(w\). Moreover \(2|b|\le |w|\): if its two copies overlapped, their overlap would be a nonempty border of \(b\), again a contradiction. Hence \(w=bvb\), uniquely, with \(b\) unbordered and \(v\) an arbitrary possibly empty word. Conversely, any \(bvb\) with \(b\) unbordered has shortest border \(b\): a shorter border would already border \(b\). If the weight of a word is the product of its letter variables, the arbitrary middle contributes \((1-\sum_a x_a)^{-1}\) and the repeated border contributes \(\mathcal U((x_a^2)_a)\). Subtracting the empty word from the free-monoid series gives the displayed recurrence. More explicitly, \(\sum_{w\ne\epsilon}\mathrm{wt}(w)=\mathcal U(\mathbf x)+\mathcal U(\mathbf x^2)/(1-\sum x_a)\), proving \((1-\sum x_a)\mathcal U(\mathbf x)=\sum x_a-\mathcal U(\mathbf x^2)\). All identities hold as formal multivariate series.

**3. Positivity and identification of the limiting density.** For any positive probability vector \(\mathbf v\) with at least two letters, put \(s_2=\sum_a v_a^2<1\). By the same unique shortest-border decomposition, for a random length-\(m\) word with law \(\mathbf v\), the probability of being bordered is
\[
\sum_{j=1}^{\lfloor m/2\rfloor}\ \sum_{b\in\Sigma^j\text{ unbordered}}
\Bigl(\prod_{i=1}^jv_{b_i}\Bigr)^2.
\]
These partial sums increase to \(\mathcal U((v_a^2)_a)\le\sum_{j\ge1}s_2^j<\infty\), so the probability of being unbordered decreases to \(\theta=1-\mathcal U((v_a^2)_a)\ge0\). To show strict positivity, let \(a\) maximize \(v_a\) and let \(b\ne a\). Strictly \(s_2<v_a\). Choose \(K\ge1\) such that \(v_b v_a^K>s_2^{K+1}/(1-s_2)\). For all \(m\ge2K+1\), the event that the first symbol is \(b\) and the last \(K\) symbols are all \(a\) has probability \(v_b v_a^K\) and prevents any border of length at most \(K\). By a union bound, the probability of any border longer than \(K\) is at most \(\sum_{j>K}s_2^j=s_2^{K+1}/(1-s_2)\). Therefore the unbordered probability, and its limit, are bounded below by a strictly positive constant. In particular, \(0<\theta\le1\).

**4. Singularities and the asymptotic.** Each \(g_a\) has positive Taylor coefficients and is strictly increasing on \([0,1]\); \(S(0)=0\) and \(S(1)=q>1\). Thus \(S(r)=1\) has one \(r\in(0,1)\) with \(S'(r)>0\). The vector \(\mathbf v=\mathbf g(r)\) is positive and sums to one. Since \(\sum_a v_a^2<1\), \(\mathcal U((g_a(z)^2)_a)\) is holomorphic on a disk \(|z|<r+\delta\) for some \(\delta>0\): its defining series is dominated there by the geometric sum with ratio \(\sum_a g_a(|z|)^2<1\). The recurrence therefore gives
\[
\frac{\mathcal U(\mathbf g(z))}{1-z}=
\frac{S(z)-\mathcal U((g_a(z)^2)_a)}{(1-z)(1-S(z))}.
\]
Its numerator is \(\theta>0\) at \(r\); the pole there is simple. Since the Taylor series of \(S\) has strictly positive coefficients in every positive degree, the triangle inequality is strict on \(|z|=r\) off the positive real axis, so there are no other poles on that circle. A slightly larger circle can be chosen without poles, establishing coefficient asymptotics by taking the principal-pole residue and estimating the remaining analytic function. The coefficient of \(z^n\) from the pole is \(\theta r^{-n}/((1-r)rS'(r))\). The unrestricted series has the same pole with numerator \(S(r)=1\), giving the stated ratio and exponentially smaller error terms.

**5. Explicit source specializations.** For uniform probabilities \(p_a=1/q\), solving \(S(r)=1\) gives \(r=q/(2q-1)\), \(v_a=1/q\), and \((1-r)rS'(r)=(q-1)/q\). For binary probabilities \(p,1-p\), direct substitution into \(S(r)=1\) gives \(r=(1+\sqrt{p(1-p)})^{-1}\); simplifying \(g_a(r)\) gives the square-root tilt.

## Verification

The companion standalone program `verify_unbordered.py` uses rational arithmetic. It exhaustively enumerates host words under six rational iid source distributions (binary, ternary, and four-letter) and constructs actual sets of scattered subsequences; it compares expected unbordered pattern counts with coefficients obtained from the weighted shortest-border recurrence and the independent geometric-waiting transform. It separately enumerates short unbordered pattern words to check the recurrence, for a total of 30,260 host strings. It also checks the uniform binary limiting density against the independently published constant. Output:

`VERIFY_OK exact_source_words=30260 rational_sources=6 full_weighted_pattern_check=TRUE fair_binary_unbordered_limit=0.2677868402178891 fair_ternary_limit=0.556979839764`

These finite tests check the implementation of the exact identities, not the infinite asymptotic. The proof above supplies the infinite result.

## Relationship to prior work

Gabric (2023) develops the shortest-border structure and algorithms to rank/unrank ordinary unbordered words; these established structural facts underlie the weighted recurrence. Harju and Nowotka (2005) count bordered and primitive words by fixed Parikh weight, so weighted language enumeration is not asserted new. Holub and Shallit (2015) calculate unbordered probabilities for random *whole words*, including the uniform limiting density; that density is used here, not rediscovered. Biers-Ariel, Godbole and Kelley (2017) analyze expectations for **unrestricted** distinct scattered subsequences of random words. Cording, Gagie, Knudsen and Kociumaka (2017) study maximal **contiguous** unbordered factors. The contribution evaluated here is specifically the exact restriction of the distinct scattered-subsequence expectation to unbordered patterns and its analytic arbitrary-source asymptotic, including the square-root tilt for binary bias and limiting expected-count ratio.

## Limitations

The asymptotic is for a fixed finite alphabet with every symbol of positive probability; a degenerate single-symbol source and growing alphabets are excluded. The ratio of expectations is not the expectation of a per-word ratio and does not imply concentration. The unbordered-word density is an established combinatorial quantity; neither its uniform value nor the shortest-border recurrence is claimed as an original theorem. Overlap with an unindexed weighted-language or probabilistic-pattern result cannot be excluded by finite literature searches. The 2005 fixed-weight full text was not accessible during this comparison; its abstract and indexed sequence were checked, not represented as a full-text inspection.

## References

1. Daniel Gabric, *Ranking and unranking bordered and unbordered words*, arXiv:2305.03000, first publicly posted 2023-05-04. https://arxiv.org/abs/2305.03000
2. Štěpán Holub and Jeffrey Shallit, *Periods and borders of random words*, arXiv:1509.05240, first posted 2015-09-17. https://arxiv.org/abs/1509.05240
3. Yonah Biers-Ariel, Anant Godbole, and Elizabeth Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661, first posted 2017-04-27. https://arxiv.org/abs/1704.08661
4. Tero Harju and Dirk Nowotka, *Counting bordered and primitive words with a fixed weight*, Theoretical Computer Science 340 (2005), 273–279, DOI:10.1016/j.tcs.2005.03.040. https://doi.org/10.1016/j.tcs.2005.03.040
5. E. Cording, T. Gagie, M. B. T. Knudsen, D. Kociumaka, *Maximal Unbordered Factors of Random Strings*, arXiv:1704.04472, 2017. https://arxiv.org/abs/1704.04472
