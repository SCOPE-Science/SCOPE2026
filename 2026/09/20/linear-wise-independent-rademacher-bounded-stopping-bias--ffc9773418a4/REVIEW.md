# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The two-block upper bound is pathwise: after the block boundary, every selected partial sum is bounded between the minimum and maximum of the second-block walk. Because the first block has mean-zero sum and the second block has the iid simple-walk law, taking expectations gives the stated envelope. The extremizing stopping time is legitimate because the linear-character construction makes the complete second block measurable at the block boundary; the first maximizer is therefore already measurable when the second block begins.

The limited-independence calculation is exact. For coefficient matrix \([I_m\ A]\), a dependence relation is \((Ay,y)\), so the minimum relation weight is \(d(A)=\min_{y\ne0}(\operatorname{wt}(y)+\operatorname{wt}(Ay))\). Uniform latent bits therefore produce \((d(A)-1)\)-wise independent signs. The random-injective-map criterion follows by first moment: each fixed nonzero \(y\) is sent uniformly to a nonzero \(m\)-bit vector. The entropy corollary is the standard binomial-volume estimate.

The simplex specialization was checked directly from its systematic relation code: length \(2^r-1\), dimension \(r\), and minimum distance \(2^{r-1}\) give \((N-1)/2\)-wise independence while leaving an iid predictable tail of length \(r\). The closed form for the simple-walk maximum follows from the reflection identity and standard central-binomial moments.

The global \(O(\sqrt N)\) upper bound is not re-proved here; it uses Narayanan's published four-wise maximal second-moment theorem. Since any \(k\)-wise law with \(k\ge4\) is four-wise independent, Cauchy--Schwarz transfers that theorem immediately to bounded stopped expectations. Combined with the code construction, this gives the claimed \(\Theta_\delta(\sqrt N)\) order for every fixed \(\delta<1/2\).

Exact-rational checks independently reproduce the elementary extremizers and the reported finite examples.

## Originality

**PASS, to the best of our knowledge.** The classical ingredients are explicitly separated from the proposed contribution. Wald's stopped-sum theory, pairwise-independent but globally deterministic families, Walsh-character constructions, k-wise-independent random walks, binary-code constructions of limited independence, and simple-walk reflection formulas are not claimed as new.

The most relevant primary random-walk source inspected was Benjamini--Kozma--Romik (2006): its Theorem 1 constructs pairwise-independent signs with almost-surely bounded partial sums and identifies the Walsh-system mechanism. Narayanan's later work studies maximal moments under k-wise independence and proves the four-wise maximal bound used for the global upper estimate. Joffe's 1971 note gives a still earlier demonstration that pairwise-independent families can be collectively almost deterministic. Wang (1990) places such independent-subset constructions in a broader historical line.

Literature checks covered optional stopping, Wald identities, stopped sums, pairwise and k-wise independent increments, limited-independent random-walk maxima, Walsh systems, orthogonal arrays and linear-code constructions, and online stopping/prophet problems under pairwise-independent priors. No located source states the exact two-iid-block stopped-sum envelope together with a completely predictable future iid block, the systematic-code distance criterion preserving its sharpness at linear independence levels, or the resulting fixed-fraction \(\Theta(\sqrt N)\) bounded-stopping bias.

The principal residual originality risk is terminological: an equivalent construction may be present in older orthogonal-array, resilient-function, coding, or optimal-stopping literature without being phrased as a limited-independence stopped-sum theorem. The coding existence step itself is a standard probabilistic-method argument and is not part of the novelty claim. Pairwise independence being insufficient for martingale arguments is also not claimed as a new observation; the claimed contribution is the sharp envelope and high-independence quantitative realization.

## Value

**PASS.** Optional stopping depends on conditional fairness with respect to the full past, whereas limited independence controls only small coordinate subsets. The result quantifies the gap in a particularly stringent setting: both halves individually look exactly iid, and the full increment family may remain independent on a linear fraction of coordinates, yet a legal bounded stopping rule can create a full square-root-scale mean shift. The simplex family additionally shows a diverging bias at essentially half-wise independence. This gives a concrete boundary phenomenon relevant to probabilistic reasoning with pseudorandom or limited-independent streams.

## Scientific limitations

The exact leading constant is established only for the two-block class; the global fixed-fraction theorem is order-sharp rather than constant-sharp. The construction is for fair binary increments. The linear-wise existence range uses a sufficient coding bound, not an optimal code-rate/distance tradeoff, so it does not identify the largest possible independence fraction compatible with a specified bias. At the half-wise boundary only the explicit \(\Omega(\sqrt{\log N})\) lower family is claimed, not a matching global order. Equivalent prior formulations under coding or orthogonal-array language remain the main originality uncertainty.
