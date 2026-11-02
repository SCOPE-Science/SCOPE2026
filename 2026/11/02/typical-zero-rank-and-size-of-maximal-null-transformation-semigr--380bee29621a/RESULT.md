# Typical zero rank and size of maximal null transformation semigroups

## Finding

Let \(\mathcal T_n\) be the full transformation semigroup on a fixed labeled \(n\)-element set, under composition. A **null subsemigroup** is a nonempty subsemigroup \(S\) for which all products of two elements equal one idempotent \(\zeta\in S\). Write \(\mathcal M_n\) for the collection of inclusion-maximal null subsemigroups of \(\mathcal T_n\), and \(F_n=|\mathcal M_n|\). For \(S\in\mathcal M_n\), let \(R(S)=|\operatorname{im}\zeta|\). All logarithms below are natural.

**Theorem.** For \(n\ge1\), every real \(\theta\), and formal variables \(z,u\), the exact marked enumerator is
\[
\sum_{n\ge0}\frac{z^n}{n!}\sum_{S\in\mathcal M_n}u^{R(S)}|S|^\theta
=\exp\bigl(u C_\theta(z)\bigr),
\]
where \(\mathcal M_0\) consists by convention of one empty structure and
\[
C_\theta(z)=z+z^2+\sum_{k\ge3}\frac{z^k}{(k-1)!}
\sum_{j=2}^{k-1}\binom{k-1}{j-1}j^{\theta(k-j)}.
\]
In particular, at \(\theta=0\),
\[
C_0(z)=B(z)=ze^{2z}-2ze^z+2z+z^2,
\qquad
\sum_{n\ge0}\frac{z^n}{n!}\sum_{S\in\mathcal M_n}u^{R(S)}=e^{uB(z)}.
\]
These exact marked identities are derived from the established maximal-null normal form, and are included to make the asymptotic claim explicit and reproducible; the normal form and the unmarked total-count recurrence are prior work.

Choose \(S_n\) uniformly from \(\mathcal M_n\), set \(R_n=R(S_n)\), and let \(L_n=\log|S_n|\). As \(n\to\infty\),
\[
\boxed{\frac{R_n\log n}{n}\ \xrightarrow{\mathbb P}\ 1,\qquad
\frac{2L_n}{n\log\log n}\ \xrightarrow{\mathbb P}\ 1.}
\]
Moreover, the total number of maximal null subsemigroups satisfies
\[
\boxed{\log F_n=n\log n-n\log\log n+(\log2-1)n+o(n).}
\]
The first law concerns the **rank of the zero transformation**, not the number of generators or the rank of a typical member of the null semigroup. The second concerns the number of transformations in the randomly chosen subsemigroup itself.

## Assumptions and scope

The ground set is labeled; isomorphic embedded subsemigroups are counted separately. Maximal means maximal by inclusion **among null subsemigroups** of the full transformation semigroup, not maximal among all subsemigroups and not necessarily of maximum cardinality. For a fixed \(n\), the uniform measure assigns equal weight to each distinct embedded maximal null subsemigroup. The limits are in probability with respect to this measure. The exact exponential generating functions are formal in \(z\); for real \(\theta\), each coefficient is a finite real number. The limit statements concern integer \(n\to\infty\), with no finite-field or other auxiliary parameter.

## Proof

**1. Structural normal form and the marked count.** We first reconstruct the relevant maximal-null decomposition. Let \(\zeta\) be the zero of a null subsemigroup and write its distinct kernel classes as \(Z_1,\ldots,Z_r\), each containing its fixed image point \(a_i\). Since \(f\zeta=\zeta f=\zeta\) for every \(f\) in that subsemigroup, each \(f\) preserves every \(Z_i\) and fixes \(a_i\). The null condition holds independently on these disjoint classes. If the semigroup is inclusion-maximal, it must contain every coordinatewise combination of admissible components, and each component must itself be maximal null with constant zero \(a_i\).

