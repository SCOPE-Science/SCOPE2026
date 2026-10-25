# Logarithmic second-order depletion of three-point Abelian pattern Sturmian prefixes

## Finding
Let \(\mathcal T_N\) be the number of triples of integers \(0\le a<b<c\le N\) that occur as the **first three** positions of the sparse letter in an infinite binary Abelian pattern Sturmian word. Then, as the integer \(N\) tends to infinity,
\[
\boxed{\mathcal T_N=\frac{N^3}{12}-\frac{3}{2\pi^2}N^2\log N+O(N^2).}
\]
Equivalently, among all \(\binom{N+1}{3}\) increasing triples, the extendible proportion is
\[
\boxed{\frac{\mathcal T_N}{\binom{N+1}{3}}=\frac12-\frac9{\pi^2}\frac{\log N}{N}+O(N^{-1}).}
\]
There is also an exact finite formula, valid for every integer \(N\ge2\):
\[
\boxed{\mathcal T_N=\sum_{\substack{x,y\ge1\\x+y\le N}}\max\bigl\{0,\min(N-x-y+1,\,y-\gcd(x,y))\bigr\}.}
\]
The already-known two-distance Toeplitz forest criterion yields the underlying characterization: a triple is extendible if and only if \(c>a+b+\gcd(b-a,c-b)\). The new claim here is the **sharp two-term asymptotic enumeration** of all such extendible prefixes, not the Toeplitz graph criterion.

## Assumptions and scope
A two-sided bipartite sum-incidence graph \(\Gamma_D\) has one left and one right copy of \(\mathbb N_0\); its edges join \(L_i\) to \(R_j\) exactly when \(i+j\in D\). The forest characterization of Zeng, Xue and Zeng (2026) says that a sparse binary support \(D\subset\mathbb N_0\) produces an Abelian pattern Sturmian word precisely when \(\Gamma_D\) is acyclic. We count triples that can be the **first three** support elements, not arbitrary three-element subsets of a larger support. Only three-point prefix extendibility is counted; no census of full infinite words is asserted.

The classical Toeplitz graph \(T_n(A,B)\), for \(1\le B<A<n\), is the undirected graph with vertex set \(\{0,\ldots,n-1\}\) and edges at separations \(A\) or \(B\). Its established forest criterion is \(n\le A+B-\gcd(A,B)\); see the 2013 reference below. We use this published theorem as a premise rather than claim it as original.

## Proof
**Step 1: exact three-point forest condition.** Suppose \(0\le a<b<c\). Restrict \(\Gamma_{\{a,b,c\}}\) to the vertices with labels at most \(c\); all its edges occur there. The edges \(L_iR_{c-i}\), for \(0\le i\le c\), form a perfect matching. Contract them. The edges at sum \(a\) become edges joining positions separated by \(A=c-a\), and those at sum \(b\) become edges at separation \(B=c-b\). The resulting simple graph is \(T_{c+1}(A,B)\). Edge contraction of this perfect matching preserves the presence or absence of cycles (in this setting no loops or coincident parallel edges arise, because \(0\le a<b<c\)). The established Toeplitz criterion gives
\[
\Gamma_{\{a,b,c\}}\text{ forest}
\iff c+1\le( c-a)+(c-b)-\gcd(c-a,c-b)
\iff c>a+b+\gcd(b-a,c-b).
\]
A cyclic finite prefix cannot be repaired by adding edges. Conversely, if the three-sum graph is a forest, choose all later support positions successively more than twice the preceding maximum. At each such addition, every new edge has at most one endpoint in the previously occupied finite square, and the new-edge matching is disjoint; therefore no cycle can be created. Thus every forest triple extends to an infinite forest support and hence to an Abelian pattern Sturmian word. The extension can be constructed with positions \(d_{j+1}>2d_j\).

**Step 2: exact count.** Put \(x=b-a\ge1\) and \(y=c-b\ge1\). The inequality in Step 1 becomes \(a<y-\gcd(x,y)\), while \(c\le N\) means \(a\le N-x-y\). The possible nonnegative \(a\)'s are counted exactly by \(\max\{0,\min(N-x-y+1,y-\gcd(x,y))\}\). Summing over \(x,y\ge1\) gives the finite formula.

**Step 3: the cubic term.** Ignore the greatest-common-divisor restriction temporarily, and set
\[
Q_N=\sum_{\substack{x,y\ge1\\x+y\le N}}\min(N-x-y+1,y).
\]
It counts integer points \(a,x,y\) satisfying \(a\ge0\), \(x,y\ge1\), \(a+x+y\le N\) and \(a<y\). Its unit-scale limiting region has volume
\[
\int_0^1\int_0^{1-y}\min(y,1-x-y)\,dx\,dy=\frac1{12}.
\]
Equivalently, use a standard grid-cube boundary estimate for this rational polytope to get \(Q_N=N^3/12+O(N^2)\).

