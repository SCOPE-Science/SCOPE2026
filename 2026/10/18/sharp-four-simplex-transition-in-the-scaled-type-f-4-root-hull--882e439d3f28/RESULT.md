# Sharp four-simplex transition in the scaled type-\(F_4\) root hull

## Finding

In \(\mathbb R^4\), with standard basis \(e_1,\ldots,e_4\), define the two 24-point root configurations
\[
L=\{\epsilon e_i+\eta e_j:1\le i<j\le4,\ \epsilon,\eta\in\{-1,1\}\},
\quad
S=\{\pm e_i:1\le i\le4\}\cup\left\{\tfrac12(\epsilon_1,\epsilon_2,\epsilon_3,\epsilon_4):\epsilon_i\in\{-1,1\}\right\}.
\]
For every real \(t>0\), set \(K_t=\operatorname{conv}(L\cup tS)\). The maximum four-dimensional Euclidean volume of **any** nondegenerate four-simplex contained in \(K_t\), with no restriction on its vertices, is
\[
\boxed{M(t)=\max\{\tfrac12,\tfrac{t^4}{8}\}.}
\]
There are exactly \(48\) maximizing geometric four-simplices for \(0<t<\sqrt2\), exactly \(96\) for \(t=\sqrt2\), and exactly \(48\) for \(t>\sqrt2\). All their vertices belong to the specified root generators: all five are in \(L\) below the transition and all five are in \(tS\) above it. At the transition there are exactly \(48\) of each pure type and **no mixed-type maximizer**. The 48 pure-long maximizers form one orbit under signed-coordinate permutations. The 48 pure-short maximizers split into three orbits of 16 each under that same group; the two pure families are related by an explicit orthogonal transformation.

At \(t=\sqrt2\), among *vertex-supported* four-simplices with at least one long and one scaled short root, the sharp maximum volume is \(\sqrt2/3<1/2\). Precisely \(288\) mixed-root sets attain that lesser maximum: \(144\) with four long roots and one short root, and \(144\) with one long root and four short roots.

## Assumptions and scope

The point sets are sets of distinct points, and simplex volume means four-dimensional Lebesgue volume. A geometric simplex is counted once, ignoring the order of its five vertices. The optimizer classification is unrestricted over the entire convex body, not merely over its displayed generators. The mixed-root secondary bound refers specifically to five distinct root generators at the equal-circumradius transition. The root families above give the classical long and short type-\(F_4\) configuration; the normalized equality configuration is also called the disphenoidal 288-cell. The precise coordinates, rather than a polytope name, define all statements.

## Proof

**Dual 24-cell geometry.** Let
\[
Q=\frac1{\sqrt2}\begin{pmatrix}
1&1&0&0\\1&-1&0&0\\0&0&1&1\\0&0&1&-1
\end{pmatrix}.
\]
Then \(Q\) is orthogonal and \(Q(L)=\sqrt2 S\): roots supported on either two-coordinate block map to axial short roots, while cross-block roots map to all sixteen signed half-coordinate roots after scaling. Thus \(\operatorname{conv}(L)\) and \(\operatorname{conv}(\sqrt2 S)\) are congruent regular 24-cells. Signed permutations of four coordinates preserve each set and act transitively on \(L\).

**Exact finite mixed-root bound at the critical body.** Put \(K_*=K_{\sqrt2}\). Double every unscaled root coordinate to work with integers: each long row has entries \(\pm2\) in two positions, and each short row is axial \(\pm2e_i\) or a vector with four entries \(\pm1\). For five selected roots, use the augmented determinant \(D(t)\) with a first column of ones and the other four columns equal to the doubled vertex coordinates, multiplying every short-root row's four coordinates by \(t\). If exactly \(k\) of the five selected vertices are short, Laplace expansion along the first column shows
\[
D(t)=t^{k-1}(At+B)\quad (1\le k\le5),
\]
where \(A,B\) are explicit integers, each computed from determinants of four integer root vectors. For \(k=0\) the determinant is an integer independent of \(t\). In particular, at \(t=\sqrt2\), every determinant has the form \(u+v\sqrt2\) with integers \(u,v\). The associated Euclidean simplex volume is \(|D(t)|/384\), because doubling four spatial coordinates multiplies the edge determinant by \(16\), and division by \(4!=24\) converts determinant to volume.

