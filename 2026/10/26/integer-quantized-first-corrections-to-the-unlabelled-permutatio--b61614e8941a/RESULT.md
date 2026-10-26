# Integer-quantized first corrections to the unlabelled-permutation first-order zero-one law

## Finding
Let \(P_n\) be uniformly chosen among the isomorphism classes of bijections on an \(n\)-element set: equivalently, choose a uniformly random integer partition of \(n\) and take one directed cycle per part. Interpret \(P_n\) in the first-order relational signature with one binary symbol \(R\), where \(R(x,y)\) means that \(y\) is the image of \(x\).

For **every** first-order sentence \(\varphi\) in this signature there are **effectively computable** integers \(\varepsilon_\varphi\in\{0,1\}\) and \(M_\varphi\in\mathbb Z\), with \(M_\varphi\geq0\) if \(\varepsilon_\varphi=0\) and \(M_\varphi\leq0\) if \(\varepsilon_\varphi=1\), such that
\[
\Pr(P_n\models\varphi)=\varepsilon_\varphi+\frac{\pi M_\varphi}{\sqrt{6n}}+O_\varphi(n^{-1}).
\]
Conversely, **every** pair \((0,m)\) and \((1,-m)\) with \(m\) any nonnegative integer occurs. Thus the complete attainable first-correction spectrum is the signed integer lattice in units of \(\pi/\sqrt6\), not merely the previously known \(\{0,1\}\) limit spectrum. If \(M_\varphi=0\), convergence improves to \(O_\varphi(n^{-1})\); if it is nonzero, the \(n^{-1/2}\) rate is sharp for that sentence.

## Assumptions and scope
The probability space consists of **isomorphism classes** of bijections, all weighted equally, *not* of the \(n!\) labelled permutations with equal weight. Let \(p(n)\) be the number of integer partitions of \(n\), and set \(p(t)=0\) for negative integers \(t\). Let \(a_j\) be the number of cycles of length \(j\). The language has only equality and the directed successor relation \(R\); it has neither an ambient linear order nor a global counting operator. The sentence \(\varphi\) and its quantifier rank are fixed as \(n\to\infty\). All asymptotic constants may depend on \(\varphi\).

## Proof
**1. Exact cycle-multiplicity identities and their asymptotics.** Deleting \(r\) copies of the part \(j\) bijects partitions of \(n\) with \(a_j\geq r\) with all partitions of \(n-rj\). Hence, for fixed \(j\geq1\), \(r\geq0\),
\[
\Pr(a_j\geq r)=\frac{p(n-rj)}{p(n)},\qquad
\Pr(a_j=r)=\frac{p(n-rj)-p(n-(r+1)j)}{p(n)}.
\]
The refined Hardy--Ramanujan partition asymptotic (or the leading Rademacher term with its exponentially smaller remainder), expanded at any *fixed* integer shift \(h\), gives
\[
\frac{p(n-h)}{p(n)}=1-\frac{\pi h}{\sqrt{6n}}+O_h(n^{-1}).
\]
Therefore, for each fixed \(j,r\),
\[
\Pr(a_j=r)=\frac{\pi j}{\sqrt{6n}}+O_{j,r}(n^{-1}). \tag{1}
\]
For different fixed \(j\neq \ell\), prescribing both multiplicities to fixed values \(r,s\) yields a mixed finite difference:
\[
\Pr(a_j=r,a_\ell=s)=\frac{p(n-rj-s\ell)-p(n-(r+1)j-s\ell)-p(n-rj-(s+1)\ell)+p(n-(r+1)j-(s+1)\ell)}{p(n)}=O_{j,\ell,r,s}(n^{-1}). \tag{2}
\]
Indeed the constant and first-order terms of the four shifted partition ratios cancel. Thus any **two distinct bounded small-cycle multiplicity defects** have joint probability \(O(n^{-1})\).

**2. Finite logical locality.** Regard a bijection as a directed degree-two cycle graph. The effective bounded-degree Hanf theorem supplies, from \(\varphi\), a radius \(\rho\geq0\) and a vertex-count threshold \(t\geq1\) such that two finite bijections agreeing in the count of each rooted radius-\(\rho\) neighborhood below \(t\), and with counts at least \(t\) in both when the threshold is reached, agree on \(\varphi\). Set \(K=2\rho+1\). A rooted neighborhood in a cycle of length \(j\leq K\) determines \(j\) and is realized by exactly \(j a_j\) vertices. Every cycle of length \(>K\) has the same rooted radius-\(\rho\) neighborhood (a directed path). Consequently the Hanf data for \(\varphi\) consist solely of the truncated numbers
\[
\min(t,j a_j),\quad 1\leq j\leq K,
\]
and the truncated number \(\min(t,V_{>K})\) of vertices lying in longer cycles. Define \(T_j=\lceil t/j\rceil\). A fully saturated representative \(B_\infty\) has \(T_j\) cycles of each length \(j\leq K\) and one long cycle of length exceeding \(\max(K,t)\). For each \(j\leq K\) and \(0\leq r<T_j\), a single-defect representative \(B_{j,r}\) has exactly \(r\) cycles of length \(j\), \(T_\ell\) cycles of every other short length \(\ell\), and the same long cycle. All these are explicit finite structures; evaluating a sentence on them is a terminating finite computation.

