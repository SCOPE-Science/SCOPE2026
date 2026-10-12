# Wang's stratum maximum is always attained by the ambient weighted projective space
## Finding
Let
\[
\mathbf P=\mathbf P(a_0,\ldots,a_n),\qquad n\ge3,
\]
be a well-formed weighted projective space with isolated singularities, in the setup of Wang's Proposition 3.17. Write
\[
A=\{0,\ldots,n\},\qquad
P=\prod_{i\in A}a_i,\qquad
S=\sum_{i\in A}a_i.
\]
Wang defines
\[
\Theta=
\max_{\substack{I\subseteq A\\ |I|\ge4}}
\frac{1}{\prod_{i\notin I}a_i}
\left(
\frac{\sum_{i\in I}a_i}{\prod_{i\in I}a_i}
+|I|-3
\right).
\]
Then the maximum is uniquely attained by the full set \(I=A\), and therefore
\[
\boxed{\Theta=n-2+\frac{S}{P}}.
\]

Combining this identity with Wang's Proposition 3.17 gives the global hyperbolicity criterion
\[
\boxed{
m>n-2+\frac{\sum_{i=0}^{n}a_i}{\prod_{i=0}^{n}a_i}
\quad\Longrightarrow\quad
X\in|mH|\text{ very general is algebraically hyperbolic}.
}
\]
This is exactly the numerical threshold that Wang's Proposition 3.11 gives for algebraic hyperbolicity away from the toric boundary. Thus, within Wang's isolated-singularity setup, the toric boundary imposes no additional numerical penalty.

For the example
\[
\mathbf P(1,1,2,3,5),
\]
one has
\[
\Theta=2+\frac{12}{30}=\frac{12}{5},
\]
so every very general \(X\in|mH|\) with \(m\ge3\) is algebraically hyperbolic globally.

## Assumptions and scope
The weights \(a_i\) are positive integers. Wang assumes that \(\mathbf P(a_0,\ldots,a_n)\) is well formed, has isolated singularities, and has dimension \(n\ge3\). In this situation the weights are pairwise coprime and
\[
k=\prod_{i=0}^{n}a_i.
\]
For a toric resolution
\[
f:\widetilde{\mathbf P}\to\mathbf P,
\]
Wang writes
\[
H=f^*\mathcal O_{\mathbf P}(k)
\]
and studies zero loci of very general sections of \(mH\). General such hypersurfaces avoid the isolated singular points and correspond to general hypersurfaces of weighted degree \(mk\) on \(\mathbf P\).

The conclusion is a sufficient condition for algebraic hyperbolicity of a very general hypersurface. It is not asserted to be a necessary condition.

## Proof
For a subset
\[
I\subseteq A,\qquad |I|\ge4,
\]
put
\[
S_I=\sum_{i\in I}a_i,\qquad
P_I=\prod_{i\in I}a_i,\qquad
q_I=\prod_{i\notin I}a_i.
\]
Because
\[
P_Iq_I=P,
\]
the quantity occurring in Wang's maximum can be rewritten exactly as
\[
\theta_I
=
\frac{1}{q_I}
\left(
\frac{S_I}{P_I}+|I|-3
\right)
=
\frac{S_I}{P}+\frac{|I|-3}{q_I}.
\]

For the full set \(I=A\), one has \(q_A=1\), \(|A|=n+1\), and \(S_A=S\), so
\[
\theta_A
=
\frac{S}{P}+n-2.
\]

Now let \(I\subsetneq A\) be proper. Since all weights are positive,
\[
S_I<S.
\]
Also \(q_I\ge1\) and \(|I|\le n\), hence
\[
\frac{|I|-3}{q_I}
\le |I|-3
\le n-3
<n-2.
\]
Therefore
\[
\theta_I
=
\frac{S_I}{P}+\frac{|I|-3}{q_I}
<
\frac{S}{P}+n-2
=
\theta_A.
\]
Thus \(I=A\) is the unique maximizer and
\[
\Theta=\theta_A=n-2+\frac{S}{P}.
\]

