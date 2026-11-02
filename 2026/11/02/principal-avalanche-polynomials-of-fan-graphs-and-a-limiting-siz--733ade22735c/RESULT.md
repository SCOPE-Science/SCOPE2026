# Principal avalanche polynomials of fan graphs and a limiting size-biased geometric law

## Finding

For the fan graph \(F_n=K_1\vee P_n\), with hub used as the sink, consider the principal avalanche polynomial \(A_n(t)\): sum over every recurrent stable sandpile configuration \(c\) and every nonsink vertex \(i\), with weight \(t^{a(c,i)}\), where \(a(c,i)\) is the number of individual topplings in the stabilization of \(c+e_i\). A zero-toppling addition contributes \(1\). For every integer \(n\ge2\), writing \(\Delta(z)=1-3z+z^2\), the exact bivariate rational generating function is

\[
\sum_{n\ge2}A_n(t)z^n=\frac{2z^2(1-z)}{\Delta(z)^2}+\frac{tz^2(2-5z+2z^2)}{(1-tz)^2\Delta(z)^2}+\frac{t^2z^2(2-tz)}{(1-tz)^2}.
\]

In particular let \(B(z)=(2-5z+2z^2)/\Delta(z)^2=\sum_{j\ge0}b_j z^j\). Then, for all \(1\le\ell<n\),
\[
[t^\ell]A_n(t)=\ell b_{n-\ell-1},\qquad [t^n]A_n(t)=n,\qquad [t^0]A_n(t)=[z^{n-2}]\frac{2(1-z)}{\Delta(z)^2}.
\]
All avalanche sizes from zero through \(n\) actually occur. For example,
\[
A_4(t)=38+22t+14t^2+6t^3+4t^4.
\]

The limiting law is also explicit. With \(\alpha=(3+\sqrt5)/2\), sample uniformly one of the recurrent configurations and one of the \(n\) nonsink vertices. For each fixed positive integer \(\ell\),
\[
\lim_{n\to\infty}\mathbb P(a(c,i)=0)=1-\frac1{\sqrt5},\qquad
\lim_{n\to\infty}\mathbb P(a(c,i)=\ell)=\frac{\ell}{\sqrt5}\alpha^{-\ell}.
\]
Thus the nonzero part is a size-biased geometric-type law, with total mass \(1/\sqrt5\).

## Assumptions and scope

The graph is finite, simple, undirected and has vertices \(s,1,\ldots,n\). The sink \(s\) is adjacent to every path vertex; consecutive path vertices are adjacent. A stable height at an endpoint belongs to \(\{0,1\}\); at an interior vertex it belongs to \(\{0,1,2\}\). A site topples when its height reaches its full graph degree; each toppling sends one chip to each nonsink neighbour and loses the chips sent to the sink. Recurrence means the ordinary abelian-sandpile recurrent state relative to sink \(s\). Events count individual topplings, not merely the number of distinct toppled vertices. The theorem applies for every \(n\ge2\) and does not address a different sink choice.

## Proof

**1. Recurrent words.** The sink-burning test sends one chip to each path vertex. A stable configuration is recurrent precisely when any two zero heights have a height-two vertex strictly between them. Indeed, after the sink burns, a height-two internal site can burn even with both neighbours unburned, and every site of height one can burn once an adjacent site has burned (or if it is an endpoint); a height-zero site needs both neighbours previously burned. A block without height twos containing two zeros would be separated into pieces with no legal initial burning order. Conversely, divide at every height-two site: each intervening binary segment has at most one zero and can be burned inward from its boundary. This recurrent-word characterization was already present in the primary literature and is not claimed as new.

Let \(L(z)=1/(1-z)^2\) count binary segments with at most one zero. A recurrent word of length at least two without a two contributes \(L(z)-1-2z\). Otherwise it has an initial and final nonempty binary segment, separated by at least one height-two letter, with arbitrary such binary segments between consecutive twos. Therefore the known recurrent-count generating function is
\[
R(z)=\sum_{n\ge2}r_nz^n=L(z)-1-2z+\frac{z(L(z)-1)^2}{1-zL(z)}=\frac{z^2(3-z)}{\Delta(z)}.
\]
Thus \(r_n=F_{2n}\), with the conventional Fibonacci numbers \(F_0=0,F_1=1\).

**2. Saturated-run avalanche lemma.** Call a path vertex saturated when its height is degree minus one: an endpoint at height one, or an internal vertex at height two. If the addition site is unsaturated, nothing topples. Otherwise start at its maximal consecutive saturated interval \(I\). An addition triggers every site of \(I\) exactly once by outward propagation. Neither adjacent exterior vertex, if any, topples: it is unsaturated and receives at most one chip. A site inside \(I\), after its one toppling, receives at most two further chips, leaving its height at most two (or at most one at an endpoint), hence is stable. Consequently the total number of topplings is \(|I|\). No unbounded-toppling assumption is hidden in this argument.

