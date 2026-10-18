# Optimal interaction projections on weighted Hamming rectangles

## Finding
Let \(A\) and \(B\) be finite sets of cardinalities \(m,n\geq2\), and equip \(M=A\times B\) with the metric
\[
d((a,b),(a',b'))=\alpha\,\mathbf 1_{a\ne a'}+\beta\,\mathbf 1_{b\ne b'},\qquad \alpha,\beta>0.
\]
Identify the real Lipschitz-free space \(\mathcal F(M)\) with real signed arrays \(\mu=(\mu_{ab})\) satisfying \(\sum_{a,b}\mu_{ab}=0\), equipped with the transportation-cost norm. Let
\[
U=\left\{\mu:\ \sum_{b\in B}\mu_{ab}=0\ (a\in A),\quad
\sum_{a\in A}\mu_{ab}=0\ (b\in B)\right\}.
\]
Then \(\dim U=(m-1)(n-1)\), and the least operator norm of a linear projection of \(\mathcal F(M)\) onto \(U\) is exactly
\[
\boxed{\lambda(U,\mathcal F(M))=
2\min\{\alpha,\beta\}\max\!\left\{\frac{n-1}{n\alpha},\frac{m-1}{m\beta}\right\}.}
\]
The double-centering projection attains this minimum. In particular, \(U\) is the range of a norm-one projection precisely in the following mutually exclusive cases:
\[
\begin{array}{ll}
 m=n=2;&\\
 m=2,\ n>2,\ \alpha\geq 2(n-1)\beta/n;&\\
 n=2,\ m>2,\ \beta\geq 2(m-1)\alpha/m.&
\end{array}
\]
When \(m,n\geq3\), \(U\) is never contractively complemented, whatever the positive weights.

## Assumptions and scope
Only finite sets, real scalars, and positive coordinate distances are assumed. All maps called projections are linear idempotents onto the specified subspace; no permutation-equivariance hypothesis is imposed. The transportation norm is determined by the duality
\[
\|\mu\|_{\mathcal F(M)}=
\sup\left\{\left|\sum_{a,b}\mu_{ab}f(a,b)\right|:\operatorname{Lip}(f)\leq1\right\}.
\]
The additive constant of \(f\) is immaterial because \(\sum_{a,b}\mu_{ab}=0\). The Lipschitz seminorm on this weighted Cartesian product is the maximum of normalized differences along edges that change just one coordinate.

## Proof
**1. A canonical projection.** For any zero-total array \(\mu\), define
\[
(R\mu)_{ab}=\mu_{ab}-\frac1n\sum_{b'\in B}\mu_{ab'}-
\frac1m\sum_{a'\in A}\mu_{a'b}.
\]
The zero-total assumption makes every row sum and every column sum of \(R\mu\) equal to zero. On \(U\), the formula is the identity, hence \(R^2=R\) and \(\operatorname{ran}R=U\). Every zero-total array decomposes uniquely as the sum of one array in \(U\), an array of the form \(u_a/n\) with \(\sum_a u_a=0\), and an array of the form \(v_b/m\) with \(\sum_b v_b=0\).

**2. Global optimality, not just symmetric optimality.** The finite group \(G=S_A\times S_B\) acts on signed arrays by coordinate permutations and preserves both the metric and \(U\). Given any projection \(P\) onto \(U\), average \(g^{-1}Pg\) over \(g\in G\). This gives a \(G\)-equivariant projection \(\overline P\) onto \(U\) with \(\|\overline P\|\leq\|P\|\). For an array of the form \(u_a/n\), permutations of \(B\) act trivially. Its image under \(\overline P\) is consequently a \(B\)-permutation-invariant member of \(U\), and must vanish: a matrix constant along every row has zero row sum only if it is zero. The analogous argument eliminates arrays of the form \(v_b/m\). Because \(\overline P\) fixes \(U\), the decomposition from Step 1 implies \(\overline P=R\). Thus \(\|R\|\leq\|P\|\) for every projection \(P\) onto \(U\).

