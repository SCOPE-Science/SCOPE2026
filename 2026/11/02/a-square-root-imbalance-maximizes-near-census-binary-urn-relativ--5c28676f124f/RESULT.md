# A square-root imbalance maximizes near-census binary-urn relative entropy

## Finding

An urn contains \(n\ge 2\) balls, of which \(j\in\{1,\ldots,n-1\}\) have one color and the remaining \(n-j\) have another. Draw \(n-1\) balls. Write \(H_{n,j}\) for the first-color count when sampling without replacement, and \(B_{n,j}\sim\operatorname{Bin}(n-1,j/n)\) for the first-color count under independent sampling with replacement. Define the relative entropy, in nats, by
\[
D_n(j)=D_{\mathrm{KL}}\!\left(\mathcal L(H_{n,j})\,\middle\|\,\mathcal L(B_{n,j})\right).
\]
Set \(p=j/n\), \(q=1-p\), and \(h(p)=-p\log p-q\log q\). Then the exact finite-population identity is
\[
\boxed{D_n(j)=-\log\!\left[\binom nj p^j q^{n-j}\right]-h(p).}
\]
For **every** selection of global maximizers \(j_n\in\operatorname*{arg\,max}_{1\le j<n}D_n(j)\), and with \(a_n=\min\{j_n,n-j_n\}\),
\[
\boxed{\frac{n/2-a_n}{\sqrt n}\longrightarrow\frac12,\qquad
n^2\!\left[\max_{1\le j<n}D_n(j)-D_n(\lfloor n/2\rfloor)\right]\longrightarrow\frac16.}
\]
Thus the most divergent binary urn is asymptotically balanced in proportion but displaced from the balanced composition by \(\frac12\sqrt n+o(\sqrt n)\) balls. The improvement over the most balanced composition is strictly positive for all sufficiently large \(n\), with the precise leading scale \(1/(6n^2)\). Already at \(n=4\), \(D_4(1)-D_4(2)=\frac14\log(256/243)>0\).

## Assumptions and scope

All draws are uniform at the individual-ball level. The urn is binary and has two nonempty color classes. The sample size is **exactly** \(n-1\), i.e. one ball is withheld. The comparator uses \(n-1\) independent draws with success probability \(j/n\). The divergence is directed from the hypergeometric count distribution to the corresponding binomial count distribution, with natural logarithms. The result concerns maximizing this divergence over the integer composition \(1\le j<n\). It makes no assertion of uniqueness of a maximizer at finite \(n\).

## Proof

**1. Exact reduction.** The single ball omitted in sampling without replacement has the first color with probability \(p\), so \(H_{n,j}=j-1\) with probability \(p\), and \(H_{n,j}=j\) with probability \(q\). The binomial probabilities at those two states are exactly equal:
\[
\begin{aligned}
\Pr(B_{n,j}=j-1)&=\binom{n-1}{j-1}p^{j-1}q^{n-j}
=\binom nj p^j q^{n-j},\\
\Pr(B_{n,j}=j)&=\binom{n-1}{j}p^j q^{n-j-1}
=\binom nj p^j q^{n-j}.
\end{aligned}
\]
Writing their common value as \(b_n(j)\) and summing the two relative-entropy terms gives
\(D_n(j)=p\log(p/b_n(j))+q\log(q/b_n(j))=-\log b_n(j)-h(p)\). In particular \(D_n(j)=D_n(n-j)\).

**2. Uniform large-\(n\) expansion in the interior.** Extend the preceding exact expression to real \(0<p<1\) by replacing factorials with gamma functions, and call the resulting function \(F_n(p)\):
\[
F_n(p)=-\log\!\left[\frac{\Gamma(n+1)}{\Gamma(np+1)\Gamma(n(1-p)+1)}p^{np}(1-p)^{n(1-p)}\right]-h(p).
\]
Then \(F_n(j/n)=D_n(j)\). Define
\[
G(p)=\tfrac12\log(p(1-p))-h(p),\qquad
A(p)=\tfrac1{12}\!\left(\frac1p+\frac1{1-p}-1\right).
\]
The factorial Stirling expansion with remainder \(O(t^{-3})\), applied separately at \(t=n,np,n(1-p)\), shows for each fixed \(\eta\in(0,1/2)\) that, uniformly for \(\eta\le p\le1-\eta\),
\[
F_n(p)=\tfrac12\log(2\pi n)+G(p)+\frac{A(p)}n+O_\eta(n^{-3}). \tag{1}
\]
The \(n^{-2}\) term is absent in the logarithmic Stirling series. The error bound is uniform on every such closed interior interval.

