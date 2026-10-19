# Complete period census of generalized Arnold cat maps modulo powers of three

## Finding
Fix an integer \(e\ge1\), put \(N=3^e\), and take each parameter pair \((p,q)\) from the ring \(R_e=\mathbb Z/N\mathbb Z\). The generalized discrete cat map acts on \(R_e^2\) by the matrix
\[
A_{p,q}=\begin{pmatrix}1&p\\q&1+pq\end{pmatrix}.
\]
Let \(T(p,q)\) be its **global period**, the least positive integer for which \(A_{p,q}^{T(p,q)}=I\pmod N\); equivalently, every state is restored after this many steps. Because \(\det A_{p,q}=1\), the period always exists. All \(N^2\) parameter choices are counted separately.

Define the truncated ternary valuation by \(v_e(z)=\max\{s\in\{0,\ldots,e\}:z\equiv0\pmod{3^s}\}\). In particular \(v_e(0)=e\), and a unit has valuation zero. The parameters fall into exactly one of these four types, each with \(1\le s\le e\):

| Condition on \((p,q)\) | \(r\) | \(s\) | Global period |
| :--- | ---: | :--- | :--- |
| Both \(p,q\) divisible by three | 1 | \(\min(v_e(p),v_e(q))\) | \(r3^{e-s}\) |
| Exactly one of \(p,q\) a unit modulo three | 3 | \(v_e(pq+3)\) | \(r3^{e-s}\) |
| \(pq\equiv1\pmod3\) | 4 | \(v_e(pq+2)\) | \(r3^{e-s}\) |
| \(pq\equiv2\pmod3\) | 6 | \(v_e(pq+1)\) | \(r3^{e-s}\) |

Here \(r\) is also the exact order of \(A_{p,q}\) modulo three. The **complete exact joint period-class census** is
\[
\begin{aligned}
&\#\{(p,q):(r,s)=(1,e)\}=1,\\
&\#\{(p,q):(r,s)=(1,s)\}=8\cdot3^{2e-2s-2}&& (1\le s<e),\\
&\#\{(p,q):(r,s)=(3,e)\}=4\cdot3^{e-1},\\
&\#\{(p,q):(r,s)=(3,s)\}=8\cdot3^{2e-s-2}&& (1\le s<e),\\
&\#\{(p,q):(r,s)=(r_0,e)\}=2\cdot3^{e-1}&& (r_0\in\{4,6\}),\\
&\#\{(p,q):(r,s)=(r_0,s)\}=4\cdot3^{2e-s-2}&& (r_0\in\{4,6\},\;1\le s<e).
\end{aligned}
\]
Every listed class is nonempty and their total is \(3^{2e}\). Summing entries that give the same integer \(r3^{e-s}\) yields the complete ordinary period histogram, including the overlap between the \(r=1\) and \(r=3\) families. In particular the distinct period values are precisely
\[
\{1\}\cup\{3^j:1\le j\le e\}\cup\{4\cdot3^j,6\cdot3^j:0\le j<e\}.
\]
The maximum period is \(2N\), achieved by precisely two pairs for \(e=1\) and by \(4\cdot3^{2e-3}\) pairs for every \(e\ge2\). Thus the fraction of maximal-period parameter choices is exactly \(4/27\) for every \(e\ge2\), independent of the exponent.

## Assumptions and scope
All congruences and divisions by units are in the finite ring \(R_e\). Both parameters range without restrictions through all \(N\) residues. The period belongs to the whole finite-state permutation, **not** to an arbitrarily selected point or only to the orbit of the origin. This theorem covers every integer exponent \(e\ge1\), hence particularly the nonprime powers \(3^e\) with \(e>1\). Its primary classification is MSC2020 37P35.

