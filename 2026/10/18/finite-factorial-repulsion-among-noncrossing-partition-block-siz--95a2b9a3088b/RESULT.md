# Finite factorial repulsion among noncrossing partition block sizes

## Finding

Let \(\Pi_n\) be uniformly distributed over the noncrossing partitions of \(\{1,\ldots,n\}\), and let \(X_r\) be its number of blocks of cardinality \(r\). Write \((x)_{\underline a}=x(x-1)\cdots(x-a+1)\), with \((x)_{\underline 0}=1\). For every \(n\ge3\), every choice of distinct positive sizes \(r_1,\ldots,r_d\), with \(d\ge2\), and positive integers \(a_1,\ldots,a_d\) satisfying \(\sum_i r_i a_i\le n\),

\[
0<\mathbb E\prod_{i=1}^d(X_{r_i})_{\underline{a_i}}
<\prod_{i=1}^d\mathbb E(X_{r_i})_{\underline{a_i}}.
\]

More generally, if \(\alpha\) and \(\beta\) are two nonzero, finitely supported, nonnegative-integer vectors indexed by positive block sizes, their supports are disjoint, and their individual total sizes are at most \(n\), then \(M_n(\alpha+\beta)<M_n(\alpha)M_n(\beta)\), where \(M_n(\gamma)=\mathbb E\prod_r(X_r)_{\underline{\gamma_r}}\). This also holds when the combined total size exceeds \(n\), in which case the left side vanishes. In particular, \(\operatorname{Cov}(X_r,X_s)<0\) for distinct sizes and \(n\ge3\).

This *factorial* repulsion is not ordinary negative association. At \(n=3\),

\[
\operatorname{Cov}(X_1,X_2)=-\frac3{25},\qquad
\operatorname{Cov}(\mathbf1_{\{X_1\ge1\}},\mathbf1_{\{X_2\ge1\}})=\frac3{25}>0.
\]

## Assumptions and scope

A partition is noncrossing when it has no two blocks containing elements \(a<c\) and \(b<d\), respectively, with \(a<b<c<d\). The law is uniform over all \(C_n=\binom{2n}{n}/(n+1)\) noncrossing partitions. All block sizes and factorial orders in the theorem are positive integers. No assertion of negative association for arbitrary increasing functions is made.

The mixed factorial moments themselves have the exact formula: for \(t=\sum_r\gamma_r\) and \(w=\sum_r r\gamma_r\le n\),

\[
M_n(\gamma)=\frac{(n+1)_{\underline t}}{(n+1)C_n}\binom{2n-t-w}{n-w};
\qquad M_n(\gamma)=0\ \text{if }w>n.
\]

The convention at \(t=0\) gives \(M_n(0)=1\).

## Proof

**1. Catalan decomposition and marked moments.** Let \(q_r\) mark each block of size \(r\), with \(q_0=1\). Decomposing a noncrossing partition at the block containing its first element gives the ordinary generating function \(C(z;\mathbf q)=1+\sum_{r\ge1}q_r(zC(z;\mathbf q))^r\). With \(G=zC\), Lagrange inversion yields

\[
[z^n]C(z;\mathbf q)=\frac1{n+1}[u^n]
\left(1+\sum_{r\ge1}q_r u^r\right)^{n+1}.
\]

Set all marks to one and differentiate \(\gamma_r\) times in each \(q_r\). Dividing by \(C_n\) proves the displayed moment formula. The same coefficient identity says that the vector \((X_r)_{r\ge1}\) has the same distribution as the positive-part-size multiplicities in a uniformly selected weak composition of \(n\) into \(n+1\) nonnegative parts. This profile equivalence (and the generating function) is a standard enumeration ingredient, not the claimed new dependence theorem.

**2. The local inequality.** For a nonnegative multiindex \(\gamma\) with \(w\le n\), let \(t=\sum\gamma_r\), \(m=n+1-t\), and \(N=n-w\). As every marked block has positive size, \(m\ge N+1\). For a uniform weak composition of \(N\) into \(m\) parts, let \(Y_r\) count parts equal to \(r\). The formula in step 1 gives

\[
\frac{M_n(\gamma+e_r)}{M_n(\gamma)}=\mathbb E Y_r,
\quad
\frac{M_n(\gamma+e_r+e_s)}{M_n(\gamma)}
=\mathbb E(Y_rY_s-\mathbf1_{\{r=s\}}Y_r).
\]

Thus it suffices to show \(\mathbb E(Y_rY_s-\mathbf1_{\{r=s\}}Y_r)\le\mathbb EY_r\mathbb EY_s\) for positive \(r,s\), whenever \(m\ge N+1\). This is immediate if \(r+s>N\). If \(N\ge2\) and \(r+s\le N\), put

\[
U=\binom{N+m-1}{m-1},\quad
U_r=\binom{N-r+m-2}{m-2},\quad
U_{r,s}=\binom{N-r-s+m-3}{m-3}.
\]

