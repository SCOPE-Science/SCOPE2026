# Generic finite-field subspaces have two-step-flag tuple orbits

## Finding

Fix a prime power \(q\). Let \(M_q=(V,G)\) be the countable pair in which \(V\) is an infinite-dimensional \(\mathbb F_q\)-vector space, \(G\le V\) is infinite-dimensional, and \(V/G\) is infinite-dimensional. This is the pure finite-field specialization of the dense-codense generic-submodule construction, and also the familiar lovely-pair instance of pure vector spaces.

For an ordered tuple \(v=(v_1,\ldots,v_n)\), define the coordinate map
\[
f_v:\mathbb F_q^n\longrightarrow V,\qquad e_i\longmapsto v_i,
\]
and the two subspaces
\[
K_v=\ker f_v,\qquad U_v=f_v^{-1}(G).
\]
Then \(K_v\le U_v\le\mathbb F_q^n\), and the pair \((K_v,U_v)\) is a complete automorphism-orbit invariant for the tuple. Every such two-step flag occurs. Consequently the number of all ordered \(n\)-tuple orbits is exactly
\[
\boxed{O_n(q)=\sum_{0\le a\le b\le n}{n\brack b}_q{b\brack a}_q
      =\sum_{a+b+c=n}{n\brack a,b,c}_q}.
\]
For injective ordered tuples, \(K_v=0\), so the exact orbit count is the Galois number
\[
\boxed{I_n(q)=\sum_{b=0}^n {n\brack b}_q}.
\]
For fixed \(q\), these have different quadratic logarithmic growth:
\[
\boxed{O_n(q)=\Theta_q(q^{\lfloor n^2/3\rfloor}),\qquad
I_n(q)=\Theta_q(q^{\lfloor n^2/4\rfloor}).}
\]
Thus allowing linear dependencies changes the leading base-\(q\) orbit-growth exponent from \(1/4\) to \(1/3\).

## Assumptions and scope

The pair \(M_q\) is the countable infinite/infinite pair: \(\dim G=\dim(V/G)=\aleph_0\). The language is the pure \(\mathbb F_q\)-vector-space language together with a unary predicate for \(G\). Because the field is finite, the structure is countable and oligomorphic.

The result counts ordered tuples, including repetitions and zero coordinates. "Injective" means that the tuple entries are pairwise distinct; however the displayed formula \(I_n(q)\) actually counts the stronger stratum of linearly independent tuples. To avoid ambiguity, throughout this finding \(I_n(q)\) denotes the linearly independent tuple-orbit count. The comparison is between the complete tuple profile and this natural independent stratum, not between all tuples and merely pairwise-distinct tuples.

## Proof

An automorphism of \(M_q\) is an invertible \(\mathbb F_q\)-linear map of \(V\) preserving \(G\). It therefore preserves every linear relation among the coordinates and whether each linear combination lies in \(G\). Hence it preserves \(K_v\) and \(U_v\).

Conversely suppose \(v,w\) have the same pair \(K\le U\). The rule
\[
f_v(x)\longmapsto f_w(x)
\]
is well-defined because the two coordinate maps have the same kernel. It gives a linear isomorphism
\[
h:\operatorname{span}(v)\longrightarrow\operatorname{span}(w).
\]
Moreover
\[
f_v(x)\in G\iff x\in U\iff f_w(x)\in G,
\]
so \(h\) maps \(\operatorname{span}(v)\cap G\) onto \(\operatorname{span}(w)\cap G\).

Any isomorphism between finite-dimensional subspace pairs of this form extends to an automorphism of \((V,G)\). Indeed, extend a basis of the intersection inside \(G\), extend the induced basis of the quotient inside \(V/G\), and then extend the resulting finite partial linear map to bases of the two infinite-dimensional pieces. Therefore \(v\) and \(w\) are in the same orbit.

Every flag \(K\le U\le\mathbb F_q^n\) is realized. The quotient \(W=\mathbb F_q^n/K\) carries the distinguished subspace \(U/K\). Since both \(G\) and \(V/G\) have infinite dimension, this finite-dimensional pair embeds into \((V,G)\); the images of the standard basis give a tuple with exactly the prescribed \(K\) and \(U\).

To count flags, first choose \(U\) of dimension \(b\), then choose \(K\le U\) of dimension \(a\). This gives
\[
O_n(q)=\sum_{b=0}^n {n\brack b}_q\sum_{a=0}^b{b\brack a}_q.
\]
Writing the three successive quotient dimensions as \(a,b,c\) with \(a+b+c=n\) gives the equivalent Gaussian multinomial sum. If the tuple is linearly independent then \(K=0\), leaving one arbitrary subspace \(U\le\mathbb F_q^n\), hence the Galois-number formula for \(I_n(q)\).

