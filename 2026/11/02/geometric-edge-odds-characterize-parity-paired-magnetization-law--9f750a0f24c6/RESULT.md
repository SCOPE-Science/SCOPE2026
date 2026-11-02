# Geometric edge odds characterize parity-paired magnetization laws in finite spin chains

## Finding
Consider a path of \(m\ge2\) spins taking values \(\pm1\), with a fair initial spin and independent nearest-neighbor flip indicators. Write \(K\) for its number of sign changes and \(M\) for the sum of its spins. If the edge flip odds form a geometric progression, \(w_i=\lambda q^i\) for \(1\le i<m\) and \(\lambda,q>0\), then
\[
\mathcal L(M\mid K=2j-1)=\mathcal L(M\mid K=2j),\qquad 1\le j,\quad 2j\le m-1.
\]
Moreover, as the paired index \(j\) increases, the laws of \(|M|\) decrease **strictly in monotone likelihood-ratio order**. In particular, for any strictly increasing function \(h\) on the attainable absolute magnetizations,
\[
\operatorname{Cov}\bigl(K,h(|M|)\bigr)<0,\qquad m\ge2.
\]

Conversely, suppose a path has \(n\ge4\) spins and strictly positive finite flip odds \(w_1,\ldots,w_{n-1}\). The following two conditions are equivalent: (a) on every contiguous four-spin subpath, the conditional law of its spin sum given one change equals that given two changes; (b) \(w_i=\lambda q^i\) for some \(\lambda,q>0\) and all \(i\). Thus the parity pairing on overlapping four-spin windows **characterizes** precisely the geometric-odds family. Here a subpath is assigned its own number of changes and spin sum.

## Assumptions and scope
Fix \(n\ge2\). Let \(X_1\) be uniform on \(\{-1,1\}\). For \(1\le i<n\), independently sample \(B_i\in\{0,1\}\) with \(\Pr(B_i=1)=w_i/(1+w_i)\), where every \(w_i\in(0,\infty)\). Set \(X_{i+1}=X_i(-1)^{B_i}\), \(K=\sum_{i=1}^{n-1}B_i\), \(M=\sum_{i=1}^{n}X_i\). A contiguous subpath inherits its independent change indicators and has a fair first spin by global spin-flip symmetry. Products \(\lambda q^i\) may be reindexed on a subpath by rescaling \(\lambda\). The theorem concerns free, spin-flip-symmetric boundary conditions; it does not concern a fixed initial spin, an external magnetic field, a cyclic chain, or dependent changes.

Define for \(Q>0\) the Gaussian coefficient
\[
G_Q(v,r)=\prod_{t=1}^{r}\frac{1-Q^{v-r+t}}{1-Q^t},\quad 0\le r\le v,
\]
with the value \(\binom vr\) at \(Q=1\), and zero for indices outside \(0\le r\le v\). The product has the usual positive, polynomial continuation for \(Q>0\). Define \(E_k(q,m)=q^{k(k+1)/2}G_q(m-1,k)\). All displayed conditional distributions are well-defined because every possible change count has positive probability.

## Proof
**1. Conditional weighted subset representation.** Since each change set \(S\subseteq\{1,\ldots,m-1\}\) has probability proportional to \(\lambda^{|S|}q^{\sum_{i\in S}i}\), its law conditional on \(K=k\) gives \(S\) weight \(q^{\sum_{i\in S}i}/E_k(q,m)\). The initial sign remains independently fair. Consequently the parameter \(\lambda\) cancels from every conditional magnetization law. This also proves the statement for arbitrary geometric subpaths.

**2. Run-composition identity.** For a word with \(a\) plus and \(b=m-a\) minus spins, a configuration with \(2j-1\) changes has exactly \(j\) runs of each sign. Splitting by the initial sign and enumerating positive run lengths using the Gaussian-binomial composition identity gives the unnormalized magnetization mass
\[
W^o_j(a)=q^{2j(j-1)}(q^a+q^b)G_{q^2}(a-1,j-1)G_{q^2}(b-1,j-1).
\]
The actual probability is \(W^o_j(a)/(2E_{2j-1}(q,m))\). To verify the composition identity directly, encode \(j\) positive run lengths of total \(R\) by their \(j-1\) strictly increasing cumulative boundaries. Their Gaussian subset sum is \(q^{j(j-1)}G_{q^2}(R-1,j-1)\), with the prefactors above resulting from the positions of alternating boundaries.

For \(2j\) changes there are \(j+1\) runs of the initial sign and \(j\) of the other. The same enumeration yields
\[
W^e_j(a)=q^{2j^2}\bigl[q^bG_{q^2}(a-1,j)G_{q^2}(b-1,j-1)+q^aG_{q^2}(a-1,j-1)G_{q^2}(b-1,j)\bigr].
\]
The Gaussian coefficient quotient \(G_{q^2}(v,j)/G_{q^2}(v,j-1)=(1-q^{2(v-j+1)})/(1-q^{2j})\), together with \(a+b=m\), gives the **pointwise proportionality**
\[
W^e_j(a)=q^{2j}\frac{1-q^{m-2j}}{1-q^{2j}}W^o_j(a).
\]
For \(q=1\), this ratio is \((m-2j)/(2j)\). Since the factor is independent of \(a\), normalization proves the parity-paired conditional laws. The formulas hold for \(j\ge1\) when the associated change counts are permitted; the last odd count in an even-length chain is allowed to be unpaired.

