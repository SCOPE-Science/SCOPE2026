# Exact four-gram profile capacity of binary circular words with runs of length at most two

## Finding

Let \(n\ge 1\). A binary circular word is read with cyclic wraparound, including when \(n<4\). Require that neither \(000\) nor \(111\) occurs in any cyclic length-three window. For a permitted circular word \(w\), define its **complete ordered four-gram multiplicity vector** \(P(w)=(N_e(w))_{e\in E}\), where

\[
E=(0010,0011,0100,0101,0110,1001,1010,1011,1100,1101),
\]

and \(N_e(w)\) is the number of cyclic starting positions whose length-four window is \(e\). The order in \(E\) names vector coordinates; the order of reads is *not* observed. Let \(C_n\) be the number of different attainable vectors. Then

\[
\boxed{\sum_{n\ge1}C_nz^n
=\frac{1+z^6}{(1-z^2)(1-z^3)^2(1-z^4)(1-z^6)}-1
-\frac{z^6}{(1-z^3)^2}-\frac{z^6}{(1-z^2)(1-z^4)}.}
\]

Consequently \(C_n\) is a degree-four quasipolynomial, for positive \(n\), with **exact least period twelve** and leading term \(n^4/5184\). It is also the exact largest size of a zero-error code under this constrained, noiseless read-multiset channel: choose one representative circular word for each attainable vector.

A complete realizability test for a proposed vector is given in the proof. Specifically, balanced nonnegative four-gram counts are realizable unless all their positive edges form one of two explicitly classified disconnected two-cycle unions. The first values \((C_2,\ldots,C_{18})\) are

