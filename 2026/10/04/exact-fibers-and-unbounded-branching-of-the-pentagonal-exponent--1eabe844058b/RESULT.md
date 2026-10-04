# Exact fibers and unbounded branching of the pentagonal exponent map

## Finding
Let \(\nu_2(x)\) denote the \(2\)-adic valuation of a positive integer and define
\[
e(m)=m\bigl(\nu_2(m)+2\bigr)\qquad(m\ge1).
\]
For any positive integer \(n\), write \(n=2^\ell w\) with \(w\) odd. Then the preimages of \(n\) under \(e\) are classified exactly as follows. For every integer \(t\) with
\[
0\le t\le\ell,\qquad \nu_2(\ell+2-t)=t,
\]
put
\[
b_t=\frac{\ell+2-t}{2^t}.
\]
This \(b_t\) is odd. There is a preimage corresponding to \(t\) exactly when \(b_t\mid w\), and in that case it is unique and equals
\[
m_t=2^{\ell-t}\frac{w}{b_t}.
\]
Consequently
\[
\#e^{-1}(n)=\#\left\{t\in\{0,\ldots,\ell\}:\nu_2(\ell+2-t)=t\text{ and }b_t\mid w\right\}.
\]
Although every individual fiber is finite, these fiber cardinalities are unbounded.

More explicitly, define \(a_1=1\) and
\[
a_{j+1}=a_j+2^{a_j}\qquad(j\ge1).
\]
For any \(R\ge1\), let \(L=a_{R+1}\), \(\ell=L-2\), and
\[
T_R=\{0,a_1,\ldots,a_R\}.
\]
For \(t\in T_R\), define \(b_t=(L-t)/2^t\), let \(w\) be the least common multiple of these odd integers, and put \(n=2^\ell w\). Then \(n\) has at least \(R+1\) distinct preimages.

## Assumptions and scope
The map \(e\) is the exponent map used by Saikia and Sarma in their recent orbit-telescoping proof for truncated pentagonal-number series. Their argument needs three particular forward orbits to be disjoint and explicitly notes that \(e\) is not injective, for example \(e(2)=e(3)=6\). The present result concerns the global fiber structure of that same map. It does not alter their positivity theorem and does not assert that arbitrary merged orbit collections may be regrouped without multiplicity bookkeeping.

All variables are positive integers unless indicated otherwise. The theorem is exact and infinite; the finite computation described below is only an independent replay of the algebraic classification on a large bounded range.

## Proof
Write a possible preimage as \(m=2^k u\) with \(u\) odd. Since \(\nu_2(m)=k\),
\[
e(m)=2^k u(k+2).
\]
Set \(t=\nu_2(k+2)\) and write \(k+2=2^t b\) with \(b\) odd. Then
\[
e(m)=2^{k+t}ub.
\]
If this is equal to \(n=2^\ell w\), uniqueness of the odd-times-power-of-two decomposition gives
\[
\ell=k+t,
\qquad
w=ub.
\]
Thus \(k=\ell-t\), and therefore
\[
k+2=\ell+2-t.
\]
The definition of \(t\) is now exactly
\[
\nu_2(\ell+2-t)=t,
\]
and
\[
b=\frac{\ell+2-t}{2^t}=b_t.
\]
The odd equation \(w=ub_t\) has a positive odd solution \(u\) exactly when \(b_t\mid w\), in which case \(u=w/b_t\) and
\[
m=2^{\ell-t}\frac{w}{b_t}.
\]
This proves both necessity and sufficiency and gives the exact fiber formula. It also shows directly that each fiber is finite. Independently, finiteness follows from \(e(m)\ge2m\), so a preimage of \(n\) must satisfy \(m\le n/2\).

