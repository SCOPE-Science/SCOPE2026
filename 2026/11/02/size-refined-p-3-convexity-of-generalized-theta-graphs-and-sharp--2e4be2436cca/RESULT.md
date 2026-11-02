# Size-refined \(P_3\)-convexity of generalized theta graphs and sharp cardinality gaps

## Finding
Let \(r\ge 3\) and let \(\ell_1,\ldots,\ell_r\ge 2\) be integers. The generalized theta graph \(\Theta(\ell_1,\ldots,\ell_r)\) has two distinct terminals \(s,t\) joined by \(r\) internally vertex-disjoint paths, the \(i\)-th having \(\ell_i\) edges. A vertex subset \(S\) is **\(P_3\)-convex** if every vertex outside \(S\) has at most one neighbor inside \(S\). Define its size-enumerator by
\[
C_G(z)=\sum_{\substack{S\subseteq V(G)\\ S\text{ is }P_3\text{-convex}}}z^{|S|}.
\]
We give an exact finite-transfer product for \(C_G(z)\) at **every** tuple of path lengths. For the natural equal-length-three family \(G_r=\Theta(3,\ldots,3)\), its full polynomial has the closed form
\[
\boxed{C_{G_r}(z)=(1+rz)^2+2z\bigl((1+z)^r+rz^2(1+z)^{r-1}\bigr)+z^2(1+z^2)^r.}
\]
In particular, the total number of convex sets is
\[
\boxed{C_{G_r}(1)=(r+1)^2+(r+3)2^r.}
\]
The nonzero coefficient degrees are **exactly**
\[
\boxed{\{0,1,\ldots,r+2\}\ \cup\ \{j: r+2<j\le 2r+2,\ j\equiv0\pmod2\}.}
\]
Thus every odd cardinality strictly between \(r+2\) and \(2r+2\) is impossible, whereas all other cardinalities occur. The unique largest convex set is the entire vertex set of size \(2r+2\). The largest *proper* convex sets have size \(2r\), and there are exactly \(r\) of them: the complements of the two interior vertices of any one of the \(r\) terminal-to-terminal paths.

## Assumptions and scope
All graphs are finite, simple, undirected, and have distinctly identified vertices (sets are not taken modulo graph automorphisms). Throughout, \(r\ge3\), every \(\ell_i\ge2\), and the two common terminals are not adjacent. The count includes both \(\varnothing\) and \(V(G)\). The ordinary \(P_3\)-convexity used here involves **all three-vertex paths**, not just induced paths or geodesics.

For an integer \(L\ge1\), terminal indicators \(a,b\in\{0,1\}\), and interior indicators \(x_1,\ldots,x_L\in\{0,1\}\), set \(x_0=a\), \(x_{L+1}=b\) and define
\[
H_{ab}^{(L)}(p,q;z)=\sum_{x_1,\ldots,x_L\in\{0,1\}}
 z^{\sum_{j=1}^L x_j}p^{x_1}q^{x_L}
 \prod_{j=1}^{L}\mathbf 1\bigl((x_{j-1},x_j,x_{j+1})\ne(1,0,1)\bigr).
\]
For a polynomial \(F(p)\) write \(\mathcal L_0^p F=[p^0]F+[p^1]F\) and \(\mathcal L_1^p F=F(1)\). Define the same functionals in \(q\). All expressions are formal polynomials with integer coefficients.

**Exact arbitrary-length formula.** With \(L_i=\ell_i-1\),
\[
\boxed{
C_{\Theta(\ell_1,\ldots,\ell_r)}(z)=
\sum_{a,b\in\{0,1\}}z^{a+b}
\bigl(\mathcal L_a^p\mathcal L_b^q\bigr)
\prod_{i=1}^r H_{ab}^{(L_i)}(p,q;z).}
\]
The first and last interior indicators coincide when \(L_i=1\); the definition then correctly contributes \(p^{x_1}q^{x_1}\). The four-state recurrence described below computes each path factor without enumerating its internal binary strings.

## Proof
**1. The local rule.** If a vertex \(v\) is outside a candidate set, having two selected neighbors is equivalent to the presence of a three-vertex path whose endpoints are selected and whose center is not. Therefore a set is \(P_3\)-convex if and only if no vertex outside the set has more than one selected neighbor.

Fix the terminal membership indicators \(a=\mathbf 1_{s\in S}\) and \(b=\mathbf 1_{t\in S}\). On path \(i\), write its \(L_i\) internal membership indicators in order as \(x_{i,1},\ldots,x_{i,L_i}\). Every internal vertex has exactly two neighbors, its immediate predecessor and successor. The local rule is precisely that no triple of consecutive indicators equals \((1,0,1)\). Thus \(H_{ab}^{(L_i)}\) counts exactly the admissible internal memberships, weighted by selected vertices and recording the first and last interior membership using \(p,q\).

Different paths meet only at \(s,t\). If \(s\) is selected (\(a=1\)), no further condition is imposed at \(s\); otherwise at most one of the \(r\) first internal vertices may be selected, which is exactly the operator \(\mathcal L_0^p\). The same argument at \(t\) gives \(\mathcal L_b^q\). Hence the product and four terminal cases count each convex set once, proving the arbitrary-length formula.

