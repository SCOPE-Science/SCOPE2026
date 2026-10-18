# Poisson extreme gaps in two-dimensional Zeckendorf simple jump paths

## Finding
Choose uniformly a two-dimensional *simple jump path* from \((n,n)\) to \((0,0)\), where each step decreases both integer coordinates strictly. Write its \(K_n\) successive step vectors as \((A_i,B_i)\), for \(1\le i\le K_n\), and their gap sums as \(S_i=A_i+B_i\). For each integer threshold \(u\), define
\[
X_n(u)=\#\{i\le K_n:S_i\ge u\},\qquad L_n=\max_{i\le K_n}S_i.
\]
**Theorem.** For any integer sequence \(u_n\) such that
\[
\lambda_n=n u_n 2^{-u_n}\longrightarrow\lambda\in(0,\infty),
\]
one has \(X_n(u_n)\Rightarrow\operatorname{Poisson}(\lambda)\). In particular,
\[
\Pr(L_n<u_n)\longrightarrow e^{-\lambda},\qquad
\Pr\bigl(S^{\downarrow}_{n,j}<u_n\bigr)\longrightarrow
 e^{-\lambda}\sum_{\ell=0}^{j-1}\frac{\lambda^\ell}{\ell!}
\]
for every fixed \(j\ge1\), with \(S^{\downarrow}_{n,j}\) the \(j\)-th largest gap sum (set to zero if the path has fewer than \(j\) steps). Consequently
\[
L_n=\log_2 n+\log_2\log_2 n+O_{\mathbb P}(1).
\]
The fluctuations are lattice-valued and do **not** generally have one phase-independent centered limiting law. For example, along \(n_t=2^{2^t}\), for every fixed integer \(h\),
\[
\Pr(L_{n_t}<2^t+t+h)\longrightarrow\exp(-2^{-h}).
\]

## Assumptions and scope
The path starts at \((n,n)\), includes its terminal step to the origin, and every coordinate of every step is a strictly positive integer. The path is selected uniformly from *all* lengths, not conditioned on its number of steps. Gap *sum* is the \(\ell^1\)-size \(A_i+B_i\), **not** the Euclidean gap length or the largest single coordinate. Integers \(n\) tend to infinity. The Poisson theorem concerns fixed factorial-moment order and thresholds with the specified positive finite limit. The extreme-value statements concern any fixed successive rank. All logarithms with subscript 2 are base two.

## Proof
**1. Exact composition model and concentration of length.** A strict path of length \(k\) is equivalently a pair of ordered positive \(k\)-compositions \((A_1,\ldots,A_k)\) and \((B_1,\ldots,B_k)\), each summing to \(n\). There are exactly \(\binom{n-1}{k-1}^2\) such paths, hence by Vandermonde there are \(\binom{2n-2}{n-1}\) paths in total. Conditionally on \(K_n=k\), the two compositions are independent and separately uniform. The variable \(K_n-1\) has a hypergeometric law with population size \(2n-2\), \(n-1\) marked items, and sample size \(n-1\). Thus \(\mathbb E K_n=(n+1)/2\), and the hypergeometric Hoeffding bound implies
\[
\Pr\bigl(|K_n-n/2|>n^{2/3}\bigr)\le 2e^{-c n^{1/3}}
\]
for some absolute \(c>0\) and all sufficiently large \(n\). We call the complementary range of \(k\) central.

**2. Uniform local law for selected steps.** For any fixed \(r\), positive integers \(a_1,\ldots,a_r\) with \(T=\sum a_i\), and central \(k\), an exact stars-and-bars count gives
\[
\Pr(A_1=a_1,\ldots,A_r=a_r\mid K_n=k)
=\frac{\binom{n-T-1}{k-r-1}}{\binom{n-1}{k-1}}
=\frac{(k-1)_{\underline r}(n-k)_{\underline{T-r}}}{(n-1)_{\underline T}},
\]
whenever the displayed compositions are feasible. Here \((z)_{\underline j}=z(z-1)\cdots(z-j+1)\) is a falling factorial. If \(T=O_r(\log n)\), then taking logarithms of the finite products, uniformly over central \(k\), yields
\[
\Pr(A_1=a_1,\ldots,A_r=a_r\mid K_n=k)
=2^{-T}(1+O_r(n^{-1/3}\log n+(\log n)^2/n))
=2^{-T}(1+o(1)).
\]
The same formula applies independently to \(B_1,\ldots,B_r\), yielding joint probability \(2^{-\sum_i(a_i+b_i)}(1+o(1))\) for selected gap vectors of total size \(O_r(\log n)\).

The restriction to small sizes causes no loss in the rare-event range. In fact, for any \(v\ge0\) and central \(k\), one coordinate of one step satisfies
\[
\Pr(A_i>v\mid K_n=k)=
\frac{\binom{n-v-1}{k-1}}{\binom{n-1}{k-1}}
\le\left(\frac{n-k}{n-1}\right)^v\le 0.51^v
\]
for all sufficiently large \(n\), with zero understood beyond the feasible range. Consequently \(\Pr(S_i>T\mid k)\le2(0.51)^{T/2}\). For each fixed \(r\), choose \(T=C_r\log_2 n\) with \(C_r\) large enough that the probability any one of \(r\) selected gaps exceeds \(T\) is \(o(n^{-r})\). In the independent geometric comparison, the same truncation is also \(o(n^{-r})\).

