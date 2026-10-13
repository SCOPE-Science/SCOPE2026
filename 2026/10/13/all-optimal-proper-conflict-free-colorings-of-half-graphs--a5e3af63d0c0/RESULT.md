# All optimal proper conflict-free colorings of half graphs
## Finding
For every integer \(n\ge4\), let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and edge rule
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\chi_{\mathrm{pcf}}(H_n)=4.
\]

More strongly, all optimal colorings are completely classified. For any optimal coloring \(\varphi\), define
\[
c_0=\varphi(a_1),\quad c_1=\varphi(a_2),\quad c_2=\varphi(b_{n-1}),\quad c_3=\varphi(b_n).
\]
These four colors are pairwise distinct. Choose independently
\[
t\in\{c_0,c_1\},\qquad s\in\{c_2,c_3\}.
\]
Then every optimal coloring has exactly the form
\[
\varphi(a_3)=\cdots=\varphi(a_{n-1})=t,
\qquad
\varphi(a_n)\in\{t,c_2\},
\]
and
\[
\varphi(b_2)=\cdots=\varphi(b_{n-2})=s,
\qquad
\varphi(b_1)\in\{c_1,s\}.
\]
Conversely, every assignment of this form is a proper conflict-free coloring.

Thus there are exactly
\[
2^4=16
\]
optimal colorings up to permutation of the four colors, and exactly
\[
4!\,2^4=384
\]
named optimal four-colorings. Remarkably, this count is independent of \(n\).

## Assumptions and scope
A proper conflict-free coloring is a proper vertex coloring in which every nonisolated vertex has a color that appears exactly once in its open neighborhood. The minimum number of colors is denoted \(\chi_{\mathrm{pcf}}\).

The half graph convention here is the nested-neighborhood bipartite graph above. It is a canonical chain/Ferrers graph: the neighborhoods on each side are linearly ordered by inclusion.

The structural classification is stated for \(n\ge4\). The boundary \(H_3\) also has proper conflict-free chromatic number \(4\), but it has additional optimal coloring patterns because the two interior constant blocks used in the theorem are empty. The graph \(H_2\) is a path on four vertices and belongs to the previously solved tree case.

## Proof
We first prove the lower bound. Suppose \(n\ge3\) and \(\varphi\) is proper conflict-free.

The open neighborhood of \(b_2\) is exactly
\[
N(b_2)=\{a_1,a_2\}.
\]
For a color to occur exactly once there, \(a_1\) and \(a_2\) must have different colors. Similarly,
\[
N(a_{n-1})=\{b_{n-1},b_n\},
\]
so \(b_{n-1}\) and \(b_n\) have different colors.

Every vertex in \(\{a_1,a_2\}\) is adjacent to every vertex in \(\{b_{n-1},b_n\}\). Properness therefore makes all four colors
\[
\varphi(a_1),\quad \varphi(a_2),\quad \varphi(b_{n-1}),\quad \varphi(b_n)
\]
pairwise distinct. Hence
\[
\chi_{\mathrm{pcf}}(H_n)\ge4.
\tag{1}
\]

A four-coloring exists, for example by coloring \(a_1\) with one color, all other vertices of \(A\) with a second color except as needed to keep \(a_1,a_2\) distinct, coloring \(b_n\) with a third color, and all earlier vertices of \(B\) with a fourth color. More explicitly, the classified family below contains such a coloring, so equality holds in (1).

Now fix an optimal four-coloring and write
\[
c_0=\varphi(a_1),\quad c_1=\varphi(a_2),\quad c_2=\varphi(b_{n-1}),\quad c_3=\varphi(b_n).
\]
The lower-bound argument already shows that these are the four distinct available colors.

Because \(b_n\) is adjacent to every vertex of \(A\), color \(c_3\) does not occur on \(A\). Because \(b_{n-1}\) is adjacent to \(a_1,\ldots,a_{n-1}\), color \(c_2\) does not occur on those first \(n-1\) vertices. Thus
\[
\varphi(a_i)\in\{c_0,c_1\}
\qquad(1\le i\le n-1).
\tag{2}
\]
For every \(j\), the neighborhood of \(b_j\) is the prefix
\[
N(b_j)=\{a_1,\ldots,a_j\}.
\]
Hence every prefix of the sequence
\[
\varphi(a_1),\ldots,\varphi(a_{n-1})
\]
must contain a color occurring exactly once.

We use a simple binary-prefix observation. If a binary sequence begins with two distinct symbols and every prefix has a singleton symbol, then from the third term onward all terms are equal. Indeed, after the third term one symbol occurs once and the other twice; adding the singleton symbol would make both multiplicities at least two, so every later term must repeat the current majority symbol. Consequently there is
\[
t\in\{c_0,c_1\}
\]
such that
\[
\varphi(a_3)=\cdots=\varphi(a_{n-1})=t.
\tag{3}
\]

The last vertex \(a_n\) cannot receive \(c_3\), and it may receive \(c_2\). If it receives the color in \(\{c_0,c_1\}\setminus\{t\}\), then the full prefix \(N(b_n)=A\) has no singleton color: the formerly unique color is used a second time, while \(t\) is already repeated. Therefore
\[
\varphi(a_n)\in\{t,c_2\}.
\tag{4}
\]

