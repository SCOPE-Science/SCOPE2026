# Coordinate rigidity and weighted idempotent spectra for finite Gödel-product EARS algebras

## Finding

The equivalential algebra with semilattice of regular elements (EARS) associated with an \(m\)-element Gödel/Heyting chain is the algebra \(A_m=(C_m,\leftrightarrow,\widetilde\wedge)\), for \(m\ge2\). For every finite nonempty list of integers \(m_1,\ldots,m_r\ge2\) and \(n_1,\ldots,n_s\ge2\), **every** EARS-homomorphism
\[
 f:\prod_{i=1}^{r}A_{m_i}\longrightarrow\prod_{j=1}^{s}A_{n_j}
\]
has the following unique coordinate normal form: for every output coordinate \(j\), either \(f_j\) is the constant map with value \(1\), or there is a unique input coordinate \(i\) and a unique nonconstant homomorphism \(\varphi_{ij}:A_{m_i}\to A_{n_j}\) such that \(f_j=\varphi_{ij}\circ\pi_i\). Thus one output coordinate cannot genuinely depend on two input coordinates.

The number of nonconstant scalar homomorphisms is
\[
 h(m,n)=\sum_{k=0}^{\min(m-2,n-2)}\binom{n-2}{k},
\]
so this is the exact **product-to-product hom-set census**:
\[
 \boxed{\left|\operatorname{Hom}_{\mathrm{EARS}}\!\left(\prod_{i=1}^{r}A_{m_i},\prod_{j=1}^{s}A_{n_j}\right)\right|
 =\prod_{j=1}^{s}\left(1+\sum_{i=1}^{r}h(m_i,n_j)\right).}
\]
In particular, with \(E_{m,r}=A_m^r\),
\[
 \boxed{|\operatorname{End}(E_{m,r})|=(1+r2^{m-2})^r,\qquad
 \operatorname{Aut}(E_{m,r})\cong S_r.}
\]

There is also a closed **weighted-rooted-star enumeration of idempotents**, or equivalently retract maps. Put
\[
 w_{m,p}=\sum_{k=0}^{p}\binom{m-2}{k}
 \quad (0\le p\le m-2),
\]
and let \(I_{m,r}\) be the number of idempotent endomorphisms of \(E_{m,r}\), with \(I_{m,0}=1\). Then
\[
 \boxed{I_{m,r}=\sum_{t=0}^{r}\binom rt
   \sum_{(p_1,\ldots,p_t)\in\{0,\ldots,m-2\}^{t}}
       \left(1+\sum_{a=1}^{t}w_{m,p_a}\right)^{r-t}.}
\]
Equivalently, all ranks have the exponential generating function
\[
 \boxed{\sum_{r\ge0} I_{m,r}\frac{z^r}{r!}
 =\exp\!\left(z+z\sum_{p=0}^{m-2}\exp(w_{m,p}z)\right).}
\]
For example, the three-valued case \(m=3\) yields \(|\operatorname{End}(E_{3,r})|=(1+2r)^r\), automorphism group \(S_r\), and
\[
 \sum_{r\ge0}I_{3,r}\frac{z^r}{r!}=\exp(z+ze^z+ze^{2z}),
\]
with \(I_{3,0},I_{3,1},I_{3,2},I_{3,3},I_{3,4}=1,3,15,96,729\).

## Assumptions and scope

The underlying chain is \(C_m=\{x_0<\cdots<x_{m-1}\}\), with bottom \(x_0=0\) and top \(x_{m-1}=1\), equipped with its ordinary Gödel Heyting operations. For elements identified with their integer indices, the two **reduct** operations are precisely
\[
 a\leftrightarrow b=\begin{cases}m-1,&a=b,\\ \min(a,b),&a\ne b,\end{cases}
 \qquad
 a\widetilde\wedge b=\begin{cases}0,&a=0\text{ or }b=0,\\m-1,&a,b>0.\end{cases}
\]
Here \(a\widetilde\wedge b=(\neg\neg a)\wedge(\neg\neg b)\); it is **not** ordinary chain meet. A homomorphism must preserve exactly the two displayed binary operations, not an unmentioned constant \(0\) or the full Heyting signature. This distinction is essential: the constant-\(1\) map is an EARS homomorphism, but is not a homomorphism of nontrivial Heyting algebras. Products use these operations coordinatewise.

The product-rigidity and hom-set formulas apply to nonempty products with factors of size at least two. The idempotent EGF uses the empty product only as the standard one-element convention. All statements concern the stated finite-product subclass; no classification of general EARS algebras is asserted.

## Proof

