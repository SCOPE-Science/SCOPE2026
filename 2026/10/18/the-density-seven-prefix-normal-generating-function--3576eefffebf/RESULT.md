# The density-seven prefix-normal generating function

## Finding

A binary word is *prefix normal* if, for each length \(\ell\), its prefix of length \(\ell\) has at least as many ones as any contiguous factor of length \(\ell\). Let \(p_7(n)\) denote the number of prefix-normal binary words of length \(n\) having exactly seven ones (with \(p_7(n)=0\) for \(n<7\)). The exact ordinary generating function for every \(n\ge0\) is

\[
F_7(z)=\sum_{n\ge0}p_7(n)z^n
=\frac{z^7 P(z)}{(1-z)(1-z^3)(1-z^4)^2(1-z^6)^3},
\]
where
\[
\begin{aligned}
P(z)={}&1+3z+9z^{2}+17z^{3}+35z^{4}+48z^{5}
+76z^{6}+85z^{7}+108z^{8}+103z^{9}\\
&+108z^{10}+85z^{11}+76z^{12}+48z^{13}
+35z^{14}+17z^{15}+9z^{16}+3z^{17}+z^{18}.
\end{aligned}
\]

This extends the explicit fixed-density generating-function list previously given through density six to density seven; the prior general rationality theorem alone did not specify this rational function.

## Assumptions and scope

Words are finite, over the labeled alphabet \(\{0,1\}\), and contain **exactly** seven occurrences of symbol \(1\). A factor means a *contiguous* substring, including the word itself. All lengths \(n\ge0\) are covered. In particular there are no such words below length seven; at length seven the all-one word is the sole example. No assumption on the number of zeros is made.

## Proof

**1. Gap criterion.** Every nonzero prefix-normal word begins with \(1\). Let \(r_1,\ldots,r_6\ge1\) be the successive distances between its seven ones, and let \(r_7\ge1\) be the final distance from its seventh one to the end, including the seventh-one position itself. Thus \(n=\sum_{i=1}^7r_i\). A prefix is a shortest factor containing any prescribed \(k\) consecutive ones precisely when, for every \(m=k-1\in\{1,\ldots,5\}\) and every start \(2\le j\le 7-m\),
\[
r_1+\cdots+r_m\le r_j+\cdots+r_{j+m-1}.
\]
To justify equivalence, the shortest length of any factor containing \(k\) ones is the minimal span between its first and last occurrence, plus one; the prefix attaining \(k\) ones has span \(1+r_1+\cdots+r_{k-1}\). This condition for each \(k\) is equivalent to the prefix-normal definition, since any factor with more ones than a prefix would have a shorter span containing those ones.

Set \(r_1=1+h\), \((r_2,\ldots,r_6)=(r_1+A,r_1+B,r_1+C,r_1+D,r_1+E)\), and \(r_7=1+t\). The gap criterion is **equivalent** to \(h,t,A,B,C,D,E\ge0\) together with just four inequalities
\[
A\le B+C,\qquad A\le C+D,\qquad A\le D+E,
\qquad A+B\le C+D+E.
\]
Indeed the single-gap comparisons give \(A,B,C,D,E\ge0\), the two-gap comparisons give the first three additional inequalities, and the three-gap comparisons yield the fourth; all remaining longer-gap comparisons duplicate one of these or a nonnegativity condition.

**2. Removing the final two nonnegative variables.** For fixed \(A,B,C\ge0\) satisfying \(A\le B+C\), set
\[
D_0=\max(0,A-C),\qquad T=A+\max(0,B-C).
\]
The remaining constraints on \(D,E\) are exactly \(D\ge D_0\), \(E\ge0\), and \(D+E\ge T\). As \(D_0\le T\), their weighted count is
\[
\sum_{\substack{D\ge D_0,\ E\ge0\\D+E\ge T}} z^{D+E}
=\frac{(T-D_0+1)z^T}{1-z}+\frac{z^{T+1}}{(1-z)^2}.
\]
Define \(e=A+B+C+T\) and \(m=T-D_0+1\). Let \(K(z)=\sum z^e\) and \(L(z)=\sum m z^e\) over all admissible triples \((A,B,C)\). It follows that
\[
F_7(z)=\frac{z^7}{(1-z)(1-z^6)}
\left(\frac{L(z)}{1-z}+\frac{zK(z)}{(1-z)^2}\right).
\]
The first denominators count the unrestricted tail \(t\) and common increment \(h\): the total length is \(7+6h+t+A+B+C+D+E\).

