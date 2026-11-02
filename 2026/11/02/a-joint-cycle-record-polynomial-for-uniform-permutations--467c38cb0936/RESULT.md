# A joint cycle–record polynomial for uniform permutations

## Finding

Let \(n\ge2\) and let \(\Pi\) be uniform on permutations of \(\{1,\ldots,n\}\). Define \(C\) as the number of disjoint cycles of **this same permutation** (including fixed points). For \(1\le i\le n\), let \(R_i\) be the indicator of the one-line upper-record event \(\Pi(i)=\max\{\Pi(1),\ldots,\Pi(i)\}\). For a complex number \(t\), write \(t^{\overline r}=\prod_{j=0}^{r-1}(t+j)\) and \(t^{\overline0}=1\).

**Joint polynomial theorem.** For every \(2\le i\le n\) and all complex \(t\),

\[
\mathbb E\bigl[t^C R_i\bigr]
=\frac{t^{\overline n}}{i\,n!}
+\frac{i-1}{i\,n!}\,t^{\overline{n-i}}(t-1)^{\overline i}.
\tag{1}
\]

Thus the joint distribution of the total cycle count and the indicator of a record at **any specified position** is explicitly determined, not merely its first moment. In particular,

\[
\operatorname{Cov}(R_i,C)=\frac{i-1}{i^2\binom ni}>0
\qquad (2\le i\le n),
\tag{2}
\]

whereas \(R_1=1\) deterministically. Let \(R=\sum_{i=1}^n R_i\) be the number of upper records. Then

\[
\operatorname{Cov}(R,C)=\sum_{i=2}^n\frac{i-1}{i^2\binom ni}
=\frac1n+O(n^{-2}),
\qquad
\operatorname{Corr}(R,C)\sim\frac{1}{n\log n}.
\tag{3}
\]

There is also an exact change-of-measure consequence. Under the **conventional cycle-weighted Ewens law on the same permutation**, \(\Pr_\theta(\pi)=\theta^{C(\pi)}/\theta^{\overline n}\) for \(\theta>0\),

\[
\Pr_\theta(R_i=1)
=\frac1i\left[1+(i-1)\frac{(\theta-1)^{\overline i}}{(\theta+n-i)^{\overline i}}\right].
\tag{4}
\]

For every \(2\le i\le n\), this probability is strictly below \(1/i\) if \(0<\theta<1\), equals \(1/i\) at \(\theta=1\), and is strictly above \(1/i\) if \(\theta>1\). The comparison uses one-line records and cycles **of the same sampled permutation**, not the equidistribution of records and cycles under a separate Foata transform.

## Assumptions and scope

All permutations are bijections of \(\{1,\ldots,n\}\), expressed in one-line notation when defining records and in disjoint-cycle notation when defining \(C\). There is no conditioning on cycle type or avoidance class. Equations (1)–(3) concern the uniform law, while (4) concerns the cycle-weighted Ewens law for real \(\theta>0\). Equation (1) is a polynomial identity valid for complex \(t\); its probabilistic generating-function interpretation is immediate for nonnegative real \(t\). The endpoint \(i=1\) is deterministic and excluded from the nontrivial formulas. All fixed finite sizes \(n\ge2\) and all admissible record positions are included.

## Proof

**Lemma 1 (partial-permutation completion).** Fix an injection from some \(a\) specified domain labels into the full set of \(n\) labels. The directed graph of its prescribed arrows consists of some closed directed cycles (say \(c\) of them) and \(n-a\) directed paths, including singleton paths. For a uniform completion to a permutation, the \(n-a\) remaining arrows bijectively join path endpoints to path starts, forming a uniform permutation of the path components. Thus its total cycle count has conditional generating polynomial

\[
 t^c\frac{t^{\overline{n-a}}}{(n-a)!}.
\tag{5}
\]

This remains valid for \(a=n\): the empty path permutation has polynomial one.

**Lemma 2 (closed cycles of an injection).** If \(\phi:[k]\hookrightarrow[m]\) is a uniform injection, where \(0\le k\le m\), and \(B\) counts directed cycles of \(\phi\) entirely contained in \([k]\), then

\[
\mathbb E[t^B]=\frac{(t+m-k)^{\overline k}}{m^{\underline k}},
\tag{6}
\]

