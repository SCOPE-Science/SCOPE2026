# Correlated patch weather creates a sharp dormant-seed phase transition

## Finding

Let \(k\ge 1\) equally weighted habitat patches share a fresh annual latent weather quality \(P\sim\operatorname{Beta}(\alpha,\beta)\), where \(\alpha,\beta>0\). Conditional on \(P\), each patch independently yields a favorable season with probability \(P\). Let \(K_k\) denote the number of favorable patches. An annual seed bank that holds back fraction \(h\in[0,1]\) and germinates \(1-h\) has random density-independent multiplication factor
\[
R_k(h)=s h+B(1-h)\frac{K_k}{k},
\]
where \(0<s\le1\) is dormant survival and \(B>0\) is seed output per germinated seed in favorable patches. In distinct years the latent weather and conditional patch outcomes are independent. Maximize the almost-sure long-run logarithmic growth rate \(L_k(h)=\mathbb E[\log R_k(h)]\); set \(L_k(1)=\log s\).

**Theorem.** Assume \(B\alpha/(\alpha+\beta)>s\). For every finite \(k\) the optimum \(h_k\) exists uniquely in \((0,1)\), is strictly decreasing in \(k\), and converges to the unique maximizer \(h_\infty\) of
\[
 L_\infty(h)=\mathbb E_{P}[\log(sh+B(1-h)P)].
\]
Define \(r=(s/B)\mathbb E[P^{-1}]\), taking \(r=+\infty\) if the inverse moment diverges. Then \(h_\infty>0\) **if and only if** \(r>1\). Specifically, \(r=+\infty\) for \(\alpha\le1\), while for \(\alpha>1\),
\[
 r=\frac{s(\alpha+\beta-1)}{B(\alpha-1)}.
\]
When \(\alpha>1\) and \(r<1\), the optimal dormant reserve vanishes at the **sharp polynomial rate**
\[
 \boxed{h_k\sim \frac{\Gamma(\alpha+\beta)}{\Gamma(\beta)(1-r)}\,k^{-\alpha}.}
\]
At the critical boundary \(r=1\), the theorem asserts \(h_k\downarrow0\) but makes no universal rate claim.

Three exact illustrations mark distinct regimes. With \((\alpha,\beta,s,B)=(2,1,1,4)\), \(h_k\sim4k^{-2}\). With \((2,1,1,2)\), \(r=1\) and **exactly** \(h_k=2/(k+2)\) for every \(k\ge1\). With \((1/2,1/2,1,4)\), \(h_k\downarrow1/3\). Thus a common environmental component can preserve a positive dormant reserve even with infinitely many patches, or convert exponentially rare failures under independent fixed-quality patches into polynomially rare shared failures.

## Assumptions and scope

The weather state \(P\) is redrawn independently each year. Within a year all \(k\) patches share it, but favorable-patch indicators are independent conditional on \(P\); hence their marginal correlation is strictly positive. Seeds are pooled and uniformly allocated over the \(k\) patches; dormant seeds survive at deterministic fraction \(s\). The germination decision is a fixed genotype-like fraction, not weather-adaptive. No density dependence, finite census extinction, patch-specific seed banks, dispersal mortality, or environmentally dependent dormancy survival is modeled. \(L_k\) is an almost-sure growth exponent for this scalar multiplicative process when the logarithm is integrable; it is not an extinction-probability objective. If \(B\alpha/(\alpha+\beta)\le s\), concavity instead gives the unique optimum \(h=1\) for every finite \(k\).

## Proof

