# Discrete-Gaussian lattice phases in logarithmic-colour Markov logic networks

## Finding
Consider the two-predicate Markov logic network for a unary colour \(P\) and a binary relation \(R\) on the labelled domain \([n]\), with the eight nonnegative weights of a complete set of Boolean colour/edge constraints. Let \(c_{11},c_{00},c_{10},c_{01}>0\) be the total edge-weight factors for each ordered colour pair, as defined below. Assume
\[
c_{10}c_{01}=c_{00}^{2},\qquad 0<c_{11}<c_{00},\qquad a=\log(c_{00}/c_{11})>0.
\]
Let \(M_n\) be the number of vertices of colour \(P\). Put
\[
x_n=\frac{W(2an)}{2a},\quad h_n=\lfloor x_n\rfloor,\quad \theta_n=x_n-h_n,\quad
\Theta_a(\theta)=\sum_{j\in\mathbb Z}\exp(-a(j-\theta)^2),
\]
where \(W\) is the positive real Lambert function. Then, with \(Q_{a,\theta}\) the probability law on the integers assigning mass \(\exp(-a(j-\theta)^2)/\Theta_a(\theta)\) to \(j\),
\[
d_{\mathrm{TV}}\big(\mathcal L(M_n-h_n),Q_{a,\theta_n}\big)\longrightarrow0. \tag{1}
\]
Furthermore the exact colour partition sum has the asymptotic form
\[
\sum_{m=0}^{n}\binom nm e^{-am^2}
=\frac{\exp(a x_n^2+x_n)}{\sqrt{2\pi x_n}}\Theta_a(\theta_n)\,[1+o(1)].\tag{2}
\]
Each \(\theta\in[0,1)\) occurs as a subsequential limit of \(\theta_n\). Consequently \(M_n-h_n\) has distinct subsequential weak limits \(Q_{a,\theta}\); it has **no single limiting integer-valued law**. The theta factor in (2) is genuinely nonconstant in its lattice phase.

A colour-reversed companion holds when \(c_{10}c_{01}=c_{11}^{2}\) and \(c_{00}<c_{11}\): then (1)–(2) apply to the number \(n-M_n\) of vertices with \(\neg P\), using \(a=\log(c_{11}/c_{00})\).

## Assumptions and scope
For each ordered pair \((u,v)\), including loops, two possible values of \(R(u,v)\) are summed. If the ordered colour pair is \((s,t)\in\{0,1\}^2\) and its two soft-constraint weights are \(w_{st,0},w_{st,1}\ge0\), define \(c_{st}=e^{w_{st,0}}+e^{w_{st,1}}\). Conditional on all unary colours, binary edge choices are independent. The network uses **unscaled** feature weights. There are exactly \(n^2\) directed edge variables. The result concerns the colour-count distribution, not probabilities of arbitrary first-order sentences.

The parameter hypothesis is realizable with nonnegative weights. For example, give weight \(\log 3\) to the feature \(R(u,v)\land\neg(P(u)\land P(v))\), all other constraints zero. Then \(c_{11}=2\), and \(c_{00}=c_{01}=c_{10}=4\), so \(a=\log2\) and \(\mathbb P(M_n=m)\propto\binom nm2^{-m^2}\).

## Proof
**Exact reduction.** For a fixed assignment with \(m\) coloured vertices, summation over every binary edge variable gives the factor
\[
c_{11}^{m^2}c_{00}^{(n-m)^2}c_{10}^{m(n-m)}c_{01}^{m(n-m)}.
\]
There are \(\binom nm\) assignments of the unary predicate with that size. On the displayed boundary the factor equals \(c_{00}^{n^2}(c_{11}/c_{00})^{m^2}\). Thus, with
\[
b_{n,m}=\binom nm e^{-a m^2},\qquad Z_n=\sum_{m=0}^n b_{n,m},
\]
we have the **exact** identity \(\mathbb P(M_n=m)=b_{n,m}/Z_n\).

