# Exact ternary minimal-absent-subsequence spectrum of repeated permutation words

## Finding

Let \(\Sigma_q=\{0,1,\ldots,q-1\}\) be ordered, let \(P_q=01\cdots(q-1)\), and let \(W_{q,m}=P_q^m\), for integers \(q\ge 3\) and \(m\ge1\). A minimal absent subsequence (MAS) is a nonempty word that does not occur as a scattered subsequence of \(W_{q,m}\), although all words obtained by deleting one letter do occur.

For a nonempty word \(u=u_1\cdots u_\ell\), put
\[
 d(u)=\sum_{i=1}^{\ell-1}\mathbf 1_{\{u_i\ge u_{i+1}\}}.
\]
The complete MAS set is characterized by these three tests: \(d(u)=m\); the first and last adjacent pairs are weak descents; and every consecutive triple \((a,b,c)\) satisfies
\[
 \mathbf 1_{\{a\ge b\}}+\mathbf 1_{\{b\ge c\}}-\mathbf 1_{\{a\ge c\}}=1.
\]
Thus every MAS has length between \(m+1\) and \(2m\). The characterization yields, for every \(q\ge3\), a finite \(q^2\)-state transfer formula for the exact bivariate length spectrum.

For the first nonbinary case \(q=3\), let \(c_{m,\ell}\) denote the number of distinct ternary MAS of length \(\ell\) for \(W_{3,m}=(012)^m\). Then
\[
 F(t,z)=\sum_{m\ge1}\sum_{\ell\ge1}c_{m,\ell}t^m z^\ell=\frac{N(t,z)}{D(t,z)},
\]
where
\[
\begin{aligned}
N(t,z)=tz^2(&6-8tz+6tz^2+3t^2z^2+6t^2z^3+t^2z^4\\
&-9t^3z^4+6t^3z^5+9t^4z^6-t^4z^7-3t^5z^8),
\end{aligned}
\]
and
\[
\begin{aligned}
D(t,z)={}&1-3tz+3t^2z^2-t^2z^3-t^3z^3-3t^3z^4\\
&+3t^4z^5-t^4z^6-3t^5z^7+t^6z^9.
\end{aligned}
\]
In particular the exact total MAS counts \(A_m=\sum_\ell c_{m,\ell}\) satisfy
\[
 \sum_{m\ge1}A_m t^m=\frac{t(6-2t+10t^2-3t^3+8t^4-3t^5)}{1-3t+2t^2-4t^3+2t^4-3t^5+t^6}.
\]
The first eight values are \(6,16,46,127,349,960,2640,7264\). The shortest layer has the already-known count \(c_{m,m+1}=\binom{m+3}{2}\); the result here resolves every longer minimal-absent layer as well.

## Assumptions and scope

All host words are full powers of the same increasing permutation on a fixed ordered alphabet. Only scattered subsequence absence is considered, **not** absent contiguous factors. Minimality means deletion of **any one** target letter restores subsequence occurrence. Counting is by distinct target strings rather than embeddings or index subsets. All displayed rational functions are formal power series around \((t,z)=(0,0)\), with constant denominator coefficient one. Alphabet relabeling by a common permutation preserves the counts.

## Proof

**Greedy embedding.** For any nonempty target \(u\), greedily match its first letter in the first copy of \(P_q\). From a matched letter \(a\), the next target letter \(b\) fits later in the same copy exactly when \(a<b\); otherwise it must use the next copy. This greedy choice is optimal. Therefore \(u\) occurs in \(P_q^m\) if and only if \(d(u)\le m-1\).

**Deletion-local minimality.** Removing the first or last target letter decreases \(d\) by zero or one. Removing an internal letter \(b\) from a consecutive triple \((a,b,c)\) decreases \(d\) by
\[
 \Delta(a,b,c)=\mathbf1_{\{a\ge b\}}+\mathbf1_{\{b\ge c\}}-\mathbf1_{\{a\ge c\}}.
\]
For a total order, \(\Delta\) is zero or one: with two weak descents, transitivity gives \(\Delta=1\); with two strict ascents it is zero; and with one of each it is one precisely when \(a<c\). A target is absent iff \(d(u)\ge m\); every one-letter deletion is present iff every deletion lowers \(d\) below \(m\). Since deleting an endpoint lowers \(d\) by at most one, this is equivalent to \(d(u)=m\) and decrement one at every deletion. The endpoint and triple tests above are exactly those conditions. They also imply that strict ascent edges cannot be adjacent or endpoints; hence, with \(m\) weak descents, there are at most \(m-1\) ascents and \(m+1\le |u|\le2m\).

