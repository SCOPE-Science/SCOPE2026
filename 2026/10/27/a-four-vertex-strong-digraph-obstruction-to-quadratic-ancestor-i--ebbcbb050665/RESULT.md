# A four-vertex strong-digraph obstruction to quadratic ancestor inequalities

## Finding

**Theorem.** On a fixed strongly connected directed graph with four vertices and strictly positive arc weights, the directed in-arborescence analogue of the quadratic ancestor inequality can fail by an arbitrarily large factor. More precisely, for every real \(z>0\) there is a weighted digraph \(G_z\) with distinguished root \(r\), a singleton \(B=\{b\}\), and a probability measure \(f_z\) supported on two other vertices such that the ratio

\[
\mathcal R(z)=\frac{\mathbb P(\operatorname{LCA}_T(X,Y)=b)}{\mathbb P(b\in\gamma_X)^2}
=\frac{1+z+2z^2+z^3}{2z(z+1)(z+2)}
\sim\frac1{4z}\quad(z\downarrow0).
\]

Here \(T\) is a product-weighted random in-arborescence toward \(r\), \(X,Y\) are independent with law \(f_z\), independently of \(T\), and \(\gamma_v\) is the directed parent path from \(v\) to \(r\) (including endpoints). Thus there is **no finite universal multiplicative constant** for the directed counterpart, even with strong connectivity, strictly positive weights, and a fixed four-vertex underlying graph.

At the concrete rational parameter \(z=1/8\), the ratio is exactly \(593/306>1\). For this family, the quadratic inequality fails precisely when \(1-3z-4z^2-z^3>0\); the polynomial has a unique positive zero.

## Assumptions and scope

Let \(V=\{r,b,x,y\}\). For \(z>0\) consider exactly the seven arcs with the indicated weights:

| Arc | Weight |
| --- | ---: |
| \(r\to b\) | \(1\) |
| \(b\to r\) | \(z\) |
| \(b\to x\) | \(1\) |
| \(x\to b\) | \(z\) |
| \(x\to y\) | \(1\) |
| \(y\to b\) | \(z\) |
| \(y\to r\) | \(1\) |

The cycle \(r\to b\to x\to y\to r\) proves strong connectivity. An *in-arborescence toward* \(r\) is a spanning directed tree in which each non-root vertex has exactly one outgoing parent arc and following parents eventually reaches \(r\). A random in-arborescence has probability proportional to the product of weights of its selected arcs. The outgoing root arc never belongs to such a tree.

Define \(H_b(v)=\mathbb P(b\in\gamma_v)\) for \(v\in\{x,y\}\), and \(a_b(x,y)=\mathbb P(\operatorname{LCA}_T(x,y)=b)\). Define the probability distribution

\[
f_z(x)=\frac{z+1}{2z+3},\qquad f_z(y)=\frac{z+2}{2z+3},\qquad f_z(r)=f_z(b)=0.
\]

The lowest common ancestor is the first common vertex encountered on the two parent paths from their respective starting vertices.

## Proof

A non-root parent choice is one of \(2^3=8\) combinations. Exactly three choices are invalid: two create the directed two-cycle \(b\leftrightarrow x\), and one creates \(b\to x\to y\to b\). The five valid choices appear below. The triple in the first column lists \((p(b),p(x),p(y))\), where \(p\) denotes the chosen parent.

| Parent triple | Weight | \(b\in\gamma_x\) | \(b\in\gamma_y\) | \(\operatorname{LCA}(x,y)=b\) |
| --- | ---: | :---: | :---: | :---: |
| \((r,b,r)\) | \(z^2\) | yes | no | no |
| \((r,b,b)\) | \(z^3\) | yes | yes | yes |
| \((r,y,r)\) | \(z\) | no | no | no |
| \((r,y,b)\) | \(z^2\) | yes | yes | no |
| \((x,y,r)\) | \(1\) | no | no | no |

Consequently the exact normalizing partition function is

