# Exact preperiod census for the dyadic quadratic Dickson map

## Finding

Let \(f(x)=x^2-2=D_2(x,1)\), considered modulo \(2^k\). For every integer \(k\ge1\), its entire finite functional graph consists of two fixed points, the odd residue \(-1\) and even residue \(2\), with all odd and all even inputs, respectively, eventually reaching those fixed points. The theorem below gives both the **least arrival time of each residue** and the **exact number of residues at each arrival time**. In particular, the tail-depth asymmetry of the two basins is explicit at every modulus.

Write \(v(z)=v_2(z)\), with \(v(0)=+\infty\). Let \(T_k(x)\) denote the least \(t\ge0\) such that \(f^{\circ t}(x)\equiv-1\pmod{2^k}\) for odd \(x\), or \(f^{\circ t}(x)\equiv2\pmod{2^k}\) for even \(x\).

For \(k\ge3\) the pointwise law is
\[
T_k(x)=\begin{cases}
0,&x\equiv-1\pmod{2^k},\\
1+\max\{0,k-v(x^2-1)\},&x\text{ odd, not fixed},\\
0,&x\equiv2\pmod{2^k},\\
1+\max\{0,\lceil(k-v(x^2-4))/2\rceil\},&x\equiv2\pmod4,\ x\not\equiv2\pmod{2^k},\\
\max\{2,2+\lfloor(k-1)/2\rfloor-v(x)\},&x\equiv0\pmod4.
\end{cases}
\]
For \(k=1\), both parity classes are fixed. For \(k=2\), the two fixed classes \(-1\) and \(2\) each have one other input of arrival time one.

Let \(O_k(t)\) and \(E_k(t)\) count the odd and even residues with \(T_k(x)=t\), respectively. For \(k\ge3\),
\[
O_k(0)=1,\qquad O_k(1)=3,\qquad O_k(t)=2^t\ (2\le t\le k-2),
\]
with all other odd counts zero. For the even basin, the histograms for \(k=3\) and \(k=4\) are, in increasing time order, \((1,1,2)\) and \((1,3,4)\). For every \(k\ge5\), put \(L=\lfloor(k-1)/2\rfloor\), and define
\[
A_k(s)=\begin{cases}2^{k-2},&s\le5,\\2^{k-s+3},&6\le s\le k,\\0,&s>k,\end{cases}
\qquad
B_k(t)=\begin{cases}2^{k-\max(2,L)},&t=2,\\2^{k-L-3+t},&3\le t\le L,\\0,&\text{otherwise}.\end{cases}
\]
Then
\[
E_k(0)=1,\quad E_k(1)=7,\quad
E_k(t)=A_k(k-2t+2)-A_k(k-2t+4)+B_k(t)\quad(t\ge2).
\]
These expressions vanish for sufficiently large \(t\). They sum to \(2^{k-1}\) separately within both parities. For example, for \(k=8\), the odd histogram is \((1,3,4,8,16,32,64)\) and the even histogram is \((1,7,56,64)\). In particular, the maximum transient is exactly \(k-2\) for \(k\ge4\); the maximum even transient is at most \(\max\{2,\lfloor(k-1)/2\rfloor\}\).

## Assumptions and scope

The theorem concerns **every** modulus \(2^k\), not merely samples or an asymptotic density. Inputs are residue classes, represented by any integer. The valuation formulas are invariant under changing representatives because each valuation is used only up to the required modulus. The infinity convention makes a zero difference behave as a valuation exceeding every finite threshold. The map is monic Dickson \(D_2(x,1)\); it is not assumed to be conjugate over \(\mathbb Z/2^k\mathbb Z\) to the standard real-normalized Chebyshev map through division by two.

## Proof

**Attracting points.** The congruences \(f(-1)=-1\), \(f(2)=2\) hold integrally, and \(f(x)\equiv x\pmod2\). Thus parity is invariant. The valuations proved next show that every point eventually reaches the corresponding fixed point, excluding any additional cycles.

**Odd valuations and arrival time.** For odd \(x\), \(f(x)+1=x^2-1\) is divisible by eight. If \(y\equiv-1\pmod8\), then \(v(y-1)=1\) and
\[
v(f(y)+1)=v(y^2-1)=v(y+1)+1.
\]
Starting with \(y=f(x)\), its distance valuation to \(-1\) increases **exactly by one** until it reaches \(k\). If \(x\not\equiv-1\pmod{2^k}\), this requires one initial step followed by \(\max\{0,k-v(x^2-1)\}\) steps, proving the odd pointwise formula.

For \(s\ge3\), exactly four classes solve \(x^2\equiv1\pmod{2^s}\); for \(3\le s<k\), exactly \(2^{k-s+1}\) odd classes modulo \(2^k\) have \(v(x^2-1)=s\). (Indeed, the congruence modulo \(2^s\) has four roots, with \(2^{k-s}\) lifts each; subtract the roots modulo \(2^{s+1}\) to count exact valuations.) Among the four square roots of one modulo \(2^k\), one is the fixed class \(-1\) and three have time one. Substituting \(t=1+k-s\) gives \(O_k(0)=1\), \(O_k(1)=3\), and \(O_k(t)=2^t\) for \(2\le t\le k-2\).

