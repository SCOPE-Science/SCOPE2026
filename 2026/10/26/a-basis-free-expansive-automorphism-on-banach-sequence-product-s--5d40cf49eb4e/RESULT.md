# A basis-free expansive automorphism on Banach–sequence product spaces with a sharp scalar boundary

## Finding
Let \(\mathbb K\) be \(\mathbb R\) or \(\mathbb C\), let \(\omega=\mathbb K^{\mathbb N}\) with its product Fréchet topology, and let \(E\) be any Banach space containing a complemented closed subspace linearly isomorphic to \(\ell_\infty(\Gamma)\), for an infinite index set \(\Gamma\). There is an explicit family \((T_\lambda)_{\lambda\in\mathbb K\setminus\{0\}}\) of continuous linear automorphisms of \(E\oplus\omega\) with the **exact phase equivalence**

\[
T_\lambda\text{ is metrically positively expansive}\quad\Longleftrightarrow\quad
T_\lambda\text{ is metrically expansive}\quad\Longleftrightarrow\quad |\lambda|>1.
\]

Here metric expansivity refers to any compatible translation-invariant metric; the equivalence does not depend on the particular compatible invariant metric. In particular, \(\ell_\infty(\Gamma)\oplus\omega\) supports an invertible metrically positively expansive linear operator for every infinite \(\Gamma\). Conversely, for finite \(\Gamma\), no metrically expansive linear automorphism exists on \(\ell_\infty(\Gamma)\oplus\omega\), by the cited nonexistence theorem for \(\omega\). Thus the existence question for this natural cardinal family has the exact boundary of finite versus infinite \(\Gamma\).

The stronger structural statement is the following *exact orbit formula*. Choose a complemented splitting \(E=M\oplus Y\), identify \(M\) with \(\ell_\infty(\Gamma)\), and choose an injective isometry \(S:M\to M\) with one-dimensional coordinate defect, as in the proof. Writing \(w=(w_1,w_2,\ldots)\), the \(M\)-component of the forward orbit of \((m+y,w)\) satisfies for every integer \(n\ge1\)

\[
\big\|P_M T_\lambda^n(m+y,w)\big\|_\infty
=\max\left\{ |\lambda|^n\|m\|_\infty,
\max_{1\le j\le n}|\lambda|^{n-j}|w_j|\right\},
\]

while its \(Y\)-component equals \(\lambda^n y\) and its sequence component is \((w_{n+1},w_{n+2},\ldots)\). Here \(P_M\) denotes the splitting-coordinate projection onto \(M\), followed by the fixed identification with \(\ell_\infty(\Gamma)\).

## Assumptions and scope
An *automorphism* is a continuous linear bijection with continuous inverse. For a compatible translation-invariant metric \(d\), an automorphism \(T\) is *metrically expansive* if some \(c>0\) satisfies: for each nonzero \(z\), some integer \(n\in\mathbb Z\) has \(d(T^nz,0)\ge c\); it is *positively expansive* if such an \(n\) can always be taken nonnegative. Equivalent definitions for two distinct initial points follow by linearity. The topology of \(E\oplus\omega\) is its finite product topology, independent of the particular equivalent norm on \(E\). Choose seminorms

\[
p_k(m+y,w)=\max\{\|m\|_\infty,\|y\|_Y,|w_1|,\ldots,|w_k|\},\qquad k\ge1,
\]

and the compatible invariant metric \(d(z,z')=\sum_{k\ge1}2^{-k}\min\{1,p_k(z-z')\}\). Any two compatible translation-invariant metrics on a topological vector space induce the same uniformity, so expansivity is metric-independent within this class. We make no claim for non-translation-invariant compatible metrics.

The first-source problem concerns topological vector spaces without continuous norms: \(E\oplus\omega\) is such a space, since every continuous seminorm vanishes on some nonzero tail vector in the \(\omega\)-factor.

