# Sharp two-node Szegő-kernel approximation of the quadratic Hardy monomial

## Finding
In the classical Hardy Hilbert space \(H^2(\mathbb D)\), let \(k_a(z)=(1-\overline a z)^{-1}\) and \(f(z)=z^2\). For distinct nodes \(a,b\in\mathbb D\), write \(V_{a,b}=\operatorname{span}\{k_a,k_b\}\). Allow a repeated node by taking the confluent span of \(k_a\) and \(\partial_{\overline a}k_a\). Then
\[
\sup_{a,b\in\mathbb D}\|P_{V_{a,b}}f\|_{H^2}^2=\frac7{16},\qquad
\inf_{a,b\in\mathbb D}\|f-P_{V_{a,b}}f\|_{H^2}^2=\frac9{16}.
\]
All optimal configurations consist of **distinct** nodes. Up to interchange and a common rotation, these nodes are exactly
\[
a=\frac{1+i}{2},\qquad b=\frac{1-i}{2}.
\]
Thus their common modulus is \(1/\sqrt2\) and their angular separation is \(\pi/2\). The optimal (unsquared) approximation error is \(3/4\).

## Assumptions and scope
The inner product is \(\langle f,g\rangle=\sum_{m\ge0}f_m\overline{g_m}\) for analytic coefficient sequences; \(\|z^2\|=1\). The infimum is over complex coefficients multiplying two Szegő kernels with unrestricted nodes in the open disk; for repeated nodes, a first kernel derivative is permitted, as in the standard multiplicity-aware kernel approximation problem. No restriction to real nodes or interpolation data is imposed. The result is for exactly two kernel dimensions and the target quadratic monomial; no claim is made about other target functions or about general pole counts.

## Proof
**1. Model-space reduction.** For the unordered pair (with multiplicity) define the degree-two Blaschke product, up to an irrelevant unimodular constant,
\[
B(z)=\frac{(z-a)(z-b)}{(1-\overline a z)(1-\overline b z)}
=\frac{z^2-sz+p}{1-\overline s z+\overline p z^2},\quad s=a+b,\quad p=ab.
\]
By the standard Hardy-space zero-multiplicity description of finite model spaces, \(V_{a,b}=H^2\ominus BH^2\). This includes the repeated-node case with the derivative kernel. Multiplication by inner \(B\) is an isometry; the orthogonal projection onto \(BH^2\) is \(B P_+(\overline B\,\cdot)\). Write \(B(z)=\sum_{j\ge0}c_jz^j\). Since \(f=z^2\), Parseval yields
\[
\|f-P_{V_{a,b}}f\|^2=\|P_+(\overline B z^2)\|^2=|c_0|^2+|c_1|^2+|c_2|^2.\tag{1}
\]
The exact first coefficients are
\[
c_0=p,\qquad c_1=t=-s+p\overline s,\qquad
c_2=1-|p|^2+\overline s\,t.\tag{2}
\]

