# Bivariate enumeration and exponential scarcity of two-sided locating-dominating cycle partitions

## Finding

Let \(C_n\) be the labelled simple cycle with vertices \(0,1,\ldots,n-1\), and assume \(n\ge5\). Let \(\mathcal A_n\) consist of ordered partitions \((D,L)\) of its vertices with \(D\) dominating and \(L\) locating-dominating. Let \(\mathcal B_n\subseteq\mathcal A_n\) consist of partitions for which **both** \(D\) and \(L\) are locating-dominating. Vertices remain labelled: rotations and reversals are not identified.

Define \(A_n(t)=\sum_{(D,L)\in\mathcal A_n}t^{|L|}\) and \(B_n(t)=\sum_{(D,L)\in\mathcal B_n}t^{|L|}\). Then for every integer \(n\ge5\),

\[
A_n(t)=[z^n]\left(-z\frac{\partial}{\partial z}\log P_A(z,t)\right),\qquad
B_n(t)=[z^n]\left(-z\frac{\partial}{\partial z}\log P_B(z,t)\right),
\]

where

\[
P_A(z,t)=1-tz^2-t^2z^3-t^2z^4-t^2z^5-t^3z^6,
\]

\[
P_B(z,t)=1-tz^2-t^2z^4-(t^2+t^3)z^5-t^3z^6-t^4z^8.
\]

These are exact size-resolved enumerators, not just total counts. The associated cyclic binary words, with \(1\) denoting membership in \(L\), are precisely those avoiding the cyclic factors \(000\), \(111\), \(00100\) for \(\mathcal A_n\); the words in \(\mathcal B_n\) must also avoid \(11011\).

Put \(a_n=A_n(1)\) and \(b_n=B_n(1)\). There are unique roots \(\alpha,\beta\in(0,1)\) of \(P_A(z,1)=0\) and \(P_B(z,1)=0\) respectively, and

\[
\alpha\approx0.636882916801845,\qquad
\beta\approx0.660992531890120.
\]

In particular, the precise exponential scarcity law is

\[
\frac{b_n}{a_n}\sim\left(\frac{\alpha}{\beta}\right)^n
\approx(0.963525132395470)^n\quad(n\to\infty).
\]

Thus among partitions into a dominating set and a locating-dominating set, the fraction whose two parts are both locating-dominating tends to zero exponentially.

## Assumptions and scope

All graphs are simple. A set \(S\subseteq V(C_n)\) dominates if every vertex outside it has a neighbour in it. It is locating-dominating (LD) if, additionally, the sets \(N(u)\cap S\) are nonempty and pairwise different as \(u\) ranges over vertices outside \(S\). The partition is ordered: \((D,L)\) designates the distinguished LD side. The variable \(t\) marks the number of vertices of \(L\), and \([z^n]\) denotes ordinary coefficient extraction in formal series over \(\mathbb Z[t]\). All assertions about the cycle partition counts require \(n\ge5\), since shorter cycles have distinct neighbourhood-coincidence behaviour.

## Proof

**1. Local characterization.** Encode each partition by its cyclic binary word \(w_0\cdots w_{n-1}\), with ones in \(L\). The set \(L\) dominates precisely when \(000\) is absent; likewise \(D\) dominates precisely when \(111\) is absent. Suppose \(L\) dominates. If distinct zeros have the same set of neighbouring ones, that set is nonempty. On a simple cycle of length at least five, two distinct vertices have at most one common neighbour. The common nonempty set must therefore be a single one-vertex neighbour, lying between the two zeros at distance two. Their respective other neighbours are then zeros, producing the cyclic factor \(00100\). Conversely, this factor produces two distinct zeros whose only neighbour in \(L\) is its central one. Therefore \(L\) is LD precisely when \(000\) and \(00100\) are absent; \(D\) is LD precisely when \(111\) and \(11011\) are absent. Together with domination of \(D\), these are the stated factor-avoidance descriptions. The argument uses labelled vertices and does not quotient by graph automorphisms.

**2. Run representation.** Avoidance of \(000\) and \(111\) forces all maximal runs of zeros and ones to have lengths one or two, alternating around the cycle. Write the consecutive ordered pairs of run lengths as \((a_i,b_i)\in\{1,2\}^2\), with \(a_i\) a zero-run and \(b_i\) its succeeding one-run. The factor \(00100\) occurs exactly when \(a_i=a_{i+1}=2\) and \(b_i=1\). The factor \(11011\) occurs exactly when \(b_i=b_{i+1}=2\) and \(a_{i+1}=1\). Indices here are cyclic. Each pair contributes \(a_i+b_i\) vertices and \(b_i\) members of \(L\).

**3. Transfer matrices and determinants.** For one-sided partitions, use states \(a\in\{1,2\}\). The transition \(a\to c\) has weight \(\sum_{b=1}^2 z^{a+b}t^b\) except that \(a=c=2\) forbids \(b=1\). The resulting matrix is

\[
T_A=\begin{pmatrix}
z^2t+z^3t^2&z^2t+z^3t^2\\
z^3t+z^4t^2&z^4t^2
\end{pmatrix},\qquad \det(I-T_A)=P_A(z,t).
\]

For two-sided partitions use states \((a,b)\in\{1,2\}^2\), with transition \((a,b)\to(c,e)\) of weight \(z^{a+b}t^b\) if and only if

