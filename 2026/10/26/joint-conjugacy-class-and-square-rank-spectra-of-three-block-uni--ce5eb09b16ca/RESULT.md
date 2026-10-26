# Joint conjugacy-class and square-rank spectra of three-block unipotent radicals

## Finding
Let \(q\) be any prime power and let \(a,b,c\geq 1\). Consider the three-block unipotent radical
\[
G_{a,b,c}(q)=\left\{g(X,Y,Z)=
\begin{pmatrix}I_a&X&Z\\0&I_b&Y\\0&0&I_c\end{pmatrix}:
X\in M_{a\times b}(\mathbb F_q),\ Y\in M_{b\times c}(\mathbb F_q),\ Z\in M_{a\times c}(\mathbb F_q)\right\}.
\]
For \(g\in G_{a,b,c}(q)\), define \(t(g)\) by \(|g^{G_{a,b,c}(q)}|=q^{t(g)}\) and define \(k(g)=\operatorname{rank}((g-I)^2)\). For integers \(t,k\geq0\), the exact number \(M_{a,b,c;q}(t,k)\) of elements with these two invariants is
\[
\boxed{
M_{a,b,c;q}(t,k)=q^{ac}
\sum_{r=0}^{\min(a,b)}\sum_{s=0}^{\min(b,c)}
\mathbf1_{\{t=cr+as-rs\}}
R_q(a,b;r)\,S_q(c,s)\,
{b-r\brack s-k}_q{r\brack k}_q
q^{k(b-r-s+k)}.
}
\]
Terms are interpreted as zero unless \(\max(0,r+s-b)\leq k\leq\min(r,s)\). Here
\[
R_q(a,b;r)={a\brack r}_q{b\brack r}_q|\operatorname{GL}_r(\mathbb F_q)|,
\qquad S_q(c,s)=\prod_{j=0}^{s-1}(q^c-q^j),
\]
with empty products equal to one and \({n\brack h}_q=0\) outside \(0\leq h\leq n\). Every conjugacy class in the \((t,k)\)-stratum has cardinality \(q^t\); hence the exact **number of conjugacy classes** in that stratum is \(M_{a,b,c;q}(t,k)/q^t\). These formulas hold in every characteristic, including two.

The formula records the rank of a square and the full conjugacy-class-size distribution jointly: one does not determine the other. For example, when \(q=2\) and \((a,b,c)=(2,2,2)\), among the elements in classes of cardinality \(16\), the numbers of elements having square ranks \(0,1,2\) are respectively \(192,1728,576\); equivalently the numbers of classes are \(12,108,36\). In characteristic two these are, respectively, elements of order at most two and elements of order four, within **one and the same conjugacy-class-size stratum**.

There is also a fixed-end limiting law. Fix \(q,a,c\) and let \(b\to\infty\). For uniformly random \(g\in G_{a,b,c}(q)\),
\[
\Pr\big(t(g)=ac,\ k(g)=j\big)\longrightarrow
\frac{R_q(a,c;j)}{q^{ac}}
\quad(0\leq j\leq\min(a,c)),
\]
and all probabilities outside these joint values tend to zero. Thus almost every element has the maximal conjugacy-class size \(q^{ac}\), while its square rank retains the nondegenerate rank distribution of a uniform \(a\)-by-\(c\) finite-field matrix. The total variation error is at most
\[
1-\prod_{i=0}^{a-1}(1-q^{i-b})
\]
for \(b\geq a\). In characteristic two, the limiting probability that an element has order four is \(1-q^{-ac}\).

## Assumptions and scope
The field is the finite field \(\mathbb F_q\), with no restriction on its characteristic. All three block sizes are positive integers. Ranks are over \(\mathbb F_q\). Conjugation is by the **unipotent radical itself**, not by its normalizing parabolic subgroup or by the ambient general linear group. Every matrix \(Z\) is permitted and counted separately. The invariant \(k(g)\) concerns \((g-I)^2\), not \(g^2-I\); in characteristic two these coincide, but they do not generally coincide in odd characteristic.

