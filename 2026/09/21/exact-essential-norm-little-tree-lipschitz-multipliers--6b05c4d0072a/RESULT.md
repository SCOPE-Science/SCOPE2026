# Exact essential norms for multipliers on little weighted Lipschitz spaces of rooted trees

## Result

Let \(T\) be an infinite locally finite rooted tree with root \(o\), let
\(T^*=T\setminus\{o\}\), and write \(v^-\) for the parent of \(v\in T^*\).
Fix positive edge weights \(c_v>0\) for \(v\in T^*\), and define
\[
\Delta f(v)=f(v)-f(v^-),\qquad
\mathcal L_{c,0}(T)=
\left\{f:T\to\mathbb C:\ c_v|\Delta f(v)|\longrightarrow0
\text{ as }|v|\to\infty\right\}.
\]
Equip this space either with
\[
\|f\|_{\max}=
\max\left\{|f(o)|,\sup_{v\in T^*}c_v|\Delta f(v)|\right\}
\]
or with the original sum-type norm
\[
\|f\|_{+}=
|f(o)|+\sup_{v\in T^*}c_v|\Delta f(v)|.
\]
For \(v\in T^*\), put
\[
H_c(v)=
\sum_{\substack{w\in[o,v^-]\\w\neq o}}\frac1{c_w},
\]
with the empty sum equal to \(0\).

Let \(M_\psi f=\psi f\) be bounded on \(\mathcal L_{c,0}(T)\).
Then its essential norm is given exactly by

\[
\boxed{
\|M_\psi\|_{e,\max}
=
\limsup_{|v|\to\infty}
\left(
|\psi(v)|
+c_v|\Delta\psi(v)|\,[1+H_c(v)]
\right)
}
\tag{1}
\]

and

\[
\boxed{
\|M_\psi\|_{e,+}
=
\limsup_{|v|\to\infty}
\max\left\{
c_v|\Delta\psi(v)|,\,
|\psi(v)|+c_v|\Delta\psi(v)|H_c(v)
\right\}.
}
\tag{2}
\]

The formulas apply to arbitrary positive edge weights.  They concern the little
spaces; no corresponding claim is made here for the nonseparable big
Lipschitz spaces.

## Proof

Define weighted difference coordinates by
\[
J_cf=
\bigl(x_o,(x_v)_{v\in T^*}\bigr),\qquad
x_o=f(o),\quad x_v=c_v\Delta f(v).
\]
For every \(v\), the root-to-\(v\) path is finite, so
\[
f(v)=x_o+
\sum_{\substack{w\in[o,v]\\w\neq o}}\frac{x_w}{c_w}.
\]
Hence \(J_c\) is an isometric isomorphism from
\((\mathcal L_{c,0}(T),\|\cdot\|_{\max})\) onto \(c_0(T)\), and from
\((\mathcal L_{c,0}(T),\|\cdot\|_+)\) onto
\(\mathbb C\oplus_1c_0(T^*)\).

Write \(\delta_v=\psi(v)-\psi(v^-)\).  For \(v\in T^*\),
\[
\begin{aligned}
[J_cM_\psi J_c^{-1}x]_v
&=c_v\bigl(\psi(v)f(v)-\psi(v^-)f(v^-)\bigr)\\
&=\psi(v)x_v
+c_v\delta_v x_o
+c_v\delta_v
\sum_{\substack{w\in[o,v^-]\\w\neq o}}\frac{x_w}{c_w}.
\end{aligned}
\tag{3}
\]
Thus the \(v\)-th row functional has norm
\[
|\psi(v)|+c_v|\delta_v|\,[1+H_c(v)]
\tag{4}
\]
on \(c_0(T)\).  On
\(\mathbb C\oplus_1c_0(T^*)\), whose dual is
\(\mathbb C\oplus_\infty\ell_1(T^*)\), the same row has norm
\[
\max\left\{
c_v|\delta_v|,\,
|\psi(v)|+c_v|\delta_v|H_c(v)
\right\}.
\tag{5}
\]

It remains to identify the essential norm from the tail row norms.  We use the
following elementary coordinate lemma.

**Tail-row lemma.**  Let \(E=c_0(T)\), or
\(E=\mathbb C\oplus_1c_0(T^*)\), and let \(A:E\to E\) be bounded.  If
\(\rho_v=e_v^*A\) denotes its \(v\)-th non-root row functional, then
\[
\|A\|_e=\limsup_{|v|\to\infty}\|\rho_v\|.
\tag{6}
\]

Indeed, let \(P_N\) retain the root and the coordinates with \(|v|\le N\).
Local finiteness makes \(P_NA\) finite rank, and
\[
\|A-P_NA\|=\sup_{|v|>N}\|\rho_v\|,
\]
which gives the upper bound in (6).  Conversely, if \(K:E\to E\) is compact,
then the coordinate rows \(e_v^*K\) converge to \(0\) in norm as
\(|v|\to\infty\): equivalently, compact subsets of the \(c_0\)-part have
uniformly small coordinate tails.  Therefore
\[
\|A-K\|
\ge \|\rho_v-e_v^*K\|
\ge \|\rho_v\|-\|e_v^*K\|,
\]
and taking the radial limsup and then the infimum over compact \(K\) gives the
reverse inequality.  Applying (6) to the row norms (4) and (5) proves
(1) and (2).

## Classical little Lipschitz space

For the ordinary little Lipschitz space, \(c_v=1\).  Then
\(H_c(v)=|v|-1\), so (1) becomes
\[
\|M_\psi\|_{e,\max}
=
\limsup_{|v|\to\infty}
\left(|\psi(v)|+|v|\,|\Delta\psi(v)|\right).
\tag{7}
\]
Under the sum norm, (2) is eventually
\[
\limsup_{|v|\to\infty}
\left(|\psi(v)|+(|v|-1)|\Delta\psi(v)|\right).
\]
Boundedness of the multiplier implies
\(|v||\Delta\psi(v)|=O(1)\), hence
\(|\Delta\psi(v)|\to0\); consequently the two displayed essential norms are
equal, and both are given by the right side of (7).

