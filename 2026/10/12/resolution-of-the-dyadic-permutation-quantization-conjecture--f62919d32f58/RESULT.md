# Resolution of the dyadic-permutation quantization conjecture
## Finding
Let \(k\ge2\). Let \(p_1,\ldots,p_{k-1}\) be any permutation of
\[
\{2^{-1},2^{-2},\ldots,2^{-(k-1)}\},
\]
and let \(P\) be the probability measure on the positive integers with
\[
P(\{j\})=p_j\quad(1\le j<k),
\qquad
P(\{j\})=2^{-j}\quad(j\ge k).
\]
For every \(n\ge k+2\), every optimal \(n\)-point quantizer for squared Euclidean distortion, written increasingly as \(a_1<\cdots<a_n\), satisfies
\[
a_j=j\qquad(1\le j\le n-3).
\]
This proves Conjecture 1.5 of Gomez--Martinez--Roychowdhury--Salazar--Vallez for every permutation allowed in their Definition 1.2. Their Theorem 1.3 therefore applies without an additional hypothesis: every optimal set has one of the two tail patterns stated there, and
\[
V_n=\frac{2^{3-n}}{3}\qquad(n\ge k+2).
\]

## Assumptions and scope
The distortion is
\[
V(P;\alpha)=\sum_{j\ge1}P(\{j\})\min_{a\in\alpha}(j-a)^2,
\]
and \(V_n\) is its minimum over sets with at most \(n\) representatives. All support masses are positive. We use standard one-dimensional optimal-quantizer facts: each representative has positive Voronoi mass, no support atom lies on a Voronoi boundary, each representative is the centroid of its cell, and cells meet the ordered support in consecutive blocks.

The result is specific to the dyadic multiset in Definition 1.2. It does not assert the same conclusion for arbitrary perturbations of the first \(k-1\) masses.

## Proof
Write \(w_j=P(\{j\})\). Consider the \(n\)-point competitor
\[
\beta=\{1,2,\ldots,n-2,\operatorname{Av}[n-1,n],\operatorname{Av}[n+1,\infty)\}.
\]
Because \(n\ge k+2\), every mass from \(n-1\) onward is geometric. The block \(\{n-1,n\}\) contributes
\[
\frac{2^{-(n-1)}2^{-n}}{2^{-(n-1)}+2^{-n}}=\frac{2^{1-n}}{3}.
\]
The tail \(\{n+1,n+2,\ldots\}\) has total mass \(2^{-n}\); after conditioning and subtracting \(n+1\), it is the geometric law \(P(G=t)=2^{-(t+1)}\) on \(t\ge0\), whose variance is \(2\). Thus the tail contributes \(2^{1-n}\), and
\[
V_n\le V(P;\beta)=\frac{2^{3-n}}{3}=:U_n.
\]

Suppose an optimal Voronoi cell contains adjacent support points \(r\) and \(r+1\). For any representative \(a\), the contribution of just these two atoms satisfies
\[
w_r(r-a)^2+w_{r+1}(r+1-a)^2\ge d_r:=\frac{w_rw_{r+1}}{w_r+w_{r+1}}.
\]
If \(r\le k-2\), the two weights are distinct members of the initial dyadic permutation. For distinct \(u,v\in\{1,\ldots,k-1\}\),
\[
\frac{2^{-u}2^{-v}}{2^{-u}+2^{-v}}=\frac1{2^u+2^v}\ge\frac{2^{2-k}}3>U_n.
\]
If \(r=k-1\), monotonicity of \(xy/(x+y)\) in both positive variables gives
\[
d_r\ge\frac{2^{-(k-1)}2^{-k}}{2^{-(k-1)}+2^{-k}}=\frac{2^{1-k}}3\ge U_n.
\]
If \(r\ge k\), then
\[
d_r=\frac{2^{-r}}3,
\]
so \(d_r\ge U_n\) whenever \(r\le n-3\).

The full distortion is strictly larger than the two-atom minimum \(d_r\). Indeed, the support is infinite while the quantizer set is finite, so some positive-mass support atom outside the selected pair is not itself a representative and contributes positive distortion. Therefore a cell containing adjacent \(r,r+1\) with \(r\le n-3\) would imply
\[
V_n>d_r\ge U_n,
\]
contradicting the competitor bound.

No such adjacent pair can occur. Since Voronoi cells intersect the ordered support in consecutive blocks, each support atom \(1,2,\ldots,n-3\) is a singleton cell. The centroid condition forces a representative at each of these atoms. Every remaining representative is the centroid of support points at least \(n-2\), so the increasing optimal set has \(a_j=j\) for \(1\le j\le n-3\). This proves the conjecture. The unconditional two-tail classification and the formula for \(V_n\) then follow from Theorem 1.3 of the motivating paper.

## Verification
The proof is analytic. The bundled `verify.py` checks the competitor identity and exhaustively checks the adjacent-pair inequalities for every initial permutation through \(k=8\) and several admissible \(n\). These finite checks are supplemental and are not used to infer the theorem for arbitrary \(k\) or \(n\).

## Relationship to prior work
Gomez, Martinez, Roychowdhury, Salazar, and Vallez introduce this permutation family, prove Theorem 1.3 conditional on the first \(n-3\) representatives being fixed atoms, verify Conjecture 1.5 in two examples, and explicitly state that the general proof is unknown. Their proof also gives the sharp competitor bound \(V_n\le2^{3-n}/3\), but does not combine it with a permutation-uniform adjacent-pair floor.

Cabasag, Huq, Mendoza, and Roychowdhury determine optimal quantizers for the unpermuted geometric law \(P(\{j\})=2^{-j}\). That special law does not imply the arbitrary finite-permutation statement. The present argument isolates the feature that survives every allowed permutation: any early adjacent merger already costs at least the globally attainable error scale.

Targeted searches using the conjecture number, exact source identifier, singleton-cell formulation, first-\(n-3\)-representative formulation, dyadic parameters, and adjacent-pair mechanism found no later statement proving the general conjecture. Current institutional metadata for the source still describes the conjecture as verified only by examples and used conditionally.

## Limitations
The theorem does not extend the conjecture beyond permutations of the prescribed dyadic masses. It uses squared error and one-dimensional ordered support. The source indicates that the conclusion can fail when the initial weights are not a permutation of the dyadic multiset. An unindexed or differently phrased proof remains the principal originality risk.

## References
1. J. Gomez, H. Martinez, M. K. Roychowdhury, A. Salazar, and D. J. Vallez, “Quantization for a set of discrete distributions on the set of natural numbers,” arXiv:2305.02372v1, first public 2023-05-03.
2. R. Cabasag, S. Huq, E. Mendoza, and M. K. Roychowdhury, “Optimal quantization for discrete distributions,” arXiv:2008.03255v1, first public 2020-08-07.
