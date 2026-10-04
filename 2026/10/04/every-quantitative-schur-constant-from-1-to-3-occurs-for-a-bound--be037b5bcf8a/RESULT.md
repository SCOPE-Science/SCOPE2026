# Every quantitative Schur constant from \(1\) to \(3\) occurs for a bounded uniformly discrete Lipschitz-free space
## Finding
For a Banach space \(X\), write \(\sigma(X)\) for the infimum of the constants \(c>0\) for which \(X\) is \(c\)-Schur, meaning that every bounded sequence \((x_n)\subset X\) satisfies
\[
\operatorname{ca}(x_n)\le c\,\delta(x_n),
\]
where
\[
\operatorname{ca}(x_n)=\inf_N\sup_{k,l\ge N}\|x_k-x_l\|
\]
and
\[
\delta(x_n)=\sup_{x^*\in B_{X^*}}\left(\limsup_n x^*(x_n)-\liminf_n x^*(x_n)\right).
\]
Then every value in \([1,3]\) occurs exactly as \(\sigma(\mathcal F(M))\) for a countable bounded uniformly discrete metric space \(M\). More precisely, for every \(q\in[1,3]\) the two explicit families below give a \(1\)-separated space \(M_q\) of diameter \(q\) with
\[
\sigma(\mathcal F(M_q))=q.
\]
Together with the universal \(3\)-Schur theorem for uniformly discrete metric spaces, this shows that the spectrum of optimal quantitative Schur constants of nonzero bounded uniformly discrete Lipschitz-free spaces is exactly \([1,3]\).

## Assumptions and scope
All spaces and free spaces are real. For \(1\le q\le2\), let \(M_q^{(A)}=\mathbb Z\) with basepoint \(0\) and
\[
d_q(m,n)=\begin{cases}
0,&m=n,\\
q,&m=-n\ne0,\\
1,&\text{otherwise}.
\end{cases}
\]
For \(2\le q\le3\), let \(M_q^{(B)}=\mathbb Z\setminus\{0\}\) with basepoint \(1\) and
\[
d_q(m,n)=\begin{cases}
0,&m=n,\\
q,&m=-n,\\
1,&mn<0\text{ and }m\ne-n,\\
2,&mn>0\text{ and }m\ne n.
\end{cases}
\]
The first formula is a metric because its only nonunit nonzero side has length at most \(2\). The second is a metric because an antipodal side has an alternative two-edge path of length \(3\), a same-sign side of length \(2\) has a two-edge path of length \(2\) through a nonantipodal point of the opposite sign, and all remaining sides have length \(1\). Thus both families are \(1\)-separated, bounded, complete, and uniformly discrete.

## Proof
Kalenda's Proposition 8.2 in arXiv:2505.12893v1 states that if all nonzero distances in a bounded metric space lie in \([a,b]\), then its Lipschitz-free space is \(b/a\)-Schur. Hence \(\mathcal F(M_q^{(A)})\) is \(q\)-Schur for \(1\le q\le2\), and \(\mathcal F(M_q^{(B)})\) is \(q\)-Schur for \(2\le q\le3\). It remains to prove that these constants cannot be lowered.

For the first family, define a bounded sequence in \(\mathcal F(M_q^{(A)})\) by
\[
x_{2n-1}=\delta(n),\qquad x_{2n}=\delta(-n)\qquad(n\ge1).
\]
The canonical map \(\delta:M_q^{(A)}\to\mathcal F(M_q^{(A)})\) is isometric. Every tail of \((x_k)\) contains an antipodal pair, so
\[
\operatorname{ca}(x_k)=q.
\]
Let \(f\in B_{\operatorname{Lip}_0(M_q^{(A)})}\). Among the antipodal pairs \(\{n,-n\}\), at most one can satisfy \(|f(n)-f(-n)|>1\): if \(a>b+1\) are the values on one such pair, then every point belonging to any other antipodal pair has value in \([a-1,b+1]\), an interval of length strictly less than \(1\). After deleting that possible exceptional pair, all remaining values of \(f\) have diameter at most \(1\). Therefore
\[
\delta(x_k)\le1.
\]
Equality holds: the function taking value \(1\) on positive integers and \(0\) on nonpositive integers is \(1\)-Lipschitz and makes \(f(x_k)\) alternate between \(1\) and \(0\). Hence \(\delta(x_k)=1\), so the inequality \(\operatorname{ca}\le c\delta\) fails for every \(c<q\). Thus
\[
\sigma(\mathcal F(M_q^{(A)}))=q\qquad(1\le q\le2).
\]

