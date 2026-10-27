# Exact periodic Floquet spectrum distribution of the twisted baker map

## Finding
Let \(M\geq 2\), \(n\geq1\), and \(1\leq k\leq n\) be integers. Write \(g=\gcd(M,k)\), \(\ell=M/g\), \(q=k/g\), and \(N=n-k\). For the twisted baker map defined below, consider all nontrivial fixed points of its \(n\)-th iterate with precisely \(k\) right-branch visits in their length-\(n\) itineraries. Their **complete set of distinct return-Jacobian characteristic polynomials** is
\[
\left\{\prod_{r=0}^{g-1}\bigl(t^{\ell}-(-1)^q2^{q+b_r}\bigr):\quad b_r\in\mathbb Z_{\geq0},\ \sum_{r=0}^{g-1}b_r=N\right\}.
\]
Different vectors \((b_0,\ldots,b_{g-1})\) yield the same polynomial if and only if they are permutations of each other. Thus the number of **distinct eigenvalue multisets** is \(p_{\leq g}(N)\), the number of integer partitions of \(N\) into at most \(g\) parts, including the empty partition when \(N=0\). Its generating function is
\[
\sum_{N\geq0}p_{\leq g}(N)z^N=\prod_{j=1}^{g}(1-z^j)^{-1}.
\]

There is also an exact **frequency formula**, not just an existence classification. For a multiset \(\lambda\) of \(g\) nonnegative integers summing to \(N\), let \(\mathcal P(\lambda)\) be its distinct orderings. The number of fixed points with the characteristic polynomial determined by \(\lambda\) equals
\[
\boxed{\quad
W_{M,n,k}(\lambda)=\sum_{(b_0,\ldots,b_{g-1})\in\mathcal P(\lambda)}
\binom{b_0+q}{q}\prod_{r=1}^{g-1}\binom{b_r+q-1}{q-1}.
\quad}
\]
In particular \(\sum_{\lambda}W_{M,n,k}(\lambda)=\binom nk\): every nontrivial periodic point of this twist count is included once.

Define the **spectral modulus contrast** of a return Jacobian as the largest modulus of a complex eigenvalue divided by the smallest modulus. If \(g=1\) every such Jacobian has contrast \(1\). If \(g\geq2\), the sharp maximum is \(2^{N/\ell}\); the sharp minimum is \(1\) when \(g\mid N\) and \(2^{1/\ell}\) otherwise. Every stated extremum is attained by a period-dividing-\(n\) point with exactly \(k\) right visits.

## Assumptions and scope
The state space is \(X=[-1,1]\times[0,1]^{M-1}\), and the piecewise-affine map is
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\geq0.
\end{cases}
\]
The trivial fixed-point face \(\{x_1=-1\}\) is excluded. As in Saiki--Takahasi--Yorke, the length-\(n\) words containing a right symbol correspond bijectively to the nontrivial points of \(F^n(x)=x\), even when their least period properly divides \(n\). A branch is selected by the stated sign convention, and its one-sided derivative is used at a switch. The spectrum is the eigenvalue multiset of \(DF^n(x)\), **not** the singular-value spectrum; the modulus contrast therefore measures periodic eigenvalue anisotropy rather than one-step Euclidean distortion.

## Proof
**1. Inverse-itinerary correspondence.** The originating map's symbolic-coding lemma (Saiki--Takahasi--Yorke, Lemmas 2.4--2.6) identifies every length-\(n\) word containing a right symbol with exactly one nontrivial fixed point of \(F^n\), with no duplicated branch-boundary point. The all-left word belongs to the excluded fixed face. Fix \(k\geq1\) and express the word uniquely as
\[
L^{u_0}R L^{u_1}R\cdots R L^{u_k},\qquad
u_j\in\mathbb Z_{\geq0},\quad\sum_{j=0}^{k}u_j=N,
\]
where the \(u_j\) are uniquely determined nonnegative gap lengths.

**2. Weighted permutation cycles.** The two branch derivative matrices are
\[
J_L=\operatorname{diag}(2,1,\ldots,1),\quad
J_R e_j=\begin{cases}e_{j+1},&j<M,\\-2e_1,&j=M.\end{cases}
\]
Thus their ordered product along a word is a signed monomial matrix with underlying coordinate permutation \(j\mapsto j+k\pmod M\), partitioning coordinates into \(g\) cycles of length \(\ell\). Traversing one complete permutation cycle processes \(k\ell\) right-branch advances, which pass the cyclic coordinate boundary exactly \(k\ell/M=q\) times. Each passage contributes a factor \(-2\). Hence **each** cycle's signed multiplier already contains \((-1)^q2^q\) from the right visits, independently of the placement of left symbols.

A left symbol doubles the coordinate at index \(1\) of the intermediate state. If it occurs after exactly \(j\) preceding right symbols, that coordinate traces back to an initial coordinate with index congruent to \(1-j\pmod M\). Hence each left symbol contributes one further factor \(2\) to the permutation cycle indexed by \(j\pmod g\) (up to a fixed relabeling of cycle indices). Write
\[
b_r=\sum_{\substack{0\leq j\leq k\\j\equiv r\ (\mathrm{mod}\ g)}}u_j.
\]
The signed product on that cycle is exactly \((-1)^q2^{q+b_r}\), so its characteristic factor is \(t^{\ell}-(-1)^q2^{q+b_r}\), proving every actual return spectrum belongs to the stated family.

