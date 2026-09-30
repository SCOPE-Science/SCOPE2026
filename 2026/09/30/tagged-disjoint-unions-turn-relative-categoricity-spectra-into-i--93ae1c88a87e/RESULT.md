# Tagged disjoint unions turn relative categoricity spectra into intersections
## Finding
Let \(\mathcal A_0,\ldots,\mathcal A_{m-1}\) be finitely many computable structures, each in its own renamed computable relational language. Form their tagged disjoint union \(\mathcal U\) by adding unary predicates \(P_0,\ldots,P_{m-1}\) naming the components and interpreting each component language only on its corresponding predicate.

Then the relative categoricity spectrum satisfies the exact identity
\[
\operatorname{RelCatSpec}(\mathcal U)=\bigcap_{i<m}\operatorname{RelCatSpec}(\mathcal A_i).
\]
Consequently, if each \(\mathcal A_i\) has a degree \(\mathbf d_i\) of relative computable categoricity, then \(\mathcal U\) has degree
\[
\mathbf d_0\vee\cdots\vee\mathbf d_{m-1}.
\]
Thus the class of degrees of relative computable categoricity is closed under finite Turing joins whenever the input degrees are witnessed by computable structures.

If every \(\mathcal A_i\) is rigid, then \(\mathcal U\) is rigid. Hence finite joins of degrees that have rigid relative-categoricity witnesses again have rigid witnesses.

## Assumptions and scope
A computable structure is relatively \(\mathbf d\)-computably categorical in the sense used by Kalimullin: above the cone based at \(\mathbf d\), every oracle-computable copy admits an isomorphism computable in that same oracle. The relative categoricity spectrum is the set of all such base degrees.

The tags are part of the language and therefore are uniformly available in every presentation. Component relation symbols are renamed before taking the disjoint union so that no relation mixes different components. The theorem is stated for a finite nonempty family; no claim is made for countably many components.

## Proof
It is enough to prove the spectrum identity.

First suppose
\[
\mathbf d\in\bigcap_{i<m}\operatorname{RelCatSpec}(\mathcal A_i).
\]
Let \(\mathbf a\geq_T\mathbf d\), and let \(\mathcal V\cong\mathcal U\) be an \(\mathbf a\)-computable copy. Because the unary predicates \(P_i\) belong to the language, the domain
\[
V_i=\{x:\mathcal V\models P_i(x)\}
\]
is \(\mathbf a\)-computable uniformly in \(i\). With the inherited renamed relations, \(\mathcal V_i\) is an \(\mathbf a\)-computable copy of \(\mathcal A_i\). Since \(\mathbf d\in\operatorname{RelCatSpec}(\mathcal A_i)\), there is an \(\mathbf a\)-computable isomorphism
\[
f_i:\mathcal A_i\cong\mathcal V_i.
\]
The tags make the component domains disjoint, so the union
\[
f=\bigcup_{i<m}f_i
\]
is an \(\mathbf a\)-computable isomorphism \(\mathcal U\cong\mathcal V\). Therefore
\[
\mathbf d\in\operatorname{RelCatSpec}(\mathcal U).
\]
This proves the inclusion from right to left.

Conversely, suppose
\[
\mathbf d\in\operatorname{RelCatSpec}(\mathcal U).
\]
Fix an index \(j<m\), a degree \(\mathbf a\geq_T\mathbf d\), and an arbitrary \(\mathbf a\)-computable copy \(\mathcal B_j\cong\mathcal A_j\). For every \(i\neq j\), use a fixed computable copy of \(\mathcal A_i\). By placing these copies on computably separated columns of \(\omega\), tagging the columns, and putting \(\mathcal B_j\) on the \(j\)-th column, we obtain an \(\mathbf a\)-computable copy \(\mathcal W\cong\mathcal U\).

Relative \(\mathbf d\)-computable categoricity of \(\mathcal U\) gives an \(\mathbf a\)-computable isomorphism
\[
g:\mathcal U\cong\mathcal W.
\]
Every isomorphism preserves the predicate \(P_j\), so the restriction of \(g\) to the \(j\)-th component is an \(\mathbf a\)-computable isomorphism
\[
\mathcal A_j\cong\mathcal B_j.
\]
Since \(\mathbf a\geq_T\mathbf d\) and \(\mathcal B_j\) were arbitrary,
\[
\mathbf d\in\operatorname{RelCatSpec}(\mathcal A_j).
\]
As \(j\) was arbitrary, the reverse inclusion follows.

Now assume that each spectrum has a least degree \(\mathbf d_i\). Relative categoricity spectra are upward closed, so
\[
\operatorname{RelCatSpec}(\mathcal A_i)=\{\mathbf e:\mathbf e\geq_T\mathbf d_i\}.
\]
Their finite intersection is therefore exactly the cone above the finite Turing join
\[
\mathbf d_0\vee\cdots\vee\mathbf d_{m-1},
\]
which proves the degree statement.

Finally, an automorphism of \(\mathcal U\) must preserve every unary tag \(P_i\), and its restriction to the \(i\)-th component is an automorphism of \(\mathcal A_i\). Hence if all components are rigid, every restriction is the identity and so is the whole automorphism. This proves rigidity preservation.

## Verification
The two spectrum inclusions were reconstructed directly from the quantifiers in relative computable categoricity. The forward construction uses computable tags to split an oracle-computable copy into oracle-computable component copies. The reverse construction varies one component copy at a time while keeping all other components computable, so an isomorphism of tagged unions necessarily restricts to the desired component isomorphism.

The least-degree consequence was checked separately: an upward-closed set with least Turing degree \(\mathbf d\) is precisely the cone above \(\mathbf d\), and the intersection of finitely many principal Turing cones is the cone above their finite join.

The included `verify.py` exhaustively checks the finite structural analogue for all binary-relation structures on two points. It verifies that the number of isomorphisms between two tagged two-component unions is the product of the numbers of component isomorphisms, and that a tagged union is rigid exactly when both components are rigid. The script terminates with `VERIFY_OK 65536`.

## Relationship to prior work
Kalimullin studies relative categoricity spectra and degrees of relative computable categoricity, records their Scott-family characterization, and proves general upper bounds and realization results. In particular, the paper explicitly defines \(\operatorname{RelCatSpec}(\mathcal A)\) and its least degree when one exists.

The result here gives an exact finite composition law for those spectra. Tagged disjoint union realizes set-theoretic intersection of relative categoricity spectra, so at the level of least degrees it realizes Turing join. This supplies a closure operation on the class of relative categoricity degrees and preserves rigid witnesses.

## Limitations
The tags are essential to the stated proof. Without named component predicates, isomorphisms may permute or mix isomorphic components, and the spectrum need not decompose by the same argument.

Only finite tagged unions are covered. For infinitely many components, even when every component separately admits an oracle-computable isomorphism, the individual procedures need not be uniformly available from one oracle program, so the finite proof does not automatically extend.

The theorem concerns relative computable categoricity, not ordinary degrees of categoricity. The latter quantify only over computable copies and do not admit the same spectrum-intersection argument without additional hypotheses.

The originality assessment is best-of-knowledge rather than exhaustive.

## References
I. Sh. Kalimullin, “Notes on degrees of relative computable categoricity,” arXiv:2207.08316v3. First public version submitted 17 July 2022.
