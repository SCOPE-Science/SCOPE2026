# Sharp re-entrant unimodality windows for \(K_4\times K_r\) and \(K_5\times K_r\)

## Finding
For \(a\in\{4,5\}\) and each integer \(r\ge3\), let \(G_{a,r}=K_a\times K_r\) be the direct (categorical/tensor) product: its vertices are pairs \((i,j)\in[a]\times[r]\), and distinct vertices are adjacent precisely when both coordinates differ. Let
\[
\Psi_{a,r}(z)=\sum_{S\subseteq V(G_{a,r})\text{ in general position}}z^{|S|}=\sum_k b_k(a,r)z^k.
\]
A set is in general position if no three distinct selected vertices occur on a common graph geodesic. Then, **for every integer \(r\ge3\)**,
\[
\begin{aligned}
\Psi_{4,r}(z)\text{ is unimodal}&\iff 3\le r\le11\ \text{or}\ r\ge40,\\
\Psi_{5,r}(z)\text{ is unimodal}&\iff 3\le r\le13\ \text{or}\ r\ge156.
\end{aligned}
\]
Thus the exact nonunimodal windows are \(12\le r\le39\) for \(a=4\) and \(14\le r\le155\) for \(a=5\). Both families first lose and later regain unimodality, with sharp re-entry dimensions \(40\) and \(156\), respectively. These statements concern coefficient unimodality, **not** log-concavity or roots.

## Assumptions and scope
All graphs are finite, undirected and simple. Binomial coefficients \(\binom nk\) vanish for \(k<0\) or \(k>n\). A finite nonnegative sequence is unimodal when its entries are weakly nondecreasing up to some index and weakly nonincreasing thereafter. Degree ranges terminate at the degree of the polynomial; zero coefficients beyond that degree are not counted as additional terms. The parameter \(r\) is integral and at least three. Coordinate order is fixed by \([a]\times[r]\).

## Proof
**General-position counting premise.** The graph \(K_a\times K_r\) has diameter two for \(a,r\ge3\). In any diameter-two graph, a three-vertex set violates general position exactly when it induces a path of length two. Therefore an induced vertex set is in general position exactly when its induced graph is a disjoint union of cliques. For \(K_a\times K_r\), a set of size at least three with this property is of exactly one of the following disjoint kinds: wholly in one fixed first-coordinate row; wholly in one fixed second-coordinate column; a partial permutation (all first coordinates distinct and all second coordinates distinct); or a subset of size three or four of a two-by-two coordinate rectangle using both rows and both columns. To see exhaustiveness, take two selected vertices with one common coordinate, say one row. Every selected vertex outside that row must occupy one of the two columns of this pair, otherwise it forms an induced two-edge path with the pair. Three vertices in the row prohibit any outside vertex. With exactly two, two outside vertices cannot occupy distinct outside rows (nor the same outside column), again by an induced two-edge path. Thus all selected vertices fit in a two-by-two rectangle. The symmetric argument treats a repeated column. If no coordinate is repeated, the set is a partial permutation. Inside a two-by-two rectangle the graph consists of two independent edges, and every size-three or size-four subset is valid. The classification, also provided in the published enumeration literature, yields, for \(k\ge3\),
\[
 b_k(a,r)=a\binom rk+r\binom ak+k!\binom ak\binom rk+\binom a2\binom r2\binom4k,
\]
where \(b_0=1\), \(b_1=ar\), and \(b_2=\binom{ar}{2}\). This formula is the *previously known premise*, not the novel claim. In particular the tail beginning at \(k=a+1\) is \(a\binom rk\), a nonnegative unimodal binomial tail. The new task is to compare the finitely many exceptional boundary coefficients *uniformly in the unbounded parameter* \(r\).

**The case \(a=4\).** In this case
\[
\begin{aligned}
b_3&=28\binom r3+24\binom r2+4r,\\
b_4&=28\binom r4+6\binom r2+r,\\
b_k&=4\binom rk\quad(k\ge5).
\end{aligned}
\]
For every \(r\ge3\), direct subtraction gives
\[
 b_3-b_2=\frac{2r}{3}(7r^2-15r+5)>0.
\]
Also
\[
 b_4-b_3=7(r-7)\binom r3-18\binom r2-3r.
\]
This is negative for \(3\le r\le7\), and equals \(-136\) for \(r=8\). For \(r\ge9\), the first term is at least \(14\binom r3\), while \(\binom r3/\binom r2=(r-2)/3\ge7/3\), hence \(b_4-b_3\ge(44/3)\binom r2-3r>0\). Thus the coefficients through degree four increase to degree three when \(3\le r\le8\), and increase to degree four when \(r\ge9\).

