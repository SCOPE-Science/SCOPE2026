# Exact four-run distinct-subsequence spectrum and opposite-run balancing

## Finding
For positive integers \(a,b,c,d\), let \(w=0^a1^b0^c1^d\), of length \(n=a+b+c+d\), and let \(N(w)\) be the number of **distinct nonempty scattered subsequences** of \(w\), counting each output string once irrespective of the number of embeddings. Then
\[
N(w)=n+(a+c)(b+d)+bc(a+d)+abcd. \tag{1}
\]
The exact extremal problem at every length reduces to a *single* integer parameter, and the extremizers are balanced within opposite-run pairs. Put \(p=a+d\), \(q=b+c=n-p\), with \(2\le p\le n-2\). Define
\[
H_n(p)=n+\frac{n^2}{4}+\frac{p(n-p)^2(p+4)}{16}.
\]
For \(q=n-p\), define the correction
\[
D_n(p)=\begin{cases}
0,&p,q\text{ both even},\\
(p^2+q^2+4p-1)/16,&p,q\text{ both odd},\\
(p+2)^2/16,&p\text{ even},\ q\text{ odd},\\
(q^2+4)/16,&p\text{ odd},\ q\text{ even}.
\end{cases}
\]
Thus the exact maximum is
\[
M_4(n)=\max_{2\le p\le n-2}\bigl(H_n(p)-D_n(p)\bigr),\qquad n\ge4. \tag{2}
\]
For each value of \(p\), the maximizing quadruples are obtained by making \(a,d\) as equal as integrality allows and likewise \(b,c\); if both sums are odd, the two longer runs must be at corresponding ends (\(a>d\) if and only if \(b>c\)). This gives all maximizers from the maximizing indices in (2). In particular,
\[
M_4(n)=\frac{n^4}{256}+\frac{n^3}{32}+O(n^2). \tag{3}
\]
For any sequence of positive quadruples of lengths tending to infinity, \(N(w)/n^4\to1/256\) holds exactly when \((a,b,c,d)/n\to(1/4,1/4,1/4,1/4)\).

## Assumptions and scope
The alphabet is binary and exactly four nonempty alternating constant-letter runs occur. Complementing symbols does not change any count. Subsequences may omit arbitrarily many positions but preserve position order; the empty word is **excluded**. The four-run restriction is necessary: no global-unrestricted Fibonacci maximum is asserted. Formula (2) is an exact finite one-dimensional maximum, not a claimed residue-class closed form.

## Proof
First classify distinct nonempty subsequences by run pattern. Unary outputs contribute \(a+c\) words of the form \(0^i\) and \(b+d\) words of the form \(1^j\). A two-run output of type \(1^i0^j\) has \(1\le i\le b\), \(1\le j\le c\), contributing \(bc\). For the pattern \(0^i1^j\), one may use \(i\le a,j\le b+d\), or \(i\le a+c,j\le d\), producing two rectangles whose overlap has area \(ad\), hence \(ab+ad+cd\) distinct words. Three-run patterns \(0^i1^j0^k\) and \(1^i0^j1^k\) contribute \(abc\) and \(bcd\), respectively. Four-run pattern \(0^i1^j0^k1^\ell\) contributes \(abcd\). No output has more than four runs, and different patterns are disjoint. Summing yields (1).

For fixed \(p=a+d\) and \(q=b+c\), set \(u=a-d\), \(v=b-c\); then \(|u|\le p-2\), \(|v|\le q-2\), and \(u\equiv p\pmod2\), \(v\equiv q\pmod2\). Substitution in (1) yields the exact nonnegative deficit
\[
H_n(p)-N(w)=\frac{(u-v)^2}{4}+\frac{pv^2}{4}
+\frac{q^2u^2+(p^2-u^2)v^2}{16}. \tag{4}
\]
The right side is unchanged or decreased when the signs of \(u,v\) are made equal. For fixed \(\beta=|v|\), considered as a quadratic function of \(\alpha=|u|\ge0\), its real minimizer is
\[
\alpha_* =\frac{4\beta}{4+q^2-\beta^2}<1,
\]
because \(0\le\beta\le q-2\) and \(q\ge2\). Therefore, within the allowable parity class, \(\alpha\) is minimized at \(0\) if \(p\) is even and at \(1\) if \(p\) is odd; the minimizer is unique as an absolute value. Holding this minimized \(\alpha\le1\) fixed, the real minimizer in \(\beta\) is
\[
\beta_* =\frac{4\alpha}{4+4p+p^2-\alpha^2}<1.
\]
Thus \(\beta\) is uniquely minimized at \(0\) or \(1\) according to the parity of \(q\). When both parities are odd, the \((u-v)^2\) term forces matching signs. Substituting \(u,v\in\{0,\pm1\}\) gives exactly the four corrections in (2), proves the conditional equality classification, and proves (2) after maximizing over the finitely many choices of \(p\).

For (3), the polynomial \(H_n(p)\) has its unique interior continuous maximum at the positive zero of \(2p^2+(6-n)p-2n\), namely
\[
p_*=\frac{n-6+\sqrt{n^2+4n+36}}{4}
=\frac n2-1+O(n^{-1}).
\]
Its other critical point is the endpoint \(p=n\). Consequently, \(\max_{2\le p\le n-2}H_n(p)=n^4/256+n^3/32+O(n^2)\). The correction \(D_n(p)\) is nonnegative, giving the upper bound in (3). Choose four positive run lengths differing from \(n/4\) by bounded amounts, giving the matching lower bound with the same first two coefficients. Finally, (1) gives \(N(w)/n^4=(a/n)(b/n)(c/n)(d/n)+O(n^{-1})\) uniformly across all positive run lengths. The arithmetic-geometric mean inequality on four nonnegative proportions summing to one gives at most \(1/256\), with equality uniquely at the uniform quadruple. Compactness of the simplex proves the asserted if-and-only-if limiting rigidity.

## Verification
The accompanying standalone `verify.py` independently counts distinct subsequences by a last-occurrence dynamic program, tests (1) across a parameter grid, and compares (2) and its equality classification with exhaustive run compositions at small lengths. The infinite claims are justified by the algebra above, not by finite experiments. Execute `python verify.py` with Python 3, without external dependencies.

## Relationship to prior work
Flaxman, Harrow and Sorkin (2004) solve the *unrestricted* maximum number of distinct subsequences, attained by the alternating word with exponentially many outputs. They do not optimize among four-run words. Biers-Ariel, Godbole and Kelley (arXiv first submitted April 28, 2017; journal 2018) study *expected* distinct-subsequence counts for random word models, not the exact four-run extremal spectrum. The present finite-parameter identity, opposite-run balancing and one-dimensional conditional maximum are not consequences of their stated optimization and expectation results without further calculation. Searches of relevant current indexed mathematical records did not identify an exact equivalent four-run statement; lack of a hit is not a uniqueness proof.

## Limitations
The result does not resolve unrestricted or variable-run extrema, nor provide a closed expression for which index \(p\) maximizes (2) in each residue class. The O-term in (3) is uniform but no explicit sharp quadratic correction is claimed. Equivalent elementary derivations or unindexed restricted-run results may exist. Independent validation has not been performed.

## References
- Abraham Flaxman, Aram W. Harrow, Gregory B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics 11 (2004), R8, DOI:10.37236/1761. Full primary paper inspected.
- Yonah Biers-Ariel, Anant Godbole, Elizabeth Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, Discrete Mathematics & Theoretical Computer Science 19:2 (2018), article 10, arXiv:1704.08661, DOI:10.23638/DMTCS-19-2-10. Primary full text inspected.
