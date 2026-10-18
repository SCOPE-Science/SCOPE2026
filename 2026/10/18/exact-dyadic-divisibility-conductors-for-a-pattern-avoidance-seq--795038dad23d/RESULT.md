# Exact dyadic divisibility conductors for a pattern-avoidance sequence

## Finding
Let \(a_n\) count permutations of \(\{1,\ldots,n\}\) avoiding both classical patterns \(1342\) and \(2143\), with \(a_0=1\). For every integer \(r\ge1\), define its **dyadic divisibility conductor** by
\[
L(r)=\min\{N\ge0:2^r\mid a_n\text{ for every }n\ge N\}.
\]
Write \(s_2(k)\) for the number of ones in the binary expansion of a nonnegative integer, and put
\[
K(r)=\max\{k\in\{1,\ldots,r\}: k+s_2(k)\le r+1\}.
\]
The maximum exists, and the exact conductor is
\[
\boxed{L(r)=3K(r)-1.}
\]
Equivalently, if \(d_r\) is the least integer \(d\ge0\) such that \(s_2(r-d)\le d+1\), then \(L(r)=3(r-d_r)-1\). The search needs at most \(\lfloor\log_2 r\rfloor+1\) candidate values of \(d\). In particular,
\[
\boxed{L(r)\le 3r-1,\qquad L(r)=3r-1\iff r\text{ is a power of }2.}
\]
The same theorem resolves the four-residue avoidance question stated as Open Question 3.25 by Rowland and Yassawi: for all \(r\ge6\), all \(n\ge0\), and each \(c\in\{1,2,6,22\}\),
\[
a_n\not\equiv 2^{r-1}+c\pmod{2^r}.
\]

## Assumptions and scope
All variables \(n\) and \(r\) are integers with \(n\ge0\) and \(r\ge1\). Pattern avoidance refers to subsequences with the same relative order, not necessarily adjacent positions. Congruences are ordinary integer congruences. The conductor describes eventual divisibility uniformly for all indices beyond its threshold; it is not the first divisible index. The assertion about the four residues is a corollary of the conductor theorem plus a fixed finite calculation, not a general claim that every other residue occurs.

## Proof
Let \(F(x)=\sum_{n\ge0}a_nx^n\). The established generating-function equation for this enumeration is
\[
2x(x-1)F(x)^2+F(x)+x-1=0,
\]
with \(F(0)=1\). Rearranging and writing \(H(x)=F(x)/(1-x)\) gives \(H(x)=1+2x(1-x)^2H(x)^2\). The unique formal-power-series solution of \(C(z)=1+zC(z)^2\), with \(C(0)=1\), is the Catalan series \(C(z)=\sum_{j\ge0}C_jz^j\), where \(C_j=\binom{2j}{j}/(j+1)\). Consequently
\[
F(x)=(1-x)C\bigl(2x(1-x)^2\bigr)
    =\sum_{j\ge0}2^jC_jx^j(1-x)^{2j+1}.\tag{1}
\]
The identity is also recorded in the OEIS entry for this sequence; the argument below evaluates a different invariant from it.

The elementary factorial valuation identity \(\nu_2(m!)=m-s_2(m)\) yields \(\nu_2\bigl(\binom{2j}{j}\bigr)=s_2(j)\). Since incrementing \(j\) by one changes the binary weight by \(1-\nu_2(j+1)\),
\[
\nu_2(C_j)=s_2(j)-\nu_2(j+1)=s_2(j+1)-1.\tag{2}
\]
Fix \(r\ge1\). By (2), the entire polynomial \(2^jC_jx^j(1-x)^{2j+1}\) vanishes coefficientwise modulo \(2^r\) precisely when
\[
j+s_2(j+1)-1\ge r.
\]
Equivalently, the surviving indices \(j=k-1\) are those with \(k+s_2(k)\le r+1\). All such \(k\) lie in \(\{1,\ldots,r\}\), and \(k=1\) always survives. Let \(k_*=K(r)\), and put \(j_*=k_*-1\). Modulo \(2^r\), (1) is a finite polynomial of degree at most \(3j_*+1=3k_*-2\). Its coefficient of \(x^{3k_*-2}\) comes **only** from the highest surviving summand, because every lower summand has smaller degree. That coefficient is \(-2^{j_*}C_{j_*}\), which is nonzero modulo \(2^r\) by the definition of survival. Thus \(2^r\mid a_n\) for every \(n\ge3k_*-1\), whereas \(2^r\nmid a_{3k_*-2}\), proving \(L(r)=3k_*-1\) with exactness at the boundary.

