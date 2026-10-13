# Sharp parity-dependent asymptotics for binary palindromic periodicities

## Finding

Let \(P(n)\) count binary length-\(n\) words that are prefixes of \((ps)^\omega\), for palindromes \(p,s\), possibly empty, satisfying \(1\le |ps|\le n\). Then
\[
P(2m)\sim 10m\,2^m,\qquad P(2m+1)\sim7(2m+1)\,2^m\quad(m\to\infty).
\]
Equivalently, the leading constants relative to \(n2^{n/2}\) are \(5\) for even \(n\), and \(7/\sqrt2\) for odd \(n\).

## Assumptions and scope

Words use the alphabet \(\{0,1\}\), and indices start at zero. The empty word is a palindrome. A length-\(n\) palindromic periodicity has a representation with root \(u=ps\) of length \(d\in\{1,\ldots,n\}\), where \(p\) and \(s\) are palindromes and \(u\) is repeated periodically. We count distinct length-\(n\) words, not representations. No primitivity requirement is imposed on \(u\). For each \(d\) and split \(0\le c<d\), let \(F_{n;d,c}\) be the set of length-\(n\) periodic extensions of roots with a palindrome of length \(c\) followed by a palindrome of length \(d-c\). The excluded split \(c=d\) duplicates \(c=0\).

## Proof

**One-model count and the global upper bound.** Choosing half of each palindrome, with its middle letter if the length is odd, yields exactly
\[
|F_{n;d,c}|=2^{\lceil c/2\rceil+\lceil(d-c)/2\rceil}.
\]
Distinct roots give distinct periodic extensions because \(d\le n\). Consequently the total representation count at root length \(d\) is
\[
S_d:=\sum_{c=0}^{d-1}|F_{n;d,c}|=
\begin{cases}
\frac32d\,2^{d/2},&d\text{ even},\\
d\,2^{(d+1)/2},&d\text{ odd}.
\end{cases}
\]
Indeed, for even \(d\), half the cuts have two even blocks and half have two odd blocks; for odd \(d\), every cut gives the same count. Taking the union over all \(d,c\),
\[
P(n)\le\sum_{d=1}^n S_d.
\]

**Asymptotic near-disjointness.** Fix an integer \(L\ge0\) and a real \(0<\delta<1/4\). Restrict to \(n-L\le d\le n\) and \(\delta n\le c\le d-\delta n\). We show that, uniformly over distinct such pairs \((d,c)\ne(e,f)\),
\[
|F_{n;d,c}\cap F_{n;e,f}|\le
2^{n/2+L+2-\delta n/4},
\]
for sufficiently large \(n\), with an immaterial adjustment to the constant for rounding.

For a root of length \(d\), each of its palindrome constraints joins position \(i\), \(0\le i<d\), to its reflection partner
\[
R_{d,c}(i)=
\begin{cases}
c-1-i,&i<c,\\
d+c-1-i,&c\le i<d.
\end{cases}
\]
This is a matching with at most two fixed vertices. Its connected components have size at most two. On the \(n\) positions of the entire word, impose only this first matching and leave the last \(n-d\) positions isolated (ignoring extra periodicity constraints only increases the intersection). There are at most \(n/2+L+1\) components, since the root matching has \(\lceil c/2\rceil+\lceil(d-c)/2\rceil\le d/2+1\) components.

For two distinct models, there are at least \(\delta n\) indices \(i\) at which the reflection partners differ: if \(c\ne f\), use \(0\le i<\min(c,f)\), where the partners are \(c-1-i\) and \(f-1-i\); if \(c=f\) but \(d\ne e\), use \(c\le i<\min(d,e)\), where the partners are \(d+c-1-i\) and \(e+c-1-i\). All partners lie in their respective root intervals. Discard at most two indices fixed by the second reflection. The remaining at least \(\delta n-2\) indices exhibit second-matching edges joining distinct components of the first matching. Since every second-matching edge is counted by at most two indices, there are at least \((\delta n-2)/2\) distinct joining edges.

