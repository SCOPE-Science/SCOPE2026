# A sharper Newton-basis norm bound for product-image projectors

## Finding

Let \(B\) and \(E\) be finite-dimensional Hilbert spaces, let \(P\) be an orthogonal projection on \(B\otimes E\), and let \(P_i\) denote its copy on \(B_i\otimes E_i\) for \(i=1,\ldots,n\). For integers \(n\ge6\) and \(3\le D\le n/2\), take the degree-at-most-\(D\) polynomial \(p_{n,D}\) supplied by the NOR-approximation lemma in [1], so that \(p_{n,D}(0)=1\) and \(|p_{n,D}(k)|\le\epsilon:=2^{-cD^2/n}\) for every integer \(1\le k\le n\), with universal constant \(c>0\).

Define \(q(x)=p_{n,D}(n-x)\), \(S=\sum_{i=1}^nP_i\), and \(\widetilde P=q(S)\). Write \(\mu=\|P\|_\pi\), where \(\|\cdot\|_\pi\) is the projective tensor norm induced by the local operator norms across \(B:E\). Then

\[
\widetilde P P^{\otimes n}=P^{\otimes n}\widetilde P=P^{\otimes n},\qquad
\|\widetilde P-P^{\otimes n}\|_\infty\le\epsilon,
\]

and the sharper norm estimate

\[
\boxed{\displaystyle \|\widetilde P\|_\pi\le\epsilon\sum_{s=0}^{D}\binom ns(2\mu)^s.}
\]

The dimension bound in [1, Lemma 2] gives \(\mu\le\kappa:=\min\{(\dim B)^2,(\dim E)^2\}\). Consequently,

\[
\|\widetilde P\|_\pi\le\epsilon(2\kappa)^D2^{n h(D/n)},
\]

where \(h(t)=-t\log_2t-(1-t)\log_2(1-t)\) is binary entropy. This improves the published upper bound for the same polynomial approximation by the exponential factor \(\epsilon\).

## Assumptions and scope

All spaces are finite-dimensional. The operators \(P_i\) are commuting copies of one orthogonal projection. The parameter range \(3\le D\le n/2\) ensures that every integer sampled in the Newton coefficients is strictly less than \(n\), where the polynomial is uniformly small after the substitution \(q(x)=p_{n,D}(n-x)\). The constant \(c\) and existence of \(p_{n,D}\) are inherited from [1, Fact 2]; they are not newly optimized here. The claim bounds the same approximant used in [1], not the optimal possible approximant.

## Proof

By the NOR-approximation lemma [1, Fact 2], the polynomial \(p_{n,D}\) has degree at most \(D\), satisfies \(p_{n,D}(0)=1\), and obeys \(|p_{n,D}(k)|\le\epsilon\) for integer \(k=1,\ldots,n\). Thus \(q(n)=1\), while \(|q(j)|=|p_{n,D}(n-j)|\le\epsilon\) for every integer \(0\le j<n\).

Expand \(q\) in the Newton basis:

\[
q(x)=\sum_{s=0}^{D}a_s\binom{x}{s},\qquad
a_s=\sum_{j=0}^{s}(-1)^{s-j}\binom{s}{j}q(j).
\]

For every \(s\le D\le n/2<n\), each value \(q(j)\) appearing in this finite difference has magnitude at most \(\epsilon\). Hence

\[
|a_s|\le\epsilon\sum_{j=0}^{s}\binom{s}{j}=\epsilon 2^s.
\]

Because the projections \(P_i\) commute, the binomial identity for commuting projections gives

\[
\binom{S}{s}=\sum_{\substack{T\subseteq\{1,\ldots,n\}\\|T|=s}}\prod_{i\in T}P_i.
\]

A product over a set \(T\) of size \(s\) is a tensor product of \(s\) copies of \(P\), with identities on the other pairs. By the definition of the projective norm, tensor-product submultiplicativity, and \(\|I\|_\pi=1\), its norm across \(B^n:E^n\) is at most \(\mu^s\). Therefore the triangle inequality yields

