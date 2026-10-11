# Independent mathematical audit

## correctness

PASS

In a complete multipartite graph, a selected vertex in part \(i\) has exactly \(q-c_i\) neighbours outside \(D\), so certification is precisely the exclusion of value one. A set dominates exactly when it meets at least two parts or is one whole part, giving the ordinary domination polynomial used in the formula. Among dominating sets, every \(q=1\) set is a certification failure, contributing \(Nz^{N-1}\). For \(q\ge2\), the bad event for part \(i\) is: omit exactly one vertex outside \(V_i\) and a nonempty proper subset inside \(V_i\); pairwise intersections are possible only at \(q=2\), with one omitted vertex in each of two parts of size at least two, and triple intersections are impossible. Inclusion--exclusion therefore gives exactly the displayed correction terms. An independent brute-force enumeration over all 58 complete multipartite part profiles of total order at most 8 matched the closed formula coefficient-by-coefficient.

## originality

PASS

The foundational certified-domination literature defines and studies the minimum parameter, while the only directly relevant polynomial source located gives exact formulas for the special family \(K_{3,n}\). Searches for arbitrary complete multipartite certified-domination polynomials found no broader formula. The audited all-part-size criterion and inclusion--exclusion formula therefore strictly extend the inspected primary special case.

## value

PASS

The result gives an all-set polynomial for a canonical graph class and turns certification into a sharp part-occupancy rule. It strictly generalizes the existing \(K_{3,n}\) calculation and is directly reusable for coefficients, totals and specializations across arbitrary multipartite profiles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
