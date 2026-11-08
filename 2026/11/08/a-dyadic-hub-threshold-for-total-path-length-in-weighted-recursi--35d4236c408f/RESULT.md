# A dyadic-hub threshold for total path length in weighted recursive trees

## Finding

Consider the weighted recursive tree on vertices \(1,2,\ldots\), rooted at \(1\). At the arrival of vertex \(j\ge2\), independently choose its parent \(i<j\) with probability proportional to a fixed deterministic weight \(w_i\). For a fixed exponent \(\beta\ge0\), set

\[
w_j=\begin{cases}j^\beta,&j\text{ is a power of }2,\\1,&\text{otherwise.}\end{cases}
\]

Write \(D_j\) for the root depth of vertex \(j\) and \(T_n=\sum_{j=1}^nD_j\) for total path length. The following is a sharp dichotomy *within this dyadic-hub weight family*:

**Theorem.** If \(0\le\beta<1\), there is a nonconstant, square-integrable random variable \(Z_\beta\) and a finite deterministic number \(c_\beta\) such that

\[
\frac{T_n}{n}-\log n\longrightarrow c_\beta+Z_\beta
\quad\text{almost surely and in }L^2,
\]

where \(\mathbb E Z_\beta=0\) and \(\operatorname{Var}(Z_\beta)>0\). In particular,

\[
\frac{\operatorname{Var}(T_n)}{n^2}\longrightarrow\operatorname{Var}(Z_\beta)\in(0,\infty).
\]

For every \(\beta\ge1\), there exist \(a_\beta>0\) and \(n_\beta<\infty\) such that

\[
\frac{\operatorname{Var}(T_n)}{n^2}\ge a_\beta\log n\qquad(n\ge n_\beta).
\]

Thus no finite-variance \(L^2\) limit at the linear fluctuation scale is possible when \(\beta\ge1\). The latter conclusion does **not** assert non-tightness or rule out convergence after a larger normalization.

For \(0\le\beta<1\), put \(W_j=\sum_{i=1}^jw_i\), \(p_j=w_j/W_j\), and let \(\gamma\) be Euler's constant. An explicit convergent-series description of the center is

\[
c_\beta=\gamma-1+\sum_{j=1}^\infty\left(p_j-\frac1j\right).
\]

The case \(\beta=0\) reduces to uniform recursive attachment and \(c_0=\gamma-1\). All conclusions concern a fixed exponent \(\beta\) as \(n\to\infty\).

## Assumptions and scope

All weights are strictly positive and deterministic, all parent choices are independent conditional on these weights, and depths are counted in edges from the root. The exact spike set consists of powers of two including vertex \(1\). The theorem classifies the **linear fluctuation variance and convergence boundary** in this specified family; it does not characterize every deterministic weight sequence, nor identify the distribution of \(Z_\beta\).

## Proof

**1. Insertion-depth law.** Put \(p_1=1\). For arbitrary positive deterministic weights, the recursive parent rule implies the probability generating identity

\[
\mathbb E[z^{D_j}]=z\prod_{r=2}^{j-1}\bigl(1+p_r(z-1)\bigr),\qquad j\ge2.
\]

Indeed, writing \(G_j(z)=\sum_{i=1}^jw_i\mathbb E[z^{D_i}]\), the identity \(G_j(z)=G_{j-1}(z)(1+w_jz/W_{j-1})\) and \(\mathbb E[z^{D_{j+1}}]=zG_j(z)/W_j\) telescope. Hence \(D_j\) has the distribution of \(1\) plus a sum of independent Bernoulli variables with respective parameters \(p_2,\ldots,p_{j-1}\). In particular,

\[
\mathbb E D_j=\sum_{r<j}p_r,\qquad
\operatorname{Var}(D_j)=\sum_{2\le r<j}p_r(1-p_r).
\]

The independence here is a representation of the *marginal depth law*, not an assertion that different vertex depths are independent.