This sharpens the earlier essential-norm estimates for tree Lipschitz
multipliers while remaining consistent with their compactness criterion.

## Weighted little Lipschitz space of Allen--Colonna--Easley

For the weighted space
\[
\|f\|_{\mathbf w}
=
|f(o)|+\sup_{v\in T^*}|v|\,|\Delta f(v)|,
\]
take \(c_v=|v|\).  If \(n=|v|\), then
\[
H_c(v)=H_{n-1}:=\sum_{k=1}^{n-1}\frac1k.
\]
For \(n\ge2\), the second entry of the maximum in (2) dominates the first.
Therefore every bounded multiplier on the little weighted space satisfies

\[
\boxed{
\|M_\psi\|_e
=
\limsup_{|v|\to\infty}
\left(
|\psi(v)|
+|v|H_{|v|-1}\,|\Delta\psi(v)|
\right).
}
\tag{8}
\]

The 2013 theorem of Allen, Colonna and Easley gives the boundedness condition
\[
\psi\in\ell_\infty(T),\qquad
\sup_{v\in T^*}|v|\log|v|\,|\Delta\psi(v)|<\infty,
\]
and their essential-norm estimates are
\[
\max\{A(\psi),B(\psi)\}
\le \|M_\psi\|_e
\le A(\psi)+B(\psi),
\]
where
\[
A(\psi)=\limsup_{|v|\to\infty}|\psi(v)|,\qquad
B(\psi)=\limsup_{|v|\to\infty}|v|\log|v|\,|\Delta\psi(v)|.
\]
Since \(H_{n-1}/\log n\to1\), formula (8) gives the exact quantity lying
between those two bounds.  It retains whether the two tail contributions peak
along the same vertices, information that the pair \((A(\psi),B(\psi))\)
alone does not encode.

The equivalent max renorm used in later work has the row expression
\[
|\psi(v)|+|v|\,[1+H_{|v|-1}]\,|\Delta\psi(v)|.
\]
The boundedness condition above implies
\(|v||\Delta\psi(v)|\to0\), so it has the same essential norm (8).

As a consistency check, (8) vanishes exactly when
\[
\psi(v)\to0,\qquad
|v|\log|v|\,|\Delta\psi(v)|\to0,
\]
recovering the known compactness characterization on the little weighted
space.

## Context and originality

The coordinate tail-row lemma is standard Banach-space technology and is not
claimed as new.  The scientific contribution claimed here is the exact
essential-norm formula for multiplication operators on the little weighted
tree Lipschitz spaces, including the arbitrary positive-edge-weight form
(1)--(2) and the harmonic-number specialization (8).

Colonna and Easley (2010) characterized boundedness and compactness for
multipliers on the tree Lipschitz and little Lipschitz spaces and gave
essential-norm estimates.  Allen, Colonna and Easley (2013) did the same for
the weighted space and explicitly proved the lower/upper bounds above rather
than an exact formula.  López-Martínez (2026) identified the little Lipschitz
space isometrically with \(c_0(T)\) under an equivalent max norm and used that
identification to obtain exact operator norms, but the paper does not state an
essential-norm formula.  Issa-Barbará and Martínez-Avendaño (2026) extended
the graph setting and likewise described their essential-norm results as
estimates.

To the best of our knowledge, the exact formulas (1), (2), and (8) have not
previously been stated.  A residual literature risk remains from Rachel
Locke's 2016 dissertation on multiplication operators in infinite-graph
settings and the cited 2023 Colonna--Locke preprint, neither of which was
available here in sufficiently inspectable full text.  Those sources are most
relevant to the ordinary graph/tree specialization; they are less directly
targeted at the arbitrary weighted-tree formula above.

## Limitations

1. The theorem is for the little spaces, whose weighted-difference coordinate
   models are \(c_0\)-type spaces.  It does not assert the same essential norm
   for the corresponding big spaces modeled on \(\ell_\infty\).
2. Boundedness of \(M_\psi\) is assumed in the general weighted statement.
   Existing special-space results provide concrete boundedness criteria.
3. Originality is to the best of our knowledge; the two older sources noted
   above remain the principal unresolved literature risk.

## References

1. F. Colonna and G. R. Easley, *Multiplication Operators on the Lipschitz
   Space of a Tree*, Integral Equations and Operator Theory 68 (2010),
   391--411. DOI: 10.1007/s00020-010-1824-5.
2. R. F. Allen, F. Colonna and G. R. Easley, *Multiplication Operators on the
   Weighted Lipschitz Space of a Tree*, Journal of Operator Theory 69 (2013),
   209--231. DOI: 10.7900/jot.2010sep22.1885.
3. R. F. Allen, F. Colonna and G. R. Easley, *Multiplication Operators on the
   Iterated Logarithmic Lipschitz Spaces of a Tree*, Mediterranean Journal of
   Mathematics 9 (2012). DOI: 10.1007/s00009-011-0157-1.
4. A. López-Martínez, *Frequently Hypercyclic Composition Operators on The
   Little Lipschitz Space of A Rooted Tree*, Mediterranean Journal of
   Mathematics 23, 87 (2026). DOI: 10.1007/s00009-026-03075-6.
5. J. A. Issa-Barbará and R. A. Martínez-Avendaño, *Multiplication Operators
   on the Lipschitz Space of an Infinite Graph*, Boletín de la Sociedad
   Matemática Mexicana 32, 27 (2026). DOI: 10.1007/s40590-026-00859-4.