\[
\neg(a=c=2\ \text{and}\ b=1),\qquad
\neg(b=e=2\ \text{and}\ c=1);
\]

otherwise its weight is zero. Direct four-by-four determinant expansion gives \(\det(I-T_B)=P_B(z,t)\). Both matrices have entries of positive \(z\)-valuation, so formal logarithms are valid. The formal identity

\[
-z\frac{\partial}{\partial z}\log\det(I-T)
= z\frac{\partial}{\partial z}\sum_{k\ge1}\frac{\operatorname{tr}(T^k)}k
\]

counts labelled cyclic words: a cyclic word with \(k\) zero-runs admits \(k\) possible choices of a distinguished zero-run, while the derivative weights each run sequence by its total length \(n\). Thus the cyclic trace contributes exactly \(n/k\) times each rooted run cycle and counts every word once on the fixed labelled cycle. This proves both coefficient formulas. The run encoding is unambiguous for \(n\ge5\); no artificial short-cycle terms from the rational series are asserted as partition counts.

**4. Dominant poles and strict separation.** At \(t=1\), each denominator is of form \(1-\sum_j c_jz^j\) with strictly positive coefficients \(c_j\) on an exponent set whose gcd is one: \(\{2,3,4,5,6\}\) for \(P_A\), and \(\{2,4,5,6,8\}\) for \(P_B\). It has a unique positive real zero in \((0,1)\). By the triangle inequality, any other complex zero has modulus at least the positive zero; equality forces all the powers of its phase corresponding to the supported exponents to equal one, and the gcd-one condition forces the positive zero itself. Its derivative is strictly negative, so the zero is simple. Consequently, for some constants \(q_A,q_B\in(0,1)\),

\[
a_n=\alpha^{-n}(1+O(q_A^n)),\qquad
b_n=\beta^{-n}(1+O(q_B^n)).
\]

For \(0<z\le2/3\),

\[
P_B(z,1)-P_A(z,1)=z^3(1-z^2-z^5)>0.
\]

Since \(P_A(2/3,1)<0\), one has \(\alpha<2/3\), hence \(P_B(\alpha,1)>0\). Strict decrease of \(P_B(z,1)\) on positive \(z\) implies \(\beta>\alpha\). Dividing the coefficient asymptotics proves the displayed exponential ratio.

## Verification

The standalone file `verify_cycle_partitions.py` (standard-library-only, invoked with `python3 verify_cycle_partitions.py`) constructs the two transfer matrices independently, expands their determinants by the permutation formula, and extracts all size-marked coefficients through length sixteen. It separately enumerates every labelled vertex subset of every cycle of lengths \(5\) through \(16\), directly tests the graph-neighbourhood definitions of dominating and LD sets, and checks the cyclic forbidden-factor characterization for each subset. Every exact coefficient agrees. The terminal output is `VERIFY_OK n=5..16 all labelled 2^n subsets; determinants via permutations; independent neighborhood and forbidden-word checks`. This finite replay is a consistency check; the all-length statement follows from the proof above.

Univariate examples \((a_n,b_n)\) at \(n=5,6,7,8,9,10\) are \((10,10),(17,14),(21,14),(38,30),(57,36),(92,72)\). The univariate sequence \((a_n)\) coincides with the previously tabulated OEIS A001636; its bare unweighted numerical sequence is **not** claimed as new.

## Relationship to prior work

Chakraborty, Foucaud, Henning and Laihonen prove that every isolate-free graph admits a partition into a dominating set and an LD set, using structural arguments and a polynomial-time construction [1]. Their paper poses and discusses stronger LD-partition questions, but does not give these labelled cycle enumerators, the two-sided bivariate determinant, or the exponential rarity law. Foucaud, Maniya, Paul and Pradhan establish the existence of two LD parts for other graph classes [2], not these exact cycle counts. OEIS A001636 already records the unweighted sequence matching \(a_n\) [3]; that known sequence is subtracted from the originality claim. The point here is the simultaneously size-resolved one- and two-sided enumeration, especially the strict disparity of the two asymptotic growth constants.

## Limitations

The local characterization and enumeration concern ordinary simple cycles of length at least five. Neither arbitrary graphs nor non-ordered partitions nor symmetry-orbit counts are classified. The exponential constant describes the ratio of labelled partition counts, not random graphs or randomly sampled LD sets under another distribution. The formulas and proof have not received independent mathematical audit. Historical priority for the bivariate and two-sided identities is assessed against accessible literature and databases, not certified absolutely.

## References

[1] D. Chakraborty, F. Foucaud, M. A. Henning, T. Laihonen, *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*, Electronic Journal of Combinatorics 33 (2026), P1.51, published 2026-03-13, DOI: 10.37236/14049. Author-hosted full article: https://perso.limos.fr/ffoucaud/Publications/Papers/J64_Partitioning-LD-D_E-JC_2026.pdf

[2] F. Foucaud, P. V. Maniya, K. Paul, D. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933 (first posted 2025-06-15), https://arxiv.org/abs/2506.12933

[3] OEIS Foundation, *A001636: A Fielder sequence*, https://oeis.org/A001636 (known matching univariate recurrence; no claim to novelty of its terms).
