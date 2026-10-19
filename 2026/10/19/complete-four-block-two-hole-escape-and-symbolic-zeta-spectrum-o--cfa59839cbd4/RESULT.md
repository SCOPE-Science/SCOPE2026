# Complete four-block two-hole escape and symbolic zeta spectrum of the doubling map

## Finding

For the doubling map \(T(x)=2x\pmod 1\), consider every unordered pair \(B=\{u,v\}\) of **distinct length-four binary words**. Let \(H_B\) be the union of their two binary cylinders (each of Lebesgue measure \(1/16\)); let \(P_B(n)\) be the Lebesgue measure of points avoiding \(H_B\) at times \(0,1,\ldots,n-1\). Put \(\gamma_B=-\lim_{n\to\infty}n^{-1}\log P_B(n)\).

**Complete classification.** Across all \(\binom{16}{2}=120\) pairs, there are exactly **16 distinct escape rates** and **26 distinct symbolic dynamical zeta functions** for their survivor subshifts. The \(16\) escape-rate classes, listed in increasing order of their associated Perron radii \(r_B=2e^{-\gamma_B}\), have multiplicities

\[
(2,22,10,4,6,8,4,4,28,4,4,2,4,4,6,8).
\]

Let \(r_-\) be the unique root greater than one of \(t^3-t^2-1=0\), and \(r_+\) the unique root greater than one of \(t^3-t^2-t-1=0\). The sharp bounds for **every** pair are

\[
\boxed{\log(2/r_+)\leq\gamma_B\leq\log(2/r_-)}.
\]

The **fastest-escape** pairs (equality on the right, exactly two) are \(\{0011,0101\}\) and \(\{1010,1100\}\). The **slowest-escape** pairs (equality on the left, exactly eight) are

\[
\begin{gathered}
\{0000,0001\},\quad\{0000,1000\},\quad\{0000,1111\},\quad\{0001,1000\},\\
\{0101,1010\},\quad\{0111,1110\},\quad\{0111,1111\},\quad\{1110,1111\}.
\end{gathered}
\]

The rate fails to determine even the **symbolic periodic-orbit counts** among slowest-escape pairs: using the usual Artin–Mazur zeta function of binary itineraries,

\[
\zeta_{\{0000,0001\}}(z)=\frac{1}{1-z-z^2-z^3},\qquad
\zeta_{\{0000,1111\}}(z)=\frac{1}{(1+z)(1+z^2)(1-z-z^2-z^3)}.
\]

## Assumptions and scope

Work in the full one-sided binary shift \(\{0,1\}^{\mathbb N}\) with its fair Bernoulli measure. A word denotes a cylinder of its initial digits. Under binary coding, this is the Lebesgue-measure model for the doubling map, apart from countably many ambiguous dyadic endpoints, which do not affect the finite-time survival probabilities or escape rates. **The zeta function is that of the symbolic survivor shift**, counting periodic binary itineraries, not a claim of an identical interval-map periodic-point count at ambiguous boundaries. Each pair specifies a simultaneous *fixed union* of two length-four cylinder holes; there is no time-varying switching, parameter limit, or claim for other hole lengths.

There are \(16\) binary length-four words and \(120\) unordered distinct pairs. The classifications above and below quantify over **all** these pairs, not over selected examples.

## Proof

**Step 1: Exact finite-time coding.** Index the three-digit states by \(i=0,\ldots,7\). For each forbidden pair \(B\), construct the nonnegative integer matrix \(A_B\) of size \(8\) by

\[
(A_B)_{ij}=\sum_{b\in\{0,1\}}\mathbf1_{\{j=(2i+b)\bmod8\}}\mathbf1_{\{2i+b\notin B\}}.
\]

Here the integers \(0,\ldots,15\) in the final condition encode four-bit words. The transition keeps the final three bits and appends the new bit; deleting the two forbidden transitions enforces exactly the desired hole exclusion. For every integer \(n\ge0\), the \(n\)-step survival probability therefore equals

\[
P_B(n)=2^{-(n+3)}\mathbf1^{\mathsf T}A_B^n\mathbf1.
\]

