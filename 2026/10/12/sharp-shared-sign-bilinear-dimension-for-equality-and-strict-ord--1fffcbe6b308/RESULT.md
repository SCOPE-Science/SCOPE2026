# Sharp shared sign-bilinear dimension for equality and strict order

## Finding
Let \(D_n=\{1,\ldots,n\}\) with its equality relation and the strict order \(<\). A **shared sign-bilinear representation in dimension \(d\)** consists of one vector \(h_i\in\mathbb R^d\) for each entity, and separate real matrices \(B_{\mathrm{eq}},B_{\mathrm{lt}}\in\mathbb R^{d\times d}\), with all the scores nonzero and
\[
\begin{aligned}
h_i^{\mathsf T} B_{\mathrm{eq}}h_j>0&\quad\Longleftrightarrow\quad i=j,\\
h_i^{\mathsf T} B_{\mathrm{lt}}h_j>0&\quad\Longleftrightarrow\quad i<j.
\end{aligned}
\]
Consequently, all false atomic statements have **strictly negative** scores. Let \(d_{\pm}(n)\) be the least dimension allowing such a representation, with \(d\ge1\).

**Theorem.** For every integer \(n\ge1\),
\[
d_{\pm}(n)=\begin{cases}
1,&n=1,\\
2,&n=2,\\
3,&n\ge3.
\end{cases}
\]
The threshold at three entities is a genuine shared-geometry obstruction: on \(D_3\), equality alone and strict order alone each admit a two-dimensional sign-bilinear representation, but the two relations cannot use the same two-dimensional entity vectors.

## Assumptions and scope
The domain is a nonempty finite linearly ordered set, labeled in its order as \(D_n\). The matrices need not be symmetric, positive semidefinite, normalized, learned, or equal to one another. The **same** entity vector is used in the first and second argument positions and in both relation readouts. There is **one fixed zero decision threshold**, with strict signs: ties are forbidden. The result concerns exact **atomic truth values after thresholding**, not exact real scores or a compositional calculus for quantifiers.

## Proof
**Construction for \(n\ge3\).** Put
\[
h_i=(1,i,i^2)^{\mathsf T},\qquad
B_{\mathrm{eq}}=\begin{pmatrix}1&0&-2\\0&4&0\\-2&0&0\end{pmatrix},\qquad
B_{\mathrm{lt}}=\begin{pmatrix}-1&2&0\\-2&0&0\\0&0&0\end{pmatrix}.
\]
Direct multiplication yields the exact integer identities
\[
h_i^{\mathsf T}B_{\mathrm{eq}}h_j=1-2(i-j)^2,\qquad
h_i^{\mathsf T}B_{\mathrm{lt}}h_j=2(j-i)-1.
\]
When \(i=j\), the equality score is \(1\), whereas for distinct integers it is at most \(-1\). Likewise, the order score is at least \(1\) precisely for \(i<j\), and at most \(-1\) otherwise. Hence \(d_{\pm}(n)\le3\) with strict integral margins for every finite \(n\ge3\).

**Small domains.** For \(n=1\), take \(h_1=(1)\), \(B_{\mathrm{eq}}=(1)\), \(B_{\mathrm{lt}}=(-1)\). For \(n=2\), take \(h_1=(1,0)^{\mathsf T}\), \(h_2=(0,1)^{\mathsf T}\) and
\[
B_{\mathrm{eq}}=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
B_{\mathrm{lt}}=\begin{pmatrix}-1&1\\-1&-1\end{pmatrix}.
\]
Both have precisely the required strict sign patterns. Dimension zero cannot realize the positive equality score on a nonempty domain, so \(d_{\pm}(1)=1\). In dimension one, a bilinear score has the form \(a h_i h_j\), symmetric in \(i,j\). But on \(D_2\) the order scores for \((1,2)\) and \((2,1)\) must have opposite signs, so \(d_{\pm}(2)=2\).

**Three-vector sign lemma.** Suppose nonzero vectors \(v_1,v_2,v_3\) lie in a real vector space of dimension at most two and a bilinear form \(E\) satisfies \(E(v_i,v_i)>0\) and \(E(v_i,v_j)<0\) whenever \(i\ne j\). Then there are strictly positive real scalars \(c_1,c_2,c_3\) such that
\[
c_1v_1+c_2v_2+c_3v_3=0.
\]
Indeed, linear dependence supplies a nonzero coefficient triple with zero sum of vectors. No vector is zero because its diagonal \(E\)-score is positive. All coefficients in this dependence must be nonzero: otherwise two distinct vectors are proportional, say \(v_j=\lambda v_i\). If \(\lambda>0\), the off-diagonal value \(E(v_i,v_j)\) is positive. If \(\lambda<0\), choosing the remaining index \(k\) makes \(E(v_i,v_k)\) and \(E(v_j,v_k)\) have opposite signs. Both cases contradict the prescribed signs. Finally, mixed-sign coefficients would express one vector as a strictly positive linear combination of the other two. Applying \(E(v_i,-)\) to that identity would equate a strictly positive diagonal score to a strictly negative sum. Thus all coefficients have the same sign, and multiplying the dependence by \(-1\) if needed makes all of them positive.

