# Sharp one-point odd-order completion and parity-profile census of partial permutations

## Finding

Consider a partial bijection \(f:D\to R\) on a nonempty finite set \(X\), with \(D,R\subseteq X\). Form its directed graph with an arrow \(a\to f(a)\) for each \(a\in D\). Decompose this graph into directed cycles and open directed paths, counting an isolated vertex as a path containing one vertex. Let \(u\) and \(v\) be the numbers of open paths having, respectively, odd and even vertex counts, and put \(k=u+v\). A *completion* means a permutation \(\sigma\) of \(X\) with \(\sigma|_D=f\). A permutation has odd order precisely when every one of its cycles has odd vertex length.

**Theorem (sharp extension and exact count).** If the graph of \(f\) contains any even directed cycle, an odd-order completion on any finite superset of \(X\) is impossible. If all existing directed cycles have odd length, the number \(N(f)\) of odd-order completions on \(X\) is
\[
N(f)=\begin{cases}
1,&k=0,\\
0,&k>0\text{ and }u=0,\\
\displaystyle u(k-1)!\,\frac{\binom{2\lfloor u/2\rfloor}{\lfloor u/2\rfloor}}{4^{\lfloor u/2\rfloor}},&u>0.
\end{cases}
\]
Every displayed count is an integer. In particular, the answer depends on the open-path lengths only through the parity profile \((u,v)\), not their actual sizes. If \(u=0<v\), *exactly one new vertex* is necessary and sufficient; for a specified extra vertex, exactly \(v!\) odd-order completions exist on the enlarged set. All other admissible cases require no extra vertex. Moreover, if \(N(u,v)\) denotes this count for \(u\) distinguished odd paths and \(v\) distinguished even paths, including \(N(0,0)=1\), then
\[
\sum_{u,v\ge0}N(u,v)\frac{x^u}{u!}\frac{y^v}{v!}
 =\sqrt{\frac{1-y+x}{1-y-x}}.
\]

## Assumptions and scope

There is exactly **one** partial bijection, acting on an arbitrary finite nonempty labelled set. A partial bijection is injective where defined; its finite directed graph has in-degree and out-degree at most one. A *new vertex* is a distinct extra element on which the partial bijection is initially undefined. An odd-order extension is a single permutation whose generated cyclic subgroup has odd order. We do not require a simultaneous extension of several partial bijections; such an extension is a substantially different problem.

## Proof

**1. From open paths to permutations.** Every directed cycle of \(f\) is already closed and cannot be broken by an extending permutation. An existing even cycle therefore makes an odd-order extension impossible on every superset. Assume no such cycle. For every open path, exactly its terminal vertex lacks an assigned outgoing arrow and exactly its initial vertex lacks an incoming arrow. Consequently any completion is uniquely specified by a bijection from the \(k\) terminal vertices to the \(k\) initial vertices. This bijection is equivalent to a permutation of the \(k\) distinguished open paths; each cycle of the latter concatenates its constituent paths into one completed permutation cycle. That cycle has an odd number of vertices if and only if it contains an odd number of odd-length paths. Thus the count is the number of permutations of \(u\) odd-colored and \(v\) even-colored distinguished objects in which each permutation cycle contains an odd number of odd-colored objects.

**2. Enumeration.** A single permitted cycle with \(j\) odd objects and \(t\) even objects must have \(j\) odd, \(j\ge1\), and \(t\ge0\). The labelled cycle-construction exponential generating series is
\[
L(x,y)=\sum_{j\ge1\atop j\,\mathrm{odd}}\sum_{t\ge0}
 \frac{(j+t-1)!}{j!t!}x^jy^t
 =\frac12\log\frac{1-y+x}{1-y-x}.
\]
The finite SET of permutation cycles therefore has series \(\exp L(x,y)\), which gives the stated square root. Put \(h_j=\binom{2j}{j}/4^j\). Expanding the square root as
\[
\sqrt{\frac{1+z}{1-z}}=(1+z)(1-z^2)^{-1/2}
 =\sum_{u\ge0}h_{\lfloor u/2\rfloor}z^u
\]
with \(z=x/(1-y)\), we obtain, for \(u>0\),
\[
N(u,v)=u!v!h_{\lfloor u/2\rfloor}
 \binom{u+v-1}{v}
 =u(u+v-1)!h_{\lfloor u/2\rfloor}.
\]
For \(u=0\), only the empty permutation of paths is permitted, proving the other cases. Integrality is automatic because this counts permutations.

**3. Sharp enlargement.** When \(u>0\), one may concatenate **all** open paths into one cycle: its total size is odd if and only if \(u\) is odd. For even positive \(u\), take one odd path as a singleton cycle, and concatenate the remaining \(u-1\) odd paths and all even paths into a second odd cycle. This constructs a completion without extra vertices. If \(k=0\), the existing cycles already give the unique completion. If \(u=0<v\), a completion on \(X\) cannot work: every cycle formed entirely from even-length paths has even size. Adjoin a new isolated vertex \(z\). It becomes one additional odd-length path, changing the profile to \((1,v)\). By the count formula there are \(N(1,v)=v!\) odd-order completions on \(X\cup\{z\}\), and the preceding impossibility establishes minimality. Thus exactly one new point is necessary and sufficient. If an existing even directed cycle exists, adding points cannot repair it.

## Verification

Run the standalone Python 3 standard-library file `checker.py`. It enumerates every partial injection on each labelled set of sizes \(1\) through \(5\), independently exhausts all permutation completions, tests every completed cycle's parity, and compares the exact counts to the theorem; this yields 1,798 checked partial injections. It also checks the factorial claim by exhaustive one-point enlargements in all 296 relevant small cases. These are finite checks, not a substitute for the all-sizes proof above.

## Relationship to prior work

Etedadialiabadi and Gao, *Extension Properties for Partial Permutations* (2026, arXiv:2610.04870v1), define general odd-extension problems for **sets** of partial permutations, connect them with tournament EPPA and finite-group properties, and obtain qualitative extension theorems under structural hypotheses. Their cyclic-fundamental-group case encompasses existence phenomena, but the inspected statements do not specify the sharp enlargement on a fixed finite set or the exact parity-profile completion multiplicity for one partial bijection. The classical formula counting permutations with all cycles odd is the special case \(v=0\), and is not claimed new. The standard labelled exponential formula, likewise, is an established enumeration tool. Kim, Kim and Seo (2017) study two-colored permutations with **no monochromatic cycles**, a different cycle restriction; the inspected abstract does not cover this theorem.

## Limitations

The criterion and counts concern one partial bijection only. They do not establish the general odd-extension property or the EPPA of finite tournaments. The EGF derives from classical cycle construction and may have equivalent antecedents under colored-permutation terminology; priority beyond inspected results has not been established. The computational check covers at most five original vertices; all-sizes correctness rests on the explicit bijection and generating-function argument.

## References

1. M. Etedadialiabadi and S. Gao, *Extension Properties for Partial Permutations*, arXiv:2610.04870v1, posted October 4, 2026; https://arxiv.org/html/2610.04870v1.
2. D. Kim, J. S. Kim, and S. Seo, *Colored permutations with no monochromatic cycles*, Journal of the Korean Mathematical Society **54** (2017), 1149–1161, DOI:10.4134/JKMS.j160392.
3. S. Hopkins, *Cycle generating function of permutations with only odd cycles*, MathOverflow question 308178, August 13, 2018; https://mathoverflow.net/questions/308178/cycle-generating-function-of-permutations-with-only-odd-cycles.
