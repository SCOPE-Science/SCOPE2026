# Sharp quadratic loss of pivotal fairness under heterogeneous votes in the six-voter Icos rule

## Finding

Fix the six-voter Icos decision rule defined below. When independent voters have potentially different probabilities \(p_i\) of voting yes, the maximal difference between any two voters' pivotal probabilities across the box \([\alpha,1-\alpha]^6\) is **exactly** \((1-2\alpha)^2\), for every real \(0\le\alpha\le1/2\). This is an exact worst-case bound (not an asymptotic approximation). An explicit heterogeneous profile attains it for every \(\alpha\).

## Assumptions and scope

Let \(N=\{0,1,2,3,4,5\}\), and write triples by concatenated voter labels. The ten minimal winning three-voter coalitions are
\[
\mathcal T=\{012,013,024,035,045,125,134,145,234,235\}.
\]
The rule \(f:2^N\to\{0,1\}\) elects yes precisely when \(|S|\ge4\), or when \(|S|=3\) and \(S\in\mathcal T\). No set of size at most two wins. Each triple's complementary triple loses, and each voter belongs to exactly five winning triples; the rule is neutral, monotone, and treats all voters equally under a common Bernoulli voting probability.

Let voters' yes/no votes be independent with \(\Pr(X_j=1)=p_j\). For each voter \(i\), define the **absolute pivotal probability**
\[
\beta_i(\mathbf p)=\sum_{S\subseteq N\setminus\{i\}}
 (f(S\cup\{i\})-f(S))
 \prod_{j\in S}p_j\prod_{j\notin S,\,j\ne i}(1-p_j).
\]
This is an absolute influence, not a normalized share of total influence. It does not depend on \(p_i\). Define the disparity \(D(\mathbf p)=\max_i\beta_i(\mathbf p)-\min_i\beta_i(\mathbf p)\). All real \(0\le\alpha\le1/2\) and all six independent probabilities in the indicated closed box are included.

**Theorem.** For every such \(\alpha\),
\[
\max_{\mathbf p\in[\alpha,1-\alpha]^6}D(\mathbf p)=(1-2\alpha)^2.
\]
The upper endpoint is achieved when \(p_0=p_1=1-\alpha\), and \(p_2=p_3=p_4=p_5=\alpha\); specifically, \(\beta_2(\mathbf p)-\beta_4(\mathbf p)=(1-2\alpha)^2\).

## Proof

**Step 1 (reduce the continuous box to finitely many corners).** Put \(\delta=1-2\alpha\in[0,1]\). Each difference \(\beta_i-\beta_j\) is multiaffine separately in every coordinate \(p_h\): for fixed \(i\), the coordinate \(p_i\) is absent, and each of the other five appears in degree at most one. A real multiaffine function on a rectangular box attains its maximum and minimum at vertices, by repeatedly maximizing the affine dependence on one coordinate. Because
\(D(\mathbf p)=\max_{i<j}|\beta_i(\mathbf p)-\beta_j(\mathbf p)|\), it suffices to bound all \(15\) unordered pairs at the \(64\) corners \(p_h=(1+\varepsilon_h\delta)/2\), \(\varepsilon_h\in\{-1,+1\}\).

**Step 2 (exact corner polynomials).** At each corner, multiplying the pivotal probability formula by \(32\) gives
\[
32\beta_i=\sum_{S\subseteq N\setminus\{i\}}(f(S\cup\{i\})-f(S))
\prod_{h\in N\setminus\{i\}}\bigl(1+\varepsilon_h\delta(2\mathbf1_{\{h\in S\}}-1)\bigr).
\]
This is an integer-coefficient polynomial of degree at most five. Neutrality pairs each pivotal set \(S\) with the complementary subset of \(N\setminus\{i\}\), so all odd coefficients vanish. Evaluating at \(\delta=0\), each voter has \(10\) pivotal configurations among \(32\), hence \(32\beta_i=10+a_i\delta^2+b_i\delta^4\) with integer coefficients. The pivotal-count statement also follows directly from the listed ten triples (and is checked independently in the certificate).