**3. Global localization at proportion one-half.** For \(p<1/2\), put \(r=(1-p)/p>1\). Direct differentiation gives
\[
G'(p)=\tfrac12(r-r^{-1})-\log r=\sinh(\log r)-\log r>0.
\]
Symmetry yields \(G'(p)<0\) for \(p>1/2\); hence \(p=1/2\) is its unique global maximizer. To rule out integer compositions near the endpoints without improperly using the interior expansion, use the elementary factorial bounds \(0<\epsilon_m<1/(12m)\) in
\(\log(m!)=(m+\frac12)\log m-m+\frac12\log(2\pi)+\epsilon_m\). The exact identity from Step 1 and \(-h(p)\le0\) give
\[
D_n(j)\le\tfrac12\log(2\pi n)+\tfrac12\log(p(1-p))
+\frac1{12j}+\frac1{12(n-j)}.
\]
Choose a sufficiently small fixed \(\eta>0\). Whenever \(\min(j,n-j)\le\eta n\), this upper bound is strictly smaller than \(D_n(\lfloor n/2\rfloor)=\frac12\log(2\pi n)+G(1/2)+o(1)\), for all sufficiently large \(n\). Consequently every integer maximizer lies inside \([\eta,1-\eta]\) eventually. Uniformity of (1), and the strict maximum of \(G\), then imply \(j_n/n\to1/2\).

**4. The degeneracy produces the square-root scale.** Write \(p=1/2+\delta\). Analytic Taylor expansion gives
\[
G(1/2+\delta)-G(1/2)=-\tfrac83\delta^4+O(\delta^6),
\qquad A(1/2+\delta)-A(1/2)=\tfrac43\delta^2+O(\delta^4). \tag{2}
\]
The quadratic term of \(G\) vanishes, while the finite-population correction \(A/n\) has positive quadratic curvature. Setting \(p_{0,n}=\lfloor n/2\rfloor/n\), (1)-(2) show \(F_n(p_{0,n})-F_n(1/2)=O(n^{-3})\). Since a maximizing \(p_n=j_n/n\) satisfies \(F_n(p_n)\ge F_n(p_{0,n})\), for some constants \(c,C>0\) and all sufficiently large \(n\),
\[
0\le-c\delta_n^4+\frac Cn\delta_n^2+\frac C{n^3},\qquad\delta_n=p_n-\tfrac12.
\]
Solving this quadratic inequality in \(\delta_n^2\) yields \(\delta_n=O(n^{-1/2})\).

**5. Sharp optimization.** For bounded real \(x\), substitute \(p=1/2+x/\sqrt n\) into (1)-(2). Uniformly on every bounded \(x\)-interval,
\[
n^2\left[F_n(1/2+x/\sqrt n)-F_n(1/2)\right]
\longrightarrow f(x):=\tfrac43x^2-\tfrac83x^4. \tag{3}
\]
The function \(f\) has precisely two global maximizers \(x=\pm1/2\), both with value \(1/6\). The integer grid \(j/n\) has mesh \(1/\sqrt n\) in the rescaled coordinate \(x=\sqrt n(j/n-1/2)\), so a grid point can approximate every fixed real \(x\). Localization from Step 4 and uniform convergence in (3) show that every subsequential limit of \(\sqrt n(p_n-1/2)\) is either \(+1/2\) or \(-1/2\), and the maximum of (3) on the grid tends to \(1/6\). Since \(n^2[F_n(p_{0,n})-F_n(1/2)]\to0\), both claimed limits follow. No finite-search assumption enters the proof.

For the finite witness \(n=4\), direct substitution in Step 1 yields \(D_4(1)-D_4(2)=2\log2-\frac54\log3=\frac14\log(256/243)>0\), completing the demonstration.

## Verification

The accompanying standalone `checker.py` uses exact rational probabilities and 75-digit decimal logarithms. It checks both binomial probabilities at the two hypergeometric support points, re-evaluates the KL divergence independently from its definition, and tests color-swap symmetry for all binary compositions of populations of sizes 3 through 16. It also enumerates maximizers for several populations between 50 and 801 to illustrate the predicted \(\sqrt n/2\) offset and \(1/(6n^2)\) gain. There are 357 assertions covering the exact probability/identity comparisons. Finite checks corroborate the elementary reduction but do not certify the infinite asymptotic statement; Steps 2–5 supply that proof.

Reproduce with `python3 checker.py` from the directory containing the embedded files. No nonstandard Python dependencies are required.

## Relationship to prior work

The sample-count comparison and relative-entropy notation follow Johnson, Gavalakis, and Kontoyiannis, *Relative entropy bounds for sampling with and without replacement* (first public version April 9, 2024), which develops composition-sensitive upper bounds and compares balanced versus extreme color populations. Its leading theorem assumes the sample contains at most half of the population, and its discussion of the very unbalanced case treats a fixed sampling fraction. Neither result implies the present exact near-census composition optimizer, whose sample contains all but one ball. Harremoës and Matúš (2020) establish divergence inequalities and a fixed-fraction asymptotic; those results likewise do not determine the square-root displacement or the \(1/(6n^2)\) excess. The relationship is one of a new near-census extremal calculation using the same established probability model, not an independent definition of that model.

## Limitations

The optimal composition is specified asymptotically; no formula for its exact integer value or finite-\(n\) uniqueness is claimed. No statement is made for samples leaving two or more balls, for more than two colors, for replacement models with unequal draw weights, or for the divergence in the reverse direction. The entire result is for the two **count** laws, not the joint distributions of ordered color sequences. A complete search of every historical source cannot be certified, and priority requires independent scholarly verification. Independent mathematical validation has not been performed.

## References

1. Oliver Johnson, Lampros Gavalakis, and Ioannis Kontoyiannis, *Relative entropy bounds for sampling with and without replacement*, arXiv:2404.06632, first posted April 9, 2024. https://arxiv.org/abs/2404.06632 ; Journal of Applied Probability 62 (2025), 1578–1593, https://doi.org/10.1017/jpr.2025.27 .
2. Peter Harremoës and František Matúš, *Bounds on the information divergence for hypergeometric distributions*, Kybernetika 56 (2020), 1111–1132, https://doi.org/10.14736/kyb-2020-6-1111 ; https://arxiv.org/abs/2002.03002 .