**2. A depth-mean martingale.** Let \(\mathcal F_j\) be the tree history through \(j\), and set \(\mu_j=\sum_{i\le j}w_iD_i/W_j\). At arrival \(j\ge2\), let \(P_j\) be the chosen parent and define the martingale difference \(\xi_j=D_{P_j}-\mu_{j-1}\). It satisfies \(\mathbb E(\xi_j\mid\mathcal F_{j-1})=0\), with conditional variance

\[
v_j=\sum_{i<j}\frac{w_i}{W_{j-1}}(D_i-\mu_{j-1})^2.
\]

Updating \(\mu_j\) gives \(\mu_j=\mu_{j-1}+p_j(1+\xi_j)\). Thus \(M_j=\mu_j-\sum_{r=2}^jp_r=\sum_{r=2}^jp_r\xi_r\) is a mean-zero martingale, and exact expansion of each insertion depth gives

\[
T_n-\mathbb ET_n=\sum_{j=2}^n\bigl[1+(n-j)p_j\bigr]\xi_j.
\tag{1}
\]

The terms are orthogonal in \(L^2\), hence

\[
\frac{\operatorname{Var}(T_n)}{n^2}
=\sum_{j=2}^n\left(\frac{1+(n-j)p_j}{n}\right)^2\mathbb Ev_j.
\tag{2}
\]

**3. Sublinear hubs.** Assume \(0\le\beta<1\). Since \(W_j\ge j\), every nonhub satisfies \(p_j\le1/j\), while a hub \(j=2^k\) satisfies \(p_j\le2^{-k(1-\beta)}\). Summing shows \(\sum_{r\le j}p_r=O_\beta(\log(j+1))\). Step 1 consequently gives \(\max_{i\le j}\mathbb ED_i^2=O_\beta(\log^2(j+1))\), and the definition of conditional variance gives \(\mathbb Ev_j=O_\beta(\log^2(j+1))\).

It follows that

\[
\sum_{j\ge2}p_j^2\mathbb Ev_j
\le C_\beta\sum_{j\ge2}\frac{\log^2(j+1)}{j^2}
+C_\beta\sum_{k\ge1}k^2 2^{-2k(1-\beta)}<\infty.
\]

The martingale \(M_n\) therefore converges almost surely and in \(L^2\) to a centered variable \(Z_\beta\). Since \(\sum_j\mathbb E\xi_j^2/j^2<\infty\), the martingale series \(\sum_j\xi_j/j\) converges almost surely and in \(L^2\). Kronecker's lemma (and the corresponding \(L^2\) bound) gives \(n^{-1}\sum_{j\le n}\xi_j\to0\) almost surely and in \(L^2\). From

\[
\frac{T_n-\mathbb ET_n}{n}
=\frac1n\sum_{j=2}^nM_{j-1}+\frac1n\sum_{j=2}^n\xi_j,
\]

Cesàro convergence yields the claimed limit \(Z_\beta\). Strict positivity of its variance follows already from the nonzero martingale innovation at arrival \(3\): vertices \(1\) and \(2\) have different depths and both positive parent-selection probabilities.

**4. The deterministic center.** For \(0\le\beta<1\), the cumulative excess hub weight is \(W_j-j=O_\beta(j^\beta)\), with the convention \(W_j=j\) at \(\beta=0\). Hence the nonhub differences \(p_j-1/j\) are absolutely summable, as are the hub differences, bounded by a geometric series in \(2^{-k(1-\beta)}\). The insertion-depth identity therefore implies

\[
\mathbb ED_j=\log j+\gamma+\sum_{r\ge1}(p_r-1/r)+o(1).
\]

Averaging over \(j\le n\) and using \(n^{-1}\sum_{j\le n}\log j=\log n-1+o(1)\) proves \(\mathbb ET_n/n-\log n\to c_\beta\).

**5. Linear and superlinear hubs.** Fix \(\beta\ge1\) and define \(C_\beta=1+(2^\beta-1)^{-1}\). For every \(k\ge3\), the total weight immediately before the hub at \(j=2^k\) satisfies \(W_{j-1}\le C_\beta 2^{k\beta}\). Consequently its own normalized mass satisfies

\[
p_j\ge\frac1{C_\beta+1}.
\]

