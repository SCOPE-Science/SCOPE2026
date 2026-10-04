# Fibonacci extremals for shortest absent subsequences of binary words

## Finding
Let \(\operatorname{SAS}(w)\) be the set of shortest words that are not subsequences of a finite word \(w\). As in the standard universality convention, the alphabet is \(\operatorname{alph}(w)\). Define Fibonacci numbers by \(F_0=0\), \(F_1=1\), and \(F_{t+2}=F_{t+1}+F_t\). For
\[
M_n=\max_{w\in\{0,1\}^n}|\operatorname{SAS}(w)|,
\]
the exact values are
\[
M_1=1,\qquad M_{2m}=F_{m+3},\qquad M_{2m+1}=2F_{m+1}\quad(m\ge 1).
\]
Thus the extremal profile has two different Fibonacci subsequences according to the parity of the word length.

For the even case, write \(C_i=01\) for odd \(i\) and \(C_i=10\) for even \(i\). Then \(C_1\cdots C_m\) attains \(F_{m+3}\). For the odd case, \(C_1\cdots C_{m-1}E_m\) attains \(2F_{m+1}\), where \(E_m=001\) for odd \(m\) and \(E_m=110\) for even \(m\).

## Assumptions and scope
A subsequence is obtained by deleting letters while preserving order. The universality index \(\iota(w)\) is the largest \(k\) such that every word of length \(k\) over \(\operatorname{alph}(w)\) occurs as a subsequence. Hence every SAS has length \(\iota(w)+1\). A unary word has exactly one SAS, so for \(n\ge2\) it cannot beat the displayed binary constructions; the proof below therefore treats non-unary words over \(\{0,1\}\).

An arch is a shortest prefix of the remaining word containing both symbols. Its last symbol occurs only once in that arch. A word of binary universality index \(k\) has \(k\) arches followed by a rest containing at most one symbol.

## Proof
We use two elementary consequences of the arch decomposition.

**Monotonicity at fixed universality.** If \(u\) is a subsequence of \(w\) and \(\iota(u)=\iota(w)=k\), then
\[
\operatorname{SAS}(w)\subseteq\operatorname{SAS}(u).
\]
Indeed, every SAS of \(w\) has length \(k+1\). If it were a subsequence of \(u\), it would also be a subsequence of \(w\). It is therefore absent from \(u\), and because \(u\) is \(k\)-universal it is shortest absent there as well.

From each binary arch choose one occurrence of the symbol opposite to the unique last symbol, together with that last symbol. Doing this in every arch produces a subsequence with the same universality index, length \(2k\), empty rest, and arches each equal to \(01\) or \(10\). Consequently, at fixed \(k\), the largest possible number of SAS is achieved by a concatenation of such two-letter arches.

