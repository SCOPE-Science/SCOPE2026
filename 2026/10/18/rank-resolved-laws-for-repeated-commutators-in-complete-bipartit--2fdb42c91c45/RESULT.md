# Rank-resolved laws for repeated commutators in complete-bipartite graphical groups

## Finding

The distribution of every finite product of group commutators can be evaluated exactly, target by target, for the graphical group of a complete bipartite graph. Both the characteristic and the extension degree of the coefficient field are arbitrary.

For positive integers \(a,b,k\) and a prime power \(q\), define the group
\[
G=\mathbb F_q^a\times\mathbb F_q^b\times M_{a\times b}(\mathbb F_q),\qquad
(u,v,Z)(u',v',Z')=(u+u',v+v',Z+Z'+uv'^{\mathsf T}).
\]
The derived subgroup and the center both consist of the elements \((0,0,C)\), one for each \(a\)-by-\(b\) matrix \(C\). Write \(F_k(C)\) for the number of ordered \(2k\)-tuples \((x_1,y_1,\ldots,x_k,y_k)\in G^{2k}\) satisfying
\[
[x_1,y_1]\cdots[x_k,y_k]=(0,0,C),
\qquad [x,y]=x^{-1}y^{-1}xy.
\]
For an integer \(n\ge0\), let \(\mathcal G_q(n,j)\) be the number of \(j\)-dimensional subspaces of \(\mathbb F_q^n\):
\[
\mathcal G_q(n,j)=\prod_{i=0}^{j-1}\frac{q^{n-i}-1}{q^{j-i}-1}
\quad(0\le j\le n),\qquad \mathcal G_q(n,j)=0\quad\text{otherwise}.
\]
If \(r=\operatorname{rank}C\), define for \(0\le s\le\min(a,b)\)
\[
K_s(r)=\sum_{j=0}^{s}(-1)^{s-j}q^{\binom{s-j}{2}+aj}
 \mathcal G_q(b-r,j)\mathcal G_q(b-j,s-j).
\]
**Exact fiber theorem.** For every such parameter and every target matrix,
\[
\boxed{F_k(C)=q^{2kab-ab}\sum_{s=0}^{\min(a,b)}q^{2k(a+b-s)}K_s(r).}
\]
The formula is integral and nonnegative as it counts an actual finite set, despite possible cancellation between terms. A target outside the center has no representation as a product of commutators.

**Sharp length theorem.** The least number of commutators needed to express \((0,0,C)\), taking the empty product for the identity, is
\[
\boxed{\ell(C)=\left\lceil\frac{\operatorname{rank}C}{2}\right\rceil.}
\]
Consequently \(\operatorname{cw}(G)=\lceil\min(a,b)/2\rceil\). The number of central matrices of rank \(r\) is
\[
R_r=\mathcal G_q(a,r)\mathcal G_q(b,r)
\prod_{i=0}^{r-1}(q^r-q^i).
\]
Therefore the number of elements of minimal length \(h\ge1\) is \(R_{2h-1}+R_{2h}\), with out-of-range ranks contributing zero, and the identity is the sole length-zero element.

For one commutator, remove the free central input factor by writing \(F_1(C)=q^{2ab}f(C)\) and abbreviate \(A=q^a\), \(B=q^b\). Then
\[
f(C)=\begin{cases}
 A^2+B^2+(q+1)AB-(q+1)(A+B)+q,&r=0,\\
 (q^2-1)(A+B-q),&r=1,\\
 (q^2-1)(q^2-q),&r=2,\\
 0,&r>2.
\end{cases}
\]
Only ranks compatible with the matrix dimensions occur. The formulas for \(k\ge2\) are generally not obtained by replacing \(r\) in these one-step expressions: they give the full higher-convolution distribution.

## Assumptions and scope

The field is any finite field \(\mathbb F_q\), including characteristic two; both sides of the bipartition are nonempty. The group model realizes the graphical-group presentation associated with \(K_{a,b}\): generators on the same bipartition commute, whereas the cross-commutators are independent central coordinates. The group has \(q^{a+b+ab}\) elements. All counts include every allowed choice of central coordinates in all \(2k\) input group elements. The theorem concerns prescribed products of group commutators, not conjugacy-class sizes. The target is a specific matrix rather than merely a similarity class.

## Proof

**1. Commutator reduction.** Direct multiplication and inversion in the displayed group law give
\[
[(u,v,Z),(u',v',Z')]=(0,0,uv'^{\mathsf T}-u'v^{\mathsf T}).
\]
Thus the central coordinates \(Z,Z'\) of each pair are unrestricted, contributing the factor \(q^{2kab}\). Every matrix unit is a commutator (take one of \(u',v\) zero), so the derived group equals the full central matrix space. No noncentral element commutes with every vector of the opposite bipartition, hence the center is precisely that matrix space.

**2. Fourier transform of the one-pair map.** Put \(U=\mathbb F_q^a\) and \(V=\mathbb F_q^b\). Let \(f(C)\) count \((u,v,u',v')\in(U\times V)^2\) with \(uv'^{\mathsf T}-u'v^{\mathsf T}=C\). Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). For a matrix \(D\in M_{b\times a}(\mathbb F_q)\), use the pairing \(\psi(\operatorname{tr}(DC))\). Summing first over \(v'\) and \(u'\) imposes \(Du=0\) and \(D^{\mathsf T}v=0\). When \(s=\operatorname{rank}D\), character orthogonality gives
\[
\widehat f(D)=q^{a+b}\,q^{a-s}\,q^{b-s}=q^{2(a+b-s)}.
\]
Since distinct commutators add in the central matrix group, their \(k\)-fold product distribution is the additive convolution \(f^{*k}\), whose Fourier transform is \(\widehat f(D)^k\). Fourier inversion therefore yields
\[
 f^{*k}(C)=q^{-ab}\sum_{D\in M_{b\times a}(\mathbb F_q)}
 q^{2k(a+b-\operatorname{rank}D)}\psi(-\operatorname{tr}(DC)).
\]

**3. Rank-stratified character sums.** Let \(\mathcal S_s(C)\) be the sum of \(\psi(\operatorname{tr}(DC))\) over matrices \(D\) of rank exactly \(s\). The value depends only on \(r=\operatorname{rank}C\), by the left-right general linear action. For a subspace \(S\le V\), sum over linear maps \(D:U\to V\) with \(\operatorname{im}D\subseteq S\). Character orthogonality gives
\[
H(S):=\sum_{\operatorname{im}D\subseteq S}\psi(\operatorname{tr}(DC))
=\begin{cases}q^{a\dim S},& S\subseteq\ker C,\\0,&\text{otherwise}.
\end{cases}
\]
The kernel here is for \(C:V\to U\), so its dimension is \(b-r\). Möbius inversion on the subspace lattice, whose interval Möbius function for codimension \(t\) is \((-1)^tq^{\binom t2}\), separates the condition \(\operatorname{im}D=S\) from \(\operatorname{im}D\subseteq S\). The number of \(j\)-spaces \(T\) inside \(\ker C\) is \(\mathcal G_q(b-r,j)\), and each lies in \(\mathcal G_q(b-j,s-j)\) spaces \(S\) of dimension \(s\). Consequently
\[
\mathcal S_s(C)=\sum_{j=0}^s(-1)^{s-j}q^{\binom{s-j}{2}+aj}
 \mathcal G_q(b-r,j)\mathcal G_q(b-j,s-j)=K_s(r).
\]
This is real and invariant under replacing \(C\) by \(-C\), so it may be substituted into the Fourier inversion with the negative sign. Multiplication by the free-center factor \(q^{2kab}\) proves the boxed \(F_k\) formula.

**4. Commutator length.** Every single commutator has matrix rank at most two, because it is a difference of two rank-one matrices. A sum of \(h\) such matrices has rank at most \(2h\), establishing the lower bound \(\ell(C)\ge\lceil r/2\rceil\). Conversely every rank-\(r\) matrix has a rank-one decomposition \(C=\sum_{i=1}^r u_i v_i^{\mathsf T}\). Pair consecutive terms and absorb their signs into the vectors. Each resulting matrix of rank at most two has the required form \(uv'^{\mathsf T}-u'v^{\mathsf T}\), giving an expression using \(\lceil r/2\rceil\) commutators. Counting ranks by choosing column and row spaces and an isomorphism between them proves the expression for \(R_r\). Finally the explicit one-step table follows by character inversion at \(k=1\), or by direct rank-one-decomposition counting.

## Verification

The accompanying standalone Python checker enumerates every one-step four-vector input for nine dimension-field configurations and compares the fiber over *every* target matrix, including targets of rank above two, with the closed one-step formula. It separately verifies the counts for input support types. It computes repeated additive convolutions by direct integer-array addition and compares them with the full Gaussian-rank formula at \(k=1,2,3\), including \(k=4\) in one configuration. Fields include \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), where the extension-field arithmetic is implemented explicitly. The run ends with `ALL_EXACT_CHECKS_PASSED 9 one-step cases + 4 multi-step cases`.

