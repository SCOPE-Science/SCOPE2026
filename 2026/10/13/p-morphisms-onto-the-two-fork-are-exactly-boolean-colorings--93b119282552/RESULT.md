# P-morphisms onto the two-fork are exactly Boolean colorings

## Finding

For every integer \(n\ge 1\), let \(\mathbf A_n\) be the finite partial-function frame whose points are partial functions \(x:[n]\rightharpoonup\{1,2\}\), ordered by extension. Let \(\mathbf A_1\) be the two-fork, with root \(0\) and incomparable maximal points \(1\) and \(2\). Then restriction to the maximal points gives a bijection
\[
\operatorname{PMor}(\mathbf A_n,\mathbf A_1)
\longleftrightarrow
\{c:\{1,2\}^n\to\{1,2\}\}.
\]
Explicitly, if \(M(x)\) is the set of total extensions of \(x\), the coloring \(c\) determines
\[
f_c(x)=
\begin{cases}
1,& c[M(x)]=\{1\},\\
2,& c[M(x)]=\{2\},\\
0,& c[M(x)]=\{1,2\}.
\end{cases}
\]
Hence
\[
\bigl|\operatorname{PMor}(\mathbf A_n,\mathbf A_1)\bigr|=2^{2^n}.
\]
The map is onto exactly when \(c\) is nonconstant, so the number of surjective p-morphisms is
\[
2^{2^n}-2.
\]

## Assumptions and scope

A p-morphism between finite posets is used in the standard intuitionistic-frame sense: it is monotone and satisfies the back condition that whenever \(f(x)\le u\), some \(y\ge x\) satisfies \(f(y)=u\). This is the convention in Xiao's Definition 2.1. Xiao also identifies the finite partial-function frame \(\mathbf A_n\) with the \(n\)-fold product \(\mathbf V_n\) of the two-fork. The statement is only about maps with target \(\mathbf A_1\); it makes no classification claim for p-morphisms \(\mathbf A_n\to\mathbf A_m\) when \(m>1\).

## Proof

Let \(f:\mathbf A_n\to\mathbf A_1\) be a p-morphism. A maximal point \(z\in\mathbf A_n\) is a total function. It cannot satisfy \(f(z)=0\): because \(0\le 1\) in the target, the back condition would require some \(y\ge z\) with \(f(y)=1\), while maximality forces \(y=z\). Thus every maximal point maps to \(1\) or \(2\). Define \(c(z)=f(z)\) on \(\{1,2\}^n\).

Fix \(x\in\mathbf A_n\). If \(f(x)=1\), then monotonicity forces \(f(z)=1\) for every maximal \(z\ge x\), because \(1\) is maximal in \(\mathbf A_1\). The same argument holds with \(2\).

Conversely, suppose every maximal extension of \(x\) has color \(1\). The value \(f(x)\) cannot be \(2\) by monotonicity. If \(f(x)=0\), the back condition for \(0\le2\) supplies \(y\ge x\) with \(f(y)=2\). Extend \(y\) to a maximal \(z\). Monotonicity then forces \(f(z)=2\), contradicting the assumed colors of maximal extensions. Hence \(f(x)=1\). The case in which every maximal extension has color \(2\) is symmetric. If maximal extensions of \(x\) occur in both colors, monotonicity rules out both maximal target values, so \(f(x)=0\). Therefore the displayed formula is forced and the restriction map is injective.

For surjectivity of the restriction construction, start with an arbitrary coloring \(c:\{1,2\}^n\to\{1,2\}\) and define \(f_c\) by the displayed formula. If \(x\le y\), then \(M(y)\subseteq M(x)\). Therefore a constant color on \(M(x)\) remains constant on \(M(y)\), proving monotonicity; when \(f_c(x)=0\), monotonicity is automatic because \(0\) is the root.

For the back condition, if \(f_c(x)\) is \(1\) or \(2\), its only extension in the target is itself, and one may take \(y=x\). If \(f_c(x)=0\), then \(M(x)\) contains a maximal extension of each color. For target value \(1\) or \(2\), choose such a maximal extension \(y\); for target value \(0\), take \(y=x\). Thus \(f_c\) is a p-morphism.

There are \(2^{2^n}\) colorings of the \(2^n\) maximal points. A constant coloring makes \(f_c\) constant at the corresponding maximal target point, so it is not onto. If \(c\) is nonconstant, the root of \(\mathbf A_n\) has maximal extensions of both colors and therefore maps to \(0\), while maximal points realize both \(1\) and \(2\). Hence exactly the two constant colorings are nonsurjective.

## Verification

The proof is symbolic and does not rely on finite enumeration. As a sanity check, `verify_p_morphisms.py` exhaustively enumerates every set map for \(n=1\) and \(n=2\), tests monotonicity and the p-morphism back condition directly, constructs the maps arising from all colorings, and checks equality of the two sets. It finds \(4\) p-morphisms, \(2\) surjective, for \(n=1\), and \(16\) p-morphisms, \(14\) surjective, for \(n=2\), exactly as the formulas predict.

## Relationship to prior work

Xiao's 2026 paper makes the finite partial-function frames central to the new analysis of \(\mathsf{Cheq}\): Definition 2.14 defines \(\mathbf A_n\), Lemma 2.15 identifies \(\mathbf A_n\cong\mathbf V_n\), and Sections 3 and 5 construct particular p-morphisms from these frames onto other target frames. The inspected full text does not classify all p-morphisms from \(\mathbf A_n\) onto the canonical factor \(\mathbf A_1\), nor give the count \(2^{2^n}\).

Fontaine's 2006 thesis uses the same product-of-two-forks characterization of \(\mathsf{Cheq}\) and develops p-morphic images of these frames for axiomatization questions. The inspected full text likewise does not give this Boolean-coloring correspondence. The result here therefore complements the existence-oriented p-morphism constructions by giving a complete mapping classification for the first canonical target.

## Limitations

The theorem is specific to target \(\mathbf A_1\). The proof uses that the target has one root and exactly two incomparable maximal points; it does not by itself yield an analogous classification for \(\mathbf A_m\) with \(m>1\). The exhaustive checker covers only \(n=1,2\) and is supplementary evidence, not the proof of the general statement.

## References

1. Han Xiao, “Non-finite Axiomatizability and Undecidability of \(\mathsf{Cheq}\),” arXiv:2609.39577v1, 2026.
2. Gaëlle Fontaine, *Axiomatization of ML and Cheq*, Master of Logic thesis, MoL-2006-08, University of Amsterdam, 2006.
3. Johan van Benthem, Guram Bezhanishvili, and Mai Gehrke, “Euclidean Hierarchy in Modal Logic,” *Studia Logica* 75 (2003), 327–344, doi:10.1023/B:STUD.0000009564.00287.16.
