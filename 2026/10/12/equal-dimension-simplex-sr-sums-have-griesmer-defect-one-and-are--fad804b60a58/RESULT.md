# Equal-dimension simplex SR-sums have Griesmer defect one and are distance-optimal
## Finding
For every prime power \(q\) and every integer \(k\ge 2\), let \(S_{k,q}\) be the \(q\)-ary simplex code and let \(K(S_{k,q})\) be its length-\(q^k-1\) one-weight expansion used in Kwiatkowski's SR-sum construction. Then \(E_{k,q}=K(S_{k,q})\oplus_{\mathrm{sr}}K(S_{k,q})\) has parameters \([(q^k-1)^2,\,2k,\,(q-1)q^{k-1}(q^k-2)]_q\). Writing \(N=(q^k-1)^2\) and \(d=(q-1)q^{k-1}(q^k-2)\), its dimension-\(2k\) Griesmer sum is exactly \(G_q(2k,d)=N-1\): the equal-dimension SR-sum misses the Griesmer bound by exactly one coordinate. Nevertheless it is distance-optimal among \(q\)-ary linear codes of length \(N\) and dimension \(2k\), because \(G_q(2k,d+1)>N\); more precisely, \(G_q(2k,d+1)-N=k\) when \(q=2\), and it equals \(k-1\) when \(q>2\).

## Assumptions and scope
Let \(q\) be a prime power and \(k\ge 2\). The simplex code \(S_{k,q}\) has parameters \([(q^k-1)/(q-1),k,q^{k-1}]_q\). Following Kwiatkowski, \(K(S_{k,q})\) concatenates the nonzero scalar multiples of simplex columns and is a one-weight code with parameters \([q^k-1,k,q^{k-1}(q-1)]_q\).

Kwiatkowski's Proposition 4.2 gives the two nonzero weights and frequencies of the equal SR-sum. Specializing it to this one-weight code gives
\[
w_1=q^{k-1}(q-1)(q^k-1),\qquad
w_2=(q-1)q^{k-1}(q^k-2),
\]
with frequencies \(2(q^k-1)\) and \((q^k-1)^2\), respectively. Together with the zero word, these frequencies sum to \(q^{2k}\), so the SR-sum has dimension \(2k\). Since \(w_2<w_1\), its minimum distance is \(d=w_2\).

The claim concerns ordinary Hamming distance for linear codes over \(\mathbb F_q\). It does not assert nonlinear optimality, equivalence classification, or a result for \(k=1\).

## Proof
Set
\[
N=(q^k-1)^2,\qquad d=(q-1)q^{k-1}(q^k-2).
\]
For the first \(k\) terms of the Griesmer sum, division is exact:
\[
\sum_{i=0}^{k-1}\frac{d}{q^i}
=q^{2k}-3q^k+2.
\]
For the remaining terms, write \(i=k+j\) with \(0\le j\le k-1\). Then
\[
\left\lceil\frac{d}{q^{k+j}}\right\rceil
=(q-1)q^{k-1-j}
-\left\lfloor\frac{2(q-1)}{q^{j+1}}\right\rfloor.
\]
The floor is \(1\) for \(j=0\) and \(0\) for every \(j\ge1\). Hence the tail contributes
\[
\sum_{j=0}^{k-1}
\left\lceil\frac{d}{q^{k+j}}\right\rceil
=q^k-2.
\]
Therefore
\[
G_q(2k,d)
=q^{2k}-2q^k
=(q^k-1)^2-1
=N-1.
\]

It remains to exclude distance \(d+1\) at the same length and dimension. For every positive integer \(Q\),
\[
\left\lceil\frac{d+1}{Q}\right\rceil-
\left\lceil\frac{d}{Q}\right\rceil
=
\begin{cases}
1,&Q\mid d,\\
0,&Q\nmid d.
\end{cases}
\]
When \(q>2\), the largest power of \(q\) dividing \(d\) is \(q^{k-1}\), so exactly \(k\) summands increase. When \(q=2\), one extra factor of \(2\) occurs because \(2^k-2=2(2^{k-1}-1)\), so exactly \(k+1\) summands increase. Thus
\[
G_q(2k,d+1)=
\begin{cases}
N+k,&q=2,\\
N+k-1,&q>2.
\end{cases}
\]
Because \(k\ge2\), both values exceed \(N\). The Griesmer bound therefore rules out every linear \([N,2k,d+1]_q\) code, proving distance-optimality.

## Verification
The accompanying `verify.py` checks the ceiling identities for \(q\in\{2,3,4,5,7,8,9,11,16,25}\) and \(2\le k\le8\). It also constructs the SR-sum directly for the prime-field cases \((q,k)=(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\), using all nonzero vectors of \(\mathbb F_q^k\) as the columns of \(K(S_{k,q})\). In each case it verifies rank \(2k\), the two predicted weights and frequencies, the exact one-coordinate Griesmer defect, and the strict Griesmer obstruction at distance \(d+1\). The recorded output is `VERIFY_OK`.

These finite calculations are consistency checks; the all-parameter result is supplied by the algebraic ceiling computation above together with the published SR-sum weight formulas.

## Relationship to prior work
Kwiatkowski's Proposition 4.2 supplies the equal-SR-sum weight distribution used here. Theorem 4.4 then proves that \(K(S_{k_1,q})\oplus_{\mathrm{sr}}K(S_{k_2,q})\) meets the Griesmer bound when \(k_1\ne k_2\). Immediately after the proof, the paper observes that equality does not hold when \(k_1=k_2\), but it does not state the exact deficit or determine whether the equal-dimension family is distance-optimal.

The calculation above resolves precisely that omitted boundary: the deficit is always one coordinate, while the next possible minimum distance is already forbidden by the Griesmer bound. Searches for the exact parameter family, the equal-dimension SR-sum, near-Griesmer formulations, and the displayed distance formula did not locate an earlier statement of these two conclusions. The paper cites Helleseth's 1981 classification for binary codes meeting the Griesmer bound; that does not directly imply the present equal-dimension claim because this family does not meet the bound.

## Limitations
The parameter and weight-distribution premises are taken from Kwiatkowski's published Proposition 4.2 and its simplex specialization. The new argument proves the exact Griesmer defect and linear distance-optimality; it does not classify the codes up to equivalence or address nonlinear codes. The full text of Helleseth's 1981 paper was not inspected here, so an older reformulation of the binary subfamily remains a residual literature risk, although its cited scope is Griesmer-equality codes rather than this one-defect family.

## References
1. M. Kwiatkowski, *SR-sum of linear codes*, Advances in Mathematics of Communications 25 (2026), 267–281, DOI: 10.3934/amc.2026052. Published online 2026-06-22.
2. T. Helleseth, *A Characterization of Codes Meeting the Griesmer Bound*, Information and Control 50 (1981), 128–159.
3. J. H. Griesmer, *A bound for error-correcting codes*, IBM Journal of Research and Development 4 (1960), 532–542.