**3. Exact upper norm bound.** Under the transportation/Lipschitz duality the adjoint of \(R\), modulo constants, is the double-centering map
\[
(Qf)(a,b)=f(a,b)-\frac1n\sum_{b'}f(a,b')-
\frac1m\sum_{a'}f(a',b)+\frac1{mn}\sum_{a',b'}f(a',b').
\]
Consequently \(\|R\|=\|Q\|\). Suppose \(\operatorname{Lip}(f)\leq1\). For fixed distinct \(a,a'\), put \(g(b)=f(a,b)-f(a',b)\). Then \(|g(b)|\leq\alpha\) and \(|g(b)-g(b')|\leq2\beta\), so also \(|g(b)-g(b')|\leq2\min\{\alpha,\beta\}\). It follows that
\[
\frac{|(Qf)(a,b)-(Qf)(a',b)|}{\alpha}
=\frac{|g(b)-n^{-1}\sum_{b'}g(b')|}{\alpha}
\leq \frac{2(n-1)\min\{\alpha,\beta\}}{n\alpha}.
\]
Exchanging the two coordinates yields the bound \(2(m-1)\min\{\alpha,\beta\}/(m\beta)\) on every edge changing the \(B\)-coordinate. All pairwise Lipschitz quotients are dominated by the maximum of the edge quotients, giving the claimed upper bound.

**4. Attainment.** Set \(t=\min\{\alpha,\beta\}\). Choose two distinct rows \(a_0,a_1\) and one column \(b_0\), and define \(g(b_0)=\alpha\), \(g(b)=\alpha-2t\) for \(b\ne b_0\). Put \(f(a_0,b)=g(b)/2\), \(f(a_1,b)=-g(b)/2\), and \(f(a,b)=0\) on any remaining rows. Since \(|g(b)|\leq\alpha\) and \(|g(b)-g(b')|\leq2\beta\), every normalized coordinate-edge difference of \(f\) is at most one. The edge joining \((a_0,b_0)\) and \((a_1,b_0)\) has difference exactly \(\alpha\), so \(\operatorname{Lip}(f)=1\). But the corresponding normalized difference of \(Qf\) is exactly \(2(n-1)t/(n\alpha)\). Interchanging rows and columns constructs a second unit-Lipschitz function reaching \(2(m-1)t/(m\beta)\). Thus both competing upper bounds are sharp, and \(\|Q\|\) is their maximum.

**5. Contractive threshold.** If \(\alpha\leq\beta\), the first term is \(2(n-1)/n\); if \(\beta\leq\alpha\), the second is \(2(m-1)/m\). Hence \(m,n\geq3\) always forces norm greater than one. If \(m=2<n\), the second term is one whenever \(\alpha\geq\beta\), and the first is at most one exactly when \(\alpha\geq2(n-1)\beta/n\). The case \(n=2<m\) is symmetric. For \(m=n=2\), one of the two competing terms equals one and the other is at most one. These are all cases.

## Verification
The standalone script `CHECK.py` constructs the actual double-centering matrix, verifies that it is an idempotent with zero row and column marginals, and independently evaluates its transportation-norm operator norm by linear programming over all normalized edges. It checks \(144\) parameter combinations with \(2\leq m,n\leq5\) and \(\alpha,\beta\in\{1,2,3\}\), comparing the independent optimization with the closed formula. To reproduce, install the dependencies in `requirements.txt` and run `python CHECK.py`. Finite optimization is a diagnostic, not a proof of the quantified theorem; Steps 1–5 above are the proof.

For illustration, when \(m=2,n=3\) and \(\alpha=\beta=1\), the optimal projection norm is \(4/3\); increasing \(\alpha\) to \(2\) while retaining \(\beta=1\) makes the interaction projection contractive. For \(m=n=3\) with equal weights the constant is \(4/3\).

## Relationship to prior work
Cúth and Doucha (2021, arXiv:2104.11519v1) develop norm-one projections onto subspaces invariant under group actions and general averaging principles. Here the target is instead the *interaction subspace*, simultaneously annihilated by both coordinate marginal maps; for most parameters its optimal projection norm is strictly above one. The finite-group averaging argument is classical, and no priority is claimed for that method. Ostrovska and Ostrovskii (2021, arXiv:2112.02689v1) study the representation and isometric structure of finite transportation-cost spaces, but their roadmap and graph-embedding results do not give the interaction projection constant. Dilworth, Kutzarova, and Ostrovskii (2018, arXiv:1807.03814v1) also use symmetry averaging for different graph-cycle subspaces. The exact weighted rectangular formula and its complementability threshold are the contribution asserted here.

## Limitations
The theorem is for real Lipschitz-free spaces of **two-factor products of equilateral finite sets** with the \(\ell_1\)-product metric. It does not determine optimal projections for general non-equilateral factor metrics, arbitrary higher-factor interactions, or other transportation costs. A complete independent literature audit is not claimed; an equivalent result under matrix-centering or transport terminology may exist outside the sources compared. No numerical experiment substitutes for the proof.

## References
1. Marek Cúth and Michal Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519v1, first public 23 April 2021, https://arxiv.org/html/2104.11519v1 (notably Lemma 3.2, Theorem 4.5, and Corollary 4.6).
2. Sofiya Ostrovska and Mikhail I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689v1, first public 5 December 2021, https://arxiv.org/html/2112.02689v1 (Proposition 1.5 and Sections 1.1, 3).
3. Stephen J. Dilworth, Denka Kutzarova, and Mikhail I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, first public 10 July 2018, https://arxiv.org/html/1807.03814v1 (Sections 1.1 and 4.4–4.7).
