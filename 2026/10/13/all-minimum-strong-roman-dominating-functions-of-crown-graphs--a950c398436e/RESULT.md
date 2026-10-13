# All minimum strong Roman dominating functions of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). A strong Roman dominating function is denoted by \(f\). The already published minimum-value formula is
\[
\gamma_{\mathrm{StR}}(\operatorname{Cr}_n)=
\begin{cases}
n+1,&n\text{ odd},\\
n+2,&n\text{ even}.
\end{cases}
\]
The new statement here is the complete classification and count of every function attaining that value.

If \(n=2m+1\), there are exactly \(n\) minimum functions. Choose one index \(k\); then
\[
f(a_k)=f(b_k)=m+1
\]
and every other vertex has label \(0\).

If \(n=2m\), write \(P_A=\{i:f(a_i)>0\}\) and \(P_B=\{i:f(b_i)>0\}\). Every minimum function belongs to exactly one of the following five disjoint families.

1. Common singleton: \(P_A=P_B=\{k\}\), with \(f(a_k)=f(b_k)=m+1\). There are \(n\) functions.
2. Two-by-one support: \(P_A=\{k,u\}\), \(P_B=\{k\}\), where \(k\ne u\), with \(f(a_k)=m+1\), \(f(a_u)=1\), and \(f(b_k)=m\). There are \(n(n-1)\) functions.
3. The symmetric one-by-two support: there are another \(n(n-1)\) functions.
4. Two supports meeting once: \(P_A=\{k,u\}\) and \(P_B=\{k,v\}\), where \(k,u,v\) are distinct, with \(f(a_k)=f(b_k)=m\) and the two other positive labels equal to \(1\). There are \(n(n-1)(n-2)\) functions.
5. Identical two-supports: \(P_A=P_B=\{k,\ell\}\). On each side independently, one of the two vertices has label \(m\) and the other label \(1\). There are \(4\binom n2=2n(n-1)\) functions.

Consequently, for even \(n\), the number of minimum functions is
\[
n+4n(n-1)+n(n-1)(n-2)=n(n^2+n-1).
\]

## Assumptions and scope
The graph is finite, simple, and undirected, and \(n\ge3\). The strong Roman definition used is the standard one: if \(Z=\{v:f(v)=0\}\), every \(v\in Z\) has a neighbor \(w\) satisfying
\[
f(w)\ge 1+\left\lceil\frac{|N(w)\cap Z|}{2}\right\rceil.
\]
The label range is the standard range \(\{0,1,\ldots,1+\lceil(n-1)/2\rceil\}\), since \(\operatorname{Cr}_n\) is \((n-1)\)-regular.

The scalar value of \(\gamma_{\mathrm{StR}}(\operatorname{Cr}_n)\) is not claimed as new: it appears as Proposition 12 in the 2026 exact-values paper cited below. The contribution assessed here is the full minimum-function classification and its exact enumeration.

## Proof
Let
\[
Z_A=\{i:f(a_i)=0\},\qquad Z_B=\{i:f(b_i)=0\},
\]
and put \(p=|Z_A|\), \(q=|Z_B|\), \(c=|Z_A\cap Z_B|\), and
\[
r=n-p-q+c.
\]
Thus \(r\) is the number of indices at which both matched vertices are positive. Define the positive-label excesses over the baseline label \(1\) by
\[
E_A=\sum_{i\notin Z_A}(f(a_i)-1),\qquad
E_B=\sum_{i\notin Z_B}(f(b_i)-1).
\]
The weight is
\[
w(f)=2n-p-q+E_A+E_B.
\]

Fix the zero sets. To defend the \(q\) zero vertices in \(B\), a positive vertex \(a_i\) with \(i\notin Z_B\) is adjacent to all of them, so one such strong vertex costs excess \(\lceil q/2\rceil\). If no such common-positive index is used, every strong \(A\)-defender has its index in \(Z_B\), misses its matched zero vertex, and therefore at least two distinct defenders are necessary; each then costs excess \(\lceil(q-1)/2\rceil\). Hence the exact least possible \(A\)-side excess for the fixed zero supports is
\[
\varepsilon_A=
\min\left(
\left\{\left\lceil\frac q2\right\rceil:r\ge1\right\}
\cup
\left\{2\left\lceil\frac{q-1}{2}\right\rceil:q-c\ge2\right\}
\right),
\]
with \(\varepsilon_A=0\) when \(q=0\); if the displayed set is empty the zero supports are infeasible. The formula is exact because one common-positive defender covers all \(q\) zeros in the first case, while two distinct inside-index defenders cover all \(q\) zeros in the second. Symmetrically,
\[
\varepsilon_B=
\min\left(
\left\{\left\lceil\frac p2\right\rceil:r\ge1\right\}
\cup
\left\{2\left\lceil\frac{p-1}{2}\right\rceil:p-c\ge2\right\}
\right).
\]
Therefore the least weight compatible with fixed \((p,q,c)\) is exactly
\[
2n-p-q+\varepsilon_A+\varepsilon_B.
\]
In particular,
\[
E_A\ge\left\lceil\frac q2\right\rceil,
\qquad
E_B\ge\left\lceil\frac p2\right\rceil,
\]
so every feasible function satisfies
\[
w(f)\ge 2n-\left\lfloor\frac p2\right\rfloor-\left\lfloor\frac q2\right\rfloor.
\]

