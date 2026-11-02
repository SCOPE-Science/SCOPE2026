# A logarithmic correction in the enumeration of extendible three-one binary prefixes

## Finding
For an integer \(N\ge2\), let \(T(N)\) count binary words of length \(N+1\) containing exactly three \(1\)s that extend, without altering the prefix, to the characteristic word of an infinite set \(D\) whose incidence graph \(\Gamma_D\) is a forest. Such a word is a **normalized** Abelian pattern Sturmian word, with \(1\) designated as its sparse letter. Abelian pattern Sturmian has its established meaning: maximal Abelian pattern complexity at every pattern size \(k\) equals the least integer \(m\) satisfying \(\binom m2\ge k\).

If the three \(1\)-positions are \(0\le a<b<c\le N\), such an extension exists **if and only if**
\[
a<c-b-\gcd(c-b,b-a).
\]
Consequently, for every integer \(N\ge2\),
\[
T(N)=\sum_{\substack{x,y\ge1\\x+y\le N}}
\max\{0,\min\{x-\gcd(x,y),\,N-x-y+1\}\}.
\]
The main quantitative conclusion is the two-term asymptotic
\[
\boxed{T(N)=\frac{N^3}{12}-\frac{3}{2\pi^2}N^2\log N+O(N^2)}
\qquad(N\longrightarrow\infty).
\]
Equivalently, the fraction of all three-one words of length \(N+1\) that admit an Abelian pattern Sturmian extension is
\[
\frac{T(N)}{\binom{N+1}{3}}=\frac12-\frac9{\pi^2}\frac{\log N}{N}+O(N^{-1}).
\]
Moreover, for \(N\ge7\), the same \(T(N)\) counts **all** length-\(N+1\) three-one prefixes extendible to an Abelian pattern Sturmian word, even when the letters may be interchanged: the complement has \(N-2\) zeros, too many to be a Sidon support. The graph-theoretic threshold used in the classification is known; the enumerative correction is the distinct claim.

## Assumptions and scope
Indices are nonnegative integers, and \(\gcd\) is the positive greatest common divisor. An infinite binary word is required to agree with the entire specified prefix of length \(N+1\), not merely contain its three nonzero positions. The support of a normalized infinite word is its set of positions occupied by \(1\). The normalization is essential at small lengths, because interchanging \(0\) and \(1\) preserves Abelian pattern complexity; the exact formula for \(N\ge2\) counts the normalized class, and the equality with the unrestricted class is proved for \(N\ge7\).

For a set \(D\subseteq\mathbb N_0\), let \(\Gamma_D\) be the bipartite graph on disjoint left and right copies of \(\mathbb N_0\), joining \(\mathrm L_i\) to \(\mathrm R_j\) exactly when \(i+j\in D\). The published incidence-graph characterization states that the characteristic word of an infinite set \(D\) is Abelian pattern Sturmian when \(\Gamma_D\) is a forest, and every Abelian pattern Sturmian word is of this form after a possible exchange of letters. All asymptotic constants are absolute.

## Proof
**1. From a three-point support to a two-distance graph.** Fix \(D_0=\{a,b,c\}\), where \(0\le a<b<c\). All its nonisolated incidence vertices lie among \(\mathrm L_0,\ldots,\mathrm L_c\) and \(\mathrm R_0,\ldots,\mathrm R_c\). The \(c+1\) edges \(\mathrm L_i\mathrm R_{c-i}\) for \(0\le i\le c\) are a perfect matching. Contracting them leaves a graph with vertices \(0,\ldots,c\). An additional edge with sum \(t<c\) joins the contracted vertices \(i\) and \(c-t+i\), hence has distance \(c-t\). Therefore the contracted graph is exactly the finite Toeplitz graph with vertex count \(c+1\) and distinct distances \(p=c-b\), \(q=c-a\). Contracting forest edges preserves whether a cycle exists.

