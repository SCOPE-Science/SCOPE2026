# Rank-stratified idempotent laws for random evolution algebras in characteristic two

## Finding
For integers \(n\ge1\), \(e\ge1\), \(q=2^e\) and \(0\le s\le n\), choose an \(n\)-by-\(n\) structure matrix \(A\) uniformly among matrices of rank \(s\) over \(\mathbb F_q\). Let \(E_A\) denote the evolution algebra on the specified natural basis, with multiplication \(e_i e_j=0\) for distinct indices and \(e_i^2=\sum_j A_{ij}e_j\). Write \(K(A)\) for the number of *nonzero elements* \(x\in E_A\) satisfying \(x^2=x\); the word idempotent refers to elements, not to the condition \(E_A^2=E_A\).

Define the Gaussian binomial coefficient for \(0\le b\le a\) by
\[
{a\brack b}_q=\prod_{j=0}^{b-1}\frac{q^a-q^j}{q^b-q^j},
\]
with \({a\brack b}_q=0\) for out-of-range indices, and \(g_r=|\operatorname{GL}_r(\mathbb F_2)|=\prod_{j=0}^{r-1}(2^r-2^j)\), including \(g_0=1\). For \(0\le r\le s\) set
\[
\alpha_{n,s,r}(q)=q^{r(n-s)}\frac{{n-r\brack s-r}_q}{{n\brack s}_q}.
\]
Then \(K(A)=2^D-1\) for a uniquely determined integer \(0\le D\le s\), with the exact conditional distribution
\[
\boxed{\Pr(D=d\mid \operatorname{rank}A=s)=\sum_{r=d}^{s}(-1)^{r-d}2^{\binom{r-d}{2}}{r\brack d}_2\frac{\alpha_{n,s,r}(q)}{g_r}\quad(0\le d\le s).}
\]
These probabilities apply to uniformly sampled **labelled structure matrices**, not isomorphism classes. Their decisive moment identity is
\[
\mathbb E\!\left[\prod_{j=0}^{r-1}(2^D-2^j)\,\middle|\,\operatorname{rank}A=s\right]=\alpha_{n,s,r}(q).
\]

For all fixed \(n,s\), as \(q=2^e\to\infty\), this distribution tends to the fixed-space-dimension distribution of a uniformly sampled matrix in \(\operatorname{GL}_s(\mathbb F_2)\). The convergence follows term by term from \(\alpha_{n,s,r}(q)\to1\). At finite \(q\) the rank-deficient laws depend on field size: for rank one, \(\Pr(K=1)=q^{n-1}(q-1)/(q^n-1)\), whereas for full rank the law is independent of \(q\).

## Assumptions and scope
All fields have characteristic exactly two. The structure matrix is square, of exact rank \(s\), and uniform within its finite rank stratum; its natural basis is fixed and labelled. There is no condition of nondegeneracy or perfection when \(s<n\). There is exactly one idempotent when \(s=0\) if zero is included; the claimed random variable counts *nonzero* idempotents and thus equals zero in that case. The zero element always satisfies \(x^2=x\), and is omitted from \(K\). The field-size limit is taken with fixed \(n,s\) and extension degree \(e\to\infty\).

## Proof
**Step 1: fixed-space structure.** In coordinates, the idempotent equation is \(x=A^{\mathsf T}x^{[2]}\), with coordinatewise Frobenius squaring. The map \(F_A(x)=A^{\mathsf T}x^{[2]}\) is \(\mathbb F_2\)-linear. Hence its fixed space \(V_A\) is an \(\mathbb F_2\)-vector space, of dimension \(D\), and \(K=2^D-1\). We claim that every \(\mathbb F_2\)-independent family of fixed points is \(\mathbb F_q\)-independent. Otherwise choose a smallest \(\mathbb F_q\)-dependent subfamily and express one member as a linear combination of the remaining, which are \(\mathbb F_q\)-independent. Apply \(F_A\) to that relation. Since it fixes every member and is semilinear with Frobenius on coefficients, all the coefficients equal their squares, so each lies in the fixed field \(\mathbb F_2\). This contradicts \(\mathbb F_2\)-independence. All fixed points also lie in \(\operatorname{im}(A^{\mathsf T})\), whose \(\mathbb F_q\)-dimension is \(s\). Thus \(0\le D\le s\).

**Step 2: frame moments.** Let \(r\le s\) and fix an ordered \(\mathbb F_q\)-independent \(r\)-tuple of vectors \(x_1,\ldots,x_r\). Their coordinatewise squares \(w_i=x_i^{[2]}\) form an \(r\)-frame as well. A rank-\(s\) matrix \(A^{\mathsf T}\) has uniformly random kernel of dimension \(n-s\). For a prescribed \(r\)-plane \(W=\operatorname{span}_{\mathbb F_q}\{w_i\}\), the number of \((n-s)\)-planes missing \(W\) is \(q^{r(n-s)}{n-r\brack n-s}_q\): first choose an \((n-s)\)-plane in the quotient by \(W\), then choose one of \(q^{r(n-s)}\) graph lifts. Dividing by the total \({n\brack n-s}_q\) gives exactly \(\alpha_{n,s,r}(q)\). Conditional on injectivity on \(W\), the ordered image frame is uniform among the \(\prod_{j=0}^{r-1}(q^n-q^j)\) ordered \(r\)-frames of \(\mathbb F_q^n\), by left multiplication invariance of the uniform rank stratum. Hence the chance that \(F_A(x_i)=x_i\) for all \(i\) is
\[
\alpha_{n,s,r}(q)\bigg/\prod_{j=0}^{r-1}(q^n-q^j).
\]
All \(\mathbb F_2\)-independent tuples of fixed points are \(\mathbb F_q\)-independent by Step 1, so summing over the above number of ordered \(\mathbb F_q\)-frames yields the stated moment \(\alpha_{n,s,r}(q)\). (The case \(r=0\) is the constant moment one.)

