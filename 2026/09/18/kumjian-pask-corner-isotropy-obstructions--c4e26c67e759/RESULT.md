# Corner and isolation obstructions in Kumjian--Pask induction--restriction

## Statement

Let \(R\) be a nonzero unital commutative ring and let \(A=KP_R(\Lambda)\) for a row-finite \(k\)-graph with no sources. Three structural assertions used in arXiv:2609.20230v1 fail without additional hypotheses.

### 1. A vertex corner need not be scalar

There is no general isomorphism
\[
s_v A s_v\cong R
\]
via \(s_v\mapsto 1\). For the one-vertex one-loop graph,
\[
A\cong R[t,t^{-1}],\qquad s_v=1_A,
\]
so
\[
s_vAs_v=A=R[t,t^{-1}],
\]
and the scalar map \(R\to s_vAs_v\) is not surjective. Thus the vertex-corner identification used in Section 3.1 of arXiv:2609.20230v1 is false as stated. In the same example, \(As_v=A\) contains negative Laurent powers, so the proposed reduction of the principal left ideal to the span of ordinary paths also fails.

The safe replacement is to induce from the actual corner \(s_vAs_v\), unless a separate hypothesis proves that this corner is exactly \(Rs_v\).

### 2. The ambient algebra need not be free over a hereditary corner

Even over a field, \(A\) need not be a free right module over \(B=KP_R(\Lambda|_H)\) under the corner inclusion \(B\cong p_HAp_H\hookrightarrow A\).

Take \(R=k\) a field and let \(\Lambda\) be the disjoint union of two one-vertex one-loop graphs, with vertices \(v,w\). Put \(H=\{w\}\), which is hereditary and saturated. Then
\[
A\cong k[t,t^{-1}]\oplus k[u,u^{-1}],\qquad
B\cong k[u,u^{-1}],
\]
with \(B\) embedded as the second summand and identity \(p_H=(0,1)\). Hence
\[
(1,0)\,B=0.
\]
A free right module over the unital ring \(B\) is unital, whereas the displayed right \(B\)-module \(A\) is not: \((1,0)p_H=0\ne(1,0)\). Therefore \(A_B\) is not free. Equivalently, the proposed transversal in Theorem 3.5 cannot generate the outside vertex idempotent \(s_v\), because \(s_v b=0\) for every \(b\in B\).

There is, however, a general idempotent-corner repair. For every ring \(A\), idempotent \(p\), \(B=pAp\), and unital left \(B\)-module \(V\), inclusion induces a canonical isomorphism
\[
Ap\otimes_B V\;\xrightarrow{\ \cong\ }\;A\otimes_B V.
\]
Indeed,
\[
a\otimes v=a\otimes pv=ap\otimes v,
\]
so every tensor is represented in \(Ap\otimes_BV\); the inverse is \(a\otimes v\mapsto ap\otimes v\). Thus the natural induction bimodule attached to the corner is \(Ap_H\), not the whole ambient algebra regarded as a free right \(B\)-module. Exactness requires flatness of \((Ap_H)_B\), which does not follow from the freeness argument in Theorem 3.5.

### 3. Singleton isotropy embeds in a Steinberg algebra exactly at isolated units

Let \(\mathcal G\) be a Hausdorff ample groupoid, \(x\in\mathcal G^{(0)}\), and \(\mathcal G_x^x\) its isotropy group. Consider the point-mass assignment
\[
\delta_g\longmapsto \mathbf 1_{\{g\}},\qquad g\in\mathcal G_x^x.
\]
Then this defines an algebra embedding
\[
R[\mathcal G_x^x]\hookrightarrow A_R(\mathcal G)
\]
if and only if \(x\) is an isolated point of \(\mathcal G^{(0)}\).

For necessity, the group identity \(1_x\) must map to \(\mathbf 1_{\{x\}}\). A singleton characteristic function belongs to the Steinberg algebra only when its singleton support is open, because Steinberg functions are locally constant. Hence \(x\) must be isolated.

