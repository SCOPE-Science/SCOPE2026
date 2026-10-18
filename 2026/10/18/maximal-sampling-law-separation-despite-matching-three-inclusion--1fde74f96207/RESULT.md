# Maximal sampling-law separation despite matching three inclusion orders

## Finding

For every integer \(m\ge 2\), there are a population of \(N=2^{2m}\) bounded observations in \(\{-1,1\}\), a fixed-size sampling design \(\mathcal H_m\) of size \(n=N/2\), and simple random sampling without replacement (SRSWOR) of the same size such that:

1. For each \(t\in\{1,2,3\}\) and every \(t\) distinct population units, the two designs have **exactly equal joint inclusion probability** \(\binom{n}{t}/\binom{N}{t}\).
2. Their sample totals have exactly the same mean \(\sqrt N/2\) and variance \(N/4\). After common centering and standardization, the \(\mathcal H_m\) sample total is **exactly Rademacher**: each of \(-1\) and \(1\) has probability \(1/2\), for every \(m\).
3. The SRSWOR-standardized total converges in distribution to a standard normal random variable. In fact, the total-variation distance between the two standardized laws tends to its maximum value \(1\).

Thus the first three inclusion orders do not determine the asymptotic distribution, even for uniformly bounded population values, an exactly balanced sampling fraction, and identical variance at every finite size.

## Assumptions and scope

All vector-space arithmetic in the construction is over \(\mathbb F_2\). Write \(G_m=\mathbb F_2^{2m}\), \(N=|G_m|=2^{2m}\), and equip each unit \(x=(x_1,\ldots,x_{2m})\in G_m\) with the deterministic outcome
\[
Q_m(x)=\sum_{j=1}^m x_{2j-1}x_{2j}\pmod 2,\qquad y_x=(-1)^{Q_m(x)}.
\]
The sample \(\mathcal H_m\) is drawn by choosing uniformly \(a\in G_m\setminus\{0\}\) and an independent fair bit \(b\in\mathbb F_2\), then taking precisely those \(x\in G_m\) for which \(a\cdot x=b\). There are \(2(N-1)\) distinct equally probable affine hyperplanes, each of size \(N/2\). The comparator is SRSWOR on \(G_m\) of size \(N/2\). The sample total is \(T_m=\sum_{x\in S}y_x\), and in either design we use
\[
W_m=\frac{T_m-\sqrt N/2}{\sqrt N/2}.
\]
The construction concerns first-, second-, and third-order inclusion probabilities, not fourth-order inclusion probabilities or higher. There is no random population: the outcomes are specified explicitly.

## Proof

**Step 1 (exact three-wise inclusion matching).** Fix \(t\in\{1,2,3\}\) distinct units \(x_1,\ldots,x_t\). In characteristic two, the \(t-1\) difference vectors \(x_j-x_1\), \(2\le j\le t\), are linearly independent. This is immediate for two distinct points, and for three distinct points the two nonzero differences cannot be equal. A hyperplane \(\{x:a\cdot x=b\}\) contains all units exactly when \(a\) is orthogonal to these \(t-1\) independent differences and \(b=a\cdot x_1\). There are \(2^{2m-t+1}-1=N/2^{t-1}-1\) permissible nonzero normals and exactly one permissible \(b\) for each. Hence
\[
\Pr_{\mathcal H_m}(x_1,\ldots,x_t\in S)=\frac{N/2^{t-1}-1}{2(N-1)}.
\]
For \(t=1,2,3\), respectively, the right side is \(1/2\), \((N-2)/(4(N-1))\), and \((N-4)/(8(N-1))\). Direct cancellation shows each equals \(\binom{N/2}{t}/\binom Nt\), the SRSWOR inclusion probability. These are exact finite-population identities; they do not arise merely from asymptotic approximations.

**Step 2 (a flat Walsh transform).** The elementary four-term identity
\[
\sum_{u,v\in\mathbb F_2}(-1)^{uv+\alpha u+\beta v}=2(-1)^{\alpha\beta},\qquad \alpha,\beta\in\mathbb F_2,
\]
gives, on multiplying the independent coordinate-pair sums,
\[
\widehat y(a):=\sum_{x\in G_m} y_x(-1)^{a\cdot x}=2^m(-1)^{Q_m(a)}=\sqrt N(-1)^{Q_m(a)}
\]
for every \(a\in G_m\), including \(a=0\). In particular \(\sum_x y_x=\sqrt N\); the finite-population mean is \(\bar y=N^{-1/2}\). Since \(y_x^2=1\), its finite-population variance with divisor \(N-1\) equals
\[
V_N^2=\frac{\sum_x(y_x-\bar y)^2}{N-1}=\frac{N-N\bar y^2}{N-1}=1.
\]

**Step 3 (the exact two-point sample law).** The hyperplane indicator admits the identity
\[
\mathbf 1_{\{a\cdot x=b\}}=\frac{1+(-1)^{a\cdot x+b}}2.
\]
Therefore the corresponding sample total is
\[
T_m(a,b)=\frac{\widehat y(0)+(-1)^b\widehat y(a)}2
=\frac{\sqrt N}{2}\left[1+(-1)^{b+Q_m(a)}\right].
\]
For every fixed nonzero \(a\), the independent uniform bit \(b\) makes \((-1)^{b+Q_m(a)}\) a fair sign, and thus \(W_m\) is exactly Rademacher under \(\mathcal H_m\).

