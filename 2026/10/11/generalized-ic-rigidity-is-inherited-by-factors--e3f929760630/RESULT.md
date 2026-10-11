# Generalized IC-rigidity is inherited by factors
## Finding
Let \(G\) be a locally compact second-countable amenable group acting continuously on compact metric spaces \(X\) and \(Y\). Let
\[
\pi:X\longrightarrow Y
\]
be a continuous surjective \(G\)-equivariant map. In the generalized definition of IC-rigidity of Kanigowski, Kasprzak, and Lorenzo-Laguno, let \(\mathcal K_G(X)\) denote the compact subsets of \(X\) formed as finite unions of compact orbit segments under compact subsets of the center \(Z(G)\).

If \((X,G)\) is IC-rigid, then \((Y,G)\) is IC-rigid. Thus generalized IC-rigidity is inherited by topological factors for every locally compact second-countable amenable acting group.

This strictly extends the factor-permanence statement proved by Kra and Schmieding for their original discrete-group definition. For a discrete group, \(\mathcal K_G(X)=\mathcal K_{{\rm fin}}(X)\); for a non-discrete group the 2026 extension allows genuinely infinite compact central orbit segments. Consequently, every compact-metric topological factor of an IC-rigid horocycle flow in Theorem C of arXiv:2609.36397v1 is again IC-rigid in the generalized sense.

## Assumptions and scope
The acting group \(G\) is locally compact, second countable, and amenable. Both spaces are compact metric spaces, and \(\pi\) is a continuous onto equivariant map. The IC-rigidity notion is Definition 2.8 of arXiv:2609.36397v1:
\[
\nu\bigl(\mathcal K_G(X)\cup\{{X\}}\bigr)=1
\]
for every invariant Borel probability \(\nu\) on the hyperspace \(\mathcal K(X)\).

No converse is asserted. No claim is made for nonamenable groups, because the invariant-measure lifting step used below is an amenability statement. The result concerns topological factors; it does not assert that extensions of IC-rigid systems are IC-rigid.

## Proof
Define the induced hyperspace map
\[
\pi_{\mathcal K}:\mathcal K(X)\longrightarrow\mathcal K(Y),\qquad A\longmapsto\pi(A).
\]
It is continuous and \(G\)-equivariant. It is also onto: if \(B\subseteq Y\) is nonempty and compact, then \(\pi^{-1}(B)\subseteq X\) is nonempty and compact and
\[
\pi_{\mathcal K}(\pi^{-1}(B))=B.
\]
Hence \(\pi_{\mathcal K}\) is a factor map of the induced hyperspace actions.

Let \(\eta\) be an arbitrary \(G\)-invariant Borel probability measure on \(\mathcal K(Y)\). We first construct an invariant lift. Because \(\pi_{\mathcal K}\) is a continuous surjection between compact metric spaces, its pushforward on probability measures is onto. Concretely, approximate \(\eta\) weakly by finitely supported probabilities, lift each atom to an arbitrary compact preimage, and pass to a weak limit in the compact space of probabilities on \(\mathcal K(X)\). Thus there is a probability \(\lambda_0\) with
\[
(\pi_{\mathcal K})_*\lambda_0=\eta.
\]
Let \((F_n)\) be a Følner sequence in \(G\) with Haar measure \(m\), and average the orbit of \(\lambda_0\):
\[
\lambda_n=\frac{1}{m(F_n)}\int_{F_n} g_*\lambda_0\,dm(g).
\]
Every \(\lambda_n\) still pushes forward to \(\eta\), because \(\eta\) is invariant. Any weak accumulation point \(\widetilde\eta\) therefore also pushes forward to \(\eta\), and the Følner property gives \(g_*\widetilde\eta=\widetilde\eta\) for every \(g\in G\). Hence
\[
(\pi_{\mathcal K})_*\widetilde\eta=\eta
\]
with \(\widetilde\eta\) invariant. Kra and Schmieding use the corresponding amenable lifting fact in their discrete IC-rigidity factor theorem.

