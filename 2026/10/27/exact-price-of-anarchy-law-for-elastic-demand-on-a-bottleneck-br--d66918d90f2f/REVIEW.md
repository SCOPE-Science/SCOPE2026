# Scientific review

## Correctness — PASS

For \(u=x+y\) and \(v=x+z\), the three bottleneck path costs are exactly \(\max\{u,v\}\), \(\max\{u,1\}\), and \(\max\{1,v\}\). The combined-cost objective is affine in the shortcut flow \(x\) for fixed \(u,v\), so its minimum lies at \(x=0\) or \(x=\min\{u,v\}\). The first endpoint has the unique minimum \(2(1-B)\) at \(u=v=1\). The second is bounded below by \(-B^2/4\) or \(1-B\), both strictly above \(2(1-B)\) on the stated interval. The equilibrium and combined-cost calculations follow directly from the common used-path cost \(B\). The exact-rational script reproduces the representative value \(B=6/5\); it does not replace the all-parameter proof.

## Originality — PASS, with residual priority risk

The primary full text by Cole, Dodis, and Roughgarden explicitly states that the case of elastic traffic with nonlinear path norms and lower equilibrium traffic than optimal traffic is not analyzed. The exact parameterized benchmark here supplies a specific result in that gap, not a general bound. Gabriel and Bernstein's publisher abstract concerns equilibrium existence, uniqueness, and computation for nonadditive path costs; the full text was not inspected. Chau and Sim's abstract concerns elastic demand with symmetric cost maps; the accessible full-text attempt returned a 403 response, and the abstract does not establish coverage of the bottleneck path norm. A less-indexed prior example may still subsume the benchmark.

## Mathematical value — PASS

The flow reversal is economically meaningful: a Nash flow of size \(B<2\) coexists with a unique optimum of size \(2\), and the exact welfare ratio is \(3B/(B+2)\) on an open parameter interval. The result gives a reproducible benchmark for a case expressly left open in the primary source, while making no claim to settle the general class.

Self-review: passed. Independent audit: not yet performed.