## Proof
**1. The one-coordinate defect isometry.** Because \(\Gamma\) is infinite, select distinct \(\gamma_1,\gamma_2,\ldots\) in \(\Gamma\). (The countable choice required here is part of the usual ZFC setting.) Let \(e\) denote the unit-coordinate function at \(\gamma_1\), and define

\[
(Sm)(\gamma_1)=0,\qquad (Sm)(\gamma_{j+1})=m(\gamma_j),\qquad
(Sm)(\gamma)=m(\gamma)\quad(\gamma\notin\{\gamma_j:j\ge1\}).
\]

Then \(S\) is an isometry for the supremum norm and its range is the codimension-one subspace whose \(\gamma_1\)-coordinate vanishes. Define a bounded left inverse \(L\) by \((Lv)(\gamma_j)=v(\gamma_{j+1})\) and \((Lv)(\gamma)=v(\gamma)\) outside the chosen ray. Hence \(LS=I\), \(Le=0\), and \(SLv=v-v(\gamma_1)e\). Moreover, for all scalars \(t\),

\[
\|Sm+te\|_\infty=\max\{\|m\|_\infty,|t|\}.
\]

**2. The explicit automorphism.** Let \(B(w_1,w_2,\ldots)=(w_2,w_3,\ldots)\). Given \(\lambda\ne0\), set

\[
T_\lambda(m+y,w)=\big(\lambda Sm+w_1e+\lambda y,\ Bw\big).
\]

The two components of the first entry lie respectively in \(M\) and \(Y\). Direct substitution, using the preceding identities, shows that

\[
T_\lambda^{-1}(m+y,w)=\big(\lambda^{-1}Lm+\lambda^{-1}y,\ (m(\gamma_1),w_1,w_2,\ldots)\big).
\]

Both maps are continuous for the indicated product topology, proving the automorphism claim.

**3. Exact orbit decomposition.** Induction gives, for \(n\ge1\),

\[
P_MT_\lambda^n(m+y,w)
=\lambda^nS^nm+\sum_{j=1}^n\lambda^{n-j}w_jS^{n-j}e.
\]

The first summand vanishes at \(\gamma_1,\ldots,\gamma_n\); the vectors \(S^{n-j}e\), for \(j=1,\ldots,n\), occupy those \(n\) distinct coordinates. The supremum norm of this disjointly supported sum is consequently exactly the maximum in the Finding. The \(Y\) and sequence components follow from the definition.

**4. Sharp expansivity threshold.** Suppose \(|\lambda|>1\). For any nonzero \((m+y,w)\), if \(m\ne0\) or \(y\ne0\), its corresponding Banach-component norm grows at least geometrically. If both vanish, choose any index \(j\) with \(w_j\ne0\); the exact orbit formula then gives the lower bound \(|\lambda|^{n-j}|w_j|\) for all \(n\ge j\). Thus every nonzero forward orbit eventually has \(p_1\) at least \(1\), so \(d(T_\lambda^nz,0)\ge1/2\) for some \(n\ge0\). This is positive metric expansivity, and implies two-sided expansivity.

If \(0<|\lambda|\le1\), take \(z=(e,0_Y,0_\omega)\). For \(n\ge0\), \(T_\lambda^nz=(\lambda^nS^ne,0,0)\), while for each \(h\ge1\) we have \(T_\lambda^{-h}z=(0,0,e_h)\), with \(e_h\) the \(h\)-th standard coordinate in \(\omega\). Hence \(p_k(T_\lambda^nz)\le1\) for **all** \(n\in\mathbb Z\), all \(k\), and all \(\lambda\) in this range. For any \(0<\varepsilon<1\), the nonzero vector \(\varepsilon z\) has \(d(T_\lambda^n\varepsilon z,0)\le\varepsilon\) simultaneously for every integer \(n\). There is therefore no two-sided expansivity constant. This proves both equivalences.

