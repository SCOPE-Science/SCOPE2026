# Arbitrarily high-dimensional variation-norm flats in symbolic quasimorphism moduli

## Finding

Let \((\Sigma_A,\sigma)\) be any one-sided topologically mixing subshift of finite type with positive topological entropy. Let \(\mathcal{QM}^{++}(\Sigma_A)\) be the space of positive linearly growing word-quasimorphisms modulo rough similarity, endowed with the symmetrized periodic-length metric \(\mathfrak Q\) of Cantrell–Carrasco–Corso–Rodríguez-Hertz [1]. For **every integer \(k\ge2\)** there is an explicit isometric embedding

\[
\left(\mathbb R^k/\mathbb R\mathbf1,\ \|[t]\|_{\mathrm{var}}=\max_{1\le i\le k}t_i-\min_{1\le i\le k}t_i\right)\longrightarrow \left(\mathcal{QM}^{++}(\Sigma_A),\mathfrak Q\right).
\]

Every point of the embedded flat is represented by a strictly positive locally constant additive potential. In particular, this moduli space contains normed flats of arbitrarily large finite dimension and **is not Gromov hyperbolic**, even when the underlying shift is the full binary shift. The contribution is the exact symbolic realization and its global geometric consequence; the variation-norm geometry of the positive finite-dimensional simplex itself is classical [2].

## Assumptions and scope

The alphabet is finite; \(A\) is a primitive zero-one adjacency matrix; and \(h_{\mathrm{top}}(\Sigma_A)>0\). The latter assures infinitely many distinct periodic orbits. For an admissible finite word \(w\), its length is \(|w|\), and the set of such words is \(\mathcal W\). A word-quasimorphism is a function \(\psi:\mathcal W\to\mathbb R\) with a uniform bound on \(|\psi(uv)-\psi(u)-\psi(v)|\) whenever \(uv\) is admissible. Positive linear growth means \(\psi(w)\ge c|w|-C\) for constants \(c>0\), \(C\ge0\).

For a periodic word \(w\), write \(\overline\psi\{w\}=\lim_{m\to\infty}\psi(w^m)/m\) and define \(\operatorname{Dil}(\phi,\psi)=\sup_{\{w\}\in\mathrm{Per}}\overline\phi\{w\}/\overline\psi\{w\}\). The metric is \(\mathfrak Q([\phi],[\psi])=\log(\operatorname{Dil}(\phi,\psi)\operatorname{Dil}(\psi,\phi))\). Rough similarity identifies classes for which homogenized lengths are proportional. These are the definitions of [1]; the proof below uses no new normalization of that metric.

## Proof

**1. Isolating arbitrary periodic orbit labels.** Choose \(k\) distinct periodic orbits \(O_1,\ldots,O_k\) in \(\Sigma_A\). Every \(O_i\) is finite, and different orbits are disjoint. By the clopen cylinder basis of a one-sided subshift, there exists a common integer \(L\ge1\) and pairwise disjoint clopen sets \(U_2,\ldots,U_k\), each a union of length-\(L\) cylinders, such that \(O_i\subset U_i\) for \(i\ge2\) and the sets avoid every other selected orbit. Set \(U_1=\Sigma_A\setminus\bigcup_{i=2}^kU_i\). Then the \(U_i\) form a clopen partition, and \(O_i\subset U_i\) for all \(i\).

**2. Actual word quasimorphisms.** For each \(t=(t_1,\ldots,t_k)\in\mathbb R^k\), put

\[
g_t(x)=\sum_{i=1}^k e^{t_i}\mathbf1_{U_i}(x),\qquad m_t=\min_i e^{t_i}>0,\quad M_t=\max_i e^{t_i}.
\]

For each admissible word \(w\), choose once and for all an admissible infinite extension \(x_w\) of \(w\), and set \(\psi_t(w)=\sum_{j=0}^{|w|-1}g_t(\sigma^jx_w)\). Clearly \(m_t|w|\le\psi_t(w)\le M_t|w|\). Since \(g_t\) depends only on the first \(L\) symbols, two infinite sequences with the same first \(n\) symbols can have Birkhoff sums over those \(n\) positions differing by at most \(\min(n,L-1)(M_t-m_t)\). For any admissible concatenation \(uv\), comparing the two pieces of \(\psi_t(uv)\) with \(\psi_t(u)\) and \(\psi_t(v)\) therefore gives

\[
|\psi_t(uv)-\psi_t(u)-\psi_t(v)|\le2(L-1)(M_t-m_t).
\]

Thus \(\psi_t\in\mathrm{Qm}^{++}\); when \(L=1\), the defect is zero. For a periodic word \(w\) of length \(n\), the first \(mn\) symbols of \(x_{w^m}\) agree with those of \(w^\infty\). The difference of their Birkhoff sums is uniformly bounded by \((L-1)(M_t-m_t)\), independently of \(m\). Hence

\[
\overline{\psi_t}\{w\}=\sum_{j=0}^{n-1}g_t(\sigma^jw^\infty).
\]

**3. Exact dilation, including attainment.** Let \(N_i(w)\) count how often the periodic orbit \(w^\infty\), during one period of length \(n\), lies in \(U_i\). Then \(N_i(w)\ge0\), \(\sum_iN_i(w)=n\), and

