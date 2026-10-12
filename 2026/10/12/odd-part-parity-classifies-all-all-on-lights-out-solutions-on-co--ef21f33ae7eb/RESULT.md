# Odd-part parity classifies all all-on Lights Out solutions on complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\ge1\) nonempty parts \(P_1,\ldots,P_r\), where \(n_i=|P_i|\ge1\), and put \(N=\sum_i n_i\). In the binary *closed-neighborhood Lights Out game*, all vertices are initially on; pressing a vertex once toggles that vertex and all its neighbors. An all-on solution is a subset \(S\subseteq V(G)\) whose vertices, each pressed once, turn every light off. Write \(\mathcal H_G(z)=\sum_{S\text{ solution}}z^{|S|}\).

Let \(O=\{i:n_i\text{ is odd}\}\) and \(o=|O|\). **Every solution has exactly one of the following shapes:**

* If \(o=0\), the unique solution is \(S=V(G)\).
* If \(o\ge1\), the solutions are precisely the unions \(\bigcup_{i\in J}P_i\), where \(J\subseteq O\) has odd cardinality. No vertices from an even-sized part are pressed.

Consequently, for every positive part-size profile,
\[
\boxed{\mathcal H_G(z)=\begin{cases}
z^N,&o=0,\\
\displaystyle\frac{\prod_{i\in O}(1+z^{n_i})-\prod_{i\in O}(1-z^{n_i})}{2},&o\ge1.
\end{cases}}
\]
For \(o\ge1\) there are \(2^{o-1}\) solutions; the minimum number of presses is \(\min_{i\in O}n_i\), with exactly \(|\{i\in O:n_i=\min_{j\in O}n_j\}|\) minimum solutions. For \(o=0\) the minimum is \(N\) and its solution is unique.

The closed-neighborhood matrix \(A(G)+I_N\), over \(\mathbb F_2\), has nullity \(\max\{o-1,0\}\). In particular, *every* starting state is solvable with a unique press vector if and only if \(o\le1\). In the extremality terminology of Codsi--Cristancho--Divoux--Sivashankar (2026), pressing **every** vertex is the unique all-on solution exactly when \(r=1\) or all \(n_i\) are even.

## Assumptions and scope

Graphs are finite, simple and undirected. The multipartition is into \(r\ge1\) nonempty independent sets with every edge present between distinct parts; no zero-size parts are permitted. The game uses the conventional two-state rule, with each vertex pressed either zero or one time, equivalently modulo two. The all-on solution polynomial counts *press subsets*, not distinct orders of pressing. The classification includes complete graphs, edgeless graphs, stars, and all unbalanced multipartite graphs, with no bound on \(r\) or the \(n_i\).

## Proof

Let \(x_v\in\mathbb F_2\) indicate whether vertex \(v\) is pressed. The all-on configuration is cleared if and only if, for each \(v\in P_i\),
\[
x_v+\sum_{j\ne i}\sum_{w\in P_j}x_w=1\quad\text{in }\mathbb F_2.
\]
The summation term does not depend on the chosen vertex inside \(P_i\). Subtracting the equations for any two vertices of the same part shows that their press indicators coincide. Thus \(x_v=y_i\) for all \(v\in P_i\), where \(y_i\in\mathbb F_2\). This argument also applies to singleton parts, where the assertion is automatic.

Put \(\epsilon_i=n_i\bmod2\) and \(t=\sum_{j=1}^r\epsilon_j y_j\in\mathbb F_2\). The vertex equation is now exactly
\[
y_i+\sum_{j\ne i}\epsilon_jy_j=(1+\epsilon_i)y_i+t=1.
\]
If all \(\epsilon_i=0\), then \(t=0\), so every \(y_i=1\), giving the single full-vertex solution. If at least one \(\epsilon_i=1\), its equation forces \(t=1\). Every even part then has \(y_i=0\), while every odd part has a free indicator constrained only by \(\sum_{i\in O}y_i=1\) in \(\mathbb F_2\). This is precisely an odd-cardinality selection of odd-sized parts. The polynomial is the standard even/odd subset parity projection, with its division by two interpreted over the integers, not in \(\mathbb F_2\). Counting selections proves the number, minimum size, and minimum-solution multiplicity. A positive sum of three or more positive odd part sizes exceeds any single selected odd part, so minima are exactly singleton choices among the smallest odd parts.

