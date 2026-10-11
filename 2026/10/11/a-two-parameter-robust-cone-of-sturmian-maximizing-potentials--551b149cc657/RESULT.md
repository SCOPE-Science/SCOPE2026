# A two-parameter robust cone of Sturmian-maximizing potentials
## Finding
Let \(\alpha\in(0,1)\setminus\mathbb Q\) and \(\theta\in(0,1)\). On the one-sided Sturmian beta-shift \(Y_\alpha\), write \(X_\alpha\) for the Sturmian subshift and \(\mu_\alpha\) for its unique invariant probability. Use the metric \(d_\theta\), the digit observable \(\Phi(x)=x_0\), and the distance observable \(\Psi(x)=d_\theta(x,X_\alpha)\). Define
\[
A_\theta=(1-\theta)^{-2},\qquad C_\theta=1+2(1-\theta)^{-3}.
\]
For arbitrary \(p,q>0\), set \(G_{p,q}=p\Phi-q\Psi\) and
\[
\delta_\theta(p,q)=\min\left\{\frac{p}{A_\theta},\frac{q}{C_\theta}\right\}
=\min\left\{p(1-\theta)^2,\frac{q}{1+2(1-\theta)^{-3}}\right\}.
\]
Then every invariant probability \(\nu\) on \(Y_\alpha\) satisfies
\[
\int G_{p,q}\,d\mu_\alpha-\int G_{p,q}\,d\nu
\ge \delta_\theta(p,q)W_\theta(\nu,\mu_\alpha).
\]
Hence, for every Lipschitz \(h\) with \(|h|_{\mathrm{Lip},\theta}<\delta_\theta(p,q)\), the measure \(\mu_\alpha\) is the unique maximizing measure of \(G_{p,q}+h\).

Equivalently,
\[
\mathcal K_\theta=
\left\{p\Phi-q\Psi+h:\ p,q>0,\ |h|_{\mathrm{Lip},\theta}<\delta_\theta(p,q)\right\}
\]
is an open convex cone of Lipschitz potentials, and every member of \(\mathcal K_\theta\) has the same nonperiodic maximizing measure \(\mu_\alpha\).

## Assumptions and scope
The notation and one-sided symbolic model are those of Huang, Jenkinson, Xu and Zhang, arXiv:2610.03619v1. The metric is the standard symbolic metric \(d_\theta\). The statement uses their facts that \(\mu_\alpha\) is the unique invariant measure supported on \(X_\alpha\), that
\[
\alpha-\int\Phi\,d\nu\ge0
\]
for every invariant probability \(\nu\), and the quantitative cohomological estimates appearing in their proof of Wasserstein stability.

The theorem is asserted only for \(p,q>0\). It does not claim an analogous neighborhood on either boundary ray \(p=0\) or \(q=0\), nor does it transfer the symbolic conclusion to an interval beta-transformation without an additional coding argument.

## Proof
For an invariant probability \(\nu\), define the two nonnegative defects
\[
D_1(\nu)=\alpha-\int\Phi\,d\nu,
\qquad
D_2(\nu)=\int\Psi\,d\nu.
\]
The proof of Theorem C in arXiv:2610.03619v1 is stronger before its final coefficient simplification than the diagonal statement that is recorded there. For every Lipschitz test function \(f\) with \(|f|_{\mathrm{Lip},\theta}\le1\), its decomposition and remainder estimates give
\[
\left|\int f\,d\nu-\int f\,d\mu_\alpha\right|
\le A_\theta D_1(\nu)+C_\theta D_2(\nu).
\]
Taking the supremum over such \(f\) yields
\[
W_\theta(\nu,\mu_\alpha)
\le A_\theta D_1(\nu)+C_\theta D_2(\nu). 	ag{1}
\]

Because \(\int\Phi\,d\mu_\alpha=\alpha\) and \(\Psi=0\) on \(X_\alpha\),
\[
\int G_{p,q}\,d\mu_\alpha-\int G_{p,q}\,d\nu
=pD_1(\nu)+qD_2(\nu).
\]
By the definition of \(\delta_\theta(p,q)\), one has \(p\ge\delta_\theta(p,q)A_\theta\) and \(q\ge\delta_\theta(p,q)C_\theta\). Thus
\[
pD_1+qD_2
\ge\delta_\theta(p,q)(A_\theta D_1+C_\theta D_2)
\ge\delta_\theta(p,q)W_\theta(\nu,\mu_\alpha),
\]
where the last step is (1). This proves the weighted stability inequality.

