# A rank polynomial and concentration law for Rota–Baxter operators on finite sums of fields

## Finding
Let \(K\) be any field, \(n\ge1\), and \(\lambda\in K\setminus\{0\}\). On the coordinatewise-multiplication algebra \(A=K^n\), a weight-\(\lambda\) Rota–Baxter operator is a linear map \(R:A\to A\) satisfying
\[
R(a)R(b)=R\bigl(R(a)b+aR(b)+\lambda ab\bigr),\qquad a,b\in A.
\]
The rank of every such operator is computed by an exact tree statistic. In the previously established correspondence with trees on \(\{0,\ldots,n\}\), rooted at \(0\) with nonroot vertices independently colored black or white, define
\[
D(T)=\#\{i\in\{1,\ldots,n\}:i\text{ is white and has no white child}\}.
\]
Then \(\dim_K\ker R=D(T)\), and hence \(\operatorname{rank}R=n-D(T)\), including in characteristic two.

Let \(B=B(x,u)\) and \(W=W(x,u)\) be the unique power series in \(x\mathbb Q[u][[x]]\) solving
\[
B=x\exp(B+W),\qquad W=x\exp(B)\bigl(u+\exp(W)-1\bigr).
\]
The *complete rank enumerator* is
\[
\boxed{P_n(t)=n!t^n[x^n]\exp\bigl(B(x,t^{-1})+W(x,t^{-1})\bigr).}
\]
The negative powers appearing in this coefficient-extraction expression cancel after multiplication by \(t^n\); the result belongs to \(\mathbb Z[t]\). For \(1\le n\le5\), in increasing rank order, the coefficients are
\[
(1,1),\quad(1,8,3),\quad(1,33,78,16),\quad(1,108,822,944,125),\quad(1,315,6020,20040,13800,1296).
\]
In particular, the formula refines the previously known ungraded cardinality \(2^n(n+1)^{n-1}\).

For a uniformly chosen weight-\(\lambda\) Rota–Baxter operator and its nullity \(D_n\), the exact mean is
\[
\boxed{\mathbb E D_n=\frac n2\left(1-\frac{1}{2(n+1)}\right)^{n-1}.}
\]
Moreover, \(\operatorname{Var}(D_n)=O(n)\), and thus
\[
\boxed{\frac{\operatorname{rank}R}{n}\xrightarrow{L^2}1-\frac12e^{-1/2}.}
\]
The limit is approximately \(0.6967346701\) and is independent of the ground field and of the chosen nonzero weight.

## Assumptions and scope
The algebra has \(n\) labeled primitive coordinate idempotents, so the count concerns distinct linear operators rather than conjugacy classes. The field \(K\) is arbitrary; no finiteness or characteristic hypothesis is needed. The weight \(\lambda\ne0\) is fixed, and scaling by \(\lambda^{-1}\) reduces the proof to weight one without affecting rank. The probability statement uses the uniform distribution on the finite set of distinct operators, not on their conjugacy classes. The generating functions are formal, not analytical convergence assertions.

## Proof
**1. Previously established tree bijection.** Gubarev (2018, Theorem 1 and Corollary 2) bijects the weight-one operators with rooted labeled trees on \(\{0,1,\ldots,n\}\), root \(0\), whose other vertices are black or white. For a nonroot vertex \(i\), let \(T_i\) denote its descendant subtree, including \(i\), and \(S_i=\sum_{j\in T_i}e_j\). The matrix construction behind this bijection gives
\[
R(e_i)=\begin{cases}-S_i,&i\text{ black},\\\sum_{c\text{ a child of }i}S_c,&i\text{ white}.\end{cases}
\]
Indeed every strict descendant contributes the common nonzero offdiagonal entry of its row, while a black diagonal contributes \(-1\); cf. the matrix conditions (SF1)–(SF3) and the directed-transitive-tree correspondence in the cited paper. These tree and row constructions are not claimed as new.

**2. Kernel dimension.** The vectors \(\{S_i:1\le i\le n\}\) form a basis of \(K^n\): order vertices so that ancestors precede descendants; the corresponding change-of-basis matrix is triangular with diagonal one. In this basis, a black row is \(-S_i\) and a white row is the sum of \(S_c\) over its children. The black rows are independent. Quotienting by their span erases all black-coordinate terms. The image of a white row is therefore \(\sum_{c\text{ white child of }i}S_c\). Distinct white parents have disjoint sets of children, and these quotient rows are independent precisely for white vertices having at least one white child. Thus
\[
\operatorname{rank}R=\#\{\text{black vertices}\}+\#\{\text{white vertices with a white child}\}=n-D(T).
\]
No division is used, so this works in every characteristic.

