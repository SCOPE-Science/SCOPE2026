# Complete realizability of finite-order circle break-orbit patterns

## Finding
For any reduced rational rotation \(p/q\), with \(q\ge2\), every assignment of positive derivative jumps to finitely many distinct rational-rotation orbits, subject only to product-one cancellation on each orbit, is realized *exactly* by an orientation-preserving piecewise-linear circle homeomorphism of order \(q\). In the rotation coordinate, one can prescribe exactly which orbit points are genuine breaks, and the sizes of all their jumps; no extra breaks are created.

Consequently, the possible numbers of breaks on each orbit are exactly \(2,3,\ldots,q\). With exactly \(K\ge1\) break-containing orbits, the attainable total break counts are **all and only** \(2K\le n\le qK\). Without fixing \(K\), a nonidentity finite-order piecewise-linear circle homeomorphism has an even positive number of breaks when \(q=2\), while *every* integer \(n\ge2\) is attained for every \(q\ge3\). The statement excludes the rigid rotations, which have zero breaks.

## Assumptions and scope
Let \(S^1=\mathbb R/\mathbb Z\), \(R(y)=y+p/q\pmod1\), \(q\ge2\), \(\gcd(p,q)=1\). Fix \(K\ge1\) pairwise disjoint orbits \(O_k=\{y_{k,i}:i\in\mathbb Z/q\mathbb Z\}\), indexed by \(R(y_{k,i})=y_{k,i+1}\). For each orbit choose \(\gamma_{k,i}>0\), with \(\prod_{i=0}^{q-1}\gamma_{k,i}=1\); require at least two \(\gamma_{k,i}\ne1\) on every selected orbit. At non-break points the jump is defined to equal one. A jump means the ratio \(J_f(x)=f'_+(x)/f'_-(x)\) in positively oriented coordinates. The location constraint is imposed in the rotation coordinate: physical break locations are \(H(y_{k,i})\), not arbitrary prescribed physical positions independent of the conjugacy.

**Existence:** There is an orientation-preserving piecewise-linear homeomorphism \(H:S^1\to S^1\) such that \(f=H\circ R\circ H^{-1}\) has exactly the breaks \(H(y_{k,i})\) with \(\gamma_{k,i}\ne1\), with \(J_f(H(y_{k,i}))=\gamma_{k,i}\). All points of \(f\) have least period \(q\) and \(f^q=\mathrm{id}\).

**Necessity:** Every orientation-preserving piecewise-linear circle homeomorphism \(f\) conjugate to \(R\) satisfies per-orbit cancellation \(\prod_{x\in O}J_f(x)=1\) for each period-\(q\) orbit \(O\). Thus its nonempty break-containing orbits each have between two and \(q\) breaks. No claim about arbitrary rational-rotation maps not of finite order is made.

## Proof
**1. Necessity.** Because \(f^q=\mathrm{id}\), one-sided derivatives of the composition satisfy
\[
1=J_{f^q}(x)=\prod_{i=0}^{q-1}J_f(f^i(x)).
\]
This holds also at break points: derivatives of an orientation-preserving piecewise-linear map along each side obey the ordinary composition rule. A cycle having exactly one nonunit jump contradicts the product-one identity. Every cycle has \(q\) elements, giving the necessary interval \(2\le r\le q\).

**2. A cyclic multiplicative coboundary.** For each \(k\), select positive numbers \(\ell_{k,i}\) with
\[
\frac{\ell_{k,i+1}}{\ell_{k,i}}=\gamma_{k,i}.
\]
Fix \(\ell_{k,0}=1\), and define subsequent values recursively. The final closing equation is exactly \(\prod_i\gamma_{k,i}=1\), so the definition is consistent. The \(\ell\)'s can be multiplied by an independent constant on each orbit without affecting the ratios.

