# Bidirectional product-rank fibers of square-zero matrix pairs

## Finding

Let \(q\) be any prime power, \(n\geq 1\), and \(V=\mathbb F_q^n\). For nonnegative integers \(a,b,r,s\), let \(F_{n,q}(a,b;r,s)\) count **ordered** pairs of linear operators \((X,Y)\) on \(V\) with
\[
X^2=Y^2=0,\qquad \operatorname{rank}X=a,\quad \operatorname{rank}Y=b,\quad
\operatorname{rank}(XY)=r,\quad \operatorname{rank}(YX)=s.
\]

Write \({u\brack v}_q\) for a Gaussian binomial coefficient, understood to vanish when \(v\notin\{0,\dots,u\}\), and set \(g_j(q)=\prod_{i=0}^{j-1}(q^j-q^i)\), with \(g_0(q)=1\). Assume \(0\leq a,b\leq\lfloor n/2\rfloor\) and \(0\leq r,s\leq\min(a,b)\). Put \(m=n-a-b\); for each integer \(c\), put \(d=b-r-c\) and \(e=m-b+s+c\). Then

\[
\boxed{\begin{aligned}
F_{n,q}(a,b;r,s)
={}&{n\brack a}_q{n-a\brack a}_q\,g_a(q)g_b(q)
{a\brack r}_q q^{r(m+r)}\\[-1mm]
&\quad\times\sum_{c\in\mathcal C}
{a\brack c}_q{n-2a\brack d}_q
{a-c\brack s}_q{m+c\brack e}_q
q^{d(a-c)+se},
\end{aligned}}
\]
where the **finite, explicit** index set is
\[
\mathcal C=\{c\in\mathbb Z:0\leq c\leq\min(a,b),\ 0\leq d\leq n-2a,\ 0\leq s\leq a-c,\ 0\leq e\leq m+c\}.
\]
All summands are nonnegative integers. Outside the stated rank ranges, the count is zero.

**Exact support and rank-asymmetry threshold.** For valid \(a,b,r,s\),
\[
\boxed{F_{n,q}(a,b;r,s)>0\quad\Longleftrightarrow\quad |r-s|\leq n-a-b.}
\]
In particular the greatest attainable asymmetry for fixed \(a,b\) is \(\min\{n-a-b,a,b\}\). Thus in the maximally square-zero case \(n=2h\) and \(a=b=h\), both product ranks must coincide, and their complete common-rank count collapses to
\[
\boxed{F_{2h,q}(h,h;r,s)=\mathbf1_{r=s}
{2h\brack h}_q\,g_h(q)^2\,{h\brack r}_q^2\,q^{r^2}.}
\]

As a normalization, for each pair of allowed individual ranks,
\[
\sum_{r=0}^{\min(a,b)}\sum_{s=0}^{\min(a,b)} F_{n,q}(a,b;r,s)
=\left({n\brack a}_q{n-a\brack a}_qg_a(q)\right)
\left({n\brack b}_q{n-b\brack b}_qg_b(q)\right).
\]
The distribution is symmetric under \((a,b;r,s)\leftrightarrow(b,a;s,r)\).

For \(n=3\), \(q=2\), and \(a=b=1\), the ordered multiplicities at product-rank pairs \((r,s)=(0,0),(0,1),(1,0),(1,1)\) are respectively \(105,84,84,168\). For \(n=4\), \(q=2\), and \(a=b=2\), the only possible pairs are \((0,0),(1,1),(2,2)\), with respective counts \(1260,22680,20160\).

## Assumptions and scope

The field is arbitrary finite \(\mathbb F_q\); no restriction on characteristic or prime-field degree is imposed. The matrices are not assumed to commute or anticommute. The algebra represented is \(\mathbb F_q\langle x,y\rangle/(x^2,y^2)\), without any mixed relation. All counts refer to actual ordered matrices, **not** simultaneous-similarity classes or geometric components. The empty products and rank-zero cases are included.

## Proof

**1. Parameterize square-zero operators.** For an operator \(X\) of rank \(a\), let \(U=\operatorname{im}X\) and \(K=\ker X\). Then \(U\subseteq K\), \(\dim U=a\), and \(\dim K=n-a\). Conversely a flag \(U\subseteq K\) of those dimensions, together with an isomorphism \(V/K\cong U\), uniquely determines \(X\). Hence the number of choices of \(X\) is
\[
Z_{n,q}(a)={n\brack a}_q{n-a\brack a}_qg_a(q).
\]
Fix one such \(X\). A square-zero \(Y\) of rank \(b\) corresponds bijectively to \(S=\operatorname{im}Y\subseteq W=\ker Y\) with \(\dim S=b\), \(\dim W=n-b\), and an isomorphism \(V/W\cong S\). Every flag \(S\subseteq W\) produces exactly \(g_b(q)\) operators \(Y\).

**2. Translate the two composition ranks into flag intersections.** Because \(X\) is injective on \(V/K\), and likewise \(Y\) on \(V/W\),
\[
r=b-\dim(S\cap K),\qquad s=a-\dim(U\cap W).
\]
Set \(c=\dim(S\cap U)\), so \(\dim(S\cap K)=b-r\), and define \(d=b-r-c\). The nested fixed flag is \(U\subseteq K\subseteq V\), with quotient dimensions \(a,n-2a,a\).

