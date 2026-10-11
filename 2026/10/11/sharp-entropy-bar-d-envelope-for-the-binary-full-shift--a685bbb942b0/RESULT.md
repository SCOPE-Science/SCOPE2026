# Sharp entropy–\(\bar d\) envelope for the binary full shift

## Finding

Write \(\Sigma=\{0,1\}^{\mathbb Z}\), equip it with the left shift, and let \(u=(\tfrac12\delta_0+\tfrac12\delta_1)^{\mathbb Z}\). For every invariant probability \(\mu\) on \(\Sigma\),
\[
\boxed{\ \bar d(\mu,u)\le \tfrac12-H_{\mathrm b}^{-1}(h(\mu))\ },
\]
where entropy uses natural logarithms, \(H_{\mathrm b}(p)=-p\log p-(1-p)\log(1-p)\), \(H_{\mathrm b}^{-1}:[0,\log2]\to[0,1/2]\) is the increasing inverse, and \(0\log0=0\). The inequality is optimally sharp at **every** entropy value:
\[
\sup\big\{\bar d(\mu,u):\mu\text{ invariant},\ h(\mu)=s\big\}
=\tfrac12-H_{\mathrm b}^{-1}(s),\qquad 0\le s\le\log2.
\]
This is a single exact entropy-versus-distance envelope, encompassing both the inequality and the saturating witnesses.

## Assumptions and scope

Let \(\mathcal J(\mu,u)\) be the set of invariant joinings of two shift processes, and define
\[
\bar d(\mu,u)=\inf_{\lambda\in\mathcal J(\mu,u)}\lambda\{(x,y):x_0\ne y_0\}.
\]
No mixing, Markov, ergodicity or support assumption is imposed on \(\mu\). Let \((X_t)_{t\in\mathbb Z}\) be the canonical stationary process with law \(\mu\); its entropy rate is \(h(\mu)=H(X_0\mid X_{-1},X_{-2},\ldots)\). The formula has the same meaning for invariant measures on the one-sided full shift: pass to the unique stationary natural extension, which preserves entropy and the infimum of disagreement over invariant joinings.

## Proof

**Step 1: a stationary causal maximal joining.** Fix a version of
\[
p_t=\mathbb P(X_t=1\mid X_s:s<t).
\]
Its conditional entropy satisfies
\[
h(\mu)=\mathbb E H_{\mathrm b}(p_0).
\]
Independently of the complete process \(X\), take iid uniforms \((U_t)_{t\in\mathbb Z}\) and define \(Y_t\) as follows. When \(p_t\ge1/2\), put \(Y_t=0\) if \(X_t=0\), and if \(X_t=1\), put \(Y_t=1\) exactly when \(U_t\le(2p_t)^{-1}\). When \(p_t<1/2\), put \(Y_t=1\) if \(X_t=1\), and if \(X_t=0\), put \(Y_t=0\) exactly when \(U_t\le[2(1-p_t)]^{-1}\). Both denominators are nonzero in their stated cases. A shift-covariant conditional-probability version makes the joint process \((X,Y)\) stationary.

For either case, conditioning on the complete strict past of \(X\) and \(U\) gives
\[
\mathbb P(Y_t=1\mid X_s,U_s:s<t)=\tfrac12,
\quad
\mathbb P(X_t\ne Y_t\mid X_s:s<t)=|p_t-\tfrac12|.
\]
The first identity makes \(Y_t\) independent of its entire past, which is a function of the strict past of \((X,U)\). Thus \(Y\) is an iid fair binary process, and this is a stationary joining with
\[
\bar d(\mu,u)\le\mathbb P(X_0\ne Y_0)
=\mathbb E|p_0-\tfrac12|=:a.
\]

