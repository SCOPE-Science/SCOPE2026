# Maximal abelian-subalgebra loci of cycle graphical Lie algebras: points versus a nodal polygon

## Finding

Let \(n\ge4\), let \(k\) be any field, and let \(L_n(k)\) be the two-step graphical Lie algebra of the simple cycle \(C_n\). Its basis is \(v_1,\ldots,v_n,z_1,\ldots,z_n\) with \([v_i,v_{i+1}]=z_i\) for indices modulo \(n\), all \(z_i\) central, and all other vertex brackets zero. Put \(a=\lfloor n/2\rfloor\). Every abelian Lie subalgebra has dimension at most \(n+a\), and equality occurs.

Let \(X_n\) denote the **reduced** closed subvariety of \(\operatorname{Gr}(n+a,L_n)\) whose geometric points are the abelian Lie subalgebras of dimension \(n+a\). The following classification is valid over every base field, including characteristic two:

* If \(n=2a\), \(X_n\) consists of exactly two reduced \(k\)-rational points, from the two alternating independent vertex sets.
* If \(n=2a+1\), \(X_n\) is a connected cycle of \(n\) projective lines \(P_i\cong\mathbb P^1_k\), with pairwise ordinary nodes, and \(P_i\cap P_j\ne\varnothing\) precisely for \(j\equiv i\pm2\pmod n\). Each such intersection is one \(k\)-rational point. The dual intersection graph is an \(n\)-cycle. In particular, this reduced curve has arithmetic genus one.

