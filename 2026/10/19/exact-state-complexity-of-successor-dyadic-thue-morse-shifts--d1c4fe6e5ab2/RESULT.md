# Exact state complexity of successor-dyadic Thue–Morse shifts

## Finding

Let \(t(n)\) be the parity of the number of ones in the binary expansion of a nonnegative integer. For a positive integer shift \(c\), write \(N(c)\) for the number of states in the smallest complete deterministic finite automaton with output (DFAO) that returns \(t([w]_2+c)\) on every finite binary word \(w\), read most-significant digit first. Leading zeros and the empty word are allowed.

For every integer \(k\ge1\), with \(F_0=0,F_1=1\) and \(F_{m+2}=F_{m+1}+F_m\),
\[
\boxed{N(2^k+1)=2F_{k+4}=N(2^{k+1}).}
\]
The first values for \(k=1,\ldots,8\) are \(10,16,26,42,68,110,178,288\).

## Assumptions and scope

For a finite binary word \(w\), \([w]_2\) denotes its numerical value, with \([\varepsilon]_2=0\). The output alphabet is Boolean. The shift family in the finding is exactly \(2^k+1\), \(k\ge1\). The argument uses an auxiliary equality for general shifts and the known pure-dyadic formula but does not give a closed formula for general shifts.

For \(c\ge1\), define the finite carry-offset set
\[
I_c=\{c\}\cup\left\{\left\lfloor\frac{c}{2^\ell}\right\rfloor,\left\lceil\frac{c}{2^\ell}\right\rceil:\ell\ge1\right\}.
\]
For a prefix of value \(n\), its fingerprint is \(\Phi_c(n)=(t(n+j))_{j\in I_c}\), with indices in increasing order.

## Proof

**1. Residual characterization.** After a prefix of value \(n\), a suffix of length \(\ell\ge1\) and value \(u\in\{0,\ldots,2^\ell-1\}\) gives output \(t(2^\ell n+u+c)\). Write \(c=2^\ell q+r\) with \(0\le r<2^\ell\). Separating the high and low digits gives
\[
t(2^\ell n+u+c)=t\!\left(n+q+\left\lfloor\frac{u+r}{2^\ell}\right\rfloor\right)\oplus t((u+r)\bmod 2^\ell),
\]
where \(\oplus\) denotes addition modulo two. The high-digit term has offset \(q\) or, when \(r>0\), \(q+1\). Both available high-digit bits can be recovered from individual suffix outputs by XOR with the known low-digit parity: take \(u=0\) for \(q\) and \(u=2^\ell-r\) for \(q+1\) when \(r>0\). The empty suffix gives \(t(n+c)\). Thus two prefix values agree on all continuations if and only if their fingerprints agree. All prefix values \(n\ge0\) are reachable, so
\[
N(c)=\#\{\Phi_c(n):n\ge0\}.
\]
In particular one can take the distinct fingerprints as the states, sending \(\Phi_c(n)\) to \(\Phi_c(2n+b)\) on bit \(b\). The continuation equivalence makes the transition and output independent of the representative \(n\).

**2. Dyadic count.** For \(r\ge0\), \(I_{2^r}=\{0\}\cup\{2^j:0\le j\le r\}\). Write \(R_j(n)\) for the length of the consecutive run of binary ones beginning at the bit of weight \(2^j\), with length zero if that bit is zero. Put \(e_j=R_j(n)\bmod2\). Adding \(2^j\) changes the parity by \(1\oplus e_j\), since it turns \(R_j(n)\) ones into zeros and turns one zero into a one. Thus
\[
t(n+2^j)=t(n)\oplus1\oplus e_j.
\]
If \(e_j=1\), then \(R_{j+1}(n)=R_j(n)-1\) is even. Hence the run-parity vector \((e_0,\ldots,e_r)\) has no adjacent ones. Conversely, choose any such vector as the binary digits in positions \(0,\ldots,r\), and put a zero in position \(r+1\). The resulting run parities are the chosen vector, and the independent bit at position \(r+2\) can choose either value of \(t(n)\) without changing these run parities. Length-\(r+1\) words with no adjacent ones number \(F_{r+3}\): their counts for lengths zero and one are 1 and 2, and for larger lengths splitting by initial 0 or 10 gives the Fibonacci recurrence. The fingerprint determines the whole run-parity vector and the parity bit, so
\[
N(2^r)=2F_{r+3},\qquad r\ge0.
\]

