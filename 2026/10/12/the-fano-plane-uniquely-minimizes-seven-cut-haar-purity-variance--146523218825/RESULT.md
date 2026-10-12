# The Fano plane uniquely minimizes seven-cut Haar purity variance

## Finding

Fix any integer \(p\ge2\). For a Haar-distributed normalized vector \(|\psi\rangle\) on seven labeled \(p\)-level quantum systems, write \(\rho_A=\operatorname{Tr}_{A^c}|\psi\rangle\langle\psi|\). For every set \(\mathcal F\) of **seven distinct** three-element supports \(A\subseteq\{0,1,\ldots,6\}\), set
\[
Q_{\mathcal F}(\psi)=\frac17\sum_{A\in\mathcal F}\operatorname{Tr}(\rho_A^2).
\]

**Theorem.** The global minimizers of \(\operatorname{Var}_{\psi}Q_{\mathcal F}\), over every such \(\mathcal F\), are precisely the images under permutations of the seven sites of
\[
\mathcal F_{\mathrm F}=\{012,034,056,135,146,236,245\}.
\]
Here a three-digit string denotes the corresponding three-element site set. This is the seven-line Fano plane, the Steiner triple system \(2\!-(7,3,1)\). There are exactly 30 distinct labeled minimizers, all equivalent under site permutations.

Set
\[
N=p^7,\quad a=p^3,\quad b=p^4,\quad
R=2N^3+8N^2+(N^2+4N)(a^2+b^2),
\quad T(q)=R+2Na^2p^{-2q}+2b^2p^{2q}.
\]
With \((N)_4=N(N+1)(N+2)(N+3)\), the exact minimum is
\[
\boxed{\operatorname{Var}Q_{\mathrm F}=\frac{T(3)+6T(1)}{7(N)_4}-\left(\frac{a+b}{N+1}\right)^2.}
\]
For the seven cyclic three-consecutive-site blocks \(\mathcal F_{\mathrm{cyc}}\),
\[
\boxed{\operatorname{Var}Q_{\mathrm{cyc}}-\operatorname{Var}Q_{\mathrm F}
=\frac{4p^8(p-1)^2(p+1)^3}{7(N)_4}>0.}
\]
At \(p=2\), the Fano and cyclic variances are respectively \(99/3148847\) and \(5013/110209645\); their ratio (cyclic to Fano) is \(557/385\).

## Assumptions and scope

Exactly seven distinct size-three cuts are selected; each reduction has complementary environment of four parties. A single Haar-random **global pure state** is shared by all cuts in the average. Local dimension \(p\) is an arbitrary integer at least two, and the optimization ranges over all \(\binom{35}{7}\) families of seven different three-site supports. No independence of overlapping subsystem purities is assumed. This is a property of the Haar distribution, not of one chosen state or of finite-shot purity measurement.

## Proof

**Step 1: compute pair moments.** For two three-site supports \(A,B\), let \(q=|A\cap B|\in\{0,1,2,3\}\). The four-replica Haar identity gives
\[
\mathbb E\bigl[(\operatorname{Tr}\rho_A^2)(\operatorname{Tr}\rho_B^2)\bigr]
=\frac{T(q)}{(N)_4},\qquad
\mathbb E\operatorname{Tr}\rho_A^2=\mu=\frac{a+b}{N+1}.
\]
The first identity follows directly from \(\mathbb E(|\psi\rangle\langle\psi|)^{\otimes4}=(N)_4^{-1}\sum_{\sigma\in S_4}U_\sigma\). Let \(\tau_{01}=(01)\), \(\tau_{23}=(23)\), and let \(c(\sigma)\) count cycles of \(\sigma\in S_4\). At the \(q\) sites in \(A\cap B\), the trace factor is \(p^{c(\sigma\tau_{01}\tau_{23})}\); at each of the \(3-q\) sites of \(A\setminus B\) it is \(p^{c(\sigma\tau_{01})}\); at each of the \(3-q\) sites of \(B\setminus A\) it is \(p^{c(\sigma\tau_{23})}\); and at the remaining \(1+q\) sites it is \(p^{c(\sigma)}\). Thus
\[
T(q)=\sum_{\sigma\in S_4}p^{q c(\sigma\tau_{01}\tau_{23})+(3-q)c(\sigma\tau_{01})+(3-q)c(\sigma\tau_{23})+(1+q)c(\sigma)}.
\]
Grouping the 24 permutations produces the displayed closed form \(R+2Na^2p^{-2q}+2b^2p^{2q}\). The single-cut mean follows from the two-replica identity.

