# A sharp inball-center phase transition in simplex-weighted harmonic polytopes

## Finding
Let \(n\ge3\). Let \(\Pi_n=\operatorname{conv}\{(\sigma(1),\ldots,\sigma(n)):\sigma\in\mathfrak S_n\}\subset\mathbb R^n\), and let \(D_n=\operatorname{conv}\{(e_i,e_i):1\le i\le n\}\subset\mathbb R^n\times\mathbb R^n\). For every \(\lambda>0\), define the simplex-weighted harmonic polytope
\[
H_n(\lambda)=(\Pi_n\times\Pi_n)+\lambda D_n.
\]
Equip its \((2n-2)\)-dimensional affine hull with the Euclidean metric induced from \(\mathbb R^{2n}\). Put
\[
L_n(\lambda)=\frac{\sqrt{n(n-1)}}2+\frac{\lambda}{\sqrt{n(n-1)}},\qquad
R_n=\sqrt{\frac{n(n-1)}2},\qquad
\lambda_n^*=\frac{n(n-1)(\sqrt2-1)}2.
\]
The exact Euclidean inradius is
\[
\boxed{r_{\mathrm{in}}(H_n(\lambda))=\min\{L_n(\lambda),R_n\}.}
\]
For \(0<\lambda<\lambda_n^*\), the largest ball has a **unique** center and meets precisely the \(2n\) facets of types \(S=\{i\},T=[n]\) and \(S=[n],T=\{i\}\). At \(\lambda=\lambda_n^*\), its center remains unique and exactly \(4n\) facets are tangent: the preceding \(2n\) and the \(2n\) disjoint bisubsets of sizes \(1,n-1\) (in either order). For \(\lambda>\lambda_n^*\), exactly the \(2n\) disjoint facets of sizes \(1,n-1\) touch the symmetry-centered largest ball, and the **full set of optimal centers has affine dimension \(n-1\)**. The normal fan and face lattice of \(H_n(\lambda)\) are constant throughout \(\lambda>0\): this is a metric phase transition without a combinatorial transition.

More precisely, put \(\mu=(n+1)/2+\lambda/n\). The distinguished optimal center is \(c_\lambda=(\mu\mathbf1,\mu\mathbf1)\). For \(\lambda\le\lambda_n^*\) it is the only optimal center. For \(\lambda>\lambda_n^*\), the complete optimal-center set is
\[
\left\{c_\lambda+(z,z):\sum_i z_i=0,\quad
\sum_{i\in C}z_i\le\beta_{|C|}(\lambda)\ \text{for all}\ \emptyset\ne C\subsetneq[n]\right\},
\]
where, for \(1\le k<n\),
\[
\beta_k(\lambda)=\frac{k(n-k)}2+\lambda\frac{n-k}{n}-\sqrt{\frac{(n-1)k(n-k)}2}.
\]
Every \(\beta_k(\lambda)\) is strictly positive in that regime, so the center locus is full-dimensional within the \((n-1)\)-dimensional diagonal subspace displayed above.

## Assumptions and scope
The ambient basis vectors \(e_i\) are orthonormal. All balls, face distances, and center dimensions use the **intrinsic Euclidean metric** on
\[
\sum_i x_i=\sum_i y_i=\frac{n(n+1)}2+\lambda.
\]
The statements hold for each integer \(n\ge3\) and every real \(\lambda>0\), with no genericity assumption. A bisubset is an ordered pair \(S,T\ne\emptyset\) with \(S\cup T=[n]\), excluding \(S=T=[n]\). Distinct ordered bisubsets label distinct facets for \(\lambda>0\). Neither arbitrary affine deformations nor the singular endpoint \(\lambda=0\) are included.