**3. Global normalization and conjugacy.** Set \(P=\prod_{k,i}\ell_{k,i}>0\) and multiply all \(q\) values on the first orbit by \(P^{-1/q}\). The total product of the now-prescribed numbers \(\ell_{k,i}\) over all distinct orbit points is one. Define a positive step function \(v\) on the circle, having its only potential jumps at the finitely many points \(y_{k,i}\), with \(v_+(y_{k,i})/v_-(y_{k,i})=\ell_{k,i}\). To construct it, start with any positive slope on one component of the complement of these points and propagate the slope around the circle, multiplying by \(\ell_{k,i}\) as each marked point is crossed. The total product-one condition gives consistency after a full circuit. Dividing by \(\int_0^1v(t)\,dt\) gives a positive probability density. Its integral \(H(y)=\int_0^y v(t)\,dt\pmod1\) is an orientation-preserving piecewise-linear circle homeomorphism.

For \(f=H\circ R\circ H^{-1}\), orientation preservation and the chain rule give
\[
 f'(H(y))=\frac{H'(R(y))}{H'(y)},\qquad
 J_f(H(y))=\frac{J_H(R(y))}{J_H(y)}.
\]
At every marked orbit point the second quotient is \(\ell_{k,i+1}/\ell_{k,i}=\gamma_{k,i}\), and at any unmarked point it equals one. Thus exactly the desired breaks occur. As conjugacy preserves rotation number and period, \(f\) has rotation number \(p/q\) and order \(q\).

**4. Complete count spectrum.** Choose a subset of size \(r\) of one rotation orbit for any \(2\le r\le q\). Put jump two at \(r-1\) of those points, and \(2^{1-r}\) at the last point; put jump one elsewhere. All selected positions are genuine breaks and cancellation holds. Use any \(K\) disjoint rotation orbits and sizes \(r_1,\ldots,r_K\). The realizable totals are precisely \(n=\sum r_k\) with \(2\le r_k\le q\), hence the full integer interval \(2K\le n\le qK\). For \(q=2\), every \(r_k=2\), giving only positive even totals; for \(q\ge3\), every \(n\ge2\) is a sum of twos and threes, giving every total. Conversely necessity excludes all other cases.

## Verification
The standalone Python 3 script `verify.py` checks the finite cyclic coboundary equations and support cardinalities using exact rational arithmetic for all coprime \(1\le p<q\le14\), all single-orbit support lengths \(2\le r\le q\), and selected two-orbit cases. It reports 641 passed cases. The script checks the finite algebra; the analytic integration and infinitely many allowed periods follow from the proof, not from enumeration. Run with `python3 verify.py`.

## Relationship to prior work
Glendinning, Ma and Montaldi (2025), Theorems 2.2–2.4, prove conjugacy and give the **necessary** condition that break-point jumps multiply to one on each periodic orbit, with at least two breaks per break-containing orbit. They do not state the arbitrary, orbitwise **sufficiency/realizability** prescription or the sharp feasible \((q,K,n)\) spectrum. Adouani and Marzougui (2015/2016), Lemma 2.2, prove the underlying global finite-jump realization for a piecewise-linear homeomorphism (with the reciprocal convention for jumps); the present cyclic cohomological compatibility step is explicitly the added application, not an invention of the jump-realization lemma. Their principal theorems concern conjugacy regularity, especially irrational rotation numbers. The result is a concrete inverse/realization complement to these known necessary constraints, not a new rigidity criterion or classification of all rational-rotation dynamics.

## Limitations
This is a short constructive realization theorem; its novelty depends on whether the exact inverse prescription has appeared under different terminology. It does not classify piecewise-linear conjugacies up to centralizers, determine codimension of constraints in arbitrary finite-dimensional parameter families, or prescribe break locations in the original physical coordinate. The general step-function construction and orbit cancellation are classical ingredients. Independent bibliographic checking remains to be performed.

## References
1. P. Glendinning, S. Ma, J. Montaldi, *Piecewise linear circle maps and conjugation to rigid rational rotations* (first public 2025-05-19), arXiv:2505.13689, especially Theorems 2.2–2.4 and Sections 3–4.
2. A. Adouani, H. Marzougui, *A sharp smoothness of the conjugation of class P-homeomorphisms to diffeomorphisms* (2015), arXiv:1508.03549, especially Lemma 2.2 and Theorem 2.1; Kodai Math. J. 39 (2016), 425–438.