Suppose first that \(n=2m+1\). A minimum function cannot have an entire bipartition class zero: if, for example, \(p=n\), then \(q>0\) is infeasible, while \(q=0\) has weight at least \(n+2\lceil(n-1)/2\rceil>n+1\). Hence \(p,q\le n-1\), and the lower bound is at least \(n+1\). Equality requires \(p=q=n-1\). With one positive vertex on each side, feasibility forces their indices to coincide, so \(c=n-1\) and \(r=1\). Each positive vertex then has excess \(m\), hence label \(m+1\). This proves the odd classification and its count \(n\).

Now let \(n=2m\). Again an entire zero bipartition class cannot occur in a minimum function. Thus \(p,q\le n-1\), and the lower bound is at least \(n+2\). Equality forces
\[
p,q\in\{n-2,n-1\}.
\]
For \(n\ge6\), the inside-only two-defender option is strictly more expensive than the displayed coarse bound, so equality requires \(r\ge1\). For \(n=4\), the exact fixed-support formula above gives the same conclusion. The feasible equality triples are therefore exactly
\[
(n-1,n-1,n-1),
\quad(n-2,n-1,n-2),
\quad(n-1,n-2,n-2),
\]
and
\[
(n-2,n-2,n-3),
\quad(n-2,n-2,n-2),
\]
where each triple records \((p,q,c)\). Their corresponding values of \(r\) are \(1,1,1,1,2\).

At equality, exactly one common-positive defender on each side carries the whole required excess; every other positive label is \(1\). Translating the five zero-support triples into positive supports gives precisely the five families stated in the finding. In the final family there are two common-positive indices, and either can be the unique strong defender on each side, independently, which accounts for the factor \(4\). Summing the five disjoint family sizes gives \(n(n^2+n-1)\).

## Verification
The accompanying standalone checker implements the strong Roman definition directly. It exhaustively enumerates every allowed labeling for \(n=3,4,5\), and the resulting minimum-function sets agree exactly with the classification: respectively \(3\), \(76\), and \(5\) functions. It also evaluates the exact fixed-zero-support formula for every feasible \((p,q,c)\) through \(n=50\), recovering only the equality patterns used in the proof, and constructs every classified minimum function through \(n=20\) and checks it directly.

The replay output is:

`VERIFY_OK exhaustive_n=3..5 filtered_labelings=11182 pattern_n=3..50 pattern_checks=316236 classified_n=3..20 generated_minima=25719`

The finite computation is a check of the proof and boundary cases, not a substitute for the all-\(n\) argument.

## Relationship to prior work
Álvarez-Ruiz, González Yero, Mediavilla-Gradolph, Sheikholeslami, and Valenzuela introduced strong Roman domination and gave the standard definition and general bounds. Valenzuela-Tripodoro, Mateos-Camacho, Cera López, and Álvarez-Ruíz later proved the exact crown-graph value
\[
\gamma_{\mathrm{StR}}(\operatorname{Cr}_n)=n+1\text{ for odd }n,
\qquad
\gamma_{\mathrm{StR}}(\operatorname{Cr}_n)=n+2\text{ for even }n.
\]
Their crown-graph proposition determines the scalar optimum and exhibits a canonical optimal labeling; it does not state a classification or count of all minimum functions. The present result strictly refines that proposition at the level of the complete optimum set. In particular, the scalar parity formula conceals a sharper distinction: odd crowns have only \(n\) optima, whereas even crowns have \(n(n^2+n-1)\) optima spread over five support geometries.

Searches for the exact count, for minimum strong Roman functions on crowns, and for the equivalent description \(K_{n,n}\) minus a perfect matching did not locate another statement of this classification. Closely related exact results for complete multipartite graphs do not imply it because a crown graph is not complete multipartite when \(n\ge3\).

## Limitations
The originality claim is restricted to the minimum-function classification and enumeration; the strong Roman domination number itself is already published. The literature comparison cannot exclude an obscure or poorly indexed equivalent classification, so that remains a residual bibliographic risk. No claim is made about the full weight enumerator of nonminimum strong Roman dominating functions.

## References
1. M. P. Álvarez-Ruiz, I. González Yero, T. Mediavilla-Gradolph, S. M. Sheikholeslami, and J. C. Valenzuela, *On the Strong Roman Domination Number of Graphs*, arXiv:1502.03933, first public version 2015-02-13; later published in *Discrete Applied Mathematics*, DOI: 10.1016/j.dam.2016.12.013.
2. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, and M. P. Álvarez-Ruíz, *Complexity and Exact Values for [k]-Roman and Strong Roman Domination for Specific Graph Families*, *Mathematics* 14 (2026), 1535, DOI: 10.3390/math14091535.
