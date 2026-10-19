# Unbordered factors at substitution scales in generalized Cantor words

## Finding

For each integer \(q\ge3\), let \(C_q\) be the one-sided infinite binary fixed point starting with \(1\) of
\[\mu_q(1)=10^{q-2}1,\qquad \mu_q(0)=0^q.\]
A word is **unbordered** when no nonempty proper prefix equals a suffix. Write \(U_q(n)\) for the number of distinct unbordered length-\(n\) factors of \(C_q\). For every \(k\ge1\),
\[\boxed{U_q(q^k)=2^k.}\]
The theorem completely lists these factors. Put \(m=q^{k-1}\), \(A=\mu_q^{k-1}(1)\), and let \(\mathcal R=\{r:0\le r<m,\ A[r]=1\}\) in zero-based indexing. For each \(r\in\mathcal R\), define
\[T_r=A[r:m]\,0^{(q-1)m+r}.\]
Then the complete set of unbordered factors of length \(q^k\) is
\[\boxed{\{T_r:r\in\mathcal R\}\ \cup\ \{T_r^{\mathrm{rev}}:r\in\mathcal R\}.}\]
The two parts are disjoint and each has cardinality \(2^{k-1}\). In particular the exact power-scale law is \(U_q(q^k)=(q^k)^{\log_q2}\).

## Assumptions and scope

The alphabet is \(\{0,1\}\); \(q\) and \(k\) are integers with \(q\ge3\) and \(k\ge1\). A factor means a contiguous finite subword of the infinite one-sided fixed point. Borders are nonempty proper prefix–suffix coincidences. Words and substitutions are never considered modulo rotations. Powers \(0^j\) mean runs of exactly \(j\) zeros, with \(0^0\) empty. Substring \(A[r:m]\) uses zero-based half-open indices. The theorem makes no assertion about arbitrary nondilation lengths.

## Proof

**1. Iterates and symmetry.** Let \(W_j=\mu_q^j(1)\). Since \(\mu_q\) is uniform of length \(q\), \(|W_j|=q^j\), and the number of ones in \(W_j\) is \(2^j\), by induction. Furthermore,
\[W_{j+1}=W_j\,0^{(q-2)q^j}\,W_j.\]
As \(W_0=1\), every \(W_j\) is a palindrome and begins and ends in \(1\). Its length grows without bound and \(W_j\) is a prefix of \(W_{j+1}\); hence every factor of \(C_q\) is contained in some palindromic \(W_j\). Thus its reversal is also a factor of \(C_q\).

**2. Exhaustive candidates beginning in \(1\).** Fix \(n=q^k\) and \(m=q^{k-1}\). The fixed-point identity \(C_q=\mu_q^k(C_q)\) partitions \(C_q\) into consecutive length-\(n\) blocks, each either \(W_k\) or \(0^n\). Since \(q\ge3\), the word \(C_q\) contains no adjacent ones: both letter images lack adjacent ones, and each image ends in \(0\) or \(1\) with the next block starting in \(0\) or \(1\), while \(1\)-images are followed by an image of \(0\) because the preimage has no adjacent ones. Equivalently, the explicit recurrence for the positions of ones shows this directly by induction. Consequently each \(W_k\) block is followed by at least one \(0^n\) block.

A length-\(n\) factor beginning in \(1\) starts at a one-position \(p\) of a \(W_k\) block. If \(p=0\), the factor is \(W_k\), which starts and ends in \(1\), so it is bordered. If \(p>0\), the factor is exactly
\[V_p=W_k[p:n]0^p.\]
There are no other factors beginning in \(1\) at this length.

**3. First-copy positions are bordered.** By the displayed recursion,
\[W_k=A\,0^{(q-2)m}\,A.\]
Every one-position \(p\) lies in one of the two copies of \(A\). When \(1\le p<m\), the initial \(m\)-letter segment of \(V_p\) is \(A[p:m]0^p\), because \((q-2)m\ge p\). The terminal \(m\)-letter segment also equals \(A[p:m]0^p\), since the last \(m+p\) letters of \(V_p\) are \(A0^p\). Therefore \(V_p\) has a proper border of length \(m<n\).

