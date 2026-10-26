# Strong complements invalidate the stated consumer-choice microfoundation
## Finding
For the unconstrained quadratic quasi-linear consumer problem implicit in the differentiated inverse-demand first-order conditions of Matsumoto and Szidarovszky, write
\[
B=(1-\gamma)I+\gamma\mathbf1\mathbf1^\top.
\]
The paper explicitly analyzes the complement branch \(2+(n-1)\gamma<0\). On that branch, \(1+(n-1)\gamma<-1<0\), so the objective \(W(q;p)=\alpha^\top q-\tfrac12q^\top Bq-p^\top q\) is unbounded above along \(q=t\mathbf1\). The branch has no global consumer maximizer. Its equilibrium and stability formulas can still describe a formal best-response map if inverse demand is taken as primitive, but they are not equilibria of this unconstrained consumer-choice problem.

## Assumptions and scope
There are \(n\ge2\) differentiated goods, \(|\gamma|<1\), and inverse demand is \(p=\alpha-Bq\), with \(B\) having diagonal entries \(1\) and off-diagonal entries \(\gamma\). The unconstrained quasi-linear choice problem implicit in the inverse-demand first-order conditions has objective \(W(q;p)=\alpha^\top q-\tfrac12q^\top Bq-p^\top q\) over \(q\in\mathbb R_{\ge0}^n\), with no finite income cap on \(q\). The claim concerns global maximization in that problem and the interpretation of the paper’s strict branch \(2+(n-1)\gamma<0\), not the algebra of the best-response map treated as an exogenous model.

## Proof
Write \(\mathbf1=(1,\ldots,1)^\top\). Then
\[
B=(1-\gamma)I+\gamma\mathbf1\mathbf1^\top.
\]
For every vector orthogonal to \(\mathbf1\), the eigenvalue is \(1-\gamma\), with multiplicity \(n-1\). In the direction \(\mathbf1\), the eigenvalue is \(1+(n-1)\gamma\). Since \(|\gamma|<1\), the transverse eigenvalues are positive. Strict concavity of the consumer objective therefore requires \(1+(n-1)\gamma>0\), equivalently \(-1/(n-1)<\gamma<1\).

Now suppose \(2+(n-1)\gamma<0\). Then \(1+(n-1)\gamma<-1\). For \(q=t\mathbf1\), \(t\ge0\),
\[
W(t\mathbf1;p)=t\mathbf1^\top(\alpha-p)-\frac{n}{2}\bigl(1+(n-1)\gamma\bigr)t^2.
\]
The quadratic coefficient is strictly positive, so \(W(t\mathbf1;p)\to+\infty\) as \(t\to\infty\), for every finite price vector \(p\) and finite \(\alpha\). Thus no global consumer maximizer exists on this branch. The branch is possible under \(|\gamma|<1\) only for \(n\ge4\); for those parameters it lies wholly outside the strict-concavity domain. Conversely, inside the strict-concavity domain, \(2+(n-1)\gamma>1\), so the branch cannot occur.

## Verification
The included standard-library script uses exact rational arithmetic at \(n=4\), \(\gamma=-5/6\), a representative point in the disputed branch. It verifies \(1+(n-1)\gamma=-3/2\), \(2+(n-1)\gamma=-1/2\), and the positive quadratic growth coefficient along \(q=t\mathbf1\). It also checks that a sample parameter in the strict-concavity domain has positive eigenvalue in the \(\mathbf1\) direction and cannot satisfy the disputed branch inequality. These exact checks corroborate the symbolic proof; the proof, not a finite parameter sweep, establishes the result for all \(n\ge2\).

## Relationship to prior work
Matsumoto and Szidarovszky derive the inverse-demand system from a representative-consumer utility function and later explicitly analyze the case \(2+(n-1)\gamma<0\) in their complement discussion. Comparing the inequalities shows that this case forces the utility-curvature matrix to have a negative eigenvalue in the all-goods direction. The correction is a consistency restriction on the paper’s stated microfoundation, not a claim that its linear dynamic map has been algebraically miscomputed. The broader differentiated-oligopoly literature studies equilibrium and stability under regularity assumptions, but the accessible material reviewed here did not establish this specific incompatibility for the parameter branch in question.

## Limitations
This result does not invalidate the model’s formal best-response recurrence when the linear inverse-demand formula is adopted independently of the consumer optimization. The accessible derivation does not specify a finite income cap; if a budget or nonnegative-numeraire cap was intended, that different constrained problem requires separate analysis. The claim does not reassess results in the strict-concavity domain, the positive-substitute case, or unrelated price-adjustment regimes. The literature search cannot exclude an unindexed erratum or correspondence; no claim of exhaustive bibliographic uniqueness is made.

## References
1. A. Matsumoto and F. Szidarovszky, “Theocharis Problem Reconsidered in Differentiated Oligopoly,” *Economics Research International* (2014), Article 630351. First verified public repository date 2014-03-14; the discussion-paper issue date is 2014-02-01 and the journal version first published 2014-08-17. DOI: https://doi.org/10.1155/2014/630351. Full text: https://onlinelibrary.wiley.com/doi/full/10.1155/2014/630351.
2. A. Matsumoto and F. Szidarovszky, “Theocharis Problem Reconsidered in Differentiated Oligopoly,” Chuo University repository record 6099 (public date 2014-03-14; discussion-paper issue date 2014-02-01): https://chuo-u.repo.nii.ac.jp/records/6099.
3. X. Vives, “On the Efficiency of Bertrand and Cournot Equilibria with Product Differentiation,” *Journal of Economic Theory* 36 (1985), 166–175. DOI: https://doi.org/10.1016/0022-0531(85)90086-9. The accessible abstract was used only as contextual literature, not as evidence about the specific curvature calculation.
