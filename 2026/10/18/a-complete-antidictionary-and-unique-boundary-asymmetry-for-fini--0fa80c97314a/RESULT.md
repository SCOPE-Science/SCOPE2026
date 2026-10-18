# A complete antidictionary and unique boundary asymmetry for finite Fibonacci words

## Finding
For every integer \(k\ge5\), define the finite binary Fibonacci words by \(F_0=0\), \(F_1=01\), and \(F_k=F_{k-1}F_{k-2}\). Write \(L_j=|F_j|\), with \(L_0=1\) and \(L_1=2\). A *minimal absent factor* of a finite word is an absent contiguous binary word all of whose proper contiguous factors occur. Denote their set by \(\mathcal M(F_k)\).

For each \(1\le j\le k-2\), let \(U_j\) be \(F_j\) without its final two symbols and let \(y_j\) be the binary complement of the penultimate symbol of \(F_j\). Let \(U\) be \(F_{k-1}\) without its final two symbols; let \(x\) be the penultimate symbol of \(F_{k-1}\), and let \(d\) be the final symbol of \(F_{k-3}\). The **complete** minimal-absent-factor set is
\[
\mathcal M(F_k)=\{y_jU_jy_j:1\le j\le k-2\}\ \cup\ \{xUx,\ dF_{k-2}0\}.
\]
All these \(k\) words are distinct, and their lengths are precisely
\[
L_1,L_2,\ldots,L_{k-2},\quad L_{k-2}+2,\quad L_{k-1}.
\]
Exactly one of them, \(dF_{k-2}0\), is nonpalindromic. In particular \(|\mathcal M(F_k)|=k\) for every \(k\ge5\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), substrings are **linear** contiguous factors (not scattered subsequences and not circular factors), and no reversal identification is made. Indices are zero-based in positional arguments. The theorem begins at \(k=5\); no assertion is made for smaller indices. The first family comprises the known minimal forbidden factors of the *infinite* Fibonacci word; the two additional members arise from finite endpoints.

## Proof
**1. Fibonacci occurrence and central-word facts.** Put \(q=L_{k-2}\), \(p=L_{k-1}\), and \(N=L_k=p+q\). By the exact occurrence lemma for Fibonacci blocks (Guo--Kishi, Lemma 15, with the usual two-index translation), the \(q\)-letter block \(B=F_{k-2}\) occurs in \(F_k\) at exactly the three offsets \(0,q,p\). Indeed \(F_k=B F_{k-3}B\), and the occurrence beginning at \(q\) is the standard overlap occurrence. The letters immediately before the latter two occurrences are the last letters of \(B\) and \(F_{k-3}\), respectively; these are different because consecutive Fibonacci words end in alternating binary symbols. Therefore the shortest suffix occurring just once has length \(K=q+1\): its length-\(q\) suffix \(B\) repeats and every shorter suffix repeats with it, whereas its length-\(q+1\) suffix occurs only once.

Every \(F_k\) is a finite Sturmian word, hence trapezoidal. The standard trapezoidal-word theorem gives \(R+K=N\), where \(R\) is the first length with no right-special factor, and its factor-complexity diagram increases by one, remains constant, then decreases by one. Consequently \(R=p-1\) and the number \(c(t)\) of distinct length-\(t\) factors is, for \(0\le t\le N\),
\[
c(t)=\min\{t+1,q+2,N-t+1\},\qquad c(N+1)=0.
\]
These are established facts about trapezoidal finite Sturmian words (Bucci--De Luca--Fici, Proposition 2.8 and Definition 2.5); the only additional input is the three-occurrence assertion above.

**2. Exactly which factors are bispecial.** A binary factor is bispecial when each letter occurs as a possible left extension and as a possible right extension. The bispecial factors of the infinite Fibonacci word are exactly its central palindromes \(U_j\) for \(j\ge1\) (including \(U_1=\varepsilon\)); this is recalled and used in Fici--Restivo--Rizzo, Proposition 6. For \(2\le j\le k-2\), the shorter block \(F_{j+2}\) already contains \(U_j\) at offsets \(L_{j-1}\) and \(L_j\). The standard near-commutation identity (\(F_jF_{j-1}\) and \(F_{j-1}F_j\) agree except in their final two, opposite-order letters), together with \(F_j=U_jxy\) for distinct letters \(x,y\), shows that the left-neighbor symbols at these two offsets are different and the right-neighbor symbols are different. Both offsets are internal, so \(U_j\) is bispecial in \(F_{j+2}\) and hence in \(F_k\). The empty word \(U_1\) is bispecial because all four one-sided binary extensions occur.

For \(j=k-1\), \(U=U_{k-1}\) has length \(p-2>q\) and begins with \(B\). Every occurrence of \(U\) thus begins at one of \(0,q,p\); the third offset is too late. The occurrence at zero has no left neighbor, while that at \(q\) has only one. Therefore \(U\) is not left-special. For \(j\ge k\), \(L_j-2\ge p-1=R\), so the corresponding central word cannot be right-special. Thus the bispecial factors of \(F_k\) are **exactly** \(U_1,\ldots,U_{k-2}\), with one bispecial factor at each distinct length \(L_j-2\).