**General transfer.** Index rows and columns by the ordered pairs \(S_q=\Sigma_q^2\). Set
\[
 M_{(a,b),(b,c)}(t,z)=
 \begin{cases}zt^{\mathbf1_{\{b\ge c\}}},&\Delta(a,b,c)=1,\\0,&\text{otherwise},\end{cases}
\]
and all entries with incompatible pair overlap to zero. Define \(v_{(a,b)}=tz^2\mathbf1_{\{a\ge b\}}\) and \(w_{(a,b)}=\mathbf1_{\{a\ge b\}}\). Every admissible target has a unique path of consecutive adjacent pairs; its first pair contributes \(v\), each new letter contributes the prescribed edge weight, and its last pair contributes \(w\). The exponent of \(t\) is its total weak-descent count and the exponent of \(z\) is its length. Therefore the exact series for every \(q\ge3\) is
\[
 F_q(t,z)=v(I-M)^{-1}w.
\]
Since every entry of \(M\) is divisible by \(z\), the inverse exists in the formal-series ring.

**Exact ternary evaluation.** For \(q=3\), order the nine states lexicographically. Direct rational elimination gives the displayed \(N/D\). An explicit polynomial certificate is supplied: it lists \(D\), \(N\) and a nine-component polynomial vector \(p\) and checks the exact identities \((I-M)p=Dw\) and \(vp=N\) in \(\mathbb Z[t,z]\). Because \(D(0,0)=1\), the first identity implies \((I-M)^{-1}w=p/D\), and the second implies \(F_3=N/D\). This checks the infinite formal identity rather than merely a finite coefficient prefix. Setting \(z=1\) gives the total-count formula. The shortest layer follows from the necessary and sufficient condition that all \(m\) edges are weak descents, so its targets are the weakly decreasing \((m+1)\)-tuples, counted by \(\binom{m+3}{2}\).

## Verification

The standalone script `verify_ternary_periodic_mas.py` reads `ternary_mas_algebra_certificate.json` and verifies the exact nine-vector polynomial identities using integer polynomial arithmetic, without third-party dependencies. It also compares the transfer-matrix count against direct literal subsequence tests on 143,310 candidate target words in 12 independently enumerated host cases (binary repetitions one through seven, and ternary repetitions one through five). The direct checks identified 740 minimal absent targets, and a separate exact coefficient identity comparison tested 1,035 bivariate coefficients through repetition index 22. Recorded output:

`VERIFY_OK direct_parameter_cases=12 literal_targets=143310 tested_MAS=740 rational_coefficients=1035 ternary_prefix=6,16,46,127,349,960,2640,7264`

`ALGEBRA_CERT_OK states=9 polynomial_terms=47`

The infinite mathematical proof is the greedy-deletion characterization plus formal transfer and polynomial identities; finite enumerations are consistency checks and do not replace it.

## Relationship to prior work

Kosche, Koß, Manea and Siemer (arXiv:2108.13968, first posted 31 August 2021), particularly Theorem 3.1 and Proposition 3.6, characterize minimal absent subsequences of general words and study \(B_k=(12\cdots\sigma)^k\), deriving polynomial shortest-absent counts and exponential lower bounds for minimal-absent counts with \(\sigma\ge4\). Their examined treatment does not present this complete ternary length distribution or the rational function above. Adamson et al. (arXiv:2407.18599, first posted 26 July 2024) count all **absent** subsequences at fixed lengths under universality constraints, a different statistic from this **minimal absent** antichain. Manea et al. (arXiv:2504.21471, first posted 30 April 2025) develop generic enumeration algorithms rather than a closed ternary periodic-word spectrum. A binary \((01)^m\) length-spectrum identity is previously known; this result does not claim it anew. The ternary spectrum is not implied by replacing the binary alphabet in the earlier binary formula.

## Limitations

The explicit numerator and denominator are specialized to ternary ordered permutations; larger alphabet sizes are covered by the exact finite-matrix expression, not a uniform low-degree rational fraction. The first-public date belongs to the guiding 2021 paper, not to this derived theorem. Existing generic MAS enumeration methods can in principle produce finite coefficients but do not by themselves yield the all-parameter closed form. A relevant 2023 paper by Tronícek on absent-subsequence automata was identified, but its full text was inaccessible during comparison; any undiscovered exact equivalent specialization there remains an originality risk. No independent mathematical audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (v1 dated 2021-08-31), Fundamenta Informaticae 189 (2023), 199–240. https://arxiv.org/abs/2108.13968
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (v1 dated 2024-07-26). https://arxiv.org/abs/2407.18599
3. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (v1 dated 2025-04-30). https://arxiv.org/abs/2504.21471
4. Z. Tronícek, *On Problems Related to Absent Subsequences*, COCOA 2023, LNCS 14462, 351–363, DOI:10.1007/978-3-031-49614-1_26 (material not accessed).
