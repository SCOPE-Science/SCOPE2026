# Sharp one-vertex ideal law for random perfect evolution algebras

## Finding
For fixed prime power \(q\), a uniformly chosen labelled perfect evolution algebra of dimension \(n\) over \(\mathbb F_q\) has non-simplicity probability
\[
\Pr(E_M\text{ is not simple})=
\frac{2n(1-q^{-1})q^{1-n}}{1-q^{-n}}+O_q(n^2q^{-2n+4})
\sim2n(1-q^{-1})q^{1-n}
\]
as \(n\to\infty\). Conditional on non-simplicity, with probability tending to one an ideal has dimension \(1\) or codimension \(1\), and these two exclusive mechanisms each have asymptotic conditional probability \(1/2\).

The result also yields an exact cut probability for every subset of natural-basis indices, and a bijection between all ideals and directed outgoing-closed subsets of the nonzero-entry graph.

## Assumptions and scope
Fix any prime power \(q\ge2\). For each integer \(n\ge2\), sample \(M=(M_{ij})\) uniformly from \(\mathrm{GL}_n(\mathbb F_q)\) and form the evolution algebra \(E_M\) with natural basis \(e_1,\ldots,e_n\) and multiplication \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=\sum_jM_{ij}e_j\). Since \(M\) is invertible, \(E_M^2=E_M\): the algebra is perfect. By an ideal we mean a linear subspace \(I\) such that \(IE_M\subseteq I\). Simplicity means that the only ideals are zero and the whole algebra. The support digraph has an arc \(i\to j\) exactly when \(M_{ij}\ne0\). All asymptotics take \(n\to\infty\) for fixed \(q\); no assertion concerns uniformity as \(q\to\infty\) or sampling isomorphism classes.

## Proof
**1. Exact coordinate-ideal correspondence.** Let \(I\) be a nonzero ideal and let \(S\) be the union of supports of all vectors in \(I\). For each \(i\in S\), there is \(x\in I\) with nonzero coefficient \(x_i\). Multiplication by \(e_i\) gives \(x_i e_i^2\in I\), hence \(e_i^2\in I\). Invertibility of \(M\) makes the \(n\) squares linearly independent; therefore \(\dim I\ge |S|\). Every vector of \(I\) is supported on \(S\), so \(\dim I\le|S|\), and consequently \(I=\operatorname{span}\{e_i:i\in S\}\). Such a coordinate subspace is an ideal precisely when \(M_{ij}=0\) for every \(i\in S\) and \(j\notin S\). Conversely, any such subset gives an ideal. A finite directed graph is strongly connected exactly when it has no nonempty proper outgoing-closed subset: if not strongly connected, a sink component in its condensation gives one. This proves the simplicity criterion and classifies all ideals.

**2. Exact probability of a specified ideal.** Put \(c_k(q)=\prod_{j=1}^{k}(1-q^{-j})\), with \(c_0(q)=1\). For a fixed set \(S\) of size \(r\), permuting the basis makes its zero-cut event the block lower-triangular form \(M=\begin{pmatrix}A&0\\C&B\end{pmatrix}\) with \(A\in\mathrm{GL}_r(\mathbb F_q)\), \(B\in\mathrm{GL}_{n-r}(\mathbb F_q)\), and arbitrary \(C\in M_{n-r,r}(\mathbb F_q)\). Dividing the number \(|\mathrm{GL}_r|\,|\mathrm{GL}_{n-r}|q^{r(n-r)}\) by \(|\mathrm{GL}_n|\), and using \(|\mathrm{GL}_k|=q^{k^2}c_k(q)\), gives
\[
\Pr(S\text{ indexes an ideal})=q^{-r(n-r)}\frac{c_r(q)c_{n-r}(q)}{c_n(q)}.
\]
For \(r=1\) or \(r=n-1\), this is exactly \(a_{n,q}=(1-q^{-1})q^{1-n}/(1-q^{-n})\).

