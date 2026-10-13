# Hereditary algebras are rigid under reflexive equivalence
## Finding
Let \(k\) be a field and let \(A\) be a finite-dimensional hereditary \(k\)-algebra. If a finite-dimensional \(k\)-algebra \(B\) has an equivalence
\[
\operatorname{ref} B\simeq \operatorname{ref} A
\]
of \(k\)-linear additive categories, then \(A\) and \(B\) are Morita equivalent. Thus the reflexive-equivalence class of a finite-dimensional hereditary algebra contains exactly one Morita-equivalence class.

For a basic hereditary algebra with simple right modules \(S_1,\ldots,S_n\), the sharper input is
\[
\operatorname{ref} A=\operatorname{proj} A,\qquad I_{\mathrm{ref}}(A)=\{1,\ldots,n\}.
\]

## Assumptions and scope
Here “hereditary” means that every submodule of a projective right module is projective, equivalently for a finite-dimensional algebra that the right global dimension is at most \(1\). The categories \(\operatorname{ref} A\) and \(\operatorname{ref} B\) consist of finite-dimensional reflexive right modules, with reflexivity defined by the canonical bidual map with respect to the regular module. No algebraic-closure assumption on \(k\) is used.

For a basic algebra with primitive idempotents \(e_1,\ldots,e_n\), Enomoto defines \(I_{\mathrm{ref}}(A)\) by requiring, for each index \(i\), at least one of the right- or left-sided groups \(\operatorname{Hom}(S_i,A)\), \(\operatorname{Ext}^1(S_i,A)\), or their left-module analogues to be nonzero.

## Proof
First, every reflexive module is a second syzygy. Enomoto records this directly, and therefore any algebra of global dimension at most \(2\) satisfies \(\operatorname{ref} A=\operatorname{proj} A\). In particular, a hereditary algebra is reflexive-rigid.

It remains to show that a basic hereditary algebra is reflexive-minimal, equivalently that every simple index belongs to \(I_{\mathrm{ref}}(A)\). Fix a simple right module \(S_i\).

If \(S_i\) is projective, then it is a direct summand of the regular module, so
\[
\operatorname{Hom}_A(S_i,A)\ne0.
\]
Hence \(i\in I_{\mathrm{ref}}(A)\).

Suppose instead that \(S_i\) is not projective. Since \(A\) is hereditary, a minimal projective resolution has the form
\[
0\longrightarrow P_1\xrightarrow{j}P_0\longrightarrow S_i\longrightarrow0
\]
with \(P_1\ne0\) projective. If \(\operatorname{Ext}^1_A(S_i,A)=0\), applying \(\operatorname{Hom}_A(-,A)\) makes
\[
\operatorname{Hom}_A(P_0,A)\longrightarrow\operatorname{Hom}_A(P_1,A)
\]
surjective. Because \(P_1\) is finitely generated projective, choose a split embedding \(u:P_1\to A^m\) with retraction \(r:A^m\to P_1\). Surjectivity lets every coordinate of \(u\) extend across \(j\), giving \(h:P_0\to A^m\) with \(hj=u\). Then
\[
(rh)j=ru=1_{P_1},
\]
so \(j\) splits. The displayed projective resolution then forces \(S_i\) to be a direct summand of \(P_0\), contradicting the choice of \(S_i\). Thus
\[
\operatorname{Ext}^1_A(S_i,A)\ne0,
\]
and again \(i\in I_{\mathrm{ref}}(A)\). Hence \(I_{\mathrm{ref}}(A)=\{1,\ldots,n\}\).

Enomoto's Theorem 5.5 states that, for a basic finite-dimensional algebra, every reflexively equivalent finite-dimensional algebra is Morita equivalent to it exactly when both \(\operatorname{ref} A=\operatorname{proj} A\) and \(I_{\mathrm{ref}}(A)\) contains all simple indices. The two conditions have just been verified. For a nonbasic hereditary algebra, pass to a basic Morita-equivalent algebra; hereditaryness, Morita equivalence, and reflexive equivalence are invariant under this passage.

## Verification
The proof reduces the new assertion to two independently checkable statements: hereditaryness makes every second syzygy projective, and a nonprojective simple module over a hereditary algebra has nonzero \(\operatorname{Ext}^1_A(S,A)\). The latter is verified above by a splitting argument using only finite generation and projectivity of the first syzygy. No computation, finite enumeration, or unproved extrapolation is used.

The source's Theorem 5.5 was checked in the full text, as was the definition of \(I_{\mathrm{ref}}(A)\), the statement that every reflexive module is a second syzygy, and Example 3.15 for the hereditary path algebra on three vertices.

## Relationship to prior work
Enomoto introduces reflexive equivalence and proves the criterion used here. The paper includes one hereditary example, the path algebra of \(1\to2\to3\), where all simple indices occur in \(I_{\mathrm{ref}}\), and later gives a separate global-dimension-two Nakayama example whose reflexive-equivalence class is a single Morita class. It does not state the hereditary-class theorem proved here.

Earlier work on reflexive modules, including Hanihara's Auslander-type criteria and Ringel's study of simple reflexive modules, concerns the structure of reflexive modules rather than Enomoto's new equivalence relation. The hereditary result therefore uses a classical homological fact to close an entire natural class under the new equivalence criterion, rather than merely computing another isolated example.

## Limitations
The argument uses projective dimension at most one for every simple module in the step proving \(I_{\mathrm{ref}}(A)\) is full. It does not show the analogous statement for arbitrary algebras of global dimension two: Enomoto's criterion still requires the separate \(I_{\mathrm{ref}}\)-condition there. The result is restricted to finite-dimensional algebras over a field.

## References
1. H. Enomoto, *Reflexive equivalence and reflexive-minimal algebras*, Hexagon preprint hexagon:2610.00024v1, 2026, especially Example 3.15 and Theorem 5.5.
2. N. Hanihara, *Reflexive modules and Auslander-type conditions*, arXiv:2412.19625v2; International Mathematics Research Notices, 2026.
3. C. M. Ringel, *Simple reflexive modules over finite-dimensional algebras*, arXiv:2004.12208.
