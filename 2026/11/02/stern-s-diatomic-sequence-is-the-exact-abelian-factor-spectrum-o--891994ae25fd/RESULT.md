# Stern's diatomic sequence is the exact Abelian-factor spectrum of finite Zimin words

## Finding
Let \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\), with mutually distinct symbols. For \(n\ge1\), define \(p_n(\ell)\) as the number of distinct Parikh vectors among contiguous factors of \(Z_n\) of length \(\ell\). Define the Stern diatomic function \(s(0)=0\), \(s(1)=1\), \(s(2m)=s(m)\) for \(m\ge1\), and \(s(2m+1)=s(m)+s(m+1)\) for \(m\ge1\). Then, for every \(n\ge1\) and \(0\le\ell\le2^n-1\),
\[
p_n(\ell)=s(2^n-\ell).
\]
Here \(p_n(0)=1\) counts the empty factor. Consequently the number of distinct Parikh vectors of **all nonempty factors**, with factor lengths distinguished by their coordinate sums, is
\[
\sum_{\ell=1}^{2^n-1}p_n(\ell)=\frac{3^n-1}{2}.
\]
Writing Fibonacci numbers \(F_0=0,F_1=1,F_{m+2}=F_{m+1}+F_m\), the sharp maximum over nonempty factor lengths is
\[
\max_{1\le\ell\le2^n-1}p_n(\ell)=F_{n+1}.
\]
One attaining length is the Jacobsthal number \(J_n=(2^n-(-1)^n)/3\).

## Assumptions and scope
The alphabet contains exactly \(n\) distinct formal letters, with no homomorphic identifications. Factors are contiguous, not scattered, and Parikh vectors record every letter's multiplicity. The length domain is the complete range \(0\le\ell\le 2^n-1\); counts for larger lengths are zero. The empty length is used only in the recurrence.

## Proof
**Alternating projection.** Relabel \(a_2,\ldots,a_n\) in \(Z_{n-1}\) and call the resulting word \(B\). The exact decomposition is
\[
Z_n=a_1b_1a_1b_2a_1\cdots a_1b_{2^{n-1}-1}a_1,
\]
where \(B=b_1\cdots b_{2^{n-1}-1}\). In any length-\(2t\) factor, there are exactly \(t\) copies of \(a_1\) and its projected higher-letter word is a length-\(t\) factor of \(B\). Conversely every length-\(t\) factor of \(B\) appears between the adjacent \(a_1\)'s as such a factor. Projection preserves and reflects equality of Parikh vectors since the \(a_1\)-coordinate is fixed. Thus \(p_n(2t)=p_{n-1}(t)\) for \(1\le t\le2^{n-1}-1\).

A length-\(2t+1\) factor either begins and ends with \(a_1\), giving \(t+1\) occurrences of \(a_1\) and an arbitrary length-\(t\) higher-letter factor, or begins and ends with higher letters, giving \(t\) occurrences of \(a_1\) and an arbitrary length-\(t+1\) higher-letter factor. The two classes have different \(a_1\)-coordinates; all shorter projected factors occur. With \(p_{n-1}(0)=1\) and \(p_{n-1}(u)=0\) for \(u>2^{n-1}-1\), this proves
\[
p_n(2t+1)=p_{n-1}(t)+p_{n-1}(t+1)
\]
for \(0\le t\le2^{n-1}-1\). In addition \(p_n(0)=1\).

**Stern identification.** For \(n=1\), \(p_1(0)=p_1(1)=1=s(2)=s(1)\). Assume the displayed identity at rank \(n-1\), extending \(p_{n-1}\) by zero at length \(2^{n-1}\). The even recurrence matches \(s(2m)=s(m)\); the odd recurrence matches \(s(2m-1)=s(m-1)+s(m)\). The zero-length case matches \(s(2^n)=1\). Therefore \(p_n(\ell)=s(2^n-\ell)\) for every claimed length, including the final boundary \(\ell=2^n-1\).

