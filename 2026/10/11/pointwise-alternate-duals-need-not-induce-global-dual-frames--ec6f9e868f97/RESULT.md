# Pointwise alternate duals need not induce global dual frames

## Finding
Corollary 6.2 of Xiao--Zhao--Zhou, *Redundancy, weaving and \(Q\)-dual of \(K\)-\(g\)-frames in Hilbert spaces*, claims an equivalence between alternate duality of two \(g\)-Bessel families and alternate duality of their induced ordinary frame families whenever each local pair is an alternate dual frame pair. Unlike the preceding Theorem 6.1, Corollary 6.2 does not require uniform frame bounds across the local pairs.

The printed statement is false. Let
\[
\mathcal H=\ell^2(\mathbb N;\mathbb C),\quad V_j=\mathbb C,
\quad\Lambda_jf=\Gamma_jf=f_j.
\]
The two \(g\)-frame families coincide and are Parseval. For every \(j\ge1\), choose local singleton frame pairs
\[
\varphi_{j,1}=\frac1j,\qquad\phi_{j,1}=j.
\]
These are alternate dual frames on each \(V_j\), since \(\langle z,j\rangle(1/j)=z\) for every \(z\in\mathbb C\). Thus the corollary's local hypothesis holds, as does its condition (i): \(\Gamma\) is an alternate dual of \(\Lambda\).

Nevertheless, the two induced ordinary vector families are
\[
\{\Lambda_j^*\varphi_{j,1}\}_{j\ge1}=\{e_j/j\}_{j\ge1},
\qquad
\{\Gamma_j^*\phi_{j,1}\}_{j\ge1}=\{j e_j\}_{j\ge1}.
\]
The first has no positive lower frame bound. The second is not Bessel. Consequently they cannot be alternate dual *frames*, so condition (ii) fails.

The natural repair is to restore uniform local upper frame bounds for **both** local frame families. The immediately preceding Theorem 6.1 already assumes uniform local bounds in its more general \(Q\)-dual setting. In the scalar-diagonal model, the precise dividing line is uniform seminormalization of the local scaling sequence.

## Assumptions and scope
The ambient Hilbert space is the standard separable complex Hilbert space \(\ell^2(\mathbb N)\). Every coefficient space is \(\mathbb C\), and each local index set consists of one element. The source defines an alternate dual of a \(g\)-frame through a bounded, Bessel analysis/synthesis reconstruction; hence a formal coordinatewise identity alone does not establish dual-frame status.

Each local family here is genuinely a frame of \(\mathbb C\) with its own positive lower and finite upper bound. Those bounds vary with \(j\). The original global \(g\)-frames have exact bounds \(A=B=1\), so the failure is entirely at the local-to-global transfer step.

## Proof
Let \((e_j)_{j\ge1}\) be the standard basis of \(\mathcal H\). For every \(f=(f_j)_j\in\mathcal H\),
\[
\sum_{j=1}^{\infty}|\Lambda_j f|^2
=\sum_{j=1}^{\infty}|f_j|^2=\|f\|^2
=\sum_{j=1}^{\infty}|\Gamma_j f|^2.
\]
Also, \(\Lambda_j^*z=\Gamma_j^*z=ze_j\), and
\[
\sum_{j\ge1}\Lambda_j^*\Gamma_j f
=\sum_{j\ge1}f_je_j=f,
\]
where the series converges in norm. Therefore \(\Lambda\) and \(\Gamma\) are alternate dual \(g\)-frames.

For each fixed \(j\), the singleton vectors \(1/j\) and \(j\) are frames on \(\mathbb C\) with optimal respective bounds \(j^{-2}\) and \(j^2\). They satisfy
\[
\big\langle z,\phi_{j,1}\big\rangle\varphi_{j,1}=z,
\qquad
\big\langle z,\varphi_{j,1}\big\rangle\phi_{j,1}=z.
\]
The induced vectors are \(e_j/j\) and \(j e_j\). On \(f=e_N\), their squared analysis energies are respectively \(N^{-2}\) and \(N^2\). Since \(N\) is arbitrary, no positive common lower bound exists for the former, and no finite Bessel upper bound exists for the latter.

Indeed \(f=(1/j)_{j\ge1}\) lies in \(\ell^2\), but
\[
\sum_{j=1}^{\infty}|\langle f,j e_j\rangle|^2
=\sum_{j=1}^{\infty}1=\infty.
\]
The claimed global dual analysis operator for \(\{j e_j\}\) is not \(\ell^2\)-valued on this legitimate input. The formal expansion
\[
\sum_{j=1}^{\infty}\langle f,j e_j\rangle\frac{e_j}{j}
=\sum_{j=1}^{\infty}f_je_j=f
\]
converges in norm, but is not a representation by two Bessel sequences and hence is not a dual-frame identity.

