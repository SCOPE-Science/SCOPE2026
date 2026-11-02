# A spectrally invisible output swap gives the exact transient law on every even Rule-90 ring

## Finding

Let \(n\ge4\) be even, let \(d=2^{\nu_2(n)}\) be the largest power of two dividing \(n\), and let \(S\) denote the one-site cyclic shift on \(\mathbb F_2^n\). Write \(R=S+S^{-1}\) for the synchronous Rule-90 update, and let \(Q\) exchange output coordinates 1 and 2 while leaving the other coordinates fixed. Set \(A=QR\), the partial-shift permutation XOR cellular automaton with shift-part parameter \(r=2\).

For a linear map \(F\) of this finite state space, define its *preperiod* \(\tau_F(v)\) to be the least nonnegative integer \(t\) for which \(F^t(v)\) is periodic. Then \(A\) and \(R\) have **identical characteristic polynomials** over \(\mathbb F_2\), but different exact preperiod distributions whenever \(4\mid n\):

\[
\begin{aligned}
\#\{v:\tau_A(v)=0\}&=2^{n-d},\\
\#\{v:\tau_A(v)=1\}&=3\,2^{n-d},\\
\#\{v:\tau_A(v)=t\}&=2^{n-d+t}\quad(2\le t\le d-1),
\end{aligned}
\]

with zero counts at every other nonnegative time. For the unpermuted Rule-90 map,

\[
\#\{v:\tau_R(v)=0\}=2^{n-d},\qquad
\#\{v:\tau_R(v)=t\}=3\,4^{t-1}2^{n-d}\quad(1\le t\le d/2),
\]

and all other counts vanish. In particular,

\[
\max_v\tau_A(v)=d-1,\qquad \max_v\tau_R(v)=d/2.
\]

For uniformly distributed initial binary configurations the exact mean preperiods are

\[
\mathbb E\tau_A=d-2+\frac{3}{2^d},\qquad
\mathbb E\tau_R=\frac d2-\frac13+\frac{1}{3\,2^d}.
\]

If \(n\) is a power of two, all configurations eventually reach zero; nevertheless swapping just the first two outputs raises the worst-case erasure time from \(n/2\) to \(n-1\), without changing the characteristic polynomial \(x^n\).

## Assumptions and scope

The alphabet is exactly \(\mathbb F_2\), the ring uses cyclic boundary conditions, and all sites update synchronously. The shift-part parameter is exactly \(r=2\), so the permutation exchanges the first two outputs of Rule 90 *after every update*. The statement applies to every even \(n\ge4\), including even lengths that are not powers of two. The preperiod is the entry time into any cycle, not the cycle length. Counts are for all \(2^n\) labelled initial states.

## Proof

**1. A characteristic-polynomial invariance lemma.** Let \(E\) be any symmetric, zero-diagonal matrix over \(\mathbb F_2\) such that \(E\mathbf1=0\), and let \(Q\) exchange coordinates \(i\ne j\). Put \(v=e_i+e_j\), so \(Q=I+vv^{\mathsf T}\). For every integer \(k\ge0\),

\[
v^{\mathsf T}E^kv=0.
\]

For \(k=0\) this is \(v^{\mathsf T}v=0\). For odd \(k=2h+1\) it equals \((E^hv)^{\mathsf T}E(E^hv)=0\), since every symmetric zero-diagonal binary matrix has vanishing quadratic form. For positive even \(k=2h\) it equals \((E^hv)^{\mathsf T}(E^hv)=\mathbf1^{\mathsf T}E^hv=0\). Consequently, expanding the resolvent in the formal Laurent series field \(\mathbb F_2((x^{-1}))\) gives

\[
 v^{\mathsf T}E(xI-E)^{-1}v=0.
\]

The rank-one determinant identity applied to \(QE=E+v(v^{\mathsf T}E)\) therefore yields \(\det(xI-QE)=\det(xI-E)\). The cycle adjacency matrix \(R\) meets these assumptions (every vertex has degree two), proving \(\chi_A=\chi_R\). Notice this lemma concerns a **permutation of update outputs**, not a similarity relabelling of input and output coordinates.

**2. The zero-primary sector of \(R\).** Write \(n=dm\), where \(m\) is odd and \(d\) is a power of two. Regard the cyclic shift as multiplication by \(z\) in

\[
\mathbb F_2[z]/(z^n-1),\qquad z^n-1=(z^m-1)^d.
\]

The factor \(z+1\) occurs with multiplicity precisely \(d\), because \(m\) is odd. As \(R=z^{-1}(z+1)^2\), its generalized zero eigenspace has dimension \(d\). On the local factor \(\mathbb F_2[z]/((z+1)^d)\), each power \(R^t\) has rank \(\max\{d-2t,0\}\); on the complementary factor \(R\) is invertible. Thus the zero Jordan blocks of \(R\) have sizes \(d/2,d/2\), and the total rank is \(n-\min\{d,2t\}\) at step \(t\).

**3. The zero-primary sector of \(A\).** As \(Q\) is invertible, \(\ker A=\ker R\), which has dimension two: the solutions of \(u_{i-1}+u_{i+1}=0\) are the two-periodic strings, constant \(a\) on odd sites and \(b\) on even sites. Since \(R\) is symmetric,