For sufficiency, assume \(\{x\}\) is open. Given \(g\in\mathcal G_x^x\), choose a compact-open bisection \(U\ni g\). Since the source map restricts to a homeomorphism on \(U\),
\[
U\cap s^{-1}(\{x\})=\{g\}
\]
is compact open. Thus every \(\mathbf 1_{\{g\}}\) lies in \(A_R(\mathcal G)\), and convolution of these characteristic functions reproduces multiplication in \(\mathcal G_x^x\). Distinct point masses are linearly independent.

Applied to the boundary-path groupoid \(\mathcal G_\Lambda\), the singleton embedding proposed in (4.1) of arXiv:2609.20230v1 therefore exists precisely for isolated infinite paths \(x\in\Lambda^\infty\). Equivalently, some cylinder neighbourhood of \(x\) must already equal \(\{x\}\).

A minimal counterexample is the directed graph with one vertex and two loops \(a,b\). Its infinite-path space is \(\{a,b\}^{\mathbb N}\), which has no isolated points. For \(x=a^\infty\), every cylinder around \(x\) also contains paths beginning with a long block of \(a\)'s and then taking \(b\). Consequently
\[
\mathbf 1_{\{(x,0,x)\}}\notin A_R(\mathcal G_\Lambda),
\]
so the map (4.1) is not even defined. This obstruction already occurs at the identity element of the isotropy group and hence also affects aperiodic nonisolated paths, whose isotropy group is trivial.

## Consequences for arXiv:2609.20230v1

The source paper defines its Section 4 restriction functor by treating \(R[\mathcal G_{\Lambda,x}]\) as a subalgebra of the Steinberg algebra via singleton characteristic functions. The theorem above shows that Proposition 4.1 and this restriction construction require the missing hypothesis that \(x\) be isolated. Therefore downstream statements whose proofs explicitly use this embedding are not established for general nonisolated boundary paths by the arguments given there. This does not show that analogous representation-theoretic statements are false: standard Steinberg-algebra literature already develops induction and restriction from isotropy without requiring a singleton-subalgebra embedding, so those results may admit reformulations through that established machinery.

Independently, the one-loop and two-component examples show that the Section 3 vertex-corner identification and Theorem 3.5 freeness statement also need correction. The idempotent identity \(A\otimes_{pAp}V\cong Ap\otimes_{pAp}V\) isolates the natural hereditary-corner induction object and separates it from the unsupported freeness claim.

## Prior literature and originality boundary

The definition of a Steinberg algebra as compactly supported locally constant functions, or equivalently the span of characteristic functions of compact-open bisections, is standard. Existing work also relates open singleton units to minimal ideals and develops isotropy induction for Steinberg algebras. Those facts are not claimed as new here.

The contribution claimed here is the combined diagnosis, exact missing hypotheses, explicit counterexamples, and corner-bimodule repair for the specific framework stated in arXiv:2609.20230v1. Targeted searches for the preprint identifier/title together with the vertex-corner, hereditary-freeness, singleton-isotropy, and isolated-path formulations found no prior correction.

## Limitations

Originality is to the best of our knowledge. The source is a recent v1 and may be revised. The 2024 Nguyen--Nguyen article on graded isotropy induction was verified through its published abstract and publisher-preview material rather than a complete full-text inspection in this review. The present result does not claim that every downstream theorem in arXiv:2609.20230v1 is false; it identifies specific constructions and proofs that fail as stated and gives exact conditions or replacements for the failures above.

## References

1. N. B. Van, *Induced and Restricted Representations of Kumjian--Pask Algebras of Higher-Rank Graphs*, arXiv:2609.20230v1.
2. N. Q. Loc and N. B. Van, *On induced graded simple modules over graded Steinberg algebras with applications to Leavitt path algebras*, Journal of Algebra and Its Applications 23 (2024), 2450126; arXiv:2006.09931.
3. T. G. Nam, *Simple Lie algebras arising from Steinberg algebras of Hausdorff ample groupoids*, Journal of Algebra (2022), DOI: 10.1016/j.jalgebra.2021.12.014.
4. L. O. Clark, C. Gil Canto, D. Martín Barquero, C. Martín González, and I. Ruiz Campos, *On the socle of a class of Steinberg algebras*, arXiv:2502.15574.