**Transfer matrices.** For a one-universal binary component \(U\), let \(H_U(a,b)=1\) exactly when the length-two word \(ab\) is absent from \(U\). The standard SAS gluing property for a perfect universal prefix says that when one-universal components are concatenated, the number of SAS is obtained by multiplying these boundary matrices and summing all entries. In the two minimal cases,
\[
H_{01}=A=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad
H_{10}=B=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Equivalently, if the running row vector is \((x,y)\), then
\[
(x,y)A=(x+y,y),\qquad (x,y)B=(x,x+y).
\]
Starting from \((1,1)\), after \(t\) minimal arches the two coordinates, sorted in decreasing order, are at most
\[
(F_{t+2},F_{t+1}).
\]
This follows by induction: the next larger coordinate is at most the sum \(F_{t+2}+F_{t+1}=F_{t+3}\), while the untouched coordinate is at most \(F_{t+2}\). Equality is preserved by alternately choosing the matrix that leaves the currently larger coordinate untouched. Therefore the maximum number of SAS among all binary words of universality index \(k\) is
\[
F_{k+2}+F_{k+1}=F_{k+3}.
\]

Now fix the length.

**Even length.** Let \(n=2m\). A non-unary binary word has \(\iota(w)\le m\), since every arch has length at least two. If \(\iota(w)\le m-1\), the fixed-index bound is at most \(F_{m+2}\). If \(\iota(w)=m\), all arches have length two and the rest is empty, so the transfer bound is \(F_{m+3}\), attained by \(C_1\cdots C_m\). Hence \(M_{2m}=F_{m+3}\).

**Odd length.** Let \(n=2m+1\). Again \(\iota(w)\le m\). If \(\iota(w)\le m-1\), then
\[
|\operatorname{SAS}(w)|\le F_{m+2}\le 2F_{m+1}.
\]
It remains to consider \(\iota(w)=m\). Relative to the minimum length \(2m\), there is exactly one extra symbol. Group the word into \(m\) one-universal components, taking the first \(m-1\) components to be the first \(m-1\) arches and the last component to be the final arch together with the rest. Exactly one component has length three.

If the exceptional component occurs at an interior position \(j<m\), it is itself an arch and hence is either \(001\) or \(110\). Their boundary matrices are
\[
H_{001}=\begin{pmatrix}0&0\\1&1\end{pmatrix},\qquad
H_{110}=\begin{pmatrix}1&1\\0&0\end{pmatrix}.
\]
After the first \(j-1\) minimal arches, each coordinate is at most \(F_{j+1}\). The exceptional matrix therefore replaces the state by \((z,z)\) with \(z\le F_{j+1}\). With \(m-j\) minimal arches left, the total is at most
\[
F_{j+1}F_{m-j+3}.
\]
For all \(a\ge2\) and \(b\ge4\),
\[
F_aF_b\le 2F_{a+b-3}.
\]
This is proved by induction on \(a\): the cases \(a=2,3\) are immediate, and for \(a\ge4\),
\[
F_aF_b=F_{a-1}F_b+F_{a-2}F_b\le2F_{a+b-4}+2F_{a+b-5}=2F_{a+b-3}.
\]
Taking \(a=j+1\) and \(b=m-j+3\) gives the desired bound \(2F_{m+1}\).

If the exceptional component is the last one, it is one of
\[
001,110,011,100,010,101.
\]
Their boundary matrices send \((x,y)\), respectively, to states whose total is
\[
2y,\ 2x,\ x+y,\ x+y,\ y,\ x.
\]
After \(m-1\) minimal arches, \(x,y\le F_{m+1}\) and \(x+y\le F_{m+2}\le2F_{m+1}\). Thus the last component also gives at most \(2F_{m+1}\).

Finally, after \(m-1\) alternating minimal arches the larger coordinate is \(y=F_{m+1}\) when \(m\) is odd and \(x=F_{m+1}\) when \(m\) is even. Appending \(001\) in the first case or \(110\) in the second doubles that coordinate. Hence \(M_{2m+1}=2F_{m+1}\), completing the proof.

## Verification
The proof is infinite and does not depend on finite enumeration. Two supplementary checks are included. `verify.py` independently recomputes all binary words through length \(14\), checks the exact parity formulas, checks the transfer recurrence, the exceptional-component inequality, and the explicit witnesses. `census.c` is a separate exhaustive engine based on distinct-subsequence dynamic programming; its recorded output through length \(22\) is `census_22.txt`. The maxima for lengths \(1\) through \(22\) are
\[
1,3,2,5,4,8,6,13,10,21,16,34,26,55,42,89,68,144,110,233,178,377,
\]
matching the theorem.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced and studied shortest absent subsequences and proved the fixed-universality monotonicity and gluing tools used here. Their Proposition 3.14 identifies an alternating permutation word \(A_k\) as extremal at fixed universality index, while Proposition 3.10 only gives a non-tight exponential lower bound for its SAS count under the section's large-even-alphabet standing assumption. Specializing the transfer to a binary alphabet yields the Fibonacci fixed-index count used above; the even-length part is therefore close to a specialization of that framework rather than an isolated new phenomenon.

Fleischmann, Haschke, Huch, Mayrock, and Nowotka characterize classes of words by numbers of absent length-\(k\) subsequences, including the subclass that is \((k-1)\)-universal. Fleischmann, Höfer, Huch, and Nowotka subsequently characterize binary Simon-congruence classes via the \(\alpha\)-\(\beta\) factorization. Neither inspected work states the fixed-word-length extremal problem or the even/odd Fibonacci profile above. The new step is the exact optimization under a length budget, especially the one-extra-symbol analysis that gives the odd value \(2F_{m+1}\).

## Limitations
The theorem is only for a binary alphabet and maximizes the number of shortest absent subsequences, not minimal absent subsequences of arbitrary length. It gives explicit extremizers but does not classify all extremizing words for every \(n\). The literature search found no equivalent fixed-length formula, but an older equivalent formulation in subsequence-universality or Simon-congruence terminology remains a residual originality risk.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, 31 August 2021; later published in *Fundamenta Informaticae* 189 (2023), 199–240.
2. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981v1, 16 February 2022.
3. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *α-β-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192v1, 25 June 2023.
