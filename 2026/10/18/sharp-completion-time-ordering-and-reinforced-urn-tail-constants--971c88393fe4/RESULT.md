# Sharp completion-time ordering and reinforced-urn tail constants

## Finding

For integers \(q\ge 2\) and \(a\ge r\ge 1\), begin with \(a\) balls of each of \(q\) colors and stop when each color has been **observed** at least \(r\) times. Let \(T_-\), \(T_0\), and \(T_+\) be the number of observations required when, respectively, a sampled ball is removed (sampling without replacement), is returned unchanged (independent sampling with replacement), or is returned together with one extra ball of the same color (linear Pólya reinforcement). Then for every integer \(k\ge qr\),
\[
\Pr(T_-\le k)>\Pr(T_0\le k)>\Pr(T_+\le k).
\]
For \(k<qr\), all three completion probabilities vanish. Consequently \(T_-\) is stochastically smaller than \(T_0\), which is stochastically smaller than \(T_+\); strictness refers to the displayed finite horizons, not a claimed joint pathwise construction.

There is also a sharp reinforced-urn tail law:
\[
\Pr(T_+>k)\sim C_{q,a,r}\,k^{-a},\qquad
C_{q,a,r}=q\,\frac{\Gamma(qa)}{\Gamma((q-1)a)}
\sum_{j=0}^{r-1}\frac{(a)^{\overline j}}{j!},
\]
where \((a)^{\overline j}=a(a+1)\cdots(a+j-1)\) and \((a)^{\overline0}=1\). For all real \(s>0\), \(\mathbb E[T_+^s]<\infty\) exactly when \(s<a\). In particular, for \((q,a,r)=(3,2,2)\), \(C_{3,2,2}=180\), and the reinforced completion time has a finite mean but infinite variance.

## Assumptions and scope

All three processes have the same initial **balanced** finite urn of \(qa\) balls, with \(q,a,r\) fixed positive integers satisfying \(q\ge2\) and \(1\le r\le a\). Colors are recorded on each draw; an observed ball need not be removed from the record to count toward a target. In the reinforced process, the extra ball is added after observing its color. A Pólya draw sequence is the usual Dirichlet mixture of independent categorical draws with random parameter vector \(\Theta\sim\mathrm{Dirichlet}(a,\ldots,a)\). All three stopping times are almost surely finite; \(T_-\le qa\) deterministically.

The notation \(X\le_{\mathrm{st}}Y\) means \(\Pr(X\le k)\ge\Pr(Y\le k)\) for all integers \(k\). The formula gives asymptotics in \(k\to\infty\) with \(q,a,r\) fixed, not uniform asymptotics when the numbers of colors or targets grow.

## Proof

**Lemma 1: finite-population balancing.** Fix an urn composition \(c=(c_1,\ldots,c_q)\) of total \(N\). Let \(H_k(c)\) be the probability that sampling \(k\le N\) balls uniformly *without replacement* obtains at least \(r\) balls of every color. If \(c_i=A\ge B+2=c_j+2\), moving one ball from color \(i\) to color \(j\) cannot decrease \(H_k\).

To verify this, mark one of the \(A\) balls of color \(i\) and recolor it as \(j\), coupling the sample's *indices* before and after. If the marked ball is absent, the success events coincide. Conditional on its presence and on the sample from the other \(q-2\) categories, suppose that \(t\) sampled balls came from these two categories, including the marked ball; conditional on those choices, let \(U\) count color-\(i\) balls among the other \(t-1\). Then \(U\) is hypergeometric with populations \(A-1,B\). Before recoloring the pair passes its two target conditions when \(r-1\le U\le t-r-1\); afterward it passes when \(r\le U\le t-r\). For \(t<2r\), both events are empty. For \(t\ge2r\), the gain in conditional success probability equals
\[
\Pr(U=t-r)-\Pr(U=r-1).
\]
After multiplying by the common positive hypergeometric denominator, the difference becomes
\[
\binom{A-1}{t-r}\binom{B}{r-1}
-\binom{A-1}{r-1}\binom{B}{t-r}\ge0.
\]
Indeed \(A-1\ge B\) and \(t-r\ge r>r-1\), and for any \(v>u\) the ratio \(\binom{x}{v}/\binom{x}{u}\) is nondecreasing in integer \(x\) wherever both binomial factors exist. The zero-boundary cases obey the same inequality by inspection. Conditioning and averaging prove the lemma. Repeating balancing steps proves that the equal population \((a,\ldots,a)\) maximizes \(H_k\) among all compositions of total \(qa\).