**Total count.** Put \(A_n=\sum_{\ell=0}^{2^n-1}p_n(\ell)\). The even-length part has sum \(A_{n-1}\); the odd-length part has sum \(2A_{n-1}-1\), since \(p_{n-1}(0)=1\) and the out-of-range terminal value vanishes. Hence \(A_n=3A_{n-1}-1\) with \(A_1=2\), yielding \(A_n=(3^n+1)/2\). Subtract the empty factor.

**Sharp Fibonacci maximum.** Consider a Stern row \(R_m=(s(k))_{k=2^{m-1}}^{2^m}\), \(m\ge1\), and let \(M_m\) be its largest entry and \(T_m\) its largest sum of adjacent entries. Row \(R_{m+1}\) arises from \(R_m\) by inserting between every adjacent pair \((u,v)\) its sum \(u+v\). The row \(R_1=(1,1)\) has \(M_1=1=F_2\), \(T_1=2=F_3\), and the maximizing adjacent pair includes a maximizing entry. If a maximizing adjacent pair of \(R_m\) includes \(M_m\), then \(M_{m+1}=T_m\) (all entries are positive), and each new adjacent-pair sum has the form \(2u+v\) or \(u+2v\), at most \(T_m+M_m\). The old maximizing pair produces a new pair \((M_m,T_m)\) in one order, attaining \(T_m+M_m\), which includes the new maximum \(T_m\). Induction gives \(M_m=F_{m+1}\), \(T_m=F_{m+2}\). Since the complete Stern indices \(1,\ldots,2^n-1\) lie in these rows through \(R_n\), the upper bound is \(F_{n+1}\).

For sharpness put \(J_m=(2^m-(-1)^m)/3\). Its recurrence is \(J_{m+1}=2J_m+(-1)^m\) and \(J_m+J_{m+1}=2^m\). Let \(x_m=s(J_m)\) and \(h_m=s(J_m+(-1)^m)\). Stern's recurrence gives \((x_{m+1},h_{m+1})=(x_m+h_m,x_m)\) for \(m\ge2\), starting \((x_2,h_2)=(1,1)\). Consequently \(x_m=F_m\). Since \(2^n-J_n=J_{n+1}\), \(p_n(J_n)=s(J_{n+1})=F_{n+1}\), for \(n\ge2\). The case \(n=1\) is immediate.

## Verification
Run `python3 checker.py` from this package. The independent sliding-window Parikh-vector enumeration is compared against Stern values for all lengths at ranks \(1\) through \(9\). It also checks the total and maximum formulas and the Jacobsthal witness. This finite enumeration is a reproducibility check; the preceding arguments prove all ranks.

## Relationship to prior work
Zimin words and their ruler-word description are classical; Cooper and Rorabaugh (2014), *Bounds on Zimin Word Avoidance*, explicitly give the recursive definition and \(2\)-adic letter formula. De Luca and De Luca (2014), *Sturmian words and the Stern sequence*, study Stern values through Christoffel-word lengths and discuss the ruler sequence, without asserting the Parikh-profile identity for finite Zimin factors in the inspected text. The Fibonacci extremum of Stern rows is classical, so novelty is claimed for the **precise Abelian-spectrum identification and its word-combinatorial implications**, not for Stern's standalone recurrence or its maximum.

## Limitations
This is not a classification of multiplicities of factors within each Parikh class, nor a \(2\)-Abelian complexity formula, and does not extend automatically to identified-letter images or prefixes other than complete Zimin words. Bibliographic priority cannot be proven by search alone; related papers outside the inspected corpus may contain equivalent results. Independent mathematical audit has not been performed.

## References
1. J. Cooper and D. Rorabaugh, *Bounds on Zimin Word Avoidance*, arXiv:1409.3080, first posted 2014-09-10. https://arxiv.org/abs/1409.3080
2. A. de Luca and A. De Luca, *Sturmian words and the Stern sequence*, arXiv:1410.4085, first posted 2014-10-15. https://arxiv.org/abs/1410.4085
3. C. Defant, *Upper Bounds for Stern's Diatomic Sequence and Related Sequences*, Electronic Journal of Combinatorics 23(4), 2016, #P4.8. DOI:10.37236/5342 (2016-10-14).
