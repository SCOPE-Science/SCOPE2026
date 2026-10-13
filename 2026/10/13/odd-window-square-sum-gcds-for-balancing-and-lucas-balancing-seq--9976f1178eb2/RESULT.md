# Odd-window square-sum GCDs for balancing and Lucas-balancing sequences

## Finding
Let \(B_0=0\), \(B_1=1\), and \(B_n=6B_{{n-1}}-B_{{n-2}}\) be the balancing sequence. Let \(C_0=1\), \(C_1=3\), and \(C_n=6C_{{n-1}}-C_{{n-2}}\) be the Lucas-balancing sequence. Define
\[
\mathcal B_2(k)=\gcd_{{n\ge0}}\left(\sum_{{i=1}}^k B_{{n+i}}^2\right),
\qquad
\mathcal C_2(k)=\gcd_{{n\ge0}}\left(\sum_{{i=1}}^k C_{{n+i}}^2\right).
\]
For every odd integer \(k\ge1\),
\[
\boxed{{\mathcal B_2(k)=\mathcal C_2(k)=\gcd(B_k,k)}}.
\]
This gives an exact formula on the complete odd-window branch for two of the four square-sum GCDs asked about in Question 30 of Mbirika--Schrader--Spilker.

## Assumptions and scope
Write \(P_n\) and \(Q_n\) for the Pell and associated Pell sequences, normalized by \(P_0=0,P_1=1\) and \(Q_0=Q_1=1\), both satisfying \(X_n=2X_{{n-1}}+X_{{n-2}}\). The standard identities
\[
B_n=\frac{P_{{2n}}}{2}=P_nQ_n,
\qquad C_n=Q_{{2n}}
\]
are used. The theorem concerns every odd \(k\); no assertion is made here for even \(k\).

## Proof
For \(m\ge1\), the Pell identities
\[
Q_{{2m}}^2=\frac{Q_{{4m}}+1}{2},
\qquad
P_{{2m}}^2=\frac{Q_{{4m}}-1}{4}
\]
give
\[
C_m^2=\frac{Q_{{4m}}+1}{2},
\qquad
B_m^2=\frac{Q_{{4m}}-1}{16}.
\]
Also
\[
\sum_{{i=1}}^m Q_{{4i}}=B_mC_{{m+1}}.
\]
Indeed \(B_mC_{{m+1}}=(P_{{4m+2}}-2)/4\), and consecutive values telescope because \(P_{{4m+2}}-P_{{4m-2}}=4Q_{{4m}}\).

Consequently, for \(n\ge0\),
\[
\sum_{{i=1}}^k B_{{n+i}}^2
=\frac{B_kQ_{{4n+2k+2}}-k}{16},
\qquad
\sum_{{i=1}}^k C_{{n+i}}^2
=\frac{B_kQ_{{4n+2k+2}}+k}{2}.
\]
Here we used
\[
B_{{n+k}}C_{{n+k+1}}-B_nC_{{n+1}}
=B_kQ_{{4n+2k+2}},
\]
which follows from the Pell difference identity \(P_u-P_v=2P_{{(u-v)/2}}Q_{{(u+v)/2}}\) when \(u-v\) is divisible by \(4\).

Fix odd \(k\) and put \(A=B_k\). Then \(A\) is odd. Since
\[
Q_{{r+4}}-Q_r=8P_{{r+2}},
\]
the successive differences of the balancing-square block sums are
\[
A\frac{P_{{4n+2k+4}}}{2}.
\]
The Pell sequence is a strong divisibility sequence, so because \(4n+2k+4\equiv2\pmod4\), the GCD of the integers \(P_{{4n+2k+4}}/2\) over \(n\ge0\) is \(1\). Hence the GCD of all successive differences is exactly \(A\). Therefore
\[
\mathcal B_2(k)=\gcd\left(\frac{AQ_{{2k+2}}-k}{16},A\right).
\]
As \(A\) is odd, \(16\) is invertible modulo \(A\), and thus
\[
\mathcal B_2(k)=\gcd(A,k)=\gcd(B_k,k).
\]

For the Lucas-balancing square sums, the successive differences are
\[
4A P_{{4n+2k+4}},
\]
whose GCD is \(8A\). Hence
\[
\mathcal C_2(k)=\gcd\left(\frac{AQ_{{2k+2}}+k}{2},8A\right).
\]
The recurrence for \(B_n\) gives \(B_n\equiv n\pmod4\), while the associated Pell recurrence gives \(Q_{{4j}}\equiv1\pmod4\). Since odd \(k\) makes \(2k+2\) divisible by \(4\),
\[
AQ_{{2k+2}}+k\equiv2k\equiv2\pmod4.
\]
Thus the displayed half-sum is odd, so it is coprime to \(8\). Its GCD with the odd number \(A\) is again \(\gcd(A,k)\), because \(2\) is invertible modulo \(A\). Therefore
\[
\mathcal C_2(k)=\gcd(B_k,k),
\]
which completes the proof.

## Verification
The proof is symbolic and covers every odd positive integer \(k\). The accompanying verifier independently regenerates the four recurrence sequences, checks the two block-sum identities, and compares direct finite GCDs against \(\gcd(B_k,k)\) for odd \(k\) through \(199\). These computations are regression tests only; the infinite theorem rests on the identities and GCD argument above.

## Relationship to prior work
Mbirika, Schrader, and Spilker define these square-sum GCDs and explicitly ask in Question 30 for closed forms for the balancing, Lucas-balancing, cobalancing, and Lucas-cobalancing cases. They report computational evidence that \(\mathcal B_2(k)=\mathcal C_2(k)\) when \(k\) is odd, but do not give the formula \(\gcd(B_k,k)\) or a proof of that odd branch. Their paper also distinguishes formulas involving a sequence term and its index as a separate structural theme in Question 31.

Mbirika and Spilker's earlier generalized-Fibonacci square-sum theorem concerns recurrences of Fibonacci type \(G_n=G_{{n-1}}+G_{{n-2}}\). It does not directly cover the balancing recurrence \(X_n=6X_{{n-1}}-X_{{n-2}}\), and the later 2023 paper still leaves the balancing square-sum problem open.

## Limitations
The result settles only odd window lengths and only the balancing and Lucas-balancing members of Question 30. It does not determine the even branch or the cobalancing and Lucas-cobalancing square-sum GCDs. The expression \(\gcd(B_k,k)\) is exact but is not a prime-factor closed form; determining such sequence-index GCDs is itself the subject of the source paper's Question 31. A later or unindexed treatment could contain an equivalent reduction, although targeted searches located none.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, “Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers,” *Journal of Integer Sequences* 26 (2023), Article 23.6.4; arXiv:2301.05758v1, first posted January 13, 2023.
2. aBa Mbirika and Jürgen Spilker, “GCD of Sums of k Consecutive Squares of Generalized Fibonacci Numbers,” *Fibonacci Quarterly* 60 (2022), 255–269; arXiv:2204.12626.
3. R. Flórez, R. Higuita, and A. Mukherjee, “Characterization of the strong divisibility property for generalized Fibonacci polynomials,” *Integers* 18 (2018), Paper A14.
