# An infinite counterfamily to the proposed second-largest \(Z_1\) tripod

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

For a graph \(G\), let \(Z_1(G)\) denote the number of edge subsets containing exactly one pair of adjacent edges. Following Andriantiana--Shozi, write
\[
[P_a,P_b,P_c]
\]
for the tripod whose three branches at its unique degree-three vertex have lengths \(a,b,c\). It has \(a+b+c+1\) vertices.

Conjecture 1 of Andriantiana--Shozi, arXiv:2405.17154v1, proposes that for every forest \(F\ne P_n\) of order \(n\ge 12\),
\[
Z_1(F)\le Z_1([P_3,P_3,P_{n-7}]),
\]
with equality only for the displayed tripod.

This conjecture is false for every \(n\ge 21\). More precisely,
\[
\boxed{
Z_1([P_2,P_2,P_{n-5}])
-
Z_1([P_3,P_3,P_{n-7}])
=
2(n-8)F_{n-6}-3(n-7)F_{n-7}>0
}
\]
for every \(n\ge21\), where \(F_0=0,F_1=1\) are the Fibonacci numbers.

At the first counterexample order,
\[
Z_1([P_2,P_2,P_{16}])=55273,
\qquad
Z_1([P_3,P_3,P_{14}])=55247.
\]
Thus the conjectured extremal value is exceeded by 26 already at \(n=21\).

## Tripod counting formula

Let \(q_t=\sigma_1(P_t)\), where \(\sigma_1(H)\) counts vertex subsets of \(H\) inducing exactly one edge. The line-graph identity
\[
Z_1(G)=\sigma_1(L(G))
\]
is recorded in the source paper. For a path,
\[
q_t=\frac{2tF_{t+1}-(t+1)F_t}{5}\qquad (t\ge1),
\]
with \(q_0=0\); this is the source paper's explicit path formula written in Fibonacci form.

The line graph of \([P_a,P_b,P_c]\) is a triangle whose three vertices carry path tails. On an arm of length \(s\), classify a selected vertex subset according to whether the triangle vertex on that arm is selected and whether the arm itself contains the unique induced edge. The four counts are
\[
F_{s+1},\qquad F_s,\qquad q_{s-1},\qquad q_s-q_{s-1},
\]
respectively for: independent/not selected at the triangle, independent/selected at the triangle, one-edge/not selected at the triangle, and one-edge/selected at the triangle.

Combining the three arms, with the unique induced edge either inside one arm or between exactly two selected triangle vertices, gives
\[
\begin{aligned}
Z_1([P_a,P_b,P_c])={}&
\sum_{\rm cyc}
\Bigl(
q_aF_{b+1}F_{c+1}
+q_{a-1}(F_bF_{c+1}+F_{b+1}F_c)
\Bigr)\\
&+F_aF_bF_{c+1}+F_aF_{b+1}F_c+F_{a+1}F_bF_c.
\end{aligned}
\tag{1}
\]

Two specializations of (1) are
\[
Z_1([P_2,P_2,P_c])
=4q_c+4q_{c-1}+5F_{c+1}+4F_c,
\tag{2}
\]
and
\[
Z_1([P_3,P_3,P_c])
=9q_c+12q_{c-1}+20F_{c+1}+18F_c.
\tag{3}
\]

## Proof of the counterfamily

Put \(d=n-7\). The two competing trees of order \(n\) are
\[
[P_2,P_2,P_{d+2}]
\quad\text{and}\quad
[P_3,P_3,P_d].
\]
Substituting the path formula for \(q_t\) into (2)--(3), and using the Fibonacci recurrence, gives
\[
\begin{aligned}
&Z_1([P_2,P_2,P_{d+2}])-Z_1([P_3,P_3,P_d])\\
&\hspace{3cm}=2(d-1)F_{d+1}-3dF_d.
\end{aligned}
\tag{4}
\]
For \(d=14\) and \(d=15\), the right side of (4) is respectively 26 and 186.

For every \(d\ge16\), the elementary identity
\[
5F_{d+1}-8F_d=F_{d-5}>0
\]
implies \(F_{d+1}/F_d>8/5\). Hence
\[
2(d-1)F_{d+1}-3dF_d
>
\left(\frac{16(d-1)}5-3d\right)F_d
=
\frac{d-16}{5}F_d\ge0.
\]
The inequality is strict also at \(d=16\) because \(F_{d+1}/F_d>8/5\). Therefore (4) is positive for every \(d\ge14\), equivalently for every \(n\ge21\).

Since \([P_2,P_2,P_{n-5}]\) is itself an \(n\)-vertex tree, it is an admissible forest in Conjecture 1 and disproves the proposed inequality for all \(n\ge21\).

## Verification

A direct enumeration of all \(2^{20}\) edge subsets of each of the two 21-vertex trees independently reproduces
\[
55273\quad\text{and}\quad55247.
\]
The accompanying script also verifies formula (1), the closed difference (4), and positivity through \(n=200\). As an additional finite check, it enumerates every unordered tripod parameter triple for \(12\le n\le200\); the largest tripod is \([P_3,P_3,P_{n-7}]\) for \(12\le n\le20\) and \([P_2,P_2,P_{n-5}]\) for \(21\le n\le200\). This finite scan is evidence only and is not used to prove a corrected all-\(n\) extremal theorem.

## Relation to prior work and originality

Andriantiana and Shozi define \(Z_1\), prove \(Z_1(G)=\sigma_1(L(G))\), derive the explicit path formula, and show that any tree attaining the second-largest \(Z_1\) at fixed order must be a tripod. Their Conjecture 1 is based on computations through order 20 and explicitly proposes \([P_3,P_3,P_{n-7}]\) for every \(n\ge12\).

Exact-phrase, family-name, arXiv/DOI, author, and later-literature searches did not locate a published correction or a prior counterexample to this conjecture. Later work located in the same authors' publication stream concerns vertex-subset versions or other nearly-independent parameters rather than this tripod conjecture. Accordingly, the counterfamily and its closed comparison are reported as original to the best of our knowledge.

## Limitations

This record disproves the stated conjecture and supplies an infinite counterfamily; it does **not** prove that \([P_2,P_2,P_{n-5}]\) is the true second-largest tree for every \(n\ge21\). The finite all-tripod scan through order 200 suggests that corrected statement, but a general extremal proof is not supplied here. No claim is made about variants of \(Z_k\) for \(k\ne1\).

## References

1. E. O. D. Andriantiana and Z. B. Shozi, *The number of 1-nearly independent edge subsets*, arXiv:2405.17154 (2024), especially Lemma 1, the path formulas in Section 2.3, Theorem 6, and Conjecture 1. Published version metadata: Iranian Journal of Mathematical Chemistry, DOI: 10.22052/IJMC.2024.254977.1871.
2. E. O. D. Andriantiana and Z. B. Shozi, *The number of 1-nearly independent vertex subsets*, Quaestiones Mathematicae 47 (2024), 2353--2373, DOI: 10.2989/16073606.2024.2367714.