At the moment just before its arrival, the two earlier hubs \(A=2^{k-1}\), \(B=2^{k-2}\) have normalized parent-selection probabilities at least \(2^{-\beta}/C_\beta\) and \(2^{-2\beta}/C_\beta\), respectively. The weighted-variance identity gives

\[
v_j=\sum_{a<b<j}\frac{w_aw_b}{W_{j-1}^2}(D_a-D_b)^2
\ge\frac{2^{-3\beta}}{C_\beta^2}(D_A-D_B)^2.
\]

By Step 1, \(\mathbb ED_A-\mathbb ED_B=\sum_{r=B}^{A-1}p_r\ge p_B\ge1/(C_\beta+1)\). Jensen's inequality yields the uniform lower bound

\[
\mathbb Ev_{2^k}\ge
\frac{2^{-3\beta}}{C_\beta^2(C_\beta+1)^2}>0.
\tag{3}
\]

For every hub \(j\le n/2\), the coefficient in (2) is at least \(p_j/2\), so (2) and (3) imply

\[
\frac{\operatorname{Var}(T_n)}{n^2}
\ge\frac{2^{-3\beta}}{4C_\beta^2(C_\beta+1)^4}
\left(\left\lfloor\log_2(n/2)\right\rfloor-2\right)
\]

for sufficiently large \(n\). This is at least a positive constant depending on \(\beta\) times \(\log n\), finishing the proof.

## Verification

The companion standalone `CHECK.py` executes exact rational enumerations of every parent-choice tree through eight vertices for exponents \(0,1,2\), compares first and second total-path-length moments with (1)–(2), verifies the martingale-variance expression, and checks the hub lower bounds with rational arithmetic through vertex \(256\) for integer exponents. Invoke `python3 CHECK.py` using Python's standard library. The checker is a finite diagnostic; the preceding inequalities and martingale arguments, not the enumeration, establish the infinite theorem.

## Relationship to prior work

Gałązka and Wdowicka (2026, arXiv:2610.00614, Sections 5–6 and 10) derive the innovation representation and prove linear-scale martingale limits under the sufficient condition \(p_j=O(1/j)\). Here this condition fails for every \(\beta>0\) along the hub subsequence. Their discussion specifically asks for more general deterministic weight sequences and a boundary of the condition. The present theorem uses their exact martingale viewpoint but provides the explicit all-exponent dyadic-hub classification, including logarithmically divergent normalized variances above the boundary.

Sénizergues (2019/2021, arXiv:1904.07115) proves broad profile results under polynomial-precision cumulative-weight hypotheses. Our \(\beta<1\) family satisfies \(W_j=j(1+O(j^{-(1-\beta)}))\), so aspects of the positive-regime limit may also follow from that stronger theory. **No novelty is claimed for the positive-regime limit alone.** The significant boundary statement is the contrast with \(\beta\ge1\), when geometric hub mass persists and the normalized variance diverges. Earlier work on weighted node depths in increasing tree families addresses a different weighting convention; a complete comparison with all older formulations remains a priority risk.

## Limitations

The classification is specific to geometrically spaced hubs and deterministic positive weights. At and above the threshold the result proves divergence of the variance on the \(n\) scale, not a central limit theorem, a larger-scale limit, or failure of tightness. It does not determine the law of the subcritical limiting variable. Full historical priority and independent validation have not been established.

## References

- M. Gałązka and H. Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614 (first posted 2026-09-30), https://arxiv.org/abs/2610.00614.
- D. Sénizergues, *Geometry of weighted recursive and affine preferential attachment trees*, arXiv:1904.07115; *Electronic Journal of Probability* 26 (2021), https://arxiv.org/abs/1904.07115.
- C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735; *Journal of Statistical Mechanics* 2019, https://arxiv.org/abs/1810.02735.
- M. Kuba and A. Panholzer, *On Weighted Path Lengths and Distances in Increasing Trees*, *Probability in the Engineering and Informational Sciences* 21 (2007), 419–433, https://doi.org/10.1017/S0269964807000058.
