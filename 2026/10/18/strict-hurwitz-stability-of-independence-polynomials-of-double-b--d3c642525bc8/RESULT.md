# Strict Hurwitz stability of independence polynomials of double-broom trees

## Finding

**Theorem.** For any integers \(a,b\ge2\) and \(d\ge1\), form a double-broom tree \(B_{a,b,d}\) by joining two distinct vertices (the hubs) by an internally induced path of length \(d\) edges and attaching \(a\) new leaves to the first hub and \(b\) new leaves to the second hub. Write
\[
I(G,z)=\sum_{S\subseteq V(G),\ S\text{ independent}}z^{|S|}.
\]
Every zero of \(I(B_{a,b,d},z)\) has **strictly negative real part**.

More quantitatively, set \(t=1+z\), \(u=z/t^a\), \(v=z/t^b\), and define the path independence polynomials \(F_0(z)=1\), \(F_1(z)=1+z\), \(F_j(z)=F_{j-1}(z)+zF_{j-2}(z)\) for \(j\ge2\). Then for every \(\operatorname{Re}z\ge0\),
\[
\operatorname{Re}\frac{I(B_{a,b,d},z)}{t^{a+b}F_{d-2}(z)}>\frac1{12}\qquad(d\ge2),
\]
where \(F_{d-2}\) is nonzero there. In the adjacent-hub case \(d=1\), the corresponding normalized real part \(\operatorname{Re}(I/t^{a+b})\) exceeds \(1/3\). The constants are uniform over the displayed integer parameters and are not asserted to be sharp.

## Assumptions and scope

Graphs are finite, simple, undirected trees. The two hubs are distinct, each has at least two leaf neighbors, and their joining path has no additional pendant edges. Thus the family has exactly two vertices of degree greater than two; its members with \(d\ge1\) are not spiders. The half-plane \(\operatorname{Re}z\ge0\) includes its imaginary boundary. Only roots of the independence polynomial are studied; no statement about arbitrary trees is made.

For a convenient boundary convention set \(F_{-1}=1\). This agrees with the terminal empty-path contribution when both hubs are selected and separated by exactly one internal vertex.

## Proof

**Step 1: exact independence polynomial.** Classify independent sets according to which hubs are selected. If neither is selected, all leaves are independently optional and the internal path contributes \(F_{d-1}\). If exactly one hub is selected, no leaf adjacent to that hub may be selected and its nearest internal vertex is forbidden; the other hub's leaves are optional. If both hubs are selected (possible only for \(d\ge2\)), both nearest internal vertices are forbidden. Consequently, for \(d\ge2\),
\[
I(B_{a,b,d},z)=t^{a+b}F_{d-1}(z)
  +z(t^a+t^b)F_{d-2}(z)+z^2F_{d-3}(z).
\]
For \(d=1\), the two hubs are adjacent and cannot both be selected, giving \(I(B_{a,b,1},z)=t^{a+b}+z(t^a+t^b)\).

**Step 2: a half-plane transfer inequality.** For \(m\ge1\) let \(R_m=F_{m-2}/F_{m-1}\). The initial value is \(R_1=1\), and the path recursion gives
\[
R_{m+1}=\frac1{1+zR_m}.
\]
We prove simultaneously that, for all \(\operatorname{Re}z\ge0\), the denominator polynomials are nonzero and
\[
|R_m|\le1,\quad \operatorname{Re}R_m>0,\quad
\operatorname{Re}(zR_m)\ge0.
\]
These hold at \(m=1\). Assuming them at \(m\), the real part of \(1+zR_m\) is at least one, so its reciprocal exists, has positive real part, and has modulus at most one. For \(z\ne0\),
\[
zR_{m+1}=\frac1{z^{-1}+R_m},
\]
whose denominator has positive real part, because \(\operatorname{Re}z^{-1}\ge0\) and \(\operatorname{Re}R_m>0\). Therefore \(\operatorname{Re}(zR_{m+1})>0\). At \(z=0\), it is zero. This inductively proves all assertions and the nonvanishing of each \(F_j\) in the closed right half-plane.

**Step 3: uniform leaf factors.** For \(\operatorname{Re}z\ge0\), one has \(|1+z|\ge1\) and \(|1+z|^2\ge2|z|\). Consequently \(|z/(1+z)^s|\le1/2\) for every integer \(s\ge2\).

