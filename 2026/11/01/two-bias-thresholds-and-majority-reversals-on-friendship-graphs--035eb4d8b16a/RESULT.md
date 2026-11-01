# Two bias thresholds and majority reversals on friendship graphs

## Finding

Let \(F_n\) be the *friendship graph* consisting of \(n\ge1\) triangles sharing one central vertex and otherwise disjoint. Under simultaneous binary strict-neighbor majority with retention of the existing state at a tie, **every initial state is fixed after at most two updates**. At update one the center adopts the **initial global majority**; after update two it adopts the **final global majority**. The latter can differ from the former, and this occurs if and only if the first fixed state is reached at update two.

For independent unbiased starting opinions, let \(Q_n\) be the probability that the center changes at update one, \(P_n\) the probability that its eventual opinion differs from its starting opinion, and \(R_n\) the probability of a reversal of the global majority between the initial and final configurations. Then

\[
Q_n=\frac12\left(1-\frac{\binom{2n}{n}}{4^n}\right),
\]

\[
P_n=4^{-n}\left(\sum_{k=\lceil n/2\rceil}^{n}\binom nk 3^{n-k}-\mathbf1_{2\mid n}\binom n{n/2}\right),\qquad R_n=Q_n-P_n.
\]

In particular,

\[
R_n=\frac12-\frac{1}{2\sqrt{\pi n}}+O(n^{-3/2}).
\]

Thus **almost half of unbiased initial states reverse their global majority**, even though no periodic oscillation survives. The final-center-flip probability is exponentially small: with \(q=\sqrt3/2\),

\[
P_n\sim\sqrt{\frac{2}{\pi n}}q^n\begin{cases}3/2,&n\text{ even},\\ \sqrt3/2,&n\text{ odd}.\end{cases}
\]

The exact number of fixed configurations is
\[
2^n+\mathbf1_{2\mid n}\binom n{n/2}.
\]
The bound of two updates is attained if and only if \(n\ge3\).

A **bias phase diagram** holds as well. Fix the center initially at opinion \(0\); let all \(2n\) peripheral opinions independently equal \(1\) with probability \(p\in[0,1]\). Write \(Q_n(p)\) for the chance the center changes at update one and \(P_n(p)\) for the chance it eventually changes. There is an exact formula

\[
P_n(p)=\sum_{k=\lceil n/2\rceil}^{n}\binom nk p^{2k}(1-p^2)^{n-k}
-\mathbf1_{2\mid n}\binom n{n/2}[p(1-p)]^n.
\]

For fixed \(p\) away from the two thresholds, the pair \((Q_n(p),P_n(p))\) tends to \((0,0)\) when \(p<1/2\), to \((1,0)\) when \(1/2<p<1/\sqrt2\), and to \((1,1)\) when \(p>1/\sqrt2\). Hence the intermediate phase flips the center at the first update **and returns it to its initial opinion at the second update**, with probability tending to one. The two critical windows have matching Gaussian profiles. For each fixed real \(s\), with \(\Phi\) the standard normal distribution function,

\[
\begin{aligned}
Q_n\bigl(\tfrac12+s/\sqrt n\bigr)&\longrightarrow\Phi(2\sqrt2\,s),\\
P_n\bigl(\tfrac1{\sqrt2}+s/\sqrt n\bigr)&\longrightarrow\Phi(2\sqrt2\,s).
\end{aligned}
\]

## Assumptions and scope

The graph has a center \(c\) and labelled pairs \(\{u_i,v_i\}\), \(1\le i\le n\), with exactly the three edges \(cu_i\), \(cv_i\), and \(u_iv_i\) for each pair and no other edges. A vertex of degree \(d\) changes to opinion \(1\) when more than \(d/2\) of its neighbors have opinion \(1\), changes to \(0\) when fewer than \(d/2\) do, and otherwise retains its present opinion. All updates occur simultaneously. There are no self-loops, random tie-breaks, asynchronous steps, or interaction weights.

