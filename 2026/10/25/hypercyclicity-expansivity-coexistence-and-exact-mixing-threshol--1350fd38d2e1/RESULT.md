# Hypercyclicity–expansivity coexistence and exact mixing thresholds on a mixed Fréchet shift

## Finding

Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\), \(1\le p<\infty\), and define
\[
E_p=\ell^p(\{j\in\mathbb Z:j\le0\})\oplus\mathbb K^{\{j\ge1\}},
\]
with the norm topology in the left summand and coordinatewise convergence in the right summand. For every nonzero scalar weight sequence satisfying
\[
0<a:=\inf_{j\le0}|w_j|\le\sup_{j\le0}|w_j|=:b<\infty,
\]
define the bilateral weighted backward shift by \((T_wx)_j=w_{j+1}x_{j+1}\), and let
\[
P_n=\prod_{j=-n+1}^0|w_j|,\qquad n\ge1.
\]
Then \(T_w\) is a continuous linear automorphism with continuous inverse, and the following are equivalent descriptions of its dynamics:

1. \(T_w\) is **hypercyclic** (has a dense forward orbit) exactly when \(\liminf_{n\to\infty}P_n=0\).
2. \(T_w\) is **topologically mixing** exactly when \(P_n\to0\).
3. \(T_w\) is **positively expansive in the metric sense** (for every compatible translation-invariant metric) exactly when \(\sup_{n\ge1}P_n=\infty\).

In particular, hypercyclicity and positive metric expansivity coexist exactly when
\[
\liminf_{n\to\infty}P_n=0,\qquad\limsup_{n\to\infty}P_n=\infty.
\]
Such an automorphism cannot be topologically mixing.

## Assumptions and scope

The result holds over both scalar fields, for every finite \(p\ge1\). Positive expansivity means that there is a constant \(c>0\) such that each nonzero difference \(x-y\) has some forward iterate separated by at least \(c\) in a fixed compatible translation-invariant metric. This does **not** mean uniform positive expansivity in the stronger operator-theoretic sense. No restriction is imposed on the nonzero weights at positive indices.

A defining sequence of continuous seminorms is
\[
q_h(x)=\left(\sum_{j\le0}|x_j|^p\right)^{1/p}+\max_{1\le j\le h}|x_j|,\qquad h\ge1,
\]
which produces a compatible translation-invariant metric \(d(x,y)=\sum_{h\ge1}2^{-h}\min\{1,q_h(x-y)\}\).

## Proof

**Automorphism.** For \(j\le-1\), the coordinate \((T_wx)_j\) is a boundedly weighted copy of an existing negative coordinate; the remaining negative coordinate is \((T_wx)_0=w_1x_1\). Thus \(T_w:E_p\to E_p\) is continuous. Its inverse is
\[
(T_w^{-1}x)_j=\frac{x_{j-1}}{w_j},\qquad j\in\mathbb Z.
\]
The lower bound on negative-index weights controls the inverse on the norm summand, and the positive coordinates have the product topology, so the inverse is continuous.

**Comparability of individual amplitudes.** For each fixed \(k\in\mathbb Z\), the coefficient initially at index \(k\) moves to index \(k-n\) with modulus multiplied by
\[
Q_{n,k}=\prod_{r=k-n+1}^k|w_r|.
\]
For all sufficiently large \(n\), there are constants \(0<c_k\le C_k<\infty\), independent of \(n\), such that
\[
c_kP_n\le Q_{n,k}\le C_kP_n.
\]
Indeed, canceling common factors in the two products leaves only finitely many fixed positive-index factors and at most \(|k|\) negative-index factors (or their reciprocals), all bounded above and below by \(a\) and \(b\). Every nonzero \(x\) has at least one nonzero fixed coordinate \(x_k\). Once \(n\ge k\), that coordinate reaches the \(\ell^p\) summand, so
\[
\|(T_w^nx)_{j\le0}\|_p\ge |x_k|Q_{n,k}\ge c_k|x_k|P_n.
\]

**Positive expansivity.** If \(\sup_nP_n=\infty\), the preceding lower bound shows that \(\sup_nq_1(T_w^nx)=\infty\) for every nonzero \(x\). Therefore some iterate has \(d(T_w^nx,0)\ge1/2\), uniformly over nonzero \(x\); translation invariance gives metric positive expansivity. Conversely, if \(P_n\) is bounded, \(T_w^ne_0\) has only the coordinate at \(-n\), with norm \(P_n\). Scaling \(e_0\) by an arbitrarily small nonzero scalar keeps its entire forward orbit in any prescribed metric ball, contradicting positive expansivity.