For the sharp upper bound, \(s_2(k)\ge1\) for \(k\ge1\), so the survival condition forces \(k\le r\). Equality \(K(r)=r\) holds exactly when \(s_2(r)=1\), or equivalently when \(r\) is a power of two. For the alternate short calculation, put \(d=r-k\). The survival condition becomes \(s_2(r-d)\le d+1\). A solution exists among \(0\le d\le\lfloor\log_2r\rfloor\), since the binary weight of every positive integer at most \(r\) is at most \(\lfloor\log_2r\rfloor+1\).

Finally, (1) reduced modulo \(32\) retains only \(j=0,1,2,3,4\). Its coefficient residues for \(n=0,\ldots,10\) are, in order,
\[
1,1,2,6,22,24,16,16,24,24,24\pmod{32},
\]
with all later coefficients zero modulo \(32\), since \(L(5)=11\). Thus \(a_n\pmod{32}\) never belongs to \(\{1,2,6,22\}\) when \(n\ge5\). For \(n\le4\), the exact integers are \(1,1,2,6,22\), all less than \(32\). If \(r\ge6\), every prohibited class \(2^{r-1}+c\pmod{2^r}\) reduces to \(c\pmod{32}\); for \(n\le4\), the value \(a_n\) is strictly below \(2^{r-1}\). Neither range can contain a prohibited class. This proves the stated corollary for all \(r,n\).

## Verification
The accompanying standalone script `verify.py` constructs the coefficients independently from the quadratic equation and the Catalan expansion, comparing \(156\) exact integer coefficients. It checks the binary-weight valuation identity through \(140\) Catalan indices; tests the conductor and its sharpness for \(1\le r\le49\); and checks the four avoided residues for \(6\le r\le39\). Run `python3 verify.py`; successful execution prints `VERIFY_OK`. The script is a finite consistency test, not a replacement for the preceding infinite proof. For orientation, the first sixteen conductors are \(2,5,5,11,11,14,17,23,23,26,29,29,35,35,38,47\).

## Relationship to prior work
Le (2005) established the enumeration and its generating function. The OEIS record A109033 includes Barry's December 2008 Catalan-substitution expression (1), which is acknowledged rather than presented as new. Rowland and Yassawi (2015, Example 3.24) used automata to give several forbidden residue classes for this sequence; their Open Question 3.25 asks for the uniform four-class avoidance just proved. Neither statement cited here gives the exact all-precision conductor or its binary-weight sharpness criterion. The result evaluates that invariant from the earlier generating series. A more general published result not found in the available searches could cover it, and the elementary nature of the derivation limits claims of methodological novelty.

## Limitations
The formula identifies the last index not divisible by \(2^r\), not the full distribution of all earlier residues or the exact valuation at every individual index. It proves no assertions about odd-prime powers. The algebraic generating function and Catalan transform are prior literature, not new mathematical content. Independent expert assessment and an exhaustive literature survey have not been performed. The inaccessible full text of the initial 2005 enumeration paper leaves some residual coverage risk, although the later primary full-text source explicitly poses the congruence question as open.

## References
1. I. Le, *Wilf Classes of Pairs of Permutations of Length 4*, Electronic Journal of Combinatorics 12 (2005), R25, DOI: 10.37236/1922; published 2005-05-26.
2. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, Journal de Théorie des Nombres de Bordeaux 27 (2015), 245–288, DOI: 10.5802/jtnb.901; see Example 3.24 and Open Question 3.25. Preprint arXiv:1310.8635 first submitted 2013-10-31.
3. OEIS Foundation, entry A109033, *Number of permutations in \(S_n\) avoiding the patterns 1342 and 2143*, including P. Barry's generating-function identity dated 2008-12-15, https://oeis.org/A109033.
4. E. Rowland and D. Zeilberger, *A Case Study in Meta-AUTOMATION: AUTOMATIC Generation of Congruence AUTOMATA For Combinatorial Sequences*, arXiv:1311.4776 (2013); broader congruence-automaton context.
