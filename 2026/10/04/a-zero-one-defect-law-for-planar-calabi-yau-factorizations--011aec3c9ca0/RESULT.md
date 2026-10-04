# A zero-one defect law for planar Calabi-Yau factorizations
## Finding
Let \(P\) be a planar surface and let \(\phi\in\operatorname{Mod}(P\operatorname{rel}\partial P)\). Suppose
\[
\lambda=(	au_{\gamma_1},\ldots,	au_{\gamma_m})
\]
is a positive allowable Calabi-Yau factorization of \(\phi\), with integral trivialization \(u\in H^1(P;\mathbb Z)\). Thus
\[
u([\gamma_i])=1\qquad(1\le i\le m).
\]
For every other positive factorization
\[
\lambda'=(	au_{\gamma'_1},\ldots,	au_{\gamma'_{m'}})
\]
of the same monodromy, one has the stronger zero-one law
\[
u([\gamma'_j])\in\{0,1\}\qquad(1\le j\le m').
\]
Moreover exactly \(m\) of these values are \(1\), and therefore
\[
m'-m=\#\{j:u([\gamma'_j])=0\}.
\]
If \(\lambda'\) is allowable and \(W_0,W\) are the associated Stein fillings, then
\[
b_2(W)-b_2(W_0)=\chi(W)-\chi(W_0)=m'-m
=\#\{j:u([\gamma'_j])=0\}.
\]
Thus every unit of topological excess above a Calabi-Yau filling is accounted for by one vanishing cycle annihilated by the original integral trivialization.

## Assumptions and scope
The page is planar. The reference factorization is positive and allowable and admits an integral trivialization in the sense of Mori: a class \(u\in H^1(P;\mathbb Z)\) evaluating to \(1\) on every reference vanishing cycle. The competing factorization may be any positive factorization for the zero-one statement. The filling statement additionally assumes that the competing factorization is allowable so that it defines a positive allowable Lefschetz fibration and hence a Stein filling.

No claim is made for nonplanar pages, for rational rather than integral trivializations, or for arbitrary Lefschetz fibrations not related by positive factorization of the same planar monodromy.

## Proof
Mori's Lemma 3.5 proves that for a fixed planar monodromy \(\phi\) and any integral class \(u\), the linear and quadratic multiplicities
\[
L_\phi(u)=\sum_j u([\gamma_j]),\qquad
Q_\phi(u)=\sum_j u([\gamma_j])^2
\]
are independent of the chosen positive factorization. For the Calabi-Yau reference factorization, triviality gives
\[
L_\phi(u)=Q_\phi(u)=m.
\]

For a competing factorization put
\[
x_j=u([\gamma'_j])\in\mathbb Z.
\]
The same invariance therefore gives
\[
\sum_{j=1}^{m'}x_j=m,
\qquad
\sum_{j=1}^{m'}x_j^2=m.
\]
Subtracting yields
\[
\sum_{j=1}^{m'}x_j(x_j-1)=0.
\]
For every integer \(x\),
\[
x(x-1)\ge0,
\]
with equality exactly for \(x=0\) or \(x=1\). Every summand in the preceding equality is therefore nonnegative, so every one must vanish. Hence each \(x_j\) is \(0\) or \(1\). The first sum now says that exactly \(m\) entries equal \(1\), leaving exactly \(m'-m\) zero entries. This proves the defect formula.

For allowable factorizations, Mori also proves that \(\operatorname{rank}V=\operatorname{rank}VV^T\) depends only on \(\phi\), and that a factorization of length \(r\) has
\[
b_2=r-\operatorname{rank}V,
\qquad
\chi=2-d+r,
\]
where \(d\) is the number of boundary components of the planar page. Subtracting the reference and competing formulas gives
\[
b_2(W)-b_2(W_0)=\chi(W)-\chi(W_0)=m'-m,
\]
which equals the zero count already proved.

Finally, the competing factorization is Calabi-Yau exactly when it has a trivialization. If the defect is zero, the original \(u\) evaluates to \(1\) on every competing vanishing cycle and is itself such a trivialization. Conversely, any Calabi-Yau factorization has Mori's minimal length \(m\), so its defect is zero.

## Verification
The proof is symbolic and uses only the two monodromy-invariant multiplicities and integrality. The bundled finite regression checker separately tests the elementary integer lemma on a large scalar window and exhaustively enumerates short tuples. Its output is:

`VERIFY_OK integer_window=-10000..10000 exhaustive_lengths=0..7 values=-3..3 solutions=255 zero_one_only=true`

This computation is not used as an infinite proof. The infinite step is the exact identity
\[
\sum_j x_j(x_j-1)=0
\]
together with nonnegativity for every integer \(x_j\).

## Relationship to prior work
Mori's arXiv:2609.30406v1 introduces the integral trivialization criterion for planar Calabi-Yau Stein fillings, proves invariance of the linear and quadratic multiplicities, and derives the minimal-length theorem by Cauchy-Schwarz. The source states only the inequality \(m'\ge m\) and characterizes equality. It does not state that every competing evaluation must already lie in \(\{0,1\}\), nor that the full length and Betti-number excess is exactly the number of \(u\)-null vanishing cycles.

Plamenevskaya and Van Horn-Morris develop the planar hole and pairwise-hole multiplicities underlying this kind of factorization comparison. Their inspected text uses those multiplicities to constrain positive factorizations and fillings, but does not contain the integral Calabi-Yau trivialization or the zero-one defect formula.

The present statement is therefore a structural refinement of the recent minimality theorem: it identifies the precise local defect carried by each extra factor, rather than only bounding the total number of factors.

## Limitations
The zero-one conclusion depends crucially on integrality. Replacing \(u\in H^1(P;\mathbb Z)\) by a merely rational solution destroys the elementary nonnegativity argument because \(x(x-1)\) can be negative for \(0<x<1\).

The theorem controls evaluations under one fixed Calabi-Yau trivialization and counts excess handles in a planar positive factorization. It does not classify the isotopy classes of the null-evaluated vanishing cycles, distinguish fillings with the same defect, or extend automatically to higher-genus pages.

## References
1. A. Mori, *Planar Contact Structures with Calabi-Yau Fillings and Topological Quantum Computation*, arXiv:2609.30406v1, first posted 2026-09-24.
2. O. Plamenevskaya and J. Van Horn-Morris, *Planar open books, monodromy factorizations, and symplectic fillings*, Geometry & Topology 14 (2010), 2077--2101; arXiv:0912.1916.
3. P. Ghiggini, M. Golla, and O. Plamenevskaya, *Surface singularities and planar contact structures*, Annales de l'Institut Fourier 70 (2020), 1791--1823.
