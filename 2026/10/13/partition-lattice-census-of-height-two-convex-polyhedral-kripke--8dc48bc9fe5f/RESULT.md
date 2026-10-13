# Partition-lattice census of height-two convex-polyhedral Kripke frames

## Finding
Let \(\mathrm{PL}_2\) be the intermediate logic of convex polyhedra of dimension at most \(2\). By the source theorem, this is also the logic of any single two-dimensional convex polyhedron. Consider finite rooted Kripke frames of **exact height two** satisfying \(\mathrm{PL}_2\). Fix \(t\ge 1\) labeled top points and \(e\ge 1\) labeled depth-one points, with a distinguished root below them all.

Such frames are exactly connected incidence systems in which every depth-one point chooses a nonempty \(1\)- or \(2\)-subset of the \(t\) top points. Equivalently, after deleting the root, the comparability graph is a connected bipartite graph whose depth-one side has degrees only \(1\) and \(2\).

Let \(N_{t,e}\) be the number of these level-labeled frames. Then
\[
\boxed{
N_{t,e}=\sum_{\pi\in\Pi_t}(-1)^{|\pi|-1}(|\pi|-1)!
\left(t+\sum_{B\in\pi}\binom{|B|}{2}\right)^e,
}
\]
where \(\Pi_t\) is the lattice of set partitions of the top-point set. The same numbers have the two-sort exponential generating function
\[
\boxed{
\sum_{t\ge1}\sum_{e\ge0}N_{t,e}\frac{x^t}{t!}\frac{y^e}{e!}
=
\log\!\left(\sum_{t\ge0}\exp\!\left(\binom{t+1}{2}y\right)\frac{x^t}{t!}\right),
}
\]
where the harmless term \(N_{1,0}=1\) is included for the connected-structure convention; exact-height-two frames have \(e\ge1\).

For example,
\[
N_{2,e}=3^e-2^e,
\]
and the first rows \((e=1,\ldots,7)\) are
\[
\begin{array}{c|rrrrrrr}
t&1&2&3&4&5&6&7\\\hline
1&1&1&1&1&1&1&1\\
2&1&5&19&65&211&665&2059\\
3&0&6&78&690&5190&35826&235158\\
4&0&0&96&2472&40800&552360&6705216\\
5&0&0&0&3000&131640&3566400&77322000
\end{array}
\]
(the columns are the depth-one counts \(e\)).

If instead the distinguished root is fixed and the remaining \(m\) points are globally labeled, the exact-height-two count is
\[
\boxed{R_m=\sum_{t=1}^{m-1}\binom mt N_{t,m-t}.}
\]
Thus
\[
(R_2,R_3,R_4,R_5,R_6,R_7,R_8)
=(2,6,34,255,2541,31948,482308).
\]

## Assumptions and scope
The source characterizes finite \(\mathrm{PL}_n\)-frames structurally: height at most \(n\); points of depth one have at most two strict successors; and the strict upset of every point of depth greater than one is connected. The result here specializes that theorem to rooted frames of exact height two and counts labeled frames. It does not count isomorphism classes, and it does not claim that the special sequence \(N_{2,e}=3^e-2^e\) is new; that one-row sequence is classical. The new claim is the explicit frame/incidence correspondence and all-\((t,e)\) census for the two-dimensional convex-polyhedral logic.

## Proof
Let \(F\) be a finite rooted frame of exact height two. Write \(T\) for its top points and \(E\) for its depth-one points. Every \(u\in E\) has at least one top point above it, and the source's depth-one condition gives
\[
1\le |\Uparrow u|\le2.
\]
Thus \(u\) determines either a singleton or an unordered pair of elements of \(T\). Conversely, any such choices, together with a root below all nonroot points, define a unique height-two rooted poset satisfying the depth-one condition.

The only remaining source condition is connectedness of the strict upset of the root, namely \(F\setminus\{\bot\}\). In height two its comparability graph is exactly the incidence graph between \(E\) and \(T\). A singleton choice merely attaches a leaf to one top point; a pair choice joins two top points through its depth-one point. Hence the incidence graph is connected exactly when the graph on \(T\) formed by the pair choices is connected (with the one-vertex case understood as connected). This proves the structural bijection.

To count, temporarily fix a set partition \(\pi\) of \(T\). The pair choices that never cross between blocks of \(\pi\) number
\[
\sum_{B\in\pi}\binom{|B|}{2},
\]
while all \(t\) singleton choices remain available. Therefore each labeled depth-one point has
\[
t+\sum_{B\in\pi}\binom{|B|}{2}
\]
allowed neighborhoods if every connected component of the top graph must refine \(\pi\). Möbius inversion on the partition lattice extracts the one-block component partition. Since
\[
\mu(\pi,\hat1)=(-1)^{|\pi|-1}(|\pi|-1)!,
\]
the displayed formula for \(N_{t,e}\) follows.

For the generating function, an arbitrary incidence system decomposes uniquely as a set of connected components, each carrying its own top labels and depth-one labels. With \(t\) top labels, there are \(\binom{t+1}{2}=t+\binom t2\) possible neighborhoods for each depth-one label, so the two-sort EGF of all systems is
\[
A(x,y)=\sum_{t\ge0}\exp\!\left(\binom{t+1}{2}y\right)\frac{x^t}{t!}.
\]
The labeled exponential formula gives \(A=\exp C\), where \(C\) is the connected EGF, hence \(C=\log A\).

Finally, with \(m\) globally labeled nonroot points, choosing which \(t\) are top points contributes \(\binom mt\), and summing over \(1\le t\le m-1\) gives \(R_m\).

## Verification
A standalone exact replay performs two independent checks. First, it exhaustively generates every allowed neighborhood assignment for \(t\le4\) over a substantial range of \(e\), tests graph connectivity directly, and compares the counts with the partition-lattice formula. Second, it checks the independent connected-component recurrence equivalent to the bivariate exponential formula for \(t\le8\) and \(e\le10\). It also verifies the special row \(N_{2,e}=3^e-2^e\) and the stated values of \(R_m\).

The replay returns:

```text
VERIFY_OK 136 exact formula/recurrence assertions; exhaustive assignment grid through t=4
```

## Prior-art boundary
Adam-Day, Bezhanishvili, Gabelaia, and Marra supply the geometric completeness theorem and the structural characterization of finite \(\mathrm{PL}_n\)-frames. Their paper does not enumerate such frames and contains no occurrence of “enumerat”, “count”, “generating function”, “multigraph”, or “incidence” in the inspected full text. Targeted literature and semantic-index searches under the logic name, height-two frame description, connected-incidence formulation, and partition-lattice counting formulation did not locate the displayed census or generating function. Exact sequence search identifies the special \(t=2\) row as the classical sequence \(3^e-2^e\); that special case is therefore explicitly excluded from the originality claim. No equivalent result appears in the current or preceding owned foundations ledgers.

Residual risk remains that the all-\((t,e)\) count occurs in general labeled-graph enumeration under different terminology. Even in that event, the transfer of that census to finite \(\mathrm{PL}_2\)-frames would remain the logical synthesis established here.