By IC-rigidity of \((X,G)\),
\[
\widetilde\eta\bigl(\mathcal K_G(X)\cup\{{X\}}\bigr)=1.
\]
It remains to check that the allowed class is respected by \(\pi_{\mathcal K}\). Take
\[
S=\bigcup_{x\in F}\{g x:g\in I_x\}\in\mathcal K_G(X),
\]
where \(F\subset X\) is finite and every \(I_x\subset Z(G)\) is nonempty and compact. Equivariance gives
\[
\pi_{\mathcal K}(S)=\bigcup_{x\in F}\{g\pi(x):g\in I_x\}\in\mathcal K_G(Y).
\]
Also \(\pi_{\mathcal K}(X)=Y\). Therefore
\[
\pi_{\mathcal K}\bigl(\mathcal K_G(X)\cup\{{X\}}\bigr)
\subseteq\mathcal K_G(Y)\cup\{{Y\}}.
\]
Pushing forward the preceding full-measure statement yields
\[
\eta\bigl(\mathcal K_G(Y)\cup\{{Y\}}\bigr)=1.
\]
Since \(\eta\) was arbitrary, \((Y,G)\) is IC-rigid.

## Verification
The proof was checked against the exact generalized definition in arXiv:2609.36397v1. The invariant lift was reconstructed directly by first lifting a probability measure and then averaging over a Følner sequence; arXiv:2605.03993 records the corresponding amenable lifting fact in the discrete setting. The remaining nonformal compatibility step is the displayed image calculation for \(\mathcal K_G\), which uses the same compact sets \(I_x\subset Z(G)\) before and after applying the equivariant factor map.

Surjectivity of the hyperspace map was checked directly by using the compact preimage \(\pi^{-1}(B)\). No selection theorem, finite experiment, or numerical computation is needed. The proof does not assume that fibers of \(\pi\) are finite.

## Relationship to prior work
Kra and Schmieding introduced invariant random compacts and prove, for amenable discrete groups under their original definition, that every factor of an IC-rigid system is IC-rigid. Their proof uses invariant-measure lifting on hyperspaces. Kanigowski, Kasprzak, and Lorenzo-Laguno subsequently extend IC-rigidity to non-discrete locally compact groups by replacing finite compacts with \(\mathcal K_G(X)\), the finite unions of compact central orbit segments, and use this extension to prove IC-rigidity for certain horocycle flows.

The recent paper does not state a factor-permanence theorem for this enlarged definition. The new point is that the factor argument survives exactly because equivariant maps send compact central orbit segments to compact central orbit segments. The discrete theorem alone does not cover this: for a flow, allowed members of \(\mathcal K_G(X)\) can be infinite.

Targeted searches for factor heredity, quotient stability, flow factors, and the generalized \(\mathcal K_G\) definition found no statement equivalent to this continuous-group extension.

## Limitations
Amenability is used only to lift an invariant probability through the hyperspace factor map; the argument gives no nonamenable analogue without another lifting hypothesis. The theorem is one-way: it says factors inherit IC-rigidity, not that extensions do. It also does not classify factors of the horocycle examples or prove that any particular nontrivial factor exists.

The closest prior theorem is the discrete-group factor result of Kra and Schmieding. The mathematical novelty is therefore the compatibility and permanence statement for the enlarged non-discrete definition, not a new proof of the discrete case.

## References
1. Adam Kanigowski, Kosma Kasprzak, Miriam Lorenzo-Laguno, *IC-rigidity for abelian actions*, arXiv:2609.36397v1, first public 2026-09-28; Definition 2.8 and Theorem C.
2. Bryna Kra, Scott Schmieding, *Invariant random compacts*, arXiv:2605.03993, first public 2026-05-05; invariant-measure lifting for factor maps and the discrete factor-permanence discussion in Section 3.
