# Complete periodic-cycle spectra of the generalized Narayana recurrence modulo powers of two

## Finding
For every integer parameter \(c\) and modulus \(2^k\), \(k\ge1\), the periodic-cycle lengths and their numbers are explicitly classified. Define \(T(a,b,d)=(b,d,ca+d)\bmod 2^k\). The cases below give the complete cycle census, including the noninvertible coefficient regime.

If \(c\) is odd: one fixed point; for each \(1\le j\le k\), exactly \(4^{j-1}\) cycles of length \(7\cdot 2^{j-1}\). All \(2^{3k}\) states lie on cycles, with a total of \((4^k+2)/3\) cycles.

If \(c=0\): precisely \(2^k\) fixed points and no other cycles.

If \(c\ne0\) and \(h=\nu_2(c)\ge2\): exactly \(2^{\min(k,h)}\) fixed points; for each \(1\le j\le k-h\), exactly \(2^{h-1}\) cycles of length \(2^j\).

If \(\nu_2(c)=1\), let \(t=\nu_2(c+2)\ge2\), taking \(t=\infty\) if \(c=-2\). There are exactly two fixed points, exactly \(2^{\min(k-1,t)}-1\) cycles of length two, and, if \(t\) is finite, exactly \(2^{t-1}\) cycles of length \(2^j\) for every \(2\le j\le k-t\). A negative or empty indicated range contributes nothing. No further periodic-cycle lengths occur. In each even-\(c\) case, exactly \(2^k\) states are periodic; the remaining \(2^{3k}-2^k\) states are transient.

## Assumptions and scope
The parameter \(c\) is any integer, positive, negative or zero. The exponent \(k\) is any positive integer; reduction of all entries is modulo \(2^k\). A periodic point returns to itself after a positive iterate; a transient point eventually enters a cycle but is not itself periodic. The \(2\)-adic valuation of zero is treated as infinity only in explicitly identified cases. The result classifies cycles and numbers of transient states, **not** the distribution of transient tail lengths.

## Proof
Put \(A_c=\begin{pmatrix}0&1&0\\0&0&1\\c&0&1\end{pmatrix}\). Its characteristic polynomial is \(f_c(X)=X^3-X^2-c\).

**Odd coefficients.** Modulo two, \(f_c=X^3+X^2+1\), which is irreducible and therefore primitive of degree three: \(A_c\) has order seven and every nonzero vector over \(\mathbb F_2\) has period seven. The matrix \(A_c^7-I\) is even. Write \(B_c=(A_c^7-I)/2\). Reduction of \(B_c\) modulo two depends only on \(c\bmod4\); for representatives \(c=1,3\), direct integer multiplication gives \(\det B_c\equiv\det(I+B_c)\equiv1\pmod2\) (both computations are replayed in `verify.py`). Thus \(A_c^{14}=I+4C_c\), where \(C_c=B_c+B_c^2\) is invertible modulo two. Repeated squaring shows for all \(s\ge0\) that \(A_c^{7\cdot2^s}-I\) is divisible by \(2^{s+1}\), and after division by \(2^{s+1}\), the resulting matrix is invertible modulo two. For \(s=0\), this uses \(B_c\); for \(s=1\), it uses \(C_c\); thereafter it follows by squaring, since every extra quadratic term has one more factor of two. Multiplying an iterate by an odd positive integer preserves the valuation because \((I+2^rC)^u-I\equiv u2^r C\pmod{2^{r+1}}\) for odd \(u\) and \(r\ge1\). Therefore every vector whose three coordinates have common minimum valuation \(k-r\), for \(1\le r\le k\), has exact period \(7\cdot2^{r-1}\); the zero vector is fixed. There are exactly \(7\cdot2^{3(r-1)}\) vectors in each such valuation stratum, so division by their period yields \(4^{r-1}\) cycles. Summing gives the odd-coefficient formulas.