Fix the long root \(\ell_0=(-e_1-e_2)\). Transitivity of signed-coordinate permutations reduces every five-root set containing at least one long root to the \(\binom{47}{4}=178365\) sets containing \(\ell_0\). The exhaustive exact-arithmetic certificate in `verify.py` checks the following determinant-magnitude maxima for these sets, by number \(k\) of short vertices:
\[
\begin{array}{c|rrrrr}
 k&0&1&2&3&4\\\hline
 \max |D(\sqrt2)|&192&128\sqrt2&128+32\sqrt2&128+32\sqrt2&128\sqrt2.
\end{array}
\]
Its exact grouped sizes are \(8855,42504,69828,46552,10626\), respectively. It finds \(10\) anchored pure-long sets attaining \(192\), \(24\) anchored one-short sets attaining \(128\sqrt2\), and \(6\) anchored four-short sets attaining \(128\sqrt2\). No anchored two- or three-short set attains \(128\sqrt2\). These inequalities are established by integer comparisons in \(\mathbb Q(\sqrt2)\), not floating-point estimates. The independently implemented integer-permutation checker `verify.cpp` reaches the same results. The comparisons and generators are fully specified in those standalone artifacts.

For a concrete mixed-bound witness, the five vertices
\[
(-1,-1,0,0),\quad(-1,1,0,0),\quad(1,0,-1,0),\quad(1,0,1,0),\quad(0,0,0,-\sqrt2)
\]
form a mixed-root four-simplex of volume exactly \(\sqrt2/3\) at the transition. The first four are long roots and the last is a scaled short root.

Each five-root set containing a long root has been checked: the fixed-root reduction cannot miss any such set. Five-short-root sets are equivalent, through \(Q\), to five-long-root sets. Counting incidences between maximal root sets and a marked long root gives \(24\cdot10/5=48\) pure-long maximizers, \(24\cdot24/4=144\) one-short mixed sets attaining the mixed bound, and \(24\cdot6/1=144\) four-short mixed sets attaining the bound. Congruence gives another \(48\) pure-short maximizers. Hence the largest five-root simplex in \(K_*\) has volume \(192/384=1/2\), while the sharp mixed-root bound is \(128\sqrt2/384=\sqrt2/3\).

The same exact checker enumerates all \(\binom{24}{5}=42504\) pure-long five-sets, verifies the \(48\) maximizing sets and checks that **no two** share four vertices. The pure-short sets have the same property by \(Q\); they split into exactly three signed-coordinate-permutation orbits of sixteen, according to whether each pure-short five-set has zero, one, or four axial roots. The two pure families are disjoint, so distinct maximizing five-root sets anywhere in \(K_*\) never share four vertices.

**Unrestricted optimizers and rigidity.** Because a simplex determinant is affine in each individual vertex, its absolute value over a compact convex polytope attains its maximum when all simplex vertices are chosen from the generating set. Now suppose an unrestricted maximum simplex in \(K_*\) has a non-generator vertex \(p\). Keeping \(p\) fixed, push its other four corners successively to generating roots without decreasing volume. Express \(p\) as a nontrivial convex combination of at least two distinct generating roots. Equality in the absolute-value convexity inequality forces each root appearing with positive weight to produce the same maximal **signed** determinant with the fixed four remaining corners. Those two roots would generate distinct maximum-volume five-root sets sharing four roots, contradicting the preceding exact incidence result. Therefore every unrestricted maximizing simplex in \(K_*\) uses five generating roots and belongs to one of the \(96\) pure families.

**All scale parameters.** For \(0<t\le\sqrt2\), symmetry about the origin gives \(K_t\subseteq K_*\), while \(L\subseteq K_t\); hence \(M(t)=1/2\). For \(t\ge\sqrt2\), put \(c=t/\sqrt2\). Central symmetry similarly gives \(K_t\subseteq cK_*\), while \(tS\subseteq K_t\). Four-dimensional homogeneity yields \(M(t)=c^4/2=t^4/8\).

