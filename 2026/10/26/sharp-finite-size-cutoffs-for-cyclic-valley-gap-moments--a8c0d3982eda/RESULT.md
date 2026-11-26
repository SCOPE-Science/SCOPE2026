# The positive finite-size variance correction for cyclic valley gaps

## Finding

Place independent uniform priorities at the sites of a cycle of length \(K\ge3\). A valley has lower priority than both neighbors. For integer \(i\ge1\), let \(D_{i,K}\) count clockwise gaps of length \(g=i+1\) between successive distinct valleys, including wrap-around gaps. This is also the root-gap count for homogeneous ballistic deposition on a cyclic strip [1, Lemma 2.1]. Matijasevick [1, Theorem A and Proposition 3.1] proves \(\operatorname{Var}D_{i,K}=Kb_i\) for \(K\ge 2i+7\). At the preceding size, for **every** \(i\ge1\),
\[
\operatorname{Var}D_{i,2i+6}=(2i+6)(b_i+\delta_i),\qquad
\delta_i=\|\mathcal C^{1/2}\mathcal K_i\mathcal C^{1/2}\|_{\mathrm{HS}}^2>0,
\]
where \(\mathcal C,\mathcal K_i\) are integral operators on \(L^2([0,1])\) with kernels \(c(s,t)=\min(s,t)-st\) and \(k_i(s,t)=((s+t)^i-|s-t|^i)/(2i!)\). Thus the eventual linear variance cutoff is sharp for every gap length.

## Proof

Write \(Y_x\) for the indicator of a marked gap from \(x\) to \(x+g\). The \(i\) interior priorities must rise and fall between the two endpoint valleys. Conditional on endpoint survival probabilities \(s,t\) (one minus their priorities), the probability that the interior satisfies these inequalities, including those next to the endpoints, is \(k_i(s,t)\) by [1, Lemma 4.2]. At all cycle sizes used in the variance proof the window \([x-1,x+g+1]\) consists of distinct sites. Its two outward neighbors contribute \(st\), giving
\[
a_i=\mathbb E Y_x=\int_0^1\int_0^1 st\,k_i(s,t)\,ds\,dt
=\frac{i2^{i+1}}{(i+1)(i+2)(i+4)i!}.
\]

On the priority line there is independence for offsets \(|h|>g+2\). For \(1\le |h|<g\), the second start would be strictly inside the first gap (or conversely), and for \(|h|=g+1\) the second start would be adjacent to the first end (or conversely). Both types are impossible. At \(|h|=g\) there is a shared valley; denote the joint probability by \(u_i\). At \(|h|=g+2\) there is one shared outward neighbor between adjacent long gaps; denote the joint probability by \(v_i\). Summing the covariance terms, including the variance at \(h=0\), yields \(b_i=a_i-(2g+5)a_i^2+2u_i+2v_i\), since the non-independent offsets have their line diagrams on cycles of size at least \(2g+5\).

At \(K=2g+4\), the two offsets \(\pm(g+2)\) coincide, and the intervening arc on *each* side between the two long gaps has length two. All offsets represented by \(|h|\le g+1\) have the same diagram as on the line (the union of their windows spans at most \(2g+4\) distinct sites). Let \(w_i\) be the cyclic joint probability at the single antipodal offset. Replacing two line terms \(v_i-a_i^2\) by one cyclic term \(w_i-a_i^2\) gives
\[
\delta_i=w_i-2v_i+a_i^2.
\]

Let \(\mathcal M\) and \(\mathcal R\) have kernels \(\min(s,t)\) and \(st\), respectively. The former comes from one priority that exceeds both endpoint priorities across a length-two arc; the latter comes from two independent outward guards. Conditioning on the four marked endpoints and integrating independent interior priorities gives the cyclic integrals
\[
w_i=\operatorname{Tr}(\mathcal K_i\mathcal M\mathcal K_i\mathcal M),\quad
v_i=\operatorname{Tr}(\mathcal K_i\mathcal M\mathcal K_i\mathcal R),\quad
a_i^2=\operatorname{Tr}(\mathcal K_i\mathcal R\mathcal K_i\mathcal R).
\]
The kernels are bounded, symmetric and Hilbert–Schmidt. The products are trace class, and cyclic permutation makes the two mixed terms equal. Therefore \(\delta_i=\operatorname{Tr}(\mathcal K_i\mathcal C\mathcal K_i\mathcal C)\) for \(\mathcal C=\mathcal M-\mathcal R\). This Brownian-bridge covariance operator has the complete sine basis \(\sqrt2\sin(\pi n s)\) with eigenvalues \((\pi n)^{-2}\): its kernel is the Dirichlet Green function of the negative second derivative. Consequently \(\mathcal C^{1/2}\) is injective with dense range. By cyclicity the trace is the squared Hilbert–Schmidt norm of the self-adjoint sandwich \(\mathcal C^{1/2}\mathcal K_i\mathcal C^{1/2}\). If that sandwich vanished, injectivity and density would force \(\mathcal K_i=0\), contrary to the strict positivity of its continuous kernel in the interior. Thus \(\delta_i>0\) for every \(i\), irrespective of whether \(\mathcal K_i\) is positive as an operator.

## Mean boundary (companion calculation)

The all-index sharp mean cutoff \(K=i+4\) is due to [1, Remark 3.2]. That remark gives the boundary integral \(\mathbb E D_{i,i+3}=(i+3)\iint \min(s,t)k_i(s,t)\,ds\,dt\) because the two outward neighbors coincide. Integrating over the triangle \(s=ut<t\) and using symmetry evaluates this integral:
\[
\mathbb E D_{i,i+3}=\frac{1}{i!}\int_0^1 u\big((1+u)^i-(1-u)^i\big)\,du=(i+4)a_i.
\]
For \(3\le K\le i+2\) such gaps are impossible: two distinct valleys need at least one separating site in each direction. For \(K\ge i+4\) the mean is \(Ka_i\) [1]. The evaluation and zero regime are included for completeness, not as a new proof of the mean cutoff.

## Verification, prior work and scope

The companion `verify.py` implements exact cyclic ranking enumeration for the mean at \(K=i+3\) for \(1\le i\le6\), and for the first excluded variance size at \(i=1,2\), with \(\delta_1=29/28350\) and \(\delta_2=1/2025\). Run `python3 verify.py`. The finite calculations do not establish the variance identity for all indices; the shared-guard factorization and positivity argument above do.

Remark 3.2 of [1] distinguishes its analytic all-index sharpness proof for the **mean** from the exhaustive checks of the **variance** boundary for \(i=1,\ldots,4\). The distinct claim here is the formula for the positive variance correction and hence the all-index variance sharpness. Mansour, Rastegar and Roitershtein [2, Theorems 3.3 and 3.5] give the initial gap-variance cases and selected larger-cycle formulas; in particular their first-index boundary variance already agrees with the correction here. Operator traces for cyclic permutation patterns appear in [3], with a different counting objective. The comparison is limited to the inspected literature. The result does not classify smaller-size variances, mixed gap covariances, nonuniform clocks or other geometries.

[1] M. Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, https://arxiv.org/abs/2610.21094 (v1).

[2] T. Mansour, R. Rastegar and A. Roitershtein, *On ballistic deposition process on a strip*, https://arxiv.org/abs/1903.12548 (v2).

[3] R. Ehrenborg, *Cyclically consecutive permutation avoidance*, https://arxiv.org/abs/1312.2051 (v1).