For a fixed kernel class \(Z\) of size \(k\), with root \(a\), write
\[
N(W,a)=\{f:Z\to Z:\ f(Z)\subseteq W,\ f(W)=\{a\}\},\qquad a\in W\subseteq Z.
\]
Every product of two members of \(N(W,a)\) is the constant map \(a\). Conversely, for any null subsemigroup with constant zero \(a\), its union \(U\) of images is pointwise collapsed to \(a\) by all members; it is therefore contained in \(N(U,a)\). For \(k\ge3\), the distinct maximal possibilities are precisely \(N(W,a)\) with \(\{a\}\subsetneq W\subsetneq Z\): the union of their images and their common collapsed set both equal \(W\), forcing any commuting null extension to remain in \(N(W,a)\). When \(k=1\) or \(2\), each possible root yields a singleton constant-map component. This is the maximal-null normal form also established by Cameron et al. [1, Section 4.2].

For \(k\ge3\), fix \(|W|=j\), so \(2\le j\le k-1\). There are \(k\binom{k-1}{j-1}\) rooted choices of \(W\), and \(N(W,a)\) contains exactly \(j^{k-j}\) transformations: the \(k-j\) points outside \(W\) have independent images in \(W\), while every point of \(W\) maps to \(a\). For \(k=1\) and \(2\) there are respectively one and two rooted component choices, each of semigroup order one. The zero of the direct product has image size equal to the number of kernel blocks, and the subsemigroup order is the product of the component orders. The labeled exponential formula applied to these decorated set partitions proves the \(C_\theta\) identity. At \(\theta=0\), the block counts are
\[
b_1=1,\quad b_2=2,\quad b_k=k(2^{k-1}-2)\quad(k\ge3).
\]
Summing their exponential series gives the stated explicit \(B(z)\).