**3. Longer cycles are saturated with negligible exceptional probability.** If \(V_{>K}<t\), then the partition of \(n\) has at most \(t-1\) total vertices in parts longer than \(K\). The number of choices for these exceptional long parts is bounded independently of \(n\) (their total size is bounded), and the number of remaining partitions into parts \(\leq K\) is polynomial in \(n\) of degree at most \(K\). Since \(p(n)=\exp(\pi\sqrt{2n/3}+O(\log n))\),
\[
\Pr(V_{>K}<t)=\exp(-\Omega_{\varphi}(\sqrt n)). \tag{3}
\]

**4. Extract the first correction.** Let \(b_\infty=\mathbf1\{B_\infty\models\varphi\}\) and \(b_{j,r}=\mathbf1\{B_{j,r}\models\varphi\}\). Define the *integer*
\[
M_\varphi=\sum_{j=1}^{K}j\sum_{r=0}^{T_j-1}(b_{j,r}-b_\infty). \tag{4}
\]
Outside the negligible event (3), Hanf locality identifies the value of \(\varphi\) with \(b_\infty\), except when at least one \(a_j<T_j\). By (2), configurations with two such defects contribute only \(O_\varphi(n^{-1})\). For a single defect \(a_j=r<T_j\), other defects can be discarded at the same order. Inserting (1) and summing finitely many possibilities gives
\[
\Pr(P_n\models\varphi)=b_\infty+\frac{\pi}{\sqrt{6n}}\sum_{j=1}^{K}j\sum_{r=0}^{T_j-1}(b_{j,r}-b_\infty)+O_\varphi(n^{-1}).
\]
Thus \(\varepsilon_\varphi=b_\infty\) and \(M_\varphi\) is computed by (4). Since each \(b\) is zero or one, (4) also forces the claimed sign restriction.

**5. Every permitted coefficient occurs.** For each integer \(m\geq1\), the first-order sentence asserting **there is no \(m\)-cycle** has probability
\[
\frac{p(n)-p(n-m)}{p(n)}=\frac{\pi m}{\sqrt{6n}}+O_m(n^{-1}),
\]
so realizes \((\varepsilon,M)=(0,m)\); its negation realizes \((1,-m)\). The always-false and always-true sentences realize the two \(m=0\) cases. An \(m\)-cycle is definable by quantifying \(m\) distinct vertices and asserting that \(R\) cyclically connects them, so all witnesses belong to the stated signature.

## Verification
A standalone standard-library Python checker, `checker.py`, tests the exact cycle-multiplicity identity by exhaustive enumeration of integer partitions through \(n=17\), checks fixed-shift first-term numerical bounds at selected larger \(n\), and tests mixed differences for two distinct short-cycle lengths. Its observed signal is `UNLABELLED_FO_FIRST_CORRECTION_FINITE_OK 527 partition_n 297 p3500_digits 62`. These are finite arithmetic consistency checks, **not** an infinite proof or an exhaustive search of all sentences. The general proof is steps 1--5 above.

## Relationship to prior work
The **unlabelled first-order zero-one law itself is previously known**, including Compton's first-order asymptotic-combinatorics framework and the explicit reference in Albert--Bouvel--Féray, *Two first-order logics of permutations*, to a zero-one law for unlabelled models of one bijection. Burris--Compton--Odlyzko--Richmond provide broad fine-spectrum criteria for zero-one laws. Woods proves an unlabelled MSO convergence theorem for appropriate component classes. No part of these qualitative results is claimed here as new. The contribution assessed here is the **universal explicit first-order correction, its integer quantization, the improved \(O(n^{-1})\) remainder, and the complete realizable coefficient spectrum**, which are not supplied by a bare zero-one or convergence law. Koponen's 2026 analysis of finite model properties and logical convergence motivates distinguishing what the asymptotic finite structures determine at finer scales; it does not imply (4).

## Limitations
The result concerns uniform **isomorphism classes**, not uniform labelled permutations, and only the directed-bijection signature. It gives one correction term, not a full all-orders asymptotic series. It does not extend automatically to monadic second-order sentences, additional unary colours, or linear orders. Earlier comprehensive quantitative results may exist outside accessible sources; broad prior first-order-zero-one papers must be checked for this precise coefficient. Independent scientific validation has not been performed.

## References
1. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first public 2026-10-12), especially the discussion of finite-model properties and logical convergence.
2. M. Albert, M. Bouvel, V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459v2; *Journal of Combinatorial Theory, Series A* **171** (2020), 105158.
3. S. Burris, K. Compton, A. Odlyzko, B. Richmond, *Fine Spectra and Limit Laws, II: First-Order 0--1 Laws*, *Canadian Journal of Mathematics* **49** (1997), 641--652, doi:10.4153/CJM-1997-030-6.
4. A. R. Woods, *Counting finite models*, *Journal of Symbolic Logic* **62** (1997), 925--949, doi:10.2307/2275580.
5. G. H. Hardy and S. Ramanujan, *Asymptotic formulae in combinatory analysis*, *Proceedings of the London Mathematical Society* (1918), doi:10.1112/plms/s2-17.1.75.
6. L. Libkin, *Elements of Finite Model Theory*, Springer (2004), chapter on locality and Hanf's theorem.