**Hypercyclicity.** Suppose \(\liminf_nP_n=0\). Choose an increasing sequence \(n_r\) with \(P_{n_r}\to0\). Finite-support sequences form a dense subset \(D\) of \(E_p\). For each \(u\in D\), the amplitude comparison shows \(T_w^{n_r}u\to0\) in the norm/product topology. For each \(v\in D\), \(T_w^{-n_r}v\to0\): after sufficiently many inverse shifts all nonzero coordinates lie strictly in the positive-index product component and escape every fixed finite coordinate window. Hence, for any \(u,v\in D\),
\[
z_r=u+T_w^{-n_r}v\to u,\qquad T_w^{n_r}z_r=T_w^{n_r}u+v\to v.
\]
This is the transitivity criterion; since \(E_p\) is separable, complete, metrizable, and has no isolated points, Birkhoff's transitivity theorem gives a hypercyclic vector.

Conversely, if \(x\) is hypercyclic, its forward orbit visits arbitrarily small neighborhoods of zero at arbitrarily large times: take any decreasing neighborhood basis at zero and use the fact that every tail of a dense orbit is dense. Choose a fixed \(k\) with \(x_k\ne0\). Along some \(n_r\to\infty\), the norm of the negative-coordinate projection of \(T_w^{n_r}x\) tends to zero. The same lower bound forces \(P_{n_r}\to0\).

**Mixing.** If \(P_n\to0\), the two finite-support convergence assertions just proved hold as \(n\to\infty\), not merely along a subsequence, so the displayed transitivity construction gives the mixing property. Conversely, assume mixing. Choose the open set \(U=\{x:|x_0-1|<1/2\}\) and, for \(\varepsilon>0\), \(V_\varepsilon=\{y:\|(y_j)_{j\le0}\|_p<\varepsilon\}\). For every sufficiently large \(n\), mixing supplies \(x\in U\) with \(T_w^nx\in V_\varepsilon\). Its coordinate at \(-n\) has modulus \(P_n|x_0|>P_n/2\); hence \(P_n<2\varepsilon\) for all sufficiently large \(n\). Since \(\varepsilon\) is arbitrary, \(P_n\to0\).

**Coexistence example.** Take \(w_j=1\) for all \(j\ge1\). Moving leftward from \(j=0\), divide the remaining weights into consecutive blocks of lengths \(2,4,6,8,\ldots\). Give block number \(r\) the constant weight \(2\) when \(r\) is odd and \(1/2\) when \(r\) is even. At the end of block \(2m-1\) the product is \(P_n=2^{2m}\); at the end of block \(2m\) it is \(P_n=2^{-2m}\). Therefore the same bounded-weight automorphism is both hypercyclic and positively metric expansive, but not mixing.

## Verification

The weight-product comparison is exact, based on cancellation of finitely many factors. The endpoint block products were checked by the identities \(\sum_{r=1}^{2m-1}(-1)^{r+1}2r=2m\) and \(\sum_{r=1}^{2m}(-1)^{r+1}2r=-2m\). The proofs of hypercyclicity and mixing use dense finite-support sequences and convergence in each defining seminorm. All claims are infinite-dimensional analytical arguments; finite examples alone would not prove the equivalences.

## Relationship to prior work

López-Martínez and Menet (2026, arXiv:2610.19954v1, Section 3) construct invertible positively expansive maps on \(\ell^p\oplus\omega\), including the constant-expansion shift; their stated results do not classify hypercyclicity and mixing in the variable-weight family or exhibit this coexistence regime. Bernardes et al. (2024/2025, arXiv:2403.02843, Theorem 42) give a general topological-expansivity characterization for weighted shifts on Fréchet sequence spaces, which explains one part of the weight-product condition. Bernardes, Martínez-Giménez, and Rodenas (2025, arXiv:2509.12410v1) separately study average and uniform expansivity; their notions should not be conflated with the metric positive expansivity here. The dense-orbit argument uses standard Birkhoff transitivity principles. The combined sharp three-way phase diagram and explicit coexistence example are the present claim, subject to historical-priority checking.

## Limitations

The theorem is confined to this mixed norm/product Fréchet space and the indicated bilateral weighted shifts. It does not claim that positive expansivity and hypercyclicity can coexist for every Fréchet space, nor does it assert uniform positive expansivity, frequent hypercyclicity, distributional chaos, or any Schatten/spectral classification. General weighted-shift theorems may subsume some separate equivalences; the synthesis and coexistence should receive independent literature review.

## References

- A. López-Martínez and Q. Menet, *Expansive operators on Fréchet spaces without continuous norm*, arXiv:2610.19954v1 (public 2026-10-14), Section 3. https://arxiv.org/html/2610.19954v1
- N. C. Bernardes Jr., B. M. Caraballo, U. B. Darji, V. V. Fávaro and A. Peris, *Generalized hyperbolicity, stability and expansivity for operators on locally convex spaces*, arXiv:2403.02843; J. Funct. Anal. 288 (2025), 110696, especially Theorem 42.
- N. C. Bernardes Jr., F. Martínez-Giménez and F. Rodenas, *On notions of expansivity for operators on locally convex spaces*, arXiv:2509.12410v1 (public 2025-09-15), Sections 1–4.
- G. D. Birkhoff's topological transitivity theorem, standard Baire-category form for continuous linear operators on separable Fréchet spaces.
