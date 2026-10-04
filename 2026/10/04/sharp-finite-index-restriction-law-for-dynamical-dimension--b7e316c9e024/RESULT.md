# Sharp finite-index restriction law for dynamical dimension
## Finding
Let \(\Gamma\) be a countable group, let \(T:\Gamma\to\operatorname{Homeo}(X)\) be an action on a compact metric space \(X\), and let \(H\leq\Gamma\) have finite index \(m=[\Gamma:H]\). For Meyerovitch's dynamical dimension,
\[
\dim(X,T)\leq \dim(X,T|_H)\leq m\,\dim(X,T).
\]
If \(\operatorname{Prob}(X,T|_H)=\varnothing\), then also \(\operatorname{Prob}(X,T)=\varnothing\), and conversely an \(H\)-invariant probability measure can be averaged over cosets to produce a \(\Gamma\)-invariant one. Thus the empty-measure case gives \(\dim(X,T)=\dim(X,T|_H)=-\infty\) under the convention in the source.

The coefficient \(m\) is sharp for every \(m\geq2\). Take \(X=[0,1]^d\times\mathbb Z/m\mathbb Z\) with \(d\geq1\), let \(\Gamma=\mathbb Z\) act by cyclic translation on the second coordinate, and set \(H=m\mathbb Z\). Every \(\Gamma\)-orbit has exactly \(m\) points, so Meyerovitch's finite-orbit formula gives \(\dim(X,T)=d/m\), while \(H\) acts trivially and hence \(\dim(X,T|_H)=d\). Consequently the upper factor cannot be improved. The lower coefficient \(1\) is also sharp, for example for trivial actions.

For a homeomorphism \(F:X\to X\) and any integer \(q\geq1\), applying the theorem to \(\Gamma=\mathbb Z\) and \(H=q\mathbb Z\) gives
\[
\dim(X,F)\leq\dim(X,F^q)\leq q\,\dim(X,F),
\]
with sharp upper coefficient.

## Assumptions and scope
Meyerovitch associates to a \(\Gamma\)-action the topological-measure pair \( (X,\operatorname{Prob}(X,T))\) and defines the dimension through finite open covers and the averaged pointwise cover order. For a finite open cover \(\mathcal V\), write
\[
\operatorname{ord}(\mathcal V,x)=-1+\sum_{V\in\mathcal V}\mathbf 1_V(x),
\]
and for a nonempty closed convex set \(P\subseteq\operatorname{Prob}(X)\), write
\[
\operatorname{ord}(\mathcal V,P)=\sup_{\mu\in P}\int_X\operatorname{ord}(\mathcal V,x)\,d\mu(x).
\]
The dimension is obtained by taking the infimum over refinements and then the supremum over starting covers. The proof uses only this definition, finite-index averaging, and Meyerovitch's Lemma 2.4 on subadditivity of pointwise cover order under joint refinements. No amenability of \(\Gamma\) is assumed.

## Proof
Put \(P_\Gamma=\operatorname{Prob}(X,T)\) and \(P_H=\operatorname{Prob}(X,T|_H)\). Since every \(\Gamma\)-invariant measure is \(H\)-invariant, \(P_\Gamma\subseteq P_H\). Therefore for every finite open cover \(\mathcal V\),
\[
\operatorname{ord}(\mathcal V,P_\Gamma)\leq\operatorname{ord}(\mathcal V,P_H),
\]
and taking the infimum over refinements and the supremum over initial covers gives
\[
\dim(X,T)\leq\dim(X,T|_H).
\]

