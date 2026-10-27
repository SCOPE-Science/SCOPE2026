# Exact zero forcing and nullity for nonuniform long-legged spider powers

## Finding

Let \(T=S(\ell_1,\ldots,\ell_m)\) be a spider with \(m\ge3\) arms of edge lengths \(\ell_i\ge k+1\), where \(k\ge3\) is an integer and **the arm lengths are not all equal**. The \(k\)-th ordinary graph power joins distinct vertices whenever their distance in \(T\) is at most \(k\). Then

\[
Z(T^k)=M_{\mathbb R}(T^k)=(m-1)k,
\qquad
\operatorname{mr}_{\mathbb R}(T^k)=1+\sum_{i=1}^m\ell_i-(m-1)k.
\]

Here \(Z\) is ordinary zero forcing, and \(M_{\mathbb R}\) is the maximum nullity among real symmetric matrices having **nonzero entries at exactly the edges** of the graph (off diagonal). In particular, the exact parameter is independent of the individual arm lengths once each arm is sufficiently long. An explicit real symmetric matrix realizes the nullity and an explicit forcing schedule realizes the matching upper bound.

## Assumptions and scope

All graphs are finite, simple, and undirected. Write \(c\) for the central vertex and \(v_{i,a}\) for the vertex at distance \(a\in\{1,\ldots,\ell_i\}\) on arm \(i\). Distances are \(d(c,v_{i,a})=a\), \(d(v_{i,a},v_{i,b})=|a-b|\), and \(d(v_{i,a},v_{j,b})=a+b\) when \(i\ne j\). A black vertex forces its sole white neighbor, and a zero-forcing set is an initial black set that admits a sequence coloring every vertex. We prove the formula for every \(m\ge3\), \(k\ge3\), and independently chosen \(\ell_i\ge k+1\), subject to at least two distinct lengths; no upper bound on any length is assumed.

## Proof

**1. Matching forcing upper bound.** Initially blacken the \(k\) outermost vertices in each of the first \(m-1\) arms, leaving the last arm initially white. In each of the first \(m-1\) arms, for \(a=\ell_i-k,\ell_i-k-1,\ldots,1\), perform \(v_{i,a+k}\to v_{i,a}\). At each move the forcer is more than \(k\) edges from \(c\), so it has no neighbors outside its arm, and all its other same-arm neighbors are black. All first \(m-1\) arms are now black. Perform \(v_{1,k}\to c\); then for \(a=1,\ldots,k-1\), perform \(v_{1,k-a}\to v_{m,a}\); then \(c\to v_{m,k}\); finally for \(a=k+1,\ldots,\ell_m\), perform \(v_{m,a-k}\to v_{m,a}\). At each stage, the indicated vertex is the only white neighbor of the forcer, by the displayed distance formulas. The first set has cardinality \((m-1)k\), proving \(Z(T^k)\le(m-1)k\).

**2. Synchronized length-dependent window kernels.** For each arm set \(r_i=\ell_i-k\ge1\), and define the real matrix \(R_i\in\mathbb R^{r_i\times\ell_i}\) by
\[
(R_i)_{s,a}=\mathbf1_{\{s\le a\le s+k\}},\qquad 1\le s\le r_i,\quad 1\le a\le\ell_i.
\]
Its first \(r_i\) columns form an upper-triangular matrix with diagonal entries one, so \(\operatorname{rank}R_i=r_i\) and \(\dim\ker R_i=k\). For any \(u=(u_1,\ldots,u_k)\in\mathbb R^k\), there is a unique vector \(w^{(i)}(u)\in\ker R_i\) whose first \(k\) coordinates are \(u\): obtain it from the recurrence
\[
 w_{s+k}=-\sum_{a=s}^{s+k-1}w_a,\qquad s=1,\ldots,\ell_i-k.
\]
These maps are linear and, importantly, their first \(k\) coordinates agree across every arm regardless of arm length.

**3. A matrix with exactly the desired off-diagonal support.** Index a real symmetric matrix \(X\) by the center and all arm vertices. Put \(X_{cc}=0\) and
\[
X_{c,(i,a)}=\mathbf1_{\{a\le k\}},
\qquad
X_{(i,a),(j,b)}=\begin{cases}
(R_i^{\mathsf T}R_i)_{a,b}+\mathbf1_{\{a+b\le k\}},&i=j,\\
\mathbf1_{\{a+b\le k\}},&i\ne j.
\end{cases}
\]
The diagonal is unconstrained. For distinct vertices on the same arm, \((R_i^{\mathsf T}R_i)_{a,b}\) is positive exactly when \(|a-b|\le k\): such a pair is contained in a length-\((k+1)\) window with starting position between \(1\) and \(\ell_i-k\), since \(\ell_i\ge k+1\). There is no cancellation because all entries are nonnegative. Cross-arm and center entries have precisely the distance-dependent supports listed above. Thus \(X\in\mathcal S(T^k)\), where \(\mathcal S\) means exact, not merely contained, off-diagonal graph support.

