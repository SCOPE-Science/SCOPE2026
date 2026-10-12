# The augmented \(D_1\) code in Theorem III.1 is projective: dual distance \(3\), not \(2\)
## Finding
For every odd prime \(p\), every integer \(m\ge2\), every \(\alpha\in\mathbb F_{p^m}^{*}\), \(\beta\in\mathbb F_{p^m}\), and \(\gamma=\operatorname{Tr}(-\beta/\alpha)\), the augmented defining-set code \(\overline{\mathcal C_{D_1}}\) of Huang--Liang--Jia--Wan--Liao has dual minimum distance exactly \(3\), not \(2\) as stated in their Theorem III.1. Choose an \(\mathbb F_p\)-basis of \(\mathbb F_{p^m}\); nondegeneracy of the trace pairing identifies each generator column with \(g(x,y)=(\phi(x),\phi(y),1)\), where \(\phi\) is injective. Hence distinct coordinates of the set \(D_1\) give nonzero, pairwise nonproportional columns, so dual weights \(1\) and \(2\) are impossible. For \(y=-\alpha^{-1}\), every \(x\in\mathbb F_{p^m}\) lies in \(D_1\); thus for any \(t\ne0\), the three distinct columns at \(x=0,t,2t\) satisfy \(g(0,y)-2g(t,y)+g(2t,y)=0\). Since \(p\) is odd, all three coefficients are nonzero, giving a dual word of weight \(3\). Consequently \(d(\overline{\mathcal C_{D_1}}^{\perp})=3\) throughout the full Theorem III.1 parameter range, so the code is projective.

## Assumptions and scope
Let \\(p\\) be an odd prime, \\(m\\ge 2\\), \\(q=p^m\\), \\(\\alpha\\in\\mathbb F_q^*\\), and \\(\\beta\\in\\mathbb F_q\\). Let \\(\\operatorname{{Tr}}:\\mathbb F_q\\to\\mathbb F_p\\) be the absolute trace and set \\(\\gamma=\\operatorname{{Tr}}(-\\beta/\\alpha)\\). The defining set is
\\[
D_1=\\{{(x,y)\\in\\mathbb F_q^2:\\operatorname{{Tr}}(\\alpha xy+\\beta y+x)=\\gamma\\}},
\\]
and the augmented code consists of the vectors
\\[
(\\operatorname{{Tr}}(ax+by)+c)_{{(x,y)\\in D_1}},\\qquad a,b\\in\\mathbb F_q,\\ c\\in\\mathbb F_p.
\\]
The claim concerns only the dual minimum distance in the parameter regime of Theorem III.1 of arXiv:2607.07181v1. It does not alter that theorem's stated length, dimension, primal minimum distance, weight distribution, or self-orthogonality claim.

## Proof
Fix an \\(\\mathbb F_p\\)-basis \\(e_1,\\ldots,e_m\\) of \\(\\mathbb F_q\\). Define
\\[
\\phi(x)=(\\operatorname{{Tr}}(e_1x),\\ldots,\\operatorname{{Tr}}(e_mx))\\in\\mathbb F_p^m.
\\]
The trace pairing is nondegenerate, so \\(\\phi\\) is injective. A generator matrix for the augmented code can therefore be chosen with the column at \\((x,y)\\in D_1\\) equal to
\\[
g(x,y)=(\\phi(x),\\phi(y),1)^{\\mathsf T}.
\\]
Every column is nonzero. If two columns are proportional, say \\(g(x_2,y_2)=\\lambda g(x_1,y_1)\\), their final coordinates force \\(\\lambda=1\\). Injectivity of \\(\\phi\\) then gives \\((x_1,y_1)=(x_2,y_2)\\). Because \\(D_1\\) is a set, distinct coordinates therefore give pairwise nonproportional columns. Hence the dual has no word of weight \\(1\\) or \\(2\\), and \\(d(\\overline{{\\mathcal C_{{D_1}}}}^\\perp)\\ge3\\).

Now put \\(y_0=-\\alpha^{{-1}}\\). For every \\(x\\in\\mathbb F_q\\),
\\[
\\operatorname{{Tr}}(\\alpha x y_0+\\beta y_0+x)=\\operatorname{{Tr}}(-x-\\beta/\\alpha+x)=\\operatorname{{Tr}}(-\\beta/\\alpha)=\\gamma,
\\]
so \\((x,y_0)\\in D_1\\). Take any \\(t\\in\\mathbb F_q^*\\). Since \\(p\\) is odd, \\(0,t,2t\\) are distinct and \\(1,-2,1\\) are all nonzero in \\(\\mathbb F_p\\). Linearity of \\(\\phi\\) gives
\\[
g(0,y_0)-2g(t,y_0)+g(2t,y_0)=0.
\\]
Thus the dual contains a word of weight exactly \\(3\\). Combining the two bounds yields
\\[
d(\\overline{{\\mathcal C_{{D_1}}}}^\\perp)=3.
\\]
In particular the augmented code is projective.

## Verification
The accompanying `verify.py` checks the paper's displayed \\(p=3,m=2,\\alpha=\\beta=\\gamma=1\\) example. It verifies that its \\(33\\) generator columns are all distinct, nonzero, and pairwise nonproportional; it exhaustively finds dependent triples and no smaller dependence. It also applies the ternary MacWilliams transform to the paper's displayed weight enumerator and obtains \\(A_1^\\perp=A_2^\\perp=0\\) and \\(A_3^\\perp=160\\), independently confirming dual distance \\(3\\) for that example.

## Relationship to prior work
Huang--Liang--Jia--Wan--Liao define \\(D_1\\) and the augmented code in equations (I.2) and (I.4). Their Theorem III.1 states the same primal family in the case \\(\\gamma=\\operatorname{{Tr}}(-\\beta/\\alpha)\\), but gives dual minimum distance \\(2\\). Their Table III supplies a ternary \\(m=2\\) instance with weight enumerator \\(1+32z^{{18}}+96z^{{21}}+112z^{{24}}+2z^{{33}}\\); its first MacWilliams coefficients already agree with dual distance \\(3\\), not \\(2\\). Focused searches for the theorem, its parameter formula, projectivity, and the dual-distance discrepancy did not locate a published correction or a stronger statement covering this claim.

## Limitations
This result corrects only the dual minimum-distance assertion in Theorem III.1. It does not reassess the remaining claims of that theorem or other results in the paper. The all-parameter argument uses that \\(p\\) is odd, exactly as assumed in the paper; the three-column dependence used above degenerates in characteristic \\(2\\).

## References
Huang, Y.; Liang, Z.; Jia, C.; Wan, Y.; Liao, Q., *Four classes of few-weight self-orthogonal codes and their applications for LCD codes and quantum codes*, arXiv:2607.07181v1, submitted 2026-07-08. See equations (I.2), (I.4), Theorem III.1, Remark III.3, and Table III.