For the reverse inequality up to the index, first note that \(P_H\neq\varnothing\) implies \(P_\Gamma\neq\varnothing\). Choose representatives \(R=\{r_1,\ldots,r_m\}\) for the left cosets \(\Gamma/H\). If \(\mu\in P_H\), define
\[
\overline\mu=\frac1m\sum_{r\in R}(T_r)_*\mu.
\]
Left multiplication by any \(g\in\Gamma\) permutes the cosets. If \(gr=r'h\) with \(r'\in R\) and \(h\in H\), then
\[
(T_g)_*(T_r)_*\mu=(T_{r'h})_*\mu=(T_{r'})_*(T_h)_*\mu=(T_{r'})_*\mu.
\]
Hence \(\overline\mu\in P_\Gamma\). This also proves simultaneous nonemptiness of \(P_H\) and \(P_\Gamma\).

Assume now that \(D=\dim(X,T)<\infty\); the case \(D=+\infty\) is immediate. Fix a finite open cover \(\mathcal U\) and \(\varepsilon>0\). Form the joint refinement
\[
\mathcal U^*=\bigvee_{r\in R}T_r\mathcal U.
\]
By the definition of \(D\), there is a finite open cover \(\mathcal W\) refining \(\mathcal U^*\) such that
\[
\operatorname{ord}(\mathcal W,P_\Gamma)<D+\varepsilon.
\]
For each \(r\in R\), let \(\mathcal W_r=T_{r^{-1}}\mathcal W\). Because \(\mathcal W\) refines \(T_r\mathcal U\), the transformed cover \(\mathcal W_r\) refines \(\mathcal U\).

Iterating Meyerovitch's Lemma 2.4 over the finite family \(\{\mathcal W_r:r\in R\}\), obtain an open cover \(\mathcal V\) refining their joint refinement, and hence refining \(\mathcal U\), with
\[
\operatorname{ord}(\mathcal V,x)\leq\sum_{r\in R}\operatorname{ord}(\mathcal W_r,x)
\]
for every \(x\in X\). For \(\mu\in P_H\), the change of variables for push-forward measures gives
\[
\begin{aligned}
\int_X\operatorname{ord}(\mathcal V,x)\,d\mu(x)
&\leq\sum_{r\in R}\int_X\operatorname{ord}(\mathcal W,T_r x)\,d\mu(x)\\
&=\sum_{r\in R}\int_X\operatorname{ord}(\mathcal W,y)\,d((T_r)_*\mu)(y)\\
&=m\int_X\operatorname{ord}(\mathcal W,y)\,d\overline\mu(y)\\
&\leq m\,\operatorname{ord}(\mathcal W,P_\Gamma)\\
&<m(D+\varepsilon).
\end{aligned}
\]
Taking the supremum over \(\mu\in P_H\) shows \(\operatorname{ord}(\mathcal V,P_H)<m(D+\varepsilon)\). Since \(\mathcal V\) refines the arbitrary starting cover \(\mathcal U\),
\[
\dim(\mathcal U,P_H)\leq m(D+\varepsilon).
\]
Now let \(\varepsilon\downarrow0\) and take the supremum over \(\mathcal U\) to obtain
\[
\dim(X,T|_H)\leq m\,D.
\]
This completes the proof.

## Verification
The argument was checked against the source definition of \(\dim(X,T)\), the convention \(\dim(X,\varnothing)=-\infty\), and Lemma 2.4. The finite-index averaging identity was checked for arbitrary, not necessarily normal, subgroups by using left-coset representatives. The transformed-cover identity
\[
\operatorname{ord}(T_{r^{-1}}\mathcal W,x)=\operatorname{ord}(\mathcal W,T_r x)
\]
is exact, so the measure integral becomes the coset average without an inequality loss. Edge cases \(m=1\), \(D=+\infty\), and empty invariant-measure simplices are explicitly covered.

For sharpness, the cyclic-layer system has exactly \(m\)-point orbits and covering dimension \(d\); Meyerovitch states that a system all of whose orbits have size \(m\) has dynamical dimension \(d/m\). The restricted \(m\mathbb Z\)-action is trivial, for which the same source identifies dynamical dimension with covering dimension.

## Relationship to prior work
Meyerovitch introduced the invariant in arXiv:2601.13161. The paper explicitly records a finite-index subgroup lower bound involving the dimension of a fixed-point set, but the inspected full text does not state a comparison between the dynamical dimensions of an action and its restriction to a finite-index subgroup. The proof above combines the source's cover-order subadditivity with a coset-average of subgroup-invariant measures. Section 7 of the same paper supplies the exact finite-orbit formula used to show sharpness.

Two later 2026 papers of Ruxi Shi use Meyerovitch's invariant for shift embeddability and compute it in specific systems. Their available abstracts concern inverse-limit/full-shift computations and sharp embedding thresholds; no finite-index restriction or power law is stated there. Full-text comparison of those two later papers was not completed, so this remains a literature risk rather than evidence of absence.

## Limitations
The theorem concerns Meyerovitch's dynamical dimension, not mean dimension or other dimension invariants. It compares an action only with restriction to a finite-index subgroup; no claim is made for infinite-index subgroups. The sharpness example uses a finite-orbit cyclic action and establishes optimality of the universal coefficient, not uniqueness of equality cases. The originality assessment is literature-search based and cannot prove global uniqueness; two highly relevant later preprints were checked only at the abstract level.

## References
1. Tom Meyerovitch, “A new notion of dimension for dynamical systems and shift embeddability,” arXiv:2601.13161, first submitted 2026-01-19; Geometric and Functional Analysis 36 (2026), 947–980. Relevant items: definition of dynamical dimension, Lemma 2.4, Introduction item 5, and Section 7.
2. Ruxi Shi, “Dynamical dimension and shift embeddability without the marker property,” arXiv:2607.27880, first submitted 2026-07-30.
3. Ruxi Shi, “A sharp embedding theorem for topological dynamical systems,” arXiv:2609.05664, first submitted 2026-09-04.
