# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The two correction criteria were checked directly against the definitions of the boundary-path groupoid and Steinberg algebra used in arXiv:2609.20230v1.

For the vertex-corner statement, the key identity is the standard reduction formula
\[
1_UA_R(\mathcal G)1_U=A_R(\mathcal G|_U)
\]
for compact open \(U\subseteq\mathcal G^{(0)}\), with extension by zero identifying the right side with a subalgebra of the left. Under the Kumjian–Pask/Steinberg isomorphism, \(s_v\) corresponds to \(1_{Z(v)}\). The scalar-corner criterion was then stress-tested in both directions:

- If \(Z(v)\) has two points, the Boolean topology supplies a proper nonempty compact open subset \(C\subset Z(v)\), and \(1_C\) is a non-scalar element of the corner.
- If \(Z(v)=\{x\}\), the reduced groupoid is precisely the isotropy group at \(x\), so the corner is \(R[\operatorname{Per}(x)]\). For nonzero unital commutative \(R\), this is the scalar copy of \(R\) exactly when \(\operatorname{Per}(x)\) is trivial.
- The finite-vertex corollary was checked by propagating uniqueness of the tail along the unique path. A repeated vertex among finitely many vertices forces equality of two shifts and hence a nonzero period.
- The one-vertex one-loop graph gives the immediate counterexample \(s_vAs_v=A\cong R[t,t^{-1}]\). This is independently confirmed by Example 4.9 of arXiv:2609.20230v1. Its later rank-two example also explicitly computes non-scalar Laurent-type vertex corners.

For the isotropy point-mass statement:

- If \(1_{\{\gamma\}}\) is a Steinberg function, local constancy at \(\gamma\) forces \(\{\gamma\}\) to be open. The source map of an étale groupoid is open, so the base singleton \(\{x\}\) is open.
- Conversely, if \(\{x\}\) is open, intersecting a compact open bisection containing \(\gamma\) with \(s^{-1}(\{x\})\) produces the compact open singleton \(\{\gamma\}\).
- Because the proposed embedding in arXiv:2609.20230v1 includes \(p=0\), failure already occurs at the unit arrow for every nonisolated path.
- In the one-vertex two-loop graph, the infinite-path space is the Cantor-type space \(\{e,f\}^{\mathbb N}\), so \(x=e^\infty\) is nonisolated even though its isotropy is \(\mathbb Z\). Thus the proposed singleton characteristic functions are not Steinberg-algebra elements.
- When \(x\) is isolated, the isotropy group algebra identifies with the corner \(e_xAe_x\). Its identity is \(e_x\), so restricting an arbitrary unital \(A\)-module to the full underlying module does not generally give a unital \(e_xAe_x\)-module. The standard idempotent adjunction uses \(e_xM\), confirming the stated unitality repair.

No computational experiment is needed: the counterexamples and equivalences follow directly from the algebraic and topological definitions.

## Originality

The originality assessment is **to the best of our knowledge** and is intentionally narrow.

The structural ingredients are prior work. Abrams--Dokuchaev--Nam establish Steinberg-algebra corners as Steinberg algebras of reductions. Clark--Gil Canto--Martín Barquero--Martín González--Ruiz Campos explicitly relate open singleton units to isotropy corners; their Remark 3.17 identifies \(1_{\{x\}}A_K(\mathcal G)1_{\{x\}}\) with the Steinberg algebra of the isotropy group, and their Kumjian–Pask application characterizes line points by a unique aperiodic boundary path. Nguyen--Nguyen's earlier work records the standard Steinberg induction/restriction theory from isotropy, using the source-fiber construction rather than a universal singleton-subalgebra embedding. None of those ingredients is claimed as a new theorem here.

The recent source arXiv:2609.20230v1 was inspected at the relevant primary statements and examples. Section 3.1 states that every vertex corner is \(R\); Section 4.1 defines the isotropy embedding by singleton characteristic functions for every infinite path. Example 4.9 states that the one-loop algebra is \(R[t^{\pm1}]\), and the rank-two example explicitly exhibits Laurent-type vertex corners, so the first universal assertion conflicts with examples inside the same source.

Targeted searches for the title, arXiv identifier, `vertex corner`, `isotropy embedding`, `point mass`, and synonymous Kumjian–Pask/Steinberg formulations did not locate a public correction, erratum, or revised version addressing these two assertions. The novelty claim is therefore restricted to the diagnosis of these errors in arXiv:2609.20230v1, the exact repair criteria, the unital-module correction, and the explicit counterexamples.

The full relevant sections of arXiv:2502.15574 were inspectable. The corner proposition of Abrams--Dokuchaev--Nam was checked from an indexed primary full-text statement. For arXiv:2006.09931, the abstract and bibliographic description establishing general isotropy induction/restriction were inspected; its full text was not needed to establish the present counterexamples, but an equivalent formulation of the repair could occur there. This is a residual terminology risk, not evidence against the correction. A further residual risk is that arXiv:2609.20230 is a recent first version and may subsequently be revised independently.

## Value

The errors occur at the foundations of two advertised module constructions. The correction separates three situations that the source conflates:

1. a genuine scalar vertex corner, which occurs exactly at a unique aperiodic path;
2. an isolated path with possibly nontrivial isotropy, where the isotropy algebra is a genuine corner and the correct unital restriction is \(e_xM\);
3. a nonisolated path, where isotropy point masses do not belong to the Steinberg algebra and standard source-fiber induction is required.

The criteria are sharp, elementary to verify in examples, and immediately show that finite source-free higher-rank graphs have no scalar vertex corners at all. They therefore provide a reusable diagnostic for subsequent work that invokes vertex-corner or isotropy-subalgebra induction in Kumjian–Pask and Steinberg algebras.
