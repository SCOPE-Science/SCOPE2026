# Exact rank-failure laws distinguish affine types in four-column Hadamard sketches

## Finding
Fix any \(d\ge3\) and \(N=2^d\). For any four distinct coordinates \(S=\{a_1,a_2,a_3,a_4\}\subset\mathbb F_2^d\), sample rows from the normalized Walsh--Hadamard matrix, optionally preceded by independent coordinate sign flips. The probability that this sketch **fails to be injective on the four-coordinate subspace** depends on \(S\) solely through the affine parity \(\epsilon(S)=a_1\oplus a_2\oplus a_3\oplus a_4\): the two cases have different exact laws despite identical row leverage scores and coherence.

Write \(P_0\) for \(\epsilon(S)=0\) (an affine plane) and \(P_1\) for \(\epsilon(S)\ne0\) (four affinely independent points). For independent uniform row draws *with replacement*, for every integer \(m\ge1\),
\[
\begin{aligned}
P_0^{\rm rep}(m)&=4(3/4)^m-6(1/2)^m+4(1/4)^m,\\
P_1^{\rm rep}(m)&=12(1/2)^m+8(3/8)^m-68(1/4)^m+72(1/8)^m.
\end{aligned}
\]
For a uniformly random \(m\)-element set of distinct rows, \(1\le m\le N\), write \(B_t(m)=\binom{t}{m}/\binom Nm\), with \(\binom{t}{m}=0\) when \(m>t\). Then
\[
\begin{aligned}
P_0^{\rm nr}(N,m)&=4B_{3N/4}(m)-6B_{N/2}(m)+4B_{N/4}(m),\\
P_1^{\rm nr}(N,m)&=12B_{N/2}(m)+8B_{3N/8}(m)-68B_{N/4}(m)+72B_{N/8}(m).
\end{aligned}
\]
The formulas are exact (not estimates) in exact arithmetic. Without replacement, injectivity is guaranteed for **every** row set precisely when \(m>3N/4\) in the affine-plane case and when \(m>N/2\) in the affine-independent case; at either stated threshold there are singular row sets. With replacement \(P_0^{\rm rep}(m)>P_1^{\rm rep}(m)\) for every \(m\ge4\), and
\[
P_0^{\rm rep}(m)\sim4(3/4)^m,\qquad P_1^{\rm rep}(m)\sim12(1/2)^m.
\]
Thus the two fixed four-dimensional coordinate subspaces can require asymptotically different row counts for the same small failure target even though every row has exactly the same squared leverage score \(4/N\). For \(N=8,m=4\), the respective no-replacement failure probabilities are \(27/35\) and \(6/35\).

## Assumptions and scope
Identify the \(N\) row and column indices with \(\mathbb F_2^d\); define \(H_{t,a}=N^{-1/2}(-1)^{t\cdot a}\), where \(t\cdot a\in\mathbb F_2\). Let \(E_S\) be the \(N\times4\) coordinate-selection matrix for the four distinct indices. A sketch has the form \(A=\sqrt{N/m}\,RHD E_S\), where \(D\) is any diagonal matrix of nonzero entries (in particular the conventional independent random signs) and \(R\) chooses \(m\) rows, either independently with replacement or uniformly without replacement as specified. All probabilities refer only to row sampling. The question is \(\operatorname{rank}_{\mathbb R}(A)<4\). The normalization \(\sqrt{N/m}\) and column signs do not affect rank. For \(m<4\) failure is certain.

The motivation is numerical subspace embedding and overdetermined least-squares preprocessing: rank loss destroys injectivity irrespective of conditioning or a multiplicative embedding-distortion tolerance. All four-coordinate supports have the same ambient leverage profile after the Walsh transform, so the difference detects a higher-order geometric feature invisible to coherence-only estimates. The two laws classify every possible set of four distinct coordinates, not just representative examples.

## Proof
**1. Reduction to two projective row designs.** Multiply each four-entry row by its first entry, and multiply columns by fixed signs if needed; none of these operations changes rank. Translate the index set so that its first member is zero. The remaining three differences have \(\mathbb F_2\)-rank either two or three, since the original four indices are distinct. Rank two occurs exactly when \(a_1\oplus a_2\oplus a_3\oplus a_4=0\). A uniformly sampled original row \(t\) yields, with all types equally likely, one of
\[
\mathcal D_0=\{(1,x,y,xy):x,y\in\{\pm1\}\},\qquad
\mathcal D_1=\{(1,x,y,z):x,y,z\in\{\pm1\}\},
\]
respectively. Every design type appears exactly \(N/4\) or \(N/8\) times among the original \(N\) rows. The first design is an invertible order-four Hadamard system, so a sampled matrix has rank four exactly when all four types occur. The second design is the real-affine evaluation matrix of sampled cube vertices.

**2. Exact singular configurations of the cube design.** A real affine plane contains at most four vertices of \(\{\pm1\}^3\): fix a coordinate whose coefficient in the plane equation is nonzero, leaving at most one value for that coordinate among the four assignments of the other two. If four vertices occur, all four assignments must work. With respect to the chosen nonzero coordinate, its two other coefficients cannot both be nonzero: otherwise the four possible values of their affine linear combination comprise at least three distinct numbers, whereas the eliminated coordinate has only two values. Hence the plane is either a coordinate face (six possibilities) or a diagonal plane \(x=\pm y\), \(x=\pm z\), \(y=\pm z\) (six possibilities). Conversely all twelve listed planes contain four cube vertices. Thus **exactly 12 four-subsets are rank-deficient**, every subset of at most three types is rank-deficient, and every five-type subset has rank four. No other bad type sets exist.