The argument on the other side is the exact reverse. Since \(a_1\) is adjacent to every vertex of \(B\), color \(c_0\) does not occur on \(B\). Since \(a_2\) is adjacent to \(b_2,\ldots,b_n\), color \(c_1\) does not occur there. Hence
\[
\varphi(b_j)\in\{c_2,c_3\}
\qquad(2\le j\le n).
\]
Every neighborhood
\[
N(a_i)=\{b_i,\ldots,b_n\}
\]
is a suffix, so the reversed binary-prefix observation yields some
\[
s\in\{c_2,c_3\}
\]
with
\[
\varphi(b_2)=\cdots=\varphi(b_{n-2})=s.
\tag{5}
\]
The full suffix at \(a_1\) then forces
\[
\varphi(b_1)\in\{c_1,s\};
\tag{6}
\]
using the other member of \(\{c_2,c_3\}\) would eliminate the last singleton color.

Equations (3)–(6) prove necessity.

Conversely, every listed assignment is proper. The only possible reuse of \(c_2\) across the bipartition is at \(a_n\), but \(a_n\) is adjacent only to \(b_n\), whose color is \(c_3\). The only possible reuse of \(c_1\) across the bipartition is at \(b_1\), but \(b_1\) is adjacent only to \(a_1\), whose color is \(c_0\). All other colors are separated by side. The binary prefix and suffix forms show directly that every neighborhood retains a singleton color. Hence every listed assignment is proper conflict-free.

There are four independent binary choices: \(t\), whether \(a_n\) is \(t\) or \(c_2\), \(s\), and whether \(b_1\) is \(s\) or \(c_1\). This gives \(16\) color-permutation classes. Assigning the four named colors to \((c_0,c_1,c_2,c_3)\) gives another factor of \(4!\), for a total of \(384\).

## Verification
The included checker constructs \(H_n\) from the defining inequality \(i\le j\) and tests properness and the open-neighborhood singleton condition directly.

It exhausts every three- and four-color assignment for \(n=3,4,5\), a total of \(1{,}184{,}547\) assignments. No three-coloring is proper conflict-free. For \(n=4\) and \(n=5\), it finds exactly \(384\) four-colorings; after fixing
\[
\varphi(a_1)=0,\quad \varphi(a_2)=1,\quad \varphi(b_{n-1})=2,\quad \varphi(b_n)=3,
\]
the complete exhaustive set consists of exactly the \(16\) theorem-predicted forms.

The verifier also constructs all \(16\) normalized forms and checks them directly for every
\[
4\le n\le50.
\]

## Relationship to prior work
Fabrici, Lužar, Rindošová, and Soták initiated the study of proper conflict-free coloring with respect to open neighborhoods. Their work focuses mainly on planar and outerplanar bounds. Its accessible full text contains no occurrence of “half”, “chain”, or “Ferrers”, and no half-graph theorem.

Caro, Petruševski, and Škrekovski subsequently determined the parameter for several basic graph classes, including trees, cycles, hypercubes, and subdivisions of complete graphs, and proved general maximum-degree bounds. Those classes and bounds do not determine the half-graph value or the exact optimizer family.

Later work developed sparse and planar upper bounds. A 2024 full-text treatment of odd and proper conflict-free coloring again contains no “half”, “chain”, or “Ferrers” occurrence. The closest indexed exact family found in the checked literature is a crown-graph result for the same parameter; crown graphs have almost-complete bipartite neighborhoods rather than the nested Ferrers neighborhoods of half graphs and do not imply the theorem above.

## Limitations
The full optimal-coloring classification is for \(n\ge4\). The boundary \(H_3\) still has \(\chi_{\mathrm{pcf}}=4\), but the absence of interior vertices creates additional optimal patterns; the exhaustive checker finds \(216\) named four-colorings there.

The theorem is for half graphs, not arbitrary chain graphs with repeated neighborhood classes.

The finite computation is corroborative only. The all-order classification and count follow from the four forced core colors and the binary prefix/suffix argument.

A differently phrased or non-indexed half-graph treatment may exist.

## References
1. I. Fabrici, B. Lužar, S. Rindošová, R. Soták, “Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods,” arXiv:2202.02570v1, first public version 5 February 2022; Discrete Applied Mathematics 324 (2023), 80–92, DOI 10.1016/j.dam.2022.09.011.
2. Y. Caro, M. Petruševski, R. Škrekovski, “Remarks on proper conflict-free colorings of graphs,” arXiv:2203.01088v1, first public version 2 March 2022; Discrete Mathematics 346(2) (2023), 113221, DOI 10.1016/j.disc.2022.113221.
3. J. Anderson, H. Chau, E.-K. Cho, N. Crawford, S. G. Hartke, E. Heath, O. Henderschedt, H. Kwon, Z. Zhang, “The forb-flex method for odd coloring and proper conflict-free coloring of planar graphs,” arXiv:2401.14590v1, first public version 26 January 2024.
