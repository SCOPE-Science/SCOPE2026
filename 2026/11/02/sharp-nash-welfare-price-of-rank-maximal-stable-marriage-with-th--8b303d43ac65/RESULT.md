# Sharp Nash-welfare price of rank-maximal stable marriage with three pairs

## Finding

For the complete strict balanced Stable Marriage problem with \(n\) agents on each side, write \(p_r(M)\) for the number of all \(2n\) agents who receive their rank-\(r\) partner in a perfect matching \(M\). A **rank-maximal** stable matching lexicographically maximizes \((p_1(M),\ldots,p_n(M))\) over stable matchings. Each agent receiving rank \(r\) has positive utility \(u_r=n+1-r\). Define the Nash product
\[
P(M)=\prod_{r=1}^n (n+1-r)^{p_r(M)},\qquad
P_*(I)=\max_{M\text{ stable}} P(M).
\]
All rank-maximal matchings have the same rank profile and thus the same product, denoted \(P_R(I)\). The **Nash price of rank-maximality** is \(\rho(I)=P_*(I)/P_R(I)\).

For every \(n=2\) profile, \(\rho(I)=1\). For all \(n=3\) complete strict profiles, the exact range and distribution are:

| \(\rho(I)\) | Number of labeled profiles |
|---:|---:|
| \(1\) | \(42{,}756\) |
| \(4/3\) | \(2{,}484\) |
| \(16/9\) | \(432\) |
| \(64/27\) | \(12\) |
| \(8/3\) | \(828\) |
| \(32/9\) | \(72\) |
| \(16/3\) | \(72\) |

Hence \(\max_I\rho(I)=16/3\). This is a **product** ratio; for the geometric-mean Nash welfare of six agents the worst-case ratio is \((16/3)^{1/6}\). For exactly \(42{,}756\) profiles the full Nash-maximizing and rank-maximal stable-matching sets coincide, and for the other \(3{,}900\) profiles they are disjoint. There are no profiles with overlapping but unequal optimizer sets.

## Assumptions and scope

Both sides have the same cardinality and every agent strictly ranks every opposite-side agent, preferring any partner to remaining unmatched. All stable outcomes are perfect pairings, with a blocking pair defined by simultaneous strict improvement for its two agents. The rank profile combines **both** sides, not only one side. The ratio is calculated against the best Nash product among stable outcomes, not among arbitrary perfect matchings. All probabilities quoted are exact frequencies under six independent uniform strict preference orders when \(n=3\).

## Proof

At \(n=2\), every utility lies in \(\{1,2\}\); consequently, for every matching \(P(M)=2^{p_1(M)}\). Since \(p_1+p_2=4\), maximizing \(p_1\) lexicographically is precisely maximizing the product. This proves \(\rho=1\) without enumeration; enumeration independently confirms all \(2^4=16\) instances.

For \(n=3\), the proof is the following complete finite exhaustive argument, with standalone integer implementations. There are exactly \((3!)^{6}=46{,}656\) labeled complete strict preference profiles. For each profile, enumerate the \(3!=6\) bijections \(M\) from men to women. Retain precisely the matchings for which there is no unmatched pair \((m,w)\) satisfying both \(r_m(w)<r_m(M(m))\) and \(r_w(m)<r_w(M(w))\). For every retained matching, calculate its six exact integer partner ranks and the profile \((p_1,p_2,p_3)\). Its exact positive product is \(3^{p_1}2^{p_2}\). Choose the lexicographic maximum rank profile and the largest product. The former determines \(P_R\) uniquely even when multiple rank-maximal matchings exist. Record their exact rational ratio.

The exhaustive certificate yields \(34{,}080\) instances with one stable matching, \(11{,}484\) with two, and \(1{,}092\) with three, totaling \(46{,}656\) instances. Their seven product-ratio cell counts are the table in the Finding section; each is obtained by exact integer arithmetic and reduced rational comparison. Comparing *sets of matchings*, not just scores, gives \(42{,}756\) identical and \(3{,}900\) disjoint optimum-set profiles, with zero partially overlapping instances.

