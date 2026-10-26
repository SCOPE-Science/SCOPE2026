# Universal finite palindrome profiles in non-self-opposite modular-difference lifts

## Finding
Let \(q\ge3\), \(m\ge1\) and let \(B\subseteq\mathbb Z/q\mathbb Z\) contain zero and satisfy \(B\cap(-B)=\{0\}\). Let \(Y\subseteq B^{\mathbb Z}\) be a nonempty subshift containing a block of exactly \(L\ge1\) consecutive zeroes but no block of \(L+1\) consecutive zeroes. Its modular-difference lift is
\[
X_{q,m}(Y)=\{x\in(\mathbb Z/q\mathbb Z)^{\mathbb Z}: (x_{j+m}-x_j)_{j\in\mathbb Z}\in Y\}.
\]
Let \(P_{q,m}(n)\) count the distinct length-\(n\) words in this lift that are ordinary palindromes. For every integer \(n\ge1\), the **complete** palindrome-complexity function is
\[
P_{q,m}(n)=\begin{cases}
q^{\lceil n/2\rceil},&1\le n\le m,\\
q^{(m+f_m(n-1))/2},&m<n\le m+L,\\
0,&n>m+L,
\end{cases}
\qquad
f_m(t)=\#\{r\in\mathbb Z/m\mathbb Z:2r\equiv t\pmod m\}.
\]
In particular, \(f_m(t)=1\) when \(m\) is odd; when \(m\) is even it equals \(2\) for even \(t\) and \(0\) for odd \(t\). The exact longest palindromic length is \(m+L\). For even \(m\), the tail counts alternate between \(q^{m/2+1}\) at odd lengths and \(q^{m/2}\) at even lengths. All statements hold regardless of minimality, entropy or other word statistics of \(Y\). At the first length beyond the delay, \(n=m+1\), the count is \(q^{\lceil(m+1)/2\rceil}\): for every \(m\ge2\) this includes exactly \(q^{\lceil(m+1)/2\rceil}-q\) **nonconstant palindromes**. By contrast, all palindromes for the earlier first-difference case \(m=1\) are constant.

For the Fibonacci substitution subshift, with \(0\mapsto01\) and \(1\mapsto0\), one has \(L=2\), so every lift with \(q\ge3\) has the above profile with an exact cutoff at \(m+2\). These are strictly ergodic lifts by Kang and Jäger's established theorem, despite having no palindrome of length \(m+3\) or greater.

## Assumptions and scope
A subshift is a nonempty closed, shift-invariant set of two-sided sequences. Every finite word in its language occurs as a contiguous block of at least one two-sided point. A palindrome is a word unchanged by reading its letters in reverse order, without complementing letters. Zero-run bound \(L\) means \(0^L\) belongs to the language and \(0^{L+1}\) does not. The cyclic additive alphabet \(\mathbb Z/q\mathbb Z\) is represented by its residue classes, and all differences are taken modulo \(q\). No symmetry under reversal is assumed for the base language. The condition \(B\cap(-B)=\{0\}\) excludes a pair of nonzero opposite residue symbols, and in particular excludes any self-opposite nonzero symbol.

## Proof
**Every starting block lifts.** Fix any \(y\in Y\) and any arbitrary \(m\)-tuple \(c=(c_0,\ldots,c_{m-1})\) of residues. The recursion \(x_{j+m}=x_j+y_j\) determines a unique two-sided sequence \(x\): iterate forward separately in each residue class modulo \(m\), and solve the same equations backward. Thus every \(m\)-letter block \(c\) occurs as the first \(m\) letters of some lift. In particular every length-\(n\) word with \(n\le m\) occurs, and the ordinary palindrome count is \(q^{\lceil n/2\rceil}\).

**Projection reverses with a minus sign.** Suppose \(w=(w_0,\ldots,w_{n-1})\) is a palindrome in the lift, with \(n>m\), and let \(t=n-m\). Its projected word \(v_i=w_{i+m}-w_i\) for \(0\le i<t\) belongs to the language of \(Y\). Because \(w_i=w_{n-1-i}\), one computes for every \(i\)
\[
v_{t-1-i}=w_{n-1-i}-w_{n-1-m-i}=w_i-w_{i+m}=-v_i.
\]
Each \(v_i\) and \(-v_i\) belongs to \(B\), hence \(v_i=0\) by the non-self-opposite assumption. Therefore every projected word of a palindrome of length \(n>m\) is exactly \(0^{n-m}\), and \(w_{i+m}=w_i\) throughout its length. In particular, if \(n>m+L\), the projected zero block is forbidden and \(P_{q,m}(n)=0\).

