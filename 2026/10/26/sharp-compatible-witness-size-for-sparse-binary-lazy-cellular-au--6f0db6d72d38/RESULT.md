# Sharp compatible-witness size for sparse binary lazy cellular automata

## Finding

For a finite set \(S\subset\mathbb Z\) containing \(0\), let \(p:S\to\{0,1\}\) satisfy \(p(0)=0\), and let the associated **lazy cellular automaton** \(F_p\) on \(\{0,1\}^{\mathbb Z}\) replace the symbol at a site by \(1\) exactly when its translated \(S\)-pattern equals \(p\); otherwise the site is unchanged. A *compatible set* is as defined precisely below. If the automaton is non-idempotent, define its witness size \(w(p)\) as the least cardinality of a nonempty compatible set.

**Theorem.** For every integer \(m\ge2\), among all non-idempotent binary lazy cellular automata with minimal neighborhood cardinality \(m\), the maximum possible witness size is

\[
\boxed{\max w(p)=\max\{1,m-3\}.}
\]

In particular, for each \(k\ge2\), the least possible neighborhood cardinality permitting \(w(p)=k\) is exactly \(k+3\). Moreover, for each such \(k\), there is an explicit pattern whose **only** nonempty compatible set is its entire \(k\)-point active fiber. Thus no uniform bound on the number of simultaneously active centers needed for a compatibility witness exists for arbitrary sparse one-dimensional neighborhoods.

## Assumptions and scope

For \(S\subset\mathbb Z\) finite with \(0\in S\) and \(p(0)=0\), write \(S_0=\{s\in S:p(s)=0\}\) and \(S_1=\{s\in S:p(s)=1\}\). Necessarily \(0\in S_0\). The local rule is

\[
F_p(x)(j)=\begin{cases}1,&x(j+s)=p(s)\ \text{for every }s\in S,\\ x(j),&\text{otherwise}.\end{cases}
\]

For a nonempty \(U\subseteq S_1\), call \(U\) *compatible* when both of the following conditions hold:

1. For every \(t,r\in U\), the copies \(s+t\mapsto p(s)\) and \(s+r\mapsto p(s)\) agree wherever \(S+t\) and \(S+r\) overlap.
2. For every \(t\in U\) and \(z\in (S+t)\cap(S\setminus U)\), one has \(p(z-t)=p(z)\).

These are the compatibility conditions of Alcalá-Arroyo, Castillo-Ramirez, Magaña-Chávez and de los Santos Baños (2026), specialized to \(\mathbb Z\). Their Corollary 4.5 states that \(F_p\) is non-idempotent exactly when a compatible nonempty set exists. Complementing symbols reduces the case \(p(0)=1\) to the one stated. The result concerns finite sparse neighborhoods (not necessarily intervals), with actual minimal-memory cardinality \(m=|S|\); these are minimal for nontrivial unique-active-transition automata by the earlier minimal-memory lemma.

## Proof

**1. A closure lemma.** Suppose \(T\subseteq S_1\) is compatible. Form a directed graph on \(T\), placing an arrow \(t\to s\) for distinct \(t,s\in T\) whenever \(s-t\in S_0\). For nonempty \(U\subseteq T\),

\[
U\text{ is compatible}\ \Longleftrightarrow\ U\text{ has no arrow to }T\setminus U.
\]

Indeed, overlaps between translated copies indexed by \(U\) are inherited from compatibility of \(T\). For the second compatibility condition, sites in \(S\setminus T\) already satisfy it. At a site \(s\in T\setminus U\), the condition, when \(s\in S+t\), reads \(p(s-t)=p(s)=1\). Its only possible failure is \(s-t\in S_0\), exactly an arrow \(t\to s\) leaving \(U\). In particular, the inclusion-minimal compatible subsets of \(T\) are precisely sink strongly connected components of this finite directed graph.

**2. Universal lower bound on memory size.** If \(S_0=\{0\}\), the closure lemma shows any singleton \(\{t\}\subseteq T\) is compatible. If \(S_0=\{0,d\}\) with \(d\ne0\), every graph edge has displacement \(d\); if \(d>0\), the largest vertex of \(T\) is a sink, and if \(d<0\), the smallest is a sink. Thus any nonempty compatible \(T\) contains a compatible singleton whenever \(|S_0|\le2\). Consequently \(w(p)\ge2\) forces \(|S_0|\ge3\), and since \(|S_1|\ge w(p)\),

\[
|S|=|S_0|+|S_1|\ge w(p)+3.
\]

For \(w(p)=1\), non-idempotence requires at least two neighborhood coordinates, since \(0\notin S_1\). These bounds imply \(w(p)\le\max\{1,|S|-3\}\) for every non-idempotent rule of memory size at least two.

**3. Equality for all memory sizes at least five.** Fix \(k\ge2\) and put

\[
S_0=\{-2,0,2\},\qquad S_1=\{5,7,9,\ldots,2k+3\},\qquad S=S_0\cup S_1,
\]