**Even coefficients and the periodic submodule.** The polynomial reduces to \(X^2(X+1)\) modulo two. Since its factors are coprime, Hensel's lemma and the Chinese-remainder decomposition of the companion module over \(\mathbb Z_2\) split it as a rank-one summand on which \(A_c\) acts by multiplication by the unique odd root \(\lambda\) of \(f_c\), and a rank-two summand with nilpotent reduction modulo two. The latter restriction obeys \(N^2\equiv0\pmod2\), hence \(N^{2k}\equiv0\pmod{2^k}\). It has no nonzero periodic point. The rank-one summand has exactly \(2^k\) points and all are periodic because \(\lambda\) is odd. These assertions also hold when \(c=0\), when \(\lambda=1\).

The root identities \(c=\lambda^2(\lambda-1)\) and \(c+2=(\lambda+1)(\lambda^2-2\lambda+2)\) are exact. Both factors \(\lambda^2\) and \(\lambda^2-2\lambda+2\) are odd, so \(\nu_2(\lambda-1)=\nu_2(c)\) and \(\nu_2(\lambda+1)=\nu_2(c+2)\), including the infinity convention. For \(h=\nu_2(c)\ge2\), the elementary lifting-the-exponent identity gives \(\operatorname{ord}_{2^r}(\lambda)=2^{\max(0,r-h)}\). When \(h=1\), put \(t=\nu_2(c+2)\ge2\); then \(\lambda\equiv-1\pmod4\), \(\nu_2(\lambda^2-1)=t+1\), and \(\operatorname{ord}_{2^r}(\lambda)\) is \(1\) for \(r=1\), \(2\) for \(2\le r\le t+1\), and \(2^{r-t}\) for \(r>t+1\). When \(c=-2\), the root is \(-1\) and the order is two for all \(r\ge2\). When \(c=0\), all orders are one.

Finally, of the \(2^k\) elements of the rank-one summand, exactly \(2^{r-1}\) have exact additive order \(2^r\), for each \(1\le r\le k\), with zero as one extra element. Their cycle lengths are exactly \(\operatorname{ord}_{2^r}(\lambda)\). Dividing by each length and gathering equal lengths gives the displayed formulas. This also proves completeness and the transient count.

## Verification
The standalone `verify.py` checks the determinant conditions needed for the odd coefficient lift in both residue classes modulo four, enumerates every functional-graph component for \(c\in\{-8,-6,-4,-2,-1,0,1,2,3,4,6,8\}\), \(1\le k\le4\), and compares the complete observed and predicted cycle multiplicities. It checks that total cycle-state mass is \(2^{3k}\) for odd coefficients and \(2^k\) for even coefficients. Run `python3 verify.py`. These finite tests support but do not replace the general proof above.

## Relationship to prior work
Narayana-type third-order recurrences and modular periods are studied by Kirthi (2015), which investigates periods modulo primes for a distinguished initialization, without an all-state parameterized functional-graph classification modulo powers of two. Linear recurring sequences and companion-matrix periods are classical, and generic 2-adic lifting and Hensel decomposition are known tools; the result here is the explicit complete parameter-dependent cycle spectrum, including the noninvertible coefficients. Rowland–Yassawi (2015) concern congruence automata for combinatorial coefficients and do not determine this recurrence dynamical classification. A full enumeration over the literature is not claimed.

## Limitations
No formula is asserted for transient preperiod distributions or individual transient tails. The claim concerns this exact cubic coefficient family and powers of two, not other moduli or unrelated recurrences. The related 2024 work on Narayana sequences in finite groups was visible through a bibliographic abstract but its full text was not obtained; this leaves residual originality risk. Independent review has not occurred.

## References
- K. Kirthi, *Narayana Sequences for Cryptographic Applications*, arXiv:1509.05745 (first publicly posted 2015-09-17), https://arxiv.org/abs/1509.05745.
- B. Kuloğlu, E. Özkan and A. G. Shannon, *The Narayana Sequence in Finite Groups*, Fibonacci Quarterly 60 (2022), 212–221; https://doi.org/10.1080/00150517.2022.12427441 (full text not inspected).
- H. T. Engstrom, *On sequences defined by linear recurrence relations*, Transactions AMS 33 (1931), 210–218, https://doi.org/10.1090/S0002-9947-1931-1501599-3 (background bibliographic record; not inspected in full).