where \(m^{\underline k}=m(m-1)\cdots(m-k+1)\). To prove this, extend the injection uniformly to a permutation on \([m]\). Insert first the \(m-k\) unmarked labels using the standard permutation-insertion construction, then insert the \(k\) marked labels one at a time. At the \(j\)-th marked insertion there are \(m-k+j-1\) equally weighted places inside existing cycles and one place for starting a new cycle. The latter creates exactly one new cycle entirely of marked labels. Consequently the cycle-count generating factor is \((t+m-k+j-1)/(m-k+j)\). Multiplying for \(j=1,\ldots,k\) proves (6). The number of entirely marked cycles is exactly the number of closed cycles in the original partial injection, regardless of subsequent insertions.

For the theorem, fix \(i\ge2\), and let \(M=\max\{\Pi(1),\ldots,\Pi(i)\}\). The record event has probability \(1/i\) and is independent of the unordered image set of the first \(i\) positions; hence, conditioned on \(R_i=1\),

\[
\Pr(M=m\mid R_i=1)=\frac{\binom{m-1}{i-1}}{\binom ni},
\qquad i\le m\le n.
\tag{7}
\]

If \(m=i\), the first \(i\) images are exactly \([i]\), \(\Pi(i)=i\), and the remaining first \(i-1\) arrows make a uniform permutation of \([i-1]\). The generating polynomial for the number \(c\) of already closed cycles is \(t\,t^{\overline{i-1}}/(i-1)!\). If \(m>i\), then \(\Pi(i)=m>i\) cannot be in a closed cycle among the first \(i\) arrows, and the other arrows form a uniform injection from \([i-1]\) into \([m-1]\). Lemma 2 gives the polynomial \((t+m-i)^{\overline{i-1}}/(m-1)^{\underline{i-1}}\). In both cases Lemma 1 supplies the independent completion factor \(t^{\overline{n-i}}/(n-i)!\).

Multiply by (7), by \(1/i\), and by the completion factor. Since

\[
 \binom{m-1}{i-1}=(m-1)^{\underline{i-1}}/(i-1)!,
\]

all nonexceptional denominators cancel. The exceptional case \(m=i\) contributes an additional \((t-1)t^{\overline{i-1}}=(t-1)^{\overline i}\). Therefore

\[
\mathbb E[t^C R_i]
=\frac{t^{\overline{n-i}}}{i\,(n-i)!\binom ni\,(i-1)!}
\left[\sum_{r=0}^{n-i}(t+r)^{\overline{i-1}}
+(t-1)^{\overline i}\right].
\tag{8}
\]

The elementary rising-factorial telescoping identity gives

\[
\sum_{r=0}^{n-i}(t+r)^{\overline{i-1}}
=\frac{(t+n-i)^{\overline i}-(t-1)^{\overline i}}{i}.
\tag{9}
\]

Substituting into (8), using \(n!=(n-i)!\,i!\binom ni\), and joining \(t^{\overline{n-i}}(t+n-i)^{\overline i}=t^{\overline n}\), proves (1).

For (2), differentiate (1) at \(t=1\) and subtract \(\mathbb E R_i\,\mathbb E C\). Here \(\mathbb E R_i=1/i\), \(\mathbb E C=H_n=\sum_{j=1}^n1/j\), and

\[
\left.\frac{d}{dt}(t-1)^{\overline i}\right|_{t=1}=(i-1)!.
\]

The difference is \((i-1)(i-1)!(n-i)!/(i n!)\), equal to (2), and it is strictly positive.

Summing proves the exact first formula in (3). The \(i=n\) term is \((n-1)/n^2=1/n+O(n^{-2})\). The two terms \(i=2\) and \(i=n-1\) are \(O(n^{-2})\); the other terms together contribute \(O(n^{-2})\), since for \(3\le i\le n-2\) we have \(\binom ni\ge\binom n3\). The familiar independent-record-indicator calculation and the standard uniform cycle-count generating polynomial \(\mathbb E[t^C]=t^{\overline n}/n!\) both give \(\operatorname{Var}(R)=\operatorname{Var}(C)=H_n-\sum_{j=1}^n j^{-2}\sim\log n\). Division proves the correlation asymptotic.

