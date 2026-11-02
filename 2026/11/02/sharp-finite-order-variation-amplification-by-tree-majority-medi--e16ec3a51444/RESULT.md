# Sharp finite-order variation amplification by tree majority-median filters

## Finding
Let \(T=(V,E)\) be any finite simple tree on \(n\ge2\) vertices. For a real function \(f:V\to\mathbb R\), define its **neighbor-majority median** \(M_T f\) as follows: at a vertex of odd degree, take the median of the values at its neighbors; at a vertex of even degree, take the median of those neighbor values together with the value at the vertex itself. In either case the sample has odd size. Equip functions modulo constants with edge variation
\[
J_T(f)=\sum_{uv\in E}|f(u)-f(v)|.
\]
Then the exact sharp constant simultaneously over all \(n\)-vertex trees and all nonconstant real signals is
\[
\boxed{\sup_{|V(T)|=n}\ \sup_{J_T(f)>0}\frac{J_T(M_Tf)}{J_T(f)}
=2-\frac{1}{\lfloor n/2\rfloor}.}
\]
In particular the optimal universal constant over all finite trees is \(2\), not attained on any fixed finite tree. For a binary coloring \(x\) and its simultaneous majority update \(y=M_Tx\), let \(F=\{v:x(v)\ne y(v)\}\). When \(F\ne\varnothing\), a stronger cut-deficit inequality holds:
\[
\boxed{J_T(y)\le 2J_T(x)-c(F),}
\]
where \(c(F)\) is the number of connected components in the forest induced by \(F\). The finite-order constant is attained by explicitly described binary inputs on a star (even \(n\)) or a once-subdivided star (odd \(n\ge5\)); \(n=2,3\) are handled separately.

## Assumptions and scope
The tree is connected, finite, unweighted, with no isolated vertices. The update is simultaneous, not sequential, and **uses neighbors only when the degree is odd**. At even degree it includes the current value to resolve ties in favor of the current state for binary inputs. In particular it differs from taking the median of the closed neighborhood at every vertex. All vertex data are arbitrary real numbers; the variation has unit weight on each tree edge. The result is a one-input gain bound \(J_T(M_Tf)/J_T(f)\), not a claim about the two-input Lipschitz constant of \(M_T\).

## Proof
**1. Binary flip inequality.** Let \(x:V\to\{0,1\}\), and let \(y=M_Tx\). A vertex changes if and only if strictly more than half of its neighbors disagree with its old color: the old color wins any even-degree tie. Write \(F=\{v:y(v)\ne x(v)\}\). For a vertex \(v\in F\), let \(b_v\) count incident edges whose endpoints initially have different colors. The strict-majority condition gives \(2b_v-\deg(v)\ge1\).

If \(F\ne\varnothing\), partition the edges meeting \(F\) as follows: \(a\) originally monochromatic edges from \(F\) to its complement, \(b\) originally bichromatic such edges, \(c\) originally bichromatic edges inside \(F\), and \(d\) originally monochromatic edges inside \(F\). Summing the strict-majority inequalities over all \(v\in F\) yields
\[
|F|\le b-a+2(c-d),\qquad a-b\le2(c-d)-|F|.
\]
Only edges with exactly one endpoint in \(F\) change whether they are bichromatic, so \(J_T(y)-J_T(x)=a-b\). Because the graph induced by \(F\) is a forest with \(|F|-c(F)\) edges, \(c+d\le|F|-c(F)\), hence
\[
a-b\le2c-|F|\le c-c(F)\le J_T(x)-c(F).
\]
This proves \(J_T(y)\le2J_T(x)-c(F)\). If \(F=\varnothing\), the variation is unchanged.

**2. The finite-order upper bound.** On a tree, \(0\le J_T(y)\le n-1\). If \(x\) is nonconstant, write \(k=J_T(x)\in\{1,\ldots,n-1\}\). By Step 1, whether or not any vertex changes,
\[
\frac{J_T(y)}{J_T(x)}\le
\max\left\{1,\min\left(2-\frac1k,\frac{n-1}{k}\right)\right\}.
\]
Indeed, the displayed inequality is immediate for \(F=\varnothing\), and for nonempty \(F\) it follows from \(c(F)\ge1\). Put \(q=\lfloor n/2\rfloor\). The function \(2-1/k\) increases with \(k\), whereas \((n-1)/k\) decreases. Their crossover is at \(k=n/2\). For even \(n=2q\) the largest integer value of the minimum is \(2-1/q\), at \(k=q\). For odd \(n=2q+1\), the only possibly maximizing values are \(k=q\) and \(k=q+1\), giving \(2-1/q\) and \(2q/(q+1)\), respectively; the first is at least the second since \(q\ge1\). Therefore \(J_T(M_Tx)\le(2-1/q)J_T(x)\) for every binary \(x\).

