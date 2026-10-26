# A coprimality dichotomy and exact descent densities for three-generator denumerants

## Finding

For positive integers \(a,b,c\) with \(\gcd(a,b,c)=1\), define the three-generator denumerant
\[
P(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^{3}:ax+by+cz=n\},\qquad
\Delta(n)=P(n+1)-P(n).
\]
The following assertions hold, with *eventually* meaning for all sufficiently large integers \(n\).

**Rigidity.** If \(a,b,c\) are pairwise coprime, then \(\Delta(n)>0\) eventually. If every generator is at least \(2\) and at least one pair is not coprime, then both \(\Delta(n)<0\) and \(\Delta(n)>0\) occur on sets of strictly positive natural density. Thus for a primitive triple with all generators at least \(2\), the denumerant is eventually strictly increasing if and only if the generators are pairwise coprime.

**Explicit sign law.** Suppose exactly one pair, relabelled \((a,b)\), has \(d=\gcd(a,b)>1\), and \(a,b,c\ge2\). Let \(u\in\{1,\ldots,d-1\}\) be the inverse of \(c\) modulo \(d\). Then the eventual strict-descent and strict-ascent sets have exact natural densities
\[
\operatorname{dens}\{n:\Delta(n)<0\}=\frac{d-u}{d},\qquad
\operatorname{dens}\{n:\Delta(n)>0\}=\frac{u}{d}.
\]
There are no eventual ties. More specifically, for all sufficiently large \(n\), descent occurs exactly when \((un\bmod d)<d-u\).

**Several noncoprime pairs.** For each unordered pair \((v,w)\) among \((a,b),(a,c),(b,c)\) with \(d_{vw}=\gcd(v,w)>1\), denote the remaining generator by \(t\) and let \(u_{vw}\) be the inverse of \(t\) modulo \(d_{vw}\). The lower densities of descent and ascent satisfy respectively
\[
\underline{\operatorname{dens}}\{n:\Delta(n)<0\}\ge
 \prod_{d_{vw}>1}\frac{d_{vw}-u_{vw}}{d_{vw}},\qquad
\underline{\operatorname{dens}}\{n:\Delta(n)>0\}\ge
 \prod_{d_{vw}>1}\frac{u_{vw}}{d_{vw}}.
\]
Each displayed product is positive. In fact, both sign sets are eventually unions of residue classes modulo \(L=\operatorname{lcm}(a,b,c)\), so their natural densities exist. No assertion of equality in these product bounds is made when several pairs have nontrivial gcd.

**Unit-generator boundary.** If one generator equals \(1\), relabel it as \(a=1\) and put \(d=\gcd(b,c)\). Then \(\Delta(n)\ge0\) for all \(n\), and eventually the ascent density is \(1/d\) while the tie density is \(1-1/d\). In particular, no descents occur when a generator equals \(1\).

## Assumptions and scope

All generators and the target index are integers, with \(a,b,c\ge1\), \(n\ge0\), and \(\gcd(a,b,c)=1\). The three variables are labelled even if some generators coincide; the solutions are ordered triples. Natural density is the limit of the proportion of nonnegative integers in a sign set up to a growing cutoff. A lower density is its lower limiting proportion. The theorem does not concern triples with a common gcd greater than \(1\).

## Proof

Write
\[
F(z)=\sum_{n\ge0}P(n)z^n=\prod_{v\in\{a,b,c\}}(1-z^v)^{-1}.
\]
Let \(\mathcal E\) be the set of unordered generator pairs \((v,w)\) with \(d=\gcd(v,w)>1\), and write \(t\) for the remaining generator. Since the triple gcd equals \(1\), \(\gcd(t,d)=1\). Furthermore, the three nontrivial pair gcds are pairwise coprime: a prime dividing two of them would divide all three generators.

