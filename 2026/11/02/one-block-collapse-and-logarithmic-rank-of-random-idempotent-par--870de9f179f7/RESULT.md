# One-block collapse and logarithmic rank of random idempotent partition endomorphisms

## Finding

Fix an integer \(r\ge 2\). For each positive integer \(m\), partition an \(rm\)-point set \(X\) into \(r\) specified blocks of size \(m\), and let \(T(X,\mathcal P)\) be its monoid of maps that send each entire block into a single (possibly different) block. Choose \(F_m\) uniformly from its idempotents. Its **block character** \(\chi(F_m)\) is the induced map on the \(r\) blocks; let \(K_m=|\operatorname{im}F_m|\).

Put
\[
H_c(m)=\sum_{k=1}^{m}\binom mk k^{cm-k}\qquad(c\in\mathbb Z_{\ge1}),
\quad \delta_r=r\log r-(r-1)\log(r-1),
\]
with natural logarithms, and set \(M_2=1\) and \(M_r=r(r-1)\) for \(r\ge3\).

**Theorem (fixed block count, growing block size).** As \(m\to\infty\) with \(r\) fixed:

1. Almost every idempotent has a **constant block character**, mapping every block into one block. More precisely,
   \[
   \Pr\bigl(\chi(F_m)\text{ is not constant}\bigr)
   \sim \frac{M_r}{r}\frac{H_{r-1}(m)H_1(m)}{H_r(m)},
   \qquad
   \lim_{m\to\infty}\frac1m\log\Pr\bigl(\chi(F_m)\text{ is not constant}\bigr)=-\delta_r.
   \]
2. Conditional on the rare event of nonconstant block character, with probability tending to one the character has exactly two fixed blocks and their inverse-image block counts are \(r-1\) and \(1\). For \(r=2\), this means the identity character.
3. The image rank obeys the logarithmic law
   \[
   \frac{K_m\log m}{m}\xrightarrow{\ \mathrm P\ }r.
   \]
   This convergence also holds conditional on a constant block character.

The finite enumerator \(H_c(m)\) and the exact idempotent-character decomposition below are included to specify the probability space and make the asymptotic reproducible. The existing exact enumeration of idempotents in uniform partition transformation monoids is prior work; the claim here is the **collapse law, exceptional-character exponent and shape, and joint image-rank concentration**, not a claim to first discover the finite enumeration.

## Assumptions and scope

The blocks are labeled, nonempty, pairwise disjoint and uniform in size. Transformations are total functions; multiplication is composition. An idempotent is a map \(f\) with \(f\circ f=f\). The block count \(r\) is fixed before sending \(m\) to infinity. No assertion is made for simultaneous growth of \(r\) and \(m\), for nonuniform block sizes, or for random maps not conditioned on idempotence.

The character \(e=\chi(f)\) of an idempotent is idempotent on the block-index set. Write \(\operatorname{Fix}(e)=\{j:e(j)=j\}\) and \(c_j=|e^{-1}(\{j\})|\), so \(c_j\ge1\) for every fixed block and \(\sum_{j\in\operatorname{Fix}(e)}c_j=r\). For an idempotent \(f\), its image equals its fixed-point set. Thus \(K_m\) is an ordinary transformation rank, not an idempotent-generation rank.

## Proof

**1. Exact character fibers.** For every idempotent character \(e\) and each fixed block \(j\), choose the image \(A_j\subseteq X_j\) of cardinality \(k_j\), then fix its points. There are \(\binom m{k_j}\) choices of \(A_j\). The remaining \(m-k_j\) points of the fixed block, together with all \(m(c_j-1)\) points in the other blocks sent to it by \(e\), may each map to any of the \(k_j\) image points. Hence the number of idempotents inducing this particular \(e\) equals
\[
\prod_{j\in\operatorname{Fix}(e)}
\left(\sum_{k=1}^{m}\binom mk k^{c_jm-k}\right)
=\prod_{j\in\operatorname{Fix}(e)}H_{c_j}(m). \tag{1}
\]
These choices are independent across the disjoint basins, and every idempotent is counted exactly once. Consequently, the total number is
\[
E_{r,m}=\sum_{\substack{e:[r]\to[r]\\e^2=e}}
\prod_{j\in\operatorname{Fix}(e)}H_{c_j}(m). \tag{2}
\]
There are exactly \(r\) constant characters, each contributing \(H_r(m)\), so the constant-character count is exactly \(rH_r(m)\). Given a constant character, \(\Pr(K_m=k)\) is exactly \(\binom mk k^{rm-k}/H_r(m)\) for \(1\le k\le m\).