**Step 4 (matching mean and variance).** In either design each unit has inclusion probability \(1/2\), so \(\mathbb E T_m=(N/2)\bar y=\sqrt N/2\). First- and second-order matching implies equal variances. Directly, for SRSWOR the standard finite-population identity gives
\[
\operatorname{Var}(T_m)=n(1-n/N)V_N^2=N/4.
\]
The preceding exact Rademacher identity gives the same variance under \(\mathcal H_m\). Thus the displayed \(W_m\) has mean zero and variance one under both plans.

**Step 5 (Gaussian limit for SRSWOR).** There are exactly
\[
N_+=\frac{N+\sqrt N}{2}\quad\text{positive units and}\quad N_-=\frac{N-\sqrt N}{2}\quad\text{negative units}.
\]
If \(K_m\) counts positive units in an SRSWOR sample, then
\[
K_m\sim\operatorname{Hypergeom}(N,N_+,N/2),\quad
\mathbb EK_m=N/4+\sqrt N/4,\quad\operatorname{Var}(K_m)=N/16.
\]
Moreover \(W_m=4(K_m-\mathbb EK_m)/\sqrt N\). Both the sampling fraction and population positive fraction stay bounded away from zero and one and converge to \(1/2\); in particular all four expected cells of the underlying two-by-two table diverge. The classical hypergeometric central limit theorem (equivalently, the finite-population CLT for uniformly bounded values) therefore gives \(W_m\Rightarrow\mathcal N(0,1)\) under SRSWOR. This step invokes a standard asymptotic theorem, not finite enumeration.

**Step 6 (asymptotically maximal separation).** Let \(P_m\) be the SRSWOR law of \(W_m\) and \(R=(\delta_{-1}+\delta_1)/2\) its exact law under \(\mathcal H_m\). The explicit hypergeometric formula and sample-complement symmetry give
\[
P_m(\{1\})=P_m(\{-1\})=p_m
=\frac{\binom{(N+\sqrt N)/2}{N/4}\binom{(N-\sqrt N)/2}{N/4}}{\binom N{N/2}}.
\]
Total variation on a countable space satisfies
\[
d_{\mathrm{TV}}(P_m,R)=1-2\min\{p_m,1/2\}.
\]
Because \(P_m\Rightarrow\mathcal N(0,1)\) and a Gaussian assigns zero probability to \(\{-1,1\}\), the Portmanteau theorem implies \(P_m(\{-1,1\})=2p_m\to0\). Consequently \(d_{\mathrm{TV}}(P_m,R)\to1\), as claimed. This limit does not require a local central limit theorem.

## Verification

Run `python check.py` using Python's standard library. The code exhaustively constructs all \(2(N-1)\) affine hyperplanes for \(m=2,3,4\), checks their sizes, verifies every Walsh coefficient against the exact algebraic formula, checks exact Rademacher counts and sample variances, and verifies all three inclusion probabilities for **every** subset of up to three units when \(m=2\). It uses integer and rational arithmetic only. These tests were run successfully. The six proof steps establish the infinite family; the finite tests are not presented as an exhaustive infinite verification.

## Relationship to prior work

Chen's 2026 paper proves failure of a transferred SRSWOR CLT under matching first- and second-order inclusion probabilities, using projective-plane block designs, and explicitly conjectures that no fixed finite inclusion order suffices; its demonstrated case is order two. The theorem above establishes the next, order-three case on deterministic uniformly bounded populations and strengthens distributional disagreement to maximal asymptotic total variation. Chen's general observation that strength-three designs reproduce three inclusion orders (Theorem 2.1) is used as context, not claimed as original.

The affine-hyperplane Hadamard three-design and the flat Walsh spectrum of quadratic Boolean bent functions are classical ingredients. Here they are combined to give an explicit survey-sampling counterexample with exact full sample-total law. Work on triplewise-independent summands supplies another distinct type of non-Gaussian example, but does not by itself impose a fixed sample size and SRSWOR-compatible inclusion probabilities.

## Limitations

This result handles exactly order three, not arbitrary fixed order \(r\ge4\); it does not resolve the full all-orders conjecture. The sampling fraction is exactly one half, population sizes follow \(N=2^{2m}\), and the outcome alphabet is \(\{-1,1\}\). Neither a general criterion for design-based CLTs nor a rate for the Gaussian approximation is asserted. The exact separation is between two specified sampling plans, not all designs with these inclusion probabilities. The construction and convergence are analytical; priority over any unlocated equivalent construction has not been independently certified.

## References

1. Jiahua Chen, *Low-Order Inclusion Probabilities Do Not Determine Asymptotic Normality*, arXiv:2610.09168v1 (first public version, October 6, 2026), https://arxiv.org/html/2610.09168v1. Sections 1, 2, 4, and 6.
2. Beaulieu, Lafaye de Micheaux, and Ouimet, *Counterexamples to the classical central limit theorem for triplewise independent random variables having a common arbitrary margin*, arXiv:2104.02292 (2021), https://arxiv.org/abs/2104.02292.
3. *Affine design*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Affine_design (classical Hadamard three-design parameters).
4. *Bent Boolean Functions*, Boolean Function Wiki, https://boolean.wiki.uib.no/Bent_Boolean_Functions (classical Walsh-spectrum property and quadratic example).
5. J. Hájek, *Limiting distributions in simple random sampling from a finite population*, Publications of the Mathematics Institute of the Hungarian Academy of Sciences 5 (1960), 361–374 (finite-population central limit theorem).
