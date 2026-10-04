# Finite expansive-observable certificates equal Euclidean embedding dimension

## Finding
For a nonempty compact metric space \(X\) and a homeomorphism \(f:X\to X\), define the finite expansive-observable certificate number \(c_{\mathrm{Exp}}(f)\) as the least \(m\in\mathbb N_0\) such that there are real-valued observables \(\varphi_1,\ldots,\varphi_m\in\mathrm{Exp}(f)\) with injective joint map
\[
\Phi(x)=(\varphi_1(x),\ldots,\varphi_m(x))\in\mathbb R^m.
\]
If no such finite family exists, put \(c_{\mathrm{Exp}}(f)=\infty\). For a singleton, the empty family is allowed, so \(c_{\mathrm{Exp}}(f)=0\).

Then \(c_{\mathrm{Exp}}(f)<\infty\) exactly when \(f\) is expansive. Moreover, whenever \(f\) is expansive,
\[
c_{\mathrm{Exp}}(f)=e_{\mathbb R}(X),
\]
where \(e_{\mathbb R}(X)\) is the least \(m\) for which \(X\) embeds topologically in \(\mathbb R^m\).

Thus, if the Lebesgue covering dimension of \(X\) is \(d<\infty\), Menger--Nöbeling gives
\[
c_{\mathrm{Exp}}(f)\le 2d+1
\]
for every expansive \(f\). The classical sharpness of the Menger--Nöbeling bound shows that no smaller universal bound works for all \(d\)-dimensional compacta.

## Assumptions and scope
The phase space is a nonempty compact metric space. The dynamics is a homeomorphism. An observable is called expansive in the sense of Bautista--Jung--Morales: \(\varphi\in C(X)\) is expansive if some \(\delta>0\) satisfies
\[
d(f^n(x),f^n(y))\le\delta\ 	ext{ for all }\ n\in\mathbb Z
\quad\Longrightarrow\quad
\varphi(x)=\varphi(y).
\]
Only real-valued observables are used in the certificate; these are a subclass of the complex-valued algebra \(C(X)\) used in the source. The equality with Euclidean embedding dimension does not require finite covering dimension. Finite covering dimension is used only for the numerical bound \(2d+1\).

## Proof
Assume first that \(c_{\mathrm{Exp}}(f)=m<\infty\). Choose expansive observables \(\varphi_1,\ldots,\varphi_m\) whose joint map \(\Phi\) is injective. For each \(j\), let \(\delta_j>0\) be an expansivity constant for \(\varphi_j\), and set
\[
\delta=\min_{1\le j\le m}\delta_j.
\]
For \(m=0\), injectivity of the empty joint map forces \(X\) to be a singleton, so \(f\) is expansive. For \(m\ge1\), if \(x,y\in X\) satisfy
\[
d(f^n(x),f^n(y))\le\delta\ 	ext{ for every }\ n\in\mathbb Z,
\]
then the defining property of each \(\varphi_j\) gives \(\varphi_j(x)=\varphi_j(y)\). Hence \(\Phi(x)=\Phi(y)\), and injectivity gives \(x=y\). Thus \(f\) is expansive.

Now suppose that \(f\) is expansive. Bautista--Jung--Morales prove that every continuous observable is expansive, in fact with a common expansivity constant. Let \(m=e_{\mathbb R}(X)\) and choose a topological embedding \(E:X\hookrightarrow\mathbb R^m\). Writing
\[
E=(e_1,\ldots,e_m),
\]
each coordinate \(e_j:X\to\mathbb R\) is continuous and therefore belongs to \(\mathrm{Exp}(f)\). Thus \(c_{\mathrm{Exp}}(f)\le e_{\mathbb R}(X)\).

Conversely, every certificate \(\Phi:X\to\mathbb R^m\) is a continuous injective map from compact \(X\) to Hausdorff \(\mathbb R^m\), hence a topological embedding. Therefore \(e_{\mathbb R}(X)\le m\) for every finite certificate, and so \(e_{\mathbb R}(X)\le c_{\mathrm{Exp}}(f)\). Equality follows.

Finally, when \(\dim X=d<\infty\), the Menger--Nöbeling theorem gives \(e_{\mathbb R}(X)\le2d+1\). Sharp examples for the classical embedding theorem show that this uniform numerical bound cannot be improved over all compacta of covering dimension \(d\).

## Verification
The proof has two independent ingredients. First, the finite-certificate implication is checked directly from the quantifiers in the definition of an expansive observable: taking the minimum of finitely many positive constants turns joint injectivity into an expansivity constant for \(f\). Second, the reverse implication uses the source theorem that expansivity makes every continuous observable expansive, followed by the coordinate functions of a Euclidean embedding. Compact-to-Hausdorff injectivity verifies that every joint certificate is genuinely an embedding.

No computation or finite experiment is used. The only external theorem beyond the 2025 expansive-observable paper is the classical Menger--Nöbeling embedding theorem for the optional \(2d+1\) bound; the exact identity \(c_{\mathrm{Exp}}(f)=e_{\mathbb R}(X)\) itself does not depend on finite-dimensionality.

## Relationship to prior work
Bautista, Jung and Morales introduce expansive observables and prove that an expansive homeomorphism is characterized by all continuous observables being expansive with a common constant. Their paper studies the algebra \(\mathrm{Exp}(f)\), pseudoexpansivity, conjugacy invariance, periodic-point level sets, and iterate invariance. Searches of the full preprint found no discussion of a finite family of expansive observables, Menger--Nöbeling, covering dimension, or Euclidean embedding dimension.

Gutman, Levin and Meyerovitch study equivariant embeddings of finite-dimensional dynamical systems, extending Menger--Nöbeling and Takens/Jaworski-type delay embeddings. Their results concern generic orbit maps into shift spaces and finite delay coordinates; they do not formulate the finite certificate number above or identify it with Euclidean embedding dimension through the newly introduced algebra of expansive observables.

published-finding corpus searches using the phrases ``finite expansive-observable certificate number Euclidean embedding dimension expansive homeomorphism'', ``real-valued expansive observables joint injective map finite family characterization expansivity'', ``Exp(f) finite separating family Menger Nobeling compact metric dimension'', and ``observable embedding dimension expansive homeomorphism'' returned no matching published published-finding corpus finding. The closest returned records concerned Euclidean nonembeddability of generic metrics and unrelated certificate problems, not dynamical expansive-observable algebras.

## Limitations
This finding does not prove that pseudoexpansivity implies expansivity, nor does it show that a dense algebra of expansive observables contains a finite separating family. It only classifies systems for which such a finite jointly injective family actually exists. The \(2d+1\) bound is a worst-case topological bound; many phase spaces have strictly smaller Euclidean embedding dimension, and then the exact certificate number is correspondingly smaller.

## References
1. S. Bautista, W. Jung, C. A. Morales, *Characterizing expansivity through C*-algebras*, arXiv:2510.17255v1, 2025. Primary MSC 37B05.
2. Y. Gutman, M. Levin, T. Meyerovitch, *Equivariant embedding of finite-dimensional dynamical systems*, arXiv:2305.17717; Mathematische Annalen 391 (2025), 915--936.
3. Classical Menger--Nöbeling embedding theorem; the sharp \(2d+1\) form is recalled in Reference 2.