For nullity, replace the right side of the vertex equations by zero. Again every kernel vector is constant on each part, and \((1+\epsilon_i)y_i+t=0\). When \(o=0\), all \(y_i=t=0\); when \(o\ge1\), the equations of odd parts give \(t=0\), those of even parts give \(y_i=0\), and the \(o\) odd-part indicators satisfy one independent parity-zero equation. Hence the kernel has dimension \(o-1\). Invertibility is equivalent to \(o\le1\), and therefore equivalent to unique solvability for every initial state.

Finally, if \(r=1\), the graph has no edges and pressing all its vertices is the only all-on solution. For \(r\ge2\), if \(o=0\), the only solution is the whole vertex set. If \(o\ge1\), every solution omits each even-sized part and any admissible odd-part subset of odd cardinality; the whole vertex set is never uniquely selected. In the case all parts are odd and \(r\) is odd, the whole set is one solution among \(2^{r-1}\), which is at least four for \(r\ge3\). This proves the extremal classification.

## Verification

The included executable `verify_lights_out.py` constructs closed-neighborhood toggle masks directly and uses an independent Gray-code traversal to enumerate **every press subset**. For all \(363\) ordered profiles with \(1\le r\le5\) and \(1\le n_i\le3\), it compared the observed full size distribution with the proposed polynomial and independently computed binary matrix rank. It tested \(579194\) press subsets on graphs of orders at most \(15\), with no discrepancies. Run `python3 verify_lights_out.py`; the expected output is included as `verification_output.txt`.

The exhaustive finite checks are illustrative checks, **not** a proof for unbounded \(r\) or \(n_i\); the preceding algebra proves those assertions.

## Relationship to prior work

Codsi, Cristancho, Divoux and Sivashankar (2026) classify extremal Lights Out graphs by even degrees and the parity of their total number of matchings, and describe general linear-algebraic characterizations. Their paper does not give a complete multipartite all-solution size distribution. Ballard, Budge and Stephenson (2019, Section 3) compute closed-neighborhood nullity for **complete bipartite** graphs over cyclic rings and give related constructions; the present theorem extends the binary full-solution classification to arbitrary numbers of parts and counts the sizes of *all* clearing sets, not only the kernel dimension. Berman, Borer and Hungerbühler (2021) develop the general kernel/Fredholm framework and complexity of minimum-press solutions, but do not give the formula above for multipartite graphs. General facts that every all-on instance is solvable and that solutions form an affine kernel coset are prior art and are not asserted as new.

## Limitations

The result concerns the conventional two-state closed-neighborhood toggling game on complete multipartite graphs, not other graph classes or modular games with more than two states. Its weight enumerator applies to the all-on initial state, not an arbitrary initial binary state (although the nullity/universal-solvability statement does apply to arbitrary states). No claim of independently audited originality or proof certification is made. Equivalent results under the terminology *odd neighborhood domination*, *parity domination*, or *inverting sets* could exist in sources not identified by the literature comparison.

## References

1. J. Codsi, S. Cristancho, A. Divoux, V. Sivashankar, *Extremal Graphs for the Lights Out Problem*, arXiv:2602.07241v1, first posted 2026-02-06. https://arxiv.org/abs/2602.07241
2. L. E. Ballard, E. L. Budge, D. R. Stephenson, *Lights Out for graphs related to one another by constructions*, Involve 12 (2019), 181--201, especially Section 3. https://doi.org/10.2140/involve.2019.12.181
3. A. Berman, F. Borer, N. Hungerbühler, *Lights Out on graphs*, Mathematische Semesterberichte 68 (2021), 237--255. https://doi.org/10.1007/s00591-021-00297-5
4. S. Edwards, V. Elandt, N. James, K. Johnson, Z. Mitchell, D. Stephenson, *Lights Out on finite graphs*, Involve 3 (2010), 17--32. https://doi.org/10.2140/involve.2010.3.17