## Proof
**1. Facets and the symmetric center.** Ardila and Escobar's facet description for \(H_n(1)\) gives, for each bisubset \((S,T)\), the inequality
\[
\sum_{i\in S}x_i+\sum_{i\in T}y_i\ge
\frac{|S|(|S|+1)+|T|(|T|+1)}2+1.
\]
As a positive Minkowski coefficient changes, the normal fan of a Minkowski sum is still the common refinement of the same two fixed normal fans. Consequently these remain exactly the facet normals for every \(\lambda>0\). The support value of \(\lambda D_n\) at each such normal equals \(\lambda\), because \(S\cup T=[n]\) but \(S=T=[n]\) is excluded. Thus the final \(1\) in the inequality is replaced by \(\lambda\). The two affine coordinate sums change by the same \(\lambda\).

Every simultaneous coordinate permutation, as well as exchanging the two coordinate blocks, acts as an orthogonal symmetry. For any radius \(r\), the allowable-center set of radius-\(r\) balls is convex and symmetry invariant. Averaging an optimal center over these symmetries produces the unique common fixed point \(c_\lambda=(\mu\mathbf1,\mu\mathbf1)\), hence the inradius is the minimum distance from \(c_\lambda\) to the facet hyperplanes.

Write \(a=n-|S|\), \(b=n-|T|\), \(k=a+b\), and \(X=a(n-a)+b(n-b)\). Valid bisubsets have \(1\le k\le n\), \(0\le a,b\le n-1\), and if \(k=n\) then \(a,b\ge1\). The centered facet slack and squared projected-normal length are exactly
\[
\ell=\frac X2+\lambda\left(1-\frac kn\right),\qquad
\|\nu\|^2=\frac Xn.
\]
Therefore its distance is the affine function of \(\lambda\)
\[
d_{a,b}(\lambda)=\sqrt n\left(\frac{\sqrt X}2+
\frac{\lambda(1-k/n)}{\sqrt X}\right).
\]
For \(k<n\), \(X=k(n-k)+2ab\ge k(n-k)\ge n-1\). For \(k=n\), \(X=2ab\ge2(n-1)\).

**2. The complete lower envelope.** The first candidate corresponds to \((a,b)=(n-1,0)\) or its exchange, yielding \(L_n(\lambda)\). The second corresponds to \((a,b)=(1,n-1)\) or its exchange, yielding the \(\lambda\)-independent value \(R_n\). They cross at \(\lambda_n^*\).

At \(\lambda=0\), all facet distances (interpreted via the positive-\(\lambda\) inequalities) are at least \(\sqrt{n(n-1)}/2=L_n(0)\). At \(\lambda=\lambda_n^*\), put \(c=(\sqrt2-1)/2\), \(t=X/(n-1)\ge1\), and \(h=n-k\). The normalized distance is
\[
\frac{d_{a,b}(\lambda_n^*)}{\sqrt{n(n-1)}}=
\frac{\sqrt t}{2}+\frac{hc}{\sqrt t}.
\]
If \(h=0\), then \(t\ge2\); the expression is at least \(1/\sqrt2\), with equality only at \((a,b)=(1,n-1)\) or the reverse. If \(h=1\), the expression is strictly increasing for \(t\ge1\), as \(2c<1\); equality with \(1/\sqrt2\) requires \(t=1\), giving \((n-1,0)\) or the reverse. If \(h\ge2\), arithmetic-geometric mean yields the strict bound
\[
\frac{\sqrt t}{2}+\frac{hc}{\sqrt t}\ge\sqrt{2hc}
\ge2\sqrt c>\frac1{\sqrt2}.
\]
The final strict inequality follows from \(4c=2(\sqrt2-1)>1/2\). All other facet distances are therefore strictly larger at the crossing.

Each \(d_{a,b}(\lambda)\) is affine in \(\lambda\) with nonnegative slope. On \([0,\lambda_n^*]\), its difference from the affine competitor \(L_n(\lambda)\) is nonnegative at both endpoints, hence throughout. On \([\lambda_n^*,\infty)\), monotonicity gives \(d_{a,b}(\lambda)\ge d_{a,b}(\lambda_n^*)\ge R_n\). Equality classifications above, together with strictness for \(\lambda>0\) away from the crossing, prove the radius and all claimed tangent-facet types.