A witness attaining the upper bound has preference orders:

| Agent | Preference list, best first |
|---|---|
| \(m_1\) | \(w_1,w_2,w_3\) |
| \(m_2\) | \(w_1,w_3,w_2\) |
| \(m_3\) | \(w_2,w_3,w_1\) |
| \(w_1\) | \(m_3,m_1,m_2\) |
| \(w_2\) | \(m_2,m_3,m_1\) |
| \(w_3\) | \(m_1,m_2,m_3\) |

Checking all six permutations gives **exactly two stable matchings**. The Nash-optimal one is \(M_N=\{(m_1,w_1),(m_2,w_3),(m_3,w_2)\}\), with profile \((2,4,0)\) and Nash product \(P(M_N)=3^2 2^4=144\). The rank-maximal one is \(M_R=\{(m_1,w_3),(m_2,w_2),(m_3,w_1)\}\), with profile \((3,0,3)\) and product \(P(M_R)=3^3=27\). Therefore \(\rho=144/27=16/3\), proving sharpness rather than merely an upper bound.

## Verification

Both files `verify_rank_price.py` and `verify_rank_price_alt.py` are complete standard-library-only programs. The first enumerates tuples of the six strict rankings and all six perfect matchings, checking blocking pairs with rank matrices and computing complete optimizer sets. The second independently indexes all profiles in base six and constructs additive rank-count vectors and multiplicative welfare **edge by edge** before enumerating stable pairings. Both were executed from the current package inputs and produced all seven exact cells and the identical/disjoint dichotomy. The first also checks all two-pair profiles and the explicit worst-case witness.

Commands:

```text
python3 verify_rank_price.py
python3 verify_rank_price_alt.py
```

The complete domain is finite; the exhaustive test is the finite proof because every possible preference input and every matching is included. The certificate does **not** test, or establish, the claimed ratio for larger markets.

## Relationship to prior work

Cooper and Manlove develop rank-maximal stable matchings as a lexicographic profile objective and give algorithms for finding them. Desai, Rasheed M, Ghalme, and Gujar develop rank-induced Nash welfare maximization over stable marriages and compare it experimentally with several standard fairness criteria. Neither inspected primary paper gives the sharp price of rank-maximality, the seven-atom three-pair ratio distribution, or the complete Nash-versus-rank-maximal optimizer-set dichotomy.

A separate publicly available three-pair classification of rank-maximal versus **egalitarian** stable matchings counts \(42{,}756\) equal, \(2{,}928\) strictly nested, and \(972\) disjoint optimizer-set profiles; that result concerns an **additive rank-sum** objective. The present product ratio \(16/3\) and its frequencies require evaluating the multiplicative utilities of both competing optimal sets; no prior count by itself establishes this product loss. A previously known three-pair Nash-versus-egalitarian inclusion result is also distinct from the price of the lexicographic rank-maximal rule.

## Limitations

The theorem applies only to strict, complete, balanced one-to-one stable marriage, with the specified positive rank utility \(u_r=n+1-r\). It does not cover incomplete preferences, ties, alternative cardinalizations, or arbitrary larger sizes. The finite proof is exact and complete, but the originality comparison cannot exclude unindexed studies or supplementary computations. Self-review is not independent external validation.

## References

1. P. Desai, Rasheed M, G. Ghalme, and S. Gujar, *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354v1, first public 2 September 2026, https://arxiv.org/abs/2609.02354.
2. F. Cooper and D. Manlove, *Two-sided profile-based optimality in the stable marriage problem*, arXiv:1905.06626, first public 16 May 2019, https://arxiv.org/abs/1905.06626.
3. R. W. Irving, P. Leather, and D. Gusfield, *An efficient algorithm for the “optimal” stable marriage*, *Journal of the ACM* 34(3) (1987), 532–543, https://doi.org/10.1145/28869.28871.