**5. The finite-cardinality boundary.** When \(\Gamma\) is finite, \(\ell_\infty(\Gamma)\oplus\omega\) is topologically linearly isomorphic to \(\omega\). López-Martínez and Menet prove that no automorphism of \(\omega\) is metrically expansive; equivalently, one may use the independent nonexistence result of Wu and Wang. These results exclude all automorphisms in the finite case, not just the constructed family.

## Verification
The proof is symbolic and covers every real or complex parameter \(\lambda\ne0\), every infinite index set \(\Gamma\), arbitrary complemented embeddings, and all initial vectors. The included standalone `CHECK.py` verifies the inverse formulas, the disjoint-support maximum identity, and the forward component formulas on finitely supported coordinate models. Running it produced **21,600 passed consistency assertions** from 1,200 deterministic complex tests; the tests are not used to infer the infinite-dimensional conclusions. The exact norm and inverse identities above supply the analytical verification.

## Relationship to prior work
López-Martínez and Menet (2026, Theorems 3.1–3.2) prove existence of metrically expansive automorphisms on \(X\oplus\omega\) under a *complemented Schauder basic sequence* hypothesis in the Banach summand. Their Proposition 3.4 covers \(\omega(X)\) for \(X=\ell^p\), \(1\le p<\infty\), or \(c_0\), and their Problem 3.5 calls for a classification of \(X\oplus\omega\). The statement proved here supplies a distinct sufficient condition based on an infinitely self-similar, nonseparable complemented \(\ell_\infty\) space, and an exact scalar threshold, without requiring a basic sequence in that complemented part. In particular, \(\ell_\infty\) has no infinite-dimensional separable complemented subspace, so the paper's basic-sequence hypothesis cannot explain this instance directly. The proof nonetheless uses the same broad principle of transferring coordinates from the nonnormable sequence factor into an expanding Banach component; it should not be construed as independent of that conceptual mechanism.

Bernardes–Caraballo–Darji–Fávaro–Peris (2024) study *topological* expansivity and weighted shifts for other Fréchet settings; metric expansivity is a stricter notion here. Wu–Wang (2026) rule out metrically expansive operators on countable products of finite-dimensional spaces, a result consistent with the finite-cardinality boundary. A related exact result concerns shifts on a mixed \(\ell^p\)-and-product Fréchet space for finite \(p\); the present assertion concerns complemented \(\ell_\infty\) components and the exact coordinate-defect automorphism.

## Limitations
This is a sufficient criterion, not a characterization of all Banach spaces \(E\) for which \(E\oplus\omega\) admits an expansive automorphism. The sharp scalar transition concerns the *specified constructed family*, not arbitrary operators on those spaces. The finite-versus-infinite statement is only for the family \(E=\ell_\infty(\Gamma)\). The exact forward-orbit identity uses the selected isometric model of the complemented subspace, not the original ambient Banach norm. No hypercyclicity, generalized hyperbolicity, shadowing, or stability theorem is claimed. An overlooked older coordinate-interface construction may establish an equivalent sufficiency statement; historical priority is not independently certified.

## References
1. A. López-Martínez and Q. Menet, *Expansive operators on Fréchet spaces without continuous norm*, arXiv:2610.19954v1, publicly submitted 14 October 2026, Sections 2–3.
2. N. C. Bernardes Jr., B. M. Caraballo, U. B. Darji, V. V. Fávaro and A. Peris, *Generalized Hyperbolicity, Stability and Expansivity for Operators on Locally Convex Spaces*, arXiv:2403.02843v2 (2024), Sections 4–5.
3. X. Wu and G. Wang, *Shadowing and metric expansivity on Fréchet spaces*, arXiv:2607.28705v1 (2026), nonexistence on countable products of finite-dimensional factors.
4. *Banach space*, Encyclopedia of Mathematics, subsection “Non-complementable subspaces,” for the classical fact that infinite-dimensional separable subspaces of the bounded-sequence space are not complemented.
