# Dyadic separation periodicity for period-doubling boundary sets

## Finding

Let \(p=p_0p_1p_2\cdots\) be the infinite binary fixed point beginning in \(0\) of \(\mu(0)=01\), \(\mu(1)=00\). For positive integers \(a,b\) and every integer \(d\ge a\), let the **ordered paired-window spectrum** be
\[
C_{a,b}(d)=\{(p_i\cdots p_{i+a-1},\ p_{i+d}\cdots p_{i+d+b-1}):i\ge0\}.
\]
Put \(M=\max(a,b)\) and \(P_M=2^{1+\lceil\log_2M\rceil}\). **For every** \(a,b\ge1\) and \(d\ge a\),
\[
\boxed{C_{a,b}(d+P_M)=C_{a,b}(d).}
\]
In particular, in the boundary-set convention of Rigo, Stipulanti and Whiteland, \(\partial_{p,\ell}[d]=C_{\ell,\ell}(d)\) for \(d\ge\ell\). Thus **every** \(\ell\)-boundary sequence of the period-doubling word is purely periodic, beginning at its first defined index, with a period dividing \(2^{1+\lceil\log_2\ell\rceil}\).

The bound is exact for \(\ell=1,2\). For \(\ell=2\), let \(A,B,D\) be the following three sets of ordered two-letter words:
\[
\begin{aligned}
A={}&\{(00,01),(00,10),(01,00),(01,01),(10,00),(10,10)\},\\
B={}&\{(00,00),(00,01),(00,10),(01,00),(01,10),(10,00),(10,01)\},\\
D={}& A\cup\{(00,00)\}.
\end{aligned}
\]
Then for all \(d\ge2\),
\[
\boxed{C_{2,2}(d)=\begin{cases}
A,&d\equiv2\pmod4,\\
B,&d\text{ odd},\\
D,&d\equiv0\pmod4.
\end{cases}}
\]
In particular the three distinct values have cardinalities \(6,7,7\), and the least positive period is exactly \(4\).

## Assumptions and scope

All indices start at zero; \(a,b,d\) are integers, \(a,b\ge1\), \(d\ge a\). The second window starts \(d\) symbols after the first window starts (so the windows do not overlap). Equality concerns **sets of existing factor pairs**, not the number of occurrences or their frequencies. The bound \(P_M\) is a (not necessarily least) period. The complete classification for length two is an additional explicit instance, not an assertion that every higher-order least period has been determined.

For inductive purposes extend the definition to \(a=0\) or \(b=0\), retaining \(d\ge a\); an empty window is the unique word \(\varepsilon\). The corresponding spectrum is independent of \(d\), because every finite factor occurs at arbitrarily large positions, as proved next.

## Proof

**1. Valuation description and recurrence.** The substitution immediately implies
\[
p_{2j}=0,\qquad p_{2j+1}=1-p_j\qquad(j\ge0).
\]
Induction on \(j\) then gives \(p_j=\nu_2(j+1)\bmod2\), where \(\nu_2\) is the exponent of \(2\). Every finite factor \(p_i\cdots p_{i+r-1}\) repeats infinitely often: choose an integer \(t\) strictly greater than all the finitely many valuations \(\nu_2(i+s+1)\) for \(0\le s<r\). For every \(k\ge0\), replacing \(i\) by \(i+k2^t\) preserves all those valuations and hence every symbol in the factor. This proves the asserted \(d\)-independence whenever either window is empty, including \(d=0\).

**2. The base spectrum.** Let \(Q(d)=C_{1,1}(d)\) for \(d\ge1\). Since even positions contain \(0\) and the odd positions contain both symbols, when \(d\) is odd,
\[
Q(d)=\{(0,0),(0,1),(1,0)\}.
\]
For \(d=2m\), even starting positions contribute \((0,0)\), and odd starting positions contribute the bitwise complement of every pair in \(Q(m)\). Strong induction on \(d\) (using the odd case) gives
\[
Q(d)=\begin{cases}
\{(0,0),(0,1),(1,0)\},&d\text{ odd},\\
\{0,1\}\times\{0,1\},&d\text{ even}.
\end{cases}
\]
Thus \(Q\) has period \(2=P_1\) from its first index.

