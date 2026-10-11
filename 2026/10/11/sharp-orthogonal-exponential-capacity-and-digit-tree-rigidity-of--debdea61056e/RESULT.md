# Sharp orthogonal exponential capacity and digit-tree rigidity of prime-power modular hyperbolas

## Finding
Fix an odd prime \(p\) and an integer \(k\ge1\). Let \(R=\mathbb Z/p^k\mathbb Z\) and consider the hyperbola
\[
H=\{(x,x^{-1}):x\in R^\times\}\subset R^2,
\qquad |H|=(p-1)p^{k-1}.
\]
For every frequency \(\lambda=(a,b)\in R^2\), let \(e_\lambda:H\to\mathbb C\) be \(e_\lambda(x,x^{-1})=\exp(2\pi i(ax+bx^{-1})/p^k)\). Put the uniform counting inner product on \(\mathbb C^H\).

**Theorem.** The maximum cardinality of a pairwise orthogonal set of these restricted characters is exactly
\[
\max\{|\Lambda|:e_\lambda\perp e_\mu\text{ for distinct }\lambda,\mu\in\Lambda\}=p^{k-1}.
\]
In particular, no collection of restricted characters gives an orthogonal basis on \(H\).

There is also a complete **local digit-tree criterion**. For two distinct frequencies, let \(j\) be the first index where their base-\(p\) digit pairs differ (least-significant digits first), and let \((u,v)\in\mathbb F_p^2\setminus\{0\}\) be the difference of these first unequal digit pairs. Their restricted characters are orthogonal **if and only if** \(j\le k-2\) and the element \(uv\) is either zero or a quadratic nonsquare in \(\mathbb F_p\).

Thus an orthogonal set corresponds exactly to a finite rooted tree of frequency digit pairs: at every level before the final level, all distinct children at a node have differences \((u,v)\) for which \(uv\) is zero or a nonsquare; at the final level, a parent has at most one child. Every internal node has at most \(p\) children. The upper bound is attained exactly when all earlier internal nodes have \(p\) children and every final parent has one child. All such trees are permitted, without additional compatibility conditions between different parents.

## Assumptions and scope
The prime \(p\) is odd, the exponent \(k\) is any positive integer, and all frequencies are taken modulo \(p^k\) in each coordinate. Orthogonality is exact over \(\mathbb C\), not an approximate or asymptotic condition. Multiplying the inner product by any positive normalization constant changes no conclusion. The digit rule concerns the first coordinatewise pair that differs, not separate valuations of the two coordinate differences. The quadratic character \(\chi_p\) has values \(0,1,-1\), with \(\chi_p(0)=0\).

## Proof
**1. Precise Kloosterman zero criterion.** Write \(\zeta_m=\exp(2\pi i/p^m)\) and define
\[
K_m(a,b)=\sum_{x\in(\mathbb Z/p^m\mathbb Z)^\times}\zeta_m^{ax+bx^{-1}}.
\]
For a nonzero frequency difference \((a,b)\bmod p^k\), let \(j=\min(\nu_p(a),\nu_p(b),k)<k\), and write \(a=p^ja'\), \(b=p^jb'\), with \((a',b')\) primitive modulo \(p^{k-j}\). Lifting units shows
\[
K_k(a,b)=p^jK_{k-j}(a',b').
\tag{1}
\]
At modulus \(p\), \(K_1(a',b')\ne0\), for all coefficients. Indeed, if it vanished, the polynomial counting the frequencies of the exponents \(a'x+b'x^{-1}\) would be an integer multiple of \(\Phi_p(X)=1+X+\cdots+X^{p-1}\); all its \(p\) coefficients would be equal, contradicting their total \(p-1\).

For \(m\ge2\), suppose \((a',b')\) is primitive. In the sum over lifts \(x=y+p^{m-1}t\), \(t\bmod p\), the phase changes by the factor \(\exp(2\pi it(a'-b'y^{-2})/p)\). Thus each group of lifts cancels unless
\[
a'-b'y^{-2}\equiv0\pmod p.
\tag{2}
\]
Such a residue exists exactly when both coefficients are units and \(b'/a'\) is a square modulo \(p\), or equivalently \(\chi_p(a'b')=1\). Therefore \(K_m(a',b')=0\) whenever \(\chi_p(a'b')\in\{0,-1\}\).

Conversely assume \(\chi_p(a'b')=1\). Hensel lifting provides the two distinct roots \(\rho,-\rho\) of \(a'\rho^2=b'\pmod{p^m}\). Stationary-point expansion around these roots gives the following explicit evaluations. For \(m=2r\), \(r\ge1\),
\[
K_{2r}(a',b')=p^r\left(\zeta_{2r}^{2a'\rho}+\zeta_{2r}^{-2a'\rho}\right).
\tag{3}
\]
For \(m=2r+1\), \(r\ge1\), let \(c=a'\rho^{-1}\bmod p\) and \(G_p(c)=\sum_{t\bmod p}\exp(2\pi ict^2/p)\); then
\[
K_{2r+1}(a',b')=p^rG_p(c)\left(\zeta_{2r+1}^{2a'\rho}+\chi_p(-1)\zeta_{2r+1}^{-2a'\rho}\right).
\tag{4}
\]
To derive (3), partition \(x\) by its residue modulo \(p^r\). Only the two stationary classes survive, each with \(p^r\) equal phases. To derive (4), partition by residue modulo \(p^r\), write \(x=\rho+p^rt\) (respectively \(-\rho+p^rt\)), and use the Taylor identity \(a'x+b'x^{-1}\equiv\pm2a'\rho\pm(a'/\rho)p^{2r}t^2\pmod{p^{2r+1}}\). Each class contributes \(p^r\) copies of the indicated quadratic Gauss sum. The standard finite-field change of variables gives \(G_p(-c)=\chi_p(-1)G_p(c)\), while \(|G_p(c)|=\sqrt p\ne0\) for \(c\ne0\).

