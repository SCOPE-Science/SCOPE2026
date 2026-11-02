# Exact support and rank census of binary linear diameter-three anticodes

## Finding

For every integer \(n\ge0\), let \(\mathcal L_2(n,3)\) be the set of linear subspaces of \(\mathbb F_2^n\) whose Hamming diameter is at most three. The exact number is
\[
|\mathcal L_2(n,3)|=1+n+2\binom n2+6\binom n3+10\binom n4.
\]
The binomial coefficient is zero when the lower index exceeds \(n\). The support-by-dimension census of full-support codes is

| dimension \(k\) | support \(s\) | number on a fixed labelled support |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 1, 2, 3 | 1 each |
| 2 | 2, 3, 4 | 1, 4, 6 respectively |
| 3 | 3, 4 | 1, 4 respectively |

All other combinations have count zero. In particular, the maximal support size is four, with ten full-support codes on any prescribed four coordinates, split into six codes of dimension two and four of dimension three. In the notation of the fixed-diameter growth theorem of Horlemann--Ravi, \(\sigma_2(3)=4\), and
\[
|\mathcal L_2(n,3)|=\frac5{12}n^4+O(n^3).
\]
The dimension-refined enumerator \(T_n(u)=\sum_{C\in\mathcal L_2(n,3)}u^{\dim C}\) is
\[
\begin{aligned}
T_n(u)={}&1+\left(n+\binom n2+\binom n3\right)u\\
&+\left(\binom n2+4\binom n3+6\binom n4\right)u^2\\
&+\left(\binom n3+4\binom n4\right)u^3.
\end{aligned}
\]

## Assumptions and scope

The space \(\mathbb F_2^n\) has labelled coordinates and Hamming distance. Subspaces, rather than their generator matrices or permutation-isomorphism classes, are counted. All dimensions, including the zero subspace, are included. A support coordinate is a coordinate on which at least one codeword is nonzero. The theorem holds for every integer \(n\ge0\), including short lengths; zero-padding a full-support code to a larger labelled coordinate set is allowed. All statements concern **linear** diameter at most three, not arbitrary non-linear anticodes and not minimum-distance-three codes.

## Proof

**Dimension and support restrictions.** For a linear subspace \(C\), the difference of two codewords is a codeword. Hence its diameter is the maximum Hamming weight of a codeword. If \(k=\dim C\), take a reduced-row-echelon generator matrix. The sum of all \(k\) basis rows has a one in each of its \(k\) pivot columns, so diameter at most three implies \(k\le3\).

Restrict \(C\) to its support of size \(s\). Every one of the \(s\) coordinate functionals on the \(k\)-dimensional message space is nonzero. Therefore each coordinate is one in exactly \(2^{k-1}\) of the \(2^k\) codewords. For \(k\ge1\),
\[
 s2^{k-1}=\sum_{c\in C}\mathrm{wt}(c)\le3(2^k-1).
\]
Consequently \(s\le3\) for \(k=1\), \(s\le4\) for \(k=2\), and \(s\le5\) for \(k=3\).

**The five-coordinate obstruction.** Suppose a three-dimensional full-support code of support five existed. Regard its generator's five columns as five nonzero vectors, counted with multiplicity, in \(\mathbb F_2^3\). For each of the seven nonzero message vectors \(u\), the corresponding hyperplane \(H_u=\{v:u\cdot v=0\}\) must contain at least two of these five columns, since the codeword indexed by \(u\) has weight at most three. Each nonzero column lies in exactly three such hyperplanes. Thus the seven intersection sizes are six twos and one three: their sum is fifteen, and each is at least two.

The number of pairs of column positions simultaneously contained in a hyperplane, summed over all seven hyperplanes, is therefore
\[
6\binom22+\binom32=9.
\]
On the other hand, any pair of nonzero columns in \(\mathbb F_2^3\) is contained in at least one two-dimensional hyperplane: the span of two columns has dimension at most two. The sum must thus be at least \(\binom52=10\), a contradiction. Hence **all** linear diameter-three anticodes have support at most four.

**Classification on each fixed support.** Support zero admits only the zero code. For a full-support one-dimensional code, its unique nonzero vector is the all-ones vector on that support; it is allowed precisely for \(s\in\{1,2,3\}\).