**Lower bound for \(n\ge3\).** Restrict a proposed representation in dimension at most two to its first three entities. Apply the lemma to the equality form \(E(v,w)=v^{\mathsf T}B_{\mathrm{eq}}w\), obtaining \(c_1v_1+c_2v_2+c_3v_3=0\) with every \(c_i>0\). The first column of the strict-order relation is entirely false, including its diagonal; therefore \(v_i^{\mathsf T}B_{\mathrm{lt}}v_1<0\) for every \(i\in\{1,2,3\}\). Applying the linear functional \(v\mapsto v^{\mathsf T}B_{\mathrm{lt}}v_1\) to the positive dependence yields
\[
0=\sum_{i=1}^3c_i\,v_i^{\mathsf T}B_{\mathrm{lt}}v_1<0,
\]
a contradiction. Thus \(d_{\pm}(n)\ge3\), matching the construction.

**Why the third coordinate is jointly necessary on \(D_3\).** Equality alone is sign-realized in dimension two by the vectors \((1,0)^{\mathsf T}\), \((-1,2)^{\mathsf T}\), \((-1,-2)^{\mathsf T}\) with bilinear matrix \(I_2\): all diagonal products are positive, and the three distinct off-diagonal products are negative. Strict order alone uses \((1,i)^{\mathsf T}\) and the matrix \(\begin{psmallmatrix}-1&2\\-2&0\end{psmallmatrix}\), yielding \(2(j-i)-1\). Hence neither relation separately forces a third coordinate at three entities, although sharing a geometry does.

## Verification
The standalone Python 3 program `verify.py` computes scores entirely with integer arithmetic. Running `python3 verify.py 100` produces `VERIFY_OK max_domain=100 domain_sizes=100 pairs=338350 standalone_3point_relation_checks=18`. These are the full positive/negative score comparisons for all ordered pairs over domain sizes one through one hundred, together with separate two-dimensional witnesses on the three-element domain. The strict lower bound is proved by the three-vector sign lemma, **not** established through a finite computational search.

## Relationship to prior work
Quigley, *Exact semantic readout from compressed vector representations* (arXiv:2609.18047v1, Sections 6–8), studies **exact** bilinear equality of truth matrices with compressed representations. Corollaries 6.1–6.2 force dimension \(n\) for exact-score identity and strict-order readouts; Section 7 distinguishes the weaker problem of recovering relational **support** and leaves that relaxation unresolved. Here only the signs matter; the scores are neither \(0\) nor \(1\) except incidentally. This change in semantics permits constant dimension, and the shared-geometry lower bound identifies the exact minimum.

Sherstov, *Lower Bounds in Communication Complexity and Learning Theory via Analytic Methods* (2009, Section 2.4), records low sign-rank representatives for equality and greater-than **individually**, with unconstrained row and column factorization. Those individual bounds do not determine the least dimension for the two predicates using one common entity embedding in both argument slots. Wang, Gemulla, and Li (2018, Theorems 5–6) establish universality and general lower bounds for multi-relational bilinear models, but their results do not give this exact special-pair minimum. Badreddine, van Krieken, and Serafini (arXiv:2506.22271v1, Theorems 3.3 and 4.1) treat general sign-reconstruction bottlenecks and sufficient dimensions, rather than a sharp simultaneous bound for equality and linear order.

## Limitations
Thresholded truth at atomic relation instances is weaker than an exact truth-vector lift. Nothing here establishes the preservation of compositional Boolean readout, counting, generalized quantifiers, or modal accumulation on a compressed carrier; these require separate analysis. The construction relies on known rank labels of the finite linear order, unrestricted real bilinear matrices, and unnormalized coordinates. The existence of a representation does not demonstrate that a learning procedure discovers it. Related results in sign-pattern or common-factor literature could contain an equivalent special case; the novelty comparison is not a proof of exhaustive absence from all literature.

## References
1. Daniel Quigley, *Exact semantic readout from compressed vector representations*, arXiv:2609.18047v1, publicly submitted 2026-09-16. https://arxiv.org/pdf/2609.18047v1
2. Alexander A. Sherstov, *Lower Bounds in Communication Complexity and Learning Theory via Analytic Methods*, doctoral dissertation, University of Texas at Austin, 2009, Section 2.4. https://web.cs.ucla.edu/~sherstov/pdf/Sherstov_Dissertation.pdf
3. Yanjie Wang, Rainer Gemulla, and Hui Li, *On Multi-Relational Link Prediction with Bilinear Models*, AAAI, 2018. https://ojs.aaai.org/index.php/AAAI/article/download/11738/11597
4. Samy Badreddine, Emile van Krieken, and Luciano Serafini, *Breaking Rank Bottlenecks in Knowledge Graph Completion*, arXiv:2506.22271v1, 2025. https://arxiv.org/html/2506.22271v1