**1. Scalar maps.** The term \(a\leftrightarrow a\) is always \(1\), so every homomorphism \(g:A_m\to A_n\) satisfies \(g(1)=1\). Because \(0\widetilde\wedge0=0\), the value \(g(0)\) must be idempotent for target \(\widetilde\wedge\), hence is \(0\) or \(1\). If \(g(0)=1\), then for each \(a>0\) the identity \(0\leftrightarrow a=0\) gives \(1=1\leftrightarrow g(a)=g(a)\), so \(g\equiv1\). Otherwise, \(g(0)=0\); then \(g(a)\ne0\) for every \(a>0\), because \(g(0\leftrightarrow a)=0\) but \(0\leftrightarrow0=1\).

For \(0<a<b\), the identity \(a\leftrightarrow b=a\) gives \(g(a)\leftrightarrow g(b)=g(a)\). With both values positive, the target operation forces either \(g(a)<g(b)\) or \(g(a)=g(b)=1\). Thus exactly an initial segment of \(k\) intermediate source levels maps strictly increasingly into the \(n-2\) intermediate target levels, with all remaining intermediate levels mapping to \(1\). Here \(0\le k\le\min(m-2,n-2)\). Choosing their \(k\) distinct target levels determines the map. Conversely each such map preserves \(\leftrightarrow\) by the displayed table and preserves \(\widetilde\wedge\) because it maps \(0\) to \(0\) and every positive element to a positive element. This proves the scalar classification and \(h(m,n)\).

**2. Coordinate rigidity.** Let \(g:\prod_iA_{m_i}\to A_n\) be a homomorphism. The map \(\iota_i:A_{m_i}\to\prod_j A_{m_j}\) inserting an element in coordinate \(i\) and \(1\) elsewhere is a homomorphism. Hence each \(g_i=g\circ\iota_i\) is either constant \(1\) or one of the nonconstant scalar maps, and in the latter case \(g_i(0)=0\).

Suppose that two of these restrictions, say \(g_i,g_j\) with \(i\ne j\), are nonconstant. Let \(u=\iota_i(0)\) and \(v=\iota_j(0)\). Coordinate by coordinate,
\[
 u\leftrightarrow v=u\widetilde\wedge v,
\]
since the only ordered coordinate pairs occurring are \((0,1)\), \((1,0)\), and \((1,1)\). But \(g(u)=g(v)=0\), whereas \(0\leftrightarrow0=1\ne0=0\widetilde\wedge0\); contradiction. Therefore at most one \(g_i\) is nonconstant. Every source tuple decomposes as an iterated \(\leftrightarrow\)-product of the \(\iota_i(x_i)\) (all other coordinates are \(1\), the identity for \(\leftrightarrow\)). Consequently, if every \(g_i\) is constant \(1\), so is \(g\); otherwise \(g=g_i\circ\pi_i\). Uniqueness follows by varying that coordinate while holding all others at \(1\). Applying this argument independently to each target factor proves the normal form and product hom-set formula.

**3. Units.** In a self-map of \(E_{m,r}\), every nonconstant output chooses one source coordinate and a nonconstant scalar map. A bijection must use every input coordinate, hence these choices form a permutation, and each scalar map must be bijective. The only bijective scalar homomorphism \(A_m\to A_m\) is the identity (strict order preservation on the fixed finite chain). Thus the unit group is precisely \(S_r\), permuting factors.

**4. Idempotents.** A nonconstant scalar idempotent \(q:A_m\to A_m\) must be one of the \(m-1\) prefix retractions
\[
 \rho_p(x_i)=\begin{cases}x_i,&0\le i\le p,\\1,&p<i<m-1,\\1,&i=m-1,\end{cases}
 \qquad 0\le p\le m-2.
\]
Indeed every nonconstant scalar endomorphism maps its \(k\) surviving intermediate levels strictly increasingly and can only move a level upward; if any such level moved strictly upward, its image could not already be fixed under the same strict-increase rule, contradicting idempotence. Hence all surviving levels are fixed, and the remainder collapse to \(1\).

Represent a general self-map \(F\) of \(E_{m,r}\) by a directed edge \(j\to i\) labelled by a nonconstant scalar endomorphism \(\varphi_j\), when output \(j\) depends on input \(i\); otherwise mark \(j\) as a **null** (constant-\(1\)) output. If \(F^2=F\) and \(j\to i\) occurs, the coordinate identity forces output \(i\) to be a fixed-point loop \(i\to i\). Its loop label is one of the \(\rho_p\). This follows because otherwise \(F^2_j\) is constant or depends on a different input coordinate, while \(F_j\) depends nontrivially on \(i\). Furthermore the arrow label must satisfy
\[
 \varphi_j\circ\rho_p=\varphi_j.
\]
By scalar normal form, this is equivalent to \(\varphi_j\) collapsing every intermediate source level strictly above \(p\), so there are exactly \(w_{m,p}\) allowed labels.

