# Pseudo-Frobenius patterns of four consecutive Mersenne generators

## Finding
For each integer \(m\ge5\), let \(a=2^m-1\) and
\[
S_m=\langle 2^m-1,\,2^{m+1}-1,\,2^{m+2}-1,\,2^{m+3}-1\rangle
=\langle a,2a+1,4a+3,8a+7\rangle.
\]
Write \(F_m\) for the Frobenius number of \(S_m\) and \(\operatorname{PF}(S_m)\) for its pseudo-Frobenius set. For every \(m\ge5\) **not divisible by three**, the exact sets are
\[
\operatorname{PF}(S_m)=
\begin{cases}
\{F_m,F_m-1,F_m-2\},&m\equiv1\pmod3,\\
\{F_m,F_m-4(a+1)\},&m\equiv2\pmod3,
\end{cases}
\]
where
\[
F_m=\begin{cases}
a(a-1+q)-1,&a=7q+1\quad(m\equiv1\pmod3),\\
a(a+q+1)-1,&a=7q+3\quad(m\equiv2\pmod3).
\end{cases}
\]
In particular, the Cohen–Macaulay type is exactly three or two according as \(m\equiv1\) or \(2\pmod3\); neither family is symmetric. The related \(m\equiv0\pmod3\) branch is previously covered by an existing general theorem and is not part of the new claim.

## Assumptions and scope
A numerical semigroup is an additive submonoid of the nonnegative integers with finite complement. A pseudo-Frobenius element is an integer \(f\notin S\) such that \(f+s\in S\) for all nonzero \(s\in S\). Its number is the type. The four displayed generators have greatest common divisor one because \((2a+1)-2a=1\). All assertions quantify over arbitrary integers \(m\ge5\) in the two indicated residue classes. No asymptotic or experimentally bounded hypothesis is used.

## Proof
**Step 1: a self-contained Apéry representation.** Put
\[
C(t)=\left\lfloor\frac t7\right\rfloor+
\left\lfloor\frac{t\bmod7}{3}\right\rfloor+(t\bmod7)\bmod3\quad(t\ge0).
\]
This is the minimum number of coins needed to pay \(t\) using denominations \(1,3,7\). To prove it, note that for denominations \(1,3\) the minimum is \(L(u)=\lfloor u/3\rfloor+(u\bmod3)\), and \(L(u+7)\ge L(u)+1\), by checking the three possible residues of \(u\) modulo three. If \(t=7q+r\), \(0\le r\le6\), a representation with \(q-h\) seven-coins has total coin count at least \(q-h+L(r+7h)\ge q+L(r)\), attained at \(h=0\).

Any element of \(S_m\) may be written with coefficients \(z,u,v,w\ge0\) as
\[
a\bigl(z+t+u+v+w\bigr)+t,\qquad t=u+3v+7w.
\]
Consequently, at fixed \(t\) the least such element is \(H(t)=a(t+C(t))+t\). The values of \(L(r)\) for \(r=0,1,\ldots,6\) are \((0,1,2,1,2,3,2)\). Thus \(C(t+1)-C(t)\ge-1\), including the transition across multiples of seven, so \(H(t+1)-H(t)\ge1\). For each residue \(r\in\{0,\ldots,a-1\}\), all eligible \(t\) are \(r+ja\), \(j\ge0\), and the additional coefficient \(z\) cannot lower a representation. Therefore the complete Apéry set relative to \(a\) consists of
\[
W(r)=a(r+C(r))+r,\qquad 0\le r<a.
\]
Because \(W(r)\) is strictly increasing, its largest element is \(W(a-1)\), and \(F_m=W(a-1)-a\). The displayed formulas for \(F_m\) follow by inserting \(a=7q+1\) or \(a=7q+3\) into \(C(a-1)\).