\[
\operatorname{im}R=\{u:\text{the sums of odd-site and even-site entries of }u\text{ are both zero}\}.
\]

For \(u\in\ker A\), membership in \(\operatorname{im}A=Q\operatorname{im}R\) is equivalent to \(Qu\in\operatorname{im}R\). Writing \(m_0=n/2\), the odd-site and even-site sums of \(Qu\) are respectively \((m_0-1)a+b\) and \((m_0-1)b+a\) in \(\mathbb F_2\). If \(4\mid n\), both vanish exactly when \(a=b\), so \(\dim(\operatorname{im}A\cap\ker A)=1\). Otherwise both vanish only for \(a=b=0\), so this intersection has dimension zero. The identity

\[
\dim\ker A^2-\dim\ker A=\dim(\operatorname{im}A\cap\ker A)
\]

now determines the zero Jordan blocks. The characteristic-polynomial invariance fixes the total algebraic zero multiplicity at \(d\); there are exactly two zero Jordan blocks because \(\dim\ker A=2\). When \(d\ge4\), the second nullity is three, forcing one block of size one and the other of size \(d-1\). When \(d=2\), both blocks necessarily have size one. Thus in every even length the zero Jordan sizes of \(A\) are precisely \(d-1,1\), and

\[
\operatorname{rank}(A^t)=n-\min\{d,t+1\}\quad(t\ge1).
\]

**4. Preperiod counts.** For any linear map on a finite vector space, its Fitting decomposition is the direct sum of a nilpotent zero-primary component and an invertible component. Every point in the invertible component is periodic. Hence the preperiod of an arbitrary state is exactly the first time its nilpotent component is killed. The invertible component has dimension \(n-d\) for both maps. For \(A\), the nilpotent kernel sizes are \(1\) at time zero and \(2^{\min\{d,t+1\}}\) at every integer \(t\ge1\). Taking successive differences and multiplying by \(2^{n-d}\) yields the claimed distribution. For \(R\), replace these kernel sizes with \(2^{\min\{d,2t\}}\). Summing the resulting time-weighted counts gives the stated exact means. For \(n=d\), the invertible sector has dimension zero, proving extinction of every configuration and the exact two worst-case times.

## Verification

The self-contained Python 3 program `verify.py` implements the XOR update and the two-output swap directly, finite-field row reduction, exact matrix powers, and (for smaller lengths) exhaustive functional-graph preperiod enumeration. It was run successfully for even lengths \(4,6,\ldots,24,28,30,32,36,40,48,64,96,128\). It exhaustively enumerates every initial configuration for \(n=4,6,8,10,12,16\), and checks every asserted rank through the stabilization point at all tested lengths. The output ends with `VERIFY_OK`. These finite checks are consistency tests; the proof above establishes the result for all even lengths.

## Relationship to prior work

Suzuki, Okuyama, Takahashi and Saito [1] define this precise permutation-XOR family and its transition matrix, concentrating on odd dimensions and long periodic orbits; their Section 3.2 explicitly sets aside even dimensions. The result here answers a different, natural question: the complete transient-entry census for the even-dimensional \(r=2\) family. Earlier work on standard Rule 90 [2] supplies established periodic-ring arithmetic and is not claimed as new. Li, Wang and Zhang [3] prove strong annihilator bounds for **symmetric** binary adjacency matrices of Eulerian graphs. Their theorem applies to \(R\) but not to the nonsymmetric output-permuted matrix \(A\); indeed the latter has a zero Jordan block of size \(d-1>d/2\) whenever \(d\ge4\). The spectral invariance lemma and the altered Jordan structure explain why unchanged eigenvalues do not imply unchanged finite-state transients. The present search did not establish an earlier all-even \(r=2\) preperiod formula; that is not a proof of worldwide priority.

## Limitations

The theorem does not enumerate primitive periods on the nonzero invertible sector when \(n\) is not a power of two. It does not characterize general partial-shift parameters \(r>2\), nonlinear XOR variants, noise, or asynchronous updates. An earlier 2025 permutation-XOR article [4] was identifiable, but full text was inaccessible; its reported focus on full-shift permutations does not establish or refute this exact two-output-swap claim. Independent scientific validation has not been performed.

## References

1. Y. Suzuki, N. Okuyama, H. Takahashi, T. Saito, *Permutation XOR cellular automata: partial-shift connections and half-primitive polynomials*, arXiv:2609.34542v1, first posted 2026-09-28. https://arxiv.org/abs/2609.34542
2. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics 93 (1984), 219–258. https://doi.org/10.1007/BF01223745
3. K. Li, W. Wang, H. Zhang, *Annihilating polynomial, Jordan canonical form, and generalized spectral characterizations of Eulerian graphs*, arXiv:2410.09833v1, 2024-10-13. https://arxiv.org/abs/2410.09833
4. M. Onuki, Y. Suzuki, T. Saito, *Permutation XOR cellular automata and direct stable periodic orbits*, Neurocomputing 656 (2025), 131510. https://doi.org/10.1016/j.neucom.2025.131510