Conversely any directed graph in which each nonnull nonroot vertex points to a chosen fixed-point loop, with a compatible label, and every other vertex is null, defines an idempotent. Choose \(t\) labelled root vertices, assign them prefix types \(p_1,\ldots,p_t\), and for each remaining labelled vertex choose either null (one choice) or one of \(w_{m,p_a}\) arrows to root \(a\). This gives the finite-sum expression for \(I_{m,r}\). Equivalently, the idempotents are labelled sets of components: singleton null vertices contribute \(\exp(z)\); a root of type \(p\) and an arbitrary set of \(w_{m,p}\)-decorated incoming leaves contribute \(z\exp(w_{m,p}z)\). The labelled exponential formula yields the displayed EGF.

## Verification

The included standalone standard-library script `verify.py` independently constructs the two binary operation tables and exhaustively screens **15,024** possible scalar assignments for all \(2\le m,n\le6\) with the top-preservation constraint. It separately screens **72,380** possible product-to-chain maps across five small mixed/homogeneous sources, confirming the coordinate normal forms, and exhaustively checks all \(4^4\) candidate set maps of the four-element Boolean square for endomorphism status. It operation-checks **811** constructed product endomorphism tables on **457,673** ordered argument pairs, with both operations checked on every pair, and independently checks idempotent normal forms, automorphism counts, and the EGF coefficients through power rank six for \(2\le m\le6\). The final replay reports **`VERIFY_OK_CERTIFIED 934995 exact assertions`**. These finite tests are independent of each other's implementations of the count, but do not replace the general proof above and are not an external mathematical audit.

## Relationship to prior work

Lipka and Słomczyńska introduced EARS as the algebraic semantics of the mixed \((\leftrightarrow,\widetilde\wedge)\) fragment of intuitionistic propositional logic, and proved the representation, local finiteness, and other structural theorems. Przybyło previously studied the subvariety generated by the three-element example, including its representation and free spectra. Those papers furnish the setting but the inspected full texts do not state the finite-product coordinate rigidity, the product hom-set formula, or the weighted idempotent EGF. Their retraction results are different: a general family of EARS retractions is known; the point here is the exact combinatorics of **all** idempotent self-maps of \(A_m^r\).

Counting homomorphisms between **Gödel algebras in the full Heyting signature** has been studied separately by Aguzzoli and Mordonini (2025). The ordinary chain-homomorphism count supplies a closely related scalar binomial sum. It does not automatically classify maps in the smaller EARS signature, where preservation of \(0\) is not required and constant-\(1\) coordinate maps are additional. For example, the four-element Boolean square has **9** EARS endomorphisms but only **4** bottom-preserving Boolean/Heyting endomorphisms. The coordinate-rigidity lemma and weighted-star idempotent EGF identify the extra structure. No theorem of novelty against inaccessible or unindexed sources is asserted.

## Limitations

The theorem is confined to finite products of Gödel-chain EARS reducts. It does not count morphisms among arbitrary EARS algebras or classify retract subalgebras up to isomorphism (only idempotent maps are counted). The literature search found no equivalent product-rigidity plus weighted-EGF theorem in inspected sources or indexed result summaries, but it cannot exclude an unindexed treatment or a general semigroup theorem from which these formulas follow. Independent mathematical audit has not yet been performed.

## References

1. E. Lipka and K. Słomczyńska, *Algebraic Semantics for a Mixed Type Fragment of IPC*, Studia Logica, first published online October 3, 2024. DOI: https://doi.org/10.1007/s11225-024-10117-1 ; open primary text: https://link.springer.com/content/pdf/10.1007/s11225-024-10117-1.pdf . Primary MSC 03G25.
2. S. Przybyło, *Equivalential algebras with conjunction on the regular elements*, Annales Universitatis Paedagogicae Cracoviensis Studia Mathematica (2021). https://studmath.uken.krakow.pl/article/download/8501/7804/26251 .
3. S. Aguzzoli and M. Mordonini, *Counting Homomorphisms Between Finite Gödel Algebras*, Information Processing and Management of Uncertainty in Knowledge-Based Systems (2025), pp. 365–377. DOI: https://doi.org/10.1007/978-3-031-74000-8_30 . The publisher full text was not accessed; the published abstract and bibliographic record were checked.
4. E. T. Lipka, *Fregean fragments of intuitionistic propositional logic* (2025 dissertation), accessible at https://rep.up.krakow.pl/xmlui/bitstream/handle/11716/13749/ETLipka-praca_doktorska.pdf?isAllowed=y&sequence=1 . Relevant EARS chapters and targeted text searches were inspected, not all 122 pages.
