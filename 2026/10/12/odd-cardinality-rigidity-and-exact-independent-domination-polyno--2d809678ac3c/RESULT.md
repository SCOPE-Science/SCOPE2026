# Odd-cardinality rigidity and exact independent-domination polynomial of Möbius ladders

## Finding

Let \(M_{2n}\) denote the Möbius ladder with \(2n\) vertices, for every integer \(n\ge3\). Define its independent-domination polynomial

\[
D_n(z)=\sum_{\substack{S\subseteq V(M_{2n})\\S\text{ independent and dominating}}}z^{|S|}.
\]

**Theorem (complete size distribution).** For every \(n\ge3\),

\[
\boxed{D_n(z)=\sum_{\substack{\lceil n/2\rceil\le j\le n\\j\ \mathrm{odd}}}\frac{2n}{j}\binom{j}{n-j}z^j.}
\]

Equivalently, the entire bivariate ordinary generating function is

\[
\boxed{\sum_{n\ge3}D_n(z)t^n
=\frac{2zt(1+2t)}{1-z^2t^2(1+t)^2}-2zt-4zt^2.}
\]

Thus every inclusion-maximal independent set has **odd cardinality**; conversely every odd cardinality \(j\) in the closed integer range \(\lceil n/2\rceil\le j\le n\) occurs. In particular, the independent-domination number and independence number are

\[
i(M_{2n})=\min\{j\ge\lceil n/2\rceil:j\text{ odd}\},
\qquad
\alpha(M_{2n})=\begin{cases}n,&n\text{ odd},\\n-1,&n\text{ even}.\end{cases}
\]

The number of maximum independent sets is \(2\) for odd \(n\) and \(2n\) for even \(n\). The number of minimum-size maximal independent sets is the displayed binomial coefficient at the least admissible odd \(j\). By taking complements, the formula is also the complete size distribution of inclusion-minimal vertex covers, with sizes \(2n-j\), all odd.

## Assumptions and scope

The graph has vertices \(u_0,\ldots,u_{n-1},v_0,\ldots,v_{n-1}\), rung edges \(u_iv_i\), ordinary rail edges \(u_iu_{i+1}\) and \(v_iv_{i+1}\) for \(0\le i<n-1\), and *twisted* closing edges \(u_{n-1}v_0\) and \(v_{n-1}u_0\). This is isomorphic to the \(2n\)-cycle with every opposite-vertex chord added. All graphs are finite, simple and labeled by this construction; no identifications of sets under graph automorphisms are made. A vertex set is independent if no two selected vertices are adjacent, and dominating if every vertex not selected has a selected neighbor. A set is independent and dominating exactly when it is inclusion-maximal independent.

## Proof

**1. States and empty-rung obstruction.** A selected independent set has at most one vertex on each rung. Write its rung state as \(U\) (only \(u_i\) selected), \(V\) (only \(v_i\) selected), or \(0\) (neither selected). Extend the states to all integer indices by the Möbius twist

\[
s_{i+n}=\tau(s_i),\qquad \tau(0)=0,\quad \tau(U)=V,\quad\tau(V)=U.
\]

This encoding incorporates the seam without any separate exception. Independence says that whenever two successive rung states are nonzero they must be different. If a rung state is \(0\), then domination of both unselected rung vertices forces its two neighboring states to be \(U\) and \(V\), in either order. In particular empty rungs cannot be adjacent. Conversely, those two local conditions, together with the rung edge, are sufficient for independence and domination: every unselected vertex on a nonempty rung sees its selected partner, and both vertices of an empty rung see selected vertices on their respective rails.

**2. Alternating sequence and the twist.** Delete all empty rungs from the bi-infinite state sequence. Every pair of consecutive retained states must be different: if their original rungs were adjacent, independence enforces this; if separated by one empty rung, domination of that rung enforces it. There are \(j\) nonempty rungs in any consecutive block of \(n\) rungs. Moving from one retained state to the state \(n\) rungs later encounters exactly \(j\) swaps \(U\leftrightarrow V\). The prescribed Möbius extension swaps that state once. Therefore \(j\) must be odd. Conversely, if the empty rungs are pairwise nonadjacent and \(j\) is odd, choosing either \(U\) or \(V\) at one nonempty rung and alternating thereafter defines exactly two globally consistent state assignments. The preceding local test proves both are maximal independent sets. Hence the maximal independent sets are in a two-to-one correspondence with cyclic \(n\)-bit strings having an odd number \(j\) of ones and no consecutive zeros.