The decisive first tail comparison is exactly
\[
 b_5-b_4=\frac{4(r-39)}5\binom r4-6\binom r2-r.
\]
For \(3\le r\le39\), this is strictly negative. For \(r\ge40\), use \(\binom r4/\binom r2=(r-2)(r-3)/12\ge(38\cdot37)/12>12\) and \(\binom r2\ge r\) to conclude \(b_5-b_4>(4/5)12\binom r2-6\binom r2-r>0\). Moreover the pure-binomial tail satisfies \(b_6>b_5\) precisely when \(r\ge12\), since \(\binom r6/\binom r5=(r-5)/6\). For \(3\le r\le11\), all early coefficients rise to one peak and the subsequent tail does not rise. For \(12\le r\le39\), the three consecutive terms satisfy \(b_4>b_5<b_6\), which forbids unimodality. For \(r\ge40\), the sequence grows through \(b_5\), and thereafter follows a unimodal binomial tail. This proves the first equivalence.

**The case \(a=5\).** Here
\[
\begin{aligned}
b_3&=65\binom r3+40\binom r2+10r,\\
b_4&=125\binom r4+10\binom r2+5r,\\
b_5&=125\binom r5+r,\\
b_k&=5\binom rk\quad(k\ge6).
\end{aligned}
\]
The first difference satisfies
\[
 b_3-b_2=\frac{5r(r-1)(13r-17)}6>0.
\]
The next two differences are
\[
\begin{aligned}
b_4-b_3&=\frac{125r-635}4\binom r3-30\binom r2-5r,\\
b_5-b_4&=25(r-9)\binom r4-10\binom r2-4r.
\end{aligned}
\]
The first is negative for \(3\le r\le5\). For \(r\ge6\), its positive first factor is at least \(115/4\) and \(\binom r3/\binom r2=(r-2)/3\ge4/3\), so it is at least \((25/3)\binom r2-5r>0\). The second is negative for \(r\le9\); for \(r\ge10\), the inequalities \(\binom r4/\binom r2\ge14/3\) and \(\binom r2\ge r\) make it strictly positive. Thus the initial coefficients rise to degree three when \(3\le r\le5\), to degree four when \(6\le r\le9\), and to degree five for \(r\ge10\).

At the tail junction,
\[
 b_6-b_5=\frac{5(r-155)}6\binom r5-r.
\]
This is strictly negative for \(3\le r\le155\). For \(r\ge156\), \(\binom r5\ge2r\) (true already for \(r\ge7\), and the ratio increases), giving \(b_6-b_5\ge(5/6)\binom r5-r>0\). The following binomial comparison is \(b_7>b_6\) precisely when \(r\ge14\), because \(\binom r7/\binom r6=(r-6)/7\). Consequently \(3\le r\le13\) is unimodal, \(14\le r\le155\) has the forbidden valley \(b_5>b_6<b_7\), and \(r\ge156\) rises to the binomial tail before its sole peak. This proves the second equivalence. All inequalities include the exact transition endpoints; no asymptotic argument is used. \(\square\)

## Verification
Standalone C++17 and Python 3 programs accompany this result. The graph verifier independently builds \(K_a\times K_r\), enumerates every subset in five small instances with a total of \(2,199,552\) examined subsets, and confirms the polynomial coefficient formula by checking induced two-edge paths. The arithmetic verifier uses arbitrary-precision integers to verify each unimodality statement independently for every \(3\le r\le500\), including the four boundary pairs. The proved inequalities, rather than these finite computations, cover all \(r\ge3\). The programs require only a C++17 compiler and Python standard library; run \(\texttt{g++ -O2 -std=c++17 verify.cpp -o verify \&\& ./verify}\) and \(\texttt{python3 verify_modal.py}\). Their recorded outputs are included. Independent external validation has not been performed.

## Relationship to prior work
Iršič, Klavžar, Rus and Tuite introduced general-position polynomials in 2024 and explicitly posed the problem of determining the unimodal parameter pairs for \(T^*(r,a)\), the same graph as \(K_a\times K_r\). Rather (2026, Theorem 5.3) supplies the corrected all-parameter coefficient formula used here; the enumeration itself is not claimed as new. Rather (Corollary 5.7) gives the sharp re-entrant interval when \(a=3\). The present result instead settles the entire \(a=4\) and \(a=5\) sections, with thresholds \(40\) and \(156\), and does not follow merely from the displayed \(a=3\) sign inequalities. Literature and database searching found no statement specifying these two intervals, but unindexed equivalences remain a bibliographic risk.

## Limitations
The result gives the two natural fixed-width sections \(a=4,5\), not the unrestricted two-parameter unimodality classification. It does not establish log-concavity, real-rootedness or analogous facts for the Cartesian product. The classification is proved mathematically and checked computationally in finite ranges; external independent scientific audit and exhaustive priority verification have not taken place.

## References
1. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first public version 2024-01-11), especially Problem 5.2. https://arxiv.org/abs/2401.05696
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (2026), Theorem 5.3 and Corollary 5.7. https://arxiv.org/abs/2603.06930
