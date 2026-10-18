# Pseudo-Frobenius spectrum and Padovan type of shifted-Fibonacci numerical semigroups

## Finding
Let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). For every integer \(a\ge3\), set
\[S(a)=\langle F_a+F_j:j\ge0\rangle=\langle F_a,F_a+F_2,\ldots,F_a+F_{a-1}\rangle.\]
A subset \(I\subseteq\{2,\ldots,a-1\}\) is *independent* if no two indices differ by one and *dominating* if every index outside \(I\) is adjacent to one inside it. Let \(\mathcal I_a\) consist of the independent dominating subsets containing \(2\), together with the single extra set \(\{3,5,\ldots,a-1\}\) when \(a\) is even. Then the complete pseudo-Frobenius set is
\[\operatorname{PF}(S(a))=\left\{(|I|-1)F_a+\sum_{i\in I}F_i:I\in\mathcal I_a\right\}.\]
In particular, if \(P_1=P_2=P_3=1\) and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge4\), then the Cohen–Macaulay type (numerical-semigroup type) is
\[\boxed{\operatorname{type}(S(a))=P_{a-2}+\mathbf1_{2\mid a}}.\]
This determines every pseudo-Frobenius number, not only their count. The initial types for \(a=3,\ldots,12\) are \(1,2,1,3,2,4,4,6,7,10\).

## Assumptions and scope
The integer \(a\) is arbitrary with \(a\ge3\). The pseudo-Frobenius numbers of a numerical semigroup \(S\) are those integers \(z\notin S\) for which \(z+s\in S\) for every nonzero \(s\in S\). No primality, asymptotic, or independence assumption is made. The classification uses the Fibonacci indexing specified above. The value of the Padovan recurrence at \(n=1,2,3\) is part of the statement.

## Proof
Put \(m=F_a\). We use the published Zeckendorf Apéry description for this exact family: for \(0\le x<m\), the unique Apéry representative is \(w(x)=\beta(x)m+x\), where \(\beta(x)\) is the number of nonconsecutive Fibonacci summands in the Zeckendorf expansion of \(x\) [1, Theorem 4.6]. Consequently each \(x\) corresponds bijectively to an independent subset \(I\subseteq\{2,\ldots,a-1\}\), with \(x=\sum_{i\in I}F_i\) and \(\beta(x)=|I|\).

For completeness we explain the standard Apéry maximality test. A representative \(w(x)\) is maximal for the partial order \(u\preceq_S v\iff v-u\in S\) exactly when adding no nonmultiplicity minimal generator \(m+F_j\), \(2\le j<a\), yields another representative. If \(x+F_j<m\), this occurs exactly when \(\beta(x+F_j)=\beta(x)+1\). If \(x+F_j\ge m\), the equality would instead require \(\beta(x+F_j-m)=\beta(x)+2\), which is impossible by the finite Fibonacci coin-reduction lemma [1, Lemma 4.3]: from a representation of \(x+F_j\ge m\) using \(\beta(x)+1\) coins with indices below \(a\), one subtracts \(F_a\) and represents the remainder using strictly fewer coins. This applies regardless of whether the original representation is canonical.

It remains to characterize when adding a Fibonacci coin strictly raises the minimum coin count. If an independent set \(I\) is not dominating, an index \(j\) outside \(I\) has neither neighbor in \(I\). Inserting it gives another admissible Zeckendorf word below \(F_a\), with one additional summand; hence \(w(x)\) is not maximal.

Suppose now \(I=\{i_1<\cdots<i_t\}\) is independent and dominating. Its successive index gaps are \(2\) or \(3\), its first index is \(2\) or \(3\), and its last index is \(a-2\) or \(a-1\). For an unoccupied index \(j\), an adjacent occupied index allows \(F_j+F_{j+1}=F_{j+2}\), or \(F_{j-1}+F_j=F_{j+1}\), so adding \(F_j\) cannot raise the minimal coin count. For an occupied \(j\), use the elementary Fibonacci carry identities
\[2F_j=F_{j+1}+F_{j-2}\quad(j\ge4),\qquad 2F_3=F_4+F_2,\qquad2F_2=F_3.\]
Beginning with the doubled occupied coin, propagate the lower coin downward through occupied indices separated by gaps of two. If this meets a gap of three, \(F_{r-2}+F_{r-3}=F_{r-1}\) combines the carried coin with its next occupied predecessor, so the total coin count never increases. If the propagation reaches occupied index \(2\), the last identity reduces the count. Thus when \(2\in I\), no generator addition increases \(\beta\), proving maximality.

