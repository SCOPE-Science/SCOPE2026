# Scientific review

## Correctness (C): PASS

The translation \(y_i=x_i+x_5\) cancels all lower-degree terms of \(e_3\) in characteristic two. Elimination of \(e_1\) gives the cubic \(F=(\sum z_i)^3+\sum z_i^3\); its gradients are squares of four independent linear forms \(w_i=\sum_{j\ne i}z_j\). This independently proves smoothness of the base surface, uniqueness and ordinary-triple type of the vertex, and the exact length-\(16\) Jacobian local algebra with Hilbert function \((1,4,6,4,1)\). Geometric planes all contain the vertex; the standard 27-line theorem bounds their number. The exact verifier enumerates all 35 and 357 candidate lines over \(\mathbb F_2\) and \(\mathbb F_4\), respectively, finds precisely 15 and 27, and checks that the extra twelve make six Frobenius pairs. First-order normal deformations of each cone plane are zero, by the normal sequence of a line on a smooth cubic surface. The verifier independently checks the corresponding nonzero normal determinants for all 27 planes. The odd-characteristic ten-node statement follows from the complete sign-pattern singularity classification and a nonzero Hessian determinant 16. No finite experiment substitutes for a geometric completeness argument.

## Originality (O): PASS, with priority risk

Dolgachev's Section 3 supplies a good characteristic-two Segre model with ten singular points and specifically cautions that the familiar symmetric expression is obtained only away from two. It does **not** classify the bad reduction of the distinct model \(V(e_1,e_3)\), its length-sixteen singular algebra, or its plane Fano scheme. Cheltsov–Tschinkel–Zhang work in characteristic zero. The classical 27 lines and fifteen-plus-twelve split on Clebsch's cubic are known and not individually claimed as new. Their appearance as the complete **reduced étale Fano scheme of planes on the dyadic symmetric Segre degeneration**, jointly with the nonflat singular scheme, was not found in the inspected primary sources or current research-record searches. A forgotten explicit calculation or an equivalent unpublished classification remains possible; publication-level priority is not certified.

## Mathematical value (V): PASS

This is not an arbitrary specialization: the symmetric equation is the familiar integral presentation of the Segre cubic and its ten-node/fifteen-plane geometry is central to birational and moduli constructions. At the bad prime, ten nodes merge into an ordinary triple point whose intrinsic singular-scheme length increases to sixteen, and the plane locus gains twelve geometric points while remaining finite étale. The exact arithmetic decomposition \(15\operatorname{Spec}(\mathbb F_2)\sqcup6\operatorname{Spec}(\mathbb F_4)\) explains which planes descend. These are natural scheme-structure and Fano-scheme boundary data for comparing integral models, not just a reduction of a known numeric invariant. The result does not classify other integral models or full stable reduction.

## Sources and limitations

Dolgachev, arXiv:2302.13101 (Section 3, characteristic-two comparison); Cheltsov–Tschinkel–Zhang, arXiv:2308.15271 (Sections 1, 2.4 and 6, characteristic-zero setup); Rowe, *Felix Klein's early contributions to anschauliche Geometrie* (Clebsch's classical 27 lines). Exact arithmetic is reproducible with the accompanying standard-library script. Independent external audit has not been undertaken. The characteristic-two cone is **not** the ten-node modular Segre model.

Self-review: passed. Independent audit: not yet performed.