**Step 2: exact binary entropy conversion.** Symmetry and concavity of binary entropy yield
\[
h(\mu)=\mathbb E H_{\mathrm b}(\tfrac12+|p_0-\tfrac12|)
\le H_{\mathrm b}(\tfrac12+a)=H_{\mathrm b}(\tfrac12-a).
\]
Because \(H_{\mathrm b}\) is increasing on \([0,1/2]\), we have \(\tfrac12-a\ge H_{\mathrm b}^{-1}(h(\mu))\), so the displayed bound follows. This reasoning includes \(a=0\), \(a=1/2\), \(h=0\), and \(h=\log2\) without limiting assumptions.

**Step 3: attainment and converse.** For any \(s\in[0,\log2]\), put \(p=H_{\mathrm b}^{-1}(s)\) and \(\mu_p=(p\delta_1+(1-p)\delta_0)^{\mathbb Z}\). Then \(h(\mu_p)=s\). Any joining of \(\mu_p\) with \(u\) has disagreement at least the total-variation distance of its one-symbol marginals, namely \(1/2-p\). The coordinatewise iid maximal coupling of \(\operatorname{Bernoulli}(p)\) and \(\operatorname{Bernoulli}(1/2)\) achieves this disagreement and is stationary. Hence \(\bar d(\mu_p,u)=1/2-p\), proving equality for each entropy level.

For one-sided shift measures, projecting a two-sided joining gives a one-sided joining with unchanged single-site mismatch. Conversely, taking the stationary natural extension of a joining on one-sided pairs gives a two-sided joining with the same mismatch and the prescribed natural-extension marginals; the infima agree.

## Verification

The proof is analytic and uses no experimental or numerical certificate. The conditional kernel was checked separately in the cases \(p_t\ge1/2\) and \(p_t<1/2\): the marginal of \(Y_t\) is exactly fair and its mismatch is exactly \(|p_t-1/2|\). The stationary joining and its past independence were checked at the process level, not inferred from one-point marginals. Monotonicity of \(H_{\mathrm b}\) on the inverse branch checks the inequality direction. The iid witnesses verify sharpness, including the endpoint entropy values. In particular the exact profile strengthens the traditional \(\bar d\le\sqrt{(\log2-h(\mu))/2}\) estimate away from maximal entropy.

## Relationship to prior work

Climenhaga and Kumari (2026, Theorem A) prove a square-root effective-uniqueness estimate for every mixing shift of finite type. Marton (1996, Proposition 1 and its independent-reference specialization) proves a Hamming-transport/informational-divergence square-root inequality for product reference measures. The present statement concerns only the binary full shift, but determines the **optimal entire entropy–distance function**, including equality at every entropy level, rather than an unspecified constant times a square root. The 1996 product inequality does not yield this strictly smaller exact profile as an implication of its stated bound. The proof also directly supplies a stationary, coordinatewise maximal causal coupling without invoking a uniform transport constant. The well-known single-symbol Pinsker and binary entropy estimates are ingredients, not equivalent statements about arbitrary stationary joinings.

## Limitations

The exact envelope is specialized to a binary full shift and its uniform Bernoulli maximal-entropy measure; no analogous optimal profile is claimed for constrained mixing shifts, nonuniform reference processes, or larger alphabets. The theorem does not classify every equality-case process. Older literature may contain an equivalent formulation under rate-distortion or process-coupling terminology despite the comparisons reported separately.

## References

1. V. Climenhaga and T. Kumari, *Effective uniqueness of the measure of maximal entropy in Ornstein's \(\bar d\)-metric*, arXiv:2608.21703v1 (first public 22 August 2026), Theorem A, Definition 1.2, and Section 3; https://arxiv.org/pdf/2608.21703.
2. K. Marton, *Bounding \(\bar d\)-Distance by Informational Divergence: A Method to Prove Measure Concentration*, Annals of Probability **24** (1996), 857–866, especially Proposition 1 and its proof on pp. 861–862; https://doi.org/10.1214/aop/1039639365.
3. R. M. Gray, *Entropy and Information Theory*, 2nd ed., Springer (2011), Chapter 6 on distortion and entropy; https://doi.org/10.1007/978-1-4419-7970-4.