**3. No missing spectra.** Since \(k=qg\) with \(q\geq1\), the gap labels \(j=0,1,\ldots,k\) contain every residue modulo \(g\). Given any nonnegative integer vector \((b_0,\ldots,b_{g-1})\) summing to \(N\), place all \(b_r\) left symbols in gap \(j=r\) for \(r=0,\ldots,g-1\), with every remaining gap empty. This realizes exactly the prescribed cycle weights, and the coding lemma supplies a genuine periodic point. Thus **every** displayed polynomial is attained, not merely algebraically admissible.

**4. Exact frequencies and distinctness.** There are \(q+1\) gaps with index \(0\) modulo \(g\), and exactly \(q\) gaps for each other residue. For any labelled \(g\)-vector \(b\), the stars-and-bars numbers of solutions for the corresponding gap lengths multiply to
\[
\binom{b_0+q}{q}\prod_{r=1}^{g-1}\binom{b_r+q-1}{q-1}.
\]
Summing over all different assignments of the same multiset \(\lambda\) to labelled cycles gives the asserted exact frequency. The factors \(t^{\ell}-(-1)^q2^{q+b}\) have roots of modulus \(2^{(q+b)/\ell}\); factors with different \(b\) therefore have disjoint root moduli. The characteristic polynomial uniquely recovers the unordered multiset of \(b_r\). Distinct spectra are accordingly indexed by partitions with at most \(g\) parts. Summing over all gap words gives \(\binom nk\) by the bijection with choices of the \(k\) right-symbol positions.

**5. Sharp modulus contrasts.** From the cycle factors, the ratio of largest to smallest eigenvalue moduli is
\[
2^{(\max_r b_r-\min_r b_r)/\ell}.
\]
If \(g=1\) the ratio is necessarily one. If \(g\geq2\), among nonnegative vectors summing to \(N\), the maximum difference is \(N\), achieved by \((N,0,\ldots,0)\); the minimum difference is zero when \(g\mid N\), and otherwise one, achieved by allocating \(\lfloor N/g\rfloor\) or \(\lceil N/g\rceil\) to each coordinate. The surjectivity established in step 3 supplies periodic points at every extremum.

## Verification
The analytical argument proves the theorem for all allowed integer dimensions, periods and right-visit counts; numerical testing does not establish this unbounded assertion. The self-contained `check_partition_spectra.py` uses exact integer matrices, computes characteristic polynomials by the Faddeev--LeVerrier recurrence, and independently enumerates every binary length-\(n\) word with \(2\leq M\leq6\) and \(1\leq n\leq8\), grouped by right-visit count. It compares full return characteristic polynomials with all predicted compositions, checks the exact word frequencies for each spectrum, and checks partition counts and their total binomial sum. The observed output is `CHECK_OK 2510 exact Jacobian characteristic-polynomial comparisons, 180 exact spectral-frequency distributions`. Execute with `python check_partition_spectra.py`; Python standard library suffices.

## Relationship to prior work
Saiki, Takahasi and Yorke introduced the twisted baker map and proved its symbolic coding, total count of nontrivial fixed points of iterates, and density/equidistribution statements distinguishing real versus nonreal multipliers. The published *Exact real-spectrum residue law for the twisted baker map* further proves that the full return characteristic polynomial factors into signed monomial-cycle factors \(t^\ell-(-1)^{k/g}2^{a_r}\), with unspecified nonnegative exponent data satisfying \(\sum a_r=n\), and it determines exact real/nonreal proportions. Those statements are **not** claimed here. This theorem resolves the additional *attainability, frequency and extremal-anisotropy* problems for the fine Floquet spectra conditional on exact twist count: the sharp lower bound \(a_r\geq k/g\), the sufficient and necessary partition of \(n-k\), exact multiplicities for each eigenvalue multiset, and both optimal modulus contrasts. A published study of periodic-point measures for heterochaos baker maps concerns different dynamical maps and does not imply these particular formulas.

## Limitations
The census includes points of period dividing \(n\), not only primitive period-\(n\) points. It is conditional on exactly \(k\) right symbols and excludes the nonisolated all-left fixed face. The result does not determine singular values, subexponential pseudospectral phenomena, nonlinear perturbations, or a central limit theorem for the spectral profile. The exact symbolic word--point correspondence is cited from the originating full text. Published-search comparisons cannot exclude an equivalent result in unindexed literature.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first publicly submitted 9 February 2022, especially Lemmas 2.1--2.6 and periodic-point results. https://arxiv.org/abs/2202.04304
2. *Exact real-spectrum residue law for the twisted baker map*, public mathematical research record dated 11 October 2026, specifically its full `RESULT.md` and weighted monomial-factorization proof. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261, submitted 2 September 2024 (different family). https://arxiv.org/abs/2409.01261