\[
(1,2,2,2,5,4,7,10,11,14,22,22,29,38,43,50,67).
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Words have positive length, are circular, and may have a proper period. Both constant cyclic runs of length three are excluded; equivalently, every maximal run of either symbol has length at most two. A length-four factor is read cyclically even if the circle has fewer than four positions. Counts retain their factor labels and their multiplicities but not their order of occurrence. Cyclic rotations define the same source necklace; neither complementation nor reversal is imposed as an identification. The statement is about exact noiseless observations, not unordered sets of *distinct* factors or a linear (noncyclic) reading convention.

Use coordinate names in the order displayed above:
\[
(a,b,c,d,e,f,g,h,i,j)=
(N_{0010},N_{0011},N_{0100},N_{0101},N_{0110},N_{1001},N_{1010},N_{1011},N_{1100},N_{1101}).
\]

A candidate is admissible precisely if these ten coordinates are nonnegative integers, sum to \(n>0\), satisfy the balance equations below, and do **not** belong to either disconnected family listed below. This is a finite arithmetic characterization for any input \(n\).

## Proof

**1. Read-incidence model and flow equations.** Form the order-three de Bruijn digraph whose arcs are the ten permitted four-grams \(E\); arc \(x_1x_2x_3x_4\) goes from \(x_1x_2x_3\) to \(x_2x_3x_4\). The six possible vertices are \(001,010,011,100,101,110\). A circular word with no forbidden triple induces a closed walk in this graph, using arc \(e\) exactly \(N_e(w)\) times. Therefore its count vector is a nonnegative integral circulation:

\[
\begin{aligned}
f&=a+b,&e&=b+h,&i&=a+b-c,\\
j&=h+c-a,&g&=c+d-a.
\end{aligned}
\]

Conversely, a nonzero, nonnegative integral circulation whose **positive-edge support is weakly connected** has a directed Euler circuit after edge multiplicities are expanded. Reading the first symbol of each successive arc produces the desired circular binary word. This proves necessity and sufficiency of the balance, nonnegativity, and positive-support connectedness conditions. Isolated vertices carrying no positive edge are ignored.

**2. Exact enumeration of all nonnegative circulations.** The five free variables are \((a,b,c,d,h)\). Nonnegativity of the other five amounts to

\[
c\le a+b,\qquad a\le c+d,\qquad a\le c+h.
\]

Split uniquely into two cases. If \(a\ge c\), set \(t=a-c\ge0\), \(u=d-t\ge0\), \(v=h-t\ge0\). Then \(b,c,t,u,v\) are independent nonnegative integers, and the sum of all ten coordinates is

\[
n=4b+3c+6t+2u+3v.
\]

If \(c>a\), set \(s=c-a\ge1\), \(w=b-s\ge0\), \(u=d\ge0\), and \(v=h\ge0\). The independent parameters are \(a,w,s,u,v\), and

\[
n=3a+4w+6s+2u+3v.
\]

Hence the generating function for **all** balanced nonnegative count vectors, including the zero vector and disconnected supports, is

\[
B(z)=\frac{1+z^6}{(1-z^2)(1-z^3)^2(1-z^4)(1-z^6)}.
\]

Each vector is counted exactly once: the two cases are disjoint, the displayed parameters recover the original ten arc counts, and the monomials in either case have total exponent equal to the number of arcs.

**3. Exactly two disconnected-support families.** The graph has exactly six simple directed cycles, with vertex sets (writing only the vertices)

\[
\begin{array}{ll}
A: (001,010,100),&B:(011,110,101),\\
C:(010,101),&D:(100,001,011,110),\\
E_6:(010,100,001,011,110,101),&F_6:(010,101,011,110,100,001).
\end{array}
\]

These are exhaustive by following the one or two outgoing arcs at each of the six vertices and closing a simple path. Every nonzero integral circulation decomposes into simple directed cycles. Among the six listed cycles, the **only** vertex-disjoint pairs are \((A,B)\) and \((C,D)\). Moreover, every other simple cycle intersects both members of either such pair, so a disconnected circulation consists of positive multiples of exactly the two cycles in one pair, and nothing else.

For \((A,B)\), the first cycle has arcs \(0010,0100,1001\), and the second has arcs \(0110,1101,1011\). A disconnected profile consists of \(x\ge1\) copies of the first and \(y\ge1\) copies of the second, giving the length contribution \(3x+3y\) and generating function

\[
D_{AB}(z)=\frac{z^6}{(1-z^3)^2}.
\]

For \((C,D)\), the two-cycle has arcs \(0101,1010\); the four-cycle has arcs \(1001,0011,0110,1100\). Positive multiplicities \(x,y\) on the four-cycle and two-cycle respectively give length \(4x+2y\), hence

\[
D_{CD}(z)=\frac{z^6}{(1-z^4)(1-z^2)}.
\]

These two disconnected families are disjoint. The only remaining excluded vector is the zero circulation, contributing \(1\). Thus \(C(z)=B(z)-1-D_{AB}(z)-D_{CD}(z)\), proving the boxed identity and the exact arithmetic realizability criterion.

**4. Quasipolynomial and code capacity.** Every denominator factor divides a power of \(1-z^{12}\), so coefficients for positive degrees form a quasipolynomial of degree at most four and period dividing twelve. The pole at \(z=1\) has order five and leading singular coefficient \(1/216\); therefore the leading coefficient of \(C_n\) is \(1/(216\cdot4!)=1/5184\). Direct cancellation of the rational expression leaves genuine poles at primitive third, fourth, and sixth roots of unity, so a smaller quasipolynomial period cannot work. Finally, two circular words are indistinguishable exactly when their complete four-gram count vectors agree. Selecting one word for each attainable vector gives a zero-error code of size \(C_n\); no larger code can distinguish more than \(C_n\) different observations.

## Verification

The accompanying standard-library-only `verify_dual_rll_fourgram.py` independently generates all nonnegative circulations from the two parameter branches through length 44. It tests support connectivity directly rather than assuming the disconnected-cycle classification, compares the resulting counts with the rational generating function, and constructs a cyclic Euler tour for **every** feasible profile through length 44. Each constructed word is checked against its prescribed ten counts and the two forbidden triples. For lengths 1 through 18 it also enumerates every labeled binary circular word and compares the full *sets* of profiles, not just their cardinalities.

Running `python verify_dual_rll_fourgram.py` produced:

```text
VERIFY_OK literal_all_binary_n=1..18 exact_flow_profiles_n=1..44 euler_tours=12596 disconnected_support_classification=PASS gf_coefficients=PASS
profile_counts_n2..18= [1, 2, 2, 2, 5, 4, 7, 10, 11, 14, 22, 22, 29, 38, 43, 50, 67]
```

These finite tests corroborate the proof but do not replace the graph-theoretic and generating-function arguments establishing the theorem for all lengths.

## Relationship to prior work

Kiah, Puleo and Milenkovic [1] formulate sequence-profile equivalence and use restricted de Bruijn graphs and Ehrhart theory to obtain general counting and growth statements. Their graph model is applicable here, but the inspected enumeration and examples do not supply this two-forbidden-triple, cyclic length-four exact generating function or its two necessary disconnected-support subtractions.

Chee and collaborators [2] treat maximum-length run-length-limited de Bruijn sequences with distinct prescribed windows and enumerate lengths and necklace constructions; their invariant is not the number of **multiplicity profiles** of all allowed circular source words. Chee and collaborators [3] count constrained de Bruijn codes with local restrictions on repeated windows, not all complete length-four read histograms under both triple exclusions. Jacquet, Knessl and Szpankowski [4] study first-order Markov type counts and asymptotics, furnishing a related balanced-frequency framework but not this exact third-order restricted graph computation. Agur, Fraenkel and Klein [5] count binary cyclic strings avoiding both constant triples, which is a different statistic from the number of distinct four-gram profiles.

The contribution here is the exact feasible-profile characterization, all-length rational generating function, optimal zero-error code capacity, and exact quasipolynomial period for the doubly bounded-run cyclic model. General graph enumeration principles and classical Eulerian existence are not claimed as new.

## Limitations

The statement is only for the binary alphabet, cyclic four-gram multiplicities, and simultaneous avoidance of cyclic \(000\) and \(111\). It does not count source words within each profile fiber, does not treat partial/noisy reads, and does not extend the closed expression to arbitrary read lengths. An equivalent formula hidden in broader Markov-type or transfer-matrix literature remains a residual priority risk. The all-length argument is a mathematical proof, while the associated computations are finite and independently scientifically unaudited.

## References

1. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1, first public February 2, 2015. https://arxiv.org/html/1502.00517v1
2. Y. M. Chee, T. Etzion, T. L. Nguyen, D. H. Ta, V. D. Tran and V. K. Vu, *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454v1, first public March 3, 2024. https://arxiv.org/html/2403.01454v1
3. Y. M. Chee, T. Etzion, H. M. Kiah, A. Vardy, V. K. Vu and E. Yaakobi, *Constrained de Bruijn Codes: Properties, Enumeration, Constructions, and Applications*, arXiv:2005.03102v1, first public May 6, 2020. https://arxiv.org/html/2005.03102v1
4. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), 387–400. https://dmtcs.episciences.org/en/articles/2768/download
5. Z. Agur, A. S. Fraenkel and S. T. Klein, *The Number of Fixed Points of the Majority Rule*, Discrete Mathematics 70 (1988), 295–302. https://doi.org/10.1016/0012-365X(88)90005-2