It remains to prove that fiber sizes are unbounded. First note inductively that every \(a_j\) is odd: \(a_1=1\), and adding \(2^{a_j}\), an even integer, preserves oddness. Fix \(R\ge1\) and put \(L=a_{R+1}\). For \(1\le j\le R\), telescoping the recurrence gives
\[
L-a_j=2^{a_j}+2^{a_{j+1}}+\cdots+2^{a_R}.
\]
Because \(a_{j+1}\ge a_j+1\), every term after the first is divisible by \(2^{a_j+1}\). Hence
\[
\nu_2(L-a_j)=a_j.
\]
Also \(L\) is odd, so \(\nu_2(L)=0\). With \(\ell=L-2\), this proves
\[
\nu_2(\ell+2-t)=t
\]
for every \(t\in T_R=\{0,a_1,\ldots,a_R\}\). Moreover \(a_R\le L-2=\ell\) because \(L-a_R=2^{a_R}\ge2\), so every such \(t\) lies in the allowed range.

For these \(t\), the integers \(b_t=(L-t)/2^t\) are odd. Choose \(w\) to be their least common multiple. The exact fiber formula then supplies one preimage \(m_t\) for every \(t\in T_R\). Distinct \(t\)'s give distinct \(2\)-adic valuations \(\nu_2(m_t)=\ell-t\), hence distinct preimages. Therefore \(\#e^{-1}(2^\ell w)\ge R+1\). Since \(R\) is arbitrary, the fiber cardinalities are unbounded.

## Verification
The standalone script `verify_fibers.py` performs two checks using exact integer arithmetic. First, for every target \(1\le n\le400000\), it compares the theorem's fiber formula with direct enumeration of every possible source \(1\le m\le200000\). This source range is exhaustive for those targets because \(e(m)\ge2m\). Second, it checks the explicit unbounded-branching construction for \(R=1,2,3\), including direct evaluation of \(e(m_t)=n\) for every constructed preimage.

The replay returns

`VERIFY_OK exhaustive_targets=400000 source_m=200000 constructions=[(1, 1, [0, 1], [3, 1], 2, 3), (2, 9, [0, 1, 3], [11, 5, 1], 3, 15), (3, 2057, [0, 1, 3, 11], [2059, 1029, 257, 1], 4, 2087)]`

The first three branching levels therefore include \(e^{-1}(6)\) with two elements, a constructed target of \(2\)-adic valuation \(9\) with three elements, and a constructed target of \(2\)-adic valuation \(2057\) with four elements. The computation is corroboration only; the unbounded statement follows from the recurrence proof for arbitrary \(R\).

## Relationship to prior work
Saikia and Sarma introduce \(e(m)=m(\nu_2(m)+2)\) as the dynamical exponent map behind a telescoping product. They prove that the three forward orbits seeded at \(1\), \(4\), and \(5\) are pairwise disjoint, and they explicitly remark that the map is not injective, giving \(e(2)=e(3)=6\) as an example of orbit merging. Their inspected argument does not give a formula for general fibers or bound their multiplicity.

The result here turns that qualitative noninjectivity into an exact inverse description and shows a stronger global phenomenon: mergers can have arbitrarily large indegree. This is relevant to extensions of the orbit-telescoping mechanism because no uniform finite merger bound can be assumed when regrouping more general collections of orbits. Statement-level searches using the exact map, its valuation equation, fiber/preimage terminology, and unbounded multiplicity did not locate a prior equivalent result.

## Limitations
The theorem classifies one-step fibers of \(e\); it does not classify all intersections of arbitrary forward orbits or the full directed functional graph. The explicit construction proves unbounded multiplicity but is not claimed to minimize the target with a given fiber size. The recurrence \(a_{j+1}=a_j+2^{a_j}\) grows very rapidly, so it is an existence device rather than an efficient search method. No claim is made that unbounded one-step indegree obstructs the specific three-orbit cancellation used by Saikia and Sarma; their three chosen orbits remain pairwise disjoint as proved in the source paper.

## References
1. Manjil P. Saikia and Abhishek Sarma, *On the positivity of truncated pentagonal number series and some conjectures of Merca*, arXiv:2609.25739v1, 2026.
2. Ji-Cai Liu, *A general positivity result on coefficients of certain \(q\)-series*, arXiv:2409.19907, first posted 2024; published version cited by Saikia and Sarma.