For the asymptotics, put
\[
C_q=\prod_{j=1}^{\infty}(1-q^{-j})>0.
\]
Uniformly in \(0\le r\le m\),
\[
C_q q^{r(m-r)}\le {m\brack r}_q\le C_q^{-1}q^{r(m-r)}.
\]
Thus the Gaussian multinomial with block sizes \(a,b,c\) is within a \(q\)-dependent constant factor of
\[
q^{ab+ac+bc}.
\]
The maximum of \(ab+ac+bc\) over \(a+b+c=n\) is \(\lfloor n^2/3\rfloor\), attained by balanced triples. Away from balance the exponent drops quadratically, so the sum of all normalized terms is bounded above and below by positive constants depending only on \(q\). This proves \(O_n(q)=\Theta_q(q^{\lfloor n^2/3\rfloor})\).

Likewise \({n\brack b}_q\) is within a fixed factor of \(q^{b(n-b)}\), whose maximum is \(\lfloor n^2/4\rfloor\); the tails again fall quadratically. Hence \(I_n(q)=\Theta_q(q^{\lfloor n^2/4\rfloor})\).

## Verification

A standalone verifier independently enumerates subspaces in reduced row-echelon form over \(\mathbb F_2\) through dimension five and over \(\mathbb F_3\) through dimension four. It counts all nested pairs \(K\le U\) directly, compares them with the Gaussian flag formula, and checks that the coefficient-vector signature recording "zero / in \(G\) / outside \(G\)" uniquely recovers every flag.

It also checks the two closed flag sums over several fields and dimensions and verifies, for \(0\le n\le100\), the exact dominant exponents \(\lfloor n^2/3\rfloor\) and \(\lfloor n^2/4\rfloor\). The run performs 8,999 assertions and prints `VERIFY_OK`.

For example,
\[
(O_n(2))_{n=0}^8=(1,3,12,66,513,5769,95706,2379348,89759799),
\]
while
\[
(I_n(2))_{n=0}^8=(1,2,5,16,67,374,2825,29212,417199).
\]

## Relationship to prior work

Berenstein, d'Elbée, and Vassiliev develop the generic-submodule theory and prove quantifier elimination in the fraction-field case. Their Corollary 2.5 says that tuple type in the expansion is controlled by the base-language type together with the module type of the part of the tuple span lying in the predicate. In the pure finite-field specialization, those data collapse exactly to the flag \(K_v\le U_v\).

The same paper identifies the pure-vector-space case with lovely-pair behavior and supplies the structural setting, but searches of the paper found no occurrence of "orbit", "Galois", or "Gaussian", and the inspected text does not enumerate tuple orbits. Standard finite-field combinatorics supplies the counts of subspaces and flags; the new synthesis is the exact orbit-profile interpretation and the contrast between the \(1/3\) all-tuple exponent and the \(1/4\) independent-stratum exponent.

Targeted searches for the exact flag formula, the distinguished-subspace orbit profile, and the exponent comparison found literature on flag varieties and orbit flag codes but no equivalent model-theoretic tuple-orbit statement.

## Limitations

The orbit classification is elementary once the pair is recognized as an infinite-dimensional vector space with an infinite-codimensional distinguished subspace. The principal originality risk is therefore uncatalogued folklore or an implicit observation in the classical theory of lovely pairs or parabolic linear groups.

The symbol \(I_n(q)\) here refers to linearly independent tuples, not merely pairwise-distinct tuples. Pairwise-distinct tuples may still satisfy nontrivial linear relations and are included in the larger flag profile.

The asymptotic constants hidden by \(\Theta_q\) are not optimized.

## References

1. Alexander Berenstein, Christian d'Elbée, and Evgueni Vassiliev, *Vector spaces with a dense-codense generic submodule*, arXiv:2204.10758v1 (22 April 2022); Annals of Pure and Applied Logic 175 (2024), 103442, DOI 10.1016/j.apal.2024.103442. See especially Theorem 2.4, Corollary 2.5, and the pure-vector-space examples.
2. Standard finite-field flag enumeration: a \(b\)-subspace of \(\mathbb F_q^n\) is counted by \({n\brack b}_q\), and an \(a\)-subspace inside it by \({b\brack a}_q\).