For every prime power \(q\), the number of maximum-dimensional abelian Lie subalgebras of \(L_n(\mathbb F_q)\) is therefore exactly
\[
\boxed{\#X_n(\mathbb F_q)=\begin{cases}2,&n\text{ even},\\nq,&n\text{ odd}.\end{cases}}
\]

For odd \(n=2a+1\), the complete parameterization is
\[
P_i:\quad [s:t]\longmapsto Z+\operatorname{span}\bigl(sv_i+tv_{i+1},v_{i+3},v_{i+5},\ldots,v_{i+2a-1}\bigr),
\]
where \(Z=\operatorname{span}(z_1,\ldots,z_n)\); all indices are modulo \(n\). In the even case the two subalgebras are \(Z+\langle v_1,v_3,\ldots,v_{n-1}\rangle\) and \(Z+\langle v_2,v_4,\ldots,v_n\rangle\).

## Assumptions and scope

The bracket is alternating and bilinear in every characteristic; when the characteristic is two, the reversed-edge bracket agrees with the forward bracket. All statements about varieties are statements about the **underlying reduced closed locus**, not the potentially nonreduced equations for the unreduced commuting-subalgebra scheme. The classification holds after extension of scalars to an algebraic closure, and all indicated components and nodes are defined over \(k\).

Maximum-dimensional means largest possible \(k\)-linear dimension among **abelian** Lie subalgebras; it is not the different notion of being maximal merely under inclusion. Every such largest subalgebra includes \(Z\), so there is a canonical reduction of its parameter space to a Grassmannian in the vertex quotient.

## Proof

**Step 1: center and dimension.** The center is precisely \(Z\): for a nonzero vertex combination \(x=\sum_i a_i v_i\), an index with \(a_i\ne0\) gives a nonzero \(z_i\) or \(z_{i-1}\) coefficient in some bracket \([x,v_j]\). If \(H\) is abelian, then \(H+Z\) is abelian; hence any abelian subalgebra of maximal possible dimension must contain \(Z\). Such subalgebras are exactly \(Z+U\), where \(U\le V=\operatorname{span}(v_1,\ldots,v_n)\) is a totally commuting subspace.

**Step 2: the support lemma.** Fix a commuting subspace \(U\le V\) of dimension \(d\ge2\). Define linear coordinate functionals \(\phi_i:U\longrightarrow k\) by \(\phi_i(u)=[v_i]u\) (coefficient of \(v_i\)). The coefficient of \(z_i\) in \([u,w]\) equals
\[
\phi_i(u)\phi_{i+1}(w)-\phi_{i+1}(u)\phi_i(w).
\]
Since the edge central basis vectors are independent, \(U\) is commuting if and only if adjacent functionals have zero exterior product. Over any field, two nonzero functionals with zero exterior product are proportional. Let \(S=\{i:\phi_i\ne0\}\). Since \(d\ge2\), \(S\ne\{1,\ldots,n\}\); otherwise adjacent proportionality around the full cycle would imply \(\dim U^*\le1\). Decompose \(S\) into its \(c(S)\) nonempty cyclic runs of consecutive vertices. Each run contributes at most one dimension to the span of all \(\phi_i\), whereas the full set of coordinate functionals spans \(U^*\). Thus
\[
d\le c(S)\le\lfloor n/2\rfloor=a.
\]
The last inequality holds because each nonempty supported run must be separated from the next by at least one omitted vertex. Alternating independent vertex subsets of size \(a\) give commuting spaces attaining the bound. Therefore the largest abelian-subalgebra dimension is \(n+a\).

**Step 3: equality rigidifies cyclic support.** Suppose \(d=a\). Equality forces \(c(S)=a\), and exactly one nonzero functional direction comes from each supported run. Since these \(a\) directions span the \(a\)-dimensional dual of \(U\), they are linearly independent. In particular, \(U\) is the direct sum of its one-dimensional coordinate contributions on the runs, with each run supporting one vector. Thus it is enough to classify the cyclic binary support pattern \(S\) with exactly \(a\) supported runs.

If \(n=2a\), there are \(a\) supported and \(a\) omitted vertices, necessarily alternating. Both possibilities give the two coordinate planes. If \(n=2a+1\), there are \(a\) supported runs and \(a\) omitted runs. Their lengths are all positive and sum to \(2a+1\); hence exactly one among the \(2a\) runs has length two and all others length one. If the double run is supported, it is a unique adjacent pair \(\{i,i+1\}\), and its proportional functional direction gives the projective parameter \([s:t]\), with the remaining singleton supported vertices \(i+3,i+5,\ldots,i+2a-1\). If the double run is omitted, \(U\) is a coordinate plane associated to a maximum independent vertex set; it is one of the endpoints of two of the preceding projective families.

**Step 4: geometry and incidence.** Fix an odd \(n\). Each family \(P_i\) varies exactly one line in the fixed two-dimensional coordinate plane \(\langle v_i,v_{i+1}\rangle\), with fixed complementary \((a-1)\)-plane, so it is a projective line under the Grassmannian's Plücker embedding. Its general point has support with a double supported run, uniquely identifying \(i\); thus the \(n\) projective lines are distinct components, and the support classification proves that their union contains every geometric point of \(X_n\). Passing to reduced loci gives equality as reduced varieties.

Its two coordinate endpoints are obtained by \([s:t]=[1:0]\) and \([0:1]\). They are, respectively, shared with \(P_{i+2}\) and \(P_{i-2}\) (up to swapping the two choices), and no other intersections occur: any common point must be a coordinate plane, and every maximum independent set on an odd cycle admits exactly two adjacent-pair thickenings. Because \(n\) is odd, the graph on indices with edges of step two is a single \(n\)-cycle. At any intersection, the two distinct Plücker lines have different tangent directions, so the reduced union has an ordinary transverse node. The normalization consists of \(n\) copies of \(\mathbb P^1\) and the number of nodes is \(n\); hence its arithmetic genus is \(1+n-n=1\). In the even case the two points are defined over \(k\) and are reduced by definition.

**Step 5: arithmetic count.** Every component \(P_i\) has \(q+1\) rational points; there are exactly \(n\) rational nodes, each lying on exactly two lines, with no triple overlaps. Inclusion-exclusion therefore gives \(n(q+1)-n=nq\). The even case has two rational points. All these deductions are invariant under field extension.

## Verification

The accompanying Python program `verify.py` enumerates **all** reduced row-echelon matrices representing \(a\)-planes in \(\mathbb F_q^n\), using direct arithmetic over prime fields. It independently tests each of the \(n\) adjacent-coordinate minors for every pair of basis rows. It checks the formulas for
\[
(n,q)=(4,2),(4,3),(4,5),(5,2),(5,3),(5,5),(6,2),(6,3),(7,2).
\]
The respective computed counts are \(2,2,2,10,15,25,2,2,14\), exactly the predicted values. The verifier terminates with `VERIFY_OK_CYCLE_MAXIMAL_ABELIAN`. These finite checks are **not** an exhaustive proof of all dimensions and fields; that is supplied by the support argument above.

## Relationship to prior work

Mainkar's paper gives the graph-to-two-step-Lie-algebra construction and establishes its isomorphism-theoretic significance. Aldi–Gabrielsen–Grandini–Harris–Kelley establish general independence-number bounds on maximal abelian-subalgebra dimension; our dimension bound is an instance of their setting and is not claimed to be new. The present new candidate invariant is the complete **geometry of the equality locus** for the cycle family: a parity change from two isolated points to a reduced nodal polygon, together with its exact rational-point count.

Rossmann's graphical-group class enumerator computes elementwise centralizer ranks, not the simultaneous-commutation condition on maximal-dimensional **linear subspaces**. The previously reported cycle graphical-group character-degree polynomial similarly counts skew adjacency specializations, and does not imply the present Grassmannian decomposition. Aguirre–Felder–Veselov study maximal-dimensional abelian subalgebra varieties of a different Lie algebra (the Kohno–Drinfeld algebra), establishing the naturality of such geometric parameter spaces but not this classification.

Searches for the cycle graph Lie algebra, abelian subalgebra Grassmannian, projective-line parameter components, parity, and exact finite-field counts did not identify the present theorem. No claim of exhaustive bibliographic uniqueness is made; combinatorial classification of maximum-rank isotropic graph-subspaces under other terminology is a residual risk.

## Limitations

Only **maximum-dimensional** abelian Lie subalgebras are classified. The reduced locus is determined, not nilpotent scheme structure or multiplicities in the unreduced zero scheme; other dimensions and maximal-under-inclusion subalgebras are not classified. Exact rational-point counts assume a finite field but the geometric classification holds for any field. The algebra is attached to a simple cycle with independent central edge labels; other graphs or edge identifications require new arguments. Independent mathematical validation has not been performed.

## References

1. M. G. Mainkar, “Graphs and and two-step nilpotent Lie algebras,” arXiv:1310.3414v1, first public 12 October 2013; *Groups, Geometry, and Dynamics* 9 (2015), 55–65, DOI 10.4171/GGD/305.
2. M. Aldi, T. Gabrielsen, D. Grandini, J. Harris, K. Kelley, “Independence Polynomials of 2-step Nilpotent Lie Algebras,” arXiv:2504.19836v1, first public 28 April 2025. See its abelian-subalgebra dimension bounds.
3. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, first public 12 July 2021; *Bulletin of the London Mathematical Society* 54 (2022), 1830–1846.
4. L. Aguirre, G. Felder, A. P. Veselov, “Gaudin subalgebras and stable rational curves,” arXiv:1004.3253v1, first public 19 April 2010.
5. “Cycle graphical groups have an explicit character-degree enumerator,” published mathematical research result, 4 October 2026, identifier `SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e`; see the publicly available full result for the different character-degree problem.
