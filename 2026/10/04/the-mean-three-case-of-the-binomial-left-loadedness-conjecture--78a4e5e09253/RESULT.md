# The mean-three case of the binomial left-loadedness conjecture
## Finding
For every integer \(n\ge 6\), let \(X\sim\operatorname{Bin}(n,3/n)\). Define, for \(i\in\{1,2,3}\),
\[
\alpha_i=\Pr(X\le 3-i)-\Pr(X\ge 3+i).
\]
Then \(X\) is left-loaded in the sense of Fokkink, Papavassiliou and Pelekis. More specifically, at \(n=6\) all three coefficients vanish, and for every \(n>6\) one has \(\alpha_1>0\) and \(\alpha_3<0\). Therefore the three-term sequence \(\alpha_1,\alpha_2,\alpha_3\) changes sign once from nonnegative to nonpositive, so condition \(L_1\) holds.

This proves their Conjecture 4.1 for the complete mean-three slice. Their paper explicitly states that the binomial conjecture was already verified for means \(1,2\) and for \(4\le m\le n/3\), leaving \(m=3\) outside the stated proved ranges.

## Assumptions and scope
The sample size \(n\) is an integer with \(n\ge6\). The success probability is exactly \(3/n\), so the binomial mean is the integer \(3\) and \(3/n\le1/2\). Left-loadedness is the source definition: either condition \(L_1\), a single sign change of the coefficients \(\alpha_i\), or condition \(L_2\), nonnegative initial partial sums. Only \(L_1\) is needed here.

The result concerns only mean \(3\). It does not settle Conjecture 4.1 for arbitrary integer mean.

## Proof
When \(n=6\), the law is \(\operatorname{Bin}(6,1/2)\), symmetric about its mean \(3\). Thus for every \(i\in\{1,2,3}\),
\[
\Pr(X\le3-i)=\Pr(X\ge3+i),
\]
so \(\alpha_1=\alpha_2=\alpha_3=0\), which satisfies \(L_1\).

Now assume \(n>6\). Simmons' inequality for a binomial variable with integer mean \(m\) and \(n>2m\) states
\[
\Pr(X\le m-1)>\Pr(X\ge m+1).
\]
At \(m=3\) this is exactly \(\alpha_1>0\).

It remains to force the opposite sign at the far endpoint. Put \(x=n-3\), so \(x\ge4\). Comparing the two point masses gives
\[
\frac{\Pr(X=6)}{\Pr(X=0)}
=\binom{n}{6}\left(\frac{3}{n-3}\right)^6
=\frac{81}{80}\frac{(x+3)(x+2)(x+1)(x-1)(x-2)}{x^5}.
\]
Subtracting one and factoring yields the exact identity
\[
\frac{\Pr(X=6)}{\Pr(X=0)}-1
=\frac{(x-3)Q(x)}{80x^5},
\]
where
\[
Q(x)=x^4+246x^3+333x^2-216x-324.
\]
For \(x\ge4\),
\[
Q(x)=x^4+246x^3+333(x-4)^2+2448(x-4)+4140>0.
\]
Hence \(\Pr(X=6)>\Pr(X=0)\). Since
\[
\alpha_3=\Pr(X=0)-\Pr(X\ge6)\le \Pr(X=0)-\Pr(X=6)<0,
\]
we have \(\alpha_1>0\) and \(\alpha_3<0\).

There is only one intermediate coefficient. If \(\alpha_2\ge0\), choose the sign-change index \(\ell=2\); if \(\alpha_2<0\), choose \(\ell=1\). In either case condition \(L_1\) is satisfied. This proves the claim.

## Verification
The proof is analytic and covers every integer \(n\ge6\). The bundled checker verifies the algebraic factorization of the point-mass ratio and the positive decomposition of \(Q(x)\); it also exactly evaluates the three coefficients for several small values of \(n\) as a stress test. Those finite checks are supplementary and are not used to infer the infinite statement.

The only imported theorem is Simmons' classical binomial inequality. The 2022 source states it with the exact hypotheses needed here, and the 2007 Perrin--Redside abstract independently restates Simmons' theorem as \(\Pr(X_m<m)>\Pr(X_m>m)\) under \(0<2m<n\), which is the same \(\alpha_1>0\) statement for an integer-mean binomial law.

## Relationship to prior work
Fokkink, Papavassiliou and Pelekis define left-loadedness and conjecture that \(\operatorname{Bin}(n,m/n)\) is left-loaded whenever \(n\ge2m\). Immediately before the conjecture, their full text says they can verify condition \(L_2\) for \(m\in\{1,2}\) and condition \(L_1\) for \(4\le m\le n/3\). Thus the complete \(m=3\) slice is not included in their stated binomial proof range.

Simmons' theorem supplies only the near-mean inequality \(\alpha_1>0\). The additional far-tail comparison \(\alpha_3<0\), together with the fact that there are only three coefficients, is what upgrades that one inequality to left-loadedness.

Targeted searches for the source conjecture, the phrase “left-loaded” with mean \(3\), the exact family \(\operatorname{Bin}(n,3/n)\), and the point-mass mechanism above did not locate a later statement covering this slice. This is evidence for originality, not a claim that search failure alone proves novelty.

## Limitations
The argument exploits the three-coefficient structure at mean \(3\). For larger means, signs at the first and last coefficient do not by themselves control all intermediate coefficients, so this proof does not extend the conjecture mechanically. A later result under different terminology or in a poorly indexed source could have escaped the searches; this remains the principal originality risk.

## References
1. R. Fokkink, S. Papavassiliou, and C. Pelekis, “On the monotonicity of tail probabilities,” Probability and Mathematical Statistics 42 (2022), 133–141. DOI: 10.37190/0208-4147.00050. Published online 2022-06-06.
2. T. C. Simmons, “A New Theorem in Probability,” Proceedings of the London Mathematical Society, s1-26 (1894), 290–325. DOI: 10.1112/plms/s1-26.1.290.
3. O. Perrin and E. Redside, “Generalization of Simmons' theorem,” Statistics & Probability Letters 77 (2007), 604–606. DOI: 10.1016/j.spl.2006.09.006.
