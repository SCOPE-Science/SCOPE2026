# Joint rank distribution for products of two finite-field idempotents

## Finding

Let \(q\) be a prime power and \(n\ge1\). For integers \(r,s,p,t\), define \(T_{n,q}(r,s;p,t)\) to be the number of **ordered** pairs \((E,F)\) of matrices in \(M_n(\mathbb F_q)\) such that \(E^2=E\), \(F^2=F\), and
\[
\bigl(\operatorname{rank}E,\operatorname{rank}F,
\operatorname{rank}(EF),\operatorname{rank}(FE)\bigr)=(r,s,p,t).
\]

Write \({a\brack b}_q\) for the Gaussian binomial coefficient, zero when \(b<0\) or \(b>a\); set
\[
G_q(j)=\prod_{i=0}^{j-1}(q^j-q^i),\qquad
R_q(a,b;j)={a\brack j}_q{b\brack j}_q G_q(j).
\]
The empty product is one. Thus \(R_q(a,b;j)\) is the number of rank-\(j\) maps from a \(b\)-space to an \(a\)-space, and the convention sets invalid dimensions/ranks to zero.

**The complete joint distribution** is
\[
\boxed{
T_{n,q}(r,s;p,t)=
{n\brack r}_q q^{r(n-r)}
\sum_{h\in\mathcal H}
{r\brack h}_q
{n-r\brack s-p}_q
{r-h\brack p-h}_q
{n-r-s+p\brack p-h}_q
G_q(p-h)
R_q(s-h,r-h;t-h)
q^{h(r-h)+s(n-s-r+h)} .
}
\]
Here \(\mathcal H\) contains exactly those integers \(h\) satisfying
\[
0\le h\le\min(r,s,p,t),\qquad
0\le s-p\le n-r,\qquad
0\le p-h\le\min(r-h,n-r-s+p),
\qquad n-s-r+h\ge0,
\qquad 0\le t-h\le\min(s-h,r-h).
\]
If \(r,s,p,t\) lie outside \(0,\ldots,n\), or if \(\mathcal H\) is empty, the count is zero. All exponents in retained terms are nonnegative.

Two consequences are
\[
T_{n,q}(r,s;p,t)=T_{n,q}(s,r;t,p)
\]
and
\[
\sum_{p=0}^n\sum_{t=0}^n T_{n,q}(r,s;p,t)
={n\brack r}_q{n\brack s}_q\,q^{r(n-r)+s(n-s)}.
\]
The left and right products need not have equal ranks. For example, over \(\mathbb F_2\), the idempotents
\[
E=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
F=\begin{pmatrix}0&1\\0&1\end{pmatrix}
\]
have \(\operatorname{rank}(EF)=1\) and \(\operatorname{rank}(FE)=0\). For \(n=2\), \(q=2\), and \(r=s=1\), the four multiplicities indexed by \((p,t)=(0,0),(0,1),(1,0),(1,1)\) are \(6,6,6,18\).

## Assumptions and scope

The matrices are arbitrary algebraic idempotents over \(\mathbb F_q\), not necessarily symmetric, orthogonal, commuting, or distinct. Matrix multiplication follows the indicated order. All statements and counts include rank zero and full rank, every field characteristic, and all prime powers. The formula counts labeled ordered pairs, not similarity classes.

## Proof

**Step 1 (fix the first idempotent).** If \(E^2=E\) and \(\operatorname{rank}E=r\), then \(U=\operatorname{im}E\) and \(K=\ker E\) give a direct-sum decomposition \(V=U\oplus K\), where \(\dim V=n\). Conversely each such ordered complementary pair determines exactly one \(E\), the projection onto \(U\) along \(K\). There are \({n\brack r}_q\) choices for \(U\) and \(q^{r(n-r)}\) for its complement \(K\). Fix this \(E\) henceforth.

**Step 2 (count the image of the second idempotent).** Set \(W=\operatorname{im}F\), \(L=\ker F\); then \(F\) is the projection onto \(W\) along \(L\), with \(\dim W=s\). Put \(h=\dim(W\cap U)\). Because \(E(W)\) has dimension \(p\), rank-nullity gives \(\dim(W\cap K)=s-p\). Let \(A=W\cap U\), \(B=W\cap K\), and \(c=p-h\). Choosing \(A\) and \(B\) contributes \({r\brack h}_q{n-r\brack s-p}_q\). Modulo \(A\oplus B\), the space \(W\) is the graph of an isomorphism between a \(c\)-space of \(U/A\) and a \(c\)-space of \(K/B\), so the remaining choices contribute \({r-h\brack c}_q{n-r-s+p\brack c}_qG_q(c)\). This proves the image factor of the sum and all of its dimensional constraints.

