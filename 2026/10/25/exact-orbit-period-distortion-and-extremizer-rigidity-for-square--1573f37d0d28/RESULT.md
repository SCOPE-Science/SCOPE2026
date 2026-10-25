# Exact orbit-period distortion and extremizer rigidity for square-function renormings of \(L^1\)

## Finding
Let \((\Omega,\mathcal B,\mu)\) be a standard Borel probability space and let \(T\colon\Omega\to\Omega\) be a Borel bimeasurable, invertible, measure-preserving transformation. Fix strictly positive weights \((a_k)_{k\in\mathbb Z}\) with \(\sum_k a_k=1\) and \(S:=\sum_k\sqrt{a_k}<\infty\). For \(f\in L^1(\mu)\), put
\[
N_T(f)=\int_\Omega\Big(\sum_{k\in\mathbb Z}a_k|f(T^kx)|^2\Big)^{1/2}d\mu(x).
\]
This is the orbit square-function norm introduced in [1]. For \(m\ge1\), let \(P_m\) denote the measurable set of points with least period exactly \(m\), let \(P_\infty\) denote the aperiodic points, and set
\[
b_{m,r}=\sum_{k\equiv r\ (\mathrm{mod}\ m)}a_k,\qquad
S_m=\sum_{r=0}^{m-1}\sqrt{b_{m,r}}.
\]
Then the exact upper equivalence constant is
\[
C_T:=\sup_{f\ne0}\frac{N_T(f)}{\|f\|_1}=
\begin{cases}
S,&\mu(P_\infty)>0\text{ or }\{m: \mu(P_m)>0\}\text{ is unbounded},\\
\max_{\mu(P_m)>0}S_m,&\mu(P_\infty)=0\text{ and the positive-measure periods are bounded}.
\end{cases}
\]
In the second case the maximum is over a nonempty finite set. Moreover, for every finite \(m\), \(S_m<S\); **the upper constant is attained by a nonzero function if and only if the transformation has essentially bounded finite periods**, namely \(\mu(P_\infty)=0\) and the positive-measure periods are bounded. The sharp lower equivalence constant is \(\inf_{f\ne0}N_T(f)/\|f\|_1=1\), attained by constant functions.

There is also a precise characterization of all asymptotic upper extremizers in the regime \(C_T=S\). For normalized \(\|f_j\|_1=1\), the convergence \(N_T(f_j)\to S\) holds **if and only if**, for every pair of distinct integers \(k\ne\ell\),
\[
\int_\Omega\min\{\sqrt{a_k}|f_j(T^kx)|,\sqrt{a_\ell}|f_j(T^\ell x)|\}d\mu(x)\longrightarrow0.
\]
Thus the strict nonattainment and all near extremizers are governed by **pairwise orbit separation**, while the sharp constant itself detects the measurable orbit-period spectrum.

## Assumptions and scope
The transformation is invertible and measure preserving on a standard Borel probability space; the measurable structure permits positive-measure finite orbit markers and finite-period cross-sections. The function field may be real or complex. The weights are strictly positive for every integer and summable in square roots; strict positivity is essential for nonattainment of \(S\) and strict inequality \(S_m<S\). The theorem concerns the identity embedding between the original \(L^1\) norm and the new weighted square-function norm; it does not claim bounds for arbitrary Koopman operators or noninvertible maps.

The formula is a complete classification of \(C_T\) and its attainment for this class of transformations, rather than a claim about periodicity or ergodicity inferred only from a finite experiment. In the aperiodic case, the supremum may be approached on arbitrarily small measurable orbit markers but is never reached.

## Proof
**1. Universal inequalities.** Pointwise Euclidean convexity and the coordinate \(\ell^1\) bound give
\[
\Big(\sum_k a_k|f(T^kx)|^2\Big)^{1/2}
\ge\sum_k a_k|f(T^kx)|,
\qquad
\Big(\sum_k a_k|f(T^kx)|^2\Big)^{1/2}
\le\sum_k\sqrt{a_k}|f(T^kx)|.
\]
For the first inequality, write the left side as the weighted root-mean-square and the right side as the weighted arithmetic mean. Tonelli and invariance of \(\mu\) yield \(\|f\|_1\le N_T(f)\le S\|f\|_1\). Constants achieve the lower inequality.

