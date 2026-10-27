# Simultaneous chain-type dominance in bounded-class nilpotent inverse semigroups

## Finding

Let \(n\ge k\ge2\), and let \(\mathcal I_n\) denote the finite symmetric inverse monoid of partial bijections on an \(n\)-point set. For any subsemigroup \(S\subseteq\mathcal I_n\) with \(S^k=\{0\}\), define \(c_j(f)\) to be the number of directed chains of exactly \(j\) vertices in the path decomposition of \(f\), **including isolated vertices as one-vertex chains**. Every element has chains of at most \(k\) vertices. Define its complete chain-profile polynomial by
\[
\Phi_S(u_1,\ldots,u_k)=\sum_{f\in S}\prod_{j=1}^k u_j^{c_j(f)}.
\]
If \(T_{\mathbf b}\) is the semigroup of every partial injection taking points strictly upward between the blocks of any ordered \(k\)-block decomposition \(\mathbf b\) of \(n\) into sizes differing by at most one, then
\[
\boxed{\Phi_S\ \preceq_{\mathrm{coeff}}\ \Phi_{T_{\mathbf b}}},
\]
where coefficientwise comparison is in the monomial basis of the independent variables \(u_1,\ldots,u_k\). Equality of these two entire polynomials holds **exactly** when \(S\) is itself a complete upward-layer semigroup for a balanced ordered \(k\)-block decomposition.

More generally, for positive block sizes \(\mathbf a=(a_1,\ldots,a_k)\) with sum \(n\), the complete chain-profile polynomial is the exact coefficient extraction
\[
\boxed{\Phi_{T_{\mathbf a}}(\mathbf u)=\Bigl(\prod_{i=1}^k a_i!\Bigr)
[z_1^{a_1}\cdots z_k^{a_k}]\exp\left(\sum_{j=1}^k u_j e_j(z_1,\ldots,z_k)\right)},
\]
where \(e_j\) is the degree-\(j\) elementary symmetric polynomial. Consequently, balanced layers simultaneously maximize the number of elements of **each individual nilpotent chain type**, not merely the number of elements of each rank. Equivalently, they simultaneously maximize each possible vector of ranks of all powers.

## Assumptions and scope

The zero map \(0\) is the nowhere-defined partial bijection. In \(S^k=\{0\}\), a product of any \(k\) elements of \(S\) equals \(0\). A complete upward-layer semigroup consists of all partial bijections \(f\) satisfying \(x\in B_i\) and \(f(x)\in B_j\) only when \(i<j\), together with \(0\). The ordered blocks \(B_i\) are disjoint and cover the underlying set. The chain polynomial counts labeled partial bijections: chains of the same length are not distinguished unless their vertices differ.

For clarity, the ranks of powers can be recovered from and recover chain types: with \(r_0=n\), \(r_m=\operatorname{rank}(f^m)\) for \(m\ge1\) and \(r_m=0\) for \(m\ge k\),
\[
r_m=\sum_{j=m+1}^k(j-m)c_j(f),\qquad
c_j(f)=r_{j-1}-2r_j+r_{j+1}\quad(1\le j\le k).
\]

## Proof

**1. Every bounded-class nilpotent subsemigroup lies in a layered one.** Make a directed graph on the underlying vertices, putting the edge \(x\to y\) whenever some \(f\in S\) sends \(x\) to \(y\). A directed walk of length \(k\) would yield a nonzero product of \(k\) elements of \(S\). Thus no such walk exists, including a walk that repeats vertices. The graph is acyclic; its longest directed path has length at most \(k-1\). Give a vertex level one plus the greatest number of edges along a path ending there. Every edge strictly raises the level; there are at most \(k\) levels. If necessary, split a nonempty level into consecutive nonempty blocks until there are \(k\) blocks; since there are \(n\ge k\) vertices, this is possible and creates no forbidden edges. This places \(S\) inside a complete upward-layer \(T_{\mathbf a}\). Coefficientwise \(\Phi_S\preceq\Phi_{T_{\mathbf a}}\) follows simply by containment.

**2. Exact chain-type enumeration.** Each element of \(T_{\mathbf a}\) is uniquely a disjoint union of directed chains. Each chain meets a subset \(J\subseteq\{1,\ldots,k\}\) of layers in strictly increasing order and contains exactly one vertex in each of them. On fixed labeled vertices, that chain is unique. The multivariate labeled exponential formula therefore gives
\[
\sum_{a_1,\ldots,a_k\ge0}\Phi_{T_{\mathbf a}}(\mathbf u)
\prod_{i=1}^k\frac{z_i^{a_i}}{a_i!}
=\exp\left(\sum_{\varnothing\ne J\subseteq[k]}u_{|J|}\prod_{i\in J}z_i\right)
=\exp\left(\sum_{j=1}^k u_j e_j(\mathbf z)\right).
\]
The statement remains valid with zero block sizes for the purpose of coefficient extraction.