**2. The two-distance forest threshold.** For integers \(1\le p<q\), put \(g=\gcd(p,q)\). The graph on \(0,\ldots,n-1\) with edges at differences \(p,q\) is a forest exactly when \(n\le p+q-g\). To see this, split into residue classes modulo \(g\). Each class is a consecutive-vertex two-distance graph with coprime distances \(p/g,q/g\). For coprime positive \(u<v\), the graph on \(u+v\) vertices with distances \(u,v\) is the single cycle obtained by successive additions of \(u\) modulo \(u+v\); its induced graph after removing the last vertex is a path. Hence a component first contains a cycle on reaching \(u+v\) vertices. The longest residue component has \(\lceil n/g\rceil\) vertices, so a cycle occurs precisely when \(\lceil n/g\rceil\ge(p+q)/g\), equivalently \(n>p+q-g\). Applying this at \(n=c+1\), with \(p=c-b\) and \(q=c-a\), proves
\[
\Gamma_{D_0}\text{ is a forest}\quad\Longleftrightarrow\quad a<c-b-\gcd(c-b,b-a).
\]

**3. Extension without changing a prefix.** If \(\Gamma_{D_0}\) contains a cycle, every super-support retains it. Conversely, if it is a forest, choose a new index \(d>\max\{N,2c\}\). Each edge introduced by the singleton sum \(d\) belongs to a matching and has at least one endpoint unused by the graph with sums at most \(c\). Thus adjoining \(d\) introduces no cycle. Repeat with each new index greater than twice the preceding maximum. The resulting infinite set \(D\) has a forest incidence graph and intersects \(\{0,\ldots,N\}\) exactly in \(D_0\). The published characterization completes the normalized extension equivalence. Furthermore, every forest incidence support is Sidon, since a repeated positive difference gives a four-cycle. If an unrestricted Abelian pattern Sturmian extension had the complementary zero support as its forest support, its first \(N+1\) positions would have \(N-2\) distinct zero positions. Their \(\binom{N-2}{2}\) positive differences would have to be distinct in \(\{1,\ldots,N\}\), forcing \(\binom{N-2}{2}\le N\). This fails for every \(N\ge7\), proving the unrestricted statement in the finding.

**4. Exact count.** Write \(x=c-b\), \(y=b-a\), and \(g=\gcd(x,y)\). Then \(c=a+x+y\) and the criterion is \(0\le a<x-g\). For given \(x,y\), the prefix bound imposes \(a\le N-x-y\). Counting integral \(a\) proves the displayed exact sum.

**5. Leading cubic term.** Ignore the gcd subtraction temporarily, requiring only \(a<x\). The resulting count is
\[
B(N)=\sum_{s=1}^{N-1}\left\lceil\frac{s}{2}\right\rceil(N-s)
=\frac{N^3}{12}+O(N^2).
\]
This follows by taking \(s=a+x\) and observing that there are \(\lceil s/2\rceil\) possibilities for \((a,x)\) and \(N-s\) possibilities for \(y\). Explicitly, \(B(2h)=h(h+1)(4h-1)/6\) and \(B(2h+1)=h(h+1)(4h+5)/6\).

**6. Arithmetic exclusion and the logarithmic term.** For each \(x,y\), the tuples counted by \(B(N)\) but excluded by the actual criterion have \(a=x-t\), where \(1\le t\le\gcd(x,y)\), and their last one lies at \(c=2x+y-t\). Hence the exact exclusion count \(E(N)=B(N)-T(N)\) equals
\[
E(N)=\sum_{x,y\ge1}\sum_{t=1}^{\gcd(x,y)}
\mathbf1_{\{2x+y-t\le N\}}.
\]
Set \(E_0(N)=\sum_{2x+y\le N}\gcd(x,y)\). The difference \(R(N)=E(N)-E_0(N)\) is supported on \(N<2x+y\le N+\gcd(x,y)\). Writing \(x=du\), \(y=dv\), \(d=\gcd(x,y)\), forces \(2u+v=\lfloor N/d\rfloor+1\). For each \(d\) there are at most \(N/(2d)+1\) positive pairs \((u,v)\); each contributes at most \(d\). Summing over \(d\le N\) proves \(0\le R(N)=O(N^2)\).

