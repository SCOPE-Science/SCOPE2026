# An Andô modular weak-compactness criterion without spatial uniformity on finite measures

## Finding
For a proper generalized \(N\)-function \(\varphi\) on a finite, separable measure space satisfying uniform \(\Delta_2\), an arbitrary subset \(S\subset L^\varphi\) is relatively weakly compact precisely when
\[
\lim_{\lambda\downarrow0}\sup_{f\in S}\frac{\rho_\varphi(\lambda f)}{\lambda}=0,\qquad
\rho_\varphi(h)=\int_\Omega\varphi(x,|h(x)|)\,d\mu(x).
\]
No spatial-uniformity bound of the form called *constrained* in [1, Definition 3.4] is needed. An explicit non-constrained, non-power example appears below.

## Assumptions and scope
Let \((\Omega,\Sigma,\mu)\) be a complete, separable measure space with \(0<\mu(\Omega)<\infty\). Assume that for each \(x\), the function \(t\mapsto\varphi(x,t)\) is finite, convex, continuous, vanishes at zero, is positive for positive \(t\), satisfies \(\varphi(x,t)/t\to0\) as \(t\downarrow0\), and \(\varphi(x,t)/t\to\infty\) as \(t\to\infty\), and that \(x\mapsto\varphi(x,t)\) is measurable for fixed \(t\). Assume properness (simple measurable functions lie in both the Luxemburg space and its Köthe associate) and that some common \(K\ge2\) gives \(\varphi(x,2t)\le K\varphi(x,t)\) for every \(x,t\). The space is real-valued with Luxemburg norm \(\|h\|_\varphi=\inf\{a>0:\rho_\varphi(h/a)\le1\}\). Both \(S\) and its weak closure are considered in the ordinary Banach-space weak topology. For the empty \(S\), the supremum is interpreted as zero.

The proof uses the published general criterion [1, Theorem 3.2]: under properness and uniform \(\Delta_2\), relative weak compactness is equivalent to boundedness together with uniform small-set integrability of \(\{fg:f\in S\}\) for each fixed \(g\in L^{\varphi^*}\). The condition concerning escape outside finite-measure sets is automatic here.

## Proof
**1. Finite-measure truncation lemma.** If \(\rho_\varphi(u_n)\le1\) and \(b_n\to\infty\), then \(\mu\{|u_n|>b_n\}\to0\). Indeed, for any \(M>0\), monotonicity gives
\[
\mu\{|u_n|>b_n\}\le \mu\{\varphi(x,b_n)<M\}+M^{-1}.
\]
The first term tends to zero: for each \(x\), \(\varphi(x,b_n)\to\infty\), and the ambient measure is finite. Let \(M\to\infty\). This is the exact replacement for the spatially uniform estimate used in [1, Lemma 3.6].

**2. Small constant functions.** Properness and uniform \(\Delta_2\) imply \(\rho_\varphi(\mathbf1_\Omega)<\infty\): a positive scaling of the indicator belongs to the modular class and finitely many doubling steps enlarge its argument to one. For each fixed positive integer \(m\), the \(N\)-function condition and convexity yield
\[
\lim_{\lambda\downarrow0}\frac{\rho_\varphi(m\lambda\mathbf1_\Omega)}{\lambda}=0.
\]
For \(m\lambda\le1\), the ratio \(\varphi(x,m\lambda)/(m\lambda)\) is bounded by the integrable function \(\varphi(x,1)\) and converges pointwise to zero; dominated convergence applies.

**3. Necessity.** Let \(S\) be relatively weakly compact. It is norm bounded. Scaling all its elements by a single positive constant changes the displayed small-modular expression only by a fixed multiplicative factor and a rescaling of \(\lambda\), so assume \(\rho_\varphi(f)\le1\) for every \(f\in S\). Otherwise there exist \(\varepsilon>0\), \(\lambda_j\downarrow0\), and \(f_j\in S\) with \(\rho_\varphi(\lambda_j f_j)>\varepsilon\lambda_j\). By step 2, pass to a subsequence and relabel so that, for every positive integer \(n\),
\[
0<2\lambda_n\le1,\qquad\sum_n\lambda_n\le1,\qquad
\rho_\varphi(n\lambda_n\mathbf1_\Omega)\le\tfrac{\varepsilon}{3}\lambda_n.
\]
Set \(g_n(x)=\partial_t^+\varphi(x,t)|_{t=\lambda_n|f_n(x)|}\). Convexity yields the pointwise Fenchel identity
\[
\varphi^*(x,g_n)=\lambda_n|f_n|g_n-\varphi(x,\lambda_n|f_n|)
\le\varphi(x,2\lambda_n|f_n|).
\]
Here the derivative at zero is zero. These measurable nonnegative functions have a pointwise supremum \(g=\sup_n g_n\). Since \(\varphi^*(x,\cdot)\) is nondecreasing on nonnegative arguments,
\[
\rho_{\varphi^*}(g)\le \sum_n\rho_{\varphi^*}(g_n)
\le\sum_n 2\lambda_n\rho_\varphi(f_n)\le2.
\]
Thus \(g\in L^{\varphi^*}(\Omega)=(L^\varphi)^*\). On the sets \(B_n=\{|f_n|>n\}\), step 1 gives \(\mu(B_n)\to0\); the uniform small-set condition in [1, Theorem 3.2] consequently gives \(\int_{B_n}|f_n|g\,d\mu\to0\). On \(\Omega\setminus B_n\), monotonicity gives \(\varphi(x,\lambda_n|f_n|)\le\varphi(x,n\lambda_n)\). Therefore
\[
\frac{\rho_\varphi(\lambda_n f_n)}{\lambda_n}
\le\int_{B_n}|f_n|g\,d\mu+
\frac{\rho_\varphi(n\lambda_n\mathbf1_\Omega)}{\lambda_n}
\longrightarrow\text{at most }\varepsilon/3,
\]
contradicting the strict lower bound \(\varepsilon\).