**3. Exhaustive disjoint cone decomposition.** Each triple is uniquely represented by one of the following six rows. The displayed parameters are nonnegative integers except where indicated; row four has \(s\ge1\), row five has \(s\ge1\), row six has \(u,v\ge1\), and rows two and three have respectively \(u\ge1\) and \(v\ge1\). No other restrictions are imposed.

| Case | \((A,B,C)\) | \(e=A+B+C+T\) | \(m=T-D_0+1\) |
| --- | --- | --- | --- |
| \(A\le C,\ B\le A\) | \((b+u,b,b+u+v)\) | \(4b+3u+v\) | \(b+u+1\) |
| \(A\le C,\ A<B\le C\) | \((a,a+u,a+u+v)\) | \(4a+2u+v\) | \(a+1\) |
| \(A\le C,\ B>C\) | \((a,a+u+v,a+u)\) | \(4a+2u+2v\) | \(a+v+1\) |
| \(A>C,\ B\le C\) | \((2s+v+u,s+v,s+v+u)\) | \(6s+4v+3u\) | \(s+v+u+1\) |
| \(A>C,\ B>C,\ A-C\le B-C\) | \((c+s,c+s+u,c)\) | \(4c+4s+2u\) | \(c+s+u+1\) |
| \(A>C,\ B>C,\ A-C>B-C\) | \((c+v+2u,c+v+u,c+u)\) | \(4c+4v+6u\) | \(c+v+u+1\) |

For example, in the fourth case \(s=A-C>0\), \(u=C-B\ge0\), \(v=B-s\ge0\); the last inequality comes exactly from \(A\le B+C\). In the sixth case \(u=A-B>0\), \(v=B-C>0\), \(c=C-u\ge0\), using the same admissibility inequality. The other four cases invert directly. Hence the six rows partition all admissible triples, rather than merely giving examples.

For every row, summing \(z^e\) over its free parameters uses \(\sum_{j\ge0}z^{kj}=1/(1-z^k)\), and summing \(mz^e\) additionally uses \(\sum_{j\ge0}(j+1)z^{kj}=1/(1-z^k)^2\). Substitution into the expression for \(F_7\) and clearing denominators gives precisely the numerator \(P\) and denominator stated under **Finding**. The accompanying standard-library program checks this last exact rational identity by integer polynomial multiplication (not interpolation or floating point). Therefore the formula holds formally for every length.

## Verification

Run `python3 verify_prefix_normal7.py`. This self-contained script performs exact integer polynomial arithmetic to check the six-cone generating-function identity after denominator clearing. Separately, for every length \(7\le n\le25\), it enumerates all seven-one words beginning with \(1\), checks prefix normality directly against all factors, compares with the independent gap criterion, and matches the resulting count against the rational generating function.

The obtained counts for lengths \(7,8,\ldots,25\), in order, are

`1, 4, 13, 31, 71, 134, 249, 417, 688, 1062, 1628, 2367, 3430, 4781, 6632, 8931, 11995, 15703, 20523`.

The program prints `FORMAL_IDENTITY_PASS` and `ALL_CHECKS_PASS`. The finite enumerations provide independent error checks; the argument in **Proof**, not finite testing, establishes the infinite formula.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada (2014, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824) introduced the gap formulation and displayed fixed-density generating functions only for densities \(0\) through \(6\) in Section 4, Lemmas 2–3. Their later extended treatment (2016, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, Section 4.2, Proposition 16) proved rationality for every fixed density but likewise gave explicit functions only through six, reporting unsuccessful computation for higher densities. Those general statements do not specify this exact numerator or denominator. The current formula treats the first omitted fixed-density case using a disjoint six-cone count. It is an explicit extension of the displayed list, not a claim that rationality itself is new.

## Limitations

The formula is for binary words with exactly seven ones. It does not give an exact formula for arbitrary density, total length-unrestricted counts, or larger fixed densities. Although the relevant primary papers explicitly stop at six, an equivalent unpublished, unindexed or differently formulated earlier computation cannot be excluded without further independent bibliographic assessment. This research result has not received independent validation.

## References

- Péter Burcsi, Gabriele Fici, Zsuzsanna Lipták, Frank Ruskey and Joe Sawada, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824, first submitted 1 April 2014; particularly Section 4 and Lemmas 2–3. https://arxiv.org/html/1404.2824v1
- Péter Burcsi, Gabriele Fici, Zsuzsanna Lipták, Frank Ruskey and Joe Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first submitted 28 November 2016; particularly Section 4.2 and Proposition 16. https://arxiv.org/html/1611.09017v1