Finally, divide (1), evaluated at \(t=\theta>0\), by \(\mathbb E[\theta^C]=\theta^{\overline n}/n!\), giving (4). Its correction factor has the sign of \(\theta-1\), since every other numerator factor and every denominator factor is positive. This proves the complete sign classification.

## Verification

The accompanying standalone `verify.py` enumerates all \(46{,}232\) permutations of sizes \(2\) through \(8\). It reconstructs cycle counts directly from the permutation map and computes each upper-record indicator from one-line prefixes. For all admissible positions, it checks every coefficient of (1) with exact rational arithmetic (196 coefficient comparisons), every positional covariance (28 comparisons), and the Ewens probability formula at parameters \(1/2,1,3/2,3\) (112 comparisons). It reports `VERIFY_OK` on success. Run with `python3 verify.py` from the same folder; only the Python standard library is used. The finite enumeration is not the proof for arbitrary \(n\); Lemmas 1–2 and equations (7)–(9) supply the infinite-family argument.

## Relationship to prior work

Gnedin (arXiv:math/0611538, first public version November 17, 2006) develops coherent random permutations and one-line record statistics, discusses the classical fundamental record–cycle bijection, and identifies Ewens-type families. Gnedin and Gorin (arXiv:1202.3680, first public version February 16, 2012) study measures weighted by **record counts**, explaining their relationship to cycle-weighted measures under a **bijection to another permutation**. These results motivate the distinction between equidistribution and the joint law for records and cycles of the original same permutation. Neither the marginal equality nor the cited change-of-permutation bijection directly implies (1). The inspected passages do not give (1)–(4). Parviainen (arXiv:math/0610616, first public version October 20, 2006) develops joint generating functions for cycles and permutation patterns **written in standard cycle form**, explicitly contrasting this with patterns of the original one-line permutation; those enumerations do not resolve the positionwise original-one-line record event in (1). Jin (arXiv:2210.08789, first public version October 17, 2022) studies Euler–Stirling permutation statistics and one-line maxima/minima, but the inspected generating functions do not simultaneously mark disjoint cycles of the original permutation and the fixed-position upper-record event.

Related publicly indexed results include a covariance profile of the total cycle count against single inversion indicators, a fixed-point-versus-descent localization result, and a cycle-count identity arising from bivariate Pareto-record events. Their objects or events differ: inversion covariances do not specify intersections that define a running maximum; the others do not involve one-line upper-record positions jointly with the cycle count of the same permutation. This is a statement-level comparison, not a claim that an unsuccessful search proves worldwide novelty.

## Limitations

The result concerns total disjoint-cycle count and one indicator of a one-line upper record, not the multivariate joint law of **all** record indicators together with cycle length counts. Positional positive covariance does not imply positive association, independence, or stochastic ordering for the full vector. The correlation asymptotic is specific to the uniform law. The exact Ewens sign classification compares each record probability with its uniform counterpart; it does not establish monotonicity in the parameter throughout either side of one. Independent mathematical assessment and exhaustive historical-priority verification have not been performed. Older or differently indexed joint permutation-enumeration identities could be equivalent to (1).

## References

1. Alexander Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first version 2006-11-17, https://arxiv.org/abs/math/0611538. Especially Sections 1–3 and the discussion of Ewens distributions.
2. Alexander Gnedin and Vadim Gorin, *Record-dependent measures on the symmetric groups*, arXiv:1202.3680, first version 2012-02-16, https://arxiv.org/abs/1202.3680. Especially the Introduction and the discussion of the fundamental bijection.
3. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, https://ac.cs.princeton.edu/home/AC.pdf. Classical records, Stirling cycle numbers, and combinatorial generating functions.
4. Robert Parviainen, *Cycles and patterns in permutations*, arXiv:math/0610616, initial submission 2006-10-20, https://arxiv.org/abs/math/0610616. Especially Sections 1–3, standard cycle form and cyclic pattern statistics.
5. Emma Yu Jin, *Symmetric generating functions and Euler–Stirling statistics on permutations*, arXiv:2210.08789, initial submission 2022-10-17, https://arxiv.org/abs/2210.08789. Compared for stronger joint-enumeration coverage.