Contract the first-matching components. Every vertex of the resulting multigraph has degree at most two, because an original first-matching component contains at most two positions, each incident to at most one second-matching edge. A loop-free degree-at-most-two multigraph with \(h\) joining edges merges at least \(h/2\) components: each path contributes its full edge count, and each cycle of length at least two contributes its edge count minus one. Therefore imposing the second matching reduces the number of free binary letters by at least \((\delta n-2)/4\). The intersection has at most \(2^{n/2+L+1-(\delta n-2)/4}\) words; the displayed bound follows. This argument permits parallel edges, fixed points and unequal root lengths.

There are at most \((L+1)n\) restricted models, so the sum of their pairwise intersections is \(O_L(n^2 2^{n/2+L+2-\delta n/4})=o(n2^{n/2})\). By the two-term inclusion-exclusion inequality, their union size equals the sum of their cardinalities up to \(o(n2^{n/2})\). For fixed \(L\), the omitted endpoint cuts contribute \(O_L(\delta n2^{n/2}+2^{n/2})\). Thus
\[
\liminf_{\substack{n\to\infty\\n\equiv r\pmod 2}}
\frac{P(n)}{n2^{n/2}}\ge
\lim_{\substack{n\to\infty\\n\equiv r\pmod 2}}
\frac{\sum_{t=0}^L S_{n-t}}{n2^{n/2}}-O_L(\delta).
\]
First let \(\delta\downarrow0\), then \(L\to\infty\). The reverse inequality follows from the global upper bound. The corresponding absolutely convergent geometric sums are, for even \(n\),
\[
\frac32\sum_{j\ge0}2^{-j}+\sum_{j\ge0}2^{-j}=3+2=5,
\]
and, for odd \(n\),
\[
\sqrt2\sum_{j\ge0}2^{-j}+\frac{3}{2\sqrt2}\sum_{j\ge0}2^{-j}
=2\sqrt2+\frac3{\sqrt2}=\frac7{\sqrt2}.
\]
This proves both asymptotic statements.

## Verification

The included `verify.py` implements two independent finite descriptions: direct detection of periodic roots with a palindromic split for every binary word through length twelve, and exhaustive construction from all root-length/split models. They agree word-for-word. It also verifies all one-model counting formulas and the published sequence A374495 at the sampled larger lengths sixteen, eighteen, and twenty. Run `python3 verify.py` with Python 3 and no external packages. These finite checks test the definitions and edge cases; the proof of the asymptotic formulas is the combinatorial matching argument above.

## Relationship to prior work

Fici, Shallit, and Simpson explicitly ask for the asymptotic count of binary palindromic periodicities in the conclusions of *On Palindromic Periodicities* (2025; first available as *Some Remarks on Palindromic Periodicities*, arXiv:2407.10564, July 15, 2024). Their paper and OEIS A374495 give initial exact counts rather than the two parity-dependent sharp asymptotic constants. Simpson's earlier *Palindromic Periodicities* (arXiv:2402.05381) analyzes multiple periodicity representations and overlap but does not provide this enumeration asymptotic. Kemp's enumeration of products of two palindromes counts roots themselves; it does not by itself count their distinct longer periodic extensions with varying root lengths. The present intersection bound controls exactly those multiple representations.

## Limitations

The result concerns the two-letter alphabet and leading asymptotics only. It does not provide an exact formula for \(P(n)\), a quantitative error term, a uniform estimate for growing root-length deficit \(L\), or asymptotics for alphabets of other sizes. The overlap proof requires fixed \(L\) before taking \(n\to\infty\), then takes \(L\to\infty\); it does not assume uniformity in \(L\). Prior coverage cannot be ruled out absolutely under unindexed terminology.

## References

1. G. Fici, J. Shallit, J. Simpson, *Some Remarks on Palindromic Periodicities*, arXiv:2407.10564 (first publicly submitted July 15, 2024); expanded as *On Palindromic Periodicities*, CPM 2025, doi:10.4230/LIPIcs.CPM.2025.11. See Section 7.
2. J. Simpson, *Palindromic Periodicities*, arXiv:2402.05381 (first publicly submitted February 8, 2024).
3. N. J. A. Sloane and collaborators, OEIS A374495, *Number of palindromic periodicities among the binary words of length n*, https://oeis.org/A374495.
4. R. Kemp, *On the number of words in the language of products of two palindromes*, Discrete Mathematics 40 (1982), 225–234.
