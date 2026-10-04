# Endpoint modified compactly Hölder failure contains a closed \(\ell_p\) subspace
## Finding
For every integer \(n\ge 1\) and every \(p>n\), put \(\alpha=1-n/p\). Then
\[
\bigl((W^{1,p}(\mathbb R^n)\cap C(\mathbb R^n))\setminus CH_m^{p,\alpha}(\mathbb R^n;\mathbb R)\bigr)\cup\{0\}
\]
contains a closed subspace \(E\) isomorphic to \(\ell_p\). With the standard Sobolev norm
\[
\|f\|_{W^{1,p}}=\bigl(\|f\|_{L^p}^p+\|\nabla f\|_{L^p}^p\bigr)^{1/p},
\]
the embedding can be chosen to be a scalar multiple of an isometry. Every nonzero element of \(E\) is continuous and lies outside the endpoint modified compactly Hölder class.

## Assumptions and scope
For a map \(f\) and a ball \(B\), write
\[
|f|_{\alpha,B}=\sup_{x\ne y\in B}\frac{|f(x)-f(y)|}{|x-y|^\alpha}.
\]
Following Alvarado and Chrontsios Garitsis [1], \(f\in CH_m^{p,\alpha}\) means that for every compact set \(F\subset\mathbb R^n\) and every \(\varepsilon\in(0,1)\), there are \(r_F,C_F>0\) such that every covering family \(\{B(x_i,r_i)\}\) of \(F\), with \(r_i<r_F\) and the contracted balls \(B(x_i,\varepsilon r_i)\) pairwise disjoint, satisfies
\[
\sum_i |f|_{\alpha,B(x_i,r_i)}^p\le C_F.
\]
The claim concerns the sharp endpoint \(\alpha=1-n/p\) and scalar-valued Sobolev functions on \(\mathbb R^n\). It does not assert that the complement is itself linear or closed.

## Proof
Theorem 5.1 of [1] constructs a continuous compactly supported function \(u\in W^{1,p}(\mathbb R^n)\) that does not belong to \(CH_m^{p,\alpha}\). Its construction is a sum of disjoint smooth bumps
\[
u_j(x)=j^{-2/p}s_j^\alpha\,\phi\!\left(\frac{x-q_j}{s_j}\right),
\qquad q_j=M^{-j^2}e_1,\qquad s_j=M^{-2j^2},
\]
for a fixed smooth compactly supported \(\phi\), with \(M\) large. The source verifies
\[
\sum_j\|\nabla u_j\|_{L^p}^p<\infty
\]
and produces, for each large \(j\), \(j\) admissible balls containing the accumulation point \(0\), whose contracted balls are pairwise disjoint and for which
\[
|u|_{\alpha,B}^p\ge c\,j^{-2}
\]
with a constant \(c>0\) independent of \(j\). Consequently the relevant \(p\)-sum dominates \(c\sum_j j^-1\) and diverges.

Because \(u\) has compact support, choose translations \(z_k\in\mathbb R^n\), \(k\ge1\), escaping to infinity so that the sets \(z_k+\operatorname{supp}u\) are pairwise disjoint and have a uniform positive separation. Put
\[
v_k(x)=u(x-z_k).
\]
For \(c=(c_k)\in\ell_p\), define
\[
T(c)=\sum_{k=1}^\infty c_kv_k.
\]
The translated supports are locally finite, so this sum defines a continuous function. They are pairwise disjoint, hence the weak gradient is the locally finite sum of the translated weak gradients and
\[
\|T(c)\|_{W^{1,p}}^p
=\bigl(\|u\|_{L^p}^p+\|\nabla u\|_{L^p}^p\bigr)\sum_{k=1}^\infty |c_k|^p.
\]
Thus \(T\) is a scalar multiple of an isometry from \(\ell_p\) into \(W^{1,p}(\mathbb R^n)\), and its range \(E=T(\ell_p)\) is closed.

It remains to prove that no nonzero vector of \(E\) enters the endpoint class. Let \(c\ne0\), and choose \(k_0\) with \(c_{k_0}\ne0\). Translate the bad-ball families from [1] by \(z_{k_0}\). Their radii tend to zero and all of them contain \(z_{k_0}\). By the positive separation of the translated supports, after discarding finitely many scales every one of these balls misses all supports except \(z_{k_0}+\operatorname{supp}u\). On those balls,
\[
T(c)=c_{k_0}v_{k_0},
\]
so each Hölder coefficient is multiplied by \(|c_{k_0}|\). Taking the compact set \(F=\{z_{k_0}\}\), the same admissible covers therefore have \(p\)-sums bounded below by
\[
|c_{k_0}|^p c\sum_j j^{-1},
\]
which diverges. Hence \(T(c)\notin CH_m^{p,\alpha}\). This holds for every nonzero \(c\in\ell_p\), completing the proof.

## Verification
The argument uses only three ingredients from [1]: the explicit compactly supported endpoint counterexample, the admissibility of its shrinking bad-ball families, and their harmonic-series lower bound. The remaining steps are direct: translation preserves the Sobolev norm and the modified compactly Hölder definition; disjoint supports give the exact \(\ell_p\) norm identity; local finiteness gives continuity; and positive separation localizes the original obstruction inside any selected nonzero coordinate.

The proof is infinite-dimensional rather than computational. No finite experiment is used as evidence for the conclusion. The only normalization dependence is the displayed standard \(p\)-sum Sobolev norm; under any equivalent standard Sobolev norm, the range remains a closed subspace isomorphic to \(\ell_p\).

## Relationship to prior work
Alvarado and Chrontsios Garitsis [1] prove the strict endpoint inclusion by constructing one function in \(W^{1,p}(\mathbb R^n)\cap C(\mathbb R^n)\) outside \(CH_m^{p,1-n/p}\). Their full text contains no statement of spaceability, a closed subspace of endpoint failures, or an \(\ell_p\) copy. The present claim strengthens that strictness statement by showing that the failure set is structurally large: it contains every nonzero vector of a closed infinite-dimensional subspace.

Targeted literature searches for modified compactly Hölder spaceability, closed \(\ell_p\) subspaces of the endpoint gap, and equivalent formulations found general work on spaceability but no statement covering this specific class or implication. A general spaceability theorem could in principle subsume the construction under different terminology; that is the principal residual originality risk.

## Limitations
The result is specific to the Euclidean endpoint counterexample of [1] and to scalar-valued functions. It does not classify all closed subspaces contained in the endpoint gap, does not claim complementedness of \(E\), and does not extend automatically to arbitrary metric-measure spaces or Banach-valued targets. The originality comparison is strongest against the focal paper and the searches described above; an unindexed abstract spaceability criterion applicable to this setting remains a residual risk.

## References
[1] R. Alvarado and E. K. Chrontsios Garitsis, “A purely metric characterization of supercritical Sobolev spaces,” arXiv:2609.24520v1, first public September 21, 2026. Primary MSC 46E36.
