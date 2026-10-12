# Sharp conductor of the eighteen-fold sixth-power golden-ratio Beatty sumset

## Finding

Let \(\varphi=(1+\sqrt5)/2\), let
\[B=\{\lfloor n\varphi^6\rfloor:n\in\mathbb Z_{\ge1}\},\]
and let \(18B=\{b_1+\cdots+b_{18}:b_i\in B\}\), with repetitions allowed. Then
\[\max(\mathbb Z_{\ge1}\setminus18B)=93041,\qquad c(18B)=93042.\]
Equivalently, \(93041\notin18B\), but every integer at least \(93042\) belongs to \(18B\). This proves the \(m=6\) instance of Conjecture 1 in Pongsriiam (2022), which had established the upper bound for all even \(m\ge4\).

## Assumptions and scope

All Beatty indices and all eighteen summands use *positive* integers. There is no zero element added to \(B\), and the sumset has *exactly* eighteen terms (not at most eighteen). Define
\[\lambda=\varphi^6=9+4\sqrt5,\qquad \theta=18-\lambda=9-4\sqrt5.\]
Thus \(17<\lambda<18\) and \(0<\theta<1\). All floor and ceiling conventions are their usual real-number definitions. The conductor is the smallest integer \(c\) such that every integer \(t\ge c\) lies in \(18B\), and the Frobenius number here denotes the greatest positive integer outside \(18B\) (the conventions of the cited paper). We rely on its already-proved global upper bound and prove the missing *sharp nonmembership* independently.

## Proof

**1. Previously proved global coverage.** By Theorem 4.3 of Pongsriiam (2022), for any even integer \(m\ge4\), with \(h=\lfloor\varphi^m\rfloor\), every integer at least
\[h^4+2h^3-h^2-h+1\]
lies in the \((h+1)\)-fold sumset of \(B(\varphi^m)\). Take \(m=6\), for which \(h=17\). The threshold becomes
\[17^4+2\cdot17^3-17^2-17+1=93042.\]
It therefore remains to prove that \(93041\notin18B\).

**2. Restriction to two index totals.** Suppose to the contrary that positive integers \(n_1,\dots,n_{18}\) satisfy
\[93041=\sum_{i=1}^{18}\lfloor\lambda n_i\rfloor,\qquad N=\sum_{i=1}^{18}n_i.\]
The floor-of-a-sum identity implies
\[\lfloor\lambda N\rfloor-17\le \sum_{i=1}^{18}\lfloor\lambda n_i\rfloor\le\lfloor\lambda N\rfloor.\]
These bounds hold because the total of eighteen fractional parts is strictly less than eighteen, so its integer part is at most seventeen. Direct *exact* comparisons with \(\sqrt5\) give
\[\begin{aligned}
\lfloor5184\lambda\rfloor&=93023,\\
\lfloor5185\lambda\rfloor&=93041,\\
\lfloor5186\lambda\rfloor&=93058,\\
\lfloor5187\lambda\rfloor&=93076.
\end{aligned}\]
Since \(\lfloor\lambda N\rfloor\) increases with \(N\), we must have \(N=5185\) or \(N=5186\).

**3. Exact ceiling formula from a Pell approximant.** Observe that
\[2889^2-5\cdot1292^2=1\]
and hence
\[\delta:=\theta-\frac{18}{323}
=\frac{2889-1292\sqrt5}{323}
=\frac1{323(2889+1292\sqrt5)}.\]
In particular \(\delta>0\). Since \(2889+1292\sqrt5>2889+2\cdot1292=5473>5186\), we have
\[0<n\delta<\frac1{323}\qquad(1\le n\le5186).\]
The fractional part of \(18n/323\) is an integer multiple of \(1/323\). Therefore adding \(n\delta\) cannot cross the next integer boundary, except that a value *already* at an integer increases strictly above it. Thus for every such positive \(n\),
\[\lceil\theta n\rceil=\frac{18n+r(n)}{323},\qquad
r(n)=323-(18n\bmod323)\in\{1,\dots,323\},\]
where the remainder \(18n\bmod323\) is in \(\{0,\dots,322\}\). In particular, \(r(n)=323\) exactly when \(323\mid n\), because \(\gcd(18,323)=1\). And because \(18n\) is integral,
\[\lfloor\lambda n\rfloor=18n-\lceil\theta n\rceil.\]