For \(q=2\), \(a=b=3\), the central part of the *one*-commutator fiber has values \(274,42,6,0\) at ranks \(0,1,2,3\). The corresponding *two*-commutator fibers have values \(172096,68160,33600,20160\). All \(168\) rank-three matrices therefore first become representable by two commutators. These four rank-stratified target counts, weighted by the numbers of matrices of each rank, sum to \(2^{24}\), the number of ordered four-vector input quadruples for two commutators before the free central coordinates are restored.

The general theorem follows from the algebraic argument, not from finite exhaustive experiments.

## Relationship to prior work

Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, establishes the graphical-group framework and class-size polynomials, including a complete-bipartite example (Example 5.3). Those class-size enumerations are not pointwise fibers of the product of \(k\) commutator words. The matrix Fourier transform of rank strata is closely related to established bilinear-forms association schemes and rank-metric Krawtchouk transforms; the subspace Möbius computation here does not assert invention of that general technique. Studies of commutator-word distributions in other finite group families, such as Naik's, likewise motivate the question without specifying these \(K_{a,b}\) fibers. General character-theoretic formulas for products of commutators exist and are not claimed as new. The stated contribution is the explicit rank-Gaussian specialization for this infinite group family, its uniform all-\(k\) prescribed-value law and the sharp elementwise width classification.

