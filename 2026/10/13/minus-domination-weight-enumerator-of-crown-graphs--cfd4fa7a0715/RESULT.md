# Minus-domination weight enumerator of crown graphs
## Finding
For every integer \(n\ge 3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M_n,
\]
where the bipartition classes are \(A_0=\{a_1,\ldots,a_n\}\) and \(B_0=\{b_1,\ldots,b_n\}\), and the deleted perfect matching consists of the nonedges \(a_i b_i\).

A minus dominating function is a map \(f:V(\operatorname{Cr}_n)\to\{-1,0,1\}\) such that \(f(N[v])\ge1\) for every vertex \(v\). Write
\[
x_i=f(a_i),\qquad y_i=f(b_i),\qquad A=\sum_{i=1}^n x_i,\qquad B=\sum_{i=1}^n y_i,
\]
and
\[
m=\min_i(x_i-y_i),\qquad M=\max_i(x_i-y_i).
\]
Then
\[
f\text{ is minus dominating}\quad\Longleftrightarrow\quad A\ge1+M\text{ and }B\ge1-m.
\]

This criterion gives an exact enumerator for every feasible function. Let \(u\) mark the sum on \(A_0\) and \(v\) mark the sum on \(B_0\). For a single matched pair define
\[
\begin{aligned}
\Phi_{-2}(u,v)&=u^{-1}v,\\
\Phi_{-1}(u,v)&=u^{-1}+v,\\
\Phi_{0}(u,v)&=u^{-1}v^{-1}+1+uv,\\
\Phi_{1}(u,v)&=v^{-1}+u,\\
\Phi_{2}(u,v)&=uv^{-1}.
\end{aligned}
\]
For \(-2\le r\le s\le2\), put
\[
H_{r,s}(u,v)=\sum_{d=r}^{s}\Phi_d(u,v),
\]
and set \(H_{r,s}=0\) when \(r>s\). The Laurent polynomial for labelings whose pair differences have exact minimum \(m\) and exact maximum \(M\) is
\[
R_{m,M}=
\begin{cases}
\Phi_m^n,&m=M,\\
H_{m,M}^n-H_{m+1,M}^n-H_{m,M-1}^n+H_{m+1,M-1}^n,&m<M.
\end{cases}
\]
For a Laurent polynomial \(P=\sum_{a,b}c_{a,b}u^a v^b\), define
\[
\mathcal T_{r,s}P=\sum_{a\ge r,\ b\ge s}c_{a,b}u^a v^b.
\]
Then the complete bivariate side-sum enumerator of minus dominating functions is
\[
F_n(u,v)=\sum_{-2\le m\le M\le2}\mathcal T_{1+M,\,1-m}R_{m,M}(u,v).
\]
The ordinary weight enumerator is therefore
\[
W_n(t)=F_n(t,t).
\]

