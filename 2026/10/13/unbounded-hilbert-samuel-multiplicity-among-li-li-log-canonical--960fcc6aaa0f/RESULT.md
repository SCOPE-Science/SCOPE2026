# Unbounded Hilbert--Samuel multiplicity among Li--Li log canonical models
## Finding
In the canonically polarized threefold construction of Li--Li, let
\[
f_i:V\longrightarrow Y_i
\]
be the small contraction associated to a section \(C_i\), put
\[
d_i=H\cdot C_i,
\]
and let \(y_i=f_i(\Gamma_i)\) be the unique singular point of \(Y_i\). Then
\[
\boxed{\operatorname{mult}_{y_i}(Y_i)=d_i+1.}
\]
Li--Li compute
\[
\operatorname{edim}_{y_i}(Y_i)=d_i+3,
\]
so equivalently
\[
\boxed{\operatorname{mult}_{y_i}(Y_i)=\operatorname{edim}_{y_i}(Y_i)-2.}
\]
Because their construction chooses the integers \(d_i\) to be strictly increasing, the Hilbert--Samuel multiplicities of the singularities appearing among log canonical models of the single fixed smooth canonically polarized threefold \(V\) are unbounded.

## Assumptions and scope
The setting is the threefold constructed in Section 5 of Li--Li. Their starting data produce infinitely many curves \(\Gamma_i\simeq\mathbf P^1\) on one smooth projective threefold \(V\), and the formal neighborhood of \(\Gamma_i\) is identified with that of the zero section in
\[
\operatorname{Tot}\!\left(\mathcal O_{\mathbf P^1}(-1)\oplus\mathcal O_{\mathbf P^1}(-d_i)\right).
\]
The curve is contracted by
\[
f_i:V\longrightarrow Y_i
\]
to the unique singular point \(y_i\). The \(Y_i\) are log canonical models for varying boundaries on the same fixed \(V\), and \(K_V\) is ample.

The multiplicity below is the Hilbert--Samuel multiplicity of the maximal ideal of the local ring \(\mathcal O_{Y_i,y_i}\). The statement concerns these specific singular points and does not assert an analogous formula for arbitrary small contractions or arbitrary log canonical models.

## Proof
Fix an integer
\[
d\ge1.
\]
Li--Li identify the completed local ring of the contraction of the zero section in
\[
E_d=\mathcal O_{\mathbf P^1}(-1)\oplus\mathcal O_{\mathbf P^1}(-d)
\]
with the completion at the homogeneous maximal ideal of the standard graded ring
\[
R_d=
\bigoplus_{m\ge0}
H^0\!\left(
\mathbf P^1,\operatorname{Sym}^m(E_d^\vee)
\right).
\]
They also note that \(R_d\) is generated in degree \(1\).

Since
\[
E_d^\vee=
\mathcal O_{\mathbf P^1}(1)\oplus
\mathcal O_{\mathbf P^1}(d),
\]
the degree-\(m\) piece decomposes as
\[
(R_d)_m=
\bigoplus_{a+b=m}
H^0\!\left(
\mathbf P^1,\mathcal O_{\mathbf P^1}(a+bd)
\right).
\]
Writing \(a=m-b\) and summing over \(0\le b\le m\) gives
\[
\begin{aligned}
\dim (R_d)_m
&=
\sum_{b=0}^{m}\left(m-b+bd+1\right)\\
&=
(m+1)^2+\frac{(d-1)m(m+1)}{2}\\
&=
\frac{d+1}{2}m^2+\frac{d+3}{2}m+1.
\end{aligned}
\]
The ring \(R_d\) has Krull dimension \(3\). For a standard graded ring of dimension \(3\), the leading coefficient of the Hilbert polynomial of its graded pieces is
\[
\frac{e(R_d)}{2!}.
\]
Comparing with the displayed formula yields
\[
e(R_d)=d+1.
\]

Hilbert--Samuel multiplicity is unchanged by completion. Therefore the local ring of the contraction point satisfies
\[
\operatorname{mult}_{y}(Y)=d+1.
\]
Applying this with \(d=d_i\) gives
\[
\operatorname{mult}_{y_i}(Y_i)=d_i+1.
\]

Li--Li independently compute
\[
\operatorname{edim}_{y_i}(Y_i)=d_i+3,
\]
which gives
\[
\operatorname{mult}_{y_i}(Y_i)
=
\operatorname{edim}_{y_i}(Y_i)-2.
\]
Finally, the construction arranges
\[
d_1<d_2<d_3<\cdots,
\]
so the multiplicities are unbounded.

## Verification
The proof was reconstructed directly from the completed local-ring model in Li--Li's Lemma 5.1 and its application in the proof of their main threefold theorem.

The critical calculation is exact. For every \(m\ge0\),
\[
\dim (R_d)_m
=
\sum_{b=0}^{m}
\left(m+1+b(d-1)\right),
\]
so
\[
\dim (R_d)_m
=
\frac{d+1}{2}m^2+\frac{d+3}{2}m+1.
\]
Thus the multiplicity is the coefficient of \(m^2\) multiplied by \(2!\), namely \(d+1\). No finite sampling is used to infer the formula.

The passage from \(R_d\) to the analytic contraction germ uses the source's explicit completion isomorphism. Completion invariance of Hilbert--Samuel multiplicity then transfers the calculation to \(\mathcal O_{Y_i,y_i}\).

The unboundedness conclusion uses the source's explicit choice of sections \(C_i\) with strictly increasing intersection numbers \(d_i=H\cdot C_i\).

## Relationship to prior work
Li--Li use the same local model to prove
\[
\operatorname{edim}_{y_i}(Y_i)=d_i+3
\]
and thereby distinguish infinitely many log canonical models. Their paper does not state the Hilbert--Samuel multiplicity of \(y_i\), nor the resulting unboundedness of multiplicity across the models.

The graded ring \(R_d\) is the homogeneous coordinate ring of the cone over the rational normal scroll of type \((1,d)\), whose degree \(d+1\) is consistent with the calculation above. The proof here does not rely on that identification: it extracts the multiplicity directly from the Hilbert function printed by the local model.

Targeted searches for the source identifier together with Hilbert--Samuel multiplicity, for the equivalent formula \(d+1\), for the scroll-cone formulation, and for unbounded multiplicity of singularities on log canonical models of a fixed threefold did not locate a statement covering this conclusion.

## Limitations
The result gives a quantitative singularity invariant for the specific Li--Li contractions. It does not classify the analytic singularities beyond the information already encoded by the completed local rings.

Unbounded multiplicity is proved for the varying log canonical models in this construction; no claim is made that every family with infinitely many log canonical models must have unbounded multiplicity.

The argument is characteristic-zero algebraic geometry in the setting of the initiating paper and does not address positive-characteristic analogues.

## References
X. Li and Z. Li, “Log canonical models of a fixed variety with varying boundaries,” arXiv:2609.03305v1, first public 2026-09-03; current inspected version arXiv:2609.03305v2. See Theorem 1.4, Lemma 5.1, and the proof in Section 5.