**1. Interior uniqueness.** Write \(Y_k=K_k/k\). The beta-binomial distribution gives \(\Pr(Y_k=0)=q_k=\mathrm B(\alpha,\beta+k)/\mathrm B(\alpha,\beta)>0\), while \(\mathbb EY_k=\alpha/(\alpha+\beta)\). For \(0<h<1\), differentiation under the finite sum yields
\[
 L'_k(h)=\mathbb E\frac{s-BY_k}{sh+B(1-h)Y_k},\qquad
 L''_k(h)=-\mathbb E\frac{(s-BY_k)^2}{[sh+B(1-h)Y_k]^2}<0.
\]
The derivative tends to \(+\infty\) at \(h\downarrow0\), because of \(q_k>0\), and \(L'_k(1)=1-B\mathbb EY_k/s<0\). Hence there is one strict interior maximizer, characterized by
\[
\boxed{\mathbb E\frac{1}{h_k+(B/s)(1-h_k)Y_k}=1.}\tag{1}
\]
For the identity, use \(s-BY=(s-R)/(1-h)\) with \(R=sh+B(1-h)Y\).

**2. Strict decrease with patch count.** Condition on \(P=p\in(0,1)\). The mean of \(k+1\) Bernoulli observations is a strict mean-preserving contraction, in convex order, of the mean of \(k\) observations: choose a uniformly random \(k\)-subset from the \(k+1\) observations and condition its mean on all \(k+1\). For fixed \(0<h<1\), \(y\mapsto[sh+B(1-h)y]^{-1}\) is strictly convex. Thus its expectation strictly decreases from \(k\) to \(k+1\), first conditionally and then unconditionally. The right side of (1) at the \(k\)-optimizer is consequently strictly smaller than one for \(k+1\), so strict concavity implies \(h_{k+1}<h_k\).

**3. Infinite-patch limit and phase boundary.** Couple all patch indicators conditionally on a common \(P\). Conditional strong laws give \(Y_k\to P\) almost surely. On each compact subinterval of \((0,1]\), the logarithms and first derivatives converge in expectation by bounded convergence. The endpoint \(h=0\) is also well-defined for the limiting distribution because \(\mathbb E|\log P|<\infty\) for every positive beta shape. Strict concavity, together with the interior derivative signs at fixed \(h>0\), implies \(h_k\to h_\infty\), the unique maximizer of \(L_\infty\). Its right derivative at zero has the sign of
\[
\lim_{h\downarrow0}L'_\infty(h)=\frac{s}{B}\mathbb E[P^{-1}]-1=r-1,
\]
including \(+\infty\) when \(\alpha\le1\). Since \(L'_\infty(1)=1-B\mathbb EP/s<0\), strict concavity implies \(h_\infty>0\) precisely when \(r>1\). The displayed beta inverse moment follows from \(\mathrm B(\alpha-1,\beta)/\mathrm B(\alpha,\beta)\).

**4. Sharp vanishing reserve.** Suppose \(\alpha>1\) and \(r<1\). We already know \(h_k\downarrow0\). Splitting (1) at \(K_k=0\) gives
\[
1=\frac{q_k}{h_k}+S_k,\qquad
S_k=\mathbb E\left[\frac{\mathbf 1_{\{K_k>0\}}}{h_k+(B/s)(1-h_k)K_k/k}\right].\tag{2}
\]
We show \(S_k\to r\). For \(h_k\le1/2\), conditional on \(P=p\), \(S_k\)'s integrand is bounded by \(2(s/B)k/K_k\) on \(K_k>0\). The binomial identity
\[
\mathbb E\left[\frac{k}{K_k+1}\mid P=p\right]
=\frac{k}{(k+1)p}[1-(1-p)^{k+1}]\le\frac1p
\]
and \(1/j\le2/(j+1)\) for integer \(j\ge1\) give a conditional bound \(4s/(Bp)\). For every fixed \(p>0\), binomial concentration ensures the conditional expectation of the integrand converges to \(s/(Bp)\): on \(K_k\ge kp/2\) use bounded convergence in probability, and the complementary positive-count event has expectation at most \(Ck e^{-kp/8}\). Since \(\mathbb E[P^{-1}]<\infty\), dominated convergence over \(P\) proves \(S_k\to r\). Thus (2) gives \(q_k/h_k\to1-r\). Finally
\[
 q_k=\frac{\Gamma(\alpha+\beta)}{\Gamma(\beta)}
      \frac{\Gamma(k+\beta)}{\Gamma(k+\alpha+\beta)}
 \sim\frac{\Gamma(\alpha+\beta)}{\Gamma(\beta)}k^{-\alpha},
\]
which proves the claimed equivalent.

**5. Exact boundary illustrations.** For \(P\sim\operatorname{Beta}(2,1)\), \(\Pr(K_k=j)=2(j+1)/[(k+1)(k+2)]\). Taking \(s=1,B=2,h=2/(k+2)\) makes \(R_k(h)=2(j+1)/(k+2)\), so \(\mathbb E[1/R_k(h)]=1\) exactly and (1) proves the critical closed form. For the arcsine beta law \(\alpha=\beta=1/2\), \(s=1,B=4\), the standard arcsine integral yields
\[
 L_\infty(h)=2\log\frac{\sqrt h+\sqrt{4-3h}}2.
\]
Its unique maximizer satisfies \(\sqrt{4-3h}=3\sqrt h\), hence \(h_\infty=1/3\). The subcritical example follows by inserting \(\alpha=2,\beta=1,s=1,B=4\) into the general equivalent.

## Verification

Run `python3 verify_beta_dormancy.py` using only the standard library. It checks the exact beta-binomial derivative at the critical closed form for 100 patch counts; 71 exact rational two-sided sign brackets consistent with \(4k^{-2}\) for \(30\le k\le100\); and 35 exact rational finite-count derivative signs consistent with convergence to \(1/3\). These finite computations are independent sanity checks, **not** proofs of the asymptotic equivalence, the universal phase criterion, or uniqueness; those are established analytically above.

## Relationship to prior work

Cohen (1966) developed the classical logarithmic-growth optimization for delayed germination under fluctuating seed yield. Klinkhamer et al. (1987) analyzed dispersal and dormancy jointly, including correlated spatial yields; their inspected full text models lognormal local yields and develops approximate fitness criteria, rather than the exact beta-mixture inverse-moment boundary and the rare-all-unfavorable-patch asymptotic. Venable and Brown (1988) explicitly considered interacting seed traits, spatial correlation and independent environmental patches; its accessible abstract does not resolve whether the precise beta-mixture asymptotic appears in the full text. Valleriani (2006) analyzed **temporal** yield autocorrelation, not the present iid-across-years, beta-correlated-across-patches mechanism. Chen et al. (2020) present an empirical global-scale dispersal–dormancy comparison, not this optimization theorem.

The concavity first-order condition in isolation is a standard bet-hedging calculation. The specific combined claim here is the beta-correlated spatial phase boundary, sharp coefficient \(\Gamma(\alpha+\beta)/[\Gamma(\beta)(1-r)]\) for the vanishing dormant reserve, and explicit contrasting boundary regimes. It is **not** a universal biological law and does not imply that correlated environmental conditions increase dormancy in every setting.

## Limitations

The Beta latent-weather assumption is a tractable stylized dependence model, not an empirical fit. The critical general asymptotic rate when \(r=1\) is not proved; the exact critical \(\operatorname{Beta}(2,1)\) example does not imply a universal exponent. Years must be independent for the stated almost-sure exponent interpretation. The central 1988 source could not be inspected in full, so unrecognized stronger/equivalent prior mathematics remains a concrete originality risk.

## References

1. D. Cohen (1966), *Optimizing reproduction in a randomly varying environment*, Journal of Theoretical Biology 12, 119–129, doi:10.1016/0022-5193(66)90188-3.
2. P. G. L. Klinkhamer, T. J. de Jong, J. A. J. Metz, J. Val (1987), *Life history tactics of annual organisms: The joint effects of dispersal and delayed germination*, Theoretical Population Biology 32, 127–156, doi:10.1016/0040-5809(87)90044-X.
3. D. L. Venable and J. S. Brown (1988), *The selective interactions of dispersal, dormancy, and seed size as adaptations for reducing risk in variable environments*, The American Naturalist 131, 360–384, doi:10.1086/284795.
4. A. Valleriani (2006), *Evolutionarily stable germination strategies with time-correlated yield*, Theoretical Population Biology 70, 255–261, doi:10.1016/j.tpb.2006.07.008.
5. S.-C. Chen et al. (2020), *Trade-off between seed dispersal in space and time*, Ecology Letters, doi:10.1111/ele.13595.