The deterministic statements hold for every integer \(n\ge1\) and every labelled initial state. Unbiased statements give exact probabilities under the uniform measure on \(\{0,1\}^{2n+1}\). In the biased statements the center is fixed initially at \(0\), and only peripheral states are independently \(\operatorname{Bernoulli}(p)\). For a center initially at \(1\), exchange the two opinions and replace \(p\) by \(1-p\). The word “majority” always refers to all \(2n+1\) vertices, so there is never a global tie.

## Proof

**1. Exact two-step reduction.** Let \(h\) be the initial center opinion. Classify each peripheral pair into three types relative to \(h\): \(a\) pairs have both opinions equal to \(h\), \(b\) pairs have both opposite to \(h\), and \(m=n-a-b\) pairs are mixed. Every monochrome peripheral pair is permanently frozen, since each vertex sees one agreeing and one possibly disagreeing neighbor. A mixed pair changes in one step to the monochrome pair with value \(h\): the endpoint opposite to \(h\) sees two disagreeing neighbors and flips, while the endpoint equal to \(h\) has a tie and stays. Hence after one update all peripheral pairs are monochrome, exactly \(b\) of them opposite to the original center. They never change again.

Initially, among the center's \(2n\) neighbors, the opposite and matching counts are respectively \(2b+m\) and \(2a+m\). Therefore the center changes at time one if and only if \(b>a\). The global initial majority is opposite to \(h\) under exactly the same condition, since the center itself supplies the one tie-breaking vote. Thus the center at time one equals the initial global majority.

At time two the center consults \(2b\) opposite and \(2(n-b)\) matching peripheral opinions. It ends opposite to \(h\) precisely when \(b>n/2\), or when \(b=n/2\) and \(b>a\) (equivalently, \(m>0\)); the latter case preserves the already flipped center on an exact peripheral tie. In every other case it ends at \(h\). The center is now compatible with the frozen peripheral majority, so the entire configuration is fixed from time two onward. The center at time two equals the global majority of that time, again because its own opinion breaks an equal peripheral split. Its time-one and time-two values disagree precisely when \(a<b<n/2\), which is exactly when the initial and final global majorities disagree. Since the peripheral pairs are frozen at time one, that event is also exactly first fixation at time two. It is realizable for \(n\ge3\) by taking \(a=0\), \(b=1\), \(m=n-1\), and impossible for \(n=1,2\).

**2. Exact unbiased distribution.** Conditional on either initial center opinion, the pairs have probabilities \(1/4\), \(1/4\), and \(1/2\) for types \(a,b,m\). The law of \(b\) is \(\operatorname{Binomial}(n,1/4)\). Symmetry gives \(\Pr(b>a)=[1-\Pr(a=b)]/2\). The diagonal probability is the constant coefficient of \((z+z^{-1}+2)^n/4^n\); using \(z+z^{-1}+2=z^{-1}(1+z)^2\) gives \(\Pr(a=b)=\binom{2n}{n}/4^n\). This proves \(Q_n\).

A permanent center flip occurs for \(b\ge\lceil n/2\rceil\), except when \(n\) is even and \(a=b=n/2\), because then all pairs are originally monochrome, no center flip occurs, and the frozen peripheral tie retains \(h\). The excluded configurations have conditional probability \(\binom n{n/2}/4^n\). This proves \(P_n\), and subtracting its event from the first-flip event gives \(R_n\). Fixed states have all peripheral pairs monochrome; for each assignment of pair opinions the center must match their strict majority, but either center value is permitted for an exact tie. This yields \(2^n+\mathbf1_{2\mid n}\binom n{n/2}\).

**3. Limit laws.** Stirling's formula gives \(\binom{2n}{n}4^{-n}=1/\sqrt{\pi n}+O(n^{-3/2})\). A binomial upper-tail estimate for parameter \(1/4\) shows that \(P_n\) decays exponentially, so the formula for \(R_n\) follows. For the sharper parity-dependent result, the first admissible binomial mass at \(\lceil n/2\rceil\) is asymptotic to \(\sqrt{2/(\pi n)}(\sqrt3/2)^n\) for even \(n\) and to \(\sqrt{2/(\pi n)}(\sqrt3/2)^n/\sqrt3\) for odd \(n\). Ratios of successive tail masses tend to \(1/3\) and are bounded by that value, so each tail is asymptotic to \(3/2\) times its first mass. The even excluded all-monochrome term is exponentially smaller. This proves the asserted coefficients.

