# Rank spectra of square-zero elements in three-block parabolic radicals

## Finding

Let \(a,b,c\) be arbitrary positive integers, and let \(q\) be any prime power. Put \(N=a+b+c\). In the nilradical of the standard three-block parabolic subalgebra of \(M_N(\mathbb F_q)\), consider
\[
X=\begin{pmatrix}0&A&C\\0&0&B\\0&0&0\end{pmatrix},\qquad
A\in M_{a\times b}(\mathbb F_q),\quad B\in M_{b\times c}(\mathbb F_q),\quad C\in M_{a\times c}(\mathbb F_q).
\]

Write \(\mathfrak n_{a,b,c}\) for this nilradical.

For integers \(m,n\geq0\) and \(r\in\mathbb Z\), let \(R_q(m,n,r)\) be the number of rank-\(r\) \(m\times n\) matrices. Explicitly,
\[
R_q(m,n,r)=\frac{\prod_{v=0}^{r-1}(q^m-q^v)(q^n-q^v)}{\prod_{v=0}^{r-1}(q^r-q^v)}
\]
when \(0\le r\le\min(m,n)\), and zero otherwise (empty products equal one).

**Theorem.** The full rank enumerator of square-zero elements in this nilradical is
\[
\boxed{\begin{aligned}
\mathcal P_{a,b,c}^{(q)}(T)
&=\sum_{\substack{X\in\mathfrak n_{a,b,c}\\ X^2=0}}T^{\operatorname{rank}X}\\
&=\sum_{i=0}^{\min(a,b)}\sum_{j=0}^{\min(b-i,c)}
\sum_{h=0}^{\min(a-i,c-j)}R_q(a,b,i)R_q(b-i,c,j)\\
&\quad\times q^{ac-(a-i)(c-j)}R_q(a-i,c-j,h)T^{i+j+h}.
\end{aligned}}
\]
Every exponent in the formula is nonnegative, and every coefficient is a nonnegative integer. The attainable ranks are **exactly**
\[
\boxed{0,1,\ldots,M},\qquad
M=\min\left\{\left\lfloor\frac{a+b+c}{2}\right\rfloor,a+b,a+c,b+c\right\}.
\]
The total number of square-zero elements has the independent one-sum expression
\[
\boxed{\mathcal P_{a,b,c}^{(q)}(1)=q^{ac}
\sum_{i=0}^{\min(a,b)}R_q(a,b,i)q^{c(b-i)}}.
\]
For example, \(\mathcal P_{2,2,2}^{(2)}(T)=1+81T+630T^2+216T^3\) and \(\mathcal P_{2,2,2}^{(3)}(T)=1+608T+19344T^2+13824T^3\).

## Assumptions and scope

The block sizes \(a,b,c\) are positive, and \(q\) ranges over all prime powers, including powers of two and nonprime fields. Rank means ordinary matrix rank as an endomorphism of \(\mathbb F_q^N\). Matrices are counted individually rather than up to conjugacy. The theorem concerns the radical with all three off-diagonal rectangular blocks present; it does not assert formulas for four or more diagonal blocks.

## Proof

**1. Square-zero equation and the two adjacent blocks.** The Gaussian formula for \(R_q(m,n,r)\) follows by choosing the \(r\)-dimensional image subspace, then a surjection onto it; the number of surjections is \(\prod_{v=0}^{r-1}(q^n-q^v)\). Direct multiplication gives
\[
X^2=\begin{pmatrix}0&0&AB\\0&0&0\\0&0&0\end{pmatrix}.
\]
Thus \(X^2=0\) precisely when \(AB=0\). Fix \(i=\operatorname{rank}A\). There are \(R_q(a,b,i)\) choices of \(A\). The condition \(AB=0\) says \(\operatorname{im}B\subseteq\ker A\), a vector space of dimension \(b-i\). For \(j=\operatorname{rank}B\), the number of choices of \(B\) is \(R_q(b-i,c,j)\).

**2. The remaining rank of the long block.** Fix such \(A,B\), let \(I=\operatorname{im}A\subseteq\mathbb F_q^a\), \(K=\ker B\subseteq\mathbb F_q^c\), and let \(\pi:\mathbb F_q^a\twoheadrightarrow\mathbb F_q^a/I\) be the quotient. The image of \(X\), modulo \(I\oplus0\oplus0\), is the image of the map
\[
\mathbb F_q^c\longrightarrow (\mathbb F_q^a/I)\oplus\mathbb F_q^b,\qquad w\longmapsto(\pi Cw,Bw).
\]
Projection to \(\operatorname{im}B\) has rank \(j\). On its kernel \(K\), the remaining rank is \(h=\operatorname{rank}(\pi C|_K)\). Therefore
\[
\operatorname{rank}X=i+j+h,
\qquad0\le h\le\min(a-i,c-j).
\]
As \(C\) varies over all \(a\times c\) matrices, the restriction-and-quotient map
\[
\operatorname{Hom}(\mathbb F_q^c,\mathbb F_q^a)
\longrightarrow\operatorname{Hom}(K,\mathbb F_q^a/I),\qquad
C\longmapsto\pi C|_K
\]
is surjective: any map on \(K\) lifts along \(\pi\) and extends to a complement of \(K\). The domain has dimension \(ac\) and the target has dimension \((a-i)(c-j)\), so each fiber has \(q^{ac-(a-i)(c-j)}\) elements. Exactly \(R_q(a-i,c-j,h)\) target maps have rank \(h\). Multiplying the independent counts proves the enumerator, including its boundary cases when either quotient dimension is zero.