By \(\gcd(x,y)=\sum_{d\mid x,\ d\mid y}\varphi(d)\), where \(\varphi\) is Euler's totient,
\[
E_0(N)=\sum_{d\le N/3}\varphi(d)
H\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\qquad H(k)=\#\{u,v\ge1:2u+v\le k\}
=\left\lfloor\frac{(k-1)^2}{4}\right\rfloor.
\]
Because \(H(k)=k^2/4+O(k)\) and \(\varphi(d)\le d\),
\[
E_0(N)=\frac{N^2}{4}\sum_{d\le N/3}\frac{\varphi(d)}{d^2}+O(N^2).
\]
The identity \(\varphi(d)/d^2=\sum_{r\mid d}\mu(r)/(r^2(d/r))\) and harmonic summation give
\[
\sum_{d\le X}\frac{\varphi(d)}{d^2}
=\frac{\log X}{\zeta(2)}+O(1),
\qquad \zeta(2)=\frac{\pi^2}{6}.
\]
Therefore \(E(N)=3N^2\log N/(2\pi^2)+O(N^2)\), which, subtracted from \(B(N)\), proves the theorem. Dividing by \(\binom{N+1}{3}=N^3/6+O(N^2)\) gives the fraction.

## Verification
Run `python3 verify.py` in the directory containing the accompanying code. The verifier independently builds the bipartite incidence graph for all \(35{,}990\) triples with largest index at most \(60\) and tests its acyclicity against the gcd criterion. It also compares the direct count, the exact arithmetic sum, and an independently organized totient/exclusion decomposition for every \(2\le N\le90\); lastly, it checks five-stage explicit forest-preserving extensions on sample triples. The recorded output is in `verification_output.txt`. These finite computations corroborate the algebraic proof; they do not establish the asymptotic independently.

## Relationship to prior work
Zeng, Xue and Zeng (first public version September 23, 2026), Theorem E, establish the incidence-forest characterization of Abelian pattern Sturmian words. The 2014 *Bipartite finite Toeplitz graphs* paper, Corollary 2, gives the exact path/cycle threshold for two-distance Toeplitz graphs. Thus neither the general extremal-word characterization nor the underlying two-distance forest criterion is claimed as new. Their combination explains the finite three-position extendibility criterion; the additional mathematical statement here is the exact number of extendible three-one prefixes and its logarithmic second-order asymptotic. Nearby published records on sparse-support envelopes do not imply such enumeration. An equivalent prior enumerative calculation outside the inspected sources remains a publication-priority risk.

## Limitations
The result concerns exactly three nonzero symbols in a binary prefix, not a general formula at four or more symbols, and the \(O(N^2)\) remainder is not evaluated to a constant. The proof uses the published Abelian pattern Sturmian incidence characterization, the two-distance forest threshold (also reproved above), and standard totient summation. No independent publication-priority certification or independent mathematical audit is asserted.

## References
1. Q. Zeng, Y. Xue, and C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059, first version September 23, 2026; Theorem E and Section 7. https://arxiv.org/abs/2609.28059
2. *Bipartite finite Toeplitz graphs*, *Discrete Applied Mathematics* **165** (2014), 233–244, DOI:10.1016/j.dam.2013.05.020; Corollary 2. https://doi.org/10.1016/j.dam.2013.05.020
3. Classical arithmetic identities: \(\gcd(m,n)=\sum_{d\mid m,n}\varphi(d)\), \(\sum_{d\le X}\varphi(d)/d^2=(\log X)/\zeta(2)+O(1)\), and \(\zeta(2)=\pi^2/6\).
