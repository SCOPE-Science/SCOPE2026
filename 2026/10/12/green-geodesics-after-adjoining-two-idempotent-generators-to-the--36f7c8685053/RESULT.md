# Green geodesics after adjoining two idempotent generators to the monogenic free inverse monoid

## Finding
Let \(F=\operatorname{FIM}_1\) be the free inverse monoid on one generator \(x\). Use the **symmetric semigroup alphabet** \(\Sigma=\{p,m,u,v\}\), with \(p=x\), \(m=x^{-1}\), \(u=xx^{-1}\), and \(v=x^{-1}x\). All four letters have cost one; \(u\) and \(v\) are nonidentity idempotents. For a Green class \(C\), a Green-geodesic word is a word of the least \(\Sigma\)-length among representatives of elements of \(C\).

**Theorem.** Each \(\mathcal R\)-class is specified by a unique rooted Munn interval \([-a,b]\), for integers \(a,b\ge0\). Its minimum length is
\[
L_R(a,b)=\begin{cases}a+b,&ab=0,\\a+b+\min(a,b)-1,&ab>0.\end{cases}
\]
The number of shortest words in this \(\mathcal R\)-class is \(1\) if \(a=b=0\), \(4\) if \(a=b>0\), and \(2\) otherwise. For \(a,b>0\) and \(a\le b\), the shortest words from the negative-first route are exactly
\[
m^{a-1}v p^{a+b-1},\qquad m^{a-1}v p^{a+b-2}u.
\]
For \(b\le a\), the positive-first words are the two strings obtained by interchanging \(p\leftrightarrow m\), \(u\leftrightarrow v\), and \(a\leftrightarrow b\). When \(a=b\), both routes are shortest. On the positive boundary \(a=0<b\) the two words are \(p^b\) and \(p^{b-1}u\); on the negative boundary they are \(m^a\) and \(m^{a-1}v\). The identity has the empty word alone.

Consequently the \(\mathcal R\)-class length enumerator and the enumerator of all \(\mathcal R\)-geodesic **words** are, respectively,
\[
G_R(z)=1+\frac{2z}{1-z}+\frac{z^2}{1-z^3}+\frac{2z^3}{(1-z)(1-z^3)},
\qquad
W_R(z)=1+\frac{4z}{1-z}+\frac{4z^2}{1-z^3}+\frac{4z^3}{(1-z)(1-z^3)}.
\]
The \(\mathcal R\)-geodesic language is deterministic context-free but not regular. By reversing words and inverting every letter, the same properties and enumerators hold for \(\mathcal L\).

For \(\mathcal D=\mathcal J\), a class is specified by its Munn interval's width \(n\). Its minimum length is \(n\). The identity class has one shortest word; width one has four; and every width \(n\ge2\) has exactly the following eight:
\[
p^n,\ m^n,\ p^{n-1}u,\ m^{n-1}v,\ v p^{n-1},\ u m^{n-1},\ v p^{n-2}u,\ u m^{n-2}v.
\]
Thus the \(\mathcal D\)-geodesic language is regular; its word-length series is \(1+4z+8z^2/(1-z)\). The \(\mathcal D\)-class length series is \(1/(1-z)\).

## Assumptions and scope
The four letters represent fixed distinct elements of \(F\), even though \(p\) and \(m\) are inverses and \(u,v\) are self-inverse; the metric is ordinary **semigroup word length** on this explicitly symmetric four-letter alphabet. These statements concern the rank-one free inverse monoid, not an arbitrary inverse monoid or generating set. \(\mathcal H\)-geodesic language complexity is not classified here.

## Proof
**Munn intervals and the Green classes.** A word gives a walk on \(\mathbb Z\) starting at zero, recording the set of visited edges as an interval and its terminal vertex. Reading \(p\) or \(m\) moves by \(+1\) or \(-1\); reading \(u\) (respectively \(v\)) exposes the adjacent edge to the right (respectively left) and returns to the same vertex. The Munn representation identifies an element by the rooted interval and its terminal vertex. As in the Munn-tree characterization of Green relations, \(\mathcal R\) fixes the interval rooted at zero, \(\mathcal L\) fixes the interval rooted at the terminal vertex, and \(\mathcal D\) fixes the unrooted interval width.

**Sharp \(\mathcal R\)-length bound.** Consider \(a,b>0\). Every required edge of \([-a,b]\) must be exposed, and a letter exposes at most one new edge. If the left extreme is exposed first, the cheapest possible path reaches the adjacent vertex \(-a+1\), exposes the final left edge by \(v\) and then crosses monotonically toward the right extreme. Its cost is \((a-1)+1+(a+b-1)=2a+b-1\). Ending with \(u\) at \(b-1\), rather than moving to \(b\), has the same cost. Any route reaching \(-a\) instead of probing it, or retracing an extra edge, costs at least one more. Conversely, to expose both extremes with fewer letters one would have to expose some required edge without either an outward move or an idempotent probe, which is impossible. Thus every left-first path has cost at least \(2a+b-1\), with equality exactly for the two displayed words. The symmetric right-first bound is \(a+2b-1\), with equality exactly for its two displayed words. Comparing gives the formula and multiplicities. If one endpoint is zero, at least \(a+b\) new edges must be exposed, with equality only through the monotone path or a terminal probe. The empty interval has the empty word.

