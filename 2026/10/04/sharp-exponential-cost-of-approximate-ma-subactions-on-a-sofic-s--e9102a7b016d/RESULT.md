# Sharp exponential cost of approximate Mañé subactions on a sofic shift
## Finding
Fix \(0<\alpha<1\). Consider the one-sided sofic shift \(X\subset\{a,b,c\}^{\mathbb N}\) from Remark 9.12 of Huang--Jenkinson--Xu--Zhang: \(X\) is the shift-orbit closure of sequences
\[
a^{n_1}ba^{n_2}ca^{n_3}ba^{n_4}c\cdots,
\]
where every \(n_i\ge1\). Equip \(X\) with the standard symbolic metric
\[
d_\alpha(x,y)=\alpha^{N(x,y)},
\]
where \(N(x,y)\) is the number of initial coordinates on which \(x\) and \(y\) agree. Let \(\sigma\) be the left shift and let \(f:X\to\mathbb R\) depend on the first coordinate by
\[
f(a\cdots)=0,\qquad f(b\cdots)=1,\qquad f(c\cdots)=-1.
\]
For \(\varepsilon>0\), define the least Lipschitz cost of an \(\varepsilon\)-subaction by
\[
\Lambda_\alpha(\varepsilon)=\inf\left\{|\phi|_{\mathrm{Lip},\alpha}:\phi\in\mathrm{Lip}(X),\ f+\phi-\phi\circ\sigma\le\varepsilon\right\}.
\]
Then for every \(0<\varepsilon<1\),
\[
\sup_{n\ge0}\alpha^{-n}\bigl(1-(n+1)\varepsilon\bigr)_+
\le \Lambda_\alpha(\varepsilon)
\le 2\alpha^{-\lceil1/\varepsilon\rceil}.
\]
Consequently,
\[
\lim_{\varepsilon\downarrow0}\varepsilon\log\Lambda_\alpha(\varepsilon)=\log(1/\alpha).
\]
Thus the previously qualitative failure of the exact Mañé lemma in this sofic example has a sharp quantitative signature: approximate subactions exist for every positive slack, but their optimal Lipschitz scale is exponentially large in \(1/\varepsilon\).

## Assumptions and scope
The statement concerns precisely the sofic shift and one-coordinate potential above. The metric parameter satisfies \(0<\alpha<1\), and \(|\cdot|_{\mathrm{Lip},\alpha}\) denotes the Lipschitz seminorm for \(d_\alpha\). The inequality \(f+\phi-\phi\circ\sigma\le\varepsilon\) is pointwise on all of \(X\). Additive constants in \(\phi\) do not affect the seminorm or the inequality.

The source proves that every invariant measure has \(f\)-average zero and that no continuous exact subaction can satisfy \(f+\phi-\phi\circ\sigma\le0\). The finding here is the quantitative positive-slack law, not another proof of exact nonexistence.

## Proof
Every finite word occurring in \(X\) has its non-\(a\) symbols alternating between \(b\) and \(c\). Therefore every Birkhoff sum obeys
\[
-1\le S_k f(x)\le1
\]
for all \(x\in X\) and all integers \(k\ge0\).

For the lower bound, suppose \(\phi\) is Lipschitz and
\[
f+\phi-\phi\circ\sigma\le\varepsilon.
\]
For \(n\ge0\), the point \(z^{(n)}=a^n b a^\infty\) belongs to \(X\), as used in the source. Summing the inequality along \(z^{(n)},\sigma z^{(n)},\ldots,\sigma^n z^{(n)}\) gives
\[
1+\phi(z^{(n)})-\phi(a^\infty)\le(n+1)\varepsilon.
\]
Since \(d_\alpha(z^{(n)},a^\infty)=\alpha^n\),
\[
|\phi|_{\mathrm{Lip},\alpha}\,\alpha^n
\ge \phi(a^\infty)-\phi(z^{(n)})
\ge1-(n+1)\varepsilon.
\]
Taking the positive part and then the supremum over \(n\) proves
\[
\Lambda_\alpha(\varepsilon)\ge
\sup_{n\ge0}\alpha^{-n}\bigl(1-(n+1)\varepsilon\bigr)_+.
\]

