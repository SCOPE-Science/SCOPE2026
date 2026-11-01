# Design-rigid vacancy fluctuations after two permuted regular layers

## Finding

**Theorem (exact variance and optimal geometry).** Fix integers \(r\ge3\) and \(d\ge3r-2\). Let \(P_1,P_2\) be deterministic \(d\times d\) doubly stochastic kernels with exactly \(r\) nonzero entries, each \(1/r\), in every row and column. Let \(\Pi_1,\Pi_2\) be independent uniform permutation matrices and put \(R_2=\Pi_1P_1\Pi_2P_2\). For any fixed starting vertex \(i\), let \(N_j=r^2(R_2)_{ij}\) be the number of two-step paths ending at \(j\), and \(Z=\#\{j:N_j=0\}\). Set
\[
 u=\frac{\binom{d-r}{r}}{\binom dr},\qquad
 f(t)=\frac{\binom{d-2r+t}{r}}{\binom dr},\qquad
 \lambda=\frac{r(r-1)}{d-1}.
\]
Let \(B_j\subseteq[d]\) be the size-\(r\) incoming-neighbor set in column \(j\) of \(P_2\), and write \(t_{jk}=|B_j\cap B_k|\). Then
\[
 \mathbb EZ=du,\qquad
 \operatorname{Var}(Z)=du(1-u)+\sum_{j\ne k}\bigl(f(t_{jk})-u^2\bigr).
\]
If \(\lambda\) is an integer, the **sharp conditional design bound** is
\[
 \operatorname{Var}(Z)\ge V_{d,r}
 :=du(1-u)+d(d-1)\bigl(f(\lambda)-u^2\bigr),
\]
with equality **if and only if** the zero-one incidence matrix \(rP_2\) is a symmetric \(2\)-\((d,r,\lambda)\) design (equivalently, every two distinct columns meet in exactly \(\lambda\) rows). Thus the displayed bound is attained whenever such a symmetric design exists; no existence is asserted otherwise.

At the natural critical two-layer scale \(d=r^2-r+1\), so \(\lambda=1\), put \(D=d-2r\). The full strict defect from the design bound is the nonnegative motif expansion
\[
 \operatorname{Var}(Z)-V_{d,r}
 =\sum_{k=2}^{r}\frac{\binom D{r-k}}{\binom dr}
     \sum_{j\ne l}\binom{t_{jl}}k.
\]
Its first term is a positive explicit multiple of the number of four-cycles in the bipartite incidence graph. Equality occurs exactly for a projective plane of order \(r-1\); when \(r-1\) is a prime power, projective planes exist and the bound is attained. Along these prime-power orders,
\[
 \lim_{r\to\infty}\frac{\min\operatorname{Var}(Z)}d
 =e^{-1}-\frac52 e^{-2}.
\]
The minimization is over all regular two-layer kernels of the stated size, with \(P_1\) arbitrary; the minimum expression is understood only when a projective plane exists.

## Assumptions and scope

A regular kernel permits directed edges and loops, but no repeated positive entries. We use \(\binom nk=0\) for nonnegative integer \(n<k\). Since \(d\ge3r-2\), every argument \(d-2r+t\) is nonnegative for \(0\le t\le r\). The random permutations act on entire vertex piles, not on individual paths. The main theorem concerns the actual number of empty destination vertices after exactly two independent shuffles and two regular layers; it does not replace the model by independent balls into boxes.

## Proof

**Step 1: exact reduction to a random subset.** The first shuffle selects a uniform row of \(P_1\), and that row carries one path to each of exactly \(r\) distinct vertices. The second independent shuffle maps those \(r\) occupied vertices to a uniform \(r\)-element subset \(S\) of \([d]\). The count ending at column \(j\) is exactly \(|S\cap B_j|\). Hence the event \(N_j=0\) is \(S\cap B_j=\varnothing\), with probability \(u\). Two such events hold jointly precisely when \(S\) avoids \(B_j\cup B_k\), which has cardinality \(2r-t_{jk}\). Its probability is \(f(t_{jk})\). Expanding the variance of a sum of indicators proves both exact formulas.

**Step 2: the forced average overlap.** Every row belongs to exactly \(r\) column supports, so counting ordered pairs of distinct columns meeting at a row gives
\[
 \sum_{j\ne k}t_{jk}=dr(r-1)=d(d-1)\lambda.
\]
The second forward difference of \(f\) is
\[
 f(t+2)-2f(t+1)+f(t)
 =\frac{\binom{d-2r+t}{r-2}}{\binom dr}>0
 \quad(0\le t\le r-2),
\]
where the strict inequality follows from \(d-2r\ge r-2\). For integer \(\lambda\), strict discrete convexity supplies a strict supporting line through \((\lambda,f(\lambda))\): \(f(t)\ge f(\lambda)+s(t-\lambda)\), equality exactly when \(t=\lambda\), for an \(s\) between the adjacent differences. Summing and using the forced overlap average proves the sharp variance bound and its equality condition.

**Step 3: identification of equality designs.** Let \(A=rP_2\), a square zero-one matrix with row and column sum \(r\). Uniform column intersections give
\[
 A^{\mathsf T}A=(r-\lambda)I+\lambda\mathbf1\mathbf1^{\mathsf T}.
\]
Here \(r+(d-1)\lambda=r^2\) and \(r>\lambda\). Therefore \(A\) has full rank; \(AA^{\mathsf T}\) has the same eigenvalues, and its eigenspace for \(r^2\) is spanned by \(\mathbf1\). It follows that \(AA^{\mathsf T}=(r-\lambda)I+\lambda\mathbf1\mathbf1^{\mathsf T}\). Thus each pair of distinct points belongs to exactly \(\lambda\) blocks, and the incidence structure is the claimed symmetric \(2\)-design. The converse is immediate. At \(d=r^2-r+1\), this is the defining incidence property of a projective plane of order \(r-1\).

**Step 4: exact defect in the critical plane parameters.** For \(\lambda=1\), apply Vandermonde's identity to each integer \(t\ge0\):
\[
 \binom{D+t}{r}=\sum_{k=0}^r\binom tk\binom D{r-k}.
\]
The constant and linear terms sum to exactly \(d(d-1)f(1)\) because the ordered average of \(t_{jl}\) equals one. The remaining terms give the displayed defect formula. All coefficients are nonnegative, and the \(k=2\) coefficient is strictly positive because \(D\ge r-2\). Consequently the defect is zero precisely when every \(t_{jl}\le1\); the average-one condition then forces every \(t_{jl}=1\). Moreover \(\sum_{j\ne l}\binom{t_{jl}}2\) equals twice the number of bipartite four-cycles.

**Step 5: limiting sharp constant.** Write \(d=r^2-r+1\), \(u_r=\binom{d-r}{r}/\binom dr\), \(v_r=\binom{d-2r+1}{r}/\binom dr\). Elementary logarithmic products give \(u_r\to e^{-1}\). Let \(H_k=\sum_{j=0}^{r-1}(d-j)^{-k}\). Their expansions are
\[
 H_1=r^{-1}+\tfrac32r^{-2}+O(r^{-3}),\quad
 H_2=r^{-3}+3r^{-4}+O(r^{-5}),\quad
 H_3=r^{-5}+O(r^{-6}).
\]
Expanding \(\log(v_r/u_r^2)\) through cubic powers of \((d-j)^{-1}\) (higher powers contribute \(O(r^{-3})\)) yields
\[
 \log(v_r/u_r^2)=H_1+(-r^2+2r-\tfrac12)H_2
 +(-2r^3+4r^2-2r+\tfrac13)H_3+O(r^{-3})
 =-\tfrac32r^{-2}+O(r^{-3}).
\]
Therefore \((d-1)(v_r-u_r^2)\to-\tfrac32e^{-2}\). Since \(V_{d,r}/d=u_r(1-u_r)+(d-1)(v_r-u_r^2)\), its limit is \(e^{-1}-\tfrac52e^{-2}\). For every prime-power order \(r-1\), projective-plane incidence attains \(V_{d,r}\), completing the assertion.

## Verification

A standalone Python 3 standard-library checker, `verify.py`, computes the vacancy variance by exact rational arithmetic in two independent ways: enumerating all \(\binom dr\) random subsets, and applying the pair-overlap formula. It checks the sharp bound and exact motif defect on the cyclic projective-plane incidence systems \(2\)-\((7,3,1)\) and \(2\)-\((13,4,1)\), as well as strict inequality after degree-preserving incidence switches. It additionally tests the general non-design formula for \((d,r)=(9,3)\) and Vandermonde identities. The checker reports 39 assertions passed. This is a finite test; the universal theorem and asymptotic limit are proved above.

## Relationship to prior work

Chiclana, *Poisson occupancy of paths on permuted regular graphs* (arXiv:2610.14724v1, October 10, 2026), introduces the permuted-layer model and proves asymptotic Poisson occupancy and exact expected chi-square contraction. Its full-text Theorems 1.1–1.6 and Section 8 do not state the two-layer **variance of the number of empty destinations**, its graph-dependent motif decomposition, or the symmetric-design equality classification. The uniform-subset reduction uses the model rather than claiming the model itself is new. The full source covariance formula fixes expected chi-square solely through \(d,r\); by contrast, the two explicit seven-vertex regular kernels checked in `verify.py` have identical \(d=7,r=3\) and hence identical source chi-square expectation, yet vacancy variances \(4/25\) and \(48/175\), a strict difference of \(4/35\). Thus the source covariance identity alone does not determine the new variance observable.

Cameron and Soicher, *Block intersection polynomials* (2007), establish general incidence-counting and Vandermonde-type identities and are credited for this established combinatorial framework. Their inspected PDF develops inequalities for block-intersection counts; it does not give this stochastic two-layer variance extremum. Classical projective planes and symmetric designs are also established objects, not new constructions. No inference of originality is drawn merely from the absence of matching titles in searches.

## Limitations

The variance bound assumes integer \(\lambda\), and the equality classification is conditional on design existence. It is not claimed to give the exact minimum when a required design is absent, or for noninteger \(\lambda\). The strict-convexity proof uses \(d\ge3r-2\); the equality theorem is not extended outside that range. No normal limit, high-probability concentration estimate, or claim for three or more layers is made. Broader earlier design-optimality results may encompass parts of the extremal argument; historical priority requires independent evaluation.

## References

- R. Chiclana, *Poisson occupancy of paths on permuted regular graphs*, arXiv:2610.14724v1, first public October 10, 2026. https://arxiv.org/abs/2610.14724
- P. J. Cameron and L. H. Soicher, *Block intersection polynomials*, Bulletin of the London Mathematical Society 39 (2007), 559–564. https://doi.org/10.1112/blms/bdm034 ; lawful preprint https://webspace.maths.qmul.ac.uk/l.h.soicher/bip.pdf
- R. A. Bailey and L. H. Soicher, *Uniform semi-Latin squares and their pairwise-variance aberrations*, Journal of Statistical Planning and Inference 213 (2021), 282–291; arXiv:2008.10552 (different design-optimality setting).
