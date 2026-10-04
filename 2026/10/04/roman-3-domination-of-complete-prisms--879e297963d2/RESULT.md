# Roman \(\{3\}\)-domination of complete prisms
## Finding
For every integer \(n\ge4\), let \(G_n=K_n\square K_2\), with clique layers \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the matching edge. Then \(\gamma_{\{R3\}}(G_4)=5\) and \(\gamma_{\{R3\}}(G_n)=6\) for every \(n\ge5\). For \(n=4\), the eight minimum functions are, up to swapping layers, exactly those with one layer labeled by a single \(2\) and three \(0\)'s, and the opposite layer labeled \(0\) at the matched coordinate and \(1\) at the other three coordinates. For \(n=5\), the minimum functions are the \(35^2\) functions whose two layer sums are both \(3\), together with ten exceptional functions of the same single-\(2\)/complementary-\(1\) form, so there are \(1235\) minima. For every \(n\ge6\), a function is minimum if and only if the labels in each clique layer sum to \(3\); consequently the number of minimum Roman \(\{3\}\)-dominating functions is \[\binom{n+2}{3}^2.\]

## Assumptions and scope
All graphs are finite and simple. For \(n\ge4\), write
\[
G_n=K_n\square K_2.
\]
Its two \(K_n\)-layers are
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
with matching edges \(a_i b_i\).

A Roman \(\{3\}\)-dominating function is a map
\[
f:V(G_n)\to\{0,1,2,3\}
\]
such that a vertex labeled \(0\) has neighbor-label sum at least \(3\), and a vertex labeled \(1\) has neighbor-label sum at least \(2\).

Put
\[
\alpha=\sum_{i=1}^n f(a_i),\qquad
\beta=\sum_{i=1}^n f(b_i).
\]

## Proof
For each \(i\), the neighbors of \(a_i\) are all other vertices in \(A\) together with \(b_i\). Hence, if \(f(a_i)\in\{0,1\}\), its defining Roman \(\{3\}\) inequality is equivalent to
\[
\alpha+f(b_i)\ge3.
\]
Similarly, if \(f(b_i)\in\{0,1\}\), then
\[
\beta+f(a_i)\ge3.
\]
These two layer-sum inequalities are an exact characterization of feasibility.

We first prove the lower bounds. Suppose a feasible function has weight at most \(5\). After swapping the two layers if necessary, assume \(\alpha\le2\).

If \(\alpha=0\), then every \(a_i\) has label at most \(1\), so every \(b_i\ge3\), which is impossible at weight at most \(5\). If \(\alpha=1\), then every \(b_i\ge2\), again impossible for \(n\ge4\). If \(\alpha=2\), then at most one \(a_i\) can have label at least \(2\); therefore at least \(n-1\) coordinates satisfy \(f(a_i)\le1\), and each corresponding \(b_i\ge1\). Thus
\[
\beta\ge n-1.
\]
For \(n\ge5\), this gives total weight at least \(2+(n-1)\ge6\). Hence
\[
\gamma_{\{R3\}}(G_n)\ge6\qquad(n\ge5).
\]
For \(n=4\), the same argument rules out weight at most \(4\), so
\[
\gamma_{\{R3\}}(G_4)\ge5.
\]

These bounds are attained. For \(n=4\), label one \(a_i\) by \(2\), label its mate \(b_i\) by \(0\), label the other three vertices of \(B\) by \(1\), and label the remaining vertices of \(A\) by \(0\). This has weight \(5\). For every \(n\ge5\), any assignment with
\[
\alpha=\beta=3
\]
is feasible, because both defining layer-sum inequalities are then automatic. Thus
\[
\gamma_{\{R3\}}(G_4)=5,\qquad
\gamma_{\{R3\}}(G_n)=6\quad(n\ge5).
\]

Now classify the minima.

For \(n=4\), a weight-\(5\) minimum has, up to swapping layers, \(\alpha=2\) and \(\beta=3\). The preceding lower-bound argument is tight only if exactly one \(a_i\) is labeled \(2\), every other \(a_j\) is labeled \(0\), \(b_i=0\), and every \(b_j\) with \(j\ne i\) is labeled \(1\). There are \(4\) such choices in each orientation, hence \(8\) minima.

For \(n=5\), let a minimum have weight \(6\), and assume \(\alpha\le\beta\). Then \(\alpha\le3\). Values \(\alpha=0,1\) are impossible. If \(\alpha=2\), tightness forces one \(a_i=2\), all other \(a_j=0\), \(b_i=0\), and the other four \(b_j=1\). This gives \(5\) functions, plus \(5\) after swapping layers. The remaining possibility is
\[
\alpha=\beta=3,
\]
and every such pair of layer labelings is feasible. A nonnegative \(n\)-tuple with sum \(3\) automatically has all entries at most \(3\), so for \(n=5\) there are
\[
\binom{7}{3}
\]
choices per layer. Therefore the total is
\[
\binom{7}{3}^2+10=1235.
\]

Finally let \(n\ge6\). If a weight-\(6\) minimum had, say, \(\alpha\le2\), then the same argument would give
\[
\beta\ge n-1\ge5,
\]
contradicting \(\alpha+\beta=6\). Hence \(\alpha,\beta\ge3\), and since their sum is \(6\),
\[
\alpha=\beta=3.
\]
Conversely every pair of layer labelings with these two sums is feasible. The number of nonnegative \(n\)-tuples summing to \(3\) is
\[
\binom{n+2}{3},
\]
so the number of minimum functions is
\[
\binom{n+2}{3}^2.
\]

## Verification
The included verifier constructs \(K_n\square K_2\) directly. For \(n=4,5\), it checks all \(4^{2n}\) labelings against the defining Roman \(\{3\}\) conditions, identifies the true minimum, and compares every minimum function with the structural classification above.

A second exact dynamic program works only with the two layer sums and the exact local feasibility inequalities. It independently verifies the minimum value and minimum-function count for every \(4\le n\le60\).

## Relationship to prior work
The 2020 paper “Bounds on the double Italian domination number of a graph” develops general lower and upper bounds for Roman \(\{3\}\)-domination. Its full text defines the same invariant and derives degree-based inequalities, but targeted searches of the inspected text found no Cartesian-product, prism, or \(K_n\square K_2\) formula.

The 2023 paper “Graphs with small or large Roman \(\{3\}\)-domination number” characterizes graphs whose Roman \(\{3\}\)-domination number is \(3\), one below the order, or equal to the order, and proves additional tree results. Its inspected full text contains no Cartesian-product or prism treatment. The complete-prism values above are not consequences of those extremal classifications for \(n\ge4\), and the minimum-function enumeration is a strictly finer statement than the domination number alone.

## Limitations
The theorem concerns the Cartesian product \(K_n\square K_2\) for \(n\ge4\). The small cases \(n=2,3\) are excluded because they belong to separate extremal regimes and have different minimum weights. No claim is made for \(K_n\square K_m\) with \(m\ge3\), for connected double Italian domination, or for other Roman variants. Literature search cannot exclude a differently phrased or non-indexed formula.

## References
1. F. Azvin, N. Jafari Rad, “Bounds on the double Italian domination number of a graph,” Discussiones Mathematicae Graph Theory 42(4) (2022), 1129–1137, DOI 10.7151/dmgt.2330; available online 25 May 2020.
2. N. Ebrahimi, H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, “Graphs with small or large Roman \(\{3\}\)-domination number,” RAIRO Operations Research 57(3) (2023), 1195–1208, DOI 10.1051/ro/2023058; published online 18 May 2023.