**2. Universal inequality.** Put \(x=|p|<1\), \(A=1-x^2\), and \(y=|t|\). As \(B\) is a disk self-map, Schwarz--Pick at the origin gives \(y=|B'(0)|\le A\). Equation (2) implies
\[
s=-\frac{t+p\overline t}{A},\qquad
c_2=A-\frac{|t|^2+\overline p\,t^2}{A}.
\]
Because \(0\le y\le A\), the real number \(A-y^2/A\) is nonnegative. Reverse triangle inequality therefore gives
\[
|c_2|\ge\left|A-\frac{(1+x)y^2}{A}\right|
=\left|A-\frac{y^2}{1-x}\right|.
\]
Set \(u=y^2/(1-x)\ge0\). Combining with (1),
\[
\begin{aligned}
\|f-P_Vf\|^2
&\ge x^2+(1-x)u+(A-u)^2\\
&=\frac9{16}+\frac{(2x-1)^2(4x+3)}{16}
+\left[u-(1-x)(x+\tfrac12)\right]^2\\
&\ge\frac9{16}.\tag{3}
\end{aligned}
\]
Every term in the last line is nonnegative for \(0\le x<1\). This is a global bound across all node pairs, including coalescent configurations.

**3. Sharpness and complete equality classification.** Take \(a=(1+i)/2\) and \(b=(1-i)/2\). Then \(p=1/2\), \(s=1\), \(t=-1/2\), and \(c_2=1/4\). Equation (1) gives exactly \(1/4+1/4+1/16=9/16\), so the bound is attained and captured energy is \(1-9/16=7/16\).

Conversely, equality in (3) forces \(x=1/2\), \(u=1/2\), and \(y=1/2\). Equality in the reverse triangle inequality then forces the complex numbers \(\overline p\,t^2\) and \(A-y^2/A\) to have the same nonnegative real direction; equivalently \(\overline p\,t^2=|p|y^2\). Rotate both nodes so that \(p=1/2\) is positive real. Then \(t=\pm1/2\) is real, and \(s=-(t+p\overline t)/A=\mp1\). The zeros of \(z^2-sz+1/2\) are therefore \((1\pm i)/2\) or their negatives. Reversing the common rotation gives precisely the stated family. In all cases the nodes are distinct. This completes the proof.

## Verification
The accompanying `check_exact.py` replays the exact polynomial identity underlying (3), the exact values of all first three Blaschke coefficients at the optimizer, and the two-kernel Gram-matrix projection. It also performs a reproducible finite randomized numerical stress test. The symbolic identities and analytic inequalities above, not the finite tests, establish the quantified result. Execute `python3 check_exact.py` from the directory containing the packaged files; only Python's standard library is needed.

## Relationship to prior work
Mashreghi--Verreault (2023, arXiv:2310.01269, Sections 2 and 5) develops nonlinear reproducing-kernel expansions and model-space decompositions, but does not solve the specific global two-node optimization for \(z^2\). Qian (2022, arXiv:2201.07228, Section 4.1) establishes existence of best kernel approximations in \(H^2\), rather than the present exact optimal constant and node geometry. Qian--Wang (2020, arXiv:2012.06184) proves an existence result by pseudo-hyperbolic methods. Baratchart--Chevillard--Qian (2015, arXiv:1501.01161) studies broad Hardy rational approximation lower bounds and numerical methods. Baratchart et al. (2026, arXiv:2603.16295, Section 5, Theorem 2) obtains a lower bound for \(\mathcal R_{n,n}\) approximation of \(z^N\) when \(n<N\); that estimate neither states nor directly entails the exact two-kernel, type-\((1,2)\) optimizer here. The well-known model-space projection identity in (1) is background, not a novelty claim.

## Limitations
This theorem is confined to a two-dimensional kernel/derivative-kernel subspace for \(z^2\). It is not a claim about all rational functions of unconstrained numerator and denominator degrees, or about the best approximation for general \(z^N\). The comparison above establishes no absolute historical priority: alternative presentations in older nonlinear approximation literature might contain an equivalent special case. No independent validation has been performed.

## References
1. J. Mashreghi and W. Verreault, *Nonlinear expansions in reproducing kernel Hilbert spaces* (2023), arXiv:2310.01269, https://arxiv.org/abs/2310.01269.
2. T. Qian, *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces* (2022), arXiv:2201.07228, https://arxiv.org/abs/2201.07228.
3. T. Qian and Y.-B. Wang, *Pseudo-hyperbolic distance and n-best rational approximation in H2 space* (2020), arXiv:2012.06184, https://arxiv.org/abs/2012.06184.
4. L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower bounds in H2-rational approximation* (2015), arXiv:1501.01161, https://arxiv.org/abs/1501.01161.
5. L. Baratchart et al., *Lower bounds in H2-rational approximation to Blaschke products* (2026), arXiv:2603.16295, https://arxiv.org/abs/2603.16295.