Wang's Proposition 3.17 states that every integer \(m>\Theta\) gives algebraic hyperbolicity for a very general \(X\in|mH|\). Substitution of the exact value of \(\Theta\) proves the claimed global criterion.

For \(\mathbf P(1,1,2,3,5)\), the dimension is \(4\), the sum of the weights is \(12\), and their product is \(30\). Hence
\[
\Theta=4-2+\frac{12}{30}=\frac{12}{5},
\]
so the integer condition \(m>\Theta\) is precisely \(m\ge3\).

## Verification
The initiating source was checked in full text at the definition of the weighted-projective setup, Proposition 3.11, Proposition 3.17, its proof, and Corollary 3.18.

The source explicitly assumes a well-formed weighted projective space with isolated singularities, records that the weights are pairwise coprime and that \(k=\prod_i a_i\), and defines \(H=f^*\mathcal O(k)\) on a toric resolution. Proposition 3.11 proves algebraic hyperbolicity outside the toric boundary under
\[
m>n-2+\frac{\sum_i a_i}{\prod_i a_i}.
\]
Proposition 3.17 introduces the stratum maximum \(\Theta\) displayed above and proves global algebraic hyperbolicity for \(m>\Theta\).

The full index set is part of the maximum. This is also forced by the source's own conventions: in dimension \(3\), there are four indices and no proper subset of cardinality at least \(4\), while Proposition 3.17 and Corollary 3.18 still apply; moreover Corollary 3.18 computes \(\Theta\) for \(\mathbf P(1,\ldots,1,r)\) using the ambient value.

The algebraic simplification
\[
\theta_I=\frac{S_I}{P}+\frac{|I|-3}{q_I}
\]
was checked directly from the printed formula. The strict comparison for every proper \(I\) uses only positivity of the weights and \(q_I\ge1\); there is no finite enumeration or asymptotic step.

As an independent numerical sanity check of the displayed example,
\[
2+\frac{12}{30}=\frac{12}{5}<3.
\]

## Relationship to prior work
Wang's Proposition 3.11 gives the ambient numerical threshold
\[
n-2+\frac{\sum_i a_i}{\prod_i a_i}
\]
but concludes only algebraic hyperbolicity outside the toric boundary. Proposition 3.17 then obtains global algebraic hyperbolicity by taking a maximum over all relevant toric strata. The present finding identifies that maximum exactly and shows that every proper-stratum contribution is strictly smaller than the ambient contribution. Consequently the global conclusion already holds at the Proposition 3.11 threshold.

Wang's Corollary 3.18 gives coarser general consequences, such as \(m\ge2n\), and a sharper special-family computation for \(\mathbf P(1,\ldots,1,r)\). The exact formula here applies uniformly to every weighted projective space covered by Proposition 3.17.

Coskun and Riedl previously obtained detailed hyperbolicity bounds for very general surfaces in \(\mathbf P(1,1,1,r)\). Their result is a special three-dimensional family and does not state the general stratum-maximization identity.

Targeted searches for the exact \(\Theta\)-formula, the equivalent statement that the ambient stratum is always the unique maximizer, and the consequence that the toric boundary never raises Wang's numerical threshold did not locate a covering statement.

## Limitations
The result simplifies Wang's sufficient criterion; it does not prove that the resulting threshold is necessary or optimal for every weight vector.

The argument uses Proposition 3.17 as stated for well-formed weighted projective spaces with isolated singularities. Wang notes additional complications for non-isolated singularities, and no extension to that setting is claimed here.

The conclusion is for very general hypersurfaces in the specified linear systems. Special hypersurfaces may behave differently.

## References
J. Wang, “Algebraic hyperbolicity of very general hypersurfaces in weighted projective spaces,” arXiv:2511.04890v1, first public 2025-11-07; especially Propositions 3.11 and 3.17 and Corollary 3.18.

I. Coskun and E. Riedl, “Algebraic hyperbolicity of very general surfaces,” arXiv:1912.07689, published in Israel Journal of Mathematics; especially the discussion of \(\mathbf P(1,1,1,r)\).
