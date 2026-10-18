# Palindromic realizability of binary two-round Ehrenfeucht–Fraïssé types

## Finding
Consider the nonempty finite words over the two named colours `0` and `1` in which **both** colours occur. Regard a word as a finite strict linear order with two unary colour predicates. Write \(u\equiv_2 v\) if the structures satisfy the same first-order sentences of quantifier rank at most two (equivalently, Duplicator wins the two-round Ehrenfeucht–Fraïssé game).

There are exactly 90 such \(\equiv_2\)-classes. **Exactly 20 classes contain a palindrome.** A class contains a palindrome if and only if it is fixed by reversal: equivalently, \(u\equiv_2 u^{\mathrm{rev}}\) for one (and hence every) word \(u\) in the class. Every one of these 20 classes has a palindromic representative with at most **nine** positions, and nine is sharp. Precisely two classes require nine positions; they are represented by `001010100` and `110010011`. Both have unrestricted shortest representatives of length eight (`00101100` and `11001011`, respectively).

The numbers of classes by **shortest palindromic representative length** are: length three: 2; four: 2; five: 6; six: 2; seven: 6; eight: 0; nine: 2. The count 90 and the unrestricted eight-position bound are earlier results; the contribution is the palindrome realizability criterion, its exact 20-class classification, and the sharp symmetry-constrained nine-position bound.

## Assumptions and scope
A word \(w=w_1\cdots w_n\) denotes the structure on \(\{1,\ldots,n\}\) with the usual strict order and predicates \(P_0,P_1\), where exactly \(P_{w_i}(i)\) holds. The theorem requires \(n\ge2\), and each of `0` and `1` occurs. Reversal changes position \(i\) to \(n+1-i\), preserving letter names, not exchanging colours. A palindrome is a word identical to its reversal. The quantifier-rank bound concerns unrestricted first-order sentences, not the number of quantifiers or a fixed sentence length.

For a position \(i\), let \(L_i\) be the *set* of letters strictly before \(i\), and \(R_i\) the set strictly after \(i\). Define its one-round character and the word signature by
\[
\chi_w(i)=(w_i,L_i,R_i),\qquad
S(w)=\{\chi_w(i):1\le i\le n\}.
\]
The empty word and monochromatic words are included in the finite-state closure calculation but not in the 90-class theorem.

## Proof
**Game lemma.** For finite words \(u,v\), one has \(u\equiv_2 v\) exactly when \(S(u)=S(v)\). On the first move, choosing \(i\) forces the response to have the same letter. For any second move, the only further atomic information is equality or which selected point is earlier, together with the second point's letter. Thus all legal second choices on either side can be matched precisely when the letter sets to the left and right agree. Requiring this for a first move in either structure is equality of the *sets* of one-round characters. This proves both directions without assuming a bound on word length.

**Finite closure.** Encode a letter subset by its two-bit mask and a character \((c,L,R)\) by index \(16c+4L+R\). The 32 possible characters give each signature a canonical 32-bit mask. If a word with signature \(S\) has used-letter set \(U(S)\) and we append letter \(a\), its new signature is exactly
\[
T_a(S)=\{(c,L,R\cup\{a\}):(c,L,R)\in S\}\ \cup\ \{(a,U(S),\varnothing)\}.
\]
This operation depends only on \(S\), since \(U(S)\) is the set of first coordinates in \(S\). Starting at the empty signature, breadth-first exploration under \(T_0,T_1\) terminates with **97 distinct states**, and both transitions from *each* visited state lead to visited states. Hence induction on word length establishes that these are **all** signatures of finite binary words, including arbitrarily long words; this is a finite closure certificate, not a finite-length extrapolation. Exactly 90 visited states use both letters; the remaining seven consist of the empty signature and three monochromatic signatures for each letter.

**Reversal and palindromes.** Reversing a word transforms \(S\) by the involution
\[
\iota(S)=\{(c,R,L):(c,L,R)\in S\}.
\]
Consequently any class containing a palindrome is \(\iota\)-fixed. Checking this involution on the complete 90-state collection gives **20** fixed states. Independently enumerate all palindromes of lengths zero through nine by choosing their first \(\lceil n/2\rceil\) letters, mirroring them, and computing their signatures directly. Exactly those 20 two-colour fixed states occur. Thus reversal invariance is also sufficient, and all of them have palindromic representatives of length at most nine. Retaining the first representative for each state in increasing order of length gives exactly the shortest-length distribution stated above. The attached `verify.py` performs every finite step, implements the game lemma independently for the displayed representatives, and checks the closure of all 97 states under both transitions.

**Sharpness.** Both length-nine witnesses have **eight distinct** one-round characters, including the self-reversing characters \((0,\{0,1\},\{0,1\})\) and \((1,\{0,1\},\{0,1\})\). Any equivalent word needs at least eight positions. A palindrome with exactly eight positions pairs each position with a *different* mirror position; a self-reversing character must then occur at least twice. Therefore an eight-position palindrome cannot realize all eight distinct characters of either witness. The two displayed nine-position palindromes attain the bound. Their respective eight-position unrestricted representatives have the same signatures (verified directly), so the symmetry constraint costs exactly one additional position in both extremal classes.

## Verification
Run `python3 verify.py` with standard Python 3; no third-party packages or data downloads are used. The expected final line is `VERIFY_OK`, preceded by the counts `97`, `90`, `20`, the minimum-length distribution, and the two extremal palindromes. The verifier uses both a transition-based state-closure enumeration and an independently written direct two-round game check for each of the 20 palindromic representatives against an unrestricted shortest representative.

## Relationship to prior work
Mwesigye and Truss (published online in 2010) established the character method for equivalence of finite coloured orders and the sharp unrestricted rank-two representative bound \(m^2+2m\), which is eight for two colours. Their later article (published online in 2018) explicitly classifies the 90 two-colour rank-two classes and studies unrestricted shortest representatives. These established results explain the foundation and the reference 90 and eight counts; they do **not** give the 20 palindrome-realizable classes or the sharp symmetry-constrained bound nine in the inspected Sections 1–2. The separate published calculation of rank-two one-red words studies a proper subfamily and does not determine the full two-colour palindrome classification. The present complete palindrome intersection and its two extremal cases require the reversal-specific comparison and certificates above.

## Limitations
The result concerns finite words using exactly two named letters and quantifier rank two. It does not assert an analogous reversal criterion, 20-class count, or nine-position bound for larger alphabets or greater quantifier ranks. The exhaustive part of the proof is valid because the 97-state closure is complete; merely checking words of bounded length would not prove the all-length assertion. Originality was assessed against the identified sources; additional unindexed presentations of symmetry-constrained representatives cannot be excluded. No independent audit has been conducted.

## References
1. F. Mwesigye and J. K. Truss, “Classification of Finite Coloured Linear Orderings,” *Order* **28** (2011), 387–397; first published online 7 September 2010. DOI: 10.1007/s11083-010-9178-9. Open full text: https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download.
2. F. Mwesigye and J. K. Truss, “On Optimal Representatives of Finite Coloured Linear Orders,” *Order* **36** (2019), 107–117; published online 2 May 2018. DOI: 10.1007/s11083-018-9458-3. Open full text: https://eprints.whiterose.ac.uk/id/eprint/129275/15/Mwesigye-Truss2019_Article_OnOptimalRepresentativesOfFini.pdf.
3. “Exact quantifier-rank profiles for finite one-red linear orders,” public mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-quantifier-rank-profiles-for-finite-one-red-linear-orders--eec9053b6af5. (The restriction to one occurrence of one colour is not imposed here.)
