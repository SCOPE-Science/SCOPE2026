# Strict likelihood-ratio ordering of same-part distances in complete-bipartite uniform spanning trees

## Finding
Fix integers \(a>b\ge 2\). Choose a spanning tree uniformly from the spanning trees of the simple complete bipartite graph \(K_{a,b}\), with labeled vertex classes \(A\) and \(B\). Let \(D_A\) be the tree distance between any two fixed distinct vertices of \(A\), and let \(D_B\) be the analogous distance for two fixed distinct vertices of \(B\). The two variables denote marginal laws; no simultaneous coupling is assumed.

**Theorem.** The laws of \(D_A/2\) and \(D_B/2\) satisfy the strict monotone likelihood-ratio order
\[
D_B/2 <_{\mathrm{lr}} D_A/2.
\]
More explicitly, if \(p_A(j)=\Pr(D_A=2j)\) and \(p_B(j)=\Pr(D_B=2j)\), then \(p_A(j)/p_B(j)\) increases strictly for \(1\le j\le b-1\), wherever both probabilities are nonzero, and \(p_A(b)>0=p_B(b)\). In particular \(D_A\) is strictly larger than \(D_B\) in the usual stochastic order, so every strictly increasing real function has larger expectation on \(D_A\). If \(a=b\ge2\), the two laws coincide by symmetry.

For any integers \(a\ge2,b\ge1\), putting \(J_A=D_A/2\), the full finite-sample law is
\[
\Pr(J_A\ge j)=\prod_{i=1}^{j-1}\frac{(a-i-1)(b-i)}{ab},
\quad 1\le j\le\min(a-1,b)+1,
\]
where the empty product is \(1\), and the probability is \(0\) above that range. Equivalently, for \(1\le j\le\min(a-1,b)\),
\[
\Pr(J_A=j)=\frac{(a-2)_{\underline{j-1}}(b)_{\underline j}}{a^j b^{j+1}}
\bigl(j(a+b)+b-j(j+1)\bigr).
\]

## Assumptions and scope
The host graph is \(K_{a,b}\) and the probability measure is uniform over its spanning trees, not a minimum-spanning-tree model. Distinct endpoints are fixed in one bipartition class. Distances between vertices in the same part are even. The comparison requires \(a>b\ge2\); the exact one-part law also holds with \(b=1\) when only one of the two same-side comparisons is possible. Falling factorials obey \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\), with \((x)_{\underline0}=1\). All numerical and stochastic comparisons are finite-sample statements, for every indicated integer pair.

## Proof
**Path containment.** A prescribed alternating simple path with \(r\) vertices in \(A\) and \(s\) vertices in \(B\) is contained in exactly the spanning trees obtained by contracting its edges, preserving parallel edges. With \(x=a-r\) and \(y=b-s\), the reduced Laplacian of the contracted graph, deleting the contracted path's vertex, is
\[
L'=\begin{pmatrix}
bI_x&-\mathbf1_{x\times y}\\
-\mathbf1_{y\times x}&aI_y
\end{pmatrix}.
\]
Its determinant, by the rank-one determinant identity, is \(b^{x-1}a^{y-1}(ab-xy)\); boundary cases with \(x=0\) or \(y=0\) follow directly from the remaining diagonal block, and \(x=y=0\) has determinant \(1\). The standard complete-bipartite tree count is \(a^{b-1}b^{a-1}\). Therefore the prescribed path is present with probability
\[
\frac{ab-(a-r)(b-s)}{b^r a^s}.
\]

**Exact distance distribution.** If endpoints lie in \(A\), their unique path of length \(2j\) has \(j+1\) vertices of \(A\) and \(j\) of \(B\). There are \((a-2)_{\underline{j-1}}(b)_{\underline j}\) possible labeled paths. Two distinct such endpoint paths cannot both be the unique path in a tree; summing their containment probabilities yields the displayed mass \(p_A(j)\). The ratio of the displayed survival product at indices \(j+1\) and \(j\) is \((a-j-1)(b-j)/(ab)\). Thus its difference is exactly \(p_A(j)\), and the final product is zero. This proves normalization, the tail formula, and all support boundaries.

