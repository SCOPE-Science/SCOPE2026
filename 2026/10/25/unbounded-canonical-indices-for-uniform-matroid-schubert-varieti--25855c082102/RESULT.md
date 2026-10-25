# Unbounded canonical indices for uniform matroid Schubert varieties

## Finding
Let \(V\subset\mathbb C^n\) be any complex realization of \(U_{r,n}\), and let \(Y_V\subset(\mathbb P^1)^n\) be its matroid Schubert variety. If \(\operatorname{ind}(Y_V)\) is the least positive integer \(m\) for which \(mK_{Y_V}\) is Cartier, then
\[
\operatorname{ind}(Y_V)=
\begin{cases}
1,&r=1,\\[2pt]
\dfrac{n-r+1}{\gcd(n-r+1,2)},&2\le r\le n.
\end{cases}
\]
In particular, for \(r=2\), the index is \(\dfrac{n-1}{\gcd(n-1,2)}\), which is unbounded as \(n\to\infty\). Every member of this family is \(\mathbb Q\)-Gorenstein.

## Assumptions and scope
The ground field is \(\mathbb C\), and every coordinate projection of \(V\) is nonzero, so its matroid is loopless and equal to \(U_{r,n}\). The result concerns the canonical Cartier index only. It does not classify singularity types or canonical indices for arbitrary matroids.

## Proof
Let \(M\) be the matroid of \(V\), let \(\mathcal H(M)\) be its corank-one flats, and let \(D_F\) denote the corresponding codimension-one orbit closures. The canonical divisor formula has coefficient \(|E\setminus F|-2\) at \(D_F\). The \(|E\setminus F|\) part is Cartier because it is the sum of the coordinate-divisor generators. Thus, modulo a Cartier divisor, \(K_{Y_V}\) is represented by \(-2\sum_{F\in\mathcal H(M)}D_F\). The Cartier-class calculation identifies the Cartier subgroup with integer weight combinations of the coordinate-divisor generators. Scaling that class calculation shows that \(mK_{Y_V}\) is Cartier if and only if there is a function \(w:E\to\mathbb Z\) satisfying
\[
\sum_{e\in C}w(e)=-2m
\quad\text{for every cocircuit }C\text{ of }M.
\]
This is the scaled canonical-class condition; the cited source proves the underlying Cartier-class and canonical-divisor formulas.

Now take \(M=U_{r,n}\) and put \(k=n-r+1\). If \(2\le r\le n\), then \(1\le k\le n-1\), and the cocircuits are exactly the \(k\)-element subsets of \(E=\{1,\ldots,n\}\). For any distinct \(i,j\in E\), choose a set \(S\subset E\setminus\{i,j\}\) with \(|S|=k-1\). Comparing the equations for \(S\cup\{i\}\) and \(S\cup\{j\}\) gives \(w(i)=w(j)\). Thus all weights equal some integer \(t\), and the condition becomes \(kt=-2m\). An integer \(t\) exists exactly when \(k\mid 2m\); the least positive such \(m\) is \(k/\gcd(k,2)\).

When \(r=1\), the only cocircuit is all of \(E\). Integer weights with total \(-2\) exist, so the index is \(1\); equivalently, the closure of a line with all coordinates nonzero is isomorphic to \(\mathbb P^1\). Finally, setting \(r=2\) gives \(k=n-1\), and \((n-1)/\gcd(n-1,2)\) grows without bound.

## Verification
The proof uses the exact cocircuit criterion for Cartier multiples of the canonical class, not a finite enumeration as a substitute for a general proof. The edge cases give index \(1\) for \(r=1\), \(r=n\) (so \(k=1\)), and \(r=n-1\) (so \(k=2\)). For \(k=3\) and \(k=4\), the formula gives indices \(3\) and \(2\), respectively. These are consistency checks only; the subset-comparison argument proves the formula for every allowed pair \((r,n)\).

## Relationship to prior work
Porcher gives a general cocircuit-weight criterion for when a matroid Schubert variety is Gorenstein or \(\mathbb Q\)-Gorenstein, and illustrates it with the uniform matroid \(U_{2,3}\), the non-Fano matroid, and \(M(K_4)\). The present result does not claim that criterion as new: it computes the least positive multiple of the canonical divisor that is Cartier for every uniform matroid and proves unboundedness in rank two. Crowley and Proudfoot provide the canonical orbit-divisor framework used in the Cartier-class calculation, but the inspected sections do not state this uniform-family index formula.

## Limitations
The result is specific to uniform matroids. It does not give a formula for the index of a general matroid Schubert variety, nor does it classify canonical, terminal, or other singularity properties. The general cocircuit criterion makes the computation accessible; the contribution here is the exact minimal index and the resulting unbounded family. The literature search was not exhaustive.

## References
1. T. Porcher, “When is the matroid Schubert variety \(\mathbb Q\)-Gorenstein?”, arXiv:2608.21637v1, first posted 2026-08-21. See Theorem 1.1, Propositions 4.2–4.3, and the proof of Theorem 1.1. https://arxiv.org/abs/2608.21637
2. C. Crowley and N. Proudfoot, “The geometry of zonotopal algebras II: Orlik–Terao algebras and Schubert varieties,” arXiv:2505.05324v1, first posted 2025-05-08. See Section 1.4 for the canonical orbit-divisor framework. https://arxiv.org/abs/2505.05324