For the second family, set
\[
y_n=\delta(n)-\delta(-n)\qquad(n\ge1).
\]
Since the norm of a molecule \(\delta(u)-\delta(v)\) equals \(d_q(u,v)\), one has \(\|y_n\|=q\) for every \(n\). If \(f\) is \(1\)-Lipschitz on \(M_q^{(B)}\), there is at most one index \(n\) with \(f(n)-f(-n)>1\): indeed, for \(m\ne n\), the two cross distances \(d_q(m,-n)\) and \(d_q(-m,n)\) equal \(1\), so
\[
f(m)-f(-m)\le 2-\bigl(f(n)-f(-n)\bigr)<1.
\]
Applying the same argument to \(-f\) shows that at most one index can satisfy \(f(n)-f(-n)<-1\). Hence, for every \(f\) in the unit ball of the Lipschitz dual,
\[
\limsup_n |f(n)-f(-n)|\le1.
\]
It follows that every weak-star cluster point \(y^{**}\) of \((y_n)\) in \(\mathcal F(M_q^{(B)})^{**}\) satisfies \(\|y^{**}\|\le1\). Proposition 5.1 of arXiv:2505.12893v1 gives the equivalent consequence of the \(c\)-Schur property
\[
\limsup_n\|z_n\|\le c\,\sup\{\|z^{**}\|:z^{**}\text{ is a weak-star cluster point of }(z_n)\}.
\]
Applied to \((y_n)\), this would force \(q\le c\). Therefore \(\mathcal F(M_q^{(B)})\) is not \(c\)-Schur for any \(c<q\), and
\[
\sigma(\mathcal F(M_q^{(B)}))=q\qquad(2\le q\le3).
\]

Finally, every nonzero Banach space has optimal Schur constant at least \(1\): for a nonzero vector \(u\), the alternating sequence \(u,-u,u,-u,\ldots\) has \(\operatorname{ca}=\delta=2\|u\|\). Cúth and Kalenda prove in arXiv:2604.01875v1 that every uniformly discrete metric space has \(3\)-Schur free space. The two families above realize every \(q\in[1,3]\), proving that the full spectrum is exactly \([1,3]\).

## Verification
The metric inequalities were checked symbolically by cases. In the first family, the only potentially restrictive triangle has side lengths \(q,1,1\), and \(q\le2\). In the second family, the only potentially restrictive antipodal triangle has side lengths \(q,2,1\), and \(q\le3\); same-sign distance \(2\) is supported by a \(1+1\) path. The lower-bound witnesses use only the canonical isometry of the metric into its free space and the exact dual characterization by \(1\)-Lipschitz functions. The endpoint \(q=2\) in the first family and \(q=3\) in the second recover the metric patterns of Kalenda's Examples 8.3 and 8.5, respectively.

## Relationship to prior work
Kalenda's 2025 paper proves the general upper bound \(b/a\) for bounded uniformly separated spaces and gives two endpoint examples: an exact constant \(2\) example (Example 8.3) and an exact constant \(3\) example (Example 8.5). The same paper does not state a parameter family realizing intermediate optimal constants. Cúth and Kalenda's 2026 theorem later proves the global \(3\)-Schur bound for every uniformly discrete metric space and records the sharpness of \(3\). The present finding interpolates the endpoint mechanisms with two explicit one-parameter metrics and determines the complete set of optimal constants that can occur in the bounded uniformly discrete class.

## Limitations
The finding classifies which optimal constants occur, not which metric spaces have a prescribed constant. The constructions are countable and bounded; no claim is made that the same parameter can be realized inside a narrower geometric class such as ultrametric spaces, where the known constant is \(1\). The originality check found no published statement of the full interval realization, but the proof deliberately deforms two published endpoint constructions, so an unindexed equivalent parameterization remains a literature risk. No independent audit has been performed.

## References
1. O. F. K. Kalenda, *Quantitative Schur property and measures of weak non-compactness*, arXiv:2505.12893v1, first posted 19 May 2025. Relevant items: Proposition 5.1, Proposition 8.2, Examples 8.3 and 8.5.
2. M. Cúth and O. F. K. Kalenda, *Lipschitz-free spaces over uniformly discrete metric spaces are 3-Schur*, arXiv:2604.01875v1, first posted 2 April 2026. Relevant item: Theorem 1.1.
