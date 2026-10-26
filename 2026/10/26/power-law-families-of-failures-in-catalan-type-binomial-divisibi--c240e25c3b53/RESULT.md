# Power-law families of failures in Catalan-type binomial divisibility

## Finding
Let \(a,b\) be positive integers and let \(p\) be a prime with \(p\mid a\) and \(p\nmid b\). Put \(m=a+b\), let \(s\ge1\) be the multiplicative order of \(p\) modulo \(m\), and set
\[
q=p^s,\qquad w=(q-1)/m,\qquad \delta=\frac{\log 2}{s\log p}.
\]
For every \(r\ge1\), the \(2^{r-1}\) distinct integers
\[
n=w\left(1+\sum_{j=1}^{r-1}\varepsilon_j q^j\right),\qquad \varepsilon_j\in\{0,1\},
\]
satisfy \(1\le n<q^r\) and
\[
p\mid bn+1,\qquad p\nmid\binom{(a+b)n}{an}.
\]
In particular, for the counting function
\[
E_{a,b}(X)=\#\left\{1\le n<X:(bn+1)\nmid\binom{(a+b)n}{an}\right\},
\]
one has, for all \(X\ge q\),
\[
E_{a,b}(X)\ge 2^{\lfloor\log_q X\rfloor-1}\gg_{a,b,p}X^\delta.
\]
The \(p\)-adic closure of this *explicit witness subfamily* is the self-similar set
\[
\mathcal C=w\left(1+\sum_{j\ge1}\varepsilon_j p^{sj}\right)\subseteq\mathbb Z_p,
\qquad \dim_H\mathcal C=\delta.
\]
The dimension assertion concerns the constructed subfamily, not the entire exception set.

## Assumptions and scope
All variables \(a,b\) are strictly positive integers; \(p\) is prime; \(p\mid a\) and \(p\nmid b\). Thus \(\gcd(p,m)=1\), and \(s\) exists. The convention \(\binom{N}{K}\) is the ordinary integer binomial coefficient for \(0\le K\le N\). The constant implicit in \(\gg\) may depend on \(a,b,p\). The \(p\)-adic dimension uses the metric \(|x-y|_p=p^{-\nu_p(x-y)}\).

## Proof
**Base block.** By definition, \(mw=q-1\), so \(1\le w<q\). Since \(p\mid a\), reduction modulo \(p\) gives \(b\equiv m\) and \(bw\equiv mw\equiv-1\pmod p\). Because \(mw=p^s-1\) has precisely \(s\) base-\(p\) digits equal to \(p-1\), Lucas's theorem gives
\[
\binom{mw}{aw}\equiv(-1)^{s_p(aw)}\pmod p,
\]
where \(s_p\) denotes base-\(p\) digit sum. This is a unit modulo \(p\).

**Independent blocks.** Let \(\varepsilon_0=1\). In base \(q=p^s\), the identity \(mw=q-1\) shows that
\[
mn=\sum_{j=0}^{r-1}\varepsilon_j(q-1)q^j,\qquad
an=\sum_{j=0}^{r-1}\varepsilon_j(aw)q^j.
\]
Each occupied block is strictly less than \(q\); therefore these expansions have no cross-block carries and correspond to \(s\)-digit base-\(p\) blocks. Lucas's theorem, applied digit by digit, gives
\[
\binom{mn}{an}\equiv\binom{mw}{aw}^{\sum_{j=0}^{r-1}\varepsilon_j}\not\equiv0\pmod p.
\]
As \(n\equiv w\pmod p\), also \(p\mid bn+1\). Therefore \(bn+1\) cannot divide the binomial coefficient. Distinct block choices give distinct integers and \(n<q^r\), proving the asserted finite count. Taking \(r=\lfloor\log_q X\rfloor\) proves the power-law lower bound for every \(X\ge q\).

**Dimension of the witness closure.** The closure of finite binary-block expansions is \(\mathcal C\) because the series converges \(p\)-adically and finite binary truncations are dense in all infinite choices. Multiplication by \(w\), a \(p\)-adic unit, and translation preserve distances. Each stage fixes one initial length-\(s\) block and allows two choices independently for each subsequent length-\(s\) block. At depth \(r\) the set is covered by \(2^{r-1}\) disjoint balls of radius \(p^{-sr}\). The usual covering estimate gives \(\dim_H\mathcal C\le\log2/(s\log p)\). Conversely the fair Bernoulli measure on the binary choices assigns each depth-\(r\) cylinder mass \(2^{-(r-1)}\); because cylinders of the same depth are disjoint \(p\)-adic balls, the mass-distribution estimate gives the reverse inequality.

## Verification
The accompanying standalone \(\texttt{verify.py}\) checks independently generated binary blocks for a range of \(a,b,p\), verifies exact Lucas residues and divisibility witnesses, checks noncollision and the finite-block cardinalities, and uses exact integer binomial coefficients where feasible. These finite checks corroborate rather than replace the proof.

## Relationship to prior work
Guo and Krattenthaler proved Sun's qualitative conjecture that if some prime divides \(a\) but not \(b\), there are infinitely many failures of \((bn+1)\mid\binom{(a+b)n}{an}\). Their Theorem 2.1 and its proof supply the seed \(w\) and one witness for each suitable exponent. The finding here instead uses *independent choices of entire Lucas blocks* to obtain a quantitative power-law lower bound and a positive-dimensional explicit \(p\)-adic witness subset. The earlier infinite-existence statement does not itself imply either quantitative conclusion.

## Limitations
No optimality is asserted for the exponent \(\delta\), no positive natural density is claimed, and no conclusion is drawn about the exact density or Hausdorff dimension of the *entire* set of failures. The argument applies when \(a\) has a prime factor absent from \(b\), not to every pair \(a,b\). General digital concatenation principles may be relevant to originality; this proof is a direct specialization with an explicit count and dimension.

## References
- Victor J. W. Guo and Christian Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651v1 (publicly posted 2013-01-31); Journal of Number Theory 135 (2014), 167–184. https://arxiv.org/abs/1301.7651 . Especially Theorem 2.1 and its proof in Section 4.
- Zhi-Wei Sun, *On divisibility of binomial coefficients*, Journal of the Australian Mathematical Society 93 (2012), 189–201; DOI:10.1017/S1446788712000171.
- Édouard Lucas, classical theorem on binomial coefficients modulo primes (1878), cited in Guo–Krattenthaler, Theorem 4.1.