**Step 4: isolate the logarithmic gcd deficit.** Write \(g=\gcd(x,y)\) and \(h=N-x-y+1\). The pointwise difference \(\min(h,y)-\max\{0,\min(h,y-g)\}\) equals \(g\) whenever \(h\ge y\), i.e. \(x+2y\le N+1\). Else it is between zero and \(g\), and can be nonzero only if \(N+1<x+2y<N+1+g\). This remaining boundary strip contributes only \(O(N^2)\): write \(x=du\), \(y=dv\) with \(\gcd(u,v)=1\), so \(d=g\). The displayed strip forces the positive integer \(u+2v\) into an interval of length one, containing at most one integer. For each \(d\le N\), that integer has \(O(N/d+1)\) positive solutions \((u,v)\); each contributes at most \(d\). Summing \(O(N+d)\) over \(d\le N\) gives \(O(N^2)\). Therefore
\[
Q_N-\mathcal T_N=\sum_{\substack{x,y\ge1\\x+2y\le N+1}}\gcd(x,y)+O(N^2).
\]

**Step 5: the totient logarithm.** Euler's identity \(\gcd(x,y)=\sum_{d\mid x,\,d\mid y}\varphi(d)\) and the exact lattice-point count
\[
M(t)=\#\{u,v\ge1:u+2v\le t\}=\left\lfloor\frac{(t-1)^2}{4}\right\rfloor=\frac{t^2}{4}+O(t)
\]
give
\[
Q_N-\mathcal T_N
=\sum_{d\le N}\varphi(d)M(\lfloor(N+1)/d\rfloor)+O(N^2)
=\frac{N^2}{4}\sum_{d\le N}\frac{\varphi(d)}{d^2}+O(N^2).
\]
The error is \(O(N^2)\), using \(\varphi(d)\le d\) and \(\sum_{d\le N}\varphi(d)/d\le N\). Finally, from \(\varphi(d)=d\sum_{r\mid d}\mu(r)/r\) and the convergent Euler product \(\sum_{r\ge1}\mu(r)/r^2=6/\pi^2\),
\[
\sum_{d\le N}\frac{\varphi(d)}{d^2}=\frac6{\pi^2}\log N+O(1).
\]
Combining Steps 3–5 proves \(\mathcal T_N=N^3/12-(3/(2\pi^2))N^2\log N+O(N^2)\). Dividing by \(\binom{N+1}{3}=N^3/6+O(N^2)\) gives the proportion formula.

## Verification
Run `python3 verify.py` with Python 3 standard library. The checker independently builds the bipartite graph and tests the forest equivalence on finite parameter boxes; it separately compares the exact counting formula with direct enumeration; it evaluates the gcd/totient floor-sum identity and checks the predicted scale numerically. These experiments do **not** prove the infinite asymptotic; the above graph contraction and number-theoretic argument do. The 2013 Toeplitz forest criterion and the 2026 Abelian-pattern forest equivalence are cited external premises.

## Relationship to prior work
The characterization of Abelian pattern Sturmian supports as incidence forests is due to Zeng, Xue and Zeng (2026). The finite Toeplitz two-distance forest threshold is already established in *Bipartite finite Toeplitz graphs* (2013), and covers the arithmetic **three-point criterion** through the contraction used above; we do not claim that criterion as new. A previously published sharp logarithmic support-envelope result derives exponential occurrence-position bounds and identifies the extremal support \(\{2^j-1\}\); it does not count how frequently arbitrary triples are extendible. The contribution assessed here is the two-term prevalence asymptotic with its explicit \(N^2\log N\) correction.

## Limitations
The formula concerns Abelian pattern Sturmian **three-point prefixes** only, not arbitrary subsets or longer prefixes. The proof depends on cited graph and symbolic equivalences; their original full texts were not all accessible during this study. The 2026 source's bibliographic data, abstract and a separately published detailed mathematical statement were consulted, but not the entire 2026 paper; the 2013 Toeplitz criterion was compared at the theorem-statement level. An unnoticed published higher-order enumeration or an equivalent analytic-counting argument could compromise priority, so historical originality is not independently certified. The self-review analytical review and independent external audit are different processes; no independent audit has been performed.

## References
1. Qingcheng Zeng, Yumei Xue, Cheng Zeng, “Abelian maximal pattern complexity and extremal words,” arXiv:2609.28059v1 (first public 2026-09-23); incidence-forest characterization and strict-doubling extension principle.
2. “Bipartite finite Toeplitz graphs,” *Discrete Applied Mathematics* (2013), DOI 10.1016/j.dam.2013.05.020; classical two-distance forest criterion.
3. “Sharp logarithmic support envelope for Abelian pattern Sturmian words,” mathematical research record (2026), identifier `2026/10/4/SCOPE-sharp-logarithmic-support-envelope-for-abelian-pattern-sturmian--71c60228ce20`; exact support envelope and Mersenne extremal example.
4. Classical elementary results: gcd divisor-sum identity for Euler's totient, and Dirichlet-series evaluation \(\sum_{n\ge1}\mu(n)/n^2=6/\pi^2\).