**3. Uniform control of other cuts.** Write \(c_\infty(q)=\prod_{j\ge1}(1-q^{-j})>0\). For an arbitrary set of \(t\) entries forced to zero, its probability under uniform \(\mathrm{GL}_n\) is at most \(c_\infty(q)^{-1}q^{-t}\): first ignore invertibility, then divide by \(\Pr(M\text{ invertible})=c_n(q)\ge c_\infty(q)\). Let \(\mathcal A_i\) denote the event that row \(i\) has all its off-diagonal entries zero, and \(\mathcal B_i\) the analogous column event. These are the \(2n\) size-one and size-\(n-1\) cut events, each of probability \(a_{n,q}\). Any two distinct events force at least \(2n-3\) different entries to vanish, so their total pairwise intersection probability is \(O_q(n^2q^{-2n+3})\). Hence by the elementary Bonferroni bounds,
\[
\Pr\Bigl(\bigcup_i(\mathcal A_i\cup\mathcal B_i)\Bigr)=2na_{n,q}+O_q(n^2q^{-2n+3}).
\]
The remaining cut events have sizes \(2\le r\le n-2\), and their union probability is at most
\[
c_\infty(q)^{-1}\sum_{r=2}^{n-2}{n\choose r}q^{-r(n-r)}=O_q(n^2q^{-2n+4}).
\]
For completeness, the last estimate follows by symmetry about \(n/2\). Up to \(\lfloor n/3\rfloor\), successive summands have ratio \(\frac{n-r}{r+1}q^{-(n-2r-1)}=o(1)\), uniformly for \(2\le r\le n/3\), so their sum is bounded by a constant multiple of the \(r=2\) term. For \(n/3\le r\le n/2\), the entire sum is at most \(2^nq^{-2n^2/9+O(n)}=o(n^2q^{-2n+4})\). This proves the displayed estimate and the asymptotic probability formula.

**4. Conditional ideal dimensions.** The union of the \(n\) row-singleton events has probability \(na_{n,q}+O_q(n^2q^{-2n+2})\), and the union of the \(n\) column-singleton events has the same probability. Their intersection has probability \(O_q(n^2q^{-2n+3})\). The other cuts also contribute a lower-order probability by Step 3. Dividing by \(\Pr(E_M\text{ not simple})\sim2na_{n,q}\) yields the claimed equal conditional weights and shows that with conditional probability tending to one at least one extremal-dimensional ideal exists, but not both.

## Verification
Run `python3 verify.py` using Python 3 with no external packages. The independent finite enumerator generates every invertible matrix for \((q,n)\) equal to \((2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\), with \(\mathbb F_4\) implemented as \(\mathbb F_2[t]/(t^2+t+1)\). It checks graph strong connectivity against exhaustive proper outgoing-cut enumeration; also verifies the exact singleton-ideal counts derived above. The observed nonsimple counts are, respectively, \(3,88,8502,20,3728,63,144\) among \(6,168,20160,48,11232,180,480\) invertible matrices. The code does not prove the asymptotic or independently enumerate all non-coordinate ideals; the infinite proof is in Steps 1–4.

## Relationship to prior work
Giacomelli's *Expander Evolution Algebras* (arXiv:2605.12672v1; first public May 12, 2026), Sections 2–3 and 11, develops the graph interpretation of evolution algebras, associated connectivity and simple-algebra questions, but neither its statements nor its proofs count simple algebras in the uniform invertible-matrix ensemble. Elduque and Labra's *Evolution algebras and graphs* (arXiv:1312.4685) is foundational for the graph approach. Rodiño Montoya, Viana Bedoya and Henao's *Group actions and Automorphisms of evolution algebras associated to finite graphs* (arXiv:2505.15604v1), introduction and Sections 2–3, studies automorphisms of prescribed graph algebras, not uniform random structure matrices or ideal probabilities. Classical independent-edge random-digraph connectivity estimates are not directly transferable: conditioning the structure matrix to be invertible changes the leading cut coefficient from \(1\) to \(1-q^{-1}\), determined here exactly. The novelty asserted is this conditioned sharp asymptotic and the asymptotic two-way ideal-type law, not the known graph criterion or matrix group order.

## Limitations
This is a self-review, not an independent audit or a verified publication-priority claim. The result is for *labelled* full-rank structure matrices and fixed \(q\). It does not determine a full finite-dimensional distribution of all ideals and does not address sparse ensembles or isomorphism-weighted probabilities. An equivalent unindexed matrix-support connectivity result cannot be excluded merely from negative searches; general random-matrix zero-pattern theorems remain a bibliographic comparison risk. The finite checker independently tests the graph and matrix counts, while the algebraic ideal correspondence and uniform error bound rely on the written proof.

## References
1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (May 12, 2026), Sections 2–3 and 11, https://arxiv.org/html/2605.12672v1.
2. M. L. Rodiño Montoya, N. A. Viana Bedoya, C. Henao, *Group actions and Automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604v1 (May 21, 2025), https://arxiv.org/html/2505.15604v1.
3. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685 (2013), https://arxiv.org/abs/1312.4685.
4. D. Salmond, A. Grant, I. Grivell, T. Chan, *On the rank of random matrices over finite fields*, arXiv:1404.3250 (2014), abstract and stated zero-constraint rank bounds, https://arxiv.org/abs/1404.3250.