**3. Likelihood-ratio ordering.** The mass at \(a\) in the law for paired index \(j+1\), divided by that for index \(j\), is a positive constant independent of \(a\), times
\[
\bigl(1-q^{2(a-j)}\bigr)\bigl(1-q^{2(m-a-j)}\bigr)
\]
on the common support \(j+1\le a\le m-j-1\). The product is nonnegative and, letting \(d=|a-m/2|\), becomes
\[
1+q^{2(m-2j)}-2q^{m-2j}\cosh(2d\log q).
\]
It is strictly decreasing in \(d\) whenever \(q\ne1\). Its normalized limit at \(q=1\) is \((a-j)(m-a-j)=(m/2-j)^2-d^2\), also strictly decreasing. The support of index \(j+1\) is properly contained in that of index \(j\). Symmetry under global sign reversal then proves strict monotone likelihood-ratio domination for the distributions of \(|M|\), and therefore strict first-order stochastic domination for each consecutive pair of indices.

At \(K=0\), \(|M|=m\) deterministically, exceeding the nonconstant law for \(K=1\). The conditional means \(\mathbb E[h(|M|)\mid K=k]\) therefore form a nonincreasing function of \(k\), constant on each \((2j-1,2j)\) pair and strictly decreasing at each transition between pairs. Because every \(k\in\{0,\ldots,m-1\}\) has positive probability, the independent-copy identity for covariance implies \(\operatorname{Cov}(K,h(|M|))<0\) for every strictly increasing \(h\).

**4. Sharp four-site converse.** For one four-spin subpath write its three consecutive odds \(u,v,w>0\). In the conditional laws with one and two changes, the respective probabilities that its magnetization is zero are
\[
\frac{v}{u+v+w}\quad\text{and}\quad\frac{uw}{uv+uw+vw}.
\]
For a four-spin chain both magnetization laws are symmetric and supported on \(\{-2,0,2\}\), so equality is equivalent to equality of these central masses. Cross multiplication reduces to \(v^2=uw\). Applying this on every overlapping four-spin window forces \(w_{i+1}^2=w_iw_{i+2}\), so consecutive ratios agree, giving \(w_i=\lambda q^i\). Conversely the first three steps prove each local equality in the geometric case. This establishes the characterization.

## Verification
The standalone file `verify.py` uses exact rational arithmetic and exhaustively sums all weighted change subsets and both initial signs for each chain of lengths \(2\) through \(11\), at \(q\in\{1/2,1,3/2,2\}\). It independently checks the Gaussian-binomial formulas, odd/even plateau equalities, strict stochastic tails, and decreasing likelihood ratios, including the four-spin converse for several geometric and nongeometric triples. Run `python3 verify.py`; the expected result is `PASS exact assertions: 986`. The all-length theorem is proved algebraically above; finite enumeration is corroboration, not proof.

## Relationship to prior work
Antal, Droz and Rácz study finite-chain magnetization and domain-wall counts with *homogeneous* Ising coupling and free boundary conditions; their domain-wall/magnetization formulas encompass the uniform-edge member \(q=1\). This paper supplies important known background rather than a novelty claim for the homogeneous case. Denisov and Hänggi investigate finite homogeneous-chain domain statistics and related joint counts. The present result instead classifies spatially varying edge odds by a local parity-pairing property and obtains a strict global absolute-magnetization ordering throughout that family, including \(q\ne1\). Classical Gaussian-binomial subset identities are used as ingredients, not claimed new. An older or broader weighted-run enumeration could still imply some statements; historical priority is not certified.

## Limitations
The theorem requires a fair initial spin, independent changes, and strictly positive finite edge odds. The characterization needs windows with four spins (hence overall length at least four). Equality of the laws for a single full chain alone has not been characterized. Strict likelihood-ratio ordering refers to absolute magnetization between distinct paired indices; the signed magnetization laws are symmetric and not asserted stochastically ordered. It does not assert an independent proof of novelty, independent validation, or a new result for homogeneous finite Ising magnetization already covered by earlier formulas.

## References
- T. Antal, M. Droz and Z. Rácz, *Probability distribution of magnetization in the one-dimensional Ising model: Effects of boundary conditions*, arXiv:cond-mat/0308442, initially public 2003-08-21, https://arxiv.org/abs/cond-mat/0308442.
- S. Denisov and P. Hänggi, *Domain statistics in a finite Ising chain*, arXiv:cond-mat/0603417, initially public 2006-03-15, https://arxiv.org/abs/cond-mat/0603417.
- T. Konstantopoulos and L. Yuan, *A probabilistic interpretation of the Gaussian binomial coefficients*, Journal of Applied Probability 54 (2017), 1295–1298, https://doi.org/10.1017/jpr.2017.64 (background on Gaussian coefficients, not a priority claim).