**Even valuations and arrival time.** Factor
\[
f(x)-2=(x-2)(x+2),\qquad f(x)+2=x^2.
\]
If \(x\equiv2\pmod4\), then \(f(x)\equiv2\pmod4\), and every subsequent point \(y\equiv2\pmod4\) has \(v(y+2)=2\). Therefore each further iteration adds exactly two to \(v(y-2)\), establishing the formula using \(v(x^2-4)\). If \(x\equiv0\pmod4\), then \(v(f(x)-2)=2\) and \(v(f(x)+2)=2v(x)\); hence \(v(f^{\circ2}(x)-2)=2+2v(x)\). Thereafter the valuation increases by two per iterate. This gives \(\max\{2,2+\lfloor(k-1)/2\rfloor-v(x)\}\). The case \(x=0\) has time two for \(k\ge3\). Direct inspection handles \(k=1,2\).

**Even histogram.** For \(k\ge5\), the \(x\equiv2\pmod4\) class has \(2^{k-2}\) elements. Writing \(x=2+4m\) yields \(x^2-4=16m(m+1)\). For \(s\ge6\), the condition \(v(x^2-4)\ge s\) is equivalent to \(m\equiv0\) or \(-1\pmod{2^{s-4}}\), giving \(2^{k-s+3}\) residue classes for \(s\le k\). Every element has valuation at least five, giving \(A_k(s)\) as above. Of the eight classes with valuation at least \(k\), one is fixed and seven have time one. At time \(t\ge2\) the count in this class is the valuation-window difference \(A_k(k-2t+2)-A_k(k-2t+4)\).

For \(x\equiv0\pmod4\), put \(r=v(x)\). Its time is \(\max\{2,2+L-r\}\), and there are \(2^{k-r-1}\) classes with each exact \(2\le r<k\), together with the zero class. Thus the number at time two is \(2^{k-\max(2,L)}\), and for \(3\le t\le L\) it is \(2^{k-L-3+t}\). This proves \(B_k\) and the complete even histogram. A direct four- and eight-class enumeration settles \(k=3,4\). Summing residue counts over the two disjoint parity classes proves the two equal basin sizes. The odd extremal time is \(k-2\) for \(k\ge4\), whereas the even formulas have time at most \(\max\{2,\lfloor(k-1)/2\rfloor\}\), which never exceeds \(k-2\). This proves the extremal assertion.

## Verification

The accompanying standalone Python file `verify.py` independently iterates every residue modulo \(2^k\) for all \(1\le k\le17\), compares its least arrival time with the valuations, and compares both full histograms with the closed formulas. The run covered **262,142 residues** and returned `VERIFY_OK`. Its finite exhaustive tests support the theorem but are not a substitute for the preceding uniform argument.

## Relationship to prior work

Chebyshev and Dickson polynomial dynamics are a classical arithmetic topic. Yoshioka and Dainobu (2015) treat **odd-degree Chebyshev permutation polynomials** and periodic structure modulo powers of two. Lu, Dai and Li (2026) likewise analyze graph structures of Chebyshev **permutation** polynomials, with odd degrees. The present monic degree-two map is **noninvertible**, so its two attracting roots and transient-depth histograms are outside those permutation results; the formal scaling \(D_2(x,1)=2T_2(x/2)\) is not an invertible affine conjugacy over the dyadic residue rings. Work on Dickson polynomial functional graphs over **finite fields** likewise does not provide the tree census over nonreduced rings of order \(2^k\). The new contribution is the complete least-time and exact-depth classification, not the polynomial's definition or known fixed points.

## Limitations

Only the monic degree-two map \(D_2(x,1)\) over powers of two is classified; no general claim is made for other Dickson parameters, degrees, or odd-prime moduli. The novelty assessment is based on accessible primary work and targeted searches; an unindexed equivalent dyadic functional-graph computation remains a publication-priority risk. Independent mathematical validation has not yet been performed.

## References

1. D. Yoshioka and Y. Dainobu, *On some properties of Chebyshev polynomial sequences modulo \(2^k\)*, Nonlinear Theory and Its Applications, IEICE 6 (2015), 443–452, DOI `10.1587/nolta.6.443`, full text: https://www.jstage.jst.go.jp/article/nolta/6/3/6_443/_pdf/-char/en.
2. X. Lu, Y. Dai and C. Li, *Graph Structure of Chebyshev Permutation Polynomials over Binary and Ternary Adic Rings* (2026), arXiv `2605.21819`, https://arxiv.org/pdf/2605.21819.
3. *Periodicity and Dynamical Systems of Dickson Polynomials in Finite Fields* (2025), arXiv `2508.08621`, https://arxiv.org/abs/2508.08621. Included only as a different-base comparison; its full text was not inspected for this result.