**Step 3: inversion.** The number of ordered linearly independent \(r\)-frames in an \(\mathbb F_2\)-space of dimension \(D\) is \(\prod_{j=0}^{r-1}(2^D-2^j)=g_r{D\brack r}_2\). Therefore
\[
\mathbb E\!\left[{D\brack r}_2\right]=\frac{\alpha_{n,s,r}(q)}{g_r}=\sum_{d=r}^{s}{d\brack r}_2\Pr(D=d).
\]
Use triangular Gaussian-binomial inversion, whose coefficient is \((-1)^{r-d}2^{\binom{r-d}{2}}{r\brack d}_2\), to obtain the probability formula for each \(d\). This also proves the probabilities sum to one and are nonnegative, without relying on cancellation in their displayed formula.

**Step 4: boundaries, mean and limit.** For \(s=0\), only the zero solution is possible. For \(s=1\), the first moment is the success probability \(\alpha_{n,1,1}(q)=q^{n-1}(q-1)/(q^n-1)\). In general \(\mathbb E[K\mid s]=\alpha_{n,s,1}(q)=q^{n-s}(q^s-1)/(q^n-1)\) for \(s\ge1\), with value zero at \(s=0\). The largest possible count has probability \(\Pr(K=2^s-1)=q^{s(n-s)}/({n\brack s}_q g_s)\). If \(s=n\), each \(\alpha_{n,n,r}=1\), recovering the known field-size-independent perfect-matrix law. For fixed \(n,s,r\), use \({n-r\brack s-r}_q/{n\brack s}_q\sim q^{-r(n-s)}\) as \(q\to\infty\); thus \(\alpha_{n,s,r}(q)\to1\). These are precisely the normalized ordered-fixed-frame moments for uniform elements of \(\operatorname{GL}_s(\mathbb F_2)\), and Gaussian inversion identifies the claimed limiting distribution.

## Verification
The independent enumerator `verify.py` constructs every matrix of each rank for \((q,n)=(2,2),(2,3),(2,4),(4,2),(4,3),(8,2)\), directly enumerates idempotents over the chosen finite field, and compares the complete conditional distribution with the rational formula above; it also verifies total matrix counts in each rank stratum. All six configurations returned `RANK_VERIFICATION_OK`. For example, among \(75\) rank-one matrices over \(\mathbb F_4\) in dimension two, exactly \(60\) have one nonzero idempotent and \(15\) have none. Among \(9\) rank-one binary matrices in dimension two, exactly \(6\) have one and \(3\) have none. These experiments are checks, not the proof of the all-parameter theorem. Reproduce with `python verify.py` using Python 3 and only its standard library.

## Relationship to prior work
Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, October 15, 2026) review evolution-algebra idempotent equations in Section 1.1, the rank/perfection dichotomy, and random evolution algebras in Question 22. Their Remark 23 computes mean nonzero idempotent count one when the structure matrix is uniform *invertible*. A separate existing result classifies the full distribution when \(s=n\) in characteristic two. That full-rank case is a boundary consequence here, **not claimed as original**. The contribution isolated here is the exact distribution for **every prescribed singular rank** \(0\le s<n\), its field-size dependence, and the uniform rank-\(s\) limiting law. Wei and Zou (arXiv:2310.12368) study isomorphism classes of *idempotent evolution algebras* in the standard terminology \(E^2=E\); this is different from counting individual idempotent elements in a random nonperfect algebra. Fulman and Goldstein (arXiv:1211.0504) study ranks of random finite-field matrices, not the Frobenius-semilinear fixed-point statistic conditioned on rank. These mathematical distinctions are statement-level, not merely differences in titles.

## Limitations
The formula is specific to characteristic two and uniform labelled matrices conditional on exact rank. It is not a classification up to algebra isomorphism and does not extend here to odd characteristic, other distributions on structure matrices, sparse random models, or to the number of solutions after scalar extension. The perfect-matrix distribution is previously known. An equivalent all-rank formula derived in unindexed literature on Frobenius-semilinear random maps remains a residual historical-priority risk; no absolute-priority claim is made. The result is supported by symbolic proof and finite checks but has no independent external mathematical audit.

## References
1. I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), https://arxiv.org/html/2610.22248v1 .
2. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023), https://arxiv.org/abs/2310.12368 .
3. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504 (2012), https://arxiv.org/abs/1211.0504 .