**4. The two totals are both impossible.** Substitute this identity into the supposed representation. Each \(n_i\le N\le5186\), so the formula applies to all indices and yields
\[\sum_{i=1}^{18}r(n_i)=323(18N-93041)-18N.\]
For \(N=5185\) the right side is \(17\), impossible because all eighteen residues are positive.

For \(N=5186\) the right side is \(5813=18\cdot323-1\). Every residue is at most \(323\); hence precisely seventeen residues must equal \(323\) and the remaining residue must equal \(322\). Consequently seventeen indices are positive multiples of \(323\), so their sum is at least \(17\cdot323\). The remaining index \(n\) satisfies \(18n\equiv1\pmod{323}\). As \(18^2=324\equiv1\pmod{323}\), this forces \(n\equiv18\pmod{323}\) and \(n\ge18\). We conclude
\[N\ge17\cdot323+18=5509>5186,\]
a contradiction.

Thus \(93041\notin18B\). Along with the global coverage in Step 1 this proves that the last missing positive integer is exactly \(93041\) and the conductor exactly \(93042\). \(\square\)

## Verification

`verify.py` is a standalone Python 3 standard-library script. Run `python3 verify.py`; its reproduced output is in `verification_output.txt`. It uses exact integer square roots for Beatty values, checks the Pell identity and all ceiling-remainder identities up to the largest possible index, and performs an independent, *finite* eighteen-fold sumset membership scan for integers no greater than \(93041\). In particular, it confirms absence of \(93041\) by a second computational route. This finite scan is not a proof of eventual coverage; that infinite statement follows from the cited published theorem. The nonmembership proof itself is exact and does not depend on the scan.

## Relationship to prior work

Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio* (2022), Theorem 4.3 and Corollary 1, establishes a uniform upper bound and verifies sharpness for exponents up to \(5\); Conjecture 1 asserts sharpness for all higher exponents. The present theorem supplies the missing nonmembership argument for its first remaining even exponent, \(6\). It does not duplicate the published upper bound.

Shallit (2020/2022) determines sumsets for the lower and upper Wythoff sequences, which have generators \(\varphi\) and \(\varphi^2\), not \(\varphi^6\). Schaeffer, Shallit and Zorcic (arXiv:2402.08331, Section 7) prove an effective decidability result for additive-basis order in quadratic Beatty sequences, but provide no value of this eighteen-fold conductor. OEIS A004921 tabulates the underlying sixth-power Beatty sequence, not the exact eighteen-fold Frobenius number. These are substantive distinctions in objects and implications, rather than differences in terminology alone.

## Limitations

This proves only the \(m=6\) instance of the even-exponent conductor conjecture, not all higher exponents and not the separate conjecture on minimal basis order. The claimed novelty is relative to the literature inspected; unindexed results remain possible. The published global-coverage theorem is used as a cited premise, not reproved here. The finite verifier cannot replace that infinite premise.

## References

1. P. Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio*, Electronic Research Archive **30** (2022), 2385–2405, DOI: 10.3934/era.2022121, especially Theorem 4.3, Corollary 1, Conjecture 1. Full text: https://www.aimspress.com/aimspress-data/era/2022/7/PDF/era-30-07-121.pdf.
2. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond*, arXiv:2006.04177 (2020); Periodica Mathematica Hungarica **84** (2022), 37–46.
3. L. Schaeffer, J. Shallit, S. Zorcic, *Beatty Sequences for a Quadratic Irrational: Decidability and Applications*, arXiv:2402.08331, Section 7, Theorem 12.
4. OEIS Foundation, entry A004921, `floor(n*phi^6)`; https://oeis.org/A004921.
5. P. N. Phunphayap, P. Pongsriiam, J. Shallit, *Sumsets associated with Beatty sequences*, Discrete Mathematics **345** (2022), 112810, DOI: 10.1016/j.disc.2022.112810 (related two- and three-term Beatty sumsets).
