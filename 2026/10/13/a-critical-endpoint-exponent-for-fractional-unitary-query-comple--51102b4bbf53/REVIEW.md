# Self-review

## Correctness

PASS. The lower half uses the anchor's explicit unspecialized Remez inequality
\[
Q(t,\delta,\varepsilon)\ge \frac{1}{4\delta}\log\frac{\sin(\pi t)}{4\varepsilon},
\]
and \(\sin(\pi c\varepsilon^\alpha)=\pi c\varepsilon^\alpha(1+o(1))\). The matching upper order for \(0<\alpha<1\) is the universal QSVT upper bound. For \(\alpha>1\), a direct spectral-arc estimate converted to diamond norm proves the zero-query and one-query endpoint statements uniformly over the promised oracle family.

No infinite claim is inferred from numerical experiments; the checker is corroborative only.

## Originality

PASS. The anchor proves optimality only for \(t\) bounded away from \(0\) and \(1\) and explicitly lists dependence on \(t\) as open. The inspected earlier fractional-query papers do not state a scaling theorem in which the distance of \(t\) from an integer is \(c\varepsilon^\alpha\). Exact and alias searches found no implication-equivalent published statement.

## Value

PASS. The theorem identifies a sharp natural exponent boundary in the open endpoint-dependence direction: the full logarithmic query cost persists for \(0<\alpha<1\), while endpoint-trivial algorithms take over for \(\alpha>1\). It isolates the remaining unresolved behavior to the constant-scale transition around \(\alpha=1\), rather than giving only a constant-factor refinement.

Closest literature and limitations are described in the result and structured audit. The theorem does not settle the full uniform-in-\(t\) conjecture, does not classify the \(\alpha=1\) constants, and does not address uncontrolled or average-case access.

Self-review: passed. Independent audit: not yet performed.