\[
Z=1+z+2z^2+z^3,
\quad H_b(x)=\frac{z^2(z+2)}Z,
\quad H_b(y)=\frac{z^2(z+1)}Z,
\quad a_b(x,y)=\frac{z^3}Z.
\]

The diagonal ancestor events vanish for \(v\in\{x,y\}\), because \(\operatorname{LCA}(v,v)=v\ne b\). Taking \(f_z(x)=H_b(y)/(H_b(x)+H_b(y))\) and \(f_z(y)=H_b(x)/(H_b(x)+H_b(y))\), independence of \(X,Y\) gives

\[
\mathbb P(\operatorname{LCA}(X,Y)=b)
=2f_z(x)f_z(y)a_b(x,y),
\qquad
\mathbb P(b\in\gamma_X)=f_z(x)H_b(x)+f_z(y)H_b(y).
\]

Their quotient is therefore

\[
\mathcal R(z)=\frac{a_b(x,y)}{2H_b(x)H_b(y)}
=\frac{1+z+2z^2+z^3}{2z(z+1)(z+2)}.
\]

All denominators are strictly positive for \(z>0\). Since the numerator tends to one and the denominator is asymptotic to \(4z\), \(\mathcal R(z)\sim(4z)^{-1}\), proving unboundedness. Furthermore, comparison of numerator and denominator shows

\[
\mathcal R(z)>1\quad\Longleftrightarrow\quad1-3z-4z^2-z^3>0.
\]

This cubic is strictly decreasing on \((0,\infty)\), starts positive and tends to minus infinity, so the indicated parameter threshold is unique. At \(z=1/8\), the exact values are \(Z=593/512\), \(H_b(x)=17/593\), \(H_b(y)=9/593\), \(a_b(x,y)=1/593\), and \((f_z(x),f_z(y))=(9/26,17/26)\), hence \(\mathcal R=593/306\). The same example violates the pointwise directed analogue of \(a_b(x,y)\le 2H_b(x)H_b(y)\).

## Verification

Execute `python3 verify.py` with Python 3 and no external dependencies. The program independently enumerates the parent choices, discards cyclic assignments, computes the common ancestor and path indicators, proves that each vertex can reach every other in the underlying digraph, checks the symbolic formulas on seventeen exact rational parameters, and confirms the rational witness and quotient. The unboundedness and unique-threshold statements additionally follow by elementary polynomial algebra in the proof, not by numerical sampling.

## Relationship to prior work

Gefei Cai, *A Quadratic Ancestor Inequality for Spanning Trees* (arXiv:2610.22180v1, first public October 15, 2026), Theorem 1.1, proves the probability bound and the related pointwise inequality for product-weighted **undirected** spanning trees. That result rests on graphic-matroid complete log-concavity. The family here retains an elementary tree-product measure but discards undirected edge symmetry; the exact quotient shows that neither a directed extension with the same constant nor one with any finite graph-independent constant is possible. This finding is a limitation of a possible extension, not a contradiction of the undirected theorem.

Relevant broader research on edge-negative dependence in random *undirected* forests concerns another class of measures and does not yield this directed counterexample merely by changing terminology. See Grimmett (2004) for that distinction.

## Limitations

This is a counterexample for unrestricted positive arc-weighted, strongly connected directed graphs. It does **not** rule out estimates under reversibility, bidirectional conductance constraints, balance assumptions, or other stronger structural hypotheses. It does not assert a universal numerical optimum over all directed graphs or a minimum number of vertices. Exact symbolic enumeration certifies this family only; priority against unlocated results in directed branching theory still requires independent literature review. 

## References

1. Gefei Cai, *A Quadratic Ancestor Inequality for Spanning Trees*, arXiv:2610.22180v1 (2026-10-15), https://arxiv.org/html/2610.22180v1, Theorem 1.1 and Section 2.
2. G. R. Grimmett, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460, doi:10.1002/rsa.20012 (background on undirected measures).