For the upper bound, put \(N=\lceil1/\varepsilon\rceil\) and \(g=f-\varepsilon\). The alternating property gives
\[
S_Ng(x)=S_Nf(x)-N\varepsilon\le1-N\varepsilon\le0
\]
for every \(x\in X\). Define
\[
u_N(x)=\max_{0\le k\le N-1}S_k g(x),
\]
with \(S_0g=0\). Then
\[
g(x)+u_N(\sigma x)
=\max_{1\le j\le N}S_jg(x)
\le u_N(x),
\]
because the extra term \(S_Ng(x)\) is nonpositive. Hence \(\phi=-u_N\) satisfies
\[
f+\phi-\phi\circ\sigma\le\varepsilon.
\]

It remains to bound its Lipschitz seminorm. For \(k\ge1\), the function \(S_k f\) is constant on length-\(k\) cylinders and takes values only in \(\{-1,0,1\}\). Thus
\[
|S_k f|_{\mathrm{Lip},\alpha}\le2\alpha^{-(k-1)}.
\]
Subtracting the constant \(k\varepsilon\) does not change this seminorm, and a finite maximum of Lipschitz functions has seminorm at most the maximum of their seminorms. Therefore
\[
|u_N|_{\mathrm{Lip},\alpha}\le2\alpha^{-N},
\]
which proves the stated upper bound.

Finally, for sufficiently small \(\varepsilon\), set \(n_\varepsilon=\lfloor1/\varepsilon\rfloor-2\). Then
\[
1-(n_\varepsilon+1)\varepsilon\ge\varepsilon,
\]
so
\[
\Lambda_\alpha(\varepsilon)\ge
\varepsilon\,\alpha^{-(\lfloor1/\varepsilon\rfloor-2)}.
\]
Together with the upper bound and the facts \(\varepsilon\lfloor1/\varepsilon\rfloor\to1\), \(\varepsilon\lceil1/\varepsilon\rceil\to1\), and \(\varepsilon\log\varepsilon\to0\), this yields
\[
\lim_{\varepsilon\downarrow0}\varepsilon\log\Lambda_\alpha(\varepsilon)=\log(1/\alpha).
\]

## Verification
The lower estimate reuses the source's explicit points \(a^n b a^\infty\), but keeps a positive slack and converts the resulting endpoint difference into a metric Lipschitz lower bound. The upper estimate is independent: it constructs an explicit finite-horizon subaction from the bound \(S_kf\le1\). No finite enumeration or numerical experiment is used as proof.

Boundary checks are direct. The closure defining \(X\) preserves alternation of the non-\(a\) symbols in every finite word, so \(S_kf\in\{-1,0,1\}\). The metric distance between \(a^n b a^\infty\) and \(a^\infty\) is exactly \(\alpha^n\). The constructed \(u_N\) is a maximum of finitely many cylinder functions and is therefore Lipschitz. The result asserts only the asymptotic Lipschitz cost for this specific potential and metric family.

## Relationship to prior work
Huang, Jenkinson, Xu, and Zhang prove in Remark 9.12 that this sofic shift admits no continuous \(\phi\) satisfying the exact inequality \(f+\phi-\phi\circ\sigma\le0\). Their proof uses the same family \(a^n b a^\infty\) to obtain a qualitative contradiction by continuity. The inspected article does not state a positive-slack problem, an optimal Lipschitz cost, or a quantitative blow-up rate; searches within the full text for approximate subactions and Lipschitz-constant estimates found no such statement.

The present result adds both directions needed for a sharp rate: the source witness gives a lower bound once combined with the symbolic metric, while the finite-horizon maximum \(u_N\) supplies an explicit approximate subaction and the matching logarithmic upper rate. Searches of published-finding indexes and the web for quantitative Mañé-lemma failure, approximate subactions on this sofic example, and Lipschitz-cost blow-up produced no statement implying the displayed limit.

## Limitations
The theorem is model-specific. It does not claim that every system without an exact Mañé lemma has exponential approximate-subaction cost, nor that the multiplicative constants in the two-sided bounds are optimal. The exact finite-\(\varepsilon\) value of \(\Lambda_\alpha(\varepsilon)\) is not determined. The novelty search cannot exclude terminology or formulations absent from the searched sources, so broader quantitative weak-KAM or ergodic-optimization literature remains a residual overlap risk.

## References
1. Wen Huang, Oliver Jenkinson, Leiye Xu, Yiwei Zhang, “Typical periodic optimization for dynamical systems: symbolic dynamics,” Inventiones Mathematicae 245 (2026), 1–63, DOI 10.1007/s00222-026-01411-x; arXiv:2603.07224v1.
2. The same article, Remark 9.12, for the explicit sofic shift, potential, zero maximizing value, and qualitative failure of the exact Mañé lemma.
