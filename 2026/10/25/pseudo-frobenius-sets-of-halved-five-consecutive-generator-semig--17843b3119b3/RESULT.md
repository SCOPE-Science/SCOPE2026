# Pseudo-Frobenius sets of halved five-consecutive-generator semigroups

## Finding

For every odd integer \(a\ge7\), set
\[
S_a=\langle a,a+1,a+2,a+3,a+4\rangle,\quad
T_a=S_a/2=\{n\in\mathbb N:2n\in S_a\},\quad x=(a+1)/2.
\]
Then
\[
T_a=\langle x,x+1,2x-1,2x+3\rangle.
\]
The Apéry set of \(T_a\) relative to \(x\) has one element \(w_r\) of residue \(r\) modulo \(x\), with \(w_0=0\) and, for \(1\le r<x\),
\[
w_r=\min\left\{\left\lfloor\frac r3\right\rfloor(2x+3)
+(r\bmod3)(x+1),\;(x-r)(2x-1)\right\}.
\]
Writing \(x=4t+u\) with \(t\ge1\) and \(0\le u\le3\), the exact pseudo-Frobenius set \(\operatorname{PF}(T_a)\) is
\[
\begin{array}{c|l}
u&\operatorname{PF}(T_a)\\\hline
0&\{(2t-1)x-t,\;(2t-1)x+3t-1\}\\
1&\{(2t-1)x-t,\;(2t-1)x+3t-1,\;(2t-1)x+3t\}\\
2&\{(2t-1)x+3t-1,\;2tx+3t+1\}\\
3&\{(2t-1)x+3t-1,\;2tx+3t+1,\;(2t+1)x-t-1\}.
\end{array}
\]
In particular \(\operatorname{type}(T_a)=2\) if \(a\equiv3\pmod4\), and \(3\) if \(a\equiv1\pmod4\). The Frobenius number is the largest number in the corresponding row.

## Assumptions and scope

Here \(\mathbb N=\{0,1,2,\ldots\}\). A pseudo-Frobenius number of a numerical semigroup \(T\) is an integer \(f\notin T\) for which \(f+g\in T\) for every nonzero \(g\in T\). No coprimality hypotheses beyond consecutiveness are needed. The displayed four generators are not claimed to be a *minimal* generating system at every boundary: at \(x=4\), the last one is redundant.

## Proof

**Quotient reduction.** Two generators of \(S_a\), namely \(a+1\) and \(a+3\), are even and halve to \(x\) and \(x+1\). The other three, \(a,a+2,a+4\), are odd. Every even sum of generators has an even number of odd terms; pair them. Halves of such pairs run through \(a,a+1,a+2,a+3,a+4\), of which the middle three are \(2x\), \(x+(x+1)\), \(2(x+1)\), and the endpoints are \(2x-1\) and \(2x+3\). This proves the displayed equality for \(T_a\).

**Apéry normal form.** Abbreviate \(b=x+1\), \(c=2x-1\), \(d=2x+3\). The identities
\[
b+c=3x,\qquad c+d=2b+2x,\qquad 3b=d+x
\]
show that a factorization of a minimal representative of a residue modulo \(x\) cannot contain \(x\), cannot mix \(c\) with \(b\) or \(d\), and, if it contains no \(c\), must contain at most two copies of \(b\). Hence every nonzero Apéry representative is the minimum among (i) \(qc\) for positive \(q\) and (ii) \(qd+sb\) for \(q\ge0\), \(s\in\{0,1,2\}\). The former has residue \(-q\pmod x\) and its least possible value in residue \(r\in\{1,\ldots,x-1\}\) occurs at \(q=x-r\). In the latter the residue is \(3q+s\pmod x\); as the cost strictly increases with the nonnegative integer \(3q+s\), its minimum in residue \(r\) occurs at \(3q+s=r\). This establishes the Apéry formula.