**Step 2: prove that one-site intersection is optimal.** Distinct size-three supports have overlap \(q\in\{0,1,2\}\). Direct subtraction gives
\[
T(0)-T(1)=2p^8(p-1)^2(p+1)(p^2+p+1)>0,
\]
\[
T(2)-T(1)=2p^9(p-1)^2(p+1)>0.
\]
Since the diagonal contribution \(T(3)\) and the squared common mean \(\mu^2\) are fixed, each of the 21 unordered distinct-support pairs contributes its smallest possible covariance precisely when it has intersection size one. The explicit family \(\mathcal F_{\mathrm F}\) has this property for every pair, so the resulting lower bound is attained; no family with an intersection of size zero or two can attain it. Summing seven diagonal and 42 ordered off-diagonal terms yields the stated exact minimum.

**Step 3: uniqueness of incidence type.** If every two of seven three-element blocks meet in exactly one point, no site-pair occurs in more than one block. There are seven blocks with three site-pairs each, namely 21 incidences with unordered pairs of points. There are exactly \(\binom72=21\) possible site-pairs, so each occurs exactly once. The blocks therefore form a \(2\!-(7,3,1)\) Steiner system. Its uniqueness can be checked constructively: each point lies in three blocks; name one point \(0\) and permute the remaining sites so its three blocks are \(012\), \(034\), and \(056\). The incidence condition forces the other four blocks, up to swapping points within these three pairs and permuting the pairs, to be \(135\), \(146\), \(236\), \(245\). Hence every optimizer is isomorphic to \(\mathcal F_{\mathrm F}\). An exact finite enumeration in `verify.py` confirms 30 labeled systems; the uniqueness does not rely on numerical exploration.

**Step 4: compare the cyclic family.** The seven cyclic length-three intervals have exactly seven unordered pairs for each overlap size \(0\), \(1\), and \(2\). The Fano family has 21 unordered pairs of overlap size one. Subtracting their pair-moment sums gives
\[
\frac{2[T(0)+T(2)-2T(1)]}{7(N)_4}
=\frac{4p^8(p-1)^2(p+1)^3}{7(N)_4},
\]
strictly positive for every integer \(p\ge2\). Exact substitution at \(p=2\) gives the stated rational values and ratio.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library, alongside this document. The script enumerates all 24 permutations of four replicas independently of the closed form; checks the equality of that trace and \(T(q)\) for every \(q\in\{0,1,2,3\}\) and \(p\in\{2,3,4,5\}\); recomputes exact rational Fano/cyclic variances; checks their symbolic-gap specialization; and enumerates all labeled seven-block pairwise-one systems. It reports exactly 30 such labeled systems and terminates with `VERIFY_OK`. These finite checks test algebra and incidence, but the general-\(p\) theorem and global minimization are proved above.

## Relationship to prior work

Mirsohi [1] derives the general two-support Haar covariance kernel by the four-replica method and explicitly raises inverse questions about which prescribed equal-size subsystem families minimize variance (§VI.C). The source studies cyclic intervals and does not give the present all-family optimizer for seven triple cuts. Here the existing kernel is used, with an independent 24-permutation derivation, to solve a specific first nontrivial incidence-design instance by a strict pairwise inequality and a finite Steiner-system rigidity argument. Neither the covariance kernel nor the Fano plane itself is asserted to be new. Facchi et al. [2] analyze averaged multipartite purity over balanced cuts rather than selecting seven supports optimally. Wang [3] studies existence of planar uniform states, not Haar variance minimization of arbitrary cut families.

## Limitations

The optimality is for seven **distinct** supports, each of cardinality three, on precisely seven parties, for Haar-random pure states. Repeated cuts, other support counts, unequal support sizes, correlated non-Haar ensembles, and measurement noise require separate analysis. The argument does not imply a new absolutely maximally entangled state or any universal state-preparation advantage. The covariance kernel and Steiner-system combinatorics are established; originality rests on this particular exact global cut-family optimization, whose possible earlier equivalent formulation remains a priority risk. The result is not independently audited.

## References

[1] K. Mirsohi, *Exact Haar Statistics of Planar \(k\)-Purity in Multipartite Quantum Systems*, arXiv:2608.28914v1 (first public 2026-08-28), especially §§III and VI.C; https://arxiv.org/abs/2608.28914 .

[2] *Multipartite Entanglement and Frustration*, arXiv:0910.3134; https://arxiv.org/abs/0910.3134 .

[3] *Planar \(k\)-uniform states*, arXiv:2106.12209; https://arxiv.org/abs/2106.12209 .