**3. Coefficientwise balancing lemma.** Fix two block positions with sizes \(a,b\), where \(a\ge b+2\). Write their marker variables as \(x,y\), and let \(Z\) denote the other \(k-2\) marker variables. Define the nonnegative-coefficient polynomials
\[
F_0=\sum_{j=1}^ku_j e_j(Z),\quad
F_1=\sum_{j=1}^ku_j e_{j-1}(Z),\quad
F_2=\sum_{j=1}^ku_j e_{j-2}(Z),
\]
with \(e_0(Z)=1\) and \(e_t(Z)=0\) for negative \(t\) or \(t>|Z|\). The exponent splits exactly into \(F_0+(x+y)F_1+xyF_2\). Consequently the contribution at \(x^ay^b\), after multiplication by \(a!b!\), is
\[
e^{F_0}\sum_{d=0}^{b}\frac{(a)_d(b)_d}{d!}
F_1^{a+b-2d}F_2^d,
\]
where \((v)_d=v(v-1)\cdots(v-d+1)\). For every \(1\le d\le b\), moving \((a,b)\) to \((a-1,b+1)\) strictly increases \((a)_d(b)_d\), because the factor pair for each \(s=0,\ldots,d-1\) increases from \((a-s)(b-s)\) to \((a-1-s)(b+1-s)\), a gain \(a-b-1>0\). If the minimum block size increases, additional summands also have nonnegative coefficients. Because \(F_0,F_1,F_2\) have nonnegative coefficients, the extracted full \(\mathbf u\)-polynomial cannot decrease coefficientwise. Iterating these transfers balances all block sizes.

**4. Strictness and equality.** The coefficient of \(u_2u_1^{n-2}\) is the number of allowed single directed arrows,
\[
\sum_{1\le i<j\le k}a_ia_j.
\]
It increases by exactly \(a-b-1\) under a nontrivial balancing transfer \((a,b)\mapsto(a-1,b+1)\). Thus an unbalanced complete layered semigroup has strictly smaller full chain polynomial than the balanced one. If \(S\) is a proper subset of the containing complete layered semigroup, its total number of elements is strictly smaller. Hence equality of full polynomials forces both completeness and balanced sizes. Conversely every balanced complete layered semigroup attains equality, since the formula is symmetric in its layer sizes.

## Verification

The accompanying standalone `verify.py` independently enumerates permitted partial injections for all nonempty block compositions in the prescribed small ranges; it compares every chain-type count with a separately implemented recursion removing the chain containing a distinguished vertex. It also checks all chain-profile coefficients for all nonempty ordered block compositions with \(2\le n\le11\) and \(2\le k\le\min(5,n)\). The supplied verifier prints `VERIFY_OK_FULL_CHAIN_TYPE_DOMINANCE`, with 251 brute-force profile cells, 18,196 coefficient domination comparisons and 909 strict unbalanced cases. These finite checks are illustrative; the proof above applies to all finite \(n\ge k\ge2\).

For example, with \(n=6\) and \(k=3\), the balanced block vector \((2,2,2)\) contains 30 elements of chain type \((c_1,c_2,c_3)=(2,2,0)\) and 8 of type \((3,0,1)\), whereas the unbalanced vector \((1,2,3)\) contains 24 and 6 respectively. Both types have rank 2, so no single rank-count comparison distinguishes them.

## Relationship to prior work

The 2005 classification by Ganyushkin and Mazorchuk establishes the ordered-partition structure of maximal bounded-class nilpotent subsemigroups; their 2005 work on partial injections studies chains and their distributions. These underlying structural and chain-decomposition facts are prior work. A previously recorded rank-polynomial extremal result for the same family establishes coefficientwise domination only after the substitution \(u_j=t^{j-1}\). That statement sums over distinct chain types of equal rank and does **not** imply the present coefficientwise theorem in independent \(u_j\) variables. The claim here is solely the simultaneous dominance of *every* individual chain type and all power-rank vectors, proved by the multivariate two-block smoothing identity above. The EGF method itself is elementary and is not asserted to be historically novel. Priority for an implicit stronger formulation in older literature remains a residual risk.

## Limitations

The semigroup consists of partial **injective** transformations and the bound assumes a uniform semigroup nilpotence class. It concerns labeled elements and their chain decomposition, not isomorphism classes of semigroups, full partial transformation monoids, or arbitrary nonnilpotent subsemigroups. No independent mathematical audit has been conducted. The existing rank-polynomial optimization and maximal-subsemigroup classification are not new claims here.

## References

1. O. Ganyushkin and V. Mazorchuk, *On classification of maximal nilpotent subsemigroups*, arXiv:math/0510372 (public 2005-10-18), especially the maximal bounded-class classification and symmetric-inverse-semigroup application.
2. O. Ganyushkin and V. Mazorchuk, *Combinatorics and distributions of partial injections*, arXiv:math/0511431 (public 2005-11-17), especially the chain-decomposition and enumeration discussion.
3. O. Ganyushkin and V. Mazorchuk, *Classical Finite Transformation Semigroups: An Introduction*, Springer (2009), Chapter 8 on nilpotent subsemigroups.
