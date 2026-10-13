# Binomial image-rank laws for finite S4.3 cluster-chain modal algebras

## Finding

Consider any finite reflexive linear-preorder Kripke frame whose equivalence clusters have ordered positive sizes \(a_0,\ldots,a_{h-1}\). Every bounded self-morphism is described by a nondecreasing surjection of the cluster-index chain onto a terminal interval; in each fiber, the **last source cluster** must map onto the corresponding target cluster, while all earlier source clusters map there arbitrarily. This supplies exact endomorphism and idempotent image-cardinality polynomials for every unequal cluster profile.

For equal cluster sizes \(a_i=r\ge1\), the endomorphism image-length statistic has the exact distribution
\[
L=1+\operatorname{Binomial}\!\left(h-1,\frac{r!}{r!+r^r}\right)
\]
when the bounded endomorphism is selected uniformly. Its rank polynomial, where the exponent measures the cardinality of the **algebraic image**, is
\[
E_{r,h}(z)=\sum_{\ell=1}^{h}
\binom{h-1}{\ell-1}(r!)^\ell r^{r(h-\ell)}z^{2^{r\ell}}.
\]
The corresponding idempotent polynomial is
\[
I_{r,h}(z)=\sum_{\ell=1}^{h}r^{r(h-\ell)}z^{2^{r\ell}}.
\]
In particular, the proportion of idempotent endomorphisms tends to zero exponentially in the number of clusters (for each fixed \(r\)); all \(h\) terminal-cluster image lengths actually occur.

## Assumptions and scope

Fix an integer \(h\ge1\) and positive integers \(a_0,\ldots,a_{h-1}\). Let \(W=C_0\sqcup\cdots\sqcup C_{h-1}\), with \(|C_i|=a_i\), and define \(xRy\) exactly when the index of \(x\) is at most the index of \(y\). This relation is reflexive, transitive, and weakly connected: it is a finite S4.3-frame in the usual modal-logic sense. Write \(U_i=C_i\sqcup\cdots\sqcup C_{h-1}\). Its Boolean modal algebra \(\mathcal A\) is the power-set algebra \(\mathcal P(W)\) equipped with \(\Diamond S=\{x\in W:\exists y\in S\ (xRy)\}\).

A **bounded morphism** \(f:W\to W\) preserves the relation and satisfies the back condition: \(f(x)Rz\) implies that \(xRy\) and \(f(y)=z\) for some \(y\). Equivalently, \(f[\{y:xRy\}]=\{z:f(x)Rz\}\) at every \(x\). Finite Boolean modal duality identifies these maps contravariantly with all endomorphisms of \(\mathcal A\), through inverse image \(S\mapsto f^{-1}[S]\). The image of this algebra endomorphism has \(2^{|f[W]|}\) elements, not merely \(|f[W]|\) elements. Idempotence is preserved by this correspondence.

For \(n\ge0\) and \(k\ge0\), let \(Q(n,k)=k!\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) count surjections from an \(n\)-element labelled set onto a \(k\)-element labelled set, with \(Q(n,k)=0\) when \(n<k\). Define \(N_t=\sum_{i=t}^{h-1}a_i\). All index intervals are inclusive and an empty sum is zero.

**Arbitrary-cluster theorem.** For each \(0\le t<h\), consider all ordered positive compositions
\[
b_t+\cdots+b_{h-1}=h,\qquad b_j\ge1.
\]
Put \(q_t=0\), \(q_{j+1}=q_j+b_j\), and \(s_j=q_j+b_j-1\), so that source indices \(q_j,\ldots,s_j\) form the block mapping to target index \(j\). The two exact polynomials are
\[
\begin{aligned}
E_{\boldsymbol a}(z)&=\sum_{t=0}^{h-1} z^{2^{N_t}}
\sum_{\substack{b_t+\cdots+b_{h-1}=h\\b_j\ge1}}
\prod_{j=t}^{h-1}a_j^{\sum_{i=q_j}^{s_j-1}a_i}
Q(a_{s_j},a_j),\\
I_{\boldsymbol a}(z)&=\sum_{t=0}^{h-1}
 a_t^{\sum_{i=0}^{t-1}a_i}z^{2^{N_t}}.
\end{aligned}
\]
The coefficient of \(z^m\) is the number of (respectively all, idempotent) modal-algebra endomorphisms whose **algebraic** image has \(m\) elements. The possible image cardinalities are exactly \(2^{N_t}\) for \(0\le t<h\). There are exactly \(h\) different images as subsets of the **dual frame** obtainable by bounded idempotent retractions, namely \(U_0,\ldots,U_{h-1}\); different retractions of a fixed dual support can still yield distinct embedded algebraic image subalgebras.

