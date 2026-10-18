# Sharp scarcity and exact diagonal stabilizer moments for random perfect evolution algebras

## Finding

Let \(q\) be a prime power, \(n\ge2\), and let \(M\) be uniform on \(\mathrm{GL}_n(\mathbb F_q)\). On a marked natural basis define the perfect evolution algebra \(E_M\) by
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=\sum_{j=1}^n M_{ij}e_j.
\]
Let \(D(M)\) be the subgroup of its \(\mathbb F_q\)-linear algebra automorphisms that are diagonal in this basis. Write
\[
G_k(q)=|\mathrm{GL}_k(\mathbb F_q)|=\prod_{j=0}^{k-1}(q^k-q^j),\qquad G_0(q)=1.
\]
Let \(H\le\mathbb F_q^\times\) be the unique subgroup of odd order. Denote by \(\mathcal C\) the set of nontrivial orbits of the squaring permutation \(a\mapsto a^2\) on \(H\setminus\{1\}\), and put \(\ell_C=|C|\). For nonnegative integers \(m_C\), set \(s=\sum_{C\in\mathcal C}\ell_Cm_C\). Then the **exact mean diagonal-stabilizer order** is
\[
\boxed{
\mathbb E_M|D(M)|=\frac{1}{G_n(q)}
\sum_{\substack{(m_C)_{C\in\mathcal C}\ge0\\s\le n}}
\frac{n!}{(n-s)!\prod_{C\in\mathcal C}(m_C!)^{\ell_C}}
G_{n-s}(q)\prod_{C\in\mathcal C}G_{m_C}(q)^{\ell_C}.}
\tag{1}
\]
The empty family contributes \(G_n(q)\); in particular the mean is at least one.

If \(q-1\) is a power of two (including \(q=2\)), then \(D(M)=\{1\}\) for **every** invertible \(M\), independently of dimension.

Otherwise define the arithmetic threshold and its limiting group order by
\[
r=r(q)=\min_{\substack{\ell\mid(q-1)\\\ell\ \mathrm{odd\ prime}}}\operatorname{ord}_{\ell}(2)\ge2,
\qquad h=h(q)=\gcd(q-1,2^r-1)>1.
\tag{2}
\]
Here \(\operatorname{ord}_{\ell}(2)\) is the multiplicative order of two modulo the odd prime \(\ell\). **Every** matrix has trivial diagonal stabilizer when \(n<r\); when \(n\ge r\), matrices with nontrivial diagonal stabilizer exist. As \(n\to\infty\) with \(q\) fixed,
\[
\boxed{
\Pr_M\bigl(|D(M)|>1\bigr)
\sim {n\choose r}(r-1)!(q-1)^r\frac{G_{n-r}(q)}{G_n(q)}
\sim\frac{(q-1)^r}{r}\,n^r q^{-2rn+r^2}.}
\tag{3}
\]
Moreover,
\[
\boxed{\Pr_M\bigl(|D(M)|=h\mid |D(M)|>1\bigr)\longrightarrow1,}
\tag{4}
\]
and the mean in (1) has the sharper asymptotic
\[
\boxed{\mathbb E_M|D(M)|-1\sim (h-1){n\choose r}(r-1)!(q-1)^r\frac{G_{n-r}(q)}{G_n(q)}.}
\tag{5}
\]
Thus the rare nontrivial diagonal symmetry is asymptotically caused by **one isolated directed cycle of the shortest arithmetically permitted length**, and its group is almost always cyclic of order \(h\). Probability refers to the *uniform labelled structure-matrix ensemble*, not to uniformly sampled isomorphism classes or to the full automorphism group.

## Assumptions and scope

All fields are finite, all automorphisms counted are \(\mathbb F_q\)-rational, and the natural basis is marked. The convention for the structure matrix is row-by-source, as displayed above. A diagonal automorphism has the form \(e_i\mapsto d_i e_i\) with \(d_i\in\mathbb F_q^\times\). The primary asymptotic fixes \(q\) and increases \(n\); it is not uniform as \(q\to\infty\). For the assertion involving \(r\), assume \(q-1\) has an odd prime factor. In finite fields, squaring is an automorphism of the odd-order subgroup \(H\), even in characteristic two. In (1), the product over an empty set is one and no term with \(s>n\) appears.

The finite-field moment formula counts the identity plus all nonidentity diagonal automorphisms, and is not an isomorphism-class count. The statements about \(D(M)\) concern its group of points, not a possible nonreduced automorphism group scheme.

## Proof

**1. Scalar constraints and permutation cycles.** Multiplicativity of a diagonal linear map is equivalent to the coefficientwise conditions
\[
M_{ij}\ne0\ \Longrightarrow\ d_j=d_i^2.\tag{6}
\]
Every invertible matrix has a nonzero determinant summand, hence a permutation \(\pi\in S_n\) with \(M_{i,\pi(i)}\ne0\) for all \(i\). Along each cycle of \(\pi\), (6) implies \(d_i^{2^k-1}=1\), where \(k\) is the cycle length. Consequently every \(d_i\) has odd multiplicative order and belongs to \(H\). A nonidentity coordinate lies on a nontrivial squaring orbit of size at least \(r\); this proves \(n<r\Rightarrow D(M)=\{1\}\). If \(H=\{1\}\), this also proves triviality for every \(n\).