\[
\frac{\overline{\psi_t}\{w\}}{\overline{\psi_s}\{w\}}=\frac{\sum_iN_i(w)e^{t_i}}{\sum_iN_i(w)e^{s_i}}=\sum_i\frac{N_i(w)e^{s_i}}{\sum_jN_j(w)e^{s_j}}\,e^{t_i-s_i}.
\]

This is a convex combination of \(e^{t_i-s_i}\), so it belongs to the closed interval whose endpoints are their minimum and maximum. For a periodic orbit \(O_i\) selected in Step 1, all of its points lie in \(U_i\): hence \(N_i=n\) and the displayed ratio is **exactly** \(e^{t_i-s_i}\). Both extrema occur among the selected periodic orbits. Therefore

\[
\operatorname{Dil}(\psi_t,\psi_s)=e^{\max_i(t_i-s_i)},\qquad \operatorname{Dil}(\psi_s,\psi_t)=e^{-\min_i(t_i-s_i)},
\]

and consequently

\[
\boxed{\mathfrak Q([\psi_t],[\psi_s])=\max_i(t_i-s_i)-\min_i(t_i-s_i).}
\]

Adding \(c\mathbf1\) to \(t\) multiplies \(g_t\) and \(\psi_t\) by \(e^c\), so the map descends to \(\mathbb R^k/\mathbb R\mathbf1\). Conversely zero distance forces all components of \(t-s\) to agree, so this quotient map is injective. It is isometric for all parameter values, not merely near the origin.

**4. Failure of Gromov hyperbolicity.** Use \(k=3\). For arbitrary \(R>0\), in the variation-norm plane write \(0\), \(u=(R,0,0)\), \(v=(0,-R,0)\), and \(u+v=(R,-R,0)\), understood modulo constants. The three four-point pairing sums are

\[
 d(0,u+v)+d(u,v)=3R,\quad d(0,u)+d(u+v,v)=2R,\quad d(0,v)+d(u+v,u)=2R.
\]

Any \(\delta\)-hyperbolic metric space in the four-point sense has the largest sum at most the second-largest plus \(2\delta\). Here this would force \(R\le2\delta\) for every \(R>0\), an impossibility. Since the embedding preserves distances, the same four-point obstruction holds in \(\mathcal{QM}^{++}(\Sigma_A)\). This proves the entire claim. \(\square\)

## Verification

The key checks are symbolic and quantified in the proof: the cylinder partition exists for every finite selection of distinct periodic orbits, the defect bound is uniform over all admissible concatenations, periodic homogenization is exact, and the dilation extrema are attained at explicitly selected periodic orbits. These checks establish the infinite-dimensional family without computational extrapolation.

As a separate finite sanity test, `verify.py` treats the full binary shift and the three-orbit partition \(U_2=[111]\), \(U_3=[010]\cup[101]\), \(U_1=\Sigma\setminus(U_2\cup U_3)\). It enumerates all periodic binary words of lengths \(1\) to \(12\) for two positive integer weight pairs, uses exact rational arithmetic for all ratios, and verifies that the coordinate extrema are reached by the three designated periodic orbits. The test cannot by itself establish the theorem for all mixing shifts or all \(k\).

## Relationship to prior work

Cantrell, Carrasco, Corso and Rodríguez-Hertz [1, Definition 1.1; §2.3; §§5.1, 5.4–5.5] define precisely this symmetrized metric, prove contractibility, unboundedness, separability, incompleteness, density of locally constant representatives, and construct pressure geodesics. In particular, their locally constant density theorem alone does not entail any exact finite-dimensional isometric flat: metric density supplies approximation, not a distance-realizing embedding. Their bi-infinite pressure geodesics likewise do not imply simultaneous normed planes or non-hyperbolicity.

The Hilbert metric of an open simplex is classically a normed-vector-space geometry [2, Theorem 1, citing de la Harpe and Nussbaum]. That background explains the variation formula once all coordinate-ratio extrema are known; it is **not** claimed anew. What is established here is that, for every fixed positive-entropy mixing subshift, arbitrarily many periodic orbits can be isolated by one clopen partition so that *every other periodic orbit remains inside those same coordinate bounds*. This enforces an exact Hilbert-simplex isometry inside the dynamical moduli rather than just an analogy with a positive cone.

## Limitations

This is a metric embedding theorem, not a claim that the full moduli space is a Banach space, that its pressure geodesics are unique, or that the image is a convex subset under every natural coordinate system. The positive-entropy hypothesis supplies the arbitrarily many distinct periodic orbits needed for the construction. The result does not quantify defects uniformly in \(k\) or across unbounded parameter values. The possible appearance of a stronger equivalent construction in other work on Hilbert projective metrics or thermodynamic potentials is a historical-priority risk; no independent mathematical audit has been performed.

## References

[1] S. Cantrell, P. D. Carrasco, E. Corso and F. Rodríguez-Hertz, *The moduli space of quasimorphisms on subshifts and its pressure geometry*, arXiv:2610.26778v1, publicly posted 2026-10-19, https://arxiv.org/html/2610.26778v1 .

[2] T. Foertsch and A. Karlsson, *Hilbert metrics and Minkowski norms*, arXiv:math/0407197v1 (2004), Theorem 1 and its cited predecessors, https://arxiv.org/abs/math/0407197 .
