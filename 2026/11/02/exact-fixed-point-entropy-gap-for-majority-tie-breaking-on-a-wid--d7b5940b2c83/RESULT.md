# Exact fixed-point entropy gap for majority tie-breaking on a width-three torus

## Finding
For every integer \(n\ge3\), put \(G_n=C_3\square C_n\), the simple four-regular Cartesian-product graph on \(3n\) individually identified vertices. Let \(A_n\) be its number of fixed binary opinion assignments under synchronous neighbor-majority updating with incumbent-color tie retention (MM). Let \(B_n\) count its *singleton absorbing* assignments for the synchronous random-tie majority model (RMM): at each tied vertex either opinion is selected with positive probability.

There is an explicitly defined \(64\times64\) zero-one matrix \(T\) such that \(A_n=\operatorname{tr}(T^n)\), and its **exact characteristic polynomial** is
\[
\begin{aligned}
\chi_T(z)={}&z^{42}(z-3)(z-1)(z+1)\\
&\cdot(z^3+z+1)^2(z^3-z^2-1)\\
&\cdot(z^3-2z^2+z+1)^2(z^4+z^2-3z-3).
\end{aligned}
\]
In contrast, if \(\varphi=(1+\sqrt5)/2\) and \(\widehat\varphi=(1-\sqrt5)/2\), then
\[
B_n=\varphi^n+\widehat\varphi^{\,n}+2\cos(n\pi/3).
\]
The exact and unequal fixed-point growth rates are
\[
\boxed{A_n\sim3^n,\qquad B_n\sim\varphi^n,\qquad A_n/B_n\sim(3/\varphi)^n.}
\]
Thus both models have exponentially many singleton stable assignments on this three-row torus, despite the random-tie model having only two singleton absorbing assignments on the ordinary cycle. All counts are for labeled vertices, without quotienting by rotations, reflections or color exchange. The entropy per vertex is \(\log(3)/3\) for MM and \(\log(\varphi)/3\) for RMM.

## Assumptions and scope
The three vertices of \(C_3\) form a triangle, and the \(n\) vertices of \(C_n\), \(n\ge3\), form an ordinary simple cycle; each \((r,j)\) has exactly four distinct neighbors \((r+1,j)\), \((r+2,j)\) (row indices modulo three), \((r,j-1)\), and \((r,j+1)\) (column indices modulo \(n\)). Both update rules use the **four neighbors**, excluding the vertex's own vote. MM retains its own opinion exactly in a two-versus-two tie. In RMM each tied vertex has positive probability of changing to either opinion (independent fair choices are a standard realization); therefore a singleton configuration is absorbing precisely when **at least three neighbors agree** with the color of each vertex. Only one-state fixed/absorbing configurations are counted, not two-cycles or larger recurrent communicating classes.

