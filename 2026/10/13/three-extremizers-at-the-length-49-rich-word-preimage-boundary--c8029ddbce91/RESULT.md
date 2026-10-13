# Three extremizers at the length-\(49\) rich-word preimage boundary
## Finding
Define the morphism \(f:\{0,1,2\}^*\to\{0,1\}^*\) by
\[
f(0)=0,\qquad f(1)=01,\qquad f(2)=011.
\]
Among all ternary words \(u\) having prefix
\[
\mathtt{0121012}
\]
for which \(f(u)\) is both rich and \(\frac{14}{5}\)-free, the maximum possible length of \(u\) is \(49\). Exactly three words attain that maximum:
\[
\begin{aligned}
&\mathtt{0121012101101210121210121011012101212101210110100},\\
&\mathtt{0121012101101210121210121011012101212101210110101},\\
&\mathtt{0121012101101210121210121011012101212101210110120}.
\end{aligned}
\]
Equivalently, all three share the same length-\(47\) prefix
\[
\mathtt{01210121011012101212101210110121012121012101101}
\]
and their final two symbols are respectively \(\mathtt{00}\), \(\mathtt{01}\), and \(\mathtt{20}\).

The scalar cutoff \(49\) is the largest finite cutoff in Table 1 of Currie, Mol, and Rampersad's structure-theorem proof; the equality set above is a complete classification of the bottleneck row.

## Assumptions and scope
A binary word \(w\) is rich when it has exactly \(|w|\) distinct nonempty palindromic factors. A nonempty factor \(x\) with least period \(p\) has exponent \(|x|/p\). The phrase \(\frac{14}{5}\)-free means that every nonempty factor has exponent strictly less than \(\frac{14}{5}\).

The ternary length is the length before applying \(f\). The three binary images have lengths \(94\), \(95\), and \(96\), respectively. Their critical exponents are \(\frac{46}{17}\), \(\frac{46}{17}\), and \(\frac{95}{34}\), all strictly below \(\frac{14}{5}\).

The claim concerns only right-extensions of the specific ternary prefix \(\mathtt{0121012}\). It does not classify every finite binary rich \(\frac{14}{5}\)-free word or every row of the source's finite obstruction table.

## Proof
The search is exhaustive because a failed prefix can never become valid after further extension.

For power avoidance this is immediate: a forbidden factor persists under extension. For richness, appending one binary letter creates at most one new distinct nonempty palindrome. Hence once a prefix has fewer distinct nonempty palindromes than its length, its palindromic defect cannot return to zero. Since \(f\) is nonerasing, the same conclusion applies when extending a ternary preimage by one letter.

Starting from \(\mathtt{0121012}\), extend each surviving ternary word by each symbol in \(\{0,1,2\}\). For every candidate \(u\), compute \(f(u)\) and test the two defining conditions exactly. The numbers of survivors at ternary lengths \(47,48,49,50\) are
\[
11,\quad 6,\quad 3,\quad 0.
\]
The complete level counts from length \(7\) through \(50\) are stored in `certificate.json`.

Richness is checked by enumerating all distinct palindromic factors of the binary image and requiring their number to equal its length. Power avoidance is checked factor by factor: for each factor \(x\), its least period \(p\) is found directly, and the factor is rejected exactly when
\[
5|x|\ge 14p.
\]

The length-\(49\) level consists exactly of the three displayed words, while the length-\(50\) level is empty. This proves both the upper bound and completeness of the equality list.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the entire prefix tree twice. One richness test counts distinct palindromic factors directly. The second uses the equivalent criterion that every nonempty prefix has a unioccurrent longest palindromic suffix. Both searches reproduce exactly the same surviving words at every ternary length through \(50\).

Each of the three boundary images is then checked directly again. The verifier recomputes its number of distinct palindromes, its critical exponent as an exact rational number, the common length-\(47\) preimage prefix, and the empty length-\(50\) level.

## Relationship to prior work
Currie, Mol, and Rampersad prove a structure theorem for infinite binary rich words avoiding \(\frac{14}{5}\)-powers. Their Table 1 lists thirteen ternary factors that cannot occur in an infinite preimage \(u\) with \(f(u)\) good, together with finite backtracking cutoffs. The row
\[
v=\mathtt{0121012}
\]
has cutoff \(49\), the largest entry in that table; the next largest is \(48\).

That source gives the scalar cutoff but not the number or identities of all length-\(49\) surviving preimages. A 2024 follow-up by Currie and Rampersad reuses the same factor \(\mathtt{0121012}\) and again invokes a length-\(50\) backtracking cutoff in the proof of its lexicographically least threshold word, but likewise gives no boundary census.

Targeted searches using the exact prefix, the cutoff, all three equality words, the morphism \(f\), and equivalent “eligible word” terminology found no published three-word equality classification.

## Limitations
This is a finite equality classification for one structurally distinguished row of the source's obstruction table. It does not strengthen the repetition-threshold value itself, and it does not claim that the three ternary preimages correspond to all extremal infinite threshold words.

The original and follow-up papers both use backtracking around this obstruction. Unpublished search output or an unindexed auxiliary file could therefore contain the same three boundary words even though no published or indexed statement located in the searches gives the complete equality set.

## References
1. J. D. Currie, L. Mol, and N. Rampersad, “The repetition threshold for binary rich words,” arXiv:1908.03169v1, first public version 2019-08-08; Discrete Mathematics & Theoretical Computer Science 22(1), article 6, 2020, DOI 10.23638/DMTCS-22-1-6.
2. J. D. Currie and N. Rampersad, “The Lexicographically Least Binary Rich Word Achieving the Repetition Threshold,” The Electronic Journal of Combinatorics 31(4), #P4.77, 2024, DOI 10.37236/12464.