Counting designated coordinates gives \(\mathbb EY_r=mU_r/U\) and the mixed falling-factorial expectation \(m(m-1)U_{r,s}/U\). Their ratio is

\[
R(r,s)=\frac{m-1}{m}\frac{U_{r,s}U}{U_rU_s}.
\]

For every admissible increment in \(r\),

\[
\frac{R(r+1,s)}{R(r,s)}
=\frac{(N-r-s)(N-r+m-2)}{(N-r-s+m-3)(N-r)}\le1,
\]

because the numerator minus the denominator equals \((N-r)-(m-2)s\le0\). The same holds for increments in \(s\), so \(R(r,s)\le R(1,1)\). Finally,

\[
R(1,1)=\frac{(m-2)(N-1)(N+m-1)(N+m-2)}{mN(N+m-3)(N+m-4)}\le1.
\]

Indeed, putting \(h=m-N-1\ge0\), the denominator minus the numerator is exactly

\[
4N(N-1)(N-2)+(4N^2-7N+1)h+(3N-2)h^2+h^3\ge0.
\]

All coefficients are nonnegative for \(N\ge2\). Equality is possible only for \((N,m,r,s)=(2,3,1,1)\). If \(N<2\), two positive parts cannot both appear, and the desired inequality follows directly. Consequently,

\[
M_n(\gamma+e_r+e_s)M_n(\gamma)
\le M_n(\gamma+e_r)M_n(\gamma+e_s).
\]

**3. From local to global.** The local inequality means that the ratio \(M_n(\gamma+e_s)/M_n(\gamma)\) cannot increase when any other positive-size mark is added, as long as the denominators are positive. Add the marks of \(\beta\) one by one after adding all the marks of \(\alpha\), and compare each marginal factor with the same addition starting from the zero multiindex. Multiplying yields \(M_n(\alpha+\beta)\le M_n(\alpha)M_n(\beta)\). The argument extends to more than two disjoint groups by induction. For \(n\ge3\), the initial local inequality is strict, because the residual pair is \((N,m)=(n,n+1)\), not the equality case. If the combined weight exceeds \(n\), the left side is zero while both marginal moments are positive. This establishes the strict claims.

**4. Ordinary negative association fails.** At \(n=3\) the five noncrossing partitions consist of one partition with three singletons, three with one singleton and one two-block, and one with a single three-block. Thus \(\mathbb EX_1=6/5\), \(\mathbb EX_2=3/5\), and \(\mathbb E X_1X_2=3/5\), giving covariance \(-3/25\). On the other hand, the events of having at least one singleton and at least one two-block have respective probabilities \(4/5\) and \(3/5\), with joint probability \(3/5\); their indicator covariance is \(3/25\). Both indicators are increasing functions of their separate counts.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently enumerates all set partitions by restricted-growth strings and filters noncrossing partitions, recovering all Catalan totals and all indicated first and mixed factorial moments through \(n=8\). It then verifies the strict pairwise factorial-moment inequalities for \(2\le n\le30\), and the local weak-composition inequality over \(2\le N\le25\) and \(N+1\le m\le N+7\). The saved checker reports 83,058 exact assertions passed. Finite checks do not establish the universal quantifiers; the algebraic argument above does.

## Relationship to prior work

Kargin, *Limit theorems for statistics of non-crossing partitions* (arXiv:1907.00632v1, first posted 1 July 2019), Theorem 2.4 and its proof, derives finite mean and mixed second-moment coefficients and the leading negative covariance for any two distinct fixed block sizes. Its equations (2)–(4) provide the marked-generating-function mechanism used here. Neither those coefficient identities nor Kargin's asymptotic covariance are claimed as new. The retained assertion is the strict, all-finite-size, all-order factorial product inequality together with the sharp failure of ordinary increasing-event negative association. Standard noncrossing-partition type enumeration is another route to the same moment formula. Work on multiplicities in ordinary (crossing-allowed) uniform set partitions concerns a different probability law.

## Limitations

The inequality is only for falling-factorial multiplicity statistics, not arbitrary increasing tests. Its conclusion does not imply negative regression, negative association, or strong Rayleigh properties. The theorem concerns uniform classical noncrossing partitions, not arbitrary simply generated trees, noncrossing partitions of other Coxeter types, or ordinary set partitions. The exact moment formula is known through earlier generating functions; historical literature could contain the all-order sign implication in an equivalent form. No independent priority audit has been performed.

## References

1. V. Kargin, *Limit theorems for statistics of non-crossing partitions*, arXiv:1907.00632v1, 1 July 2019, https://arxiv.org/html/1907.00632v1 ; especially Section 2.2, Theorem 2.4 and equations (2)–(4).
2. G. Kreweras, *Sur les partitions non croisées d'un cycle*, Discrete Mathematics 1 (1972), 333–350 (classical enumeration and definition).
3. L. R. Mutafchiev and M. Savov, *On the maximal multiplicity of block sizes in a random set partition*, Random Structures & Algorithms 56 (2020), 867–891, doi:10.1002/rsa.20891 (different, crossing-allowed partition model).
