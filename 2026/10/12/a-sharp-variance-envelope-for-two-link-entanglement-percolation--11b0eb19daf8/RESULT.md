# A sharp variance envelope for two-link entanglement percolation
## Finding
Let \(X\) be any random variable supported on \([0,1]\), with \(\mathbb E X=1/2\) and \(\operatorname{Var}(X)=v\), where \(0\le v\le 1/4\). For two independent copies \(X_1,X_2\), set \(q(X)=\mathbb E\min\{X_1,X_2\}\). Then the **exact lower envelope over all probability laws**, without density, regularity, symmetry, or unimodality assumptions, is
\[
\inf q(X)=q_*(v)=\begin{cases}
\frac12-\sqrt{v/3},&0\le v\le\frac1{12},\\[3pt]
\frac7{16}-\frac32v+3v^2,&\frac1{12}\le v\le\frac14.
\end{cases}
\]
Every infimum is attained by a unique law. For \(0<v<1/12\), it is the uniform distribution on
\[
\bigl[\frac12-\sqrt{3v},\ \frac12+\sqrt{3v}\bigr].
\]
For \(1/12<v<1/4\), define \(\alpha=3v-1/4\) and \(\beta=1-2\alpha\). The unique minimizing law places mass \(\alpha\) at each of \(0\) and \(1\), and has a constant density \(\beta\) on \((0,1)\). At \(v=0\) it is the point mass at \(1/2\); at \(v=1/12\) it is uniform on \([0,1]\); at \(v=1/4\) it has mass \(1/2\) at each endpoint. Thus the minimizing distribution undergoes a sharp transition from a compact interior uniform law to a uniform interior component with two endpoint atoms at \(v=1/12\).

In the independent double-bond honeycomb-to-triangular two-link swapping construction, define the triangular-lattice bond threshold \(\tau=2\sin(\pi/18)\). With the input mean fixed at \(1/2\), the transformed bond probability is supercritical for **every** admissible input law of variance \(v\) if and only if
\[
0\le v<v_{\mathrm{crit}}:=3\bigl(\frac12-2\sin(\pi/18)\bigr)^2=0.069955209282967\ldots .
\]
At equality there is a critically tuned law; above it there is an admissible subcritical witness law. This is a **distribution-uniform guarantee for the specified protocol**, not a claim of global local-operation optimality or a statement that all laws above the variance threshold are subcritical.

## Assumptions and scope
An input link carries a pure two-qubit state with singlet conversion probability \(X=2\lambda_{\min}\in[0,1]\). Independent input links have independent, identically distributed values \(X\). The established two-link swapping rule yields \(\min\{X_1,X_2\}\). We use this rule exactly as an input and optimize the expected output success over all probability measures supported on the physically admissible compact interval. The critical-lattice corollary additionally requires the transformed links to be independent, as in the double-bond multigraph construction using distinct initial links for each swap; correlations across outputs are not permitted by this corollary.

The fixed mean is exactly \(1/2\), and the variance is fixed, not bounded above. No statement is asserted for unequal input means, correlated links, or different swapping operations.

## Proof
**Step 1 (CDF reduction, including atoms).** For \(t\in(0,1)\), let \(F(t)=\Pr(X\le t)\). Standard layer-cake identities, valid with endpoint atoms, give
\[
\int_0^1F(t)\,dt=1-\mathbb EX=\frac12,
\qquad
\int_0^1tF(t)\,dt=\frac{1-\mathbb EX^2}{2}=\frac38-\frac v2.
\]
Independence gives \(q(X)=\int_0^1[1-F(t)]^2\,dt\). Since \(\int F=1/2\), this equals \(\int_0^1F(t)^2\,dt\). We must therefore minimize the strict convex quadratic \(\int F^2\) under the two displayed linear constraints and \(0\le F\le1\); every admissible distribution gives such an \(F\).

**Step 2 (universal affine-clipping certificate).** Suppose an affine function \(L(t)=a+bt\) has a clipped version \(F_*(t)=\max\{0,\min\{1,L(t)\}\}\) satisfying the two moment constraints. For any admissible CDF \(F\), put \(H=F-F_*\). The moment constraints imply \(\int_0^1H(t)L(t)\,dt=0\). Furthermore,
\[
H(t)[F_*(t)-L(t)]\ge0
\]
pointwise: if \(L<0\), then \(F_*=0\), \(H\ge0\), and \(F_*-L>0\); if \(L>1\), then \(F_*=1\), \(H\le0\), and \(F_*-L<0\); otherwise the product is zero. Consequently,
\[
\int_0^1(F^2-F_*^2)\,dt
=\int_0^1H^2\,dt+2\int_0^1H(F_*-L)\,dt
\ge\int_0^1H^2\,dt\ge0.
\]
Equality forces \(F=F_*\) almost everywhere. CDFs agreeing almost everywhere determine the same law (including endpoint atoms), so the optimizer is unique.

