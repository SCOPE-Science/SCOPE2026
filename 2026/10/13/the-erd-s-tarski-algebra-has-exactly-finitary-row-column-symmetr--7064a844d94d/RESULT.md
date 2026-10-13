# The Erdős–Tarski algebra has exactly finitary row-column symmetries

## Finding
Let \(A_{ET}\) be the classical one-generated infinite \(\mathsf{S5}^2\)-algebra of Erdős and Tarski. For the explicit descriptive dual frame \(\mathfrak F=(X,E_1,E_2)\) of Bezhanishvili--Meadors, one has
\[
\operatorname{Aut}(A_{ET})\cong \operatorname{Sym}_{\mathrm{fin}}(\omega)\times
\operatorname{Sym}_{\mathrm{fin}}(\omega),
\]
where \(\operatorname{Sym}_{\mathrm{fin}}(\omega)\) is the group of finite-support permutations of \(\omega\).

More concretely, every dual-frame automorphism fixes the two compactification points \(k_1,k_2\) individually and is uniquely of the form
\[
(i,j)\longmapsto (\alpha(i),\beta(j)),\qquad
\alpha,\beta\in\operatorname{Sym}_{\mathrm{fin}}(\omega),
\]
with the evident extensions \(\alpha(\omega)=\beta(\omega)=\omega\). Conversely every such pair extends to a frame automorphism. In particular the automorphism group is countable, locally finite, and not finitely generated.

## Source input
Example 5.10 of Bezhanishvili--Meadors describes the dual space as
\[
X=((\omega+1)\times(\omega+1))\setminus\{(\omega,\omega)\}\cup\{k_1,k_2\},
\]
with \(E_1\)-classes the rows and \(E_2\)-classes the columns. The points \(k_1,k_2\) lie in the intersection of the top row and rightmost column, and \(\{k_1,k_2\}\) is the unique non-singleton \(E_1\cap E_2\)-class. The topology is the two-point compactification determined by
\[
g_1=\{(i,j):i\le j\le\omega\}\cap X_0,\qquad g_2=X_0\setminus g_1,
\]
where \(X_0=((\omega+1)^2)\setminus\{(\omega,\omega)\}\). A neighborhood basis at \(k_s\) consists of \(U\cup\{k_s\}\), with \(U\) clopen in \(X_0\) and \(g_s\setminus U\) compact. Theorem 5.13 identifies \(\mathfrak F^*\) with the Erdős--Tarski algebra.

## Proof
Let \(h\) be an automorphism of \(\mathfrak F\). Because \(h\) preserves \(E_1\) and \(E_2\), it preserves the unique pair consisting of the top row and rightmost column: they are the unique \(E_1\)- and \(E_2\)-classes whose intersection has two points. Hence the finite rows are permuted among themselves, as are the finite columns. There are permutations \(\alpha,\beta\in\operatorname{Sym}(\omega)\) such that on \(X_0\)
\[
h(i,j)=(\alpha(i),\beta(j)),
\]
with \(\omega\) fixed in each coordinate. The only remaining set-theoretic possibility is that \(h\) either fixes or swaps \(k_1,k_2\).

Put \(a=\alpha^{-1}\) and \(b=\beta^{-1}\). First suppose \(h(k_s)=k_s\) for \(s=1,2\). The set \(g_1\cup\{k_1\}\) is clopen in \(X\). Its image is therefore a clopen neighborhood of \(k_1\) missing \(k_2\). From the displayed neighborhood basis, and then applying the same argument to \(h^{-1}\), it follows that
\[
h(g_1)\triangle g_1
\]
is compact in \(X_0\).

A compact subset of \(X_0\) cannot accumulate at the deleted corner \((\omega,\omega)\). Consequently there is \(N<\omega\) such that, for all finite \(i,j\ge N\),
\[
a(i)\le b(j)\quad\Longleftrightarrow\quad i\le j. \tag{1}
\]
Taking \(i=j\) and \(i=j+1\) in (1) gives
\[
a(j)\le b(j)<a(j+1)
\]
for all sufficiently large \(j\). Thus \(a\) is eventually strictly increasing. An eventually strictly increasing permutation of \(\omega\) is eventually the identity: infinitely many gaps would omit arbitrarily large integers, while once the tail has no gaps, bijectivity forces zero translation. Hence \(a(j)=j\) eventually, and the displayed inequalities then force \(b(j)=j\) eventually. Therefore \(\alpha\) and \(\beta\) have finite support.

Now suppose instead that \(h\) swaps \(k_1,k_2\). The same clopen-neighborhood argument, using the complementary clopen sets \(g_1\cup\{k_1\}\) and \(g_2\cup\{k_2\}\), yields compactness of
\[
h(g_1)\triangle g_2.
\]
Hence for all sufficiently large finite \(i,j\),
\[
a(i)\le b(j)\quad\Longleftrightarrow\quad i>j. \tag{2}
\]
Putting \(i=j\) and \(i=j+1\) in (2) gives \(a(j)>b(j)\ge a(j+1)\), so \(a\) would be eventually strictly decreasing in \(\omega\), impossible. Thus \(k_1,k_2\) are fixed individually.

Conversely, let \(\alpha,\beta\) have finite support. The coordinate map is a homeomorphism of \(X_0\), preserves rows and columns, and changes \(g_1\) only inside finitely many finite rows and columns. Those rows and columns are compact in \(X_0\), so the symmetric difference with \(g_1\) is compact. The neighborhood-basis description therefore extends the map continuously over \(k_1,k_2\), fixing them. Its inverse has the same property, so this is a frame automorphism.

This proves
\[
\operatorname{Aut}(\mathfrak F)\cong
\operatorname{Sym}_{\mathrm{fin}}(\omega)^2.
\]
Jónsson--Tarski duality identifies algebra automorphisms contravariantly with dual-frame automorphisms; inversion converts the resulting anti-isomorphism into the displayed group isomorphism for \(A_{ET}\).

## Why this is new relative to the source
The cited paper gives the explicit two-point compactification and proves that its dual algebra is the Erdős--Tarski algebra. It does not state an automorphism-group computation; direct full-text searches for “automorphism” and “symmetry” return no occurrence. The calculation above extracts the exact hidden symmetry group from the topology and the two equivalence relations.

## Limitations
The claim is specifically about the classical Erdős--Tarski \(\mathsf{S5}^2\)-algebra represented by this frame. It does not classify endomorphisms, subalgebras, or automorphisms of arbitrary finitely generated \(\mathsf{MS4}\)-algebras. A residual literature risk remains that the same group computation occurs in older uncatalogued treatments of the Erdős--Tarski example.