This identity also gives \(P_B(0)=1\). The adjacency matrices are nonnegative, and their spectral radii \(r_B\) are strictly greater than one by the exact isolation below. By Perron–Frobenius theory and the Gelfand formula for nonnegative matrices, \(\lim_{n\to\infty}(\mathbf1^{\mathsf T}A_B^n\mathbf1)^{1/n}=r_B\). Hence \(\gamma_B=\log(2/r_B)\).

**Step 2: Symbolic periodic data.** Each cyclic path of length \(n\) in the three-block graph corresponds to one binary itinerary whose period divides \(n\), counted with its starting position. Thus the number of symbolic fixed points of the \(n\)-th shift iterate is \(\operatorname{tr}(A_B^n)\), and the formal power-series identity

\[
\zeta_B(z)=\exp\!\left(\sum_{n\ge1}\frac{\operatorname{tr}(A_B^n)}{n}z^n\right)=\frac1{\det(I-zA_B)}
\]

holds without requiring irreducibility.

**Step 3: Exact finite classification.** For each of the \(120\) unordered pairs, compute the integer characteristic polynomial \(p_B(t)=\det(tI-A_B)\) by the Faddeev–LeVerrier trace recurrence, which involves only integer additions, multiplications, and exact divisions. The \(120\) polynomials reduce to exactly **26 distinct degree-eight characteristic polynomials**, hence to exactly \(26\) zeta functions via Step 2.

For every one of the \(26\) polynomials, form its square-free part over the rationals and a rational Sturm sequence. The sign-variation count certifies that the largest positive real zero lies in exactly one of the following pairwise-disjoint rational intervals, with no real zero to the right. Each row gives the number of forbidden pairs in that class and a representative pair. The polynomial shown vanishes at the **largest positive root** within that row's rational interval; the full characteristic polynomials for all pairs are recomputed by the standalone checker.

| Class | Number of pairs | Representative words | Root interval \( (L,U)/10^6 \) | Polynomial for \(r_B\) |
|---:|---:|:---|:---|:---|
| 1 | 2 | 0011, 0101 | \(\frac{1465571}{10^6}<r<\frac{1465572}{10^6}\) | \( t^3-t^2-1 \) |
| 2 | 22 | 0001, 0111 | \(\frac{1618033}{10^6}<r<\frac{1618034}{10^6}\) | \( t^2-t-1 \) |
| 3 | 10 | 0001, 0101 | \(\frac{1695620}{10^6}<r<\frac{1695621}{10^6}\) | \( t^3-t^2-2 \) |
| 4 | 4 | 0001, 0110 | \(\frac{1704902}{10^6}<r<\frac{1704903}{10^6}\) | \( t^5-t^4-t^3-1 \) |
| 5 | 6 | 0010, 0110 | \(\frac{1716672}{10^6}<r<\frac{1716673}{10^6}\) | \( t^4-2t^3+2t-2 \) |
| 6 | 8 | 0001, 0011 | \(\frac{1722083}{10^6}<r<\frac{1722084}{10^6}\) | \( t^4-t^3-t^2-t+1 \) |
| 7 | 4 | 0010, 1100 | \(\frac{1730508}{10^6}<r<\frac{1730509}{10^6}\) | \( t^6-2t^5+t^3-1 \) |
| 8 | 4 | 0000, 0111 | \(\frac{1734691}{10^6}<r<\frac{1734692}{10^6}\) | \( t^5-t^3-2t^2-2t-1 \) |
| 9 | 28 | 0000, 1001 | \(\frac{1754877}{10^6}<r<\frac{1754878}{10^6}\) | \( t^3-2t^2+t-1 \) |
| 10 | 4 | 0000, 0011 | \(\frac{1778479}{10^6}<r<\frac{1778480}{10^6}\) | \( t^5-t^4-t^3-t^2+1 \) |
| 11 | 4 | 0010, 1001 | \(\frac{1784598}{10^6}<r<\frac{1784599}{10^6}\) | \( t^5-2t^4+t^2-1 \) |
| 12 | 2 | 0000, 0110 | \(\frac{1788539}{10^6}<r<\frac{1788540}{10^6}\) | \( t^6-t^5-t^4-t^2-1 \) |
| 13 | 4 | 0000, 0101 | \(\frac{1794309}{10^6}<r<\frac{1794310}{10^6}\) | \( t^4-t^3-2t-1 \) |
| 14 | 4 | 0010, 0101 | \(\frac{1805094}{10^6}<r<\frac{1805095}{10^6}\) | \( t^6-2t^5+t^4-t^3-1 \) |
| 15 | 6 | 0000, 0010 | \(\frac{1812403}{10^6}<r<\frac{1812404}{10^6}\) | \( t^5-t^4-t^3-t-1 \) |
| 16 | 8 | 0000, 0001 | \(\frac{1839286}{10^6}<r<\frac{1839287}{10^6}\) | \( t^3-t^2-t-1 \) |