**4. Second-copy positions are unbordered.** A one-position in the final copy of \(A\) has the form \(p=(q-1)m+r\), with \(r\in\mathcal R\). Substitution into \(V_p\) gives
\[V_p=T_r=A[r:m]0^{(q-1)m+r}.\]
This word begins in \(1\), ends in \(0\), and its last \(1\) appears at zero-based index \(t=m-r-1<m\). Suppose that \(T_r\) has a proper border of length \(n-d\), with \(1\le d<n\). Then \(d\) is a period, so \(T_r[d]=T_r[0]=1\); hence \(d\le t\). But also \(t+d<2m\le n\), and periodicity forces \(T_r[t+d]=T_r[t]=1\). This contradicts \(t\) being the last one. Therefore \(T_r\) is unbordered.

**5. All cases and distinctness.** Every unbordered binary word of length \(n\ge3\) must begin and end in different symbols, because equal endpoints give a border of length one. Steps 2–4 exhaust all candidates that begin in \(1\), and exactly the \(T_r\) survive. Reversal closure from Step 1 accounts for all candidates beginning in \(0\); they are precisely \(T_r^{\mathrm{rev}}\). Distinct \(r\) produce distinct numbers of ones: as \(r\) moves through consecutive one-positions of \(A\), the suffix \(A[r:m]\) loses one \(1\) at each step, taking all values from \(2^{k-1}\) to \(1\). Thus the \(2^{k-1}\) words \(T_r\) are distinct; their reversals are distinct as well, and the two classes are disjoint by their first letters. This proves the formula and exhaustive classification. \(\square\)

## Verification

The standalone `verify.py` constructs independent prefixes both through repeated substitution and by inspecting base-\(q\) digits of positions. It enumerates all distinct factors of the relevant lengths and tests absence of proper borders with the Knuth–Morris–Pratt prefix function. The predicted class list is constructed independently from the displayed formula and compared **as a set**, not merely as a count. The finite tests cover all pairs with \(3\le q\le7\), \(1\le k\le4\), and four further pairs \((3,5),(3,6),(4,5),(5,5)\). Output: `VERIFY_OK independent_digit_vs_substitution cases=24 complete_borders=yes`. The word-prefix lengths used for enumeration exceed the factor lengths by at least two substitution levels; the global proof, not the finite window, establishes completeness for every \(q,k\).

## Relationship to prior work

Charlier, Rampersad and Shallit [1] gave general automata-based decidability and enumeration for factors of automatic sequences, including unbordered factors, and explicit examples for Thue–Morse. Goč, Mousavi and Shallit [2] treated unbordered-factor counts of Thue–Morse and period-doubling-related sequences. These results give general methods and results for different words; they do not state the present classification or the exact generalized-Cantor power-scale count. Lü, Chen, Guo and Wen [3] study the *same Cantor-like substitution family*, but the studied invariants are ordinary factor and permutation complexity; their formulas do not imply unbordered-factor counts without further structural arguments. Overlap searches for unbordered/primitive/border-free formulations found no direct coverage among the inspected literature, but an equivalent differently indexed result remains possible.

## Limitations

The classification concerns only lengths exactly equal to a positive integer power of the substitution length. The value at length one is \(2\), outside the stated formula. There is no formula here for all remaining lengths or for altered substitutions. Finite verification is corroborative and not an infinite proof. Originality judgments are bounded by the literature and records inspected; no independent scientific audit has been performed.

## References

[1] É. Charlier, N. Rampersad and J. Shallit, *Enumeration and Decidable Properties of Automatic Sequences*, arXiv:1102.3698 (first submitted 2011-02-17), https://arxiv.org/abs/1102.3698 . Especially Theorem 2 and the enumeration examples in Section 9.

[2] D. Goč, H. Mousavi and J. Shallit, *On the Number of Unbordered Factors*, arXiv:1211.1301 (first submitted 2012-11-06), https://arxiv.org/abs/1211.1301 . Especially the main Thue–Morse theorem and Section 5.

[3] X.-T. Lü, J. Chen, Y.-J. Guo and Z.-X. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, https://doi.org/10.1016/j.tcs.2015.12.022 . Especially Sections 3–4.
