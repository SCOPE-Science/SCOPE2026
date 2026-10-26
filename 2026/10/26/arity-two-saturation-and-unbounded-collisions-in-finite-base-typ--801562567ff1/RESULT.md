# Arity-two saturation and unbounded collisions in finite-base type spectra of the countable grid

## Finding

Let \(M=\mathbb N\times\mathbb N\) carry the two named equivalence relations
\(E((i,j),(i',j'))\iff i=i'\) and
\(F((i,j),(i',j'))\iff j=j'\).
For a finite nonempty parameter set \(A\subset M\), let \(m=|A|\), let
\(r\) be the number of \(E\)-classes meeting \(A\), and let \(c\) be the
number of \(F\)-classes meeting \(A\). Define \(t_k(A)\), for every integer
\(k\geq 0\), to be the number of complete types over the individually named
parameters \(A\) in ordered variables \((x_1,\ldots,x_k)\), where the variables
are pairwise distinct and distinct from all parameters. Set \(t_0(A)=1\).

Write \(B_h\) for the \(h\)-th Bell number, \(B_0=1\), and let
\(s(k,j)\) denote the signed Stirling number of the first kind. Set
\[
a_h(v)=\sum_{d=0}^{h}\binom hd v^d B_{h-d}\qquad(h,v\geq0).
\]
Then for every \(k\geq0\) the complete numerical spectrum is
\[
\boxed{\displaystyle
 t_k(A)=\sum_{j=0}^{k}s(k,j)
 \sum_{\ell=0}^{j}(-1)^\ell\binom j\ell m^\ell
 a_{j-\ell}(r)a_{j-\ell}(c).}
\]
In particular,
\[
\boxed{t_1(A)=(r+1)(c+1)-m,}
\]
\[
\boxed{t_2(A)=t_1(A)(t_1(A)-1)+(r+1)^2+(c+1)^2+1.}
\]
For finite nonempty \(A,A'\) of the **same cardinality** \(m\), the
following are equivalent: their first two counts agree; all their counts
\(t_k\) agree; and the unordered pairs of support sizes
\(\{r,c\}\) agree. Thus every higher numerical count is determined by just
the first two together with the known parameter cardinality.

This complete numerical invariant is not a complete invariant of the
finite parameter structure. Even after fixing the **ordered** support sizes
\((r,c)\), the smallest nonisomorphic collision has \(m=4\): the two
four-cell patterns
\[
A_1=\{(0,0),(0,1),(0,2),(1,0)\},\qquad
A_2=\{(0,0),(0,1),(1,1),(1,2)\}
\]
have the same \((m,r,c)=(4,2,3)\), and hence the same spectrum
\[
(t_0,t_1,t_2,t_3,t_4)=(1,8,82,1067,17108),
\]
but their row-degree multisets are respectively \(\{3,1\}\) and
\(\{2,2\}\). The incidence patterns are therefore nonisomorphic with the
two equivalence relations kept named. For every \(n\ge2\), there are
**exactly** \(\lfloor(n-1)/2\rfloor+1\) nonisomorphic finite patterns
with \((m,r,c)=(n+1,2,n)\), and all share their entire numerical spectrum.
The collision fibers are therefore unbounded.

## Assumptions and scope

The ambient structure is the full countably infinite grid with **two
separately named**, perpendicular equivalence relations. Each intersection
of an \(E\)-class and an \(F\)-class contains exactly one point. Types are
complete first-order types of pairwise distinct **new** elements over all
individually named elements of the finite base. The cardinality \(m\) is
assumed known when asserting determination by the first two counts. There
are no restrictions on the finite incidence pattern beyond distinct cells.
The statement about the minimal four-point collision holds only when the
ordered pair of support sizes is fixed; interchanging the names \(E,F\)
can already produce a two-point collision in the unrestricted comparison.

## Proof

**1. Homogeneity and stabilizers.** Every automorphism of \(M\) is a
separate permutation of its first and second coordinates, so
\(\operatorname{Aut}(M)=\operatorname{Sym}(\mathbb N)\times
\operatorname{Sym}(\mathbb N)\) in product action. Conversely every finite
partial isomorphism determines consistent partial injections on the row and
column sets, which extend to permutations. Thus \(M\) is homogeneous and
its finite complete tuple types coincide with automorphism orbits. A
permutation fixing \(A\) pointwise must fix each of its \(r\) used rows
and each of its \(c\) used columns, and this is sufficient. Its stabilizer
therefore depends on the used coordinate sets, not on which of the
\(r c\) possible intersections occur in \(A\).

**2. Arbitrary ordered tuples.** Under the infinite symmetric group fixing
\(v\) distinguished points, an arbitrary ordered \(h\)-tuple is described
by selecting \(d\) coordinates to take values among those distinguished
points (\(v^d\) choices), and an equality partition on the other
\(h-d\) positions (\(B_{h-d}\) choices). Consequently this action has
exactly \(a_h(v)\) orbits. Independent row and column actions give exactly
\(f_h=a_h(r)a_h(c)\) orbits on all of \(M^h\), allowing repetitions and
occurrences of parameters.

**3. Forbidding parameters.** Each point of \(A\) is fixed separately.
By inclusion-exclusion on the coordinates required to avoid \(A\), the
number of orbits on \((M\setminus A)^h\), still allowing repetitions, is
\[
 g_h=\sum_{\ell=0}^{h}(-1)^\ell\binom h\ell
 m^\ell f_{h-\ell}.
\]
Indeed, after choosing \(\ell\) positions that must equal members of
\(A\), there are exactly \(m^\ell\) ordered choices of their fixed
values, with the remaining positions unrestricted; no quotient identifies
distinct fixed values.

**4. Removing repetitions.** The equality pattern of an arbitrary
\(h\)-tuple is a set partition into \(j\) blocks; its ordered distinct
values contribute one of the \(t_j(A)\) orbits. Therefore
\(g_h=\sum_j S(h,j)t_j(A)\), where \(S(h,j)\) denotes Stirling numbers
of the second kind. Inversion using signed Stirling numbers yields the
boxed all-arity identity. For \(h=1,2\), use
\(a_1(v)=v+1\) and \(a_2(v)=(v+1)^2+1\) to obtain the two displayed
small-arity formulas.

**5. Exact arity-two determination.** Put \(u=r+1\) and \(v=c+1\).
Given the parameter cardinality \(m\) and the first two counts,
\[
 p:=t_1+m=uv,\qquad
 q:=t_2-t_1(t_1-1)-1=u^2+v^2.
\]
Hence \(u+v=\sqrt{q+2p}\) and \(u,v\) are precisely the two positive
roots of \(z^2-\sqrt{q+2p}\,z+p=0\). Thus \(\{r,c\}\) is recovered.
The all-arity identity is symmetric in \(r,c\), proving the equivalence.

**6. The sharp collision and unbounded fibers.** Regard \(A\) as the
edge set of a bipartite graph whose vertices are its used rows and columns.
Every vertex is incident with an edge. A simple bipartite graph having at
most three edges and no isolated vertex is, once the two side sizes are
specified, unique up to permutations within the sides: its components are
single edges, a two-edge star, or a three-edge path/star. Thus no
same-\((r,c)\) nonisomorphic collision occurs for \(m\le3\). The two
four-edge patterns displayed above have different row-degree multisets,
proving sharpness. More generally, take \(r=2\), \(c=n\), and
\(m=n+1\). Exactly one column is incident with both rows and every other
column with just one. If \(d\) of those remaining \(n-1\) columns are
incident with the first row, row exchange sends
\(d\mapsto n-1-d\). The distinct side-preserving isomorphism classes are
therefore precisely the orbits of this involution, numbering
\(\lfloor(n-1)/2\rfloor+1\). All have identical counts by Step 4.

## Verification

The standalone standard-library checker `code/check_grid.py` calculates
the Bell/Stirling formula independently of canonical finite row/column
orbit-word enumeration. It checks both four-cell witnesses directly in
arities zero through four; enumerates every bipartite incidence class of
at most three edges with prescribed side sizes to establish the finite
minimality certificate; and checks first-two-type reconstruction in
additional examples. Run `python code/check_grid.py` from this directory.
The expected output is included in `verification/check_output.txt`. Finite
checks corroborate, but do not replace, the all-size group-action proof.

## Relationship to prior work

Cameron's 2000 exposition establishes the general connection between
oligomorphic orbits and complete types, Bell-number and Stirling-transform
methods, the product action of infinite symmetric groups, and stabilizer
operations. It also identifies the **unlabelled** finite-grid orbit
problem with bipartite graph enumeration. The present theorem instead
concerns **finite-base, individually named, nonalgebraic tuple types**;
it classifies their entire numerical equivalence relation, its arity-two
saturation, and its smallest and unbounded collision fibers. These
specific conclusions were not found in the compared primary sources.
Applegate and Cameron's 2009 paper proves general orbit-growth lower
bounds and equality conditions; it does not assert the finite-base grid
profile or the collision classification. The simple symmetric-group
calculus is prior mathematics, not claimed as novel.

## Limitations

This result addresses a specially structured homogeneous model, not
arbitrary structures with two equivalence relations. The all-arity
spectrum is a **numerical** invariant: it must not be confused with the
actual sets of types, their formula labels, or a reconstruction of the
base's bipartite incidence graph. The two-count implication requires
bases of equal known cardinality. Bibliographic searches cannot exclude
unindexed or implicitly equivalent literature; no independent scientific
audit has been performed.

## References

1. P. J. Cameron, *Sequences Realized by Oligomorphic Permutation Groups*,
   Journal of Integer Sequences **3** (2000), Article 00.1.5,
   https://cs.uwaterloo.ca/journals/JIS/VOL3/groups.html
   (online publication noted there as 2000-01-25).
2. R. Applegate and P. J. Cameron, *Orbits on n-Tuples*, Communications in
   Algebra **37** (2009), 269–275, DOI 10.1080/00927870802243739;
   author preprint https://webspace.maths.qmul.ac.uk/p.j.cameron/preprints/orbitpaper.pdf