**Strict likelihood-ratio order.** Let \(n=a+b\) and \(C_j=j(n-j-1)\). For \(a>b\ge2\), on the common positive support \(1\le j\le b-1\), the ratio of the two masses is
\[
\frac{p_A(j)}{p_B(j)}
=\left[\prod_{i=1}^{j-1}
\frac{(a-i-1)(b-i)}{(b-i-1)(a-i)}\right]
\frac{C_j+b}{C_j+a}.
\]
Each factor added to the product when \(j\) increases is strictly greater than one: the numerator minus denominator of its inner fraction is precisely \(a-b>0\). The last fraction increases strictly with \(C_j\), since \(a>b\); and \(C_{j+1}-C_j=n-2j-2>0\) whenever \(j<b-1\). Hence the entire mass ratio is strictly increasing. The smaller part has maximal feasible index \(b-1\), while the larger part has index \(b\) with positive mass. This proves the strict likelihood-ratio order on the ordered union of supports. Strict stochastic order and all increasing-test consequences follow by the standard likelihood-ratio implication. Equal sizes give identical laws by side exchange.

## Verification
The standalone standard-library Python script `verify.py` performs exact rational checks of normalization, mass-tail identities and strict adjacent likelihood-ratio minors across \(2\le a\le30\), \(1\le b\le30\), plus **independent spanning-tree enumeration** for all \(2\le a,b\le4\). It completed **24,635 exact checks** with no failed assertion. This is supplementary finite evidence; the all-size theorem rests on the algebraic argument above. Run with `python verify.py`.

For example, on \(K_{4,3}\), the masses of \(D_A/2\) at \(j=1,2,3\) are \((2/3,11/36,1/36)\), while those of \(D_B/2\) are \((3/4,1/4,0)\). Their common-support likelihood ratios are \(8/9<11/9\), followed by the larger part's extra positive tail.

## Relationship to prior work
Chung, Horn and Lu, *Diameter of random spanning trees in a given graph*, publicly available in the 2011 journal edition, established general host-graph diameter estimates; the inspected preprint's spectral-gap setup explicitly treats nonbipartite graphs for those estimates and does not give a two-vertex, two-vertex-class likelihood-ratio comparison. Ge and Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs* (2019), Theorem 1.4, already give a more general formula for the number of spanning trees containing any prescribed tree. The present fixed-path containment count is an instance of that known theorem; **it is not claimed as new**. Dong and Ge (2021), Theorem 4, further subsume those containment counts by a fixed-spanning-forest formula. The assessed contribution here is the full same-part distance law together with the strict **cross-vertex-class likelihood-ratio ordering** and its finite-sample consequences, which the inspected theorems do not state. These published containment formulas provide a route to reconstruct the first step, but do not themselves assert the distributional order.

## Limitations
The result concerns only uniform spanning trees on complete bipartite host graphs; it does not concern minimum-weight trees, nonuniform edge weights, general bipartite graphs, or distances conditional on a full degree sequence. It supplies no independent expert audit and makes no claim about a new formula for prescribed-path inclusion. Published work may contain an implicitly equivalent likelihood-ratio comparison not identified in the checked sources; that is the principal remaining priority risk.

## References
- F. Chung, P. Horn and L. Lu, *Diameter of random spanning trees in a given graph*, Journal of Graph Theory 69 (2012), 223–240; first published online 2011-03-04, https://doi.org/10.1002/jgt.20577 ; accessible earlier-dated manuscript https://cs.du.edu/~paulhorn/pap/spanningtree-final.pdf .
- J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, 2019, Theorem 1.4, https://arxiv.org/abs/1904.07766 .
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, 2021, Theorem 4, https://arxiv.org/abs/2103.05294 .
