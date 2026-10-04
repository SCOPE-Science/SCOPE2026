# The Penalty W-certificate transfer constant is sharp
## Finding
Fix \(\rho>0\) and \(\iota>0\). Consider the convex problem
\[
\min_{x\in\mathbb R} -\frac{\rho}{2}x \quad\text{subject to}\quad x\le 0.
\]
Let \(\bar y=\iota\) and use the single evaluation point set \(\mathcal P=\{\bar y\}\). At the base penalty \(\rho\), this is an \(\left(\iota,\rho/2,\rho\right)\)-Penalty normalized Wolfe certificate, with equality in both the Wolfe-residual inequality and the feasibility inequality. For every \(\widetilde\rho>\rho\), the smallest transferred tolerance for the same point set is
\[
\widetilde\nu=\widetilde\rho-\frac{\rho}{2}=\frac{\rho}{2}\left(2\frac{\widetilde\rho}{\rho}-1\right).
\]
This exactly attains the transfer bound in Proposition 4.3 of Lin--Zhang. Therefore that proposition's uniform transfer coefficient is sharp without additional assumptions.

## Assumptions and scope
The claim concerns the Penalty W-certificate of Definition 3 and the certificate-transfer statement of Proposition 4.3 in arXiv:2609.03251v1. No quadratic-growth assumption is needed for the transfer statement itself. The example uses one affine objective, one affine inequality, the simple set \(X=\mathbb R\), a positive base penalty \(\rho\), a positive certificate radius \(\iota\), and a strictly larger transferred penalty \(\widetilde\rho\).

## Proof
Because \(f\) and \(g\) are affine, their cutting-plane models at \(\bar y\) are exact. Thus the separated penalty model is
\[
\psi^+_{\mathcal P}(x;\rho)=-\frac{\rho}{2}x+\rho[x]_+.
\]
The certificate ball is \(\mathcal B(\bar y,\iota)=[0,2\iota]\). On this interval, \([x]_+=x\), so
\[
\psi^+_{\mathcal P}(x;\rho)=\frac{\rho}{2}x.
\]
Its minimum over the certificate ball is attained at \(x=0\), whereas \(\psi^+_{\mathcal P}(\bar y;\rho)=\rho\iota/2\). Therefore
\[
\mathcal V^+_{\mathcal P,\rho}(\iota;\bar y)=\frac{1}{\iota}\left(\frac{\rho\iota}{2}-0\right)=\frac{\rho}{2}.
\]
The feasibility term also saturates the definition:
\[
[g(\bar y)]_+=\iota=\frac{2\iota(\rho/2)}{\rho}.
\]
Hence \(\nu=\rho/2\) is valid and is minimal at the base penalty.

Now replace the penalty by \(\widetilde\rho>\rho\), keeping the same problem, reference point, radius, and point set. On \([0,2\iota]\),
\[
\psi^+_{\mathcal P}(x;\widetilde\rho)=\left(\widetilde\rho-\frac{\rho}{2}\right)x.
\]
Since the coefficient is positive, the minimum is again at \(x=0\). Consequently
\[
\mathcal V^+_{\mathcal P,\widetilde\rho}(\iota;\bar y)=\widetilde\rho-\frac{\rho}{2}.
\]
Any valid transferred tolerance must dominate this residual. The feasibility inequality only requires \(\widetilde\nu\ge\widetilde\rho/2\), which is strictly weaker because \(\widetilde\rho>\rho\). Thus the minimal tolerance is exactly \(\widetilde\rho-\rho/2\). Substituting the base value \(\nu=\rho/2\) into Proposition 4.3 gives
\[
\nu+\frac{2\nu}{\rho}(\widetilde\rho-\rho)=\frac{\rho}{2}+(\widetilde\rho-\rho)=\widetilde\rho-\frac{\rho}{2},
\]
so the published upper bound is attained with equality.

## Verification
The proof is symbolic and uses only the affine exactness of the cutting-plane models and one-dimensional minimization on \([0,2\iota]\). The bundled `verify.py` evaluates the defining residuals for several exact rational parameter triples and checks the algebraic identity for the transferred tolerance. Its expected terminal output is `VERIFY_OK`.

## Relationship to prior work
Lin and Zhang introduce the Penalty W-certificate and prove that a certificate at penalty \(\rho\) transfers to a larger penalty \(\widetilde\rho\) with tolerance \(\widetilde\nu=\nu+2\nu(\widetilde\rho-\rho)/\rho\). Their paper motivates this transfer as the device that lets the parameter-free algorithm update penalty estimates while retaining a certificate. The inspected text states the transfer bound and its monotonicity argument but does not give a sharpness example or a lower bound showing that the coefficient is necessary. Their earlier unconstrained APEX paper has a normalized Wolfe certificate but no penalty parameter to transfer, so it does not imply the present sharpness statement. Searches of the published published-finding corpus corpus for Penalty W-certificate transfer, sharpness, and the exact source/proposition returned no statement implying this affine equality case.

## Limitations
This is a sharpness result for the certificate-transfer inequality, not a lower bound on optimization complexity and not a claim that every problem exhibits worst-case inflation. Extra structure can yield a smaller transferred tolerance. The originality comparison is limited to the inspected v1 primary source, its predecessor, targeted web searches, the published published-finding corpus corpus, and the current private ledger used only for overlap checking; a later source could independently state the same sharpness example.

## References
1. Zhenwei Lin and Zhe Zhang, *Accelerated Prox-Level Methods for Unknown Piecewise-Smooth Optimization II: Function-constrained Optimization*, arXiv:2609.03251v1, Definition 3 and Proposition 4.3, first public 2026-09-03.
2. Zhenwei Lin and Zhe Zhang, *Optimal Methods for Unknown Piecewise Smooth Problems I: Convex Optimization*, arXiv:2601.14680, normalized Wolfe certificate framework without penalty transfer.