**2. A precise conditioned-Poisson model.** Let \(t=t_n>0\) be the unique solution to
\[
n=tB'(t).
\]
Existence and uniqueness follow because \(tB'(t)=\sum_{k\ge1}k b_k t^k/k!\) is continuous, strictly increasing from zero to infinity. The dominant term \(t e^{2t}\) in \(B(t)\) gives
\[
n=t(1+2t)e^{2t}(1+o(1)),\quad 2t=\log n-2\log\log n+\log2+o(1),
\quad B(t)\sim\frac{n}{\log n}.
\]

Independently for every \(k\ge1\), take a Poisson variable \(X_k\) of mean \(\lambda_k=b_k t^k/k!\). These variables have a finite sum almost surely because \(\sum_k\lambda_k=B(t)<\infty\). Set \(K=\sum_kX_k\) and \(N=\sum_k kX_k\). Conditional on \(N=n\), the random multiset of block sizes, together with uniformly chosen decorations on each block and labels, has exactly the distribution of a uniform member of \(\mathcal M_n\). This follows by comparing the product Poisson mass \(\prod_k(\lambda_k^{X_k}/X_k!)\) with the labeled-partition factor \(n!\prod_k(b_k/k!)^{X_k}/X_k!\). In particular, \(K\mid(N=n)\) has the law of \(R_n\), while without conditioning \(K\) is Poisson with mean \(B(t)\).

We need a quantitative lower bound for the conditioning probability. Since \(X_1\) is Poisson with mean \(t\), put \(Y=N-X_1\). Then \(Y\) is independent of \(X_1\), its mean is \(n-t\), and
\[
\sigma^2=\operatorname{Var}Y=tB'(t)+t^2B''(t)-t\sim n\log n.
\]
Further, \(\sum_{k\ge2}k^3\lambda_k=O(n(\log n)^2)\). Expanding the characteristic function of the centered compound-Poisson variable \(Y/\sigma\) has a third-order remainder bounded by a constant times
\[
\frac{\sum_{k\ge2}k^3\lambda_k}{\sigma^3}=O\!\left(\sqrt{\frac{\log n}{n}}\right)\longrightarrow0.
\]
It follows directly by the characteristic-function continuity theorem that \((Y-(n-t))/\sigma\) tends to a standard normal law. As \(t/\sigma\to0\), the probability of \(n-\lceil\sigma\rceil\le Y\le n\) tends to \(\Phi(0)-\Phi(-1)>0\). For each integer \(\ell\) between zero and \(\lceil\sigma\rceil\), the Poisson mass satisfies
\[
\Pr(X_1=\ell)=e^{-t}\frac{t^\ell}{\ell!}
\ge\exp\bigl(-t-\lceil\sigma\rceil\log\lceil\sigma\rceil\bigr)
\]
for all sufficiently large \(n\), since \(t\ge1\). Thus
\[
\boxed{\Pr(N=n)\ge \exp\bigl(-O(\sqrt{n\log n}\,\log n)\bigr)
=\exp\bigl(-o(n/(\log n)^3)\bigr).}
\]
The last equality uses that every fixed power of \(\log n\) is negligible compared with \(\sqrt n\).

**3. Typical rank of the zero.** Before conditioning, \(K\) is Poisson with mean \(B(t)\sim n/\log n\). The elementary Chernoff bound gives, for each fixed \(\varepsilon>0\),
\[
\Pr\bigl(|K-B(t)|>\varepsilon B(t)\bigr)
\le 2e^{-c_\varepsilon B(t)}.
\]
Dividing this bound by \(\Pr(N=n)\) from Step 2 still gives a quantity tending to zero. Consequently \(K/B(t)\to1\) in probability conditional on \(N=n\), proving the first asserted limit.

**4. Typical logarithmic order of the subsemigroup.** Refine the Poisson model by giving every block of size \(k\ge3\) an independent uniformly selected rooted decoration \((a,W)\) among its \(b_k\) choices. Let \(j=|W|\). Conditional on the block size \(k\), the variable \(j-1\) has the distribution of a binomial \(\operatorname{Bin}(k-1,1/2)\), conditioned to avoid its two extreme values. A block contributes \((k-j)\log j\) to \(L_n\); blocks of size one or two contribute zero.

Set \(s=2t\sim\log n\) and fix \(0<\delta<1/8\). Call a decorated block *good* when its size \(k\) lies in \([(1-\delta)s,(1+\delta)s]\) and \(j/k\) lies in \([1/2-\delta,1/2+\delta]\). Otherwise call it *bad*. Unconditionally, the block-size intensities for \(k\ge3\) are bounded above by \(t s^{k-1}/(k-1)!\). This is the intensity profile of \(1+\operatorname{Pois}(s)\), up to an overall factor. Under the exponentially tilted intensities \(e^{k/s}\lambda_k\), the same profile has mean \(s e^{1/s}=s+O(1)\). Poisson Chernoff bounds for sizes and binomial Chernoff bounds for decorations therefore give, for some \(c_\delta>0\),
\[
\sum_{\text{bad decorated blocks}}\lambda_{\text{block}}e^{k/s}
=O\bigl(B(t)e^{-c_\delta s}\bigr)
=o\bigl(n/s^A\bigr)\quad\text{for every fixed }A>0.
\]
The finitely many exceptional block sizes \(1,2\) satisfy the same estimate. Let \(Y_{\mathrm{bad}}\) be the total number of ground-set points belonging to bad blocks in the unconditioned model. Its compound-Poisson moment generating function and Markov's inequality yield
\[
\Pr(Y_{\mathrm{bad}}>n/s^2)
\le\exp\left(-n/s^3+o(n/s^3)\right).
\]
After conditioning on \(N=n\), the probability still tends to zero by the lower bound in Step 2. Thus with conditional probability tending to one, at most \(n/s^2\) points belong to bad blocks.

On every good block,
\[
(k-j)\log j
=k\bigl(1/2+O(\delta)\bigr)\bigl(\log s+O_\delta(1)\bigr).
\]
The good blocks contain \(n-o(n)\) points, while the total contribution of bad blocks is nonnegative and at most \(Y_{\mathrm{bad}}\log n=O(n/\log n)=o(n\log\log n)\). Since \(\log s/\log\log n\to1\), the ratio \(L_n/(n\log\log n)\) is within \(O(\delta)+o(1)\) of \(1/2\) with probability tending to one. Letting \(\delta\downarrow0\) proves the second limit.

**5. Total-count growth.** The conditioned-Poisson coefficient identity is exactly
\[
F_n=n!\,t^{-n}e^{B(t)}\Pr(N=n).
\]
Step 2 gives \(\log\Pr(N=n)=o(n)\), while \(B(t)=o(n)\) and \(t\sim\tfrac12\log n\). Stirling's formula now yields
\[
\log F_n=\bigl(n\log n-n+o(n)\bigr)
-n\bigl(\log\log n-\log2+o(1)\bigr)+o(n),
\]
which is the claimed asymptotic.

## Verification

Run `python verify.py` with Python 3 and no external libraries. The verifier independently constructs every full transformation on labeled sets of sizes one through four, identifies idempotent zeros, tests all products under composition, and enumerates maximal compatible families of square-root transformations by maximal-clique search. It compares zero-rank spectra against the component recurrence derived from the exact marked exponential formula. The same independent enumeration checks first and second integer moments of subsemigroup order. The recurrence reproduces the previously published total counts through size ten: \(1,1,3,13,73,451,3211,26097,236433,2335123,24943171\) for sizes zero through ten, with the empty-structure convention at zero. The script exits with `VERIFY_OK` on success.

The direct censuses are finite sanity checks. The asymptotic conclusions are derived from the proof above, not extrapolated from computational evidence. The script's direct enumeration of maximal cliques is independent of the marked-exponential formula it tests.

## Relationship to prior work

Cameron, East, FitzGerald, Mitchell, Pebody, and Quinn-Gregson [1] classified and counted inclusion-maximal null subsemigroups, including the block weights \(b_k\), their partition formula, the total-count recurrence, and a table of small totals. This paper is the primary input and **the structural normal form and unmarked exact enumeration are not new**. The exact marked identity here simply makes their component data explicit with an extra order moment and zero-rank variable. The newly assessed conclusions are the typical zero-rank scale, typical logarithmic semigroup-size scale, and their simultaneous contrast with total-count growth. Cain, Malheiro, and Paulista [2] later studied *largest* commutative nilpotent subsemigroups of transformation semigroups; their main theorem concerns maximum size and does not assert these uniform-inclusion-maximal limit laws. General labeled-assembly and Poisson-conditioning methods motivate the proof; possible broader probability results that subsume the specific limit laws remain a publication-priority risk.

## Limitations

The probability measure is uniform on **inclusion-maximal null subsemigroups**, not uniform over all nilpotent or all commutative subsemigroups, and not uniform over individual transformations. The theorems concern full transformations on labeled finite sets. The formula is for the natural logarithm of the subsemigroup's number of elements, not for its algebraic nilpotency index (which is two by definition). The limit laws do not supply finite-size error constants or a central limit theorem. The exact marked identity is a direct extraction from known component enumeration, and the priority of the asymptotic application remains subject to independent literature review.

## References

[1] P. J. Cameron, J. East, D. FitzGerald, J. D. Mitchell, L. Pebody, T. Quinn-Gregson, *Minimum degrees of finite rectangular bands, null semigroups, and variants of full transformation semigroups*, arXiv:2110.09701 (first publicly posted 19 October 2021); Section 4.2, equations (4.9)–(4.14). https://arxiv.org/abs/2110.09701 . Published in *Combinatorial Theory* 3(3) (2023), article 16.

[2] A. J. Cain, A. Malheiro, T. Paulista, *Commutative nilpotent transformation semigroups*, arXiv:2310.08481 (first publicly posted 12 October 2023); Theorems 3.11–3.12. https://arxiv.org/abs/2310.08481 . Published in *Semigroup Forum* 109 (2024), 60–75.