For an efficient finite-state implementation, generate the sequence of internal indicators from left to right, remembering the preceding two bits. When appending a new bit, reject precisely the transition \((1,0)\to(0,1)\) (the resulting triple \((1,0,1)\)). On termination, check the final triple involving the right terminal. The state also carries the first internal bit and the accumulated power of \(z\). This constructs \(H_{ab}^{(L)}\) by a constant-width transfer, and the terminal capacity filters also have constant width for every fixed numerical value of \(z\).

**2. Exact closed form at length three.** Now every path is \(s-u_i-v_i-t\). Partition by the two terminal indicators.

If neither terminal is selected, no local condition restricts \((u_i,v_i)\), but at most one \(u_i\) and at most one \(v_i\) may be selected. These two independent choices contribute \((1+rz)^2\).

If \(s\) is selected and \(t\) is not, the only forbidden internal pair along any path is \((u_i,v_i)=(0,1)\). Moreover, at most one \(v_i\) may be selected. If all \(v_i\)'s are zero, each \(u_i\) is independently free, yielding \((1+z)^r\). If exactly one \(v_i\) is selected, its \(u_i\) must also be selected; this yields \(rz^2(1+z)^{r-1}\). Including \(s\) contributes an additional factor \(z\). The case with only \(t\) selected is symmetric. Their combined contribution is \(2z((1+z)^r+rz^2(1+z)^{r-1})\).

If both terminals are selected, the pairs \((0,1)\) and \((1,0)\) are forbidden on each path. Therefore each \((u_i,v_i)\) is either \((0,0)\) or \((1,1)\), independently of the other paths. The contribution is \(z^2(1+z^2)^r\). Adding the four cases proves the closed polynomial.

**3. Support and rigidity at the top.** The first summand has degrees \(0,1,2\); the middle two summands have strictly positive coefficients at every degree \(1,\ldots,r+2\); the last summand has positive coefficients exactly at even degrees \(2,4,\ldots,2r+2\). No cancellation is possible. This establishes the exact coefficient support and the odd-cardinality gaps.

Since \(r\ge3\), the highest degree below \(2r+2\) is \(2r\), and only the final summand contributes there. Its coefficient is \(\binom r{r-1}=r\). More concretely, achieving this degree requires choosing both terminals and exactly \(r-1\) of the \(r\) internal pairs; the omitted pair may lie on any one path. These are all the maximum proper convex sets. The coefficient of \(z^{2r+2}\) equals one, for the full vertex set. Substituting \(z=1\) yields \((r+1)^2+(r+3)2^r\).

## Verification
Run `python3 verify.py` using the accompanying standalone Python 3 program (standard library only). The verifier constructs each graph explicitly and enumerates **all** vertex subsets, testing the original closed-neighborhood rule directly. It independently implements the four-state path transfer, compares all polynomial coefficients on twelve mixed-length theta graphs, and compares the full closed form for six equal-length-three graphs with \(3\le r\le8\). It also checks their coefficient support, total counts, missing penultimate degree, and maximum proper-set multiplicities. The replay ended in `VERIFY_OK`.

For \(r=3,4,5,6,7,8\), the verified total counts are respectively \(64,137,292,625,1344,2897\). Direct exhaustive computations are finite corroboration; the conclusions for arbitrary \(r\) and path lengths follow from the proof above.

## Relationship to prior work
Dourado, Grippo, Lin, and Protti (2026) introduced the explicit counting problem for \(P_3\)-convex sets, established its general counting complexity, and supplied linear-time algorithms for trees and threshold graphs as well as general exponential-time methods. Their inspected manuscript treats neither the arbitrary-path theta product nor the equal-length-three polynomial and its forbidden-cardinality spectrum. General counting algorithms can evaluate particular graphs but do not provide the structural formulas proved here.

Centeno, Penso, Rautenbach, and Pereira de Sá (2013) analyze geodetic and hull numbers for \(P_3\)-convexity, different extremal parameters. The exact enumeration above is not implied by their hull/geodetic comparison. Searches for equivalent two-neighbor closure formulations, generalized theta graphs, and exact numerical sequences did not locate a directly covering published formula. This is a qualified priority assessment, not a proof that no equivalent result exists.

## Limitations
The exact transfer formula applies only to two-terminal internally disjoint paths with lengths at least two; the explicit binomial closed form and coefficient gaps are proved only when every path has length three. No formula for arbitrary series-parallel networks, graphs with further chords, or convexity defined using induced/geodetic paths is claimed. The verification program checks finite instances and does not constitute an independent audit. Exhaustive historical priority checking, especially under alternate closure-system terminology, remains open.

## References
1. M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1, publicly posted 2026-03-05. https://arxiv.org/html/2603.04706v1
2. C. C. Centeno, L. D. Penso, D. Rautenbach, and V. G. Pereira de Sá, *Geodetic Number versus Hull Number in \(P_3\)-Convexity*, SIAM Journal on Discrete Mathematics 27 (2013), 717–731. https://doi.org/10.1137/110859014
3. *The Carathéodory number of the \(P_3\) convexity of chordal graphs*, Discrete Applied Mathematics 172 (2014), 104–108. https://doi.org/10.1016/j.dam.2014.03.004