**3. Ungraded specialization.** For each rank-\(i\) matrix \(A\), the number of permissible \(B\) with \(AB=0\) is simply \(q^{c(b-i)}\); every \(C\) is allowed, giving \(q^{ac}\). This proves the one-sum specialization without using the triple sum.

**4. Sharp support.** Since \(X^2=0\), its image is contained in its kernel, giving \(\operatorname{rank}X\le\lfloor N/2\rfloor\). The zero first block-column and zero last block-row give respective bounds \(\operatorname{rank}X\le b+c\) and \(\operatorname{rank}X\le a+b\). The rank decomposition in Step 2 additionally yields
\[
\operatorname{rank}X=i+j+h\le i+j+\min(a-i,c-j)\le a+c.
\]
Thus every rank is at most \(M\).

For the opposite direction, form the complete tripartite graph on parts of sizes \(a,b,c\). Its maximum matching size is \(\min(\lfloor N/2\rfloor,N-\max(a,b,c))=M\). Indeed, no matching exceeds either bound; if the largest part has at least as many vertices as the other two combined, pair every other vertex into it, while otherwise pairing vertices from two currently largest parts repeatedly leaves at most one unmatched vertex. Fix a matching of size \(M\), and for each matched pair put a single \(1\) in the corresponding off-diagonal block, pointing from the later part to the earlier part. The resulting matrix has \(M\) nonzero entries in different rows and columns, so rank \(M\); the matched source and target coordinates are disjoint, so its square vanishes. Any subset of \(r\) matching edges yields square zero of rank \(r\), for every \(0\le r\le M\). This completes the proof.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. Run `python verify.py`. It constructs all permitted block entries and computes both \(AB\) and ordinary matrix rank over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). Forty-one parameter triples with at most 40,000 candidate matrices each were exhaustively compared against the formula; all passed. Separate checks of the one-sum total and sharp rank support also passed. The verifier prints `VERIFY_OK_PARABOLIC_SQUARE_ZERO`. These finite experiments corroborate, but do not establish, the universal statement; Steps 1–4 are the general proof.

## Relationship to prior work

Kirillov's rank-refined recurrence, quoted and used by Ekhad–Zeilberger [1], concerns all upper triangular square-zero matrices and does not condition on an ordered three-block parabolic zero pattern. The variety of complexes and its differential-rank strata are studied geometrically in [2,3]; the present count adds an unrestricted long block \(C\) and refines by the **rank of the entire square-zero endomorphism**, which is not the same invariant as the two adjacent differential ranks. Boos [4] classifies parabolic orbits of square-zero matrices over the complex numbers through link patterns and provides orbit dimensions, but not the \(q\)-dependent count of individual rank strata over finite fields. Nien's [5] studies irreducible character degrees of the corresponding three-part unipotent radical, rather than the present square-zero rank fibers. These are distinct counting questions; no priority claim is made for classical finite-field matrix-rank counts, matching bounds, or complex varieties individually.

## Limitations

The enumeration is for three blocks, individual matrices, and ordinary rank. It does not give conjugacy-orbit counts, the scheme-theoretic singularities of the square-zero locus, or analogous formulas for four or more blocks. The closest literature comparisons do not exclude an equivalent historical formula expressed through a different parametrization; this remains a bibliographic risk. A separate independent mathematical audit has not been performed.

## References

[1] S. B. Ekhad and D. Zeilberger, *An Explicit Formula for the Number of Solutions of \(X^2=0\) in Triangular Matrices over a Finite Field*, arXiv:math/9512224v1 (publicly posted 1995-12-19), https://arxiv.org/html/math/9512224v1.

[2] Darmajid and B. T. Jensen, *Varieties of complexes of fixed rank*, arXiv:1312.2058 (2013), https://arxiv.org/html/1312.2058v2.

[3] M. Kapranov and S. Pimenov, *Derived varieties of complexes and Kostant’s theorem for \(\mathfrak{gl}(m|n)\)*, arXiv:1504.00339 (2015), https://arxiv.org/html/1504.00339v2.

[4] M. Boos, *Conjugation on varieties of nilpotent matrices*, arXiv:1205.5197 (2012), https://arxiv.org/pdf/1205.5197.

[5] C. Nien, *Characters of unipotent radicals of standard parabolic subgroups with 3 parts*, J. Algebraic Combin. 55 (2022), 325–333, DOI:10.1007/s10801-021-01052-8 (first public journal version 2021).