Take \(qa\) independent initially uniform color labels to form a random population vector \(C\sim\mathrm{Multinomial}(qa;1/q,\ldots,1/q)\). Selecting \(k\) random distinct labels from this *random* population gives \(k\) independent uniform color draws: independence holds because the underlying labels at distinct sampled indices are independent. Hence
\[
\Pr(T_-\le k)=H_k(a,\ldots,a)
\ge\mathbb E[H_k(C)]=\Pr(T_0\le k)
\qquad(qr\le k\le qa).
\]
The inequality is strict: with positive probability \(C\) has all balls of one color, for which \(H_k(C)=0\), whereas \(H_k(a,\ldots,a)>0\) for every \(k\ge qr\). If \(k>qa\), \(\Pr(T_-\le k)=1\) while \(\Pr(T_0\le k)<1\). Thus the first inequality holds for all claimed horizons.

**Lemma 2: independent-sampling probability balancing.** For any categorical probability vector \(p\), define \(F_k(p)\) as the probability of obtaining at least \(r\) of each of \(q\) categories in \(k\) independent observations. Then, for \(k\ge qr\), \(F_k\) is strictly maximized by \(p=(1/q,\ldots,1/q)\).

For fixed categories \(i,j\), write their probabilities as \(su,s(1-u)\), keeping their sum \(s>0\) and all remaining probabilities fixed. Condition on the number \(t\) of trials selecting either of these categories and the counts of all other categories. When all those other counts reach \(r\), the relevant pair-success probability is
\[
B_{t,r}(u)=\sum_{h=r}^{t-r}\binom th u^h(1-u)^{t-h}.
\]
This vanishes if \(t<2r\). If \(t\ge2r\), differentiation and cancellation yield
\[
B'_{t,r}(u)=t\binom{t-1}{r-1}
 u^{r-1}(1-u)^{r-1}
\bigl((1-u)^{t-2r+1}-u^{t-2r+1}\bigr).
\]
Thus \(B_{t,r}\) strictly increases up to \(u=1/2\) and strictly decreases afterward. When every \(p_i>0\) and \(k\ge qr\), there is positive probability of a conditioning event with \(t\ge2r\) and all other counts at least \(r\); hence equalizing any unequal positive pair strictly raises \(F_k\). Repeated pair equalization, or a compactness/maximum argument, gives the uniform vector as unique maximizer. At a boundary vector at least one color is never observed, so \(F_k=0<F_k(1/q,\ldots,1/q)\).

Under Pólya reinforcement, exchangeability gives the exact Dirichlet mixture
\[
\Pr(T_+\le k)=\mathbb E[F_k(\Theta)],\qquad
\Theta\sim\operatorname{Dirichlet}(a,\ldots,a).
\]
The random vector \(\Theta\) is almost surely an interior *nonuniform* vector. Lemma 2 therefore gives
\(\Pr(T_+\le k)<F_k(1/q,\ldots,1/q)=\Pr(T_0\le k)\) for all \(k\ge qr\).