**3. Refined tree enumeration.** View the children of root \(0\) as an unordered labeled set of colored rooted trees. A black-rooted component contributes \(B=x\exp(B+W)\). A white-rooted component has arbitrary black children, and either has no white child (weight \(u\)) or has at least one white child (weight one); hence \(W=x\exp(B)(u+\exp(W)-1)\). The distinguished uncolored root contributes \(\exp(B+W)\). Labeled exponential counting proves
\[
\sum_{n\ge0}\frac{x^n}{n!}\sum_{R\in\mathcal R_n}u^{\dim\ker R}=\exp(B+W),
\]
where the \(n=0\) term is the empty operator, assigned weight one. Replacing \(u\) by \(t^{-1}\) and multiplying by \(t^n\) gives the rank formula. At \(u=1\), \(B=W=T\) and \(T=x\exp(2T)\); Lagrange inversion yields \(n![x^n]\exp(2T)=2^n(n+1)^{n-1}\), recovering the known total.

**4. Exact mean.** Put \(N=n+1\). A uniformly selected operator corresponds to a uniformly selected labeled tree on \(\{0,\ldots,n\}\) together with independent fair colors of its \(n\) nonroot vertices. Write \(I_i\) for the indicator that nonroot \(i\) is white with no white child. In a rooted tree the number of children of \(i\) equals \(\deg(i)-1\), so
\[
\mathbb E[I_i\mid T]=2^{-\deg(i)}.
\]
In the uniform Prüfer encoding of a Cayley tree, \(\deg(i)=1+X_i\), where \(X_i\sim\operatorname{Bin}(N-2,1/N)\). Therefore
\[
\mathbb E I_i=\tfrac12(1-1/(2N))^{N-2},
\]
and summing over the \(n\) nonroot indices gives the claimed exact mean.

**5. Concentration.** If distinct nonroot vertices \(i,j\) are not adjacent in their tree, the sets of colors inspected by \(I_i\) and \(I_j\) are disjoint, so they are conditionally independent and \(\mathbb E[I_iI_j\mid T]=2^{-\deg(i)-\deg(j)}\). Adjacent vertex pairs have probability \(2/N\) under the uniform labeled tree, and the discrepancy from that product is at most one. The joint Prüfer multinomial distribution gives
\[
\mathbb E[2^{-\deg(i)-\deg(j)}]=\frac14(1-1/N)^{N-2}.
\]
Comparing this with \(\mathbb E I_i\,\mathbb E I_j=\frac14(1-1/(2N))^{2(N-2)}\) shows that the covariance is \(O(1/N)\), uniformly over distinct pairs. Because all indicators are bounded, \(\operatorname{Var}(\sum_iI_i)=O(n)+O(n^2/N)=O(n)\). The exact mean divided by \(n\) tends to \(\tfrac12e^{-1/2}\); the variance bound implies convergence in \(L^2\), and subtracting from one yields the rank limit.

## Verification
The accompanying standalone `verify.py` uses three independent procedures: it enumerates all coefficient-choice matrices satisfying the defining Rota–Baxter identity for \(n=1,2,3,4\) over both \(\mathbb F_2\) and \(\mathbb F_3\), computing each matrix rank directly; it independently enumerates Prüfer-coded trees and their two-colorings for \(n\le5\); and it extracts the coefficients of the two formal functional equations using exact rational arithmetic. The three agree in every tested case. It also checks the exact mean formula for each tested dimension. The verifier prints `VERIFY_OK` on success. These finite computations are checks, not a proof of the general claims; the proof is given above.

## Relationship to prior work
Gubarev, *Rota-Baxter operators on a sum of fields* (arXiv:1811.08219, first version November 20, 2018), already establishes the tree correspondence and the total \(2^n(n+1)^{n-1}\) count, and studies splitting operators and conjugacy classes. Those facts are prerequisites, not new contributions. Gubarev, *Spectrum of Rota-Baxter operators* (arXiv:2006.02654, first version June 4, 2020), analyzes eigenvalue restrictions and minimal-polynomial indices, including the same coordinate algebra; its general spectral bounds do not give an individual-matrix rank distribution. The new claims here are the exact tree statistic for ordinary matrix nullity, its complete finite-dimensional rank polynomial, and the \(L^2\) concentration law. Searches for equivalent and stronger rank distributions found none in the inspected materials, but this does not establish publication priority exhaustively.

## Limitations
This result counts all operators, not isomorphism or conjugacy types, and concerns nonzero weight, not weight zero. It does not give a central limit theorem, a full variance asymptotic, or a rate better than the elementary \(O(1/n)\) variance bound after normalization. A broader unpublished or unlocated enumeration theorem might cover the polynomial. Independent mathematical validation has not been performed.

## References
1. V. Gubarev, *Rota-Baxter operators on a sum of fields*, arXiv:1811.08219v1, November 20, 2018, especially Statement 4, Theorem 1 and Corollary 2. https://arxiv.org/abs/1811.08219
2. V. Gubarev, *Spectrum of Rota-Baxter operators*, arXiv:2006.02654v1, June 4, 2020, especially the main theorem and the section on the Rota–Baxter index of sums of fields. https://arxiv.org/abs/2006.02654