For the general repair, let \(\Lambda=(\Lambda_j)_j\) and \(\Gamma=(\Gamma_j)_j\) be \(g\)-Bessel families with bounds \(B_\Lambda,B_\Gamma\), and suppose \((\varphi_{jk})_k\) and \((\phi_{jk})_k\) are alternate dual local frames on \(V_j\). If
\[
D_\varphi:=\sup_j B_{\varphi,j}<\infty,
\qquad D_\phi:=\sup_jB_{\phi,j}<\infty,
\]
then for every \(f\in\mathcal H\),
\[
\sum_{j,k}|\langle f,\Lambda_j^*\varphi_{jk}\rangle|^2
=\sum_j\sum_k|\langle\Lambda_jf,\varphi_{jk}\rangle|^2
\le D_\varphi\sum_j\|\Lambda_jf\|^2
\le D_\varphi B_\Lambda\|f\|^2.
\]
The analogous estimate for \(\Gamma_j^*\phi_{jk}\) gives bound \(D_\phi B_\Gamma\). Both induced sequences are therefore Bessel, so their analysis and synthesis maps are bounded. Applying the local reconstruction identities, their bounded mixed synthesis/analysis operator is exactly
\[
\sum_{j,k}\langle f,\Gamma_j^*\phi_{jk}\rangle\Lambda_j^*\varphi_{jk}
=\sum_j\Lambda_j^*\Gamma_j f.
\]
The sums have the usual unconditional Hilbert-space meaning because both induced families are Bessel. Hence the original \(g\)-frame alternate-duality equation is equivalent to the induced ordinary-frame equation. This validates the repaired corollary.

Finally, for positive scalars \((a_j)_j\), the induced local-dual pair is \((a_je_j)_j\), \((a_j^{-1}e_j)_j\). Each family is a frame precisely when its diagonal coefficients are bounded both above and away from zero. Testing \(e_j\) proves necessity, and summing weighted coordinate squares proves sufficiency. For both induced families simultaneously this is exactly
\[
0<\inf_j a_j\le\sup_j a_j<\infty.
\]

## Verification
The original 2024 article was inspected in full at Definition 2.4, Theorem 6.1, its proof, and Corollary 6.2, including their printed PDF pages. Theorem 6.1 assumes a finite uniform local upper frame bound and proves Besselness of the induced families. Corollary 6.2 restates only pointwise local alternate duality and omits that uniform assumption.

For truncated systems with \(N\) coordinates, the induced families have exact lower and upper frame bounds that include \(N^{-2}\) and \(N^2\), respectively. Their degeneration as \(N\to\infty\) is proved by the direct basis-vector argument above, not inferred from finite computational experiments.

The direct-sum local reconstruction operator \(Q\) is the identity in the example, so even a bounded \(Q\) does not supply missing Bessel control of the two induced analysis maps.

## Relationship to prior work
Theorem 6.1 in the target article explicitly requires uniform upper and lower local bounds before transferring \(Q\)-duality to induced frames. It supplies a sufficient uniformity condition but does not establish the unconditional assertion of Corollary 6.2 or the counterexample above.

Casazza--Kutyniok--Li's fusion-frame-system theorem likewise assumes local frame bounds uniform across all subspaces before identifying the global induced family as a frame. Later operator-theoretic work on fusion-frame systems retains common local bounds when composing local analysis operators into a bounded block-diagonal operator. These results support the functional-analytic boundary but do not identify the invalid unconditional corollary.

The counterexample distinguishes a bounded assembled reconstruction \(Q=I\) from bounded *individual* induced analysis maps. Exact-title, theorem-number, alternate-dual-induced-frame, uniform-local-bound, and correction searches did not locate a checked theorem-specific correction. This absence alone is not a proof of novelty.

## Limitations
The result concerns the literal hypotheses of Corollary 6.2 and its local-to-global conclusion. If the intended statement tacitly carries the uniform conditions of Theorem 6.1 into the corollary, the repaired result is valid and the defect is the missing printed hypothesis.

The uniform local upper-bound hypothesis is sufficient in general, not asserted necessary for arbitrary \(g\)-Bessel families. The iff seminormalization criterion is proved only for the natural coordinate-Parseval, scalar-singleton model. No claim is made about unrelated weaving or \(K\)-frame results in the article.

## References
1. X. Xiao, G. Zhao and G. Zhou, *Redundancy, weaving and \(Q\)-dual of \(K\)-\(g\)-frames in Hilbert spaces*, Hacettepe Journal of Mathematics and Statistics 53(3) (2024), 595--607, DOI 10.15672/hujms.1130102.
2. P. G. Casazza, G. Kutyniok and S. Li, *Fusion Frames and Distributed Processing*, Applied and Computational Harmonic Analysis 25 (2008), 114--132, Theorem 2.3.
3. L. Köhldorfer and P. Balazs, *On the relation of the frame-related operators of fusion frame systems*, Sampling Theory, Signal Processing, and Data Analysis 21 (2023), DOI 10.1007/s43670-023-00049-7.