## Proof
**1. The reduction modulo three and the four base orders.** Write \(x=pq\) and \(A=A_{p,q}\). Its determinant is one and its trace is \(2+x\), so Cayley–Hamilton gives
\[
A^2=(2+x)A-I.\tag{1}
\]
If both parameters vanish modulo three, then \(A\equiv I\pmod3\), of exact order \(r=1\). If exactly one parameter is a unit modulo three, then \(x\equiv0\) and \(A\pmod3\) is a nonidentity unipotent matrix, of exact order \(r=3\). If \(x\equiv1\pmod3\), (1) gives \(A^2\equiv-I\pmod3\) and hence \(r=4\). Finally, if \(x\equiv2\pmod3\), then \(A\) is a nonscalar matrix with characteristic polynomial \((z+1)^2\) modulo three; its negative is a nonidentity unipotent, giving exact order \(r=6\). In every class \(A^r\equiv I\pmod3\).

**2. Exact matrix lifting at the odd prime three.** For any integer matrix \(B\equiv I\pmod3\), put \(s=\min\{e,\min_{i,j}v_e((B-I)_{ij})\}\). If \(s<e\), write \(B=I+3^sC\), where at least one entry of \(C\) is a ternary unit. In the integer binomial expansion
\[
B^3-I=3^{s+1}C+3^{2s+1}C^2+3^{3s}C^3,
\]
the last two terms are divisible by \(3^{s+2}\), since \(s\ge1\). Thus \(v_3(B^3-I)=s+1\), interpreted entrywise as the least valuation; the leading unit entry cannot cancel. By induction \(v_3(B^{3^k}-I)=s+k\) until saturation at exponent \(e\). Raising \(I+3^sC\) to any positive exponent prime to three preserves the valuation \(s\), by the same first-order binomial argument. Every exponent making \(A^t\equiv I\pmod3\) is divisible by \(r\), so applying the lemma to \(B=A^r\) proves
\[
T(p,q)=r3^{e-s},\qquad s=v_e(A^r-I).\tag{2}
\]
Here \(v_e\) of a matrix is the minimum of its entry valuations.

**3. The four exact valuation identities.** For \(r=1\),
\[
A-I=\begin{pmatrix}0&p\\q&pq\end{pmatrix};
\]
hence \(s=\min(v_e(p),v_e(q))\). For \(r=3\), use (1) to obtain
\[
A^3-I=(x+3)[(x+1)A-I].\tag{3}
\]
When exactly one of \(p,q\) is a unit, the bracket has a unit off-diagonal entry. Hence \(s=v_e(x+3)\). For \(r=4\), (1) yields
\[
A^2+I=(x+2)A,\qquad A^4-I=(x+2)A(A^2-I).\tag{4}
\]
Both \(A\) and \(A^2-I\) are invertible modulo three in this class (indeed \(A^2\equiv-I\)), so \(s=v_e(x+2)\). For \(r=6\), similarly
\[
A^3+I=(x+1)[(x+3)A-I],\tag{5}
\]
and \(A^6-I=(A^3+I)(A^3-I)\). The matrix \(A^3-I\) is invertible modulo three because \(A^3\equiv-I\), while the bracket in (5) has a unit off-diagonal entry because both \(p,q\) are units and \(x+3\) is a unit. Consequently \(s=v_e(x+1)\). Multiplication by a matrix invertible modulo three does not change the minimum entrywise valuation. This proves (2) with the asserted four cases, including all limiting \(s=e\) cases.

**4. Parameter counting, without probabilistic assumptions.** When both \(p,q\) are divisible by three, the number with \(\min(v_e(p),v_e(q))\ge s\) equals \(3^{2(e-s)}\). Thus exactly one pair has \(s=e\), and for each \(1\le s<e\) the difference
\[
3^{2(e-s)}-3^{2(e-s-1)}=8\cdot3^{2e-2s-2}
\]
counts the rest. In the \(r=3\) class, for every fixed product \(x\equiv0\pmod3\), exactly \(2\varphi(3^e)=4\cdot3^{e-1}\) ordered parameter pairs have \(pq=x\) with one unit: choose either \(p\) or \(q\) to be a unit, choose its value freely, and determine the other. The number of products with \(v_e(x+3)=s\) is one if \(s=e\), or \(2\cdot3^{e-s-1}\) if \(1\le s<e\). Multiplication gives the \(r=3\) counts. For each of the \(r=4\) and \(r=6\) classes, a fixed product \(x\) is a unit and admits exactly \(\varphi(3^e)=2\cdot3^{e-1}\) factor pairs; the number of products having \(v_e(x+2)=s\) or \(v_e(x+1)=s\), respectively, has exactly the same one-or-\(2\cdot3^{e-s-1}\) structure. This gives the final two rows of the census. All four cases partition \(R_e^2\); hence their counts sum to \(N^2\).