**Language complexity.** The exact \(\mathcal R\)-geodesic language is the union of the empty word, the pure positive/negative powers, the terminal-probe boundary words, and the four families
\[
\begin{aligned}
&m^i v p^j\ (j\ge2i+1),\quad m^i v p^j u\ (j\ge2i),\\
&p^i u m^j\ (j\ge2i+1),\quad p^i u m^j v\ (j\ge2i),
\end{aligned}\qquad i,j\ge0.
\]
The boundary words are \(p^j u\), \(m^j v\) (\(j\ge0\)), together with \(p^j,m^j\) (\(j\ge1\)). A deterministic one-counter pushdown automaton recognizes this union: its first unidirectional block records twice its length, the distinguishing probe chooses the direction, and the subsequent opposite block discharges the counter, with acceptance thresholds \(2i\) or \(2i+1\) determined by whether a final probe occurs. The exceptional pure and boundary words are determined by finite control. Nonregularity follows by intersecting with the regular set \(m^+vp^+\); the intersection consists of \(m^ivp^j\) with \(i\ge1\), \(j\ge2i+1\). Distinct prefixes \(m^iv\) are distinguished by suitable suffixes \(p^{2i+1}\), so this intersection is not regular. Inversion reverses words and exchanges \(\mathcal R\) and \(\mathcal L\), preserving word length; reversal and letter permutation preserve deterministic context-freeness here because the reversed explicit counter conditions admit the same deterministic one-counter construction. (One need not invoke closure of all deterministic context-free languages under reversal.)

**\(\mathcal D\) and enumeration.** An interval of width \(n\) needs \(n\) distinct exposed edges, so the shortest length is at least \(n\); pure powers attain it. Equality forces each letter to expose one new edge. Every such word follows a monotonically advancing sweep, with at most one probe at the starting end and at most one at the finishing end, yielding precisely the eight displayed templates for \(n\ge2\), and the four single letters when \(n=1\). The language is a finite union of regular forms. Finally summing the \(\mathcal R\)-classes by \(a=0\) or \(b=0\), \(a=b>0\), and the two strict-order regions gives the rational series: the diagonal contributes \(\sum_{t\ge1}z^{3t-1}=z^2/(1-z^3)\), and the strict-order regions contribute \(2\sum_{t,k\ge1}z^{3t+k-1}=2z^3/((1-z)(1-z^3))\). Multiplicities give \(W_R\).

## Verification
The included `verify.py` independently enumerates all four-letter words of lengths zero through nine, computes rooted Munn intervals directly from their path actions, and compares the entire minimum representative set of every reachable \(\mathcal R\)-class to the closed formulas. It separately checks the complete \(\mathcal D\) minimal words through length nine, the rational generating-function coefficients, and the inverse-image correspondence for \(\mathcal L\). No experiment is used to infer infinite language results: the complete proof above covers all nonnegative interval parameters.

## Relationship to prior work
Bodart, Carvalho and Monteiro (arXiv:2609.35251v1, 2026-09-28) introduced Green geodesic languages and completely described their rank-one complexity for the **standard** generating alphabet (Theorem 9.1); Section 11 specifically asks how their complexity depends on the generating set. Its standard-alphabet formulas are not asserted as new. The present result addresses a different four-letter alphabet containing two additional genuine idempotents and determines all shortest representatives, class/word series and complexity for three Green relations. The earlier work of Kambites, Nyberg-Brodda, Szakács and Webb on ordinary free-inverse-monoid growth deals with standard word length and does not supply the modified Green-class enumerators.

## Limitations
Only one natural nonstandard symmetric generating alphabet is handled, and the result does not establish invariance under every change of generating set. The precise \(\mathcal H\)-language for this alphabet remains open here. Historical equivalences phrased in terms of weighted walks with idempotent edge probes cannot be completely excluded; the open-literature and published-result searches did not identify the same four-letter classification.

## References
1. C. Bodart, A. Carvalho and A.-C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251v1 (first posted September 28, 2026), particularly Theorem 9.1 and Section 11.
2. M. Kambites, C.-F. Nyberg-Brodda, N. Szakács and R. Webb, *The growth of free inverse monoids*, arXiv:2407.10489 (first posted July 15, 2024), especially the rank-one growth discussion.
3. P. V. Silva, *On the rational subsets of the monogenic free inverse monoid*, arXiv:2205.08854 (2022), for standard interval normal forms.