## Proof
Represent the \(j\)-th column by \(b_j\in\{0,1,\ldots,7\}\), with bit \(r\in\{0,1,2\}\) recording the vertex color. For columns \(a,b,c\) define \(w_r(a,b,c)\) as the number of neighbors of row \(r\)'s bit of \(b\) that agree with that bit: the other two bits of \(b\), bit \(r\) of \(a\), and bit \(r\) of \(c\). Explicitly, writing \(b_r\) for bit \(r\),
\[
w_r(a,b,c)=\sum_{s\ne r}[b_s=b_r]+[a_r=b_r]+[c_r=b_r],
\]
where brackets are the zero-one indicator. Index a matrix \(T\) by the \(64\) ordered pairs \((a,b)\). Set
\[
T_{(a,b),(b',c)}=[b=b']\prod_{r=0}^2[w_r(a,b,c)\ge2].
\]
All other entries vanish. The product is one exactly when the middle column is fixed by MM. A cyclic closed walk of length \(n\) in this state graph corresponds bijectively to one cyclic sequence of \(n\) columns, since the states are their consecutive overlapping pairs. The starting vertex of \(G_n\) is already labeled; this counts each assignment once, not \(n\) times. Consequently \(A_n=\operatorname{tr}(T^n)\) for each \(n\ge3\).

The displayed characteristic polynomial follows from an **integer determinant** of this fully specified \(64\times64\) matrix. To make the nontrivial finite arithmetic independently reproducible, `verify_torus.py` constructs every entry directly from \(w_r\) and asserts the complete factored polynomial by exact symbolic calculation (no numerical interpolation). The printed assertions were executed from the embedded source. Standard algebra then gives \(A_n\) as the power-sum of the characteristic roots, with algebraic multiplicity. The root \(3\) occurs exactly once. Every other root has absolute value less than \(3\): the factors \(z\pm1\) clearly do; on \(|z|=3\), Rouché's theorem applied to the leading monomial of each factor establishes all its roots lie in the interior, because the respective sums of absolute-value bounds on the lower coefficients are \(4<27\) for \(z^3+z+1\), \(10<27\) for \(z^3-z^2-1\), \(22<27\) for \(z^3-2z^2+z+1\), and \(21<81\) for \(z^4+z^2-3z-3\). The \(42\) zero roots contribute nothing. Hence \(A_n=3^n+O(\rho^n)\) for some \(0<\rho<3\), proving its asymptotics and entropy.

For RMM, suppose a column is nonmonochromatic. Because it has only three vertices, there is a uniquely colored minority vertex. Both of its vertical (within-column) neighbors disagree with it, so at most its two horizontal neighbors agree. This cannot satisfy the strict neighbor-majority condition \(w_r\ge3\). Thus **every column is monochromatic** in a singleton absorbing RMM configuration. Conversely, in a monochromatic column the two vertical neighbors always agree; a vertex has a strict majority of agreeing neighbors exactly when at least one of its two horizontally neighboring columns has the same color. Therefore the absorbing states are in bijection with binary cyclic words of length \(n\) having no isolated bit.

This last count can be derived without appealing to enumeration: index \(S\), a \(4\times4\) zero-one transfer matrix, by consecutive pairs \((a,b)\in\{0,1\}^2\), and set \(S_{(a,b),(b',c)}=[b=b'][a=b\ \mathrm{or}\ b=c]\). Its characteristic polynomial is \((z^2-z-1)(z^2-z+1)\). Consequently \(B_n=\operatorname{tr}(S^n)\), and summing the powers of its four characteristic roots yields
\(B_n=\varphi^n+\widehat\varphi^{\,n}+2\cos(n\pi/3)\). The number of cyclic binary strings with no isolated symbol and its formula are known from Agur, Fraenkel and Klein (1988); here the new step is the forced-monochromatic-column reduction and the comparative width-three entropy result.

## Verification
The standalone file `verify_torus.py`, requiring Python 3.10+ and SymPy 1.12+, constructs the \(64\times64\) matrix directly, checks the characteristic polynomial over exact integers and cross-checks against a **separate vertex-neighbor brute-force enumerator** for \(n=3,4,5,6\). It also independently verifies the random-tie counts against exhaustive binary cyclic words and the transfer trace. The outcome was

| \(n\) | \(A_n\) (MM) | \(B_n\) (RMM singleton) |
|---:|---:|---:|
| 3 | 32 | 2 |
| 4 | 94 | 6 |
| 5 | 218 | 12 |
| 6 | 712 | 20 |

The exact determinant and the combinatorial bijections, not finite brute-force experiments, establish the claim for all \(n\ge3\). Reproduction: `python -m pip install -r requirements.txt` followed by `python verify_torus.py`.

## Relationship to prior work
Zehmakan (arXiv:2302.06760, first public February 14, 2023; subsequently *Majority Opinion Diffusion: When Tie-Breaking Rule Matters*) treats MM and RMM together, establishing exponentially many MM fixed colorings but only two RMM absorbing singleton configurations on the ordinary cycle. This theorem addresses the first nondegenerate four-regular toroidal strip \(C_3\square C_n\), where the RMM count becomes exponential, and supplies an exact MM transfer spectrum. Agur–Fraenkel–Klein (1988) already enumerated no-isolated-symbol cyclic words; that combinatorial formula is **not** represented as new. The Ising zero-temperature terminology of locally stable spins is an equivalent description of the MM fixed-point condition, but an inspected covering exact width-three count was not located. Related fixed-point enumerations on open ladders use different boundary conditions and sometimes self-inclusive voting.

## Limitations
The theorem is restricted to binary synchronous majority dynamics on simple \(C_3\square C_n\), with \(n\ge3\), uniform neighborhood weights, and exactly the two tie rules specified. It counts singleton fixed/absorbing configurations, not multi-state closed classes, periodic attractors, their stability basins, hitting probabilities, expected stabilization times, noise-sensitive metastable lifetimes, or higher-width tori. Its computational certificate validates a fully stated exact determinant but is not an independent human audit. Unindexed equivalent strip/Ising enumerations remain a bibliographic risk; no uniqueness claim is drawn merely from unsuccessful searches.

## References
1. A. N. Zehmakan, *Random Majority Opinion Diffusion: Stabilization Time, Absorbing States, and Influential Nodes*, arXiv:2302.06760v1, February 14, 2023. https://arxiv.org/abs/2302.06760 . See also *Majority Opinion Diffusion: When Tie-Breaking Rule Matters*, https://doi.org/10.1007/s10458-024-09651-y .
2. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, https://doi.org/10.1016/0012-365X(88)90005-2 ; lawful accessible text https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
3. For comparison of a different self-inclusive, open-ladder setup: OEIS A395029, https://oeis.org/A395029 .