**3. Transfer to arbitrary real signals.** For every real threshold \(t\) not equal to a vertex value, taking an odd-sized median commutes with thresholding:
\[
\mathbf 1_{\{M_Tf>t\}}=M_T\bigl(\mathbf 1_{\{f>t\}}\bigr),
\]
where the right-hand operator is the binary majority update. The graph coarea identity holds exactly:
\[
J_T(f)=\int_{-\infty}^{\infty}J_T\bigl(\mathbf1_{\{f>t\}}\bigr)\,dt.
\]
Integrating the binary bound gives the asserted inequality for all real \(f\). The finitely many thresholds equal to data values have zero measure.

**4. Sharpness.** Let \(n=2q\), with \(q\ge1\). Choose a star with center value \(0\), exactly \(q\) leaves of value \(1\), and the remaining \(q-1\) leaves of value \(0\). The center changes to \(1\), all leaves copy its old value \(0\), and the initial and final variations are \(q\) and \(2q-1\). Their ratio is \(2-1/q\).

For \(n=2q+1\) with \(q\ge2\), begin with the previous star on \(2q\) vertices and subdivide one of its center-to-zero-leaf edges with an additional zero-valued vertex. That vertex and the adjacent zero leaf stay at zero; the center still changes to one and the other leaves copy zero. Thus the original \(q\) boundary edges become \(2q-1\) boundary edges, again attaining \(2-1/q\). For \(n=3\), take the three-vertex path with center zero and both leaves one: both variations are two, giving the required constant one. The two-vertex tree likewise has gain one on nonconstant binary signals. This proves sharpness for every \(n\ge2\).

## Verification
Run the included standalone Python program with `python check.py`. It uses only the Python standard library. It enumerates all labeled trees via Prüfer words for \(2\le n\le6\) and every nonconstant binary signal, checking both the sharp finite-order bound and the component-count deficit. It also tests randomized larger trees with integer-valued data and the explicit sharpness construction at every order through \(150\). The observed results were: 1,441 labeled trees, 84,346 binary configurations, 4,320 larger-tree real-signal cases, and 149 exact sharpness examples. All assertions passed. These finite checks test implementation and boundary cases; Steps 1–4 prove the infinite family of orders.

## Relationship to prior work
Synchronous majority dynamics and inertia-based tie resolution are standard: see Tamuz–Tessler (arXiv:1307.4035) and Benjamini–Chan–O'Donnell–Tamuz–Tan (arXiv:1405.2486). The former studies information retention and a temporal Lyapunov functional; the latter studies long-term stabilization and stochastic consensus. Neither source's inspected results gives the one-step edge-total-variation growth envelope \(2-1/\lfloor n/2\rfloor\). The later finite-tree study of Benjamini–Zakharov–Zhukovskii (2026) establishes exact stabilization times rather than this variation norm. The contribution assessed here is the forest-flip deficit, the exact finite-order bound, and the extension from binary majority updates to real median filtering by coarea; the majority update itself is not claimed as new.

## Limitations
The sharpness maximum ranges over all unweighted trees of fixed order; the exact constant for each individual tree is not classified. Weighted variation, non-tree graphs, asynchronous updates, different median neighborhoods, and two-input Lipschitz moduli are not covered. No independent audit or exhaustive literature certification is claimed. Earlier equivalent results outside the inspected literature remain possible.

## References
1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, first public version July 15, 2013, https://arxiv.org/abs/1307.4035.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486, first public version May 11, 2014, https://arxiv.org/abs/1405.2486.
3. I. Benjamini, G. Zakharov and M. Zhukovskii, *Majority Dynamics on Finite Trees*, Random Structures & Algorithms 69 (2026), e70092, https://doi.org/10.1002/rsa.70092. Included only for comparison, not to set the historical eligibility date.