**Every admissible reflection occurs.** Conversely let \(m<n\le m+L\) and take an \(m\)-periodic length-\(n\) word \(w\) which is a palindrome. The block \(0^{n-m}\) occurs in \(Y\) because \(0^L\) occurs. Choose a base sequence with that zero block at coordinates \(0,\ldots,n-m-1\), and lift it using the first \(m\) entries of \(w\) as the free prefix. The recursion gives exactly \(w\) for the first \(n\) entries. Thus admissible length-\(n\) palindromes are precisely the length-\(n\) palindrome words periodic with period \(m\).

**Count reflection orbits exactly.** An \(m\)-periodic word is specified by \(m\) residues \(c_r\), indexed by \(r\in\mathbb Z/m\mathbb Z\). As \(n>m\), every such residue index occurs in the length-\(n\) word. Its palindrome condition reads
\[
c_r=c_{n-1-r\pmod m}\qquad(r\in\mathbb Z/m\mathbb Z).
\]
The index map \(r\mapsto n-1-r\) is an involution on \(m\) residues, with exactly \(f_m(n-1)\) fixed points and \((m-f_m(n-1))/2\) transposed pairs. Hence it has \((m+f_m(n-1))/2\) orbits, each independently assigned one of \(q\) residues. This gives the asserted exact count. Solving \(2r\equiv n-1\pmod m\) yields the stated parity cases. Since \(f_m(n-1)\ge0\), the value at \(n=m+L\) is positive, proving sharpness of the final cutoff.

**Fibonacci specialization.** Every Fibonacci-substitution word contains no \(000\), because each substituted block is \(01\) or \(0\) and no factor \(11\) occurs; \(00\) does occur, for example in \(010010\). The statement also follows directly by inspecting the substitution's two-letter overlap types. Thus \(L=2\). The full-lift strict ergodicity is an independently established property of this example, not a consequence of palindrome counting. The positive nonconstant count for every \(m\ge2\) follows by subtracting the \(q\) constant words from the reflection count at \(m+1\).

## Verification
The accompanying standalone `verify.py` enumerates all starting \(m\)-tuples and all projected base blocks in finite test families, constructs lift words with the defining recursion, and counts ordinary palindromes without using the orbit formula. It checks Fibonacci factors and several periodic binary and ternary zero-run bases; it separately enumerates the cyclic reflection-fixed strings. On execution it reports `PASS 450 independent finite palindrome-count checks`. These checks only sample small \(q,m,n\). The argument above, rather than any finite enumeration, proves every stated quantifier.

## Relationship to prior work
Kang and Jäger (arXiv:2609.01140v1, September 1, 2026) study permutative subshift lifts and prove strict ergodicity of all Fibonacci lifts. Their Theorem 1.6 applies to exactly this family of higher-lag difference codes. Their article does not state the palindrome-complexity formula or the reflection-orbit classification. A published earlier mathematical note titled *Automorphism rigidity and palindromic collapse in cyclic Sturmian lifts* gives the exact first-difference (\(m=1\)) palindrome profile: all allowable lengths have exactly \(q\) constant palindromes, with a sharp zero cutoff. That already-proved special case is fully acknowledged and is not a novelty claim. The present result gives exact counts at every length, arbitrary lag \(m\), and the universal alphabet/zero-run criterion. General results on palindromic-factor complexity for reversal-closed languages, including work by Kim and Kwon (arXiv:2609.16596), do not directly supply this formula: the languages considered here need not be reversal-closed. No claim is made that the general notion of palindromic complexity or reflection-orbit enumeration is new.

## Limitations
The theorem deliberately excludes \(q=2\), for which \(-1=1\), so nonzero projected palindromes can survive and the universal zero-run cutoff need not hold. More generally, dropping \(B\cap(-B)=\{0\}\) removes the anti-palindrome obstruction. The result does not classify all palindromic factors of arbitrary finite-to-one symbolic extensions. There remains a bibliographic priority risk from older cyclic-word constructions or an equivalent unpublished reflection argument; independent bibliographic assessment has not been performed. The indexed first-difference note's mathematical RESULT text was directly read and its exact special-case formula compared. No whole-document exclusion is asserted for other unexamined references.

## References
- Z. Kang and T. Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1 (2026-09-01), especially Theorem 1.6 and Sections 3–5.
- D. H. Kim and S. Kwon, *On the number of palindromic factors of low complexity words*, arXiv:2609.16596 (2026-09-15), related general reversal-closed complexity bounds.
- *Automorphism rigidity and palindromic collapse in cyclic Sturmian lifts* (published mathematical record, 2026-10-11), earlier first-difference cutoff result; full text not available for direct examination.