**4. Biased threshold and crossover.** With the center initially \(0\), pair types have respective probabilities \((1-p)^2\), \(p^2\), and \(2p(1-p)\). Thus \(b\sim\operatorname{Binomial}(n,p^2)\), and the same permanent-flip criterion gives the exact formula for \(P_n(p)\). The correction for the all-monochrome tie equals \(\binom n{n/2}[p(1-p)]^n\). The first-flip criterion is \(b>a\). By the law of large numbers, the sign of \((b-a)/n\) is determined by \(p^2-(1-p)^2=2p-1\); the permanent-flip threshold is determined by \(p^2-1/2\). This proves the three open phases.

For \(p_n=1/2+s/\sqrt n\), each pair's signed contribution \(\mathbf1_{b}-\mathbf1_{a}\) has mean \(2p_n-1=2s/\sqrt n\) and variance tending to \(1/2\). The triangular-array central limit theorem therefore gives \(\Pr(b>a)\to\Phi(2\sqrt2\,s)\). For \(p_n=1/\sqrt2+s/\sqrt n\), the binomial success probability is \(p_n^2=1/2+\sqrt2 s/\sqrt n+O(n^{-1})\). Its centered binomial tail has the same standardized shift \(2\sqrt2 s\). The exceptional all-monochrome tie probability is exponentially small uniformly in a neighborhood of the threshold. This proves the second Gaussian window. Equality endpoints follow as \(s=0\), while degenerate \(p=0,1\) are covered by the exact formulas.

## Verification

Run `python3 verify.py` using the Python standard library. The verifier builds each friendship graph from its labelled edge set and independently evaluates the neighbor-majority update. It checks all \(174{,}760\) initial labelled states for \(1\le n\le8\), including two-step fixation, first-center/global-majority agreement, terminal-center/global-majority agreement, exact counts, and the equivalence between two-step entry and majority reversal. In another \(42\) cases, it checks the exact weighted formulas for independent peripheral Bernoulli laws against enumeration, for \(1\le n\le7\) and six rational parameter values. The recorded output is in `verification_output.txt`.

These finite tests support the explicit proof but do not replace the all-size combinatorial argument or the limiting-probability proofs. The normal approximations are analytic consequences of the central limit theorem and are not established by finite simulations alone.

## Relationship to prior work

Mossel, Neeman and Tamuz (arXiv:1207.0893, initially public 4 July 2012) study how repeated majority dynamics can fail to preserve aggregate information, and their Section 3.1 constructs a distinct nontransitive clique-based example with self-loops and a fixed-size core. That is the closest conceptual antecedent, but it neither contains the loopless friendship graph nor its two exact bias thresholds, its phase-reversal identity, or its finite-size Gaussian windows. Tamuz and Tessler (arXiv:1307.4035) analyze information retention and general temporal bounds, not this family. Benjamini and collaborators (arXiv:1405.2486) explain the general period-at-most-two theorem and prove results for infinite unimodular and random graphs; those do not imply a two-update fixed-point cutoff on this specific deterministic graph family. The classical Goles–Olivos result establishes eventual period at most two on finite symmetric threshold systems, not absence of two-cycles here. The present theorem does not claim these broad background principles as new.

## Limitations

The dynamics are deterministic and synchronous; random or asynchronous tie-breaking and other voting rules need not obey these formulas. Biased probability formulas condition on the starting center, unlike a model drawing its center from the same Bernoulli distribution (which can be handled by mixing the two conditional laws). The results do not identify statistical recovery from the complete final state; they address the terminal global majority and the center opinion. The originality comparison relies on inspected accessible sources and mathematical searches, not an exhaustive index of every historical preprint. Independent mathematical audit has not been performed.

## References

1. E. Mossel, J. Neeman, O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893, first submitted 2012-07-04, especially Section 3.1. https://arxiv.org/abs/1207.0893
2. O. Tamuz, R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, first submitted 2013-07-15, Sections 1.1–1.2 and 3.4. https://arxiv.org/abs/1307.4035
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, first submitted 2014-05-11, Sections 1–4. https://arxiv.org/abs/1405.2486
4. E. Goles, J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.
