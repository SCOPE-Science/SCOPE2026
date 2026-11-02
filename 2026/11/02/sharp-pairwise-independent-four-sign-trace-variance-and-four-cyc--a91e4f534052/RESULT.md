# Sharp pairwise-independent four-sign trace variance and four-cycle rigidity

## Finding
Let \(B\in\mathbb R^{4\times4}\) be any real symmetric matrix. One unbiased single-query trace estimator is \(T=s^{\mathsf T}Bs\), where \(s\in\{-1,1\}^4\) is a **fair pairwise-independent** sign vector: \(\mathbb E s_i=0\) and \(\mathbb E(s_is_j)=0\) for all distinct indices. The joint law may otherwise be arbitrary. Set
\[
u=(B_{12},B_{13},B_{14}),\qquad v=(B_{34},B_{24},B_{23}),\qquad S=u\cdot v.
\]
For every admissible law define \(\kappa=\mathbb E(s_1s_2s_3s_4)\in[-1,1]\). Then
\[
\operatorname{Var}(T)=4(\|u\|_2^2+\|v\|_2^2)+8\kappa S,
\]
and the sharp minimum over **all** admissible fair pairwise-independent sign laws is
\[
\boxed{\min\operatorname{Var}(T)=4\min\{\|u-v\|_2^2,\|u+v\|_2^2\}.}
\]
If \(S>0\), the **unique** minimizing law is uniform on the eight sign vectors satisfying \(s_1s_2s_3s_4=-1\). If \(S<0\), the unique minimizer is uniform on the eight vectors with product \(+1\). If \(S=0\), every admissible law is optimal. Thus an exactly zero-variance unbiased single-probe estimator exists in this class **if and only if** \(u=v\) or \(u=-v\).

For a weighted undirected four-cycle with edge weights \(a,b,c,d\) in cyclic order, every off-cycle off-diagonal entry zero, and nonnegative weights, the product-minus-one parity law is optimal for **every** such weight choice, with the exact robust variance
\[
\boxed{\operatorname{Var}(T)=4[(a-c)^2+(b-d)^2].}
\]
It is zero whenever opposite edge weights match. For the unweighted four-cycle adjacency \(A\), \(I+\tfrac14A\) is strictly positive definite and has \(\operatorname{Var}_{\mathrm{iid}}(T)=1\) versus \(\operatorname{Var}_{\mathrm{parity-}}(T)=0\). For every real-valued spectral function \(f\) on the spectrum of \(A\), the symmetric matrix \(f(A)\) has paired opposite entries, and its trace is likewise computed exactly by one parity-minus probe (assuming an exact matrix-function-vector product). On a block diagonal sum of such four-cycles, independent parity-minus choices per block yield an isotropic full-length probe and the exact full trace.

The first dimension in which fair pairwise independence can improve the Hutchinson single-probe variance is four: in dimensions two and three there are no disjoint off-diagonal edge pairs, so the variance is identical to that under fully independent fair signs.

## Assumptions and scope
The matrix \(B\) is real symmetric and finite-dimensional, and the oracle computes \(Bs\) exactly. The sampling law is supported on the sixteen full-amplitude binary sign vectors and has **both** fair one-dimensional marginals and pairwise independence. These conditions entail \(\mathbb E ss^{\mathsf T}=I\), hence unbiasedness. Fairness is necessary for the stated uniqueness assertion. No independence assumption is imposed on triples or all four signs. Formulae quantify variance over one random probe; diagonal entries of \(B\) may be arbitrary. The weighted-cycle corollary assumes the fixed vertex ordering \(1,2,3,4\), with edges \((1,2),(2,3),(3,4),(4,1)\) and real nonnegative weights \(a,b,c,d\), respectively.

## Proof
**(1) Mean and centered estimator.** Since each \(s_i^2=1\) and \(\mathbb E(s_is_j)=0\) for \(i\ne j\),
\[
\mathbb ET=\operatorname{tr}(B),\quad T-\operatorname{tr}(B)=2\sum_{1\le i<j\le4}B_{ij}s_is_j.
\]

**(2) Fourth-order reduction.** In the square of this centered quantity, each squared-edge term has expectation one. Two distinct edges with a shared vertex reduce, after \(s_i^2=1\), to an off-diagonal pairwise product, whose expectation is zero. The only remaining cross terms are the three pairs of vertex-disjoint edges \((12,34),(13,24),(14,23)\). Each has expectation \(\kappa=\mathbb E(s_1s_2s_3s_4)\). Their factor is eight, giving exactly
\[
\operatorname{Var}(T)=4\sum_{i<j}B_{ij}^2+8\kappa(B_{12}B_{34}+B_{13}B_{24}+B_{14}B_{23}).
\]
There are no omitted terms or assumptions beyond the stated pairwise moments.