We also have the stronger real-part bound
\[
\operatorname{Re}\frac{z}{(1+z)^s}>-\frac13\qquad(s\ge2).
\]
For \(s=2\), put \(w=(1+z)^{-1}\); then \(|w-1/2|\le1/2\) and \(z/(1+z)^2=w(1-w)\). Thus \(\operatorname{Re}(w-w^2)=(\operatorname{Re}w)(1-\operatorname{Re}w)+(\operatorname{Im}w)^2\ge0\). For \(s=3\), the function is holomorphic on the closed right half-plane and vanishes at infinity there. Its boundary real part, at \(z=iy\), is
\[
\frac{y^2(3-y^2)}{(1+y^2)^3}
\ge-\frac{y^4}{(1+y^2)^3}\ge-\frac4{27}>-\frac13.
\]
The elementary maximum/minimum principle extends this lower bound from the boundary to the half-plane. For \(s\ge4\), the maximum-modulus principle applied to \(z/(1+z)^4\), which vanishes at infinity, and the inequality \(|1+z|\ge1\), give
\[
\left|\frac{z}{(1+z)^s}\right|
\le\sup_{y\in\mathbb R}\frac{|y|}{(1+y^2)^2}
=\frac{3\sqrt3}{16}<\frac13.
\]
This proves the desired bound in every case.

**Step 4: positive real certificate.** For \(d\ge2\), divide the Step 1 formula by \(t^{a+b}F_{d-2}\). The path recursion yields
\[
\frac{I(B_{a,b,d},z)}{t^{a+b}F_{d-2}(z)}
=1+u+v+(z+uv)R_{d-1}(z).
\]
By Steps 2–3,
\[
\operatorname{Re}\bigl[1+u+v+(z+uv)R_{d-1}\bigr]
>1-\frac13-\frac13-\frac14=\frac1{12}.
\]
The term \(zR_{d-1}\) has nonnegative real part, and \(|uvR_{d-1}|\le1/4\). The denominator is nonzero on the entire closed right half-plane, so the independence polynomial is zero-free there. For \(d=1\), Step 1 gives \(I/t^{a+b}=1+u+v\), whose real part is strictly greater than \(1/3\). Thus every root lies in the open left half-plane for all allowed parameters. \(\square\)

## Verification

The standalone script `verify.py` constructs each double-broom graph explicitly and enumerates all independent vertex subsets, independently assembles the coefficient formula above, and checks equality coefficient by coefficient for all 96 parameter triples \(2\le a,b\le5\), \(1\le d\le6\). It also applies an exact rational Routh–Hurwitz sign computation to the resulting polynomials in all 96 cases; the largest graph enumerated has 17 vertices. The checks require only Python's standard library and run with `python3 verify.py`.

The finite tests check the formula and root stability on bounded instances; they do not prove either statement for unbounded parameter ranges. The universal proof is the four-step analytic argument above.

## Relationship to prior work

Brown and Cameron (2018) introduced systematic independence-polynomial half-plane stability results and explicitly asked for a characterization of stable trees; their stable-graph constructions and independence-number-at-most-three theorem do not imply the present two-branch, unbounded-size classification. Zhang and Tu (2026) proved that every spider, a tree with at most one vertex of degree exceeding two, has independence roots in the open left half-plane. The double-brooms here have **two** such vertices, separated by any distance, and independently unbounded leaf counts. This is not a graph-isomorphism specialization of spiders.

The generating-polynomial recursion for independent sets on paths is classical and is not presented as new. The contribution is the uniform right-half-plane positivity certificate for an independently varying two-hub family. A literature comparison found no prior theorem from which this exact all-parameter assertion follows; that negative search result is not proof of absolute novelty.

## Limitations

The theorem does not cover trees with a third branching vertex, degree-two side branches, or endpoints with fewer than two attached leaves. It does not classify all stable trees, optimize the constant \(1/12\), or give exact root locations. The original 2026 spider preprint was available for bibliographic and abstract inspection, but its full PDF was not accessible in this review; an unobserved theorem or equivalent formulation in that manuscript remains a residual bibliographic uncertainty. The original 2018 article was inspected in full-text PDF form, including its construction and stability sections. Independent external validation has not been performed.

## References

1. Lei Zhang and Jianhua Tu, *Stability of independence polynomials of spiders*, arXiv:2609.04694v1, first available 2026-09-04. https://arxiv.org/abs/2609.04694
2. Jason I. Brown and Ben Cameron, *On the Stability of Independence Polynomials*, Electronic Journal of Combinatorics 25(1) (2018), #P1.46, DOI 10.37236/7280. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i1p46
3. Guo Chen, Bo Ning and Jianhua Tu, *The stability of independence polynomials of complete bipartite graphs*, arXiv:2505.24381 (2025). https://arxiv.org/abs/2505.24381