**Lemma 3: sharp upper-tail constant.** Write \(N_i(k)\) for the number of observations of color \(i\) among the first \(k\) Pólya draws. By the Dirichlet mixture, \(N_i(k)\) is beta-binomial with parameters \(k,a,(q-1)a\). For every fixed nonnegative integer \(j\),
\[
\Pr(N_i(k)=j)=\binom kj
\frac{(a)^{\overline j}((q-1)a)^{\overline{k-j}}}
 {(qa)^{\overline k}}
\sim k^{-a}\frac{\Gamma(qa)}{\Gamma((q-1)a)}
\frac{(a)^{\overline j}}{j!}.
\]
Consequently \(\Pr(N_i(k)<r)\) equals the corresponding sum over \(0\le j<r\), up to a factor \(1+o(1)\). For two distinct categories, the simultaneous event \(N_i(k)<r,N_j(k)<r\) has probability \(O(k^{-2a})\) when \(q\ge3\), by the three-group Dirichlet-multinomial law with group parameters \(a,a,(q-2)a\). The last factor has a gamma-ratio asymptotic with exponent \(2a\), uniformly over the finitely many \(j,\ell<r\). If \(q=2\), simultaneous failure is impossible for \(k>2(r-1)\). Since \(\{T_+>k\}=\bigcup_{i=1}^q\{N_i(k)<r\}\), the first two Bonferroni bounds show that its probability equals the sum of the \(q\) single-category probabilities plus \(O(k^{-2a})\). This proves the displayed constant.

Finally, for a positive integer-valued random variable with \(\Pr(T_+>k)\sim Ck^{-a}\), summation by parts yields the moment criterion for every \(s>0\): \(\mathbb E[T_+^s]<\infty\) if and only if \(\sum_{k\ge1} k^{s-1-a}<\infty\), equivalently \(s<a\). All constants are positive and finite under the hypotheses.

## Verification

A standalone standard-library Python checker `verify.py` evaluates all three completion probabilities in two independent ways: (i) their multivariate hypergeometric, multinomial, or Dirichlet-multinomial mass formulas, and (ii) direct forward count-vector recurrences with exact rational arithmetic. It also calculates finite-horizon single- and double-deficiency probabilities, and checks numerical behavior against the analytical leading constant. Execution reported **79** finite-horizon triples, **237** exact closed-form/recurrence comparisons, and **45** tail-consistency cases, all passed. These finite checks are not used as substitutes for the universal lemmas above.

As an explicit benchmark, \(q=3,a=2,r=2\) gives
\[
C_{3,2,2}=3\frac{\Gamma(6)}{\Gamma(4)}(1+2)=180.
\]

## Relationship to prior work

Jacobs (2021) describes the negative hypergeometric, negative multinomial and negative Pólya laws in a unified urn-and-tube framework and notes open questions about their multicolor moments. That work supplies the natural common setting, but the inspected sections do not state the all-horizon strict comparison or the sharp simultaneous-completion constant. Anceaume, Busnel, Schulte-Geers and Sericola (2015) prove important stochastic optimization statements **within independent sampling** for collecting distinct coupon types. Those do not directly compare the three sampling mechanisms or give the reinforced \(r\)-copy tail law. Henze and Holmes (2019) study individual-color waiting times under Pólya sampling and associated moment thresholds, which motivate but do not by themselves identify the joint multicolor completion-time leading coefficient. The balancing arguments and Dirichlet-multinomial calculations are given above explicitly to delineate what is proved here.

## Limitations

The result requires an initially balanced finite urn, ordinary unit-step Pólya reinforcement, integer initial multiplicities and integer observation targets \(1\le r\le a\). It does not establish an ordering between all arbitrary unbalanced urns, different reinforcement strengths, a pathwise monotone coupling, or parameter-uniform large-\(k\) asymptotics. The comparison against indexed and inspected literature does not certify absolute historical novelty; a classical reformulation of some component may exist.

## References

1. Bart Jacobs, *Urns & Tubes* (first publicly posted 2021-10-05), arXiv:2110.02155, especially Sections 7 and 10. https://arxiv.org/abs/2110.02155
2. Emmanuelle Anceaume, Yann Busnel, Ernst Schulte-Geers, Bruno Sericola, *Optimization results for a generalized coupon collector problem* (2015), arXiv:1504.03878. https://arxiv.org/abs/1504.03878
3. Norbert Henze and Andrew Holmes, *Curiosities regarding waiting times in Pólya's urn model* (2019), arXiv:1911.01052. https://arxiv.org/abs/1911.01052