**(3) Extremal laws and uniqueness.** Every random sign product is \(\pm1\), so \(|\kappa|\le1\). Both endpoints are realized by uniform distributions over the even- and odd-product parity cosets. The first, second and third sign moments under either coset vanish: for degree three, \(s_is_js_k=\pm s_\ell\), with \(\ell\) the omitted coordinate and the fixed product sign. Hence these cosets are actually three-wise independent. The linear function of \(\kappa\) in step (2) is minimized at \(\kappa=-\operatorname{sign}(S)\) if \(S\ne0\). If \(\mathbb E(s_1s_2s_3s_4)=\pm1\), the product itself equals that sign almost surely. The fairness and pairwise conditions then determine the Fourier-Walsh moments of every monomial: degree-one and degree-two moments vanish; each degree-three moment is the fixed product times the complementary degree-one moment, hence vanishes; the degree-four moment is fixed. Walsh inversion on \(\{-1,1\}^4\) therefore forces the **unique** distribution \(\mathbb P(s=z)=(1\pm z_1z_2z_3z_4)/16\), uniform on the corresponding parity coset. If \(S=0\), step (2) is constant over all admissible laws. Completing squares gives
\[
4(\|u\|^2+\|v\|^2)-8|u\cdot v|
=4\min\{\|u-v\|^2,\|u+v\|^2\}.
\]
The minimum is zero precisely when the appropriate equality holds.

**(4) Four-cycle weights and the smallest dimension.** With \(B_{12}=a,B_{23}=b,B_{34}=c,B_{14}=d\), the other off-diagonal entries zero, one has \(u=(a,0,d)\), \(v=(c,0,b)\). For nonnegative weights \(S=ac+bd\ge0\), so the odd parity coset is optimal and the variance reduces to \(4[(a-c)^2+(d-b)^2]\). Equality of opposite edge weights implies zero variance regardless of diagonal. When \(n\le3\), any two distinct off-diagonal edges overlap in one vertex; all cross expectations in the centered-square expansion are therefore zero, implying the independent-sign variance for every fair pairwise-independent probe.

**(5) The positive-definite and matrix-function examples.** On the undirected four-cycle, \(A\) has eigenvalues \(2,0,0,-2\), so \(I+A/4\) has eigenvalues \(3/2,1,1,1/2\). Its four off-diagonal edge entries are \(1/4\): the fully independent sign law has variance \(4\cdot4(1/4)^2=1\), whereas odd parity gives variance zero. Any real spectral function of \(A\) is real symmetric and commutes with the cyclic permutation; its opposite-edge entries match, yielding the same zero-variance conclusion. For independent four-cycle blocks, conditional on each block sign vector its scalar trace estimate is already exact, so their sum is exact. The concatenated sign vector remains fair and pairwise independent, including across blocks.

## Verification
The accompanying standalone Python standard-library file `verify.py` computes \(s^{\mathsf T}Bs\) and the exact finite-distribution variance using rational arithmetic. It checks all \(5^6=15{,}625\) off-diagonal six-tuples with integer entries from \(-2\) through \(2\) for independent signs and both parity cosets; checks one thousand additional diagonal shifts; confirms the positive-definite example, an eight-dimensional two-block construction, and a family of nonuniform weighted-cycle defect identities. Reproduce with `python3 verify.py`, expecting `VERIFY_OK exact_cases=16774 exhaustive_integer_coefficient_matrices=15625`. Finite checks supplement, but do not replace, the universal algebraic argument above.

## Relationship to prior work
Frommer, Rinelli and Schweitzer (first public 2023-08-15, arXiv:2308.07722) study stochastic probing of sparse matrix-function traces, with standard independent Rademacher probes and graph-coloring variance analysis. The present theorem changes **within-vector dependence**, while preserving every fair marginal and every pairwise product moment, and classifies the entire feasible four-variable class. Fitzsimons, Osborne, Roberts and Fitzsimons (arXiv:1608.00117) instead compare mutually unbiased-basis and traditional probe ensembles on broader worst-case objectives. Wimmer, Wu and Zhang (arXiv:1405.7112) establish matrix-query complexity in worst-case models; this matrix-dependent one-shot variance optimum does not contradict their lower bounds. Pass and Spektor (arXiv:1412.7859) discuss pairwise-independent Rademacher moments; the fourth-moment dependence mechanism is classical and **not** claimed new. Epperly, Tropp and Webber (arXiv:2301.07825) analyze exchangeable trace estimation and variance reduction using multiple probes. None of these inspected results directly asserts the exact six-coefficient optimum, uniqueness of the binary parity coupling, or the four-cycle symmetry-defect variance in the stated class. Related fixed-structure Hadamard and probing constructions are prior art; publication priority of some equivalent specialized formulation is not conclusively established.

## Limitations
This is a restricted **four-coordinate fair binary** probe design theorem, not an oracle-universal trace-estimation optimality result. A fixed parity law is not uniformly better for arbitrary signed matrices: when \(S<0\), the opposite parity minimizes variance. If weights are not known a priori, selecting the parity may require extra information. Exact zero variance for cycle and matrix-function examples presumes an exact matrix-vector action; floating-point or Krylov approximation errors are not quantified. Outside four coordinates there is no claimed complete optimal-coupling classification. No independent scientific audit or universal publication-priority certification has been performed.

## References
1. A. Frommer, M. Rinelli and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722 (first public 2023-08-15), https://arxiv.org/abs/2308.07722.
2. J. K. Fitzsimons, M. A. Osborne, S. J. Roberts and J. F. Fitzsimons, *Improved stochastic trace estimation using mutually unbiased bases*, arXiv:1608.00117 (2016), https://arxiv.org/abs/1608.00117.
3. J. Wimmer, Y. Wu and P. Zhang, *Optimal query complexity for estimating the trace of a matrix*, arXiv:1405.7112 (2014), https://arxiv.org/abs/1405.7112.
4. B. Pass and E. Spektor, *On Khintchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859 (2014), https://arxiv.org/abs/1412.7859.
5. E. N. Epperly, J. A. Tropp and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825 (2023), https://arxiv.org/abs/2301.07825.