For support two, the sole full-support dimension-two code is \(\mathbb F_2^2\). On support three, every two-dimensional code is a hyperplane described by a nonzero parity-check word \(h\). It has full support unless \(h\) has weight one. There are \(7-3=4\) such hyperplanes; the unique dimension-three space also qualifies.

On support four, consider dimension two. Its generator has four nonzero columns in \(\mathbb F_2^2\). Each of the three nonzero messages must produce a word with at least one zero, so all three possible nonzero column types must occur. Their multiplicities must be \(2,1,1\). Modulo invertible row operations, which permute the three nonzero types, the resulting subspace is uniquely specified by the pair of positions carrying the repeated type. There are \(\binom42=6\) choices.

For dimension three on four positions, write the hyperplane \(C=\{x:h\cdot x=0\}\) for nonzero \(h\). It has full support precisely when \(\mathrm{wt}(h)\ge2\). It has maximum codeword weight at most three precisely when the all-ones word does not belong to \(C\), i.e., \(\mathrm{wt}(h)\) is odd. Thus \(\mathrm{wt}(h)=3\), yielding exactly four possible hyperplanes. A dimension-four subspace contains the all-ones vector and is excluded.

These exhaust all dimensions and supports. Choosing any labelled support of size \(s\), applying its full-support classification, and extending by zeros gives the bijection
\[
|\mathcal L_2(n,3)|=\sum_{s=0}^4 a(s)\binom ns,
\quad (a(0),a(1),a(2),a(3),a(4))=(1,1,2,6,10).
\]
Sorting instead by dimension yields the displayed \(T_n(u)\). The top nonzero coefficient is \(10\binom n4\), so the degree is four and the leading coefficient is \(10/4!=5/12\). This proves all assertions.

## Verification

`verify.py` independently generates every linear subspace by adjoining vectors and closing under binary addition, without using the classification proof. For every ambient length from zero through seven, it tests the maximum Hamming weight, dimensions and support sizes and compares the resulting counts against the formulas. The unrestricted full-subspace totals in dimensions zero through seven are \(1,2,5,16,67,374,2825,29212\). The respective numbers satisfying diameter at most three are \(1,2,5,16,51,136,307,610\). The program prints `VERIFY_OK` after all comparisons.

These finite enumerations check arithmetic and definitions; they are not used to prove the all-length result. The proof above supplies the all-length exclusion of support five and the exact support-four classification.

## Relationship to prior work

Horlemann and Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, first publicly posted on October 22, 2026, give the general support decomposition in Proposition 4.3 and bounds on the fixed-diameter polynomial degree in Theorem 4.6. Their bound for binary diameter three gives only \(3\le\sigma_2(3)\le6\). They do **not** list the support coefficients \(a_2(s,3)\), the exact degree, or the rank-refined polynomial. The present result supplies these values, while expressly using their definitions and support-decomposition viewpoint. Prior optimal-anticode classifications address maximum dimension rather than the number of **all** linear subspaces of maximum weight at most three. In particular, counting only dimension-three extremizers would omit six of the ten maximal-support configurations.

## Limitations

No inference is made about non-linear diameter-three anticodes, other fields, or diameter at least four. The originality comparison is based on the inspected full primary paper, accessible related literature, mathematical-record searches and locally accessible previous claims. Older or unindexed equivalent enumerations cannot be ruled out categorically. Independent mathematical audit has not been performed.

## References

1. Anna-Lena Horlemann and Ananthakrishnan Ravi, *The Asymptotic Number of Anticodes in Hamming Spaces*, arXiv:2610.31618v1, submitted October 22, 2026. https://arxiv.org/html/2610.31618v1. Relevant: Lemma 4.1, Proposition 4.3, Theorem 4.6, Remark 4.7.
2. A. Ravagnani, *Generalized weights: an anticode approach*, Journal of Pure and Applied Algebra 220 (2016), 1946–1962; arXiv:1410.7207. For the broader concept of linear anticodes and maximal dimension, not the present complete enumeration.
3. A. Di Giusto, E. Gorla and A. Ravagnani, *A distance-free approach to generalized weights*, arXiv:2512.17542 (2025). Background on extremal code support; not asserted to give a diameter-three census.