Moreover,
\[
\gamma^-(\operatorname{Cr}_n)=2.
\]
Every minimum-weight function is exactly a matched-pair-diagonal labeling
\[
f(a_i)=f(b_i)=z_i\in\{-1,0,1\},\qquad \sum_{i=1}^n z_i=1.
\]
Thus the number of minimum functions is
\[
N_n=\sum_{j=0}^{\lfloor(n-1)/2\rfloor}\frac{n!}{(j+1)!\,j!\,(n-2j-1)!}.
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. The result uses the standard closed-neighborhood definition of minus domination with labels in \(\{-1,0,1\}\). The theorem is stated for \(n\ge3\); the graph \(\operatorname{Cr}_2\) has a different minimum-function boundary behavior and is intentionally excluded.

The scalar lower bound \(\gamma^-(\operatorname{Cr}_n)\ge2\) is already implied by the classical regular-graph bound because \(\operatorname{Cr}_n\) is \((n-1)\)-regular of order \(2n\). The originality-bearing content is the exact all-function criterion, the complete bivariate and weight enumerators, and the classification and count of every minimum function.

## Proof
For every \(i\), the closed neighborhood of \(a_i\) contains \(a_i\) and all vertices of \(B_0\) except \(b_i\). Hence
\[
f(N[a_i])=x_i+\sum_{j\ne i}y_j=B+x_i-y_i.
\]
Similarly,
\[
f(N[b_i])=y_i+\sum_{j\ne i}x_j=A-(x_i-y_i).
\]
Therefore all inequalities \(f(N[a_i])\ge1\) hold exactly when
\[
B+\min_i(x_i-y_i)\ge1,
\]
and all inequalities \(f(N[b_i])\ge1\) hold exactly when
\[
A-\max_i(x_i-y_i)\ge1.
\]
This proves the criterion.

For the enumerator, each matched pair \((a_i,b_i)\) contributes one of nine label pairs. Grouping those nine states by the difference \(d=x_i-y_i\in\{-2,-1,0,1,2\}\) gives exactly the five polynomials \(\Phi_d\). Thus \(H_{r,s}^n\) enumerates all labelings whose pair differences lie in \([r,s]\). Inclusion-exclusion on the two boundary values gives \(R_{m,M}\), which enumerates exactly those labelings with minimum difference \(m\) and maximum difference \(M\). For fixed \((m,M)\), the proved criterion retains precisely the monomials with \(A\ge1+M\) and \(B\ge1-m\), which is the truncation \(\mathcal T_{1+M,1-m}\). Summing over the fifteen possible ordered ranges \((m,M)\) proves the formula for \(F_n\). Substituting \(u=v=t\) records total weight \(A+B\) and gives \(W_n\).

Finally, every minus dominating function satisfies
\[
A+B\ge(1+M)+(1-m)=2+(M-m)\ge2.
\]
Conversely, choose any \(z_1,\ldots,z_n\in\{-1,0,1\}\) with \(\sum_i z_i=1\), and set \(x_i=y_i=z_i\). Then \(m=M=0\) and \(A=B=1\), so the function is minus dominating with weight \(2\). Hence \(\gamma^-(\operatorname{Cr}_n)=2\).

Suppose now that a feasible function has weight \(2\). Equality in the previous bound forces \(M=m=d\), so every difference \(x_i-y_i\) equals the same integer \(d\). The two feasibility inequalities must also be equalities, giving \(A=1+d\) and \(B=1-d\). Therefore
\[
A-B=2d=\sum_{i=1}^n(x_i-y_i)=nd.
\]
Because \(n\ge3\), this forces \(d=0\). Hence \(x_i=y_i\) for every \(i\) and \(A=B=1\). If exactly \(j\) of the common pair labels equal \(-1\), then exactly \(j+1\) equal \(+1\) and the remaining \(n-2j-1\) equal \(0\), giving the displayed multinomial sum.

## Verification
A standalone exhaustive checker reconstructs \(\operatorname{Cr}_n\) directly, enumerates every labeling in \(\{-1,0,1\}^{2n}\) for \(3\le n\le6\), and compares the graph-definition predicate with the two-inequality criterion. It independently constructs the fifteen exact-range Laurent polynomials and compares every bivariate coefficient and every total-weight coefficient with exhaustive enumeration. It also checks the minimum weight and the diagonal minimum-function count.

The replay result is:

`VERIFY_OK n_range=3..6 labelings=597780 valid_functions=28559 criterion_checks=597780 bivariate_coefficients=94 weight_coefficients=32 minimum_checks=4 max_order=12`

The finite computation is a verification of small cases and of the implementation of the formulas; the proof above establishes the theorem for every \(n\ge3\).

## Relationship to prior work
Dunbar, Hedetniemi, Henning, and McRae studied minus domination in regular graphs and proved a sharp regular-graph lower bound. Applied to the \((n-1)\)-regular graph \(\operatorname{Cr}_n\) of order \(2n\), that bound gives the scalar lower bound \(2\). Their later general paper develops the standard minus-domination framework.

Zelinka determined the signed and minus domination numbers of complete bipartite graphs \(K_{p,q}\); in particular, the complete-bipartite minimum is scalar information rather than an all-function census. Liang subsequently determined exact scalar signed, signed-total, and minus domination numbers for complete multipartite graphs and records primary classification MSC 05C69. For part sizes at least two, the complete-multipartite minus domination number is \(2\).

For \(n\ge3\), a crown graph is not complete multipartite: the deleted perfect matching makes each vertex miss one vertex on the opposite side. The exact neighborhood sums therefore depend on the matched-pair differences \(x_i-y_i\), and the complete-bipartite or complete-multipartite scalar results do not imply the criterion, Laurent enumerator, or minimum-function classification above. Literature searches using the standard name, crown-graph terminology, and the equivalent description \(K_{n,n}\) minus a perfect matching did not locate an equivalent all-function formula.

## Limitations
No claim is made that the phrase “minus-domination weight enumerator” is standardized terminology; \(W_n\) is defined explicitly here. The literature comparison cannot rule out an older or poorly indexed equivalent census under different terminology. The excluded boundary \(n=2\) has extra minimum functions and is not covered by the classification. The exhaustive computation reaches \(n=6\); it supports implementation correctness but is not used as an infinite proof.

## References
1. J. E. Dunbar, S. T. Hedetniemi, M. A. Henning, and A. A. McRae, “Minus domination in regular graphs,” *Discrete Mathematics* 149 (1996), 311–312. DOI: 10.1016/0012-365X(94)00329-H.
2. J. Dunbar, S. Hedetniemi, M. A. Henning, and A. McRae, “Minus domination in graphs,” *Discrete Mathematics* 199 (1999), 35–47. DOI: 10.1016/S0012-365X(98)00284-2.
3. B. Zelinka, “Signed and minus domination in bipartite graphs,” *Czechoslovak Mathematical Journal* 56 (2006), 587–590. DML-CZ: 128088.
4. H. Liang, “Signed and Minus Domination in Complete Multipartite Graphs,” arXiv:1205.0343v1, 2 May 2012.
