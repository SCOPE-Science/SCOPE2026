# Exact limsup counting-product constants for higher-radix digit-splitting additive complements

## Finding
For each integer \(r\ge2\), let \(Q=r^2\), and define
\[
 A_r=\{\sum_{j\ge0}a_jQ^j:0\le a_j<r,\text{ finitely many nonzero}\},\quad B_r=rA_r.
\]
Write \(a(x)=|A_r\cap[0,x)|\), \(b(x)=|B_r\cap[0,x)|\) for integer \(x\ge0\). Each nonnegative integer has exactly one representation as a sum of an element of \(A_r\) and one of \(B_r\), by separation of even and odd base-\(r\) digits. Then
\[
 \boxed{a(x)b(x)\le\frac{2(r+1)}{r+2}x\quad(x\ge0),\qquad
 \limsup_{x\to\infty}\frac{a(x)b(x)}x=\frac{2(r+1)}{r+2}.}
\]
The new assertion is the all-radix sharp constant, especially the values \(8/5\) for \(r=3\), \(5/3\) for \(r=4\), and the approach to \(2\) as the radix increases. The binary-radix value \(3/2\) is already covered by prior studies of the Moser–de Bruijn complement pair.

## Assumptions and scope
The sets contain zero; counting functions use the half-open convention \([0,x)\) at integral \(x\). For real \(x\), the counting functions are step functions with jumps immediately to the right of integer arguments; their limsup is unchanged because for \(m<x\le m+1\) the product equals \(a(m+1)b(m+1)\), and division by \(x\ge m\) changes the integer-point bound by a factor at most \((m+1)/m\). The theorem concerns fixed integer \(r\ge2\). It asserts no estimate uniform in a radix growing with \(x\).

## Proof
Put \(\lambda=2(r+1)/(r+2)\), \(c_A=\lambda/(r+1)\), and \(c_B=\lambda r/(r+1)\). We prove simultaneously, for every integer \(x\ge0\), the following three inequalities:
\[
 D(x):=\lambda x-a(x)b(x)\ge0;\quad
 x\in A_r\Rightarrow D(x)\ge b(x)-c_A;\quad
 x\in B_r\Rightarrow D(x)\ge a(x)-c_B.
\]
At \(x=0\) these are immediate. For \(1\le x<Q\), the exact counts are \(a(x)=\min(x,r)\) and \(b(x)=\lceil x/r\rceil\). When \(x<r\) and \(x\in A_r\), the second inequality reduces to \(x(\lambda-1)-1+c_A\ge0\), with equality at \(x=1\). When \(x=rk\in B_r\), \(1\le k<r\), the third reduces to \(rk(\lambda-1)-r+c_B\ge0\), with equality at \(k=1\). The first inequality follows for \(x\le r\) from \(\lambda\ge1\), and for \(x>r\), on writing \(k=\lceil x/r\rceil\ge2\), from \(a(x)b(x)/x\le rk/[r(k-1)+1]\le2r/(r+1)<\lambda\).

Now suppose \(x=Qt+s\), with \(t\ge1\), \(0\le s<Q\), and assume all three assertions through \(t\). Write \(u=a(t)\), \(v=b(t)\). The digit decomposition gives the exact identities
\[
 a(x)=ru+\mathbf1_{t\in A_r}\min(s,r),\qquad
 b(x)=rv+\mathbf1_{t\in B_r}\lceil s/r\rceil.
\]
Since the positive sets \(A_r\) and \(B_r\) are disjoint, at most one indicator is nonzero.

If \(t\notin A_r\cup B_r\), then \(D(x)=QD(t)+\lambda s\ge0\), and \(x\) belongs to neither set, so nothing else is needed.

If \(t\in A_r\), then \(v\ge1\) and \(rv>\lambda\). Using the second inductive inequality,
\[
 D(x)\ge rv(r-\min(s,r))+\lambda s-Qc_A\ge\lambda r-Qc_A=\frac{\lambda r}{r+1}>0.
\]
If also \(x\in A_r\), necessarily \(s<r\), and
\[
 D(x)-b(x)+c_A\ge rv(r-s-1)+\lambda s-(Q-1)c_A\ge\lambda(r-1)-(Q-1)c_A=0.
\]
The displayed lower bounds use that the corresponding affine expression in \(s\) is minimized at its greatest allowed value, since \(rv>\lambda\).