**Step 2: the Apéry maximality criterion.** The integer \(f_r=W(r)-a\) is always a gap. It is pseudo-Frobenius exactly when \(f_r+g\in S_m\) for all four generators \(g\). This is automatic for \(g=a\). For \(g_d=a(d+1)+d\), where \(d\in\{1,3,7\}\), one computes \(f_r+g_d=a(r+C(r)+d)+r+d\). If \(r+d<a\), comparison with \(W(r+d)\) shows
\[
f_r+g_d\in S_m\quad\Longleftrightarrow\quad C(r)\ge C(r+d).
\]
If \(r+d\ge a\), the residue is \(s=r+d-a\in\{0,\ldots,6\}\) and
\[
f_r+g_d=a\bigl(s+a+C(r)+1\bigr)+s\ge W(s),
\]
since \(C(s)\le6\) and \(a\ge31\). Thus the generator condition always holds when the addition wraps past the modulus.

**Step 3: seven residues suffice and are classified.** Since \(C(r+7)=C(r)+1\), the \(d=7\) test fails whenever \(r+7<a\). Therefore only \(r\in\{a-7,\ldots,a-1\}\) may contribute. The remaining \(d=1\) and \(d=3\) inequalities are determined by the seven residual values \((0,1,2,1,2,3,2)\). Direct substitution, including the wrap rule just proved, gives
\[
\begin{array}{c|c|c}
a\bmod7 & \{r:\ f_r\in\operatorname{PF}(S_m)\} & \text{type}\\\hline
1&\{a-3,a-2,a-1\}&3\\
3&\{a-5,a-1\}&2
\end{array}
\]
No other residue meets all generator tests. In the first line \(W(a-1)-W(a-2)=W(a-2)-W(a-3)=1\); in the second \(W(a-1)-W(a-5)=4(a+1)\), by the same displayed formula for \(W\). Subtracting \(a\) yields exactly the pseudo-Frobenius sets in the Finding. A numerical semigroup is symmetric if and only if its type is one; both new families have larger type.

## Verification
The accompanying standalone `verify.py` computes Apéry sets by shortest paths on residues modulo \(a\), using generator edge weights rather than the closed formula. It compares every Apéry element with \(W(r)\), independently enumerates all pseudo-Frobenius residues by the generating-set membership test, and checks the claimed exact sets for every \(5\le m\le13\). These finite checks are supportive; the proof above covers all admissible \(m\).

## Relationship to prior work
Komatsu, *The Frobenius number for shifted geometric sequences associated with the number of solutions*, arXiv:2209.13118 (first posted 2022-09-27), Section 7 and Table 5, already sketches the four-variable Apéry structure and derives Frobenius formulas. Thus **the Apéry formula and Frobenius evaluations are used here only as proof machinery, not claimed as novel**. Liu, Xin, Ye and Yin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459 (first posted 2023-06-06), Theorems 2.10–2.13, give general greedy Apéry and Frobenius/genus procedures. Their Theorem 3.4 supplies pseudo-Frobenius sets in the branch with \(a\) a multiple of seven, corresponding here to \(m\equiv0\pmod3\), **excluded from the present claim**. Their analyzed full Mersenne numerical semigroup has a different generating set for \(m\ge5\): its fifth generator \(2^{m+4}-1=16a+15\) is absent from \(S_m\), since \(a>15\) and the Apéry minimum \(W(15)=18a+15\) exceeds \(16a+15\). The new statement classifies the pseudo-Frobenius sets in the two remaining Mersenne residue classes, identifying a type-three versus type-two transition and a nonconsecutive-gap regime. Literature searches did not find a direct prior statement of those two classifications; this is not a proof of publication priority.

## Limitations
The exact result applies only to four consecutive Mersenne generators and \(m\equiv1,2\pmod3\). Its Apéry groundwork is already published, and general methods for extracting pseudo-Frobenius elements from Apéry sets are standard. Originality is therefore limited to the explicit two-branch classification and precise pseudo-Frobenius arithmetic, not to the general method. Unindexed equivalent statements or implicit prior treatment could still exist. There has been no independent mathematical audit.

## References
- T. Komatsu, *The Frobenius number for shifted geometric sequences associated with the number of solutions*, arXiv:2209.13118, Sections 2 and 7, initial posting 2022-09-27.
- F. Liu, G. Xin, S. Ye and J. Yin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459, Sections 2–3, initial posting 2023-06-06.
- J. C. Rosales, M. B. Branco and D. Torrão, *The Frobenius problem for Mersenne numerical semigroups*, Math. Z. 286 (2017), 741–749, concerning the different infinite-generator family.