**Branch transition.** For \(r=3q+s\), \(s\in\{0,1,2\}\), write \(F_r=qd+sb\) and \(B_r=(x-r)c\). Direct subtraction gives
\[
B_r-F_r=x(2x-1-8q-3s).
\]
If \(x=4t+u\), the final forward-branch index \(R\) equals \(3t-1\) when \(u=0\), \(3t\) when \(u=1\), and \(3t+1\) when \(u=2,3\). The branches tie only at \(r=R\) when \(u=2\). For \(r\le R\), \(w_r=F_r\); for \(r>R\), \(w_r=B_r\).

**Maximal Apéry elements.** Recall that \(\operatorname{PF}(T_a)=\{w-x:w\text{ maximal in }\operatorname{Ap}(T_a,x)\text{ under }\le_{T_a}\}\), where \(v\le_{T_a}w\) means \(w-v\in T_a\). Maximality can be checked by adding each of \(b,c,d\) and asking whether the result lies in the Apéry set. In the forward branch, adding \(b\) gives the next forward element whenever \(r\bmod3\in\{0,1\}\) and \(r+1\le R\), while adding \(d\) gives the forward element three residues later whenever \(r+3\le R\). Other forward-to-Apéry edges are excluded by the normal-form identities and the strict branch comparison, except the indicated tie. In the backward branch, adding \(c\) gives the preceding backward element whenever \(r\ge R+2\), and also from \(R+1\) to the tied \(R\) when \(u=2\); adding \(b\) or \(d\) cannot land in an Apéry representative because it is larger than the candidate at the destination residue. For \(r=0\), a positive generator leads to an Apéry element, so \(w_0\) is not maximal. Checking the remaining indices gives the complete list of maximal residue positions:
\[
\begin{array}{c|l}
u&\text{maximal residues}\\\hline
0&\{R,R+1\}\\
1&\{R-1,R,R+1\}\\
2&\{R-2,R\}\\
3&\{R-2,R,R+1\}.
\end{array}
\]
For \(u=2\), the first backward representative is not maximal precisely because its \(c\)-edge lands on the tied element. Substituting the respective \(F_r\) and \(B_r\), then subtracting \(x\), gives all four claimed rows, with no unlisted pseudo-Frobenius number.

## Verification

The included standalone Python verifier uses Dijkstra shortest paths in residue classes modulo \(x\), independent of the proposed Apéry expression, and checks every Apéry value, the complete set of maximal Apéry elements, and all four pseudo-Frobenius formulas for every integer \(4\le x\le500\). The verifier does not establish the infinite theorem; the algebraic proof above does.

## Relationship to prior work

Adeniran and collaborators initiated explicit questions about quotients of arithmetic-progression semigroups. Liu's December 2023 treatment of quotients of almost arithmetic progressions (arXiv:2312.06096, Theorems 1.3 and Proposition 2.2) assumes that the quotient denominator divides the original first generator, whereas here the denominator is two and the original first generator is odd. Morales and Nguyen Thi Dung (arXiv:2601.07467, 2026) describe pseudo-Frobenius numbers for generalized almost arithmetic generating systems under stated conditions; the four-generator family here does not have the necessary three-generator arithmetic-subblock form uniformly in \(x\). The new contribution is the uniform complete Apéry and pseudo-Frobenius formula, with a type dichotomy, for the halved five-consecutive family.

## Limitations

No independent mathematical audit has been performed. Novelty is assessed against the sources inspected; earlier implicit consequences or unindexed equivalent formulations are possible. This result addresses only odd initial generators and denominator two, not all quotient parameters. The boundary \(x=4\) has a redundant displayed generator but is included in the proof.

## References

1. Feihu Liu, *On quotients of numerical semigroups for almost arithmetic progressions*, arXiv:2312.06096v1 (public 2023-12-11), especially Introduction, Theorem 1.3, Proposition 2.2 and the Apéry reductions. https://arxiv.org/html/2312.06096v1
2. Marcel Morales and Nguyen Thi Dung, *Frobenius Number Of Almost Symmetric Numerical Generalized Almost Arithmetic Semigroups*, arXiv:2601.07467 (public 2026-01-12), Sections 1 and 3. https://arxiv.org/abs/2601.07467
3. A. Adeniran et al., *On the genus of a quotient of a numerical semigroup*, first public 2018-09-25, as cited in Liu (2023); full original article not inspected here.