**2. A logarithmic Laplace lemma.** For every fixed positive integer \(c\), put \(L=\log m\), and \(a_{c,m}(k)=\binom mk k^{cm-k}\). Then
\[
\log H_c(m)
=cm\bigl(\log m-\log\log m+\log c-1\bigr)+o(m). \tag{3}
\]
Moreover, if \(J_{c,m}\) is sampled with masses proportional to \(a_{c,m}(k)\), then
\[
\frac{J_{c,m}\log m}{m}\xrightarrow{\ \mathrm P\ }c. \tag{4}
\]
Here is a direct proof including tail control. If \(k=\lfloor um/L\rfloor\) and \(u\) varies in a fixed compact subinterval of \((0,\infty)\), the binomial bound \(\log\binom mk=O(m\log L/L)=o(m)\) is uniform, and
\[
\log a_{c,m}(k)
=cm(L-\log L)+m\bigl(c\log u-u\bigr)+o(m) \tag{5}
\]
uniformly. The continuous strictly concave function \(c\log u-u\) has unique maximizer \(u=c\), with maximum \(c\log c-c\).

It remains to rule out other scales. For \(k\le\varepsilon m/L\), use \(-k\log k\le0\) and \(\log\binom mk\le m h(\varepsilon/L)=o(m)\), where \(h(t)=-t\log t-(1-t)\log(1-t)\), to obtain
\[
\log a_{c,m}(k)
\le cm(L-\log L)+cm\log\varepsilon+o(m).
\]
For \(k\ge M m/L\) write \(u=kL/m\); if \(M\ge1\) and \(m\) is large, then \(\log k\ge L-\log L\), \(\binom mk\le2^m\), and therefore
\[
\log a_{c,m}(k)
\le cm(L-\log L)+m\bigl(c\log u-u/2+\log2\bigr).
\]
The supremum of the last parenthesis for \(u\ge M\) tends to \(-\infty\) as \(M\to\infty\). Taking a small \(\varepsilon\), a large \(M\), and then applying the maximum principle to (5) proves (3). On every closed set of scaled values bounded away from \(c\), the maximum is strictly below that at \(c\); there are at most \(m\) summands, whose logarithmic number is \(o(m)\). This gives (4). The argument uses no assertion about a finite experiment proving an infinite limit.

**3. Competing block characters.** For an idempotent character \(e\) with fixed-block basin sizes \(c_1,\ldots,c_s\), combining (1) and (3) gives
\[
\log\#\{f:f^2=f,\ \chi(f)=e\}
=rm(L-\log L-1)
+m\sum_{j=1}^s c_j\log c_j+o(m). \tag{6}
\]
There are finitely many \(e\) because \(r\) is fixed; the \(o(m)\) is therefore uniform over characters.

For one fixed block, the entropy sum is \(r\log r\). For every nonconstant idempotent character, \(s\ge2\), and convexity of \(t\mapsto t\log t\) on the positive integers gives
\[
\sum_{j=1}^{s}c_j\log c_j
\le(r-1)\log(r-1). \tag{7}
\]
Equality holds precisely when there are two basins of sizes \((r-1,1)\), apart from the immaterial ordering, including \((1,1)\) for \(r=2\). One can see (7) by repeatedly moving one unit from a smaller basin of size at least two to a larger one, strictly increasing the convex sum, until all but one basin have size one; reducing the number of basins then increases it again. For \(r\ge3\) there are exactly \(r(r-1)\) characters realizing equality: choose the large-basin root and then its one singleton-basin root, and send all other blocks to the first. For \(r=2\) there is only one, the identity character.