Every row has a nonempty class, and the multiplicities sum to \(120\). Distinct rows have disjoint certified isolating intervals. Thus there are exactly \(16\) distinct Perron radii and escape rates. The smallest and largest classes contain precisely the pairs stated in the Finding. Their representative characteristic polynomials factor respectively as \(t^2(t^3-t^2-1)^2\) and \(t^5(t^3-t^2-t-1)\). The two displayed zeta functions follow directly from their two factorizations \(t^5(t^3-t^2-t-1)\) and \(t^2(t+1)(t^2+1)(t^3-t^2-t-1)\).

This is an exhaustive finite exact proof of the full claim: the complete code recreates the matrices, checks every rational root isolation using rational Sturm variations, counts the \(26\) polynomials and \(16\) radii, and verifies the precise equality cases. The general-in-time statement follows from Steps 1–2, not from finite-trajectory extrapolation.

## Verification

Run the self-contained Python standard-library file `certify_binary_pair_holes.py` with `python3 certify_binary_pair_holes.py`. It checks all \(120\) distinct unordered pairs, exact Faddeev–LeVerrier characteristic polynomials, exact rational Sturm isolators, all \(16\) multiplicities and both extremizer lists. Independently, it directly enumerates forbidden-word-avoiding sequences and compares their counts to the matrix formula at \(n=0,\ldots,7\) for **all** pairs (\(960\) integer equality checks). Its rational root isolation is exact; floating-point eigenvalues do not enter the certificate. Finite enumeration covers the finite pair classification; the infinite-time escape and zeta formulas are proved mathematically above.

## Relationship to prior work

Ramsey, *Perturbing Subshifts of Finite Type: Two Words* (2019), develops a correlation-polynomial perturbation framework and large-word entropy estimates. Cheriyath and Agarwal, *Subshifts of Finite Type with a Hole* (first public 2019; updated 2022), derive general two-word hole generating functions, comparative inequalities and selected examples. In particular, their main simple comparison bounds for length at least three require a larger alphabet; their examples do not state an exhaustive binary four-block classification. Those general techniques determine individual spectral quantities in principle, but the sharp global \(120\)-pair ordering, its \(16\)/\(26\) multiplicities, and the full lists of equality cases require further finite algebraic comparisons. The distinction between identical escape rates and different symbolic periodic data is explicit here.

## Limitations

The classification is restricted to two *distinct* length-four binary cylinders with the fair binary source. It does not characterize arbitrary measurable holes, random switching or longer forbidden blocks. It makes no claim of new general correlation methods or of independent priority certification. Standard algebraic word-avoidance methods can reproduce individual cases, so related specialized tables may exist. Symbolic zeta functions must not be conflated with interval-map counts at the binary boundary identification.

## References

1. N. Ramsey, *Perturbing Subshifts of Finite Type: Two Words*, arXiv:1902.03352v1, first submitted 9 February 2019. https://arxiv.org/html/1902.03352v1.
2. H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767v1 (28 May 2019), relevant revised full text v5 (6 April 2022). https://arxiv.org/html/1905.11767v5.