**3. Count the image subspace \(S\).** First choose \(S\cap U\), giving \({a\brack c}_q\) choices. Next choose the image of \(S\cap K\) in \(K/U\), giving \({n-2a\brack d}_q\) choices. Its lifts into \(U/(S\cap U)\) contribute \(q^{d(a-c)}\). Finally choose the image of \(S\) in \(V/K\), giving \({a\brack r}_q\) choices, and lift it into \(K/(S\cap K)\), whose dimension is \(n-a-(b-r)=m+r\). This last lift contributes \(q^{r(m+r)}\). Thus, for fixed \(c\), the number of possible \(S\) is
\[
{a\brack c}_q{n-2a\brack d}_q{a\brack r}_q
q^{d(a-c)+r(m+r)}.
\]
The construction and its inverse are unique at every stage, so no multiplicities are hidden in the lifting counts.

**4. Count kernels \(W\supseteq S\).** In \(V/S\), the image \(U'=(U+S)/S\) has dimension \(a-c\). The quotient kernel \(W/S\) has dimension \(n-2b\), and the desired intersection dimension is \(\dim((W/S)\cap U')=a-s-c\). Choose this intersection in \(U'\), then choose the image of \(W/S\) in \((V/S)/U'\), which has dimension \(n-a-b+c=m+c\). The latter image has dimension
\[
e=(n-2b)-(a-s-c)=m-b+s+c.
\]
For each such pair of subspaces, its graph lifts into the \(s\)-dimensional quotient of \(U'\), producing \(q^{se}\) possibilities. Hence the number of \(W\) above a fixed \(S\) is exactly
\[
{a-c\brack s}_q{m+c\brack e}_q q^{se}.
\]
Multiplying these counts, summing over the permitted \(c\), multiplying by \(g_b(q)\), and then by \(Z_{n,q}(a)\) proves the displayed formula.

**5. Prove sharp support.** The summation has a nonempty index set precisely when
\[
\max\{0,a-m-r,b-m-s\}\leq\min\{a-s,b-r\}.
\]
For allowed \(a,b,r,s\), the inequalities \(2a\leq n\) and \(2b\leq n\) make every comparison between these bounds automatic except
\[
s-r\leq m,\qquad r-s\leq m.
\]
These are equivalent to \(|r-s|\leq m\). A nonempty index set produces strictly positive factors, proving necessity and sufficiency. Taking the maximum possible difference of two values in \(\{0,\dots,\min(a,b)\}\) gives the stated sharp asymmetry.

**6. Derive the balanced formula and normalization.** If \(n=2h\) and \(a=b=h\), then \(\operatorname{im}X=\ker X\) and \(\operatorname{im}Y=\ker Y\). Thus \(r=s=h-\dim(U\cap S)\). There are \({h\brack r}_q^2q^{r^2}\) choices of the \(h\)-subspace \(S\) meeting fixed \(U\) in dimension \(h-r\), and \(g_h(q)\) choices of \(Y\) for each such \(S\). Multiply by \({2h\brack h}_qg_h(q)\) choices of \(X\). Finally, each pair of square-zero operators appears exactly once in the flag partition from steps 1–4, so summing all \((r,s)\) yields \(Z_{n,q}(a)Z_{n,q}(b)\). Interchanging \(X\) and \(Y\) proves the stated symmetry.

## Verification

The standalone standard-library script `verify_joint_squarezero.py` computes the Gaussian formula and independently enumerates square-zero matrices and the ranks of both matrix products. It checks the complete joint tables for \((n,q)=(2,2),(3,2),(4,2),(3,3),(3,4)\), including genuine arithmetic in the extension field \(\mathbb F_4\). It also checks normalization, product-order symmetry, exact support, and the balanced specialization for \(1\leq n\leq11\) and \(q\in\{2,3,4,5,7\}\). The finite tests corroborate but do not prove the unrestricted symbolic theorem.

## Relationship to prior work

Schröer [1] treats the algebraic varieties defined by the additional equations \(XY=YX=0\), classifying irreducible components; his results concern the \((r,s)=(0,0)\) fiber, not arbitrary mixed-product ranks or their finite-field multiplicities. Oblak [2] studies Jordan forms within that mutual-annihilation locus. Huang [3] gives an unrefined finite-field generating series under the same mutual-annihilation relations. Bernau and Abian [4], following Flanders [5], study the much broader elementary-divisor relationship between products \(XY\) and \(YX\), but their structural theorem does not supply the square-zero finite-field joint multiplicities. The present result is an arithmetic refinement for **noncommuting, potentially nonannihilating** square-zero pairs. No claim of priority for the standard Gaussian-subspace counts or for classical product-rank constraints is made.

## Limitations

This is a count of ordered matrices, not a classification of simultaneous-conjugacy orbits or of their geometric closures. It does not give the joint Jordan types of nonzero products; those may carry additional information beyond ranks. A historical formula under equivalent flag-incidence or tensor-algebra notation could remain undiscovered; independent literature and mathematical audits have not been conducted.

## References

[1] J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (first public version 2002-11-19); *Commentarii Mathematici Helvetici* **79** (2004), 396–426.

[2] P. Oblak, *Jordan forms for mutually annihilating nilpotent pairs*, arXiv:math/0612300 (2006); *Linear Algebra and its Applications* **428** (2008), 1476–1491.

[3] Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (2021).

[4] S. J. Bernau and A. Abian, *Jordan canonical forms of matrices AB and BA*, *Rendiconti dell’Istituto di Matematica dell’Università di Trieste* **20** (1988), 101–108. Open-access PDF: https://www.openstarts.units.it/bitstreams/aff84858-13ba-49bd-a234-36b8a77a60db/download

[5] H. Flanders, *Elementary Divisors of AB and BA*, *Proceedings of the American Mathematical Society* **2** (1951), 871–874, DOI:10.2307/2031700.