Let \(N_{r,m}=E_{r,m}-rH_r(m)\). Equations (3), (6), (7), and the finite strict gap to all other nonconstant basin shapes yield
\[
N_{r,m}=M_r H_{r-1}(m)H_1(m)(1+o(1)). \tag{8}
\]
For \(r=2\) this is an equality, not merely an asymptotic. By (3), \(N_{r,m}/H_r(m)=\exp(-m\delta_r+o(m))\), and \(\delta_r>0\), so \(E_{r,m}=rH_r(m)(1+o(1))\). Dividing (8) by \(E_{r,m}\) proves both expressions in assertion 1. The exponentially dominant basin shapes inside \(N_{r,m}\) prove assertion 2.

**4. The image rank.** Conditional on a constant character, the image-rank distribution is exactly the distribution of \(J_{r,m}\) in (4), so \(K_m\log m/m\to r\) in probability under this conditioning. Assertion 1 says the conditioning event has probability tending to one; hence unconditional convergence follows as well. This completes the proof.

## Verification

The standalone standard-library script `verify.py` separately enumerates **all maps** preserving each tested uniform partition, tests idempotence by direct composition, records block-character ranks and image ranks, and compares them with (1). It checks the ten pairs of block count and block size \((1,1),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)\). In particular, for \((r,m)=(3,3)\) it finds \(9028\) idempotents and \(3348\) with constant character; for \((r,m)=(4,2)\) it finds \(2073\) idempotents and \(264\) with constant character. The script also compares exact character sums over smaller finite cases and computes stable logarithmic numerical checks at \(m=250,1000,5000\). All reported tests returned `VERIFY_OK`.

The proof of the infinite asymptotic is (5) with explicit tail control, followed by the finite strict entropy competition (7). Numerical results are diagnostic only, not certificates of an infinite claim.

## Relationship to prior work

Dolinka and East, *Idempotent generation in the endomorphism monoid of a uniform partition* (first publicly posted 2014-07-11, arXiv:1407.3312), Proposition 3.1 and Proposition 3.2, classify and enumerate idempotents for uniform partitions. The exact character-fiber count in (1) is a reorganized specialization of that prior result, **not new**. Their paper provides recurrences and small tables, but in the inspected text does not establish a fixed-number-of-blocks, large-block-size collapse probability, a rare-character exponential rate, conditional rare-character shape, or logarithmic image-rank concentration.

Sarkar and Singh, *Semigroups of transformations whose characters belong to a given semigroup* (first publicly posted 2023-10-30, arXiv:2310.19414), Proposition 3.9, generalizes idempotent-character structure. Their stated aims concern regularity, Green relations and idempotent characterizations, not the asymptotics proved here. This 2023 paper motivates revisiting the statistical distribution of characters rather than merely counting all idempotents.

Dolinka, East and Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition* (arXiv:1504.02520, 2015), concerns generating-set ranks and nonuniform structures, not the image-rank statistic \(K_m\). Al-aadhami, *Combinatorial Questions for \(S\wr_n\mathcal T_n\) for a Semigroup* (University of York thesis, 2017), studies idempotent enumeration in general wreath products; its accessible abstract was checked, but its full body was not inspected. A hidden equivalent probabilistic limit in that work or other older transformation-semigroup literature remains a priority risk.

## Limitations

The theorem is **not** a new exact count of idempotents; the existing finite enumeration is essential input. It adds a rigorously established asymptotic distributional and large-deviation conclusion. No claims are made for growing \(r\), unequal block sizes, arbitrary subsemigroups of the block-character monoid, or conditional laws for non-idempotent maps. The rate \(\delta_r\) controls logarithmic probability, not a constant-times-\(e^{-m\delta_r}\) equivalent; the more precise equivalent in terms of exact sums \(H_c(m)\) is given explicitly. The examined literature does not certify publication priority against every possible equivalent formulation, especially in the 2017 thesis. Independent external audit has not been conducted.

## References

1. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312 (first public posting 2014-07-11), especially Propositions 3.1 and 3.2. https://arxiv.org/abs/1407.3312
2. M. Sarkar and S. N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414 (first public posting 2023-10-30), especially Proposition 3.9. https://arxiv.org/abs/2310.19414
3. I. Dolinka, J. East and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520 (first public posting 2015-04-09). https://arxiv.org/abs/1504.02520
4. A. Al-aadhami, *Combinatorial Questions for \(S\wr_n\mathcal T_n\) for a Semigroup*, PhD thesis, University of York (2017), https://etheses.whiterose.ac.uk/id/eprint/19494/ (abstract checked; thesis body not fully inspected).
