# An infinite family of five-term Lucas–Niven arithmetic progressions

## Finding
For each integer \(m\ge0\), set \(j=13+24m\), \(N=L_j+23\), with the Lucas numbers \(L_0=2\), \(L_1=1\), and \(L_{r+2}=L_{r+1}+L_r\). Then all five terms
\[
N,\quad N+2,\quad N+4,\quad N+6,\quad N+8
\]
are Lucas–Niven integers. Their Lucas summand counts, in the same order, are precisely \(4,3,4,2,3\). In particular, these give infinitely many pairwise distinct length-five progressions with common difference two.

## Assumptions and scope
A legal Lucas decomposition of a positive integer \(n\) is a representation \(n=\sum_{r\ge0}\lambda_r L_r\), with \(\lambda_r\in\{0,1\}\), \(\lambda_r+\lambda_{r+1}\le1\) for all \(r\), and \(\lambda_0+\lambda_2\le1\). The Lucas decomposition theorem gives its uniqueness; define \(s_L(n)=\sum_r\lambda_r\). Say \(n\) is Lucas–Niven when \(s_L(n)\mid n\). The claim concerns every nonnegative integer \(m\), without probabilistic or asymptotic qualifications. It makes no claim about maximal possible Lucas–Niven run lengths.

## Proof
The initial Lucas numbers are \(L_0=2\), \(L_1=1\), \(L_3=4\), \(L_4=7\), \(L_6=18\), and \(L_7=29\). For any \(j\ge13\), the following five sums are all legal Lucas decompositions:
\[
\begin{aligned}
L_j+23&=L_j+L_6+L_3+L_1,\\
L_j+25&=L_j+L_6+L_4,\\
L_j+27&=L_j+L_6+L_4+L_0,\\
L_j+29&=L_j+L_7,\\
L_j+31&=L_j+L_7+L_0.
\end{aligned}
\]
Indeed, the indices in each expression are distinct and pairwise nonadjacent, and no displayed representation simultaneously uses indices \(0\) and \(2\). The distance from the high index \(j\ge13\) to every lower displayed index is at least six. The Lucas decomposition theorem therefore makes these the canonical decompositions, yielding the exact digit-sum profile \((4,3,4,2,3)\).

The recurrence yields \(L_{13}=521\), \(L_{24}=103682\), and \(L_{25}=167761\). Thus
\[
(L_{24},L_{25})\equiv(2,1)=(L_0,L_1)\pmod{12}.
\]
By forward induction using the recurrence, \(L_{r+24}\equiv L_r\pmod{12}\) for every \(r\ge0\). Hence \(L_{13+24m}\equiv L_{13}=521\equiv5\pmod{12}\). In the five displayed integers the remainders of the offsets \(23,25,27,29,31\) give
\[
\begin{aligned}
L_j+23&\equiv0\pmod4,\\
L_j+25&\equiv0\pmod3,\\
L_j+27&\equiv0\pmod4,\\
L_j+29&\equiv0\pmod2,\\
L_j+31&\equiv0\pmod3.
\end{aligned}
\]
These moduli are exactly the canonical summand counts. Therefore all five are Lucas–Niven. Finally, \(L_j\) is strictly increasing for \(j\ge1\), so the starting values \(L_{13+24m}+23\) are distinct and unbounded. This proves infinitude.

## Verification
The finite recurrence checks \(L_{13}=521\), \(L_{24}=103682\), \(L_{25}=167761\), together with the five displayed legal decompositions, suffice for the unrestricted proof by recurrence induction. In particular, the initial progression is \(544,546,548,550,552\); its Lucas summand counts are \(4,3,4,2,3\). The accompanying `verify.py` reconstructs these exact recurrences and decompositions and checks several generated instances, but no finite range substitutes for the recurrence argument.

## Relationship to prior work
Lao, Miller, Rosa, Shiliaev, Tresch, Wong, and Zhang (arXiv:2606.24006v1, June 22, 2026) prove that Lucas–Niven numbers occur infinitely often in each arithmetic progression. Their length-five construction in Section 4, however, concerns **Zeckendorf–Niven**, not Lucas–Niven, numbers. Their Section 3 treats individual Lucas–Niven terms in progressions; its existence result does not itself enforce five successive qualifying terms in the same progression. The present explicit Lucas construction exploits Lucas-index legal decompositions and a modulo-12 recurrence to supply the simultaneous five-term pattern. This comparison does not establish exhaustive historical priority.

## Limitations
No claim is made that five is the largest achievable run length, that the displayed family contains every five-term Lucas–Niven progression, or that an independent originality assessment has been completed. The general uniqueness of Lucas decomposition is invoked as a published theorem. The modular proof itself is elementary and self-contained after that theorem.

## References
1. K. Lao, S. J. Miller, N. Rosa, M. Shiliaev, G. Tresch, T. W. H. Wong, and H. Zhang, *On Zeckendorf-Niven numbers and arithmetic progressions*, arXiv:2606.24006v1 (first posted 2026-06-22), Theorems 1.2, 4.3, 4.4 and Sections 2–5. https://arxiv.org/abs/2606.24006
2. The classical Lucas decomposition theorem, as formulated in Theorem 1.2 of reference 1.