**Saddle.** The defining equation of the Lambert function gives \(\log(n/x_n)=2a x_n\); hence \(x_n\to\infty\) and \(x_n=O(\log n)\). Uniformly for \(m=O(\log n)\), falling-factorial expansion and Stirling's formula give
\[
\log b_{n,m}=m\log n-m\log m+m-a m^2-\tfrac12\log(2\pi m)+o(1).
\]
The smooth exponent \(f_n(t)=t\log n-t\log t+t-at^2\) satisfies \(f_n'(x_n)=0\) and \(f_n''(x_n)=-2a-1/x_n\). Consequently, for every fixed integer \(j\), uniformly over the varying phase \(0\le\theta_n<1\),
\[
\log b_{n,h_n+j}=a x_n^2+x_n-\tfrac12\log(2\pi x_n)
-a(j-\theta_n)^2+o(1).\tag{3}
\]

**Uniform summable tails.** The exact successive-term ratio is
\[
r_{n,m}=\frac{b_{n,m+1}}{b_{n,m}}
=\frac{n-m}{m+1}e^{-a(2m+1)},
\]
strictly decreasing in \(m\). Writing \(h=h_n\), \(x=x_n\), for all \(t\ge0\) with \(h+t<n\),
\[
r_{n,h+t}\le\frac nx e^{-a(2h+2t+1)}\le e^{a-2at}.
\]
Thus \(b_{n,h+j}/b_{n,h}\le\exp(-a j^2+2aj)\) for \(j\ge0\) (a harmless relaxed bound). On the left, for \(1\le t\le h\),
\[
\log r_{n,h-t}\ge
\log\frac{n-h}{h+1}-a(2h-2t+1)
=2a(x-h)+a(2t-1)+o(1),
\]
with error uniform in \(t\) because the two logarithmic factors are independent of \(t\). For sufficiently large \(n\), this is at least \(a(2t-1)-1\); multiplying the ratios yields \(b_{n,h-j}/b_{n,h}\le\exp(-a j^2+j)\) for \(1\le j\le h\). These Gaussian-dominated bounds control both tails uniformly in \(n\). Equation (3), finite-window convergence and summable domination imply (2), and also (1) by Scheffé's lemma for countable probability measures (equivalently by direct summing the pointwise absolute errors). No normal approximation with a diverging variance is used.

**Lattice phases.** Since \(n=x_ne^{2ax_n}\), the increasing sequence \(x_n\) diverges and \(x_{n+1}-x_n\to0\). Its fractional parts therefore have every phase in \([0,1)\) as a subsequential limit. The ratio \(Q_{a,\theta}(1)/Q_{a,\theta}(0)=\exp[-a(1-2\theta)]\) distinguishes phases. Finally Poisson summation gives
\[
\Theta_a(\theta)=\sqrt{\pi/a}\sum_{\ell\in\mathbb Z}e^{-\pi^2\ell^2/a}e^{2\pi i\ell\theta},
\]
whose first nonzero Fourier coefficient establishes nonconstancy. Exchanging colours gives the companion case.

## Verification
The standalone `checker.py` performs independent exact integer-weight enumeration of the example network on \(n=1,2,3\) domains; compares the exact colour-count law with the asserted binomial-quadratic law; and numerically compares the finite-size probability mass function, theta approximation, and saddle partition factor over several sizes and positive \(a\). The checker is a finite consistency test, **not** a proof of the infinite limits. Equations (1)–(2) follow from the exact counting identity and the summable ratio bounds above.

## Relationship to prior work
Tousinejad and Koponen (2026) introduced the eight-weight coloured-digraph Markov logic network and classified seven unscaled-weight asymptotic regimes. In particular their stated main theorem identifies logarithmic minority-count cases. The present statement concerns the finer **order-one** fluctuations in the logarithmic regimes: phase-dependent discrete-Gaussian laws in total variation, an oscillating theta factor in the exact colour partition sum, and the full set of subsequential laws. The exact one-variable partition polynomial is **not new as an abstract polynomial family**: it equals Sokal's deformed binomial polynomial \(F_{-1/n}(ne^{-a},e^{-2a})\), introduced in his 2013 Warwick lecture (slide 24). The inspected Sokal slides concern roots, coefficient properties and deformations, not a probability law at this moving argument. The new claim is limited to the **fixed-coupling, growing-domain** total-variation theta law and uniform phase-resolved partition asymptotic for the Markov logic network. The general discrete Gaussian and theta functions, Lambert function, and saddle-point tools are classical; no novelty is claimed for those ingredients. A direct equivalent in the 2026 source paper's later detailed analysis or another earlier treatment cannot be excluded because not all relevant full text was accessible during comparison.

## Limitations
The claim is about labelled domains with directed loops allowed, independent binary edge variables conditional on unary colours, and fixed unscaled nonnegative weights satisfying an exact parameter identity. The theta law is not a first-order zero-one/convergence theorem; it only describes the auxiliary colour count. In the dual case the rare colour is \(\neg P\). The proof says nothing about perturbations away from the exact logarithmic phase boundaries. The finite checker does not prove asymptotic independence or any claim for arbitrary random-relational models. Publication priority remains subject to fuller comparison with possibly inaccessible earlier work.

## References
1. Y. Tousinejad and V. Koponen, *Random coloured digraphs defined by a Markov logic network*, arXiv:2606.23715, first posted 2026-06-16; https://arxiv.org/abs/2606.23715.
2. R. M. Corless et al., *On the Lambert W function*, Advances in Computational Mathematics **5** (1996), 329–359, https://doi.org/10.1007/BF02124750 (classical Lambert-function background).
3. A. D. Sokal, *Roots of a formal power series with applications to graph enumeration and q-series*, Warwick Mathematics Colloquium, 15 February 2013, slide 24 (definition of the deformed binomial polynomial), https://warwick.ac.uk/fac/sci/maths/research/events/colloquium/2012-13/sokal_feb_15_13_talk.pdf.
4. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009 (standard saddle-point and lattice-asymptotic background).
