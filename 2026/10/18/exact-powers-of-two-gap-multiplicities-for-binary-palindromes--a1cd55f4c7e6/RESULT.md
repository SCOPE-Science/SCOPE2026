# Exact powers-of-two gap multiplicities for binary palindromes

## Finding

Let \(\mathcal P_2\) be the set of positive integers whose ordinary base-two expansions, written without leading zeros, are palindromic. For every integer \(k\ge2\), put
\[
R_k=\{(n,m)\in\mathcal P_2^2:m-n=2^k\}.
\]
Write \(\tau(k)=\#\{a\ge1:a\mid k\}\). Then
\[
\boxed{\#R_k=2^{k-1}+\tau(k)+1.}
\]
Moreover, the following three disjoint families give **every** element of \(R_k\):

1. For each positive divisor \(a\mid k\), set \(q=k/a\) and
   \[
   n=\sum_{j=0}^{q-1}2^{ja},\qquad m=\sum_{j=0}^{q}2^{ja}.
   \]
   These are the \(\tau(k)\) short-expansion pairs.
2. The unique length-overflow pair
   \[
   (n,m)=(2^k+1,2^{k+1}+1).
   \]
3. Every length-\(2k+1\) binary palindrome whose central bit (the coefficient of \(2^k\)) is zero, together with \(m=n+2^k\). There are exactly \(2^{k-1}\) such palindromes.

This classification gives an explicit answer for a natural infinite collection of the finite multiplicities appearing in Question 26 of Pongsriiam and Saito [1].

## Assumptions and scope

All numbers are positive, expansions are the canonical finite binary expansions with leading digit one, and all pairs are ordered with \(m>n\). Every statement quantifies over **every** integer \(k\ge2\). The condition \(k\ge2\) is necessary: the gap \(2\) admits infinitely many pairs [1, Theorem 12]. The result does not classify arbitrary fixed gaps or bases other than two.

For a positive integer \(z\), let \(L(z)\) be its binary length, and let \(S(z)\subseteq\{0,\dots,L(z)-1\}\) be its set of one-bit positions, indexed from the least significant bit. Binary palindromicity means \(i\in S(z)\) if and only if \(L(z)-1-i\in S(z)\); in particular positions zero and \(L(z)-1\) are occupied.

## Proof

**Case I: \(L(n)\le k\).** Put \(L=L(n)\). Since \(n<2^k\), the digits of \(m=n+2^k\) consist of the digits of \(n\), zeros through position \(k-1\), and a new one in position \(k\). Thus \(L(m)=k+1\) and \(S(m)=S(n)\cup\{k\}\). Write \(S=S(n)\) and \(a=k-L+1\ge1\). For \(s\in S\) with \(s>0\), palindromicity of \(m\) forces \(k-s\in S\) (it cannot equal \(k\)); reflection of this bit in the length-\(L\) palindrome \(n\) forces
\[
(L-1)-(k-s)=s-a\in S.
\]
Consequently every positive member of \(S\) is at least \(a\), and repeated subtraction by \(a\) proves every member of \(S\) is divisible by \(a\). Since \(L-1\in S\), the same subtraction also forces **all** nonnegative multiples of \(a\) through \(L-1\) into \(S\). Hence \(a\mid L-1\) and \(a\mid k=(L-1)+a\). We obtain precisely the divisor-indexed family in part 1. Conversely, for every \(a\mid k\), the two asserted sums have one-bits in equally spaced positions from zero through \(k-a\), respectively through \(k\), so both are palindromes and the difference is \(2^k\). These pairs are distinct because their smaller terms have different leading positions.

**Case II: \(L(n)>k\) and \(L(m)=L(n)\).** Let \(L=L(n)\). The binary addition of \(2^k\) changes precisely a contiguous interval of positions \([k,t]\): digits \(k,\ldots,t-1\) of \(n\) are all one (the carried positions), digit \(t\) is zero, and the corresponding digits of \(m\) are all zero except the one at \(t\). Since both \(n\) and \(m\) are length-\(L\) palindromes, their bitwise difference indicator is palindromic, so the interval \([k,t]\) is fixed under reflection, forcing \(t=L-1-k\). If \(t>k\), the old digits on this reflection-invariant interval have a one at \(k\) and zero at \(t\), contradicting palindromicity of \(n\). Therefore \(t=k\) and \(L=2k+1\). Exactly one central zero digit of \(n\) flips to one, and all other digits are unchanged. Conversely, every length-\(2k+1\) palindrome with central digit zero gives another palindrome when \(2^k\) is added. After fixing its leading and trailing ones, the \(k-1\) independent off-centre digit pairs are free; hence part 3 contributes exactly \(2^{k-1}\) pairs.

**Case III: \(L(n)>k\) and \(L(m)=L(n)+1\).** Again set \(L=L(n)\). Binary overflow upon adding \(2^k\) requires all digits of \(n\) in positions \(k,k+1,\ldots,L-1\) to be one. The new top bit of \(m\) is in position \(L\), while the digits of \(m\) from \(k\) to \(L-1\) are zero. If \(L\ge k+2\), the one at position \(L-2\) in \(n\) forces its reflected position one to be one, hence the bit in position one of \(m\) is one because \(k\ge2\). Yet palindromicity of \(m\) reflects that bit to its zero at position \(L-1\), contradiction. Thus \(L=k+1\).

With \(L=k+1\), the leading and trailing bits of \(n\) are one and bit \(k\) of \(m\) is zero. Reflection in the length-\(k+2\) palindrome \(m\) gives its bit one zero, so bit one of \(n\) is zero. For every \(2\le j\le k-1\), reflection in \(m\), followed by reflection in \(n\), gives
\[
n_j=m_j=m_{k+1-j}=n_{k+1-j}=n_{j-1}.
\]
By induction all bits of \(n\) in positions \(1,\ldots,k-1\) vanish. Thus \(n=2^k+1\), \(m=2^{k+1}+1\), and this pair plainly consists of palindromes. This is the unique part-2 pair.

The three cases partition all possibilities because adding \(2^k\) changes the binary length by at most one. Their smaller terms have lengths at most \(k\), exactly \(k+1\), and exactly \(2k+1\), respectively, so the families are disjoint. Summing the three contributions completes the proof.

## Verification

The accompanying `verify.py` constructs every binary palindrome through length \(2k+2\) and enumerates each ordered pair separated by \(2^k\), independently checking it against the three explicit families. This proves the finite verification claim for all integers \(2\le k\le14\), not the theorem for all \(k\). The unrestricted proof above supplies the infinite quantifier. The script additionally checks the pairwise palindromicity and precise gaps; `verification_output.txt` contains the actual output.

Selected counts are \(\#R_2=5\), \(\#R_4=12\), \(\#R_8=133\), \(\#R_{12}=2055\), and \(\#R_{14}=8197\).

## Relationship to prior work

Pongsriiam and Saito [1, Theorem 12, pages 10–12] characterize exactly which fixed binary palindrome gaps have **infinitely many** pairs: the gap two and those of the form \(2^r+2^{r-1}\) with \(r\ge2\). Therefore their theorem establishes **finiteness** for \(2^k\), \(k\ge2\), but does not determine their cardinalities or pair classifications. Their Question 26 [1, page 26] explicitly asks for bounds on finite fixed-gap multiplicities. The present full three-family classification and exact formula supply more precise information along the geometrically natural powers-of-two gap family. Published single-palindrome counting results [2] and arithmetic progressions within the palindrome set [3] involve different invariants, not the pair count \(\#R_k\).

## Limitations

The formula is restricted to binary palindromes and differences equal to a single power of two with exponent at least two. It gives neither a count for general gaps nor an asymptotic for the sum over finite multiplicities in [1, Question 26]. A targeted comparison of the indexed literature was performed, but unpublished or unindexed equivalent statements remain a novelty risk. The computational checks are finite and do not by themselves certify the unrestricted theorem.

## References

[1] P. Pongsriiam and K. Saito, *Palindromes and Antipalindromes in Short Intervals*, Journal of Integer Sequences **26** (2023), Article 23.9.5, 28 pages. Publicly published 2023-12-11. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL26/Saito/saito1.pdf.

[2] P. Phunphayap and P. Pongsriiam, *Extremal orders and races between palindromes in different bases*, AIMS Mathematics **7** (2022), 2237–2254, as cited in [1, reference 9].

[3] P. Pongsriiam, *Longest arithmetic progressions of palindromes*, Journal of Number Theory **222** (2021), 362–375, as cited in [1, reference 11].