If instead \(i_1=3\), consider the initial chain \(3,5,7,\ldots,j\) of occupied indices separated only by gaps of two. If a later occupied index is \(j+3\), adding \(F_j\) propagates to the bottom and produces a genuine Zeckendorf representation with one extra summand: the affected chain becomes the nonconsecutive even-index sum \(F_2+F_4+\cdots+F_{j+1}\), together with the unaffected occupied indices above \(j\). The new indices are pairwise nonconsecutive because the next occupied index is \(j+3\); hence the coin count increases by exactly one, excluding this \(I\). If no such gap occurs and the top occupied index is \(a-2\), the same construction at \(j=a-2\) is a valid representation below \(F_a\), again excluding \(I\).

The sole remaining case is \(I=\{3,5,\ldots,a-1\}\), which is possible only for even \(a\). Here \(x=F_a-1\). Any attempted uppermost carry crosses \(F_a\) and cannot yield an Apéry successor; a carry begun lower down meets the next occupied coin and merges, so no addition below \(F_a\) increases \(\beta\). Thus this one further set is maximal. These cases exhaust all admissible Zeckendorf words. The usual identity \(\operatorname{PF}(S)=\{w-m:w\in\max_{\preceq_S}\operatorname{Ap}(S,m)\}\) proves the stated pseudo-Frobenius formula.

For the count, read a dominating independent binary word of length \(n=a-2\) from the highest to lowest index, imposing a final \(1\) (index \(2\) occupied). It begins with \(1\) or \(01\), and successive \(1\)'s are separated by a block \(01\) or \(001\). Thus the number is the sum of the numbers of compositions of \(n-1\) and \(n-2\) into parts \(2\) and \(3\). It equals \(P_n\) with \(P_1=P_2=P_3=1\), \(P_n=P_{n-2}+P_{n-3}\). There is exactly one additional alternating word for even \(a\), giving the asserted type formula.

## Verification
The standalone `verify.py` constructs the *actual* Apéry set using independent shortest paths on residues modulo \(F_a\), checks it against the Zeckendorf formula, and compares its maximal elements to the proposed sets. It successfully checked every integer \(3\le a\le19\) by exact arithmetic, including the pseudo-Frobenius values and recurrence. Run `python3 verify.py`. Finite checks confirm examples but do not replace the general proof.

## Relationship to prior work
Robles-Pérez and Rosales [1] identify the minimal generators and determine the Apéry set, Frobenius number, genus, and Wilf inequality for precisely \(S(a)\). Their work establishes the input Apéry theorem but does not give the maximal-element classification or pseudo-Frobenius/type formula. The familiar general Apéry characterization of pseudo-Frobenius numbers is standard numerical-semigroup theory [2], whereas the explicit dominating-Zeckendorf classification and Padovan count concern this particular family.

## Limitations
The proof uses the established Apéry formula and Fibonacci coin-reduction lemma from [1]. It does not establish an analogous classification for arbitrary shifted linear recurrences. External independent verification has not been performed, and unindexed overlapping work cannot be excluded solely by searches.

## References
[1] A. M. Robles-Pérez and J. C. Rosales, *The Extended Frobenius Problem for Fibonacci Sequences Incremented by a Fibonacci Number*, arXiv:2210.00816 (first submitted 2022-10-03), Mediterranean Journal of Mathematics 20, 222 (2023), DOI:10.1007/s00009-023-02428-9.

[2] J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*, Developments in Mathematics 20, Springer (2009), general Apéry-set and pseudo-Frobenius theory.
