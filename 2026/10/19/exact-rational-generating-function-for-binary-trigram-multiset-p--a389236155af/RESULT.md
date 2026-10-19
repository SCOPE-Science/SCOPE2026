# Exact rational generating function for binary trigram-multiset profiles

## Finding
For each binary linear word \(w\) of length \(n\ge2\), let \(M_3(w)\) be the eight-dimensional vector whose coordinates are the occurrence counts of the ordered contiguous trigrams \(000,001,010,011,100,101,110,111\). In particular, its observations do **not** include the endpoints or the counts of shorter factors. Let \(H(n)=|\{M_3(w):w\in\{0,1\}^n\}|\). Then, as an identity of formal power series,
\[
\sum_{n\ge2}H(n)z^{n-2}=
\frac{1+5z-6z^2+5z^3-z^4+6z^5+3z^6+z^7-z^8-2z^9+2z^{10}}{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.
\]
In particular,
\[
H(n)=\frac{13}{288}n^4+O(n^3)\quad(n\longrightarrow\infty).
\]
This is an exact infinite-length rational formula, not merely the previously tabulated finite initial values. The number \(H(n)\) is also the optimum cardinality of a zero-error code when the sole received observation is the multiset of contiguous, ordered three-letter reads.

## Assumptions and scope
Words are **linear**, not cyclic. Repeated trigrams retain multiplicity; their positions are forgotten. No read errors or incomplete observations are assumed. The denominator is interpreted formally at \(z=0\). For \(n=2\) the only observation is the all-zero vector; for \(n=3\) all eight trigrams give distinct vectors. The polynomial error term is absolute with the binary alphabet fixed. The theorem does not determine the sizes of the individual observation fibers.

## Proof
**Euler-trail criterion.** Identify the four vertices \(00,01,10,11\) of the binary order-two de Bruijn digraph. Denote edge multiplicities of \(000,001,010,011,100,101,110,111\) by \(a,b,c,d,e,f,g,h\), respectively. A nonnegative integer multiplicity vector is realized by a linear word exactly when its positive-edge graph is weakly connected (after discarding isolated vertices) and its directed degree imbalances are either all zero or a single \(+1,-1\) pair. This is the standard directed Euler-trail criterion. A realized trail with \(N\) edges spells a unique length-\(N+2\) source word once its starting vertex is specified; existence alone suffices to count profiles.

**Distinct imbalance types.** The loop edges \(a,h\) do not affect degrees. For an imbalance with value \(+1\) at a chosen start and \(-1\) at a distinct chosen end, or all zero for a closed trail, let \(v,u,w\) be the imbalances at \(00,01,11\). The imbalance at \(10\) is forced by zero sum. The degree equations give
\[
e=b-v,\qquad c=b+f-d+u,\qquad g=d+w.
\]
Accordingly, \(b\ge b_0:=\max(0,v)\), \(d\ge d_0:=\max(0,-w)\), and \(f\ge\max(0,d-b-u)\). The number of nonloop edges is
\[
3b+2f+d+u-v+w.
\]
Nonzero off-loop support is automatically weakly connected under these imbalance constraints. Indeed, every directed cycle of the loopless digraph passes through **both** \(01\) and \(10\). All directed paths of positive length meet one of those two vertices. If a putative Eulerian support had multiple weak components, at most one could have the nonzero imbalance pair; every additional component would carry a directed cycle. Two such components, or a path component and any cyclic component, would intersect at \(01\) or \(10\), a contradiction. This also proves connectedness for balanced support.

**Loop admissibility.** For nonzero off-loop support, an arbitrary nonnegative number of \(000\) loops is permitted if \(b+e>0\), but otherwise \(a=0\); similarly arbitrary \(111\) loops require \(d+g>0\). If there are no off-loop edges, precisely the empty profile and the two one-vertex loop profiles are permitted. This handles disconnected loops without relying on a spurious Euler-degree sufficiency condition.

**Exact generating series by boundary removal.** Put \(L=(1-z)^{-1}\) and write
\[
\begin{aligned}
S(b_0,d_0,u)&=\sum_{b\ge b_0,\ d\ge d_0}z^{3b+d+2\max(0,d-b-u)},\\
S_b(d_0,u)&=\sum_{d\ge d_0}z^{d+2\max(0,d-u)},\\
S_d(b_0,u)&=\sum_{b\ge b_0}z^{3b+2\max(0,-b-u)}.
\end{aligned}
\]
All three are rational. In detail, with \(C=\max(b_0,d_0-u)\), splitting the first sum into \(d\le b+u\) and \(d>b+u\) gives the explicit identity
\[
\begin{aligned}
S(b_0,d_0,u)={}&\frac{z^{d_0+3C}}{(1-z)(1-z^3)}
-\frac{z^{u+1+4C}}{(1-z)(1-z^4)}
+\frac{z^{u+3+4C}}{(1-z^3)(1-z^4)}\\
&+\mathbf1_{\{C>b_0\}}\frac{z^{b_0+3d_0-2u}(1-z^{C-b_0})}{(1-z)(1-z^3)}.
\end{aligned}
\]
The other two sums are a finite geometric prefix plus a tail: explicitly
\[
S_b=\mathbf1_{\{u\ge d_0\}}\sum_{d=d_0}^u z^d+\frac{z^{3\max(d_0,u+1)-2u}}{1-z^3},
\]
\[
S_d=\frac{z^{3\max(b_0,-u)}}{1-z^3}+\mathbf1_{\{-u>b_0\}}\sum_{b=b_0}^{-u-1}z^{b-2u}.
\]
The sum over admissible \(f\), after its minimum is imposed, contributes \((1-z^2)^{-1}\). The loop multipliers, with forbidden disconnected-loop boundaries excluded by inclusion-exclusion, therefore give, for each imbalance triple,
\[
\begin{aligned}
G(v,u,w)=\frac{z^{u-v+w}}{1-z^2}\big[&L^2S(b_0,d_0,u)
-\mathbf1_{\{v=0\}}L(L-1)S_b(d_0,u)\\
&-\mathbf1_{\{w=0\}}L(L-1)S_d(b_0,u)
+\mathbf1_{\{v=w=0\}}(L-1)^2z^{2\max(0,-u)}\big].
\end{aligned}
\]
The term with both boundary conditions is included only once; in particular, **no** extra geometric factor belongs in the last bracketed term. The unique zero-imbalance case contributes \(G(0,0,0)\). For each of the twelve ordered pairs of distinct start/end vertices, insert the corresponding imbalance triple into \(G\). The loop-only profiles add \(2z/(1-z)\). Thus
\[
F(z)=G(0,0,0)+\sum_{s\ne t}G(\delta_{00},\delta_{01},\delta_{11})+\frac{2z}{1-z}.
\]
For nonzero imbalance the starting/ending pair is forced by the vector, so there is no double-counting. For zero imbalance, we count the balanced vector once, not once per possible starting vertex. Exact rational simplification of the displayed finite sum yields the generating function in the finding; the accompanying `derive.py` evaluates precisely these formulas using symbolic rational arithmetic.

**Asymptotics.** At \(z=1\), the numerator is \(13\), and the non-\((1-z)\) denominator factors multiply to \(12\). Hence the order-five pole contributes \((13/12)\binom{N+4}{4}\), where \(N=n-2\). The other poles are roots of unity of order at most four and have lower order, giving \(H(n)=(13/288)n^4+O(n^3)\).

## Verification
`verify.py` implements two genuinely independent finite checks: enumeration of all binary source words (lengths \(2\) through \(17\)) and enumeration of all nonnegative eight-edge integer compositions with an independent directed Euler-trail test (edge totals \(0\) through \(13\)). Each matches the coefficients of the rational generating function. `derive.py` separately performs exact symbolic rational simplification using SymPy and independently compares direct word enumeration. The scripts need only Python 3; the derivation requires SymPy. Finite checks corroborate but do not replace the proof for unbounded lengths.

## Relationship to prior work
Varshney and Goyal (2007, Section VII-A) explicitly define Markov types via multisets of contiguous trigrams and display numerical counts; OEIS A132298 records the exact first eighteen terms of this **same** sequence. Consequently the numerical sequence, early values, existence of the invariant, and its source-coding motivation are **not new**. The result claimed here is the **infinite rational generating function, its derived polynomial leading coefficient, and an exact self-contained Euler-trail/loop-disconnection derivation**, none of which are stated in those inspected sources. Cassaigne et al. (2017) prove rationality for the distinct *finer* \(3\)-abelian equivalence invariant that remembers all factors of length at most three. OEIS A289657 records that finer invariant; for length six it gives \(60\), whereas the trigram-only profile count is \(52\). Published two-read spectrum enumeration also concerns a different observation length and does not imply this formula. A possible unlocated exact formula for A132298 remains a literature risk.

## Limitations
Prior work already tabulates the first eighteen counts, so no novelty is claimed for those values. An inaccessible full text of the 2017 rationality paper, and possible unindexed work on Markov-type lattice-point enumeration, are explicit residual novelty risks; the abstract and accessible related material do not establish this specific rational function. No independent mathematical audit has been performed. The theorem only handles a binary alphabet, contiguous ordered trigrams, and complete exact multiplicity observations, not general alphabet sizes or individual ambiguity-class multiplicities.

## References
1. Lav R. Varshney and Vivek K. Goyal, *Benefiting from Disorder: Source Coding for Unordered Data*, arXiv:0708.2310 (17 August 2007), Section VII-A, https://arxiv.org/html/0708.2310v1 .
2. OEIS A132298, *Number of distinct Markov type classes of order 3 possible in binary strings of length n*, https://oeis.org/A132298 (originally 17 August 2007).
3. Julien Cassaigne, Juhani Karhumäki, Svetlana Puzynina, Markus A. Whiteland, *k-Abelian Equivalence and Rationality*, Fundamenta Informaticae 154 (2017), https://doi.org/10.3233/FI-2017-1553 .
4. OEIS A289657, *Number of 3-abelian equivalence classes of words of length n over a binary alphabet*, https://oeis.org/A289657 .
5. AlEisa, Hamad and Elhadad, *K-Mer Spectrum-Based Error Correction Algorithm for Next-Generation Sequencing Data* (14 July 2022), https://doi.org/10.1155/2022/8077664 .