**2. Complete fixed-matrix count.** Fix a diagonal tuple \(d=(d_1,\ldots,d_n)\) in \(H^n\). For each \(a\in H\), let \(m_a\) be the number of coordinates equal to \(a\). A row of color \(a\) has entries only in columns of color \(a^2\). Such a matrix can be invertible precisely if \(m_a=m_{a^2}\) for every \(a\); this condition is also sufficient, by choosing invertible blocks. Thus all colors in the squaring orbit \(C\) occur with the same multiplicity \(m_C\), and color \(1\) occurs \(n-s\) times. The number of invertible matrices compatible with this fixed tuple is exactly
\[
G_{n-s}(q)\prod_C G_{m_C}(q)^{\ell_C}.\tag{7}
\]
Indeed, after independently ordering rows and columns by colors, the allowed rectangular blocks become square invertible blocks, with the same determinant criterion as for a block permutation matrix. The number of labelled tuples \(d\) with these prescribed multiplicities is
\[
\frac{n!}{(n-s)!\prod_C(m_C!)^{\ell_C}}.\tag{8}
\]
Sum the fixed-matrix counts over tuples and divide by \(G_n(q)\); interchanging sums proves (1).

**3. Sharp existence threshold.** Every nontrivial orbit of squaring on \(H\) has length \(\operatorname{ord}_t(2)\), where \(t>1\) is the odd order of any of its elements. This length is at least the minimum in (2), and an element of prime order realizing the minimum has orbit length \(r\). For \(n\ge r\), put a weighted directed cycle of length \(r\) on a chosen \(r\)-set, and take the complementary block to be the identity. Every edge weight on the cycle is nonzero; this gives an invertible matrix satisfying (6) for a nontrivial tuple. Hence \(r\) is the exact first dimension in which nontrivial \(D\) is possible.

**4. The dominant event.** Fix \(r\) coordinates and an oriented cycle through them; require that the only nonzero entries in their rows and columns be the cycle edges, with all their \(r\) weights nonzero. The complement is an arbitrary member of \(\mathrm{GL}_{n-r}(\mathbb F_q)\). This event has exactly
\[
(q-1)^r G_{n-r}(q)\tag{9}
\]
matrices. There are \({n\choose r}(r-1)!\) choices of the oriented cycle. Each such matrix has \(h\) diagonal symmetries restricted to the cycle, since choosing its first coordinate \(a\) requires and suffices that \(a^{2^r-1}=1\), and \(h\) is the number of such roots in \(\mathbb F_q^\times\). Minimality of \(r\) ensures every nonidentity choice has nonidentity values at all the cycle coordinates. Conversely, a diagonal symmetry supported on exactly \(r\) coordinates forces precisely one squaring orbit of length \(r\), each color appearing once, so invertibility forces this isolated directed cycle. Thus the union of the displayed events is exactly the event of a nonidentity diagonal symmetry with support \(r\).

Two distinct such events cannot overlap on their vertex sets: an isolated directed cycle on a set cannot preserve a proper nonempty coordinate subset. Different events therefore overlap only if their vertex sets are disjoint. The aggregate pairwise intersection probability is bounded by a constant depending only on \(q,r\) times
\[
n^{2r}(q-1)^{2r}G_{n-2r}(q)/G_n(q),\tag{10}
\]
which is negligible relative to the sum of (9) over all cycles, because \(G_k(q)=q^{k^2}\prod_{j=1}^{k}(1-q^{-j})\), and the product tends to a positive constant as \(k\to\infty\). Therefore the probability of the dominant event equals the first expression in (3), up to relative \(o(1)\).

**5. All larger supports are negligible.** For an automorphism tuple whose support \(s>r\) consists of coordinates not equal to one, every nontrivial squaring orbit \(C\) has length \(\ell_C\ge r\). The dimension (over \(\mathbb F_q\)) of the linear space of compatible structure matrices is
\[
(n-s)^2+\sum_C\ell_Cm_C^2
\le(n-s)^2+s^2/r.\tag{11}
\]
Thus at most \(q^{(n-s)^2+s^2/r}\) compatible matrices exist, without assuming invertibility. There are at most \({n\choose s}(q-2)^s\) choices of nonidentity coordinates on that support. Since \(G_n(q)\ge c_q q^{n^2}\), where \(c_q=\prod_{j\ge1}(1-q^{-j})>0\), the probability that **any** such tuple exists is at most
\[
c_q^{-1}\sum_{s=r+1}^{n}{n\choose s}(q-2)^s
q^{-2ns+(1+1/r)s^2}.\tag{12}
\]
For fixed \(q,r\), choose \(\epsilon=1/(4(r+1))\). In the range \(r+1\le s\le\epsilon n\), the exponent of \(q\) is at most \(-[2-(1+1/r)\epsilon]ns\); the binomial bound \({n\choose s}\le n^s\) makes this a geometric sum with a decay strictly faster than \(q^{-2rn}\). For \(\epsilon n\le s\le n\), the exponent is at most \(-c n^2\) for some \(c=c(r)>0\), by the positivity on that interval of \(2(s/n)-(1+1/r)(s/n)^2\); its sum is \(q^{-\Omega(n^2)}\) after allowing at most \((q-1)^n\) coordinate choices. Therefore (12) is \(o(n^r q^{-2rn})\). This completes (3), including its second asymptotic using \(G_{n-r}/G_n\sim q^{-2rn+r^2}\).