with \(p=0\) on \(S_0\) and \(p=1\) on \(S_1\). Then \(|S|=k+3\). For every \(t\in S_1\), the translated zero-sites \(S_0+t\) are odd and the translated one-sites \(S_1+t\) are even. All translated copies agree wherever they overlap, while \((S+t)\cap S_0=\varnothing\), because the least element of \(S+t\) is at least \(3\). Consequently the whole fiber \(T=S_1\) is compatible.

For every consecutive pair \(t,t+2\in T\), both arrows \(t\to t+2\) and \(t+2\to t\) exist, because \(\pm2\in S_0\). Hence its directed graph is strongly connected. The closure lemma gives that **no proper nonempty subset** of \(T\) is compatible. Therefore \(w(p)=|T|=k\).

For completeness, non-idempotence can also be witnessed without appealing to the literature's compatibility criterion. Let \(x:\mathbb Z\to\{0,1\}\) be the indicator of the finite sumset \(T+T\). For each \(t\in T\), one has \(x(t+s)=p(s)\) for every \(s\in S\) (the required one-sites are even in \(T+T\), and required zero-sites odd). Thus \(F_p(x)(t)=1\) for \(t\in T\). For \(s\in S_0\), \(x(s)=0\) and \(x(s+t)=0\ne p(t)\) for any \(t\in T\), so \(F_p(x)(s)=0\). It follows that \(F_p(x)|_S=p\), whence \(F_p^2(x)(0)=1\) but \(F_p(x)(0)=0\).

**4. Small memory sizes.** For \(m\in\{2,3,4\}\), choose \(S=\{0,1,\ldots,m-1\}\), with \(p(m-1)=1\) and \(p=0\) elsewhere. The singleton \(\{m-1\}\) is compatible because \((S+m-1)\cap(S\setminus\{m-1\})=\varnothing\). Thus \(w(p)=1\). Combining these examples with the upper bound gives the formula for every \(m\ge2\).

## Verification

The included standalone Python 3 script `verify.py` uses exact integer/set operations and no external libraries. Execute `python3 verify.py`. It tests every nonempty candidate subset in the explicit construction for \(2\le k\le10\), constructs finite local non-idempotence witnesses, enumerates all relevant binary patterns on support sizes at most four inside \([-4,4]\), and tests the directed-graph closure lemma for larger small supports. Its recorded output is `2035` family-subset instances, `577` small-neighborhood patterns, and `1646` graph-closure instances, all passing. The infinite theorem is proved above; no finite search is being used as an infinite certificate.

## Relationship to prior work

Alcalá-Arroyo et al. (arXiv:2610.11811v2, Sections 3–4) introduce compatible sets and prove their equivalence to non-idempotence over abelian groups. Their Example 4.7 gives a sparse five-site binary pattern for which two active centers are jointly necessary, already establishing the case \(k=2\). The present theorem does **not** claim the compatibility criterion or that example as new. Instead it determines the optimal certificate-size extremum for every memory cardinality and constructs a family attaining it, supported by the closure lemma.

Castillo-Ramirez, Magaña-Chavez and de los Santos Baños (arXiv:2411.03601v3, Theorem 1) prove a singleton-translation characterization for **interval** neighborhoods; the constructed neighborhoods here are sparse and are not covered by that theorem. Castillo-Ramirez, Magaña-Chavez and Veliz-Quintero (arXiv:2401.09593v2, Theorems 1–2) establish criteria for constant, symmetric and quasi-constant patterns rather than this sharp witness-cardinality bound. Their Lemma 1 establishes minimal memory for the unique-active-transition rules.

## Limitations

The maximum is taken over binary rules on \(\mathbb Z\) with finite, freely chosen neighborhoods and a unique active transition. It does not give a lower bound for the computational complexity of **all** idempotence algorithms; algorithms may exploit graph structure instead of enumerating subsets. The sharp bound may differ for restricted geometries, higher alphabets or other group universes. Historical priority beyond the inspected primary literature and searched mathematical records remains a possible uncertainty. Independent mathematical validation has not been performed.

## References

1. E. Alcalá-Arroyo, A. Castillo-Ramirez, M. G. Magaña-Chávez, L. de los Santos Baños, *Idempotence criteria for lazy cellular automata*, arXiv:2610.11811v1 (first posted 2026-10-08), especially v2, Definition 4.1, Corollary 4.5, Example 4.7. https://arxiv.org/html/2610.11811v2
2. A. Castillo-Ramirez, M. G. Magaña-Chavez, L. de los Santos Baños, *One-dimensional cellular automata with a unique active transition*, arXiv:2411.03601v3, Theorem 1. https://arxiv.org/html/2411.03601v3
3. A. Castillo-Ramirez, M. G. Magaña-Chavez, E. Veliz-Quintero, *Idempotent cellular automata and their natural order*, arXiv:2401.09593v2, Lemma 1 and Theorems 1–2. https://arxiv.org/pdf/2401.09593