**2. Exact value on a finite-period component.** On \(P_m\), group the square-function summands by residues modulo \(m\):
\[
N_T(f\mathbf1_{P_m})=
\int_{P_m}\Big(\sum_{r=0}^{m-1}b_{m,r}|f(T^rx)|^2\Big)^{1/2}d\mu(x)
\le S_m\|f\mathbf1_{P_m}\|_1.
\]
A standard Borel finite-class equivalence relation admits a Borel transversal: choose in each length-\(m\) orbit the point smallest under any fixed Borel injection into \([0,1]\). Denote the section by \(E_m\). Its \(m\) translates are disjoint and cover \(P_m\), so \(\mu(E_m)=\mu(P_m)/m>0\) whenever \(\mu(P_m)>0\). For \(f=\mathbf1_{E_m}\), exactly one residue coordinate can be nonzero at each point of \(P_m\), and the integral equals \(S_m\mu(E_m)\). Thus the component constant is exactly \(S_m\), attained by a normalized orbit marker.

**3. Long orbit marker lemma.** Suppose \(\mu(\{x:T^jx\ne x\text{ for }1\le j\le L\})>0\) for an integer \(L\ge1\). The points \(x,Tx,\dots,T^Lx\) are then pairwise distinct. Choose a compatible Polish realization of the standard Borel space with a countable basis. For each such \(x\) there are pairwise disjoint basic open neighborhoods \(U_0,\ldots,U_L\) of those points. The measurable cylinder
\[
E=\bigcap_{j=0}^L T^{-j}U_j
\]
contains \(x\), and its translates \(E,TE,\ldots,T^LE\) are pairwise disjoint because \(T^jE\subset U_j\). Countably many choices of basic neighborhoods cover the positive-measure set, so some such cylinder (intersected with that set if necessary) has positive measure.

Now let \(F\subset\mathbb Z\) be finite, choose \(L\ge\max F-\min F\), and use a long orbit marker \(E\) as above. Then \(T^{-k}E\), \(k\in F\), are pairwise disjoint. At almost every point the \(F\)-indexed vector of \(\sqrt{a_k}\mathbf1_E(T^kx)\) has at most one nonzero entry. Consequently
\[
N_T(\mathbf1_E)\ge\sum_{k\in F}\sqrt{a_k}\mu(E).
\]
If the aperiodic component has positive measure, this construction works for every \(L\). If instead the set of positive-measure finite periods is unbounded, take a positive-measure \(P_m\) with \(m>L\). In either case, letting finite \(F\) exhaust \(\mathbb Z\) establishes \(C_T\ge S\), and step 1 gives equality.

**4. The bounded-period case.** If aperiodic points have measure zero and all positive-measure periods are in a finite nonempty set \(M\), then \(\Omega\) is partitioned modulo null sets into \(P_m\), \(m\in M\). Every \(P_m\) is invariant, so pointwise the integrand splits along this partition. Therefore
\[
N_T(f)=\sum_{m\in M}N_T(f\mathbf1_{P_m})
\le\Big(\max_{m\in M}S_m\Big)\sum_{m\in M}\|f\mathbf1_{P_m}\|_1.
\]
An orbit marker for a maximizing period reaches this bound. To see \(S_m<S\) for every finite \(m\), note that each residue class contains at least two positive \(a_k\), so the strict inequality \(\sqrt{u+v}<\sqrt u+\sqrt v\) makes each nontrivial residue aggregation strictly smaller than its unaggregated square-root sum.

**5. Attainment and quantitative pairwise criterion.** Define nonnegative measurable entries \(c_k(x)=\sqrt{a_k}|f(T^kx)|\), their pointwise deficit \(d(x)=\sum_k c_k(x)-\big(\sum_k c_k(x)^2\big)^{1/2}\), and \(D(f)=\int d=S\|f\|_1-N_T(f)\). For any distinct \(k,\ell\), the two-variable inequality
\[
u+v-\sqrt{u^2+v^2}\ge(2-\sqrt2)\min\{u,v\},\quad u,v\ge0,
\]
combined with monotonicity of the \(\ell^1\)-to-\(\ell^2\) deficit when other nonnegative coordinates are added gives
\[
(2-\sqrt2)\int\min\{c_k,c_\ell\}d\mu\le D(f).
\]
If \(D(f)=0\) for nonzero \(f\), all shifted supports \(T^k\{f\ne0\}\), \(k\in\mathbb Z\), must be pairwise disjoint modulo null sets because every weight is positive. They have equal positive measure, impossible in a probability space. Hence \(D(f)>0\) for every nonzero \(f\), so the universal value \(S\) is never attained. Together with step 4, this proves the claimed attainment dichotomy.