**3. All optimal centers.** For \(\lambda\le\lambda_n^*\), the coordinate-type tangent facets imply, for any optimal center, all \(x_i\) and all \(y_i\) are at least their corresponding distance-supported common values. Their prescribed sums force equality coordinatewise, proving uniqueness.

For \(\lambda>\lambda_n^*\), the pairs of opposing tangent inequalities from the disjoint \((1,n-1)\)-facets force \(x_i-y_i=0\) at every optimal center, relative to the common affine sums. Thus every center has the form \(c_\lambda+(z,z)\) with \(\sum z_i=0\). If \(A=[n]\setminus S\), \(B=[n]\setminus T\), the shift in the facet slack equals \(-\sum_{i\in A\cup B}z_i\). For a fixed proper nonempty set \(C=A\cup B\), the requirement that the radius-\(R_n\) ball satisfy every such facet is
\[
\sum_{i\in C}z_i\le\min_{A\sqcup B=C}\left\{
\frac{X}2+\lambda\left(1-\frac{|C|}{n}\right)
-\sqrt{\frac{(n-1)X}{2}}\right\},
\]
where \(X=|C|(n-|C|)+2|A||B|\). The expression \(X/2-\sqrt{(n-1)X/2}\) is strictly increasing for \(X\ge n-1\); thus its minimum occurs at \(|A||B|=0\). This gives precisely \(\beta_{|C|}(\lambda)\). Facets with \(C=[n]\) are exactly the already-tight disjoint facets and impose no additional condition. All proper-set inequalities are strict at \(z=0\) for \(\lambda>\lambda_n^*\) by Step 2, so the indicated center polytope has affine dimension \(n-1\). At the threshold the coordinate facet orbit remains tangent, forcing uniqueness. This concludes the proof.

## Verification
A standalone `verify.py` enumerates every allowed facet-cardinality pair in dimensions \(3\) through \(15\), checks the stated two-line lower envelope on both sides of its transition, verifies the complete contact-type classification, and confirms the exact rational slack identity. Independent support-function tests evaluate the Minkowski sum directly at random objectives in dimensions \(3\) through \(6\), without using its facet representation. The executable returns `VERIFY_OK 8054`. These finite tests are corroborative: the displayed inequalities and symmetry argument prove the general result.

## Relationship to prior work
Ardila and Escobar establish the harmonic polytope, its normal fan, and the complete bisubset facet description, which is the essential input to this calculation. A previously published mathematical note, *Exact Euclidean inradius and incenter transition of the harmonic polytope* (2026), already determines the **unweighted** inradius for \(\lambda=1\) and a dimension-two exception. The restriction of the formula above to \(\lambda=1,n\ge3\) is therefore **not an originality claim**. What is new in the assessed statement is the entire positive Minkowski-weight deformation, its sharp quadratic threshold, and the emergence and exact description of a positive-dimensional center locus while the normal fan is unchanged. Ardila's *The bipermutahedron* describes deformations of a related, finer fan but does not calculate this Euclidean inball phase diagram.

## Limitations
This theorem is about the fixed standard-coordinate realizations and intrinsic Euclidean metric, not arbitrary affine images. It does not treat \(n=1,2\), the degenerate endpoint \(\lambda=0\), or unequal weights in the two permutohedral factors. The full center-locus inequalities need not be irredundant. Bibliographic search did not establish absolute novelty: an equivalent metric deformation result might exist under alternative Minkowski-interpolation or Chebyshev-center terminology. No independent mathematical audit is claimed here.

## References
1. Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078, original public version 2020-06-04; especially Definition 3.1 and Propositions 3.7–3.8, https://arxiv.org/html/2006.03078v2.
2. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, original public version 2020-08-05, https://arxiv.org/html/2008.02295v1.
3. *Exact Euclidean inradius and incenter transition of the harmonic polytope*, publicly accessible mathematical finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-inradius-and-incenter-transition-of-the-harmonic--81e898ba9eb4.