**3. Exact cardinality count.** Put \(k=n-j\). There must be at least as many occupied as empty rungs, so \(0\le k\le j\), equivalently \(\lceil n/2\rceil\le j\le n\). To count cyclic patterns with \(j\) nonempty and \(k\) pairwise nonadjacent empty rungs, distinguish one nonempty rung: there are \(n\) choices of its labeled position and \(\binom{j}{k}\) ways to choose which of the \(j\) following gaps contains one empty rung. Each unmarked pattern has exactly \(j\) possible distinguished occupied rungs, giving \(\frac nj\binom jk\) patterns. Each has precisely two state assignments when \(j\) is odd and none otherwise. Multiplication yields \(\frac{2n}{j}\binom{j}{n-j}\), proving the theorem for all \(n\ge3\).

**4. Bivariate generating function.** As a formal power series, temporarily admit the same cyclic-word counting expression at lengths \(n\ge1\). Setting \(a=zt(1+t)\), its generating series is

\[
2t\frac{\partial}{\partial t}\sum_{\substack{j\ge1\\j\text{ odd}}}\frac{a^j}{j}
=2t\frac{\partial}{\partial t}\operatorname{artanh}(a)
=\frac{2zt(1+2t)}{1-z^2t^2(1+t)^2}.
\]

The formal length-one and length-two contributions are \(2zt\) and \(4zt^2\). Subtracting them gives precisely the claimed \(n\ge3\) series. The statements about achievable sizes and extremal multiplicities follow by taking the lowest and highest odd exponents with nonzero coefficients. Complements of maximal independent sets are exactly inclusion-minimal vertex covers, establishing the cover interpretation.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The program constructs the labeled Möbius ladder independently, exhaustively tests independence and domination of every subset for each \(3\le n\le10\), compares every size coefficient with the closed expression, and checks the known ungraded Lucas-number identity and the extremal/parity formulas through \(n=200\). The exhaustive domain has exactly \(1{,}398{,}080\) candidate subsets. Observed result:

`VERIFY_OK exhaustive_n=3..10 masks=1398080 formula_and_OEIS_n=3..200 parity_extremal=passed`

Examples: \(D_3(z)=2z^3\), \(D_4(z)=8z^3\), \(D_5(z)=10z^3+2z^5\), and \(D_6(z)=4z^3+12z^5\). The infinite-family theorem is proved by the bijection, not inferred from these finite checks.

## Relationship to prior work

Dod (arXiv:1602.08250v1, first publicly posted 2016-02-26) defines the independent-domination polynomial and proves general identities, including concrete formulas for paths and cycles. The whole eleven-page preprint was inspected; it does not state an exact Möbius-ladder polynomial. Bautista-Ramos and Guillén-Galván (Journal of Integer Sequences 15 (2012), Article 12.7.8) give transfer-matrix enumerations for *all independent sets* on generalized Möbius ladders, a different predicate: independence alone does not enforce domination or maximality. OEIS A290608 already supplies the **ungraded total** number of maximal independent vertex sets on Möbius ladders, \(L_n-2\cos(2\pi n/3)\). Setting \(z=1\) in the formula recovers that known sequence; neither that total nor the classical independence-number bound is presented as new. The present result resolves the finer cardinality distribution and structural odd-parity restriction.

McSorley's “Counting Structures in the Möbius Ladder” (Discrete Mathematics 184 (1998), 137–164, DOI below) is an especially relevant priority risk. Its repository abstract was checked, but its full text could not be inspected, so earlier equivalent coverage under different terminology remains possible. The formula should not be regarded as independently certified or conclusively first in the literature.

## Limitations

The theorem covers the standard Möbius ladder on \(2n\) labeled vertices only for \(n\ge3\). It counts sets, not their symmetry orbits, and does not address weighted or constrained variants. The finite verifier corroborates but cannot replace the unrestricted proof. Priority is not completely settled because the complete text of McSorley's relevant paper was inaccessible; independent mathematical audit is not performed.

## References

1. Markus Dod, *The Independent Domination Polynomial*, arXiv:1602.08250v1 (submitted 2016-02-26), https://arxiv.org/abs/1602.08250 .
2. César Bautista-Ramos and Carlos Guillén-Galván, *Fibonacci Numbers of Generalized Zykov Sums*, Journal of Integer Sequences **15** (2012), Article 12.7.8, https://cs.uwaterloo.ca/journals/JIS/VOL15/Bautista/bautista4.pdf .
3. OEIS A290608, *Number of maximal independent vertex sets (and minimal vertex covers) in the n-Moebius ladder graph*, https://oeis.org/A290608 .
4. John P. McSorley, *Counting Structures in the Möbius Ladder*, Discrete Mathematics **184** (1998), 137–164, DOI:10.1016/S0012-365X(97)00086-1, repository abstract: https://opensiuc.lib.siu.edu/math_articles/93/ .
