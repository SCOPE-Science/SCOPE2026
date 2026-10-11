# A uniform complement-norm gap for the first bidual-tower layer of \(c_0(\Gamma)\)

## Finding
For every infinite set \(\Gamma\), over the complex scalars, let \(X=c_0(\Gamma)\), let \(X_n=X^{(2n)}\), and form the completed isometric direct-limit tower
\[
T=\widetilde X=\overline{\bigcup_{n\ge0}X_n}
\]
using the canonical maps \(J_{X_n}:X_n\to X_{n+1}\). Let \(j:X_1=\ell_\infty(\Gamma)\to T\) be the canonical isometric inclusion. There is a norm-one projection onto \(j(X_1)\), but **every** norm-one projection \(P:T\to j(X_1)\) obeys
\[
\boxed{\|I_T-P\|\ge\frac43.}
\]
Thus this layer is \(1\)-complemented but is not bicontractively complemented; the obstruction is uniform in the cardinality of \(\Gamma\).

## Assumptions and scope
All Banach spaces and linear maps are complex. The index set \(\Gamma\) is arbitrary and infinite, with the discrete topology when taking its Stone–Čech compactification. The iterated duals carry their usual operator norms and are joined by canonical isometries. A *bicontractive projection* means an idempotent \(P\) with \(\|P\|\le1\) and \(\|I-P\|\le1\). The estimate is a lower bound for the complementary norm among norm-one projections: it is **not** claimed to be the optimal constant for this tower or to settle the corresponding question for every Banach space.

## Proof
**1. Three-point fibers obstruct a bicontractive averaging projection.** Let \(L,K\) be compact Hausdorff spaces, \(\pi:L\to K\) a continuous surjection, and \(J:C(K)\to C(L)\) the unital isometric embedding \(Jg=g\circ\pi\). Suppose a fiber \(\pi^{-1}(u)\) contains distinct points \(y_1,y_2,y_3\). Let \(Q:C(L)\to J(C(K))\) be any projection of norm one and set \(R=J^{-1}Q\). The functional \(f\mapsto(Rf)(u)\) has norm at most one and takes the value one at the constant function \(1\). By the complex Riesz representation theorem and equality in the triangle inequality, it is integration against a *positive probability measure* \(\mu_u\) on \(L\). Since \(RJ=I_{C(K)}\), the push-forward \(\pi_*\mu_u\) equals \(\delta_u\), so \(\mu_u\) is supported on \(\pi^{-1}(u)\). Among the three named points choose \(y\) with \(\mu_u(\{y\})\le1/3\). Evaluating \(I-Q\) at that point gives
\[
\begin{aligned}
\|I-Q\|&\ge\sup_{\|f\|_\infty\le1}|f(y)-(Rf)(u)|\\
&=\|\delta_y-\mu_u\|_{M(L)}
=2(1-\mu_u(\{y\}))\ge\frac43.
\end{aligned}
\]
No finiteness assumption on the whole fiber or on \(K,L\) is used.

**2. The second positive tower level has a three-point fiber.** Put \(E=\ell_\infty(\Gamma)=C(K)\), where \(K=\beta\Gamma\). Its Stone–Čech remainder is \(U=K\setminus\Gamma\), a nonempty closed compact subspace, and write \(B=C(U)\). Restriction \(q:E\to B\) is a surjective unital \(*\)-homomorphism, with kernel \(c_0(\Gamma)\). As a consequence of the central ideal decomposition of the commutative von Neumann algebra \(E^{**}\), there is a canonical unital isometric \(*\)-isomorphism
\[
E^{**}\simeq\ell_\infty(\Gamma)\oplus_\infty B^{**},
\qquad J_E(f)\longleftrightarrow\big(f,J_B(qf)\big).
\]
For clarity, this follows directly by splitting every regular measure on \(K\) into its (countably supported) atomic mass on the open discrete set \(\Gamma\) and its mass on \(U\): \(C(K)^*=\ell_1(\Gamma)\oplus_1 M(U)\). Dualizing yields the displayed Banach-space decomposition. The two measure bands are disjoint, so their second duals are orthogonal central summands for the Arens \(*\)-product, giving the asserted \(*\)-isomorphism and the stated formula for \(J_E\).

Let \(L_B\) be the Gelfand spectrum of the commutative unital \(C^*\)-algebra \(B^{**}\). The unital isometric \(*\)-monomorphism \(J_B:C(U)\to C(L_B)\) is the pullback of a continuous surjection \(\pi_B:L_B\to U\). Hence \(E^{**}=C(K\sqcup L_B)\), and the canonical inclusion \(J_E:C(K)\to E^{**}\) is pullback by
\[
\pi:K\sqcup L_B\to K,\qquad
\pi(k)=k\ (k\in K),\qquad \pi(v)=\pi_B(v)\ (v\in L_B).
\]
Here \(\sqcup\) denotes a disjoint topological union.