**Step 3 (count complementary kernels with the other product rank).** For a fixed \(W\), choose a reference splitting \(\sigma_0:V/W\to V\) whose image contains a complement to \(U\cap W\) inside \(U\); such a splitting exists by extending a basis of the image of \(U\) in \(V/W\). Every complementary \(L\) is the image of \(\sigma_0+\phi\), uniquely for \(\phi\in\operatorname{Hom}(V/W,W)\). The induced map
\[
\bar\phi:\pi(U)\longrightarrow W/(U\cap W)
\]
has domain dimension \(r-h\), codomain dimension \(s-h\), and \(\dim(U\cap L)=(r-h)-\operatorname{rank}\bar\phi\). Since \(\operatorname{rank}(FE)=r-\dim(U\cap L)=t\), the prescribed condition is exactly \(\operatorname{rank}\bar\phi=t-h\).

There are \(R_q(s-h,r-h;t-h)\) possible induced maps. Each lifts on \(\pi(U)\) in \(q^{h(r-h)}\) ways; the values of \(\phi\) on a complementary \((n-s-r+h)\)-dimensional subspace of \(V/W\) are arbitrary, contributing \(q^{s(n-s-r+h)}\). This gives the kernel factor.

**Step 4 (combine).** Multiply the count in Step 1 by the product of the image and complementary-kernel counts in Steps 2–3 and sum over every feasible \(h\). Each ordered idempotent pair is counted once, proving the formula. Swapping \(E\) and \(F\) proves the stated symmetry. Summing over \(p,t\) removes the product-rank constraints; the independent choices of two idempotents give the stated total.

## Verification

Run `python3 verify.py` using Python 3 and no third-party packages. The program evaluates the theorem independently by exhaustive matrix enumeration over prime fields of orders \(2\) and \(3\), and over the extension field \(\mathbb F_4\) represented by binary polynomials modulo \(x^2+x+1\). It checks all strata in dimensions \(2\), \(3\), and \(4\) as applicable; verifies the identity, order sensitivity, and all possible rank quadruples, including zero counts. It separately checks the normalization and reversal symmetry through dimension \(5\) at six field orders. These finite checks corroborate but do not replace the unrestricted proof in the preceding section.

## Relationship to prior work

Pop (2016, Theorems 2.1–2.2, primary MSC 15A03) characterizes arbitrary projections by the direct sum of image and kernel, a classical premise of the present proof. The finite-field number of individual rank-\(r\) idempotents and its Gaussian-binomial form are classical; Dolinka–Gray explicitly use these counts in the context of biordered sets and maximal subgroups of the full linear monoid. The result here instead enumerates the **joint two-sided product-rank profile** \((\operatorname{rank}EF,\operatorname{rank}FE)\), conditional on both input ranks, including noncommuting idempotents. The Koliha–Rakočević and Zuo results study ranks of linear combinations of idempotents, not finite-field counts of ordered pairs stratified by both product ranks. Related matrix-pair simultaneous-similarity literature has a different quotient/classification output. The Gaussian factors in the proof are standard; the combination counting the coupled ranks is the claimed result.

## Limitations

This is a counting result, not a simultaneous-similarity classification, an expression for the distribution of the Jordan forms of the products, or a result on three or more idempotents. Published equivalents in older unindexed finite-geometry or semigroup enumeration literature cannot be ruled out by bibliographic searches alone. The readily located 2006 linear-combination paper was available through its detailed abstract, not complete text. No independent mathematical audit has been performed.

## References

1. V. Pop, *The Characterization of Some Linear Maps Using the Rank*, Journal of Science and Arts **16**, no. 3 (2016), 225–228; available at https://www.josa.ro/docs/josa_2016_3/a_06_Pop.pdf (published online 2016-09-30), especially §2, Theorems 2.1–2.2. The article lists MSC 15A03 first.
2. I. Dolinka and R. Gray, *Maximal subgroups of free idempotent generated semigroups over the full linear monoid*, arXiv:1112.0893 (first posted 2011-12-05); especially the matrix-semigroup preliminaries and the finite-field counting discussion in §8.
3. J. J. Koliha and V. Rakočević, *The nullity and rank of linear combinations of idempotent matrices*, Linear Algebra Appl. **418** (2006), 11–14; doi:10.1016/j.laa.2006.01.011.
4. K. Zuo, *The nullity and rank of combinations of idempotent matrices*, 2008, published abstract describing ranks of certain linear combinations with product terms.
5. M. Tošić, E. Ljajko, N. Kontrec, and V. Stojanović, *The Nullity, Rank, and Invertibility of Linear Combinations of k-Potent Matrices*, Mathematics **8** (2020), 2147; doi:10.3390/math8122147.
6. C. M. Florentino, *Simultaneous similarity and triangularization of sets of 2 by 2 matrices*, arXiv:0809.3032 (2008).
