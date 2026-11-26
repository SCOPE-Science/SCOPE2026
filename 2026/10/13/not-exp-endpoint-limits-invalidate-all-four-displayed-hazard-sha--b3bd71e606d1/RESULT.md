# NOT-Exp endpoint limits contradict four hazard-shape assignments accompanying Figure 1

## Finding

For \(\alpha,\gamma,\theta>0\) and \(y>0\), put \(v=1-e^{-\theta y}\). The NOT-Exp distribution of Alotaibi and Elshahhat has CDF and density
\[
G(y)=\left[\frac{(1+\alpha)v}{\alpha+v}\right]^\gamma,\qquad
g(y)=\frac{\alpha\gamma\theta(1+\alpha)^\gamma e^{-\theta y}v^{\gamma-1}}{(\alpha+v)^{\gamma+1}}.
\]
Its hazard \(h=g/(1-G)\) satisfies
\[
h(y)\sim \gamma\left(\frac{(1+\alpha)\theta}{\alpha}\right)^\gamma y^{\gamma-1}\quad(y\downarrow0),
\qquad
h(y)\longrightarrow\theta\quad(y\to\infty).
\]
In particular, \(h(0+)\) is \(+\infty\) for \(0<\gamma<1\), \((1+\alpha)\theta/\alpha\) for \(\gamma=1\), and \(0\) for \(\gamma>1\).

These endpoint laws contradict all four assignments in the prose accompanying Figure 1 (Alotaibi and Elshahhat, §2, p. 5). The order is \((\alpha,\gamma,\theta)\).

| Prose assignment | Parameter triple | Incompatible behavior |
| --- | --- | --- |
| Increasing | \((0.1,0.1,0.1)\) | Starts at \(+\infty\) and tends to \(0.1\). |
| Decreasing | \((2.8,4.5,1.5)\) | Starts at \(0\) and tends to \(1.5\). |
| Bathtub | \((1.5,2.8,1.5)\) | The positive hazard starts at \(0\), ruling out initial decline. |
| Upside-down bathtub | \((2.5,0.9,3.2)\) | Starts at \(+\infty\), ruling out initial rise. |

These are **prose assignments**, not a transcription of the hazard-panel legend. In Figure 1 (p. 6), the prose's \((1.5,2.8,1.5)\) triple appears in the density-panel legend; the hazard-panel legend instead lists \((1.5,1.2,1.5)\) and also lists \((0.5,1.1,1.5)\). Neither of those additional hazard-panel triples can have a global bathtub hazard with an initial decline, since both have \(\gamma>1\). This does not assign a shape label to any otherwise unlabelled curve.

## Assumptions and scope

The hazard is the one obtained from the paper's printed CDF and density on the entire positive half-line. Bathtub means initial decline followed by increase; upside-down bathtub means initial rise followed by decline. The constraints concern global shapes, not an impression on a finite plotting window. They do not classify all possible turning points or modify the inferential procedures. The parameter \(\theta\) is the coefficient of \(y\) in the exponential; the tail hazard is therefore \(\theta\), not \(1/\theta\).

## Proof

Write \(a=\alpha/(1+\alpha)\). As \(y\downarrow0\), \(v\sim\theta y\), \(e^{-\theta y}\to1\), and \(\alpha+v\to\alpha\). Substituting directly in the **exact density**, \(g(y)\sim\gamma(\theta/a)^\gamma y^{\gamma-1}\). Since \(G(y)\to0\), this is also the asymptotic of \(h(y)\).

For the far endpoint, set \(\epsilon=e^{-\theta y}\). The inner CDF factor is
\[
\frac{(1+\alpha)v}{\alpha+v}=\frac{1-\epsilon}{1-(1-a)\epsilon}=1-a\epsilon+O(\epsilon^2).
\]
Raising to \(\gamma\) gives \(1-G(y)\sim\gamma a\epsilon\); the exact density gives \(g(y)\sim\gamma a\theta\epsilon\). Their ratio tends to \(\theta\).

A globally nondecreasing function cannot have its initial limit above its terminal limit. This excludes increasing hazards for \(\gamma\le1\), since \(\theta/a>\theta\). A globally nonincreasing function cannot have its initial limit below its terminal limit; this excludes decreasing hazards for \(\gamma>1\). Moreover, a strictly positive function with left limit zero cannot be nonincreasing on any initial interval, and a finite-valued function with left limit \(+\infty\) cannot be nondecreasing on one. These facts give the bathtub and upside-down-bathtub exclusions and apply to the entries above.

## Verification and relation to prior work

The bundled `verify_notexp_endpoints.py` evaluates the CDF, density and hazard at high precision for the prose triples, with additional small-time checks, including \(\gamma=1\). These finite checks are not proofs of the limits or of the global exclusions. The hazard-panel alternatives are covered by the same symbolic \(\gamma>1\) argument. The source comparisons use the assignments in the article text and the separate legend of Figure 1; they do not reconstruct the original plotting code.

The inner CDF factor also equals a Marshall–Olkin exponential CDF with tilt \(a\) and rate \(\theta\), so the NOT-Exp law can be written as the \(\gamma\)-th power of that CDF. The point here is the concrete conflict between the model's endpoint behavior and the four source-specific hazard assignments, not a new construction of a distribution family or a new asymptotic method.

## Reference

R. Alotaibi and A. Elshahhat, “A New Exponential-Type Model Under Unified Progressive Hybrid Censoring: Computational Inference and Its Applications,” *Mathematics* **14** (2026), 1182, DOI `10.3390/math14071182`; §2, Eqs. (2)–(5) and accompanying prose, p. 5, and Figure 1, p. 6.