The space \(B=C(U)\) is nonreflexive. Indeed, choose pairwise disjoint infinite subsets \(A_1,A_2,\ldots\subset\Gamma\). The sets \(U_m=\overline{A_m}^{\beta\Gamma}\cap U\) are pairwise disjoint nonempty clopen subsets of \(U\). The map from \(c_0\) into \(B\) sending a null sequence \((t_m)\) to the uniformly convergent sum \(\sum_m t_m1_{U_m}\) is an isometric embedding, so \(B\) cannot be reflexive. Consequently \(J_B\) is not surjective. If \(\pi_B\) were one-to-one, it would be a homeomorphism between compact Hausdorff spaces, making \(J_B\) surjective, a contradiction. Therefore some \(u\in U\) has at least two distinct inverse images \(v_1,v_2\in L_B\). The fiber \(\pi^{-1}(u)\) contains at least the three distinct points \(u\in K\), \(v_1\in L_B\), \(v_2\in L_B\). Step 1 now proves
\[
\|I_{E^{**}}-Q\|\ge\frac43
\]
for every norm-one projection \(Q:E^{**}\to J_E(E)\).

**3. Pass from the second level to the completed tower.** The image of \(E^{**}=X_2\) in \(T\) contains \(j(E)\), and its inclusion is isometric. If \(P:T\to j(E)\) is any norm-one projection, restriction to \(X_2\), transported through this isometry, produces a norm-one projection \(Q:E^{**}\to J_E(E)\). Thus
\[
\|I_T-P\|\ge\|I_{E^{**}}-Q\|\ge\frac43.
\]

**4. Norm-one projections really exist.** For each \(n\ge1\), put \(Y_n=X^{(2n-1)}\), so \(X_n=Y_n^*\). The adjoint of the canonical embedding \(J_{Y_n}:Y_n\to Y_n^{**}\) gives a norm-one retraction \(r_n=(J_{Y_n})^*:X_{n+1}\to X_n\), satisfying \(r_nJ_{X_n}=I_{X_n}\). Their finite composites down to \(X_1\) are compatible on nested levels and have norm at most one. Thus they define a contractive retraction on the algebraic union \(\bigcup_{n\ge1}X_n\), which extends continuously to a retraction \(r:T\to X_1\) of norm one. The map \(P=jr\) is the asserted norm-one projection. Combined with Step 3 this completes the proof.

## Verification
The proof uses only exact norm identities and standard Banach-space/C*-algebra representations: the Riesz measure of a unital contraction, the central band splitting of \(C(\beta\Gamma)^{**}\), Gelfand duality, and canonical adjoint retractions. The key quantitative calculation is the exact total-variation formula \(\|\delta_y-\mu\|=2(1-\mu\{y\})\) for a probability measure. With precisely three points in a fiber and uniform mass on them, the finite-dimensional model realizes \(4/3\); this checks the *fiber bound* but is not a sharpness statement for the infinite tower. No finite experiment, computational inference, or external certificate underlies the infinite-dimensional conclusion.

## Relationship to prior work
Liu and Uglešić, *Basic Theory of Tower Systems*, arXiv:2610.03179v1, §4, Proposition 4.1, excludes an \(M\)-projection for the \(c_0\) example, but explicitly distinguishes and leaves unsettled the weaker existence of a **bicontractive** retraction. The present theorem rules out that weaker property for the same canonical layer, proves a quantitative complement norm gap, and extends the argument to all infinite index sets. The norm-one existence part uses the canonical retraction construction familiar from this paper and Gwizdek's *Isometric direct limits of bidual Banach spaces*, arXiv:2205.14385v7. General structural results on bicontractive projections in operator algebras, including Blecher and Neal, arXiv:1905.05836v4, give relevant background but do not themselves identify the three-point fiber in this particular canonical tower embedding.

## Limitations
The lower bound \(4/3\) is **not** claimed sharp among all projections on the complete tower. The claim concerns the first *positive* level \(X^{**}\) of the tower of \(c_0(\Gamma)\), not arbitrary spaces, other levels, or the base \(c_0(\Gamma)\). It is a theorem about complex Banach spaces; the real-scalar analogue has not been separately asserted. Independent validation and an exhaustive bibliographic uniqueness guarantee are not claimed.

## References
1. Q. Liu and N. Uglešić, *Basic Theory of Tower Systems*, arXiv:2610.03179v1 (first public 2026-10-02), especially §2.6, §3.3 and §4. https://arxiv.org/html/2610.03179v1
2. S. Gwizdek, *Isometric direct limits of bidual Banach spaces*, arXiv:2205.14385v7. https://arxiv.org/abs/2205.14385
3. D. Blecher and M. Neal, *Contractive projections and real positive maps on operator algebras*, arXiv:1905.05836v4. https://arxiv.org/abs/1905.05836