**3. Even and odd successor-dyadic fingerprints.** Direct division gives
\[
I_{2^k+1}=\{0,1,2^k+1\}\cup\bigcup_{j=0}^{k-1}\{2^j,2^j+1\}.
\]
For \(s\in I_{2^k+1}\), \(t(2m+s)=t(m+\lfloor s/2\rfloor)\oplus(s\bmod2)\) and \(t(2m+1+s)=t(m+\lfloor(s+1)/2\rfloor)\oplus((s+1)\bmod2)\). The two index images satisfy
\[
\{\lfloor s/2\rfloor:s\in I_{2^k+1}\}=I_{2^{k-1}},\qquad
\{\lfloor(s+1)/2\rfloor:s\in I_{2^k+1}\}=I_{2^{k-1}+1}.
\]
For the first identity, the pair \(\{2^j,2^j+1\}\) for \(j\ge1\) maps to the singleton \(2^{j-1}\), and \(2^k+1\) maps to \(2^{k-1}\); the small indices supply \(0,1\). For the second identity the same pair maps to \(\{2^{j-1},2^{j-1}+1\}\) and \(2^k+1\) maps to \(2^{k-1}+1\). When \(k=1\), the original indices are \(\{0,1,2,3\}\) and the two images are \(\{0,1\}\) and \(\{0,1,2\}\), respectively. The prescribed XOR bits are fixed and each image coordinate is represented. Hence the even and odd prefix values contribute exactly \(N(2^{k-1})\) and \(N(2^{k-1}+1)\) fingerprints, respectively.

These families are disjoint. The four offsets \(0,1,2,3\) all occur. For an even prefix value, the pairs at offsets \((0,1)\) and \((2,3)\) both have opposite bits. For an odd prefix value \(2m+1\), having both pairs opposite would require \(t(m)=t(m+1)=t(m+2)\). Every length-three interval contains an even index and its next odd index, with opposite bits, so this is impossible. It follows that
\[
N(2^k+1)=N(2^{k-1})+N(2^{k-1}+1)\qquad(k\ge1).
\]

**4. Solve the recurrence.** Put \(H_k=N(2^k+1)\) for \(k\ge0\). The dyadic count at \(r=1\) gives \(H_0=N(2)=2F_4=6\). Steps 2 and 3 give \(H_k=H_{k-1}+2F_{k+2}\). Hence
\[
H_k=6+2\sum_{j=1}^k F_{j+2}=6+2(F_{k+4}-F_4)=2F_{k+4}.
\]
By Step 2 this equals \(N(2^{k+1})\), as claimed.

## Verification

The accompanying `checker.py` and `checker_output.txt` record finite corroboration. Run `python3 checker.py` under Python 3.8 or later using the standard library. The checker constructs the finite residual offset set and enumerates low-order residues and the four possible neighboring high-order Thue–Morse pairs for each \(k=1,\ldots,8\). It checks the even/odd split and the two cardinalities and their sum. For a power-of-two block size greater than the maximum offset, adding an offset to a low-order residue carries at most one block, so the two adjacent high-order bits suffice; all four pairs occur starting at high indices 0, 1, 2, and 5. Another finite calculation compares continuation signatures and fingerprints on small shifts and prefix values. The all-\(k\) result follows from the proof, not from extending these checks by analogy.

## Relationship to prior work and limitations

Moradi, Rampersad, and Shallit (arXiv:2512.10017v5, §4.2 and Open Problem 2) give bounds and ask for an exact formula for general MSD-first Thue–Morse shifts. The pure dyadic formula is already attributed to Biswas by OEIS A382296; Step 2 supplies a self-contained argument for the benchmark. A382296 also tabulates individual state counts. The result here is the infinite successor-dyadic law and its parity-disjoint recurrence, not the already tabulated values or the pure dyadic benchmark. It does not solve the general-shift problem or make claims about LSD-first state complexity. No assertion is made about the absence of equivalent results in unindexed or unpublished sources.

## References

- D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, https://arxiv.org/html/2512.10017v5, especially §4.2 and Open Problem 2.
- R. Biswas, *State Complexity of Thue–Morse Shifts by Powers of Two*, https://github.com/rnbguy/proofs/blob/main/A382296/A382296.typ.
- OEIS A382296, https://oeis.org/A382296/internal (individual values and attribution of the pure dyadic formula).
