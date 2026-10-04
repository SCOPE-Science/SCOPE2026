# Finite-energy coarse recurrence has an unbounded product synchronization gap

## Finding
Fix \(p\in[1,\infty]\). For a map \(f:(X,d_X)\to(X,d_X)\) and \(x\in X\), define the positive coarse-recurrence threshold
\[
\rho_p(f,x):=\inf\{\varepsilon\ge0:x\in\mathrm{CR}^{\ell^p}_{\varepsilon}(f)\},
\]
where \(\mathrm{CR}^{\ell^p}_{\varepsilon}(f)\) is Yokoyama's positive \(\varepsilon\)-\(\ell^p\) chain-recurrent set. For maps \(f:X\to X\) and \(g:Y\to Y\), equip \(X\times Y\) with
\[
D_\infty((x,y),(x',y')):=\max\{d_X(x,x'),d_Y(y,y')\}.
\]
Then for \(F=f\times g\),
\[
\rho_p(F,(x,y))\ge \max\{\rho_p(f,x),\rho_p(g,y)\}.
\]
At the stepwise endpoint \(p=\infty\), this is always an equality:
\[
\rho_\infty(f\times g,(x,y))=\max\{\rho_\infty(f,x),\rho_\infty(g,y)\}.
\]
For every finite \(p\), however, the equality can fail by an arbitrarily large factor. More precisely, for every integers \(L,M\ge2\), let \(g_0=\gcd(L,M)\). There are finite metric systems with distinguished points \(s_L,s_M\) such that
\[
\rho_p(f_L,s_L)=\rho_p(f_M,s_M)=1
\]
but
\[
\rho_p(f_L\times f_M,(s_L,s_M))
=\left(\frac{M}{g_0}+\frac{L}{g_0}-1\right)^{1/p}.
\]
For coprime \(L,M\), the factor is \((L+M-1)^{1/p}\), so it is unbounded as the synchronization lengths grow.

## Assumptions and scope
Yokoyama defines an \(\varepsilon\)-\(\ell^p\) chain by bounding the \(\ell^p\)-norm of the sequence of one-step errors, and defines \(x\in\mathrm{CR}^{\ell^p}_{\varepsilon}(f)\) by requiring a return chain for every error budget strictly larger than \(\varepsilon\). The result uses only this positive branch of the filtration.

For the finite examples, fix a number \(D>1\). For \(L\ge2\), let
\[
X_L=\{s,q_0,\ldots,q_{L-1},z\}.
\]
Define a metric by \(d(s,q_{L-1})=1\) and by setting the distance between every other pair of distinct points equal to \(D\). Define
\[
f_L(s)=q_0,\qquad f_L(q_i)=q_{i+1}\quad(0\le i<L-1),\qquad f_L(q_{L-1})=z,\qquad f_L(z)=z.
\]
The metric is valid because every triangle has either all sides \(D\), or sides \(1,D,D\).

## Proof
Projection of a product chain onto either coordinate cannot increase any one-step error under \(D_\infty\). Therefore the \(\ell^p\)-norm of each projected error vector is at most the product error norm. This proves
\[
\rho_p(f\times g,(x,y))\ge\max\{\rho_p(f,x),\rho_p(g,y)\}.
\]

Now take \(p=\infty\), and put
\[
a=\max\{\rho_\infty(f,x),\rho_\infty(g,y)\}.
\]
For any \(\eta>a\), each factor has an \(\eta\)-chain returning its distinguished point to itself. If the two return chains have lengths \(m\) and \(n\), concatenate the first chain with itself \(n\) times and the second with itself \(m\) times. Concatenation does not enlarge the maximum one-step error, so both chains now have the same length \(mn\) and still have error at most \(\eta\). Pairing corresponding terms gives an \(\eta\)-chain for the product. Since this works for every \(\eta>a\),
\[
\rho_\infty(f\times g,(x,y))\le a,
\]
which proves equality.