**3. Joint rare-gap probabilities.** For independent positive-geometric variables \(G_1,G_2\), with \(\Pr(G_i=a)=2^{-a}\) for \(a\ge1\), their sum has
\[
\Pr(G_1+G_2=s)=(s-1)2^{-s}\quad(s\ge2),\qquad
q(u):=\Pr(G_1+G_2\ge u)=u2^{1-u}.
\]
The last equality follows by summing the geometric-derivative series and holds for every integer \(u\ge2\). From \(n u_n2^{-u_n}\to\lambda>0\) one gets \(u_n=\log_2n+O(\log\log n)\), so in particular \(u_n=O(\log n)\), \(q(u_n)\asymp1/n\). By the relative local-law estimate and the tail truncation, for every fixed \(r\) and every central \(k\),
\[
\Pr(S_1\ge u_n,\ldots,S_r\ge u_n\mid K_n=k)
=q(u_n)^r(1+o(1)),
\]
where the error is uniform over central \(k\). Notice that the selected gaps are **not** asserted to be independent at finite \(n\).

**4. Factorial moments and Poisson convergence.** Conditional exchangeability implies
\[
\mathbb E[(X_n(u_n))_{\underline r}\mid K_n=k]
=(k)_{\underline r}\,q(u_n)^r(1+o(1))
\]
for central \(k\). Uniformly there, \(k/n\to1/2\), and therefore this conditional factorial moment tends to
\[
\left(\frac n2\,u_n2^{1-u_n}\right)^r\longrightarrow\lambda^r.
\]
On the noncentral event, \((X_n)_{\underline r}\le n^r\), so its unconditional contribution is \(O(n^r e^{-c n^{1/3}})=o(1)\). Thus all fixed factorial moments tend to \(\lambda^r\), the factorial moments of a Poisson variable. The ordinary moments are polynomial combinations of factorial moments; the Poisson distribution is moment-determinate. It follows that \(X_n(u_n)\Rightarrow\operatorname{Poisson}(\lambda)\). The zero-count identity \(\{L_n<u_n\}=\{X_n(u_n)=0\}\) and the analogous successive-order-statistic identity give the stated limiting probabilities.

**5. Sharp centering and lattice phases.** Set \(b_n=\log_2 n+\log_2\log_2 n\). For a fixed real offset \(h\), integer thresholds \(u_n=\lceil b_n+h\rceil\) have bounded positive \(n u_n2^{-u_n}\), with bounds of order \(2^{-h}\); every subsequence has a further phase-convergent subsequence. The Poisson theorem and a subsequence contradiction prove upper and lower tight tails, yielding \(L_n-b_n=O_{\mathbb P}(1)\). Finally, for \(n_t=2^{2^t}\) and \(u_t=2^t+t+h\),
\[
n_tu_t2^{-u_t}=(1+(t+h)2^{-t})2^{-h}\longrightarrow2^{-h},
\]
which gives the displayed explicit lattice-phase law. \(\square\)

## Verification
The executable `verify.py` independently enumerates all pairs of same-length positive compositions for \(2\le n\le8\), checks the total \(\binom{2n-2}{n-1}\), and compares the complete maximum-gap threshold counts with a separate dynamic program based on the polynomial \(\sum_{a,b\ge1,\ a+b<u}x^a y^b\). It checks 70 threshold identities. These finite calculations are reproducibility tests; the Poisson limit, sharp location, and lattice-phase formula rely on the preceding proof, not numerical extrapolation.

## Relationship to prior work
Borade, Cai, Chang, Fang, Liang, Miller, and Xu (first public preprint 4 September 2019), *Gaps of Summands of the Zeckendorf Lattice*, introduce exactly these simple jump paths, their gap vectors and gap sums (Definitions 1.1–1.2). Their Theorems 1.3–1.4 give the limiting distribution of a randomly selected **individual** gap vector and gap sum, in particular \((s-1)/2^s\), but not the joint exceedance behavior at levels growing with \(n\). Their final section explicitly identifies distribution of the longest gap as requiring further work for simple paths. Fixed-size convergence by itself does not imply an extreme-value law or the additional \(\log_2\log_2 n\) shift. The present result supplies a uniform moderate-gap estimate, asymptotic Poisson joint exceedances, and the entire finite-rank extreme-value law for the natural \(\ell^1\) gap sum. The one-dimensional longest-gap theorem of Bower, Insoft, Li, Miller, and Tosteson has a different one-geometric tail and does not imply this two-coordinate, common-composition-length result. The known maximum-part results for uniform *single* compositions do not identify the present two-composition sum law.

## Limitations
Only two-dimensional **simple**, strictly decreasing paths with equal starting coordinates are treated. The result concerns \(\ell^1\) gap sums, not Euclidean gap distances, coordinate maxima, compound paths, or dimensions above two. No asymptotic for \(\mathbb E L_n\) or rate of convergence in total variation is proved. Independent priority against every possible alternate extreme-value formulation is not guaranteed. The proof uses the standard hypergeometric concentration inequality and elementary method of factorial moments; neither is claimed novel.

## References
1. N. Borade, D. Cai, D. Z. Chang, B. Fang, A. Liang, S. J. Miller and W. Xu, *Gaps of Summands of the Zeckendorf Lattice*, arXiv:1909.01935v1 (first public 4 September 2019), https://arxiv.org/abs/1909.01935 ; Fibonacci Quarterly 58 (2020), 143–156, DOI:10.1080/00150517.2020.12427596.
2. A. Bower, R. Insoft, S. Li, S. J. Miller and P. Tosteson, *The Distribution of Gaps between Summands in Generalized Zeckendorf Decompositions*, arXiv:1402.3912 (2014), https://arxiv.org/abs/1402.3912.
3. *Rigorous decorrelation of part count and maximum in uniform compositions*, mathematical-record publication (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31 ; concerns single-composition maxima, not paired-coordinate gap sums.