On a matrix with exactly one dominant isolated cycle and no additional supported symmetry, the entire group \(D(M)\) has order \(h\). By the preceding union and tail estimates, the probability of any second dominant cycle or any symmetry of larger support is negligible relative to (3). This proves (4). Finally, the contribution from tuples with support exactly \(r\) to \(\mathbb E(|D|-1)\) is exactly \((h-1){n\choose r}(r-1)!(q-1)^rG_{n-r}/G_n\), because each oriented cycle permits precisely \(h-1\) nonidentity tuples. Estimate (12), which counts all larger-support tuples rather than merely their matrices, makes their expected contribution negligible. This proves (5).

## Verification

The standalone finite-field enumerator `verify.py` exhaustively lists every invertible structure matrix over \(\mathbb F_2\) in dimension three, \(\mathbb F_3\) in dimension three, \(\mathbb F_4\) in dimensions two and three, \(\mathbb F_5\) in dimension two, and \(\mathbb F_7\) in dimension two. It tests the defining relation (6) for **every** possible nonzero diagonal tuple, compares the sum of subgroup sizes with (1), and checks the exact minimal-cycle event counts where applicable. It independently constructs a cyclic witness over \(\mathbb F_8\) in dimension three.

In particular, over \(\mathbb F_4\), among the \(180\) matrices of \(\mathrm{GL}_2\), exactly \(9\) have diagonal stabilizer order \(3\); among the \(181{,}440\) matrices of \(\mathrm{GL}_3\), exactly \(81\) have diagonal stabilizer order \(3\). Over \(\mathbb F_7\), the corresponding two-dimensional figures are \(2{,}016\) matrices and \(36\) exceptional ones. The enumerator returns `VERIFY_OK`. These finite checks do **not** prove the asymptotic: the uniform tail estimates and the dominant-event argument above are essential.

To reproduce: run `python verify.py` with a standard Python 3 interpreter; no third-party packages are used. Finite-field arithmetic in dimensions two and three is implemented in the script (including an explicit polynomial basis for the binary extension fields).

## Relationship to prior work

Elduque–Labra [1] identify the diagonal automorphism group through the directed graph of the structure matrix and establish the general group-scheme framework. Sriwongsa–Zou [2] derive root-of-unity constraints for diagonal symmetries and classify certain maximal diagonal groups, including weighted full cycles, over characteristic-zero fields. These **structural statements are known ingredients** here; neither is claimed as new.

Wei–Zou [3] count isomorphism classes of perfect evolution algebras over finite fields using a Burnside sum over the monomial group, with explicit isomorphism-class numbers in small dimensions. An isomorphism-class count is not the probability that a uniformly chosen invertible *labelled matrix* has a nonidentity **diagonal** stabilizer. Their formal fixed-point framework encompasses the identity-permutation component used in our moment count; the novelty claimed here is the explicit squared-scalar-orbit moment formula and especially the sharp first-symmetry dimension, leading rare-event asymptotic, and conditional stabilizer order in arbitrary dimension.

Rodiño Montoya–Viana Bedoya–Henao [4], first publicly available on 21 May 2025, investigate automorphisms for graph-associated evolution algebras, especially adjacency and random-walk matrices of finite undirected graphs. Those fixed graph supports differ from the uniform \(\mathrm{GL}_n(\mathbb F_q)\) model treated here. Their diagonal-group conditions are compatible with (6) in the graph case but do not give the labelled random-matrix probability law.

## Limitations

The results concern only diagonal automorphisms, not all monomial automorphisms and not the full automorphism-group scheme. The distribution is taken over matrices rather than isomorphism classes, so no conclusion about uniform random isomorphism classes follows. The sharp asymptotic is for fixed \(q\) and \(n\to\infty\); it does not establish a joint limit in \(q,n\). Formula (1) gives a first moment, not the full finite-\(n\) law of \(|D(M)|\). Existing classifications of graph diagonal groups and of full-cycle extremes are acknowledged, and there remains a possibility that equivalent probabilistic estimates occur in unindexed literature.

## References

[1] A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191 (2019), https://arxiv.org/abs/1902.02191. See Section 2 and its diagonal group of a graph.

[2] S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333 (2022), https://arxiv.org/abs/2202.01333. See Theorem 2.2 and Section 4.

[3] Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023), https://arxiv.org/abs/2310.12368. See Sections 1–3 and the Burnside formula.

[4] M. L. Rodiño Montoya, N. A. Viana Bedoya, and C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604, first posted 21 May 2025, https://arxiv.org/abs/2505.15604. See Proposition 2.5 and Theorems 2.9 and 2.17.