**Homogeneous specialization.** If \(a_i=r\) for all \(i\), then
\[
|\operatorname{End}(\mathcal A)|=r!\,(r!+r^r)^{h-1},
\qquad
|\operatorname{Idem}(\mathcal A)|=\sum_{j=0}^{h-1}r^{rj}.
\]
For \(r\ge2\), the latter total equals \((r^{rh}-1)/(r^r-1)\); for \(r=1\), it equals \(h\). If \(r\ge2\), the idempotent probability is asymptotic to
\[
\frac{r^r}{r!(r^r-1)}
\left(\frac{r^r}{r!+r^r}\right)^{h-1};
\]
for \(r=1\) it is exactly \(h/2^{h-1}\). Thus the probability tends to zero exponentially for every fixed positive \(r\).

For example, for three clusters of size two the 64-element Boolean modal algebra has
\[
E_{2,3}(z)=32z^4+32z^{16}+8z^{64},\qquad
I_{2,3}(z)=16z^4+4z^{16}+z^{64}.
\]
It therefore has 72 endomorphisms and 21 idempotents.

## Proof

**1. Fiber normal form.** Whenever \(x\) and \(x'\) lie in one cluster, \(xRx'\) and \(x'Rx\). The forward clause forces \(f(x)Rf(x')\) and \(f(x')Rf(x)\), so their images lie in one target cluster. We obtain a function \(\phi:\{0,\ldots,h-1\}\to\{0,\ldots,h-1\}\) such that \(f[C_i]\subseteq C_{\phi(i)}\). Relation preservation implies that \(\phi\) is nondecreasing. For every \(x\in C_i\), the successors of \(x\) are exactly \(U_i\); the back and forth clauses together give
\[
f[U_i]=U_{\phi(i)}.
\]
In particular, setting \(t=\phi(0)\), we have \(f[W]=U_t\). Since every cluster of \(U_t\) must be hit, \(\phi\) is a nondecreasing surjection onto the consecutive indices \(t,\ldots,h-1\). The inverse images of these indices are nonempty consecutive blocks \([q_j,s_j]\). At the last source index \(s_j\) of each block, all strictly higher source clusters go to strictly higher target clusters. Consequently, \(f[U_{s_j}]=U_j\) holds only if \(f[C_{s_j}]=C_j\). Conversely, if each last-cluster map is surjective, then every suffix beginning inside that block hits all of \(C_j\) through the last cluster and hits every higher target cluster through the following blocks. Hence \(f[U_i]=U_{\phi(i)}\) at every \(i\). This proves necessity and sufficiency without any assumption that the cluster sizes coincide.

**2. Counting the normal forms.** Fix \(t\) and a block composition. For each target block \(j\), its last source cluster has \(Q(a_{s_j},a_j)\) surjective maps to \(C_j\). Earlier source clusters in that block have \(a_j^{\sum_{i=q_j}^{s_j-1}a_i}\) independent maps. These choices across blocks are independent and determine the bounded morphism uniquely. Different choices of \(t\) or the composition give disjoint maps. The image set is \(U_t\), so the corresponding algebraic image has \(2^{N_t}\) elements. Summation gives \(E_{\boldsymbol a}\).

**3. Idempotents.** A function is idempotent exactly when it fixes every point of its image. Thus a bounded idempotent with image \(U_t\) fixes each point of \(U_t\) and in particular has \(\phi(i)=i\) for \(i\ge t\). For \(i<t\), monotonicity gives \(\phi(i)\le\phi(t)=t\), while the image restriction \(f[W]=U_t\) gives \(\phi(i)\ge t\). Thus \(\phi(i)=t\). Conversely, fixing all of \(U_t\) and mapping each earlier point arbitrarily into \(C_t\) gives an idempotent bounded morphism: each successor suffix maps onto precisely the required target suffix. There are \(a_t^{\sum_{i<t}a_i}\) such retractions. This proves \(I_{\boldsymbol a}\), the complete rank support, and existence of exactly the \(h\) dual suffix supports.

**4. Homogeneous binomial law.** When every cluster has size \(r\), the surjection from a last source cluster onto its equally sized target cluster is a permutation with \(r!\) choices. Each other source cluster in the block has \(r^r\) arbitrary maps. For a target suffix with \(\ell\) clusters, there are \(\binom{h-1}{\ell-1}\) positive source-block compositions. Every such composition contributes \((r!)^\ell r^{r(h-\ell)}\) maps. This proves the polynomial and its binomial normalization. Summing with the binomial theorem gives the total endomorphism count. Substituting the idempotent count from step 3 gives the geometric sum and the stated exponential asymptotics. No limiting or computational assumption enters the proof.

## Verification

A self-contained Python 3 standard-library verifier is included as `verify.py`. Run `python3 verify.py` from the directory containing this file. It constructs the accessibility relation directly from every positive integer composition of total world count at most six; exhaustively enumerates all world functions and independently checks the defining successor-image identity, counts algebraic image ranks and idempotents, and compares both with the theorem. Selected seven-world profiles are also exhaustively checked. For the smallest cases it independently checks preservation of the modal diamond operator on every subset, and it evaluates the homogeneous closed formulas for cluster sizes one through five and heights one through eight.

Observed output:

`VERIFY_OK 65 shapes 3192243 full function tables 6038 bounded endomorphisms 600 exact comparison assertions`

The exhaustive checks are finite consistency tests, not a replacement for the general proof. The bounds and exact test coverage are visible in the standalone source.

## Relationship to prior work

Kurucz, Wolter and Zakharyaschev's paper on interpolation in logics extending K4.3 uses chains of Kripke clusters and describes the modal and bisimulation setting. Its mathematical task is interpolation decidability; the inspected full text does not state these endomorphism or idempotent rank enumerations. Thomason's categorical treatment supplies the underlying standard frame–modal-algebra duality rather than the cluster-profile formulas. Classical Stirling surjection counts and the binomial theorem are used but not claimed as novel. The contribution here is the combined cluster-block normal form, full arbitrary-profile rank census, and its exact homogeneous probability law.

A finite **weak order as a poset** (antichains stacked in levels) should not be conflated with this total **preorder** (reflexive equivalence clusters); bounded morphisms require both a back condition and preservation of mutual accessibility. Counts or homotopy statements about ordinary monotone maps of weak-order posets do not imply the formulas above.

## Limitations

Only finite reflexive linear-preorder frames are covered. Nothing here asserts the same formulas for general K4.3 frames with irreflexive singleton clusters, branching transitive frames, or infinite descriptive frames. The algebraic image rank is a power of two and must not be mistaken for world-image cardinality. The claim makes no assertion about the number of different embedded retract subalgebras with a fixed dual support. The literature comparison is targeted rather than exhaustive: a semigroup-theoretic equivalent under another description may exist. The argument and code have not undergone independent mathematical audit.

## References

1. Agi Kurucz, Frank Wolter, and Michael Zakharyaschev, *A non-uniform view of Craig interpolation in modal logics with linear frames*, arXiv:2312.05929, first submitted 2023-12-10, primary MSC 03B45. Original arXiv abstract and current full text: https://arxiv.org/abs/2312.05929 and https://arxiv.org/pdf/2312.05929 .
2. S. K. Thomason, *Categories of frames for modal logic*, *Journal of Symbolic Logic* 40 (1975), 439–442; online article record https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/categories-of-frames-for-modal-logic1/2883BDF8CF20F5751D54776C35B0D244 . The finite modal-algebra/finite-frame duality is background, not a new result.
3. R. A. Bull, *That All Normal Extensions of S4.3 Have the Finite Model Property*, *Zeitschrift für mathematische Logik und Grundlagen der Mathematik* 12 (1966), 341–344, https://doi.org/10.1002/malq.19660120129 . This is foundational S4.3 literature, not an enumeration of maps.