If \(t\in B_r\), then \(u\ge r>\lambda\) because \(t\ge r\) and all \(0,1,\dots,r-1\) lie in \(A_r\). Put \(k=\lceil s/r\rceil\). The third inductive inequality gives
\[
 D(x)\ge ru(r-k)+\lambda s-Qc_B.
\]
For \(k=0\) this is positive. For \(1\le k\le r\), use \(s\ge r(k-1)+1\), \(u\ge r\), and \(r>\lambda\). The resulting expression is minimized at \(k=r\), where it equals
\[
 \lambda(Q-r+1)-Qc_B=\frac{\lambda}{r+1}>0.
\]
If also \(x\in B_r\), necessarily \(s=rk\) with \(0\le k<r\), and
\[
 D(x)-a(x)+c_B\ge ru(r-k-1)+\lambda rk-(Q-1)c_B\ge\lambda r(r-1)-(Q-1)c_B=0,
\]
the minimum occurring at \(k=r-1\). This proves all three inequalities by strong induction. Hence the pointwise upper bound holds.

For sharpness, let \(k\ge1\), \(j_k=2r^{k-1}-1\) and list the elements of \(A_r\) increasingly as \(\alpha_0,\alpha_1,\ldots\). The base-\(r\) digit expansion gives
\[
 r\alpha_{j_k}=\frac{r+2}{r(r+1)}Q^k-\frac r{r+1}.
\]
Set \(x_k=r\alpha_{j_k}+1\). The consecutive elements \(\alpha_{r^k-1}=(Q^k-1)/(r+1)\) and \(\alpha_{r^k}=Q^k\) straddle \(x_k\), while exactly \(j_k+1\) elements of \(B_r\) lie below \(x_k\). Thus \(a(x_k)=r^k\), \(b(x_k)=2r^{k-1}\), and
\[
 \frac{a(x_k)b(x_k)}{x_k}=\frac{2Q^k/r}{\{(r+2)/(r(r+1))\}Q^k+1/(r+1)}\longrightarrow\lambda.
\]
The upper and lower bounds coincide.

## Verification
A standalone Python verifier, `verify.py`, directly generates both sets from digit restrictions and tests the pointwise and strengthened inductive inequalities for several radices and complete finite ranges. It also checks the explicit sharpness subsequence. The program uses rational arithmetic; these tests complement, but do not replace, the preceding proof.

## Relationship to prior work
Zhang, *A Sharp Bound for Additive Complements* (arXiv:2610.29963, publicly posted 2026-10-21), proves a universal sharp threshold \(3/2\) for additive complements; this theorem instead computes the exact limsup for every higher-radix digit-splitting pair. Ma, *A Note on Additive Complements* (arXiv:2205.04128), exhibits a different example with limsup \(2\), not these fixed finite-radix values. The binary case \(r=2\) has previously been determined by the full ratio distribution for the base-four Moser–de Bruijn construction; it is retained here to state a uniform theorem, not claimed as an independent novelty. Earlier work on exact digit-split threshold equalities treats \(a(x)b(x)-x=1\), which does not imply the limsup formula.

## Limitations
The proof is for fixed integral radices and the standard even/odd digit split. It does not classify all exact additive complements or show that every intermediate real limsup value is realized. Novelty is assessed against accessible sources and may be affected by an earlier implicit general-radix statement not found in the searches.

## References
1. Z. Zhang, *A Sharp Bound for Additive Complements*, arXiv:2610.29963 (2026-10-21), https://arxiv.org/abs/2610.29963.
2. F.-Y. Ma, *A Note on Additive Complements*, arXiv:2205.04128 (2022-05-09), https://arxiv.org/abs/2205.04128.
3. N. G. de Bruijn, classical work on additive complementary sequences and digital constructions; included for historical context, without relying on any unverified theorem from this source.