For completeness, perform the finite exact expansion as follows. For each integer corner mask from \(0\) to \(63\), set \(\varepsilon_h=+1\) if bit \(h\) is present and \(-1\) otherwise; for each of the six voter indices, enumerate all \(32\) subsets of the remaining voters, retain precisely those satisfying \(f(S\cup\{i\})-f(S)=1\), and add the five-factor integer polynomials displayed above. Subtract the resulting polynomials for all \(15\) pairs. The following **complete coefficient census** records the number of corner/pair combinations with each value of \((\beta_i-\beta_j)/\delta^2\), as polynomial in \(\delta\):

| Signed quotient | Number of pairs/corners |
| --- | ---: |
| \(0\) | \(360\) |
| \(+1\), \(-1\) | \(150\) each |
| \(+(3+\delta^2)/4\), \(-(3+\delta^2)/4\) | \(60\) each |
| \(+(1-\delta^2)/2\), \(-(1-\delta^2)/2\) | \(30\) each |
| \(+(1-\delta^2)/4\), \(-(1-\delta^2)/4\) | \(60\) each |

The entries total \(64\cdot15=960\). The complete exhaustive arithmetic algorithm is included as the standalone, dependency-free file `icos_influence_certificate.py`; it constructs all coefficients with integer addition and multiplication, checks the nine classes and every multiplicity, and checks the exact witness. Thus this finite identity census is fully reproducible, and exhausts all parameter-independent corner cases rather than sampling parameters.

**Step 3 (sharp bound and attainment).** Since \(0\le\delta\le1\), all eight nonzero signed quotients in the table have absolute value at most one. Therefore \(|\beta_i-\beta_j|\le\delta^2\) at all corners, and Step 1 extends this inequality to every probability vector in the box. For the corner mask \(3\), meaning \(p_0=p_1=1-\alpha\) and all other probabilities equal \(\alpha\), the exact polynomial expansion gives \(32(\beta_2-\beta_4)=32\delta^2\). This attains the bound, proving equality. \(\square\)

## Verification

Run `python3 icos_influence_certificate.py` using Python 3 with no third-party packages. The certificate checks complementarity, monotonicity, five-fold triple incidence, \(64\cdot15=960\) symbolic integer polynomial comparisons, the complete coefficient-class histogram, and the attaining mask-\(3\) example. Verification uses symbolic polynomials represented by integer coefficient arrays, **not** floating-point parameter sampling. The short multiaffine-extrema lemma supplies the necessary passage from the finite symbolic certificate to the uncountable domain of probabilities.

## Relationship to prior work

Dhar, Mittal and Thomas (2026, arXiv:2602.13894, Section 2.2 and Figure 2) discuss Icos and the concept of fairness under a **common** Bernoulli bias \(p\); they show relationships between such unbiasedness and Banzhaf/Shapley–Shubik fairness. Loeb and Conway (2000) introduced and analyzed the Icos intersecting-family rule. Neither those credited constructions nor their stated common-bias fairness result is claimed as new here. The present statement instead determines the sharp **heterogeneous** product-measure disparity across an entire six-dimensional probability box. The full text of the 2026 preprint was inspected; only the abstract/metadata and secondary scholarly discussion of the 2000 paper could be accessed during this investigation, so older-priority risk remains.

## Limitations

The theorem is for the explicitly listed six-voter Icos rule and its relabelings, independently cast Bernoulli votes, and **absolute** (not normalized) pivotal probabilities. It does not assert that any other voting mechanism achieves the same robustness or that a probability-dependent optimal rule is Icos. It does not cover correlated votes. The finite coefficient census has a short, checkable ordinary Python implementation; the use of exhaustive exact finite algebra is essential to this proof, and is not an empirical substitute for the infinite-domain argument. A complete historical-priority guarantee is not asserted.

## References

1. Manik Dhar, Kunal Mittal and Clayton Thomas, *Existence of Fair Resolute Voting Rules*, first submitted February 14, 2026, arXiv:2602.13894v1. Full text: https://arxiv.org/html/2602.13894v1 ; bibliographic submission history: https://arxiv.org/abs/2602.13894 .
2. Daniel E. Loeb and Andrew R. Conway, *Voting Fairly: Transitive Maximal Intersecting Families of Sets*, Journal of Combinatorial Theory, Series A 91 (2000), 386–410, DOI:10.1006/jcta.2000.3103. (Bibliographic abstract examined; primary full text not accessible.)
3. Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014 (background on biased influences).