**3. Exact decimation identities.** Let \(e_r=\lfloor r/2\rfloor\), \(o_r=\lceil r/2\rceil\). For a word \(w\) of length \(e_r\), define \(E_r(w)\) as the length-\(r\) truncation of \(0\,\overline{w_0}\,0\,\overline{w_1}\cdots\). For \(w\) of length \(o_r\), define \(O_r(w)\) as the length-\(r\) truncation of \(\overline{w_0}\,0\,\overline{w_1}\,0\cdots\); here \(\overline{0}=1\), \(\overline{1}=0\). These maps also work at lengths zero. For every starting index \(i\),
\[
p_{2i}\cdots p_{2i+r-1}=E_r(p_i\cdots p_{i+e_r-1}),\qquad
p_{2i+1}\cdots p_{2i+r}=O_r(p_i\cdots p_{i+o_r-1}).
\]
Denote the Cartesian action of maps by \((F\times G)(S)=\{(F(u),G(v)):(u,v)\in S\}\). Splitting starts according to parity gives, whenever the displayed original separation is admissible,
\[
\begin{aligned}
C_{a,b}(2m)={}&(E_a\times E_b)(C_{e_a,e_b}(m))
\cup(O_a\times O_b)(C_{o_a,o_b}(m)),\\
C_{a,b}(2m+1)={}&(E_a\times O_b)(C_{e_a,o_b}(m))
\cup(O_a\times E_b)(C_{o_a,e_b}(m+1)).
\end{aligned}
\]
The lower separations satisfy their own admissibility constraints: if \(2m\ge a\), then \(m\ge o_a\); if \(2m+1\ge a\), then \(m\ge e_a\) and \(m+1\ge o_a\). The identities are **equalities of entire infinite-word spectra**, not merely inclusions, because every starting index has exactly one parity and every reduced index \(i\ge0\) gives a starting index of that parity.

**4. Period induction.** Assume the theorem for all window-length pairs having maximum strictly below \(M\ge2\), with empty-window spectra already constant. In each of the four spectra on the right side of the decimation identities, the maximum window length is at most \(\lceil M/2\rceil<M\). Write \(T=2^{\lceil\log_2M\rceil}\), so \(P_M=2T\). For any positive \(r\le\lceil M/2\rceil\), \(P_r=2^{1+\lceil\log_2r\rceil}\) divides \(T\), since \(r\le T/2\). Upon replacing \(d\) by \(d+2T\), the parity of \(d\) is unchanged and the reduced separations \(m\), \(m+1\) increase by exactly \(T\). Every lower spectrum therefore remains unchanged. The maps \(E_r,O_r\) do not depend on \(d\), so the unions remain identical. The base case from step 2 completes strong induction over \(M\), proving the theorem simultaneously for all positive \(a,b\).

**5. Exact two-letter table and least period.** At \(r=2\), the maps reduce to \(E_2(0)=01\), \(E_2(1)=00\), \(O_2(0)=10\), \(O_2(1)=00\). Substituting the base values of \(Q(m)\) from step 2 into the two displayed decimation identities gives precisely the three sets \(A,B,D\) as stated. In particular \(C_{2,2}(2)=A\), \(C_{2,2}(3)=B\), \(C_{2,2}(4)=D\), and \(C_{2,2}(5)=B\). No period \(1\) or \(2\) preserves this list, and period \(4\) does, so the least positive period is \(4\). Likewise, \(Q\) alternates between two distinct values, giving least period \(2\) at length one.

## Verification

The included standalone file `verify.py` constructs a substitution prefix and, separately, the valuation prefix of length \(32768\), checks their identity, recomputes paired-window spectra for \(1\le a,b\le6\) at two complete ranges of residues, checks hundreds of decimation identities, and verifies the exact \(\ell=2\) sets through separation \(79\). It prints `VERIFY_OK` with a finite-check count if all assertions pass. Run it using `python3 verify.py` in the directory containing the extracted file. This is a bounded consistency check: the infinite equalities are established by the proof above, not by the finite computation.

## Relationship to prior work

Rigo, Stipulanti and Whiteland define the extended boundary sequences and prove automaticity for automatic words (arXiv:2206.15319, first public June 30, 2022). Automaticity alone does not imply periodicity; their result does not give the dyadic **pure** period or the complete two-letter table for the period-doubling word. The paper's own examples explicitly exhibit nonperiodic boundary sequences for other words. The period-doubling word and its valuation formula are classical (OEIS A096268). Huang and Wen analyze return words and occurrence spectra for period doubling (arXiv:1703.07157); their accessible abstract does not state a boundary-set separation law, but full-text comparison was not possible and remains a bibliographic risk. Related string-attractor and reflection-complexity work concerns different invariants.

## Limitations

The theorem applies only to the displayed period-doubling fixed point, not every automatic or Toeplitz word. It gives uniform periods rather than the least period for each larger window size. Set membership is established, not occurrence multiplicity or limiting frequency. Bibliographic searches and the inspected full text have not ruled out unindexed equivalent arguments; the Huang–Wen full text could not be accessed for a decisive inspection. The code's finite checks are not proof of infinite cases.

## References

1. M. Rigo, M. Stipulanti, M. A. Whiteland, *On extended boundary sequences of morphic and Sturmian words*, arXiv:2206.15319v1 (2022-06-30), https://arxiv.org/abs/2206.15319; *Electronic Journal of Combinatorics* 31(1), P1.9 (2024), https://doi.org/10.37236/11728.
2. Y.-K. Huang, Z.-Y. Wen, *Envelope Words and the Reflexivity of the Return Word Sequences in the Period-doubling Sequence*, arXiv:1703.07157v1 (2017-03-21), https://arxiv.org/abs/1703.07157 (full text inaccessible in this review).
3. OEIS A096268, *Period-doubling sequence*, https://oeis.org/A096268.
