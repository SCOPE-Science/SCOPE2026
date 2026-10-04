# Exact syndrome sizes for ternary parity-lifted two-burst covering codes
## Finding
Let \(p\ge 3\) be an odd prime. For a binary word \(b=(b_1,\ldots,b_p)\), define its differential vector by \(\operatorname{Diff}(b)_i=b_{i+1}-b_i\pmod 2\) for \(1\le i<p\) and \(\operatorname{Diff}(b)_p=b_p\), and define the differential VT syndrome
\[
\sigma(b)=\sum_{i=1}^p i\,\operatorname{Diff}(b)_i\pmod{2p}.
\]
For \(a\in\{0,1,\ldots,2p-1\}\), let
\[
C_a(p)=\{x\in\{0,1,2\}^p:\sigma(x\bmod 2)=a\}.
\]
The nonbinary two-burst construction of Xie--Sun--Ge specializes at alphabet size three to these classes because its two auxiliary checksum moduli are \(\lfloor 3/2\rfloor=1\). Hence every \(C_a(p)\) is a ternary code whose length-\(p-2\) outputs under deletion of two consecutive symbols cover all of \(\{0,1,2\}^{p-2}\).

Their exact cardinalities are
\[
|C_a(p)|=
\begin{cases}
\dfrac{3^p+(p-1)2^{p+1}+1}{2p},&a=0,\\[4pt]
\dfrac{3^p+2p-3}{2p},&a=p,\\[4pt]
\dfrac{3^p-2^{p+1}+1}{2p},&a\ne0,p\text{ and }a\text{ is even},\\[4pt]
\dfrac{3^p-3}{2p},&a\ne p\text{ and }a\text{ is odd}.
\end{cases}
\]
Consequently, the \(p-1\) nonzero even syndromes are exactly the smallest classes, each of size
\[
\frac{3^p-2^{p+1}+1}{2p}.
\]
This gives an explicit strengthening, for every odd prime length, of the generic averaging bound \(|C_a(p)|\le 3^p/(2p)\) for this ternary specialization.

## Assumptions and scope
A two-burst deletion means deletion of exactly two consecutive coordinates. The result concerns the explicit parity-lift family \(C_a(p)\), not the globally smallest ternary two-burst-deletion covering code. Primality is used only to ensure that every nonconstant binary cyclic-rotation orbit has size \(p\); the statement as written does not claim an extension to composite lengths.

The source construction is Theorem VI.4 of Xie--Sun--Ge, arXiv:2606.15379v1. Its first public version is dated 2026-06-13 and its primary arXiv classification is Information Theory. The present result computes the exact cardinality distribution of its ternary specialization at odd prime lengths.

## Proof
A binary parity pattern \(b\in\{0,1\}^p\) has exactly \(2^{p-\operatorname{wt}(b)}\) ternary lifts: a zero coordinate of \(b\) may be lifted to either \(0\) or \(2\), whereas a one coordinate must lift to \(1\). Thus \(|C_a(p)|\) is a weighted syndrome count.

First, the syndrome parity records Hamming-weight parity:
\[
\sigma(b)\equiv \operatorname{wt}(b)\pmod 2.
\]
Indeed, modulo two, only the odd indices in \(\sum i\operatorname{Diff}(b)_i\) remain; after expanding the adjacent differences, every coordinate of \(b\) occurs exactly once because \(p\) is odd.

Next let \(R(b)=(b_p,b_1,\ldots,b_{p-1})\) be cyclic right rotation, and let \(\tau(b)\) be the number of transitions around the cyclic binary word. A direct index shift gives
\[
\sigma(Rb)-\sigma(b)\equiv \tau(b)\pmod p.
\]
For a nonconstant binary word, \(\tau(b)\) is a positive even integer smaller than \(p\). Since \(p\) is prime, every nonconstant rotation orbit has size \(p\), and the fixed nonzero increment \(\tau(b)\pmod p\) makes the syndromes modulo \(p\) run once through every residue on that orbit. Both \(2^{p-\operatorname{wt}(b)}\) and its signed version \((-1)^{\operatorname{wt}(b)}2^{p-\operatorname{wt}(b)}\) are rotation invariant.