For a finite nonempty \(F\subset\mathbb Z\), the elementary pointwise bound
\[
\sum_{k\in F}c_k-\big(\sum_{k\in F}c_k^2\big)^{1/2}
\le\sum_{\substack{k<\ell\\k,\ell\in F}}\min\{c_k,c_\ell\}
\]
follows by subtracting a maximal entry and bounding every remaining entry by its minimum with that maximal one. The omitted coordinates add at most \(\sum_{k\notin F}c_k\) to the deficit, hence
\[
D(f)\le\sum_{\substack{k<\ell\\k,\ell\in F}}
\int\min\{c_k,c_\ell\}d\mu
+\|f\|_1\sum_{k\notin F}\sqrt{a_k}.
\]
For normalized \(f_j\), the lower bound shows \(D(f_j)\to0\) implies vanishing of every fixed pairwise overlap. Conversely, first choose finite \(F\) making the weight tail arbitrarily small, then use vanishing of its finitely many overlaps in the upper bound. This proves the if-and-only-if criterion.

## Verification
The derivation uses exact measure-preserving identities, a countable positive-measure cylinder argument and elementary \(\ell^1\)/\(\ell^2\) inequalities. The statements concerning infinitely many orbit lengths and every pair of coordinates are proved analytically; finite numerical checks are illustrative, not substitutes for the proof.

As a concrete cyclic test take \(a_k=(3/5)4^{-|k|}\). The exact constants are \(S=3\sqrt{3/5}\), \(S_1=1\), and \(S_2=(\sqrt{17}+\sqrt8)/5\). On a two-cycle, a one-atom indicator realizes the latter constant, which is strictly below \(S\); a system with arbitrarily long positive-measure cycles instead has upper constant \(S\) without a maximizing nonzero function. These are direct substitutions into the theorem.

A stand-alone Python script `verify.py` evaluates the two-cycle constant, the convergence of \(S_m\) on longer cycles, and the elementary pairwise-deficit bounds for sampled nonnegative vectors. These checks test numerical implications only.

## Relationship to prior work
Dantas, Kaasik and Perreau [1], Section 3.1 and equation (3.1), construct exactly the weighted orbit norm \(N_T\), obtaining the bounds \(\|f\|_1\le N_T(f)\le S\|f\|_1\). Their subsequent sections establish rotundity, smoothness and Daugavet phenomena, but do not determine the best upper constant across periodic and aperiodic components, its norm attainment or a pairwise-overlap extremizer criterion. The present theorem sharpens the norm-comparison portion rather than asserting a new Daugavet property.

Doucha [2], especially Sections 3 and 5, treats existence and invariance of strictly convex renormings under group actions on \(L^1\), without the weighted orbit square-function formula or its sharp period-dependent constants. The published finite-window study [3] concerns failure of strict convexity for truncated square functions on irrational rotations; its complete stated theorem and proof concern finite supports, not the full infinite-orbit upper constant, bounded-period phase change or nonattainment classification here. These comparisons are about implications of the statements, not merely title differences.

## Limitations
The complete classification assumes a standard Borel probability space and a genuine Borel invertible action; arbitrary nonstandard measurable spaces or only partially defined/noninvertible transformations are outside the claim. Strictly positive weights and \(\sum_k\sqrt{a_k}<\infty\) are required. The result gives no new criterion for the Daugavet property and no individual rate of convergence for near extremizers. The originality comparison cannot logically rule out an uncatalogued equivalent result in older operator or ergodic literature, and independent audit has not been performed.

## References
1. Sheldon Dantas, Jaan Kristjan Kaasik and Yoël Perreau, *A strictly convex and smooth Banach space with the Daugavet property*, arXiv:2609.12562v1, first publicly submitted 11 September 2026, especially Section 3.1 and equation (3.1). https://arxiv.org/html/2609.12562v1
2. Michal Doucha, *Invariant strictly convex renormings*, arXiv:2508.16182v1, 22 August 2025, especially Sections 3 and 5. https://arxiv.org/html/2508.16182v1
3. *Finite orbit truncations destroy rotundity in an ergodic Daugavet renorming*, publicly available research result, 4 October 2026, especially its statement and proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-orbit-truncations-destroy-rotundity-in-an-ergodic-daugave--1e9c692c67c0