At \(z=1\), the rational function has a triple pole. Its contribution to \(P(n)\) is a quadratic polynomial whose coefficients of \(n^2\) and \(n\) are respectively \(1/(2abc)\) and \((a+b+c)/(2abc)\). At any other root of unity \(\zeta\), the pole has order at most two. The double poles are precisely the nonidentity \(d\)-th roots of unity for pairs in \(\mathcal E\); because the pair gcds are coprime, no such pole belongs to two different pairs.

For a fixed pair \((v,w;t)\), the leading Laurent term at \(\zeta^d=1\), \(\zeta\ne1\), is
\[
\frac1{vw(1-\zeta^t)}(1-z/\zeta)^{-2}.
\]
The coefficient of \(z^n\) in this Laurent term is \((n+1)\zeta^{-n}/[vw(1-\zeta^t)]\). All other contributions at these roots, as well as the simple-pole contributions, are periodic and bounded in \(n\) (with periods dividing \(L\)). Let \(u=t^{-1}\bmod d\) be represented in \(\{1,\dots,d-1\}\). The elementary finite Fourier identity
\[
\sum_{\substack{\xi^d=1\\\xi\ne1}}\frac{\xi^{-k}}{1-\xi}
 =\frac{d-1}{2}-(k\bmod d),\qquad k\in\mathbb Z,
\]
follows by taking the difference between successive \(k\), or by orthogonality; its value at \(k=0\) is \((d-1)/2\), using the substitution \(\xi\mapsto\xi^{-1}\). Thus for a bounded \(L\)-periodic function \(R(n)\),
\[
P(n)=\frac{n^2+(a+b+c)n}{2abc}
 +\sum_{(v,w;t)\in\mathcal E}\frac{n}{vw}
 \left(\frac{d-1}{2}-(un\bmod d)\right)+R(n).
\]
Here \(d=\gcd(v,w)\), and the displayed identity is exact for every \(n\ge0\); the quadratic term's additive constant is absorbed into \(R\).

Set \(k_{vw}(n)=un\bmod d\in\{0,\ldots,d-1\}\), and define
\[
\varepsilon_{vw}(n)=\begin{cases}
0,&k_{vw}(n)<d-u,\\
1,&k_{vw}(n)\ge d-u.
\end{cases}
\]
The difference of the sawtooth values at \(n+1\) and \(n\) is \(-u+d\varepsilon_{vw}(n)\). Taking first differences yields the **exact leading-slope formula**
\[
\boxed{\displaystyle
\Delta(n)=\frac{n}{abc}\left[1+
\sum_{(v,w;t)\in\mathcal E}
 t\bigl(-u_{vw}+d_{vw}\varepsilon_{vw}(n)\bigr)\right]+O_{a,b,c}(1).}
\]
The error is bounded and periodic. Because the bracket depends only on \(n\bmod L\), the sign on each residue class is eventually constant, including when its leading slope vanishes (then the periodic constant determines the sign). Consequently all three eventual sign sets have rational natural densities.

If \(\mathcal E\) is empty, the bracket equals \(1\), so \(\Delta(n)>0\) eventually. If \(\mathcal E\) is nonempty and every generator is at least \(2\), the Chinese remainder theorem allows all \(\varepsilon_{vw}\) to be independently prescribed, since the nontrivial pair gcds are pairwise coprime. On the residue classes where every \(\varepsilon\) vanishes, the bracket is \(1-\sum t u_{vw}<0\), as one summand is at least \(2\). On the classes where every \(\varepsilon\) equals \(1\), the bracket is \(1+\sum t(d-u_{vw})>0\). The fractions of residue classes of each type are exactly the two products displayed in the finding: for a modulus \(d\), there are \(d-u\) non-wrapping \(k\)-values and \(u\) wrapping values. Since the corresponding slopes are bounded away from zero, their signs hold for every sufficiently large target in these classes. This proves both lower-density bounds and the rigidity assertion.