**3. Marked-run generating function.** Let \(M(z,t)\) count recurrent words of length at least two with one *maximal* nonempty saturated run marked, weighted by \(t\) for each vertex of the marked run. An eight-state transfer system suffices: before the marked run retain (i) whether a zero has appeared since the last two and (ii) whether the previous vertex was saturated; inside and after the marked run retain only the zero-seen bit. A zero is allowed only when the zero-seen bit is false; a two resets this bit; a one preserves it. Marking may begin only at a saturated site preceded by an unsaturated site (or the left boundary); inside the marked run every site is saturated; exiting requires the first unsaturated site. Endpoints have alphabet \(\{0,1\}\), interiors \(\{0,1,2\}\). The complete rational-arithmetic matrix specification is implemented in `checks/transfer_identity.py`. Direct inversion of its middle-site matrix and multiplication by endpoint matrices gives, with \(B(z)=(2-5z+2z^2)/\Delta(z)^2\),
\[
M(z,t)=\frac{z^2t}{1-tz}\left(t+B(z)\right).
\]
Each length-\(j\) marked maximal run permits exactly \(j\) trigger sites and contributes an avalanche of size \(j\); therefore \(N(z,t)=t\partial_tM(z,t)\) counts all positive avalanches. The total number of trigger choices of each length is \(zR'(z)\), so the full avalanche series is \(zR'(z)-N(z,1)+N(z,t)\). Simplifying this rational identity yields the boxed formula.

**4. Coefficients and limit law.** Expanding \((1-tz)^{-2}\) yields \([t^\ell]A_n=\ell b_{n-\ell-1}\) for positive \(\ell<n\); the final rational term supplies the full-run coefficient \(n\). The constant term is obtained directly from the first rational term. The coefficients \(b_j\) are positive: equivalently, they count realizable marked-saturated-run environments; their series begins \(2,7,22,67,200,588,\ldots\). The second-order pole at \(z=1/\alpha\) gives \(b_j\sim\frac{3+\sqrt5}{10}(j+1)\alpha^j\), whereas \(r_n\sim\alpha^n/\sqrt5\). Dividing the fixed-\(\ell\) coefficients by \(nr_n\) yields \(\ell\alpha^{-\ell}/\sqrt5\). Applying the same dominant-pole calculation to the constant term gives \(1-1/\sqrt5\). The limiting masses sum to one because \(\sum_{\ell\ge1}\ell\alpha^{-\ell}=1\).

## Verification

Two reproducible Python programs are supplied. `checks/direct_burning.py` independently enumerates stable configurations for \(2\le n\le9\), classifies recurrence using an explicit sink-burning algorithm, performs all additions and topplings directly, and checks the full coefficient arrays against the rational formula. It also independently compares the burning condition with the recurrent-word condition.

`checks/transfer_identity.py` constructs the eight-state transfer matrices over \(\mathbb Q(z,t)\) in SymPy and proves by exact symbolic simplification the marked-run identity, the positive-event identity, the recurrent generating function, and the final bivariate formula. To reproduce, run `python checks/direct_burning.py` and `python checks/transfer_identity.py` with SymPy installed. These are exhaustive finite corroboration and exact algebraic identity checks respectively; the preceding combinatorial arguments explain why the formulas hold for arbitrary \(n\).

## Relationship to prior work

Austin and collaborators, *The Avalanche Polynomial of a Graph* (first public arXiv version 9 May 2016, arXiv:1605.02713), introduce the avalanche polynomial and extensively analyze wheels; their Proposition 43 characterizes and counts recurrent configurations on fans as an auxiliary to the wheel computation. The present theorem uses those recurrent facts but computes the distinct, fan-graph principal-avalanche polynomial and its limiting distribution; their wheel polynomial does not state this answer. Earlier work by Cori, Dartois and Rossin concerns avalanche polynomials for other graph families, and work of Aval and collaborators concerns complete bipartite sandpiles. The fan polynomial is not merely the specialization of the complete-bipartite formula since fan graphs have path edges among nonsink vertices.

The accessible literature search did not reveal this exact bivariate fan identity. This does not prove global bibliographic uniqueness; see the limitations below.

## Limitations

This is an exact theorem for a designated sink, a particular graph family and a particular avalanche definition. The number of topplings equals the number of distinct toppled vertices only because of the proved saturated-run lemma. The original 2004 avalanche-polynomial chapter by Cori, Dartois and Rossin (DOI below) was not available in full text during the literature comparison; its coverage as described in the 2016 primary paper appears to concern other families, but an unforeseen equivalent historical result remains possible. The findings are not independently audited.

## References

1. Austin et al., *The Avalanche Polynomial of a Graph*, arXiv:1605.02713v1, first public 2016-05-09, https://arxiv.org/abs/1605.02713 (especially the fan recurrence characterization in Proposition 43 and the wheel results in Section 6).
2. R. Cori, M. Dartois and D. Rossin, *Avalanche Polynomials of Some Families of Graphs*, 2004, DOI:10.1007/978-3-0348-7915-6_10 (historical background; full text not verified).
3. J.-C. Aval and collaborators, *Two operators on sandpile configurations, the sandpile model on the complete bipartite graph, and a Cyclic Lemma*, https://strathprints.strath.ac.uk/54658/1/Aval_etal_AAM_2015_Two_operators_on_sandpile_configurations_the_sandpile_model_on_the_complete_bipartite_graph.pdf (different family).