**Step 3 (two explicit regimes).** For \(0<v\le1/12\), let \(\ell=\sqrt{12v}\) and \(c=(1-\ell)/2\). Set \(L(t)=(t-c)/\ell\), whose clipped version is the CDF of the uniform law on \([c,c+\ell]\). This has mean \(1/2\), variance \(\ell^2/12=v\), and
\[
\int_0^1F_*^2\,dt=\frac\ell3+(1-c-\ell)=\frac12-\frac\ell6=\frac12-\sqrt{v/3}.
\]
For \(1/12\le v\le1/4\), let \(\alpha=3v-1/4\in[0,1/2]\), \(\beta=1-2\alpha\), and \(L(t)=\alpha+\beta t\). This is already in \([0,1]\) for \(0<t<1\) and is the CDF of the two-endpoint-atom plus uniform law. Its mean is \(\alpha+\beta/2=1/2\), its second moment is \(\alpha+\beta/3=1/4+v\), and
\[
\int_0^1F_*^2\,dt=\alpha^2+\alpha\beta+\frac{\beta^2}{3}
=\frac7{16}-\frac32v+3v^2.
\]
The two formulas agree at \(v=1/12\); the unique zero-variance case is \(X=1/2\) almost surely. Step 2 proves optimality and uniqueness across **all**, not merely symmetric or continuous, probability laws.

**Step 4 (sharp lattice guarantee).** The triangular bond threshold is \(\tau=2\sin(\pi/18)\), which lies strictly between \(1/3\) and \(1/2\). The function \(q_*(v)\) decreases strictly from \(1/2\) to \(1/3\) on \([0,1/12]\) and continues decreasing from \(1/3\) to \(1/4\) on \([1/12,1/4]\). Its unique crossing of \(\tau\) therefore occurs in the first regime at \(v_{\mathrm{crit}}=3(1/2-\tau)^2\). Below this variance every law has \(q(X)\ge q_*(v)>\tau\), and the independent transformed bond process is supercritical. At or above the critical variance, the unique minimizing law gives \(q(X)\le\tau\); in particular the strict universal supercritical guarantee fails. This establishes the claimed if-and-only-if guarantee.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 standard library only. The verifier performs exact rational moment and quadratic-integral checks for six interior-uniform widths and six endpoint-atom variances; random discrete-law stress tests of the claimed inequality using 16,000 symmetric and 10,000 asymmetric mean-preserving laws; endpoint matching; and numerical comparison with the triangular threshold. It prints \(\texttt{VERIFY\_OK}\) and 36,055 completed checks. This finite testing is not a substitute for the affine-clipping proof, which covers all distributions and all admissible variances.

## Relationship to prior work
Romancino, Romero-Pallejà, Palma, and Sanpera establish the minimum-of-two swapping rule, the independence mechanism of the double-bond lattice, and the distributional identity for the expected minimum (their Section 3.2, equations (6)–(14)). Their explicit threshold calculation treats uniform inputs, and their general formula treats location-scale families. The result here supplies a different, distributionally robust theorem: the exact least possible swapped success probability at each fixed mean-half variance, its unique extremizing law throughout the entire admissible variance interval, the change in the topology of that law at \(v=1/12\), and the sharp uniform triangular-lattice threshold.

The objective is equivalently a Gini mean-difference extremal problem, since \(\mathbb E\min\{X_1,X_2\}=\mathbb EX-\tfrac12\mathbb E|X_1-X_2|\). Classical Gini-moment inequalities already bound this dispersion and explain the first (interior-uniform) regime. The support-induced endpoint-atomic branch is not inferred from the unrestricted variance-only inequality. Liu, Vanduffel, Xia, and Yao study related Gini deviation optimization with Wasserstein ambiguity sets, whereas the present class has a hard physical support constraint and no Wasserstein reference law. General classical Gini-bound literature is a priority risk, not grounds for claiming that the scalar objective itself is new.

## Limitations
The model fixes the input mean at \(1/2\) and assumes independent identically distributed input links. The theorem determines the worst-case **mean** output conversion probability, not its entire distribution, multi-hop correlations, or an optimal strategy among all local operations. Above the critical variance it produces a subcritical witness but does not imply every law at that variance is subcritical. The first-regime Gini inequality is classical in spirit; no priority claim is made for the familiar identity or a variance-only bound. An equivalent hard-support fixed-moment Gini optimization might exist in earlier inaccessible or unindexed inequality literature. Independent scientific audit has not been performed.

## References
1. A. Romancino, J. Romero-Pallejà, G. M. Palma, A. Sanpera, *Entanglement percolation in random quantum networks*, arXiv:2602.10189 (first version 2026-02-10; Section 3.2, consulted in the openly available revised version at https://arxiv.org/html/2602.10189v2).
2. P. Liu, S. Vanduffel, Y. Xia, J. Yao, *Robust Distortion Risk Metrics with Wasserstein and Unimodal Constraints*, arXiv:2511.08662 (https://arxiv.org/html/2511.08662v2), Section 2 and Section 3 (distinct Wasserstein-constrained Gini optimization setting).
3. P. Cerone, *Bounding the Gini Mean Difference*, International Series of Numerical Mathematics 157, 77–89 (2008), DOI:10.1007/978-3-7643-8773-0_8 (abstract available at https://vuir.vu.edu.au/5289/; full text not accessible for complete priority comparison).
4. R. Vila, N. Balakrishnan, H. Saulo, *An upper bound and a characterization for Gini's mean difference based on correlated random variables*, arXiv:2301.07229 (2023), https://arxiv.org/abs/2301.07229 (broader dispersion inequalities).