**3. Counting identity for minimal absent factors.** For any binary word \(w\) containing both symbols, let \(b(t)\) count its bispecial factors of length \(t\). For every \(2\le t\le |w|+1\),
\[
m(t)=b(t-2)+2c(t-1)-c(t-2)-c(t),
\]
where \(m(t)\) counts its distinct minimal absent factors of length \(t\) and \(c(|w|+1)=0\). To derive this, group absent \(aub\) by their middle factor \(u\) of length \(t-2\). If \(\lambda(u)\) and \(\rho(u)\) are the numbers of distinct left and right single-letter extensions and \(e(u)\) is the number of occurring two-sided extensions, the group's contribution is \(\lambda(u)\rho(u)-e(u)\). For a proper factor \(u\), its extension-count pair is never \((0,0)\), and therefore
\[
\lambda(u)\rho(u)=(\lambda(u)-1)(\rho(u)-1)+\lambda(u)+\rho(u)-1.
\]
Here \((\lambda-1)(\rho-1)\) is one exactly for bispecial factors and otherwise zero. Summing \(\lambda\), \(\rho\), and \(e\) over length-\(t-2\) factors gives \(c(t-1)\), \(c(t-1)\), and \(c(t)\), respectively. This proves the identity (including \(t=2\), where \(u=\varepsilon\)). No absent factor can exceed length \(|w|+1\).

Using the explicit complexity from step 1, its second-difference term \(2c(t-1)-c(t-2)-c(t)\) vanishes except at \(t=q+2\) and \(t=p\), where it equals one. These two lengths are distinct for \(k\ge5\). Step 2 contributes one further minimal absent factor at each \(t=L_j\) for \(1\le j\le k-2\). Therefore **exactly one** minimal absent factor occurs at each of the \(k\) asserted lengths, and none elsewhere.

**4. Explicit identification.** The central palindromes \(U_j\) and the corresponding palindromic minimal forbidden factors \(y_jU_jy_j\) of the infinite Fibonacci word are described in Fici--Restivo--Rizzo, Table 2 and Theorem 7, and Rampersad--Wiebe, Section 2. The former factors are absent in every finite prefix. Since \(U_j\) is bispecial in \(F_k\), the two length-\((L_j-1)\) proper end factors \(y_jU_j\) and \(U_jy_j\) occur; hence these are minimal absent in \(F_k\).

Write \(F_{k-1}=Uxy\) with \(x\ne y\); \(U\) is palindromic. As above, \(U\) occurs at exactly offsets \(0\) and \(q\). At offset zero it is followed by \(x\); at offset \(q\), the near-commutation identity shows it is preceded by \(x\) but followed by \(y\). Thus \(xU\) and \(Ux\) occur while \(xUx\) does not; it is the unique minimal absent factor of length \(p\).

Finally \(B=F_{k-2}\) occurs only at \(0,q,p\). The occurrence at offset \(q\) is followed by \(0\) (the first letter of \(F_{k-3}\)), and its preceding symbol is the final symbol of \(B\), which differs from \(d\). The occurrence at offset \(p\) is preceded by \(d\) but ends at the word's right boundary; the initial occurrence has no preceding symbol. Therefore \(dB\) and \(B0\) both occur, but \(dB0\) does not. This identifies the unique factor at length \(q+2\).

The \(k-2\) infinite forbidden factors and \(xUx\) are palindromes. The last word \(dB0\) is not: when \(d=1\) its ends differ, while when \(d=0\), it would be palindromic only if \(B\) were palindromic, which it is not: \(d=0\) entails odd \(k\), hence odd \(k-2\); the odd-index Fibonacci word \(F_{k-2}\) begins in \(0\) and ends in \(1\). This completes the classification.

## Verification
The accompanying standalone `verification.py` reconstructs every contiguous factor set and then every minimal absent factor directly, independently of the formula. It checks the full identity of the sets, the count, all lengths, and the unique nonpalindromic member for \(5\le k\le11\), with source lengths \(13,21,34,55,89,144,233\). It separately checks the critical occurrence positions, the finite complexity formula, the bispecial-length spectrum, and the counting identity. The checker is finite corroboration; the unrestricted theorem relies on the arguments and cited lemmas above.

## Relationship to prior work
Fici, Restivo, and Rizzo (2017) characterize minimal forbidden factors of **circular** Fibonacci words and recall the infinite Fibonacci forbidden-factor sequence; circular factors allow boundary wrapping, so their theorem does not determine the linear finite-prefix antidictionary. Rampersad and Wiebe (2023) study correlations of forbidden factors of the **infinite** Fibonacci word. Bucci, De Luca, and Fici (2012) provide the finite-Sturmian trapezoid used here, but do not give the two endpoint minimal absent words. Guo and Kishi (2025) give the exact three-occurrence fact for shorter Fibonacci blocks, without classifying minimal absent factors. The present result combines these structures to distinguish the complete linear antidictionary and its single nonpalindromic boundary element.

## Limitations
The classification assumes standard finite Fibonacci recursion and \(k\ge5\); it does not assert a corresponding result for arbitrary Sturmian prefixes, other directive sequences, or alphabets with additional absent letters. Its originality is assessed against the inspected literature and accessible indexed records; an equivalent result in differently indexed work remains a residual risk. No independent validation has yet been performed.

## References
1. G. Fici, A. Restivo, L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450 (first posted 2017-07-14), especially Section 4, Proposition 6, Theorem 7.
2. M. Bucci, A. De Luca, G. Fici, *Enumeration and Structure of Trapezoidal Words*, arXiv:1203.1203, Proposition 2.8 and Section 2.
3. N. Rampersad, M. Wiebe, *Correlations of Minimal Forbidden Factors of the Fibonacci Word*, arXiv:2309.07070 (first posted 2023-09-13), Sections 1--2.
4. P. Guo, K. Kishi, *Net Occurrences in Fibonacci and Thue-Morse Words*, CPM 2025, DOI 10.4230/LIPIcs.CPM.2025.16, Section 4, Lemma 15.