Neither (3) nor (4) vanishes. Indeed, cancellation would require \(\zeta_m^{4a'\rho}=-1\) in the even or plus case, or \(\zeta_m^{4a'\rho}=1\) in the minus case. The first is impossible because \(p^m\) is odd; the second is impossible because \(4a'\rho\) is a unit modulo \(p\). Combining these facts with (1) proves the claimed zero criterion:
\[
K_k(a,b)=0\quad\Longleftrightarrow\quad
j\le k-2\ \text{ and }\ \chi_p((a/p^j)(b/p^j))\in\{0,-1\}.
\tag{5}
\]
Here the quotient coordinates are reduced modulo \(p\), and equality (5) concerns nonzero \((a,b)\).

**2. Digit-tree structure.** The inner product between \(e_\lambda\) and \(e_\mu\) equals \(K_k(\lambda_1-\mu_1,\lambda_2-\mu_2)\) up to a nonzero scalar. Thus (5) is precisely the first-differing-digit criterion. Different child branches at a node first differ in their child digits, independent of later digits. Two frequencies below a common prefix at the last level first differ at valuation \(k-1\), so they cannot be orthogonal. Conversely, if every sibling pair at each earlier level satisfies (5) and each final prefix has at most one leaf, all pairs of distinct leaves are orthogonal. This establishes both necessity and sufficiency.

**3. Sharp upper bound and construction.** At any nonterminal prefix, let \(T\subseteq\mathbb F_p^2\) be its child-digit set. Suppose two distinct children \((u_1,v_1)\) and \((u_2,v_2)\) had the same difference \(v-u\). Then \(u_1-u_2=v_1-v_2\ne0\), and the product of their coordinate differences would be the nonzero square \((u_1-u_2)^2\). Such children are forbidden by (5). Hence the map \((u,v)\mapsto v-u\) is injective on \(T\), and \(|T|\le p\).

There are \(k-1\) nonterminal digit levels, followed by a final level with at most one leaf per parent. Thus every orthogonal frequency set has at most \(p^{k-1}\) members. This bound is attained by
\[
\Lambda_0=\{(j,0):0\le j<p^{k-1}\}\subset R^2,
\]
since for any two distinct members the first differing digit has product zero and occurs before the final digit. The equality conditions for the tree follow from equality in each bound. When \(k=1\), the prime-level nonvanishing argument forces just one frequency, consistent with the formula.

Finally \(|H|=(p-1)p^{k-1}>p^{k-1}\) because \(p\ge3\); a restricted exponential basis would require \(|H|\) orthogonal characters, so none exists. \(\square\)

## Verification
The standalone Python program `verify_hyperbola.py` performs exact cyclotomic-zero tests for the full coefficient array at ten moduli: \((p,k)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,2)\). It checks 40,746 frequency pairs, the sharp explicit orthogonal construction, and exhaustive compatible-digit \(p\)-point clique counts for \(p=3,5\) (27 and 120 respectively). No floating-point zero tests are used: cyclotomic vanishing is decided by divisibility by \(\Phi_{p^k}\) using integer coefficient blocks. The checker terminates with `VERIFY_OK`. These finite checks corroborate the unrestricted proof, rather than proving its infinite parameter range.

## Relationship to prior work
The evaluation of ordinary Kloosterman sums modulo odd prime powers is classical; the prime-power stationary-phase method and formulas underlying (3)–(4) are not claimed as new. Gurak (2009) explicitly credits Salié's earlier treatment, and studies more general prime-power Kloosterman sums. Iosevich–Murphy–Pakianathan (2014) treat Fourier coefficients and Salem behavior of hyperbolas over finite rings and the spectra of associated Cayley graphs. Haessig–Iosevich–Pakianathan–Robins–Vaicunas (2015) study Fourier and tiling questions over finite fields. The contribution assessed here is the **sharp maximum number of pairwise orthogonal restricted characters on the modular hyperbola for every odd prime power and the necessary-and-sufficient recursive digit-tree classification for all such character sets**, derived from but not identified in these prior statements.

## Limitations
Only odd prime-power residue rings and the standard unweighted modular hyperbola are considered; no extension to even characteristic, arbitrary local rings, or other curves is established. The digit-tree theorem gives an exact finite-field compatibility test at each node but does not provide a closed formula counting all compatible \(p\)-element child sets for arbitrary \(p\). Classical sources establish substantial parts of the Kloosterman analysis, and equivalent historical formulations of the new packing/classification statement cannot be ruled out without independent expert priority review. No independent mathematical audit has been performed.

## References
1. S. J. Gurak, *Kloosterman sums for prime powers in P-adic fields*, J. Théor. Nombres Bordeaux **21** (2009), 175–201. DOI: 10.5802/jtnb.665. Published online 2009-08-24.
2. A. Iosevich, B. Murphy, J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657 (first submitted 2014-05-29).
3. C. D. Haessig, A. Iosevich, J. Pakianathan, S. Robins, L. Vaicunas, *Tiling, circle packing and exponential sums over finite fields*, arXiv:1507.05861 (first submitted 2015-07-21).
4. H. Salié, *Über die Kloostermanschen Summen S(u,v;q)*, Math. Z. **34** (1932), 91–109 (historical formula, as credited by Gurak).