## Limitations

The count is for complete bipartite graphical groups, not arbitrary graph groups or arbitrary class-two groups. The computational tests cover finitely many small parameters; the proof establishes the full prime-power and positive-integer scope. A previous rank-metric or older group-theoretic treatment could conceivably yield an equivalent all-fold expression: historical priority beyond the inspected material is not certified. No independent mathematical audit has been performed.

## References

1. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (first public 12 July 2021), *Bulletin of the London Mathematical Society* **54** (2022), 1923–1943, DOI 10.1112/blms.12665. Open text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12665
2. T. K. Naik, *On the probability distribution associated to commutator word map in finite groups* (2018/2019). Relevant commutator-word distribution literature: https://www.researchgate.net/publication/331711145_On_the_probability_distribution_associated_to_commutator_word_map_in_finite_groups
3. M. Akhavan-Malayeri and A. H. Rhemtulla, *Commutator length of abelian-by-nilpotent groups* (1998). Related class-two commutator-width context.
4. K. Kawamura, *q-Hypergeometric polynomials and group-invariant Fourier transformations over a finite field* (2020), related matrix-rank Fourier machinery. Scholarly description: https://arxiv.org/search/?query=Kawamura+group-invariant+Fourier+finite+field&searchtype=all
5. I. Sinha, *Commutators in Nilpotent Linear Groups of Class Two* (1966). Historical possible-priority source; full text was not available for inspection.