\[
\begin{aligned}
\|\widetilde P\|_\pi
&=\left\|\sum_{s=0}^{D}a_s\binom{S}{s}\right\|_\pi\\
&\le\sum_{s=0}^{D}|a_s|\binom ns\mu^s\\
&\le\epsilon\sum_{s=0}^{D}\binom ns(2\mu)^s.
\end{aligned}
\]

For the operator-norm approximation, the joint spectrum of \(S\) consists of integers \(k\in\{0,\ldots,n\}\), counting the number of local projections whose eigenvalue is one. On the all-one subspace, \(k=n\) and \(q(n)=1\); on every other joint eigenspace, \(|q(k)|=|p_{n,D}(n-k)|\le\epsilon\). This proves \(\|\widetilde P-P^{\otimes n}\|_\infty\le\epsilon\) and the two product identities.

Finally, [1, Lemma 2] gives \(\mu\le\kappa\). For \(D\le n/2\), the standard binomial-tail estimate \(\sum_{s=0}^{D}\binom ns\le2^{n h(D/n)}\) and \((2\kappa)^s\le(2\kappa)^D\) imply the stated dimension-only bound. In [1, Lemma 3], the same polynomial is expanded using the complementary projections \(I-P_i\), for which the displayed coefficient bound is \(2^s\). Expanding instead in the \(P_i\) basis exploits the small values of \(q(0),\ldots,q(D)\) and supplies the extra factor \(\epsilon\).

## Verification

The proof uses exact finite-dimensional identities only: Newton interpolation, the binomial identity for commuting projections, the projective-norm triangle inequality, and the spectral decomposition of a sum of commuting projections. No numerical computation or finite experiment is used. The only imported existence result is [1, Fact 2]. The stronger estimate is a bound on the existing approximant, not a claim of optimality.

## Relationship to prior work

Beigi and Tomamichel [1] prove a NOR-polynomial approximation and bound its projective norm by expanding in products of complementary projections; their Lemma 3 yields a dimension-dependent bound without the factor \(\epsilon\). The present estimate uses the same polynomial and the same approximation error, but changes the Newton expansion variable from the number of failed local projections to the number of successful local projections. This makes every finite-difference sample small and improves the norm estimate. Their conclusion notes that sharper projective-norm bounds can improve the quantitative tradeoff, but the particular coefficient improvement proved here is not stated in the inspected text.

Johnston and Kribs [2] and Palazuelos [3] also study projective tensor norms in quantum information, but the cited results use trace-norm local spaces or a different norm formulation; they do not directly imply this operator-norm estimate for the Stinespring-image approximation. Searches of the relevant research index did not return an equivalent claim. This search result is supporting evidence, not a proof of uniqueness.

## Limitations

The constant \(c\) is inherited from the NOR approximation and is not optimized. The bound may not be sharp, and no matching lower bound is established. The improvement is relative to the published estimate for this same approximant; it does not by itself optimize the overall strong-converse exponent or prove a new capacity theorem. A broader literature search could reveal an equivalent Newton-basis estimate not surfaced by the searches described in the review record.

## References

[1] S. Beigi and M. Tomamichel, “Strong Converse for Quantum Capacity via a Fully Quantum Blowing-Up Lemma,” arXiv:2609.11771v1 (first public version 2026-09-10); see Fact 2, Lemma 2, Lemma 3, and Theorem 4. The later version is titled “Strong Converses for Quantum Channel Capacities from Blowing-Up Lemmata.”

[2] N. Johnston and D. W. Kribs, “Duality of Entanglement Norms,” arXiv:1304.2328 (2013).

[3] C. Palazuelos, “On the largest Bell violation attainable by a quantum state,” *Journal of Functional Analysis* 267 (2014), DOI: 10.1016/j.jfa.2014.07.028.