For the finite synchronization examples, first consider one factor \((X_L,f_L,s)\). Any return chain from \(s\) whose \(\ell^p\)-error is strictly less than \(D\) cannot use a jump of metric size \(D\). Hence every step must be exact except possibly the unique short jump from the image \(q_{L-1}=f_L(q_{L-2})\) back to \(s\). Starting from \(s\), exact motion reaches \(q_{L-2}\) just before step \(L\), so the short reset produces a return chain of length \(L\) with one error equal to \(1\). If that reset is skipped, the orbit proceeds to \(q_{L-1}\), then to the absorbing point \(z\), from which no return is possible without a jump of size \(D\). Thus every low-error return to \(s\) has length \(kL\) and contains exactly \(k\) unit errors. In particular,
\[
\rho_p(f_L,s)=1.
\]

Consider the product of the \(L\)- and \(M\)-systems with the max metric, and choose
\[
D>\left(\frac{M}{g_0}+\frac{L}{g_0}-1\right)^{1/p}
\]
when \(p<\infty\). Any return chain cheaper than \(D\) again uses only exact moves and unit resets. To return both coordinates, its length must be a common multiple of \(L\) and \(M\). In one minimal synchronization block of length \(\operatorname{lcm}(L,M)\), the first coordinate resets at each multiple of \(L\), the second at each multiple of \(M\), and both reset simultaneously only at the final common multiple. Therefore the number of product steps carrying unit error is exactly
\[
\frac{\operatorname{lcm}(L,M)}{L}+\frac{\operatorname{lcm}(L,M)}{M}-1
=\frac{M}{g_0}+\frac{L}{g_0}-1.
\]
The \(\ell^p\)-norm of this product error vector is the claimed \(p\)-th root. Repeating the synchronization block only increases that norm, while any chain containing a size-\(D\) jump costs at least \(D\). Hence the displayed value is the exact threshold.

## Verification
The proof above is symbolic and covers all integers \(L,M\ge2\) and all \(p\in[1,\infty]\). A finite-state checker is included only as a sanity test: it reconstructs the transition-cost graph, computes least positive return energies by Dijkstra search, and verifies the count formula on representative small values. The checker is not used as an infinite proof.

The key boundary check is the endpoint \(p=\infty\): the same synchronization construction has maximum error \(1\), regardless of how many reset steps occur, exactly matching the general product equality. For finite \(p\), the repeated unit resets accumulate and create the synchronization gap.

## Relationship to prior work
Yokoyama's arXiv:2504.01325 introduces the positive \(\varepsilon\)-\(\ell^p\) chain-recurrence filtration, its pointwise potential, and the associated circulation-cost interpretation under bounded control or noise. The inspected full text does not discuss Cartesian products.

Wiseman's arXiv:1607.03465 studies product recurrence at the zero-error limit. It proves the ordinary chain-recurrent product identity and analyzes strong chain recurrence, explicitly emphasizing that concatenating strong chains accumulates total error. Those results do not determine the positive coarse threshold introduced later by Yokoyama, nor the exact synchronization factor above. The present result quantifies that accumulation at positive control scale and shows a sharp dichotomy between the stepwise endpoint \(p=\infty\) and every finite \(p\).

## Limitations
The exact amplification formula is proved for a concrete family of finite metric systems and the max product metric. It shows that no universal max formula can hold for finite \(p\), but it does not classify all product thresholds or optimize over all compatible product metrics. The result addresses only the positive coarse-recurrence branch; it does not assert a product law for Yokoyama's negative-error non-gradient branch or for coarse Morse graphs.

## References
1. T. Yokoyama, *Coarse chain recurrence, Morse graphs with finite errors, and persistence of circulations*, arXiv:2504.01325. First public version: 2025-04-02.
2. J. Wiseman, *Generalized Recurrence and the Nonwandering Set for Products*, arXiv:1607.03465, 2016.
3. E. Akin and J. Wiseman, *Chain Recurrence and Strong Chain Recurrence on Uniform Spaces*, Contemporary Mathematics 736 (2019), 1--29.
