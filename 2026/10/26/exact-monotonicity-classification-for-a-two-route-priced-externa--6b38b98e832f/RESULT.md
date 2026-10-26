# Exact monotonicity classification for a two-route priced externality

## Finding

Consider one unit of nonatomic traffic choosing between two parallel routes. The travel-time functions are \(\tau_1(x_1)=x_1\) and \(\tau_2(x_2)=x_2\), with \(x_1+x_2=1\). A nonnegative price \(\lambda\) is applied to per-unit externalities \(g_1(x_1)=a\) and \(g_2(x_2)=b x_2\), where \(a,b>0\). Thus the perceived route costs are \(c_1=x_1+\lambda a\) and \(c_2=(1+\lambda b)x_2\), and the aggregate externality is \(G=a x_1+b x_2^2\).

The exact monotonicity classification is:

- If \(0<b\le a/2\), then \(G(\lambda)\) strictly decreases until route 1 empties, at \(\lambda_*=(a-b)^{-1}\), and is constant thereafter.
- If \(a/2<b<a\), then \(G(\lambda)\) first decreases, then increases before route 1 empties, and is constant thereafter. It is not monotone.
- If \(a\le b<2a\), then \(G(\lambda)\) is strictly increasing for \(\lambda>0\).
- If \(b=2a\), then \(G(\lambda)\) is constant.
- If \(b>2a\), then \(G(\lambda)\) is strictly decreasing.

Consequently, pricing increases the aggregate externality exactly in the parameter regime \(a\le b<2a\). This can happen with only two parallel routes, without a Braess-type network. A one-route network has fixed flow under fixed demand, so two routes are minimal for price-induced growth in this model.

## Assumptions and scope

There is one origin-destination pair, fixed unit demand, and two parallel routes. Route flow is nonnegative and sums to one. Each traveler chooses a route of minimum perceived cost. The travel times are linear and strictly increasing. The priced per-unit externality on route 1 is constant, while that on route 2 is linear in its own flow. The aggregate externality is defined as flow times per-unit externality, summed over the two routes. The result is a static Wardrop-equilibrium statement for this exact family; it is not an empirical claim about every pollutant or traffic network.

## Proof

Write \(x=x_2\), so \(x_1=1-x\). When both routes carry positive flow, the Wardrop condition equates their costs:

\[
1-x+\lambda a=(1+\lambda b)x.
\]

Solving gives

\[
x_2(\lambda)=\frac{1+a\lambda}{2+b\lambda},\qquad
x_1(\lambda)=\frac{1+(b-a)\lambda}{2+b\lambda}.
\]

If \(b\ge a\), both flows remain positive for every finite \(\lambda\ge0\). If \(b<a\), route 1 empties at \(\lambda_*=(a-b)^{-1}\). For \(\lambda\ge\lambda_*\), the equilibrium is \((x_1,x_2)=(0,1)\), because the unused route 1 costs \(\lambda a\), which is at least the used route 2 cost \(1+\lambda b\). The equilibrium is unique: each perceived edge cost is strictly increasing in its own flow, and the total demand is fixed.

On the interval where both routes are used,

\[
G(\lambda)=a(1-x_2(\lambda))+b x_2(\lambda)^2,
\qquad
x_2'(\lambda)=\frac{2a-b}{(2+b\lambda)^2},
\]
so

\[
G'(\lambda)=\bigl(2b x_2(\lambda)-a\bigr)
\frac{2a-b}{(2+b\lambda)^2}.
\]

For \(b<a\), the flow \(x_2\) increases from \(1/2\) to \(1\), while the factor \(2b x_2-a\) increases from \(b-a<0\) to \(2b-a\). It stays nonpositive exactly when \(b\le a/2\); when \(a/2<b<a\), it crosses zero once, producing a decrease followed by an increase before the constant tail \(G=b\). For \(a\le b<2a\), \(x_2'>0\) and \(2b x_2-a>0\) for every \(\lambda>0\), so \(G\) strictly increases. When \(b=2a\), \(x_2\equiv1/2\), hence \(G\) is constant. When \(b>2a\), \(x_2'<0\) and \(2b x_2-a>0\), so \(G\) strictly decreases. This proves the classification.

For the concrete case \(a=b=1\),

\[
G(\lambda)=\frac{\lambda^2+3\lambda+3}{(\lambda+2)^2},
\qquad G'(\lambda)=\frac{\lambda}{(\lambda+2)^3}>0
\quad(\lambda>0),
\]
which exhibits the increase exactly. With only one route, fixed demand fixes its flow and therefore fixes \(G\); the two-route example is minimal in route count.

## Verification

The equilibrium equations are solved exactly, and the boundary case \(b<a\) is checked by the unused-route inequality. The sign analysis of \(G'\) partitions all \(b>0\) into the five cases above, including the equality boundaries \(b=a/2\), \(b=a\), and \(b=2a\). No finite simulation is used as a proof. The claim concerns the defined aggregate externality, not total travel time or a calibrated real-world emissions measure.

## Relationship to prior work

Klimm, Markl, Warode, Griesbach, and Harks study priced flow-dependent externalities in a general Wardrop model. Their Lemma 4.1 proves monotonicity under flow-independent externalities; their Example 4.3 gives a flow-dependent counterexample on a Braess-inspired network. The result here gives an exact coefficient-ratio classification for a two-parallel-route family and isolates a minimal route-choice mechanism. The broader fact that flow-dependent externality can increase under pricing is already present in that paper; the specific two-route classification and its thresholds are the claim here.

## Limitations

The assumptions are deliberately narrow: one commodity, fixed unit demand, equal unit-slope travel-time functions, and per-unit externalities of the forms \(a\) and \(b x_2\). The theorem does not assert that price increases externalities in arbitrary networks, nor that actual vehicle emissions follow these functions. The literature search cannot exclude an unpublished or differently phrased derivation of this elementary two-route case.

## References

S. M. Griesbach, T. Harks, M. Klimm, M. Markl, and P. Warode, “Carbon Pricing in Traffic Networks,” arXiv:2508.09280, first publicly posted 12 August 2025. Primary full text: https://arxiv.org/abs/2508.09280 and https://arxiv.org/pdf/2508.09280.