**5. Maximum and possible periods.** Each valuation depth from one through \(e\) occurs in all classes. The possible \(r3^{e-s}\) values therefore give the three listed families plus the identity. The largest is \(6\cdot3^{e-1}=2N\), occurring exactly in the \(r=6,s=1\) class. Its count is two when \(e=1\) and \(4\cdot3^{2e-3}\) when \(e\ge2\), yielding the constant fraction \(4/27\) after division by \(N^2=3^{2e}\).

## Verification
The self-contained accompanying `verify.py` independently forms every matrix \(A_{p,q}\) for every parameter pair modulo \(3^e\), with \(e=1,2,3,4\). It computes the actual matrix order by multiplication, compares it with the valuation rule, and checks every \((r,s)\) class size against its exact formula. The script prints `VERIFY_OK` only if all comparisons pass; it was executed successfully. In particular, for \(N=9\), the actual periods have counts \(1:1\), \(3:20\), \(4:6\), \(6:6\), \(9:24\), \(12:12\), \(18:12\). For \(N=27\), the corresponding counts are \(1:1\), \(3:44\), \(4:18\), \(6:18\), \(9:144\), \(12:36\), \(18:36\), \(27:216\), \(36:108\), \(54:108\). These finite checks do not assert an exhaustive computation for all exponents: the infinite assertion is established in the proof by exact lifting and counting.

## Relationship to prior work
Chen, Wong, Liao and Xiang's 2014 primary article uses this identical two-parameter matrix and defines period through restoration of every state. Its Section 5 explicitly identifies the nonprime powers \(N=3^e\) as the outstanding case left for future work. Their 2012 prime-power article states the hypothesis \(p>3\) in its abstract (there \(p\) is the prime modulus, not our matrix parameter); their 2013 study handles powers of two. The 2014 article determines the prime-modulus case, which supplies only the first ternary level and does not imply the lifting counts above. Bao and Yang's 2012 paper addresses individual periods and some formulae, but its accessible abstract does not assert the full \(3^e\) parameter census; its full text could not be inspected, leaving priority uncertainty. Nance's 2011 public preprint treats the single classical parameter choice, not the family-wide histogram. The mathematical novelty assessed here is **the exact all-exponent ternary parameter census and constant maximizer fraction**, not the existence of cat-map periods or the general concept of prime-power lifting.

## Limitations
The claim concerns a very specific two-parameter determinant-one matrix family over powers of three. No statement is made about the numbers of phase-space orbits of each pointwise length, nonlinear perturbations, or arbitrary determinant-one matrices. A relevant earlier restricted article may contain a stronger unpublished-to-us table; searches cannot establish absolute historical priority. The supporting 2012 prime-power and Bao–Yang articles were inspected through accessible abstracts rather than full text. No independent mathematical audit has occurred.

## References
1. J. Nance, *Periods of the discretized Arnold's Cat Mapping and its extension to n dimensions*, arXiv:1111.2984v1 (first publicly posted 2011-11-13). https://arxiv.org/abs/1111.2984 . This supplies a dated early study of the fixed classical cat map, not the present two-parameter census.
2. F. Chen, K.-W. Wong, X. Liao and T. Xiang, *Period Distribution of Generalized Discrete Arnold Cat Map for \(N=p^e\)*, IEEE Trans. Inf. Theory (2012), DOI:10.1109/TIT.2011.2171534; its abstract restricts the prime to \(p>3\).
3. J. Bao and Q. Yang, *Period of the discrete Arnold cat map and general cat map*, Nonlinear Dynamics 70 (2012), 1365–1375, DOI:10.1007/s11071-012-0539-3.
4. F. Chen, K.-W. Wong, X. Liao and T. Xiang, *Period distribution of generalized discrete Arnold cat map*, Theoretical Computer Science 552 (2014), 13–25, DOI:10.1016/j.tcs.2014.08.002. The identical matrix occurs in Definition 1 and the specific remaining case is stated in Section 5.