Now let \(h\) be Lipschitz. Kantorovich duality gives
\[
\left|\int h\,d\nu-\int h\,d\mu_\alpha\right|
\le |h|_{\mathrm{Lip},\theta}W_\theta(\nu,\mu_\alpha).
\]
Therefore, whenever \(\nu\ne\mu_\alpha\),
\[
\int(G_{p,q}+h)\,d\mu_\alpha-\int(G_{p,q}+h)\,d\nu
\ge
(\delta_\theta(p,q)-|h|_{\mathrm{Lip},\theta})
W_\theta(\nu,\mu_\alpha)>0.
\]
Hence \(\mu_\alpha\) is the unique maximizing measure.

It remains to check the cone assertion. Positive scalar multiplication is immediate. If two representations have parameters \(p_i,q_i,h_i\), then
\[
\delta_\theta(p_1+p_2,q_1+q_2)
\ge \delta_\theta(p_1,q_1)+\delta_\theta(p_2,q_2),
\]
because \(\delta_\theta\) is the minimum of two positive linear forms, and
\[
|h_1+h_2|_{\mathrm{Lip},\theta}
\le |h_1|_{\mathrm{Lip},\theta}+|h_2|_{\mathrm{Lip},\theta}.
\]
Thus the sum remains in \(\mathcal K_\theta\). Strict inequalities in \(p>0\), \(q>0\), and the perturbation radius make this cone open in the finite-dimensional \((p,q)\) directions together with the Lipschitz seminorm topology.

## Verification
The critical estimate was checked directly against the proof of Theorem C in arXiv:2610.03619v1. Before the authors replace both defect coefficients by one common constant, their argument gives the separate coefficients \(A_\theta=(1-\theta)^{-2}\) for the digit-frequency defect and \(C_\theta=1+2(1-\theta)^{-3}\) for the distance defect. Both defects are nonnegative, so no cancellation is used.

As a consistency check, \(p=q=1\) gives \(\delta_\theta(1,1)=C_\theta^{-1}\), because \(C_\theta>A_\theta\) for \(0<\theta<1\). This exactly recovers the published robustness radius around \(\Phi-\Psi\). The new statement therefore specializes correctly to the source theorem while retaining the two coefficients that the source proof later merges.

No finite experiment is used as proof. No optimality of \(\delta_\theta(p,q)\) is claimed.

## Relationship to prior work
Huang, Jenkinson, Xu and Zhang prove that \(F=\Phi-\Psi\) has \(\mu_\alpha\) as unique maximizing measure and give the explicit Lipschitz ball of radius \(C_\theta^{-1}\) around \(F\). Their Wasserstein proof treats the two nonnegative defects separately and only at the last step replaces their coefficients by the common larger constant \(C_\theta\). The present result keeps those coefficients separate and obtains an explicit two-parameter family \(p\Phi-q\Psi\) together with its anisotropic perturbation radius. Thus the published diagonal ball is one slice of the cone above.

Hao, Huang, Jenkinson and Li study typical periodic optimization for beta-transformations in other parameter regimes, while Huang, Jenkinson, Xu and Zhang's symbolic-dynamics work supplies broad periodic-optimization mechanisms. Neither inspected statement gives the weighted two-defect cone above.

## Limitations
The radius \(\delta_\theta(p,q)\) is a certified lower bound for robustness, not asserted to be sharp. The argument requires both coefficients to be strictly positive. It concerns the symbolic Sturmian beta-shift and does not by itself establish a corresponding open cone for interval beta-transformations. The originality comparison is strongest against the focal preprint and targeted ergodic-optimization literature; an abstract convex-duality formulation elsewhere could subsume the cone observation without using the same notation.

## References
1. Wen Huang, Oliver Jenkinson, Leiye Xu, Yiwei Zhang, “Sturmian beta-shifts do not have typical periodic optimization,” arXiv:2610.03619v1, 2 October 2026. In particular Theorems A, C, D and the proof of Theorem C.
2. Zelai Hao, Yinying Huang, Oliver Jenkinson, Zhiqiang Li, “Ergodic optimization for beta-transformations,” arXiv:2502.12269v1, 17 February 2025.
3. Wen Huang, Oliver Jenkinson, Leiye Xu, Yiwei Zhang, “Typical periodic optimization for dynamical systems: symbolic dynamics,” arXiv:2603.07224, 2026.