For strict \(t<\sqrt2\), no root \(\sqrt2 s\) with \(s\in S\) belongs to \(K_t\): taking scalar product with \(s\) gives the required value \(\sqrt2\), whereas \(h_{K_t}(s)\le\max\{1,t\}<\sqrt2\), because \(s\cdot\ell\le1\) for every \(\ell\in L\). For strict \(t>\sqrt2\), no scaled long root \(c\ell\) belongs to \(K_t\): its scalar product with \(\ell\) is \(\sqrt2 t\), whereas \(h_{K_t}(\ell)\le\max\{2,t\}<\sqrt2 t\), because \(\ell\cdot s\le1\) for every \(s\in S\). Thus the equality classification in \(K_*\), transferred through the inclusions, leaves only the asserted root type on either side of the transition, proving all counts and rigidity claims.

## Verification

Run `python3 verify.py` (Python standard library, without optimization flags). It generates precisely 24 long and 24 short integer-coordinate roots; checks all \(178365\) anchored five-sets by cached exact cofactor determinants; compares \(\mathbb Q(\sqrt2)\) values through integer sign tests; checks all \(42504\) pure-long five-sets and their four-vertex faces; and verifies the explicit block-Hadamard duality and the three 16-member pure-short symmetry orbits. It reports the expected \(48\) pure-long maximizers with no shared four-vertex face. Independently compile and run `c++ -std=c++17 -O2 verify.cpp -o verify_f4 && ./verify_f4`; this code uses signed-permutation determinant expansion instead of cofactors. Both checks complete without external data.

The finite arithmetic is a complete search of the precisely defined finite configurations, not a sample of continuous simplices. The vertex-reduction, non-generator rigidity, and parameter inclusions are separate mathematical arguments. The certificate is self-contained; its source code and all required inputs are included here.

## Relationship to prior work

Koca, Koca, and Al-Barwani (2011) study quaternionic \(D_4\)/\(F_4\) symmetry and four-polytopes; Dechant (2013) explicitly constructs the 48-point \(F_4\) root geometry from three-dimensional polyhedral groups. Neither inspected text derives a largest four-simplex formula for the long/short radial family. Horváth and Lángi (2014) determine optimal *unconstrained* spherical polytopes by number of vertices; their general five-point sphere optimum does not impose the discrete \(F_4\) root configuration, and it does not imply the sharp mixed-root bound. A previously published exact largest-simplex result for the regular \(D_4\) 24-cell gives the \(48\) pure-root optimum and its determinant spectrum but does not compare simplices whose vertices come from two orthogonal dual 24-cells. The essential additional input here is the strict mixed-root bound at equal circumradius, which drives the all-parameter transition and optimizer classification.

## Limitations

This is an exact theorem only for the specified \(F_4\) root sets and their relative radial scaling, not for arbitrary pairs of regular 24-cells or other root systems. The discrete mixed bound and optimizer-face incidence use exhaustive finite integer arithmetic reproduced in the accompanying checkers. Neither checker constitutes an independent mathematical audit. A complete historical-priority classification is not established; unindexed classical disphenoidal-288-cell or \(F_4\) simplex tables may overlap some conclusions.

## References

M. Koca, N. O. Koca, and M. Al-Barwani, “Snub 24-Cell Derived from the Coxeter–Weyl Group \(W(D_4)\),” arXiv:1106.3433, initial public version 2011-06-17; https://arxiv.org/abs/1106.3433.

P.-P. Dechant, “Platonic solids generate their four-dimensional analogues,” arXiv:1307.6768v1, first public 2013-07-25, especially Theorems 3.3–3.4; https://arxiv.org/html/1307.6768v1.

Á. G. Horváth and Z. Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496v1, first public 2014-02-26; https://arxiv.org/html/1402.6496v3.

“Exact largest-simplex volume and equality classification in the regular 24-cell,” previously published mathematical finding, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-largest-simplex-volume-and-equality-classification-in-the--bda0674b8ea5/RESULT.md (scientific overlap comparison only).