**4. Nullspace dimension.** For each \(u\in\mathbb R^k\) and coefficient vector \(\alpha=(\alpha_1,\ldots,\alpha_m)\) with \(\sum_i\alpha_i=0\), form \(x\in\mathbb R^{1+\sum\ell_i}\) with center coordinate zero and arm \(i\) equal to \(\alpha_iw^{(i)}(u)\). Each Gram block vanishes against its arm vector because \(R_iw^{(i)}(u)=0\). For an arm position \(a\), the remaining coupling contribution equals
\[
 \sum_{j=1}^m\alpha_j\sum_{b=1}^{k-a}u_b=0,
\]
where an empty sum is zero; this follows because \(a+b\le k\) only involves the common first \(k\) coordinates. The center row equals \((\sum_i\alpha_i)(\sum_{a=1}^ku_a)=0\). Hence \(Xx=0\).

Choose \(\alpha=e_i-e_m\) for \(i=1,\ldots,m-1\), and \(u=e_t\) for \(t=1,\ldots,k\). The resulting \((m-1)k\) kernel vectors are linearly independent, since the first \(k\) coordinates in arms \(1,\ldots,m-1\) form an identity matrix. Therefore \(M_{\mathbb R}(T^k)\ge\operatorname{nullity}X\ge(m-1)k\).

**5. Equality and rank.** The standard zero-forcing/nullity inequality \(M_{\mathbb R}(H)\le Z(H)\) for every graph \(H\), combined with steps 1 and 4, gives equality. Finally \(\operatorname{mr}_{\mathbb R}(H)=|V(H)|-M_{\mathbb R}(H)\), with \(|V(T)|=1+\sum_i\ell_i\). This completes the proof. \(\square\)

## Verification

The accompanying executable `verify.py` constructs the graph from the distance metric, constructs the explicit integer matrix and \((m-1)k\) null vectors, checks exact off-diagonal support, checks matrix–vector products and linear independence, and replays every force with the unique-white-neighbor rule. It checked 48 heterogeneous parameter instances involving powers \(1\) to \(4\) and two to five arms, including all the theorem's structural ingredients; it additionally ruled out smaller forcing sets by full subset enumeration in five small cases. The output was `VERIFY_OK heterogeneous_cases=48 explicit_null_vectors=300 verified_forces=516 exhaustive_cases=5`. To replay: `python3 verify.py`. This finite testing complements, but does not replace, the general proof above.

## Relationship to prior work

Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker (2026), Proposition 9, give the same forcing upper bound for **equal-length** spiders, and their Conjecture 10 asks for exact equality in that uniform family. Previously obtained exact uniform-arm results for powers three and higher concern only equal lengths. Their statements do not immediately determine an arbitrary unbalanced-length spider: zero forcing and maximum nullity are not generally preserved under adding or deleting vertices, and the unequal arm lengths eliminate the direct uniform-arm symmetry. The present theorem addresses the whole genuinely nonuniform, long-legged domain with a synchronized common-initial-data kernel across unequal-length window matrices. Chang and Lin (2013) settle graph squares of all trees, so the restriction \(k\ge3\) excludes that already-covered case. DeAlba and collaborators (2012) treat powers of paths and other differently defined tree-power variants; paths do not cover spiders with \(m\ge3\). The standard zero-forcing/nullity inequality is pre-existing and not a new assertion.

## Limitations

The theorem requires at least three arms, at least two different arm lengths, and \(\ell_i\ge k+1\) for every arm. It does not give a formula when shorter arms occur or for general branched trees with two or more branch vertices. The construction does not classify all minimum zero-forcing sets or all minimum-rank matrices. The novelty comparison is based on accessible cited sources and targeted literature comparisons; independent expert validation and exhaustive historical priority review have not been performed.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (first posted 2026-10-02), Proposition 9, Conjecture 10. https://arxiv.org/abs/2610.03892
2. C. W. Chang, H.-G. Lin, *Minimum Rank of Powers of Cycles and Trees* (2013), Theorem 4.1 (graph squares of trees). https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
3. L. DeAlba and collaborators, *Minimum Rank of Powers of Trees* (2012), especially powers of paths. https://doi.org/10.13001/1081-3810.1511
4. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs* (2008), standard \(M\le Z\) inequality.