When exactly one pair is noncoprime, the bracket is either \(1-tu<0\) or \(1+t(d-u)>0\). Therefore the two sets of residue classes exhaust all cases and have exact densities \((d-u)/d\) and \(u/d\), establishing the sign law and eventual absence of ties.

Finally, when \(a=1\), the generating functions satisfy
\[
(1-z)F(z)=\frac1{(1-z^b)(1-z^c)},
\]
so \(\Delta(n)=\#\{(y,z)\ge0:by+cz=n+1\}\) holds exactly. Such a representation is impossible unless \(d\mid n+1\), and exists for all sufficiently large multiples of \(d\), by the two-generator Frobenius theorem after dividing by \(d\). Hence exactly \(1/d\) of eventual indices give a strict ascent and the others give a tie. This proves all assertions. \(\square\)

## Verification

The accompanying stand-alone `verify.py` uses exact integer arithmetic. It enumerates coefficients of the generating function by three coin-change updates, separately computes the Laurent-pole slope bracket by modular inverses, and verifies that for each primitive triple tested and each residue class \(r\bmod L\),
\[
\Delta(r+5L)-\Delta(r+4L)=\frac{L}{abc}
\left[1+\sum_{(v,w;t)\in\mathcal E}t(-u_{vw}+d_{vw}\varepsilon_{vw}(r))\right].
\]
It also checks the predicted eventual sign sets for one-shared-pair examples, and the unit-generator boundary. These exhaustive finite-parameter checks test the critical formulas but are not substitutes for the pole proof, which covers all positive generators.

## Relationship to prior work

Aldrich, Gulbrandsen and Keddy (arXiv:2610.20899, first submitted 14 October 2026), study and bound counts of nonnegative solutions to three-term linear Diophantine equations; their Theorem C gives pointwise quasi-polynomial bounds. The present result instead classifies **changes between consecutive targets** and their sign densities. Baldoni et al. (arXiv:1312.7147, 2013) explain the general periodic-coefficient/pole machinery underlying denumerants, including double poles and pair-gcd data. Their coefficient algorithms can in principle recover relevant periodic slopes, but their inspected results do not state the coprimality rigidity or the modular-inverse formula for exact descent density. Liu and Xin (arXiv:2406.18955, 2024) provide efficient exact denumerant evaluation; this does not directly yield the present closed-form sign frequencies without further analysis. The contribution is a sharp qualitative and quantitative sign law, not a new general quasipolynomial algorithm.

## Limitations

No effective bound for the first index where each eventual sign pattern stabilizes is asserted. For several noncoprime pairs the two explicit products are rigorous **lower bounds**, not generally the exact sign densities; zero leading-slope residue classes may be decided by the periodic remainder. The proof uses standard complex rational-function partial fractions and a finite Fourier identity, rather than an independently formalized certificate. Previous algorithms for computing quasipolynomial coefficients may imply the sign law after additional analysis, and independent bibliographic priority checking remains appropriate.

## References

1. M. Aldrich, D. Gulbrandsen and C. Keddy, *Enumerating Integral Points on Triangles in \(\mathbb R^3\)*, arXiv:2610.20899 (first public version 14 October 2026), https://arxiv.org/abs/2610.20899 ; full text: https://arxiv.org/html/2610.20899v2 .
2. V. Baldoni, N. Berline, J. A. De Loera, B. E. Dutra, M. Köppe and M. Vergne, *Coefficients of Sylvester's Denumerant*, arXiv:1312.7147 (2013), https://arxiv.org/abs/1312.7147 .
3. F. Liu and G. Xin, *A Fast Algorithm for Denumerants with Three Variables*, arXiv:2406.18955 (2024), https://arxiv.org/html/2406.18955v1 .
4. F. Liu, G. Xin and C. Zhang, *Three Simple Reduction Formulas for the Denumerant Functions*, arXiv:2404.13989 (2024), https://arxiv.org/html/2404.13989v2 .
