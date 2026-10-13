# A depth hierarchy for stopping divisors in Carmichael prime wavelet trees
## Finding
Let \(n\) be a Carmichael number. For a divisor \(d\mid n\), put
\[
\lambda(d)=\operatorname{lcm}_{p\mid d}(p-1),
\]
and call \(d\) stopping when \(d\lambda(d)>n\). Let \(d_{\min}(n)\) be the least stopping divisor, and write its distinct prime divisors in decreasing order as
\[
p_1>p_2>\cdots>p_t.
\]
Then, for every integer \(j\) with \(2\le j\le t\),
\[
p_j^{j+1}<n.
\]
Consequently, in the value-ordered prime wavelet tree storing \(d_{\min}(n)\) for Carmichael numbers \(n<B\), every prime label at depth \(j\ge2\) is strictly less than \(B^{1/(j+1)}\).

For the tabulation bound \(B=10^{24}\), this gives the deterministic depth cutoffs
\[
p_2<10^8,\quad p_3<10^6,\quad p_4<63096,\quad p_5<10^4,\quad p_6<2683,\quad p_7<10^3.
\]
The depth-two cutoff is the published cube-root bound; the later cutoffs are the new hierarchy.

## Assumptions and scope
A Carmichael number is composite and satisfies Korselt's criterion: it is squarefree and \(p-1\mid n-1\) for every prime \(p\mid n\). Such an \(n\) is odd: if \(2\mid n\) and an odd prime \(p\mid n\), then the even integer \(p-1\) would have to divide the odd integer \(n-1\), which is impossible. Thus the distinct primes \(p_1,p_2,\ldots\) are all odd.

The conclusion concerns the smallest stopping divisor and the value ordering of its primes. It does not assert the same depth bounds for a different heuristically chosen stopping divisor or for a frequency-ordered tree.

## Proof
Fix \(j\) with \(2\le j\le t\). Because \(p_j\) is a prime divisor of \(d_{\min}(n)\), it divides \(n\). The divisor \(n/p_j\) still contains \(p_1\), so
\[
\lambda(n/p_j)\ge p_1-1.
\]
Since \(p_1>p_j\) are distinct odd primes, \(p_1\ge p_j+2\), hence \(p_1-1>p_j\). Therefore
\[
\frac{n}{p_j}\lambda(n/p_j)>\frac{n}{p_j}p_j=n,
\]
so \(n/p_j\) is itself a stopping divisor. By minimality of \(d_{\min}(n)\),
\[
d_{\min}(n)\le \frac{n}{p_j}.
\]
On the other hand, \(d_{\min}(n)\) is squarefree and contains \(p_1,\ldots,p_j\), so
\[
d_{\min}(n)\ge p_1p_2\cdots p_j>p_j^j.
\]
Combining the last two inequalities gives
\[
p_j^j<\frac{n}{p_j},
\]
and hence \(p_j^{j+1}<n\).

In the value-ordered tree, the depth-\(j\) label on the path for \(n\) is precisely \(p_j\). Thus \(n<B\) implies \(p_j<B^{1/(j+1)}\), proving the corollary.

## Verification
The proof is symbolic and does not depend on finite computation. A standalone exact-integer checker is included as `verify.py`. It independently enumerates all Carmichael numbers through \(2{,}000{,}000\), computes their smallest stopping divisors from the definition, and checks every applicable inequality. The computation is a finite sanity check only; it is not used as evidence for the universal quantifier.

The checker also verifies the stated integer ceilings for \(B=10^{24}\). Its recorded output is included as `verification_output.txt`.

## Relationship to prior work
Gupta, J. Webster, and S. Webster introduce the stopping divisor \(d_{\min}(n)\) and the prime wavelet tree. Their value-ordered encoder uses a prime bitmap below \(B^{1/3}\), justified by proving that only the largest prime of \(d_{\min}(n)\) can exceed \(n^{1/3}\). That is exactly the case \(j=2\) of the theorem above. Their displayed argument and pseudocode do not state the depth-by-depth continuation.

Shallue and Webster's earlier Carmichael-tabulation bounds control primes in the complete ordered factorization of \(n\), for example \(p_{k+1}<(B/P_k)^{1/(d-k)}\). Those bounds depend on the remaining factor count and the partial product of the full factorization. They neither define \(d_{\min}(n)\) nor imply the stopping-divisor inequality \(p_j^{j+1}<n\).

## Limitations
No claim is made that the bounds \(p_j<n^{1/(j+1)}\) are sharp for every depth, or that replacing the single cube-root prime universe by depth-specific universes yields a particular measured compression or decoding-speed improvement. The theorem applies to the value-ordered tree storing the least stopping divisor. It is not asserted for arbitrary heuristic stored divisors or for frequency ordering.

The finite checker tests examples only. The universal result rests on the proof above and on Korselt's criterion plus the definition and minimality of \(d_{\min}(n)\).

## References
1. A. Gupta, J. Webster, S. Webster, *The Prime Wavelet Tree: Compressing the Carmichael Numbers*, arXiv:2610.02550v1, 2026.
2. A. Shallue, J. Webster, *Advances in tabulating Carmichael numbers*, Research in Number Theory 11 (2025), DOI 10.1007/s40993-024-00598-3.
3. MSC2020, 11Y16: Number-theoretic algorithms; complexity.