**4. Sufficiency.** Suppose the modular limit vanishes. The set \(S\) must be norm bounded: otherwise, for each \(\lambda>0\) there is \(f\in S\) with \(\|\lambda f\|_\varphi>1\), forcing \(\rho_\varphi(\lambda f)>1\), inconsistent with the limit. Now fix \(g\in L^{\varphi^*}\) and select \(r>0\) for which \(\rho_{\varphi^*}(rg)<\infty\). Young's inequality gives, for every measurable \(E\),
\[
\sup_{f\in S}\int_E|fg|\,d\mu
\le\frac1{r\lambda}\sup_{f\in S}\rho_\varphi(\lambda f)
+\frac1{r\lambda}\int_E\varphi^*(x,r|g|)\,d\mu.
\]
First choose \(\lambda\) small to make the first term arbitrarily small, then \(\mu(E)\) small to make the second term small by absolute continuity of the integral. Theorem 3.2 of [1] proves relative weak compactness.

**5. Strict enlargement.** On \(\Omega=(0,1)\) with Lebesgue measure define
\[
\varphi(x,t)=x^{1/4}\bigl(t^{3/2+x}+t^{3+x}\bigr),\quad 0<x<1,\ t\ge0.
\]
Each fiber is an \(N\)-function. The uniform doubling constant \(K=16\) works, while \(\inf_{0<x<1}\varphi(x,t)=0\) for every fixed \(t>0\), so the constrained hypothesis fails decisively. For every fixed \(c>0\), \(\varphi(x,c)\) is integrable. If \(p(x)=3/2+x\), then the conjugate of the lower bound \(x^{1/4}t^{p(x)}\) shows \(\varphi^*(x,c)\le C_c x^{-1/[4(p(x)-1)]}\le C_c x^{-1/2}\). Thus all constant simple functions lie in both the primal and associate spaces; properness holds. The criterion therefore applies even to this spatially degenerate mixture of two variable powers.

## Verification
The decisive bounds are the truncation inequality of step 1, the dominated-convergence estimate of step 2, the conjugate modular sum \(\rho_{\varphi^*}(g)\le2\), and Young's inequality in step 4. The example has uniform exponent ranges \(3/2\le3/2+x\le5/2\) and \(3\le3+x\le4\), so the doubling and conjugate-integrability bounds hold uniformly. All these computations are algebraic or measure-theoretic; no finite numerical experiment is used as an infinite proof.

## Relationship to prior work
[1, Theorem 3.8] establishes the same modular characterization on \(\sigma\)-finite spaces with the extra *constrained* assumption. Its proof identifies a truncation lemma as the only step requiring that hypothesis, and [1, Remark 3.7] gives a failure of that lemma on an infinite-measure space. The finite-measure truncation argument here eliminates that hypothesis without modifying the \(N\)-function or uniform \(\Delta_2\) requirements. The general weak-compactness criterion [1, Theorem 3.2] is used, not reproved. Earlier Orlicz and variable-exponent criteria concern narrower generating functions; Musielak sequence-space work concerns counting measure and does not directly imply this nonatomic example.

## Limitations
The theorem is specific to finite measure; the truncation lemma can fail on infinite measure. It retains properness, the \(N\)-function requirements, and a uniform \(\Delta_2\) inequality. It does not establish novelty against every historically inaccessible full text, and independent validation is not claimed. The explicit example establishes strictness relative to the stated constrained assumption, not maximal generality of the result.

## References
[1] Mauro Sanchiz, *Weak compactness in nice Musielak-Orlicz spaces*, arXiv:2601.19512v1 (first public submission 27 January 2026), especially Theorems 3.2 and 3.8 and Definition 3.4, https://arxiv.org/html/2601.19512v1.

[2] Wan Zhong Gong, Si Yu Shi, Zhong Rui Shi, *Weakly Compact Sets and Riesz Representation Theorem in Musielak Sequence Spaces*, Acta Mathematica Sinica 40 (2024), 467–484, https://doi.org/10.1007/s10114-023-1076-3.

[3] Francisco Hernández, César Ruiz, Mauro Sanchiz, *Remarks on weak compactness criteria in variable exponent Lebesgue spaces*, https://doi.org/10.2989/16073606.2023.2287839.