## Proof
Write \(N=g-I\). Its only possibly nonzero blocks are \(X,Y,Z\), and direct multiplication gives
\[
N^2=\begin{pmatrix}0&0&XY\\0&0&0\\0&0&0\end{pmatrix},\qquad N^3=0.
\]
Thus \(k(g)=\operatorname{rank}(XY)\). For another group element \(h=g(X',Y',Z')\), the equality \(gh=hg\) is equivalent to
\[
XY'-X'Y=0.
\]
The two central blocks do not occur. Let \(r=\operatorname{rank}X\) and \(s=\operatorname{rank}Y\). Consider the linear map
\[
L_{X,Y}:M_{a\times b}(\mathbb F_q)\oplus M_{b\times c}(\mathbb F_q)
\longrightarrow M_{a\times c}(\mathbb F_q),
\quad (X',Y')\longmapsto XY'-X'Y.
\]
Its first summand has image the space of matrices with column spaces contained in \(\operatorname{im}X\), of dimension \(cr\). Its second summand has image the space of matrices with row spaces contained in the row space of \(Y\), of dimension \(as\). Their intersection consists of maps with both restrictions, and has dimension \(rs\). Consequently
\[
\operatorname{rank}L_{X,Y}=cr+as-rs=:t.
\]
There are \(q^{ab+bc-t}\) choices of \((X',Y')\) satisfying commutation and independently \(q^{ac}\) choices of \(Z'\). Hence the centralizer of \(g\) has size \(q^{ab+bc+ac-t}\), and the group conjugacy class has cardinality \(q^t\).

It remains to count \((X,Y)\) with ranks \(r,s\) and product rank \(k\). There are exactly \(R_q(a,b;r)\) matrices \(X\) of rank \(r\). Fix one. Its kernel \(K\subset\mathbb F_q^b\) has dimension \(b-r\). A rank-\(s\) matrix \(Y\) has \(k=\operatorname{rank}(XY)\) precisely when its image \(U\) satisfies
\[
\dim U=s,\qquad \dim(U\cap K)=s-k.
\]
The permitted \(k\) are exactly \(\max(0,r+s-b)\leq k\leq\min(r,s)\). To count such \(U\), choose its intersection \(I=U\cap K\) in \({b-r\brack s-k}_q\) ways; choose its \(k\)-dimensional projection to \(\mathbb F_q^b/K\) in \({r\brack k}_q\) ways; and choose the graph map from that projection into \(K/I\) in \(q^{k(b-r-s+k)}\) ways. This parametrization is bijective. Once \(U\) is specified, the number of surjections \(\mathbb F_q^c\twoheadrightarrow U\), and hence the number of matrices \(Y\) with image \(U\), is \(S_q(c,s)\). The block \(Z\) is arbitrary, contributing \(q^{ac}\). Multiplying these factors and summing proves the displayed joint census. Since conjugation preserves both invariants, dividing element counts by their common class size gives the class counts.

For the limit, for \(b\geq a\) a uniform \(a\)-by-\(b\) matrix \(X\) has full row rank with probability
\[
\prod_{i=0}^{a-1}(1-q^{i-b}).
\]
On this event the image of the linear map \(Y\mapsto XY\) is all of \(M_{a\times c}(\mathbb F_q)\), and its fibers have equal cardinality, so \(XY\) is **exactly uniform** on this matrix space when \(Y\) is uniform. Furthermore \(t=cr+as-rs=ac\) for \(r=a\), regardless of \(s\). Coupling with the full-row-rank event gives the total variation error bound and limiting joint rank law. In characteristic two, \((I+N)^2=I+N^2\), while \((I+N)^4=I\). Thus an element has order four exactly when \(XY\ne0\), whose limiting probability is \(1-q^{-ac}\). This proves every assertion.

## Verification
The standalone file `verify.py` computes the closed coefficient formula using exact integers and independently enumerates all pairs of adjacent blocks over small prime fields, constructing the complete linear commutator map from basis matrices rather than using the proved rank formula. It compares every \((t,k)\) coefficient and verifies that the total number of elements is \(q^{ab+bc+ac}\). The packaged verifier passed eleven cases, including \((q,a,b,c)=(2,2,3,2)\) and \((3,2,2,2)\). It also checks the explicit \((2,2,2)\) square-rank refinement. Separate exact coefficient identities were tested for field orders \(2,3,4,5,7,8,9\) and six triples of block sizes, including nonprime prime powers. Finite checks are not the proof for all dimensions or fields; the preceding linear-algebra and subspace-lattice argument is the proof.

## Relationship to prior work
Hennecart and Perry, *A Quiver Analogue of Higman's Conjecture* (arXiv:2208.07738v1, 16 August 2022), §4, count commuting pairs in radicals with three block levels by an incidence count of a pair of linear maps. Their result supplies a total commuting-pair count but not the joint distribution of the conjugacy-class size of one element and the rank of that element's square. Goodwin and Röhrle, *Counting conjugacy classes in the unipotent radical of parabolic subgroups of GL_n(q)* (arXiv:0901.0667), prove polynomiality of the total class number for flags of length at most five and describe unipotent centralizers on parabolic orbits. Their structural results are acknowledged, not replaced with a claim of first counting conjugacy classes. Diaconis and Malliaris, *Complexity and randomness in the Heisenberg groups (and beyond)* (arXiv:2107.02923v2), §1–2, describe the one-dimensional-end-block Heisenberg special case and its commuting graphs. The previously published three-block Heisenberg and total-commutation specializations remain prior work. Neither those total counts nor the mere existence of centralizer dimensions specifies the present full \((t,k)\) census and fixed-end square-rank limit without additional incidence analysis.

## Limitations
This is not a parametrization of individual conjugacy classes, and equal class sizes and equal square ranks need not imply conjugacy. It does not classify ambient-parabolic or general-linear-group orbits, nor higher block-length radicals. Computational checks cover finite small prime fields; the algebraic proof covers arbitrary prime powers. The literature comparison supports originality relative to inspected sources but does not establish exhaustive publication priority, particularly across alternative terminology involving rank distributions of products of random rectangular matrices.

## References
1. L. Hennecart and N. Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1 (16 August 2022), https://arxiv.org/html/2208.07738v1.
2. S. M. Goodwin and G. Röhrle, *Counting conjugacy classes in the unipotent radical of parabolic subgroups of GL_n(q)*, arXiv:0901.0667 (2009), https://arxiv.org/abs/0901.0667.
3. P. Diaconis and M. Malliaris, *Complexity and randomness in the Heisenberg groups (and beyond)*, arXiv:2107.02923v2 (2021), https://arxiv.org/html/2107.02923v2.
4. S. Mozgovoy, *Commuting matrices and volumes of linear stacks*, arXiv:1901.00690 (2019), https://arxiv.org/abs/1901.00690.