**3. Inclusion--exclusion, both sampling schemes.** Let \(u_j(m)\) be the probability that all draws lie in a prescribed \(j\)-element set of the \(v\) equiprobable types. For replacement sampling, \(u_j(m)=(j/v)^m\). Without replacement, when each type has \(N/v\) original rows, \(u_j(m)=\binom{jN/v}{m}/\binom Nm\). Define the probability that exactly a given \(j\)-set of types occurs as
\[
q_j(m)=\sum_{i=0}^{j}(-1)^{j-i}\binom ji u_i(m),\qquad u_0(m)=0\quad(m\ge1).
\]
For \(\mathcal D_0\), only proper type sets cause failure, giving \(P_0=4u_3-6u_2+4u_1\) after inclusion--exclusion. For \(\mathcal D_1\), the bad sets consist of all subsets of size at most three and the twelve coplanar four-subsets. Hence
\[
P_1=\sum_{j=1}^{3}\binom8j q_j+12q_4
=12u_4+8u_3-68u_2+72u_1.
\]
Substituting the corresponding \(v=4\) or \(v=8\) expressions for \(u_i\) proves all four asserted formulas. Note that no independence is required in the without-replacement model; \(u_i\) is a hypergeometric inclusion probability.

**4. Sharp thresholds and asymptotics.** In \(\mathcal D_0\), a deficient sample can contain at most three of the four types, hence at most \(3N/4\) original rows, and this maximum is attained. In \(\mathcal D_1\), every deficient sample uses at most four coplanar types, hence at most \(N/2\) rows, also attained. The two leading replacement terms dominate their smaller-base corrections, proving the positive asymptotics. For \(m=4\), direct substitution gives \(P_0^{\rm rep}=29/32>P_1^{\rm rep}=169/256\). For \(m\ge5\), the formulas yield \(P_0^{\rm rep}\ge4(3/4)^m-6(1/2)^m\) and \(P_1^{\rm rep}\le12(1/2)^m+8(3/8)^m\). The sufficient inequality \(4(3/2)^m>18+8(3/4)^m\) is true at five and strictly strengthens as \(m\) increases. This proves strict dominance for all \(m\ge4\). The stated row-count ratio is \(\log 2/\log(4/3)\), by taking logarithms of the leading failure terms for a common error target approaching zero. The rescaled row-leverage score is the same for both coordinate subspaces because every Walsh entry has modulus \(N^{-1/2}\). This completes the proof.

## Verification
Run `python verify.py` with Python's standard library only. The checker uses exact rational Gaussian elimination and `fractions.Fraction`, enumerates every four-coordinate support at ambient orders \(8\) and \(16\), verifies the two projective design classes, checks all \(12\) coplanar cube quadruples and all five-vertex spans, and independently counts with-replacement configurations by a finite-state occupancy recurrence for lengths \(1\) through \(28\). It enumerates **every** original-row subset at ambient orders \(8\) and \(16\), checking the no-replacement formula at every sample size for both affine types. It separately verifies representative fractions and the strict replacement ordering through sample size \(299\). All checks passed. The arbitrary-dimension and arbitrary-sample-length conclusions follow from the analytic proof above, not from extrapolation of finite checks.

## Relationship to prior work
Balabanov, Beaupère, Grigori and Lederer (2022) define both replacement and no-replacement SRHT row sampling and prove general high-probability oblivious subspace-embedding results, primarily for their block-structured transform; those bounds do not calculate the exact rank-loss law for four coordinate columns. Tropp (2010/2011) and Boutsidis--Gittens (2012/2013) analyze general SRHT subspace preservation and matrix approximation, again without this explicit affine-parity classification. Holodnak--Ipsen (2013/2014) give exact rank conditions and sampling bounds for general Gram matrices; a general full-rank condition does not imply the two exact Walsh-specific failure polynomials without the affine incidence calculation. Classical Walsh character orthogonality, occupancy inclusion--exclusion, and cube faces/diagonals are used as known ingredients rather than claimed as new. The specific joint classification of all four-column supports for both sampling laws, including sharp deterministic row-count thresholds and equal-coherence separation, is the proposed finding. No exhaustive publication-priority assertion is made.

## Limitations
The claim addresses exact rank loss, not spectral distortion conditioned on full rank, floating-point stability, solution error, or methods other than the ordinary Walsh--Hadamard transform. The coordinate subspaces have exactly four dimensions; no higher-dimensional affine-matroid classification is claimed. Replacement sampling permits duplicated rows; without-replacement sampling is restricted to \(m\le N\). The leading replacement asymptotics hold with \(d\) and the four-coordinate support fixed (indeed their probabilities do not depend on \(d\) except for the existence of the affine type). The cited literature comparison is not a proof of priority, and independent validation has not been performed.

## References
1. O. Balabanov, M. Beaupère, L. Grigori, V. Lederer, *Block subsampled randomized Hadamard transform for low-rank approximation on distributed architectures*, arXiv:2210.11295v1, first made public 2022-10-20, https://arxiv.org/abs/2210.11295 .
2. J. A. Tropp, *Improved analysis of the subsampled randomized Hadamard transform*, arXiv:1011.1595, https://arxiv.org/abs/1011.1595 .
3. C. Boutsidis and A. Gittens, *Improved Matrix Algorithms via the Subsampled Randomized Hadamard Transform*, arXiv:1204.0062, https://arxiv.org/abs/1204.0062 .
4. J. T. Holodnak and I. C. F. Ipsen, *Randomized approximation of the Gram matrix: Exact computation and probabilistic bounds*, arXiv:1310.1502, https://arxiv.org/abs/1310.1502 .
5. A. Jung, R. Kueng and D. G. Mixon, *Derandomizing Compressed Sensing With Combinatorial Design*, 2019, https://pmc.ncbi.nlm.nih.gov/articles/PMC6862032/ .