Define
\[
T_r=\sum_{\sigma(b)\equiv r\ (\mathrm{mod}\ p)}2^{p-\operatorname{wt}(b)}.
\]
All nonconstant rotation orbits contribute equally to the \(p\) values of \(r\). The two constant words occur only at \(r=0\), with weights \(2^p\) and \(1\). Since
\[
\sum_b2^{p-\operatorname{wt}(b)}=3^p,
\]
we obtain, for \(r\ne0\),
\[
T_r=\frac{3^p-2^p-1}{p},
\]
and
\[
T_0=\frac{3^p-2^p-1}{p}+2^p+1.
\]

Similarly put
\[
D_r=\sum_{\sigma(b)\equiv r\ (\mathrm{mod}\ p)}(-1)^{\operatorname{wt}(b)}2^{p-\operatorname{wt}(b)}.
\]
The constant words contribute \(2^p-1\) at \(r=0\), while
\[
\sum_b(-1)^{\operatorname{wt}(b)}2^{p-\operatorname{wt}(b)}=(2-1)^p=1.
\]
Therefore, for \(r\ne0\),
\[
D_r=\frac{2-2^p}{p},
\]
and
\[
D_0=\frac{2-2^p}{p}+2^p-1.
\]

The two residues modulo \(2p\) above a fixed residue \(r\pmod p\) differ by \(p\), so because \(p\) is odd they have opposite parity. By the syndrome-parity identity, the even lift contains exactly the even-weight binary patterns and the odd lift contains exactly the odd-weight patterns. Hence its weighted size is respectively \((T_r+D_r)/2\) or \((T_r-D_r)/2\). Substitution gives the four displayed formulas. Comparing them shows that the nonzero even syndromes are precisely the minima.

## Verification
The accompanying `verify.py` independently enumerates every binary parity pattern for \(p\in\{3,5,7,11\}\), checks both the parity lemma and the cyclic-rotation increment identity, and verifies the exact class-size formulas. For \(p\in\{3,5,7\}\), it also enumerates all ternary words and checks directly that every one of the \(2p\) classes covers every length-\(p-2\) ternary word under deletion of two consecutive coordinates. The program terminates with `VERIFY_OK`.

## Relationship to prior work
Xie--Sun--Ge prove that their nonbinary parity-and-checksum classes are two-burst-deletion covering codes and obtain existence of a parameter choice of size at most \(q^n/(2n\lfloor q/2\rfloor^2)\). At \(q=3\), the checksum conditions are vacuous, leaving exactly the parity-lifted binary differential-VT classes above; the source does not state their prime-length exact size distribution. Babu--Krishnamoorthy--Roth--Siegel determine exact sizes of the \(q\)-ary differential VT codes themselves, a different family in which the syndrome is taken directly over the \(q\)-ary differential word rather than after the ternary-to-binary parity map. Lenz--Rashtchian--Siegel--Yaakobi give general insertion/deletion covering bounds but do not imply this weighted syndrome distribution.

Targeted searches for the exact formula, the ternary parity-lift formulation, and equivalent differential-VT terminology did not locate a prior statement of this distribution. This is evidence against overlap, not a proof of global novelty.

## Limitations
The theorem determines sizes only inside this explicit construction and does not establish the global ternary covering number. The prime-length hypothesis is essential to the rotation-orbit proof supplied here; composite lengths may have nonconstant short rotation orbits and require a separate analysis. The covering property for all prime lengths is inherited from the cited construction theorem, while the independent exhaustive covering checks are finite anchors at \(p=3,5,7\).

## References
1. Chengfei Xie, Yubo Sun, Gennian Ge, “New bounds for covering codes under insertions or deletions,” arXiv:2606.15379v1, 2026.
2. Nithish Suresh Babu, Adi Krishnamoorthy, Ron M. Roth, Paul H. Siegel, “On Differential Varshamov–Tenengolts Codes,” IEEE ISIT 2025.
3. Andreas Lenz, Cyrus Rashtchian, Paul H. Siegel, Eitan Yaakobi, “Covering Codes Using Insertions or Deletions,” IEEE Transactions on Information Theory 67 (2021), 3376–3388; arXiv:1911.09944.
