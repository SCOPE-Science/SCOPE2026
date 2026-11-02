# Optimal odd-order completions of finite partial permutations

## Finding
Let \(X\) be any finite, possibly empty, labelled set and \(p:X\rightharpoonup X\) be a partial bijection. An *odd-order completion* is a permutation \(g\) of a finite superset \(Y\supseteq X\) whose order is odd and which satisfies \(g(x)=p(x)\) for each \(x\in\operatorname{dom}(p)\). Odd order is not the sign of a permutation: it means that *every* cycle length is odd.

Each connected component of the graph of \(p\) is a directed cycle or a directed path; an isolated vertex is a path of length one **vertex**. Write \(a\) for the number of open paths with odd numbers of vertices, and \(b\) for those with even numbers of vertices. Existing directed cycles cannot be altered in a completion. If any such cycle has even length, no odd-order completion exists, regardless of how many new vertices are allowed.

Assume all existing directed cycles have odd length. Then the sharp minimum number of additional vertices is
\[
 m(p)=\begin{cases}0,&a>0\text{ or }a=b=0,\\1,&a=0<b.\end{cases}
\]
The exact number \(N_{a,b}\) of odd-order completions on the *original* labelled ground set \(X\) is
\[
 N_{0,0}=1,\qquad N_{0,b}=0\ (b\ge1),\qquad
 N_{a,b}=c_a\,\frac{(a+b-1)!}{(a-1)!}\ (a\ge1),
\]
with
\[
 c_{2h}=((2h-1)!!)^2\ (h\ge1),\qquad
 c_{2h+1}=(2h+1)!!(2h-1)!!\ (h\ge0),
\]
and \((-1)!!=1\). Thus the answer depends only on the *parities of the open path sizes*, not on their individual sizes, nor on the lengths or number of existing odd cycles.

The corresponding two-sort exponential generating function is
\[
 \sum_{a,b\ge0}N_{a,b}\frac{x^a y^b}{a!b!}
 =\sqrt{\frac{1-y+x}{1-y-x}}.
\]
If \(a=0<b\), then on each prescribed labelled one-point extension \(X\cup\{z\}\) there are **exactly \(b!\)** odd-order completions, and every such completion merges all open paths and \(z\) into one odd cycle.

## Assumptions and scope
All finite sets and partial maps are labelled, and extensions are counted as genuinely distinct permutations (not up to conjugacy). The source and target of the partial injection are subsets of the same set \(X\). An unassigned singleton is counted as an open one-vertex path; fixed points already specified are closed one-cycles. The completed permutation may connect endpoints of different paths but cannot change prescribed arrows of \(p\). Counted one-point extensions use a *fixed* new label \(z\).

## Proof
**1. Structural rigidity and path-component correspondence.** A closed component of \(p\) already has prescribed outgoing and incoming arrows at every vertex, hence is unchanged by any extension. An even such cycle is therefore a permanent obstruction. Any remaining open component is a unique ordered directed path. On \(X\), completing each path's terminal outgoing arrow must join it to the initial vertex of another path (possibly itself), and each initial vertex must receive exactly one such arrow. Consequently completions on \(X\) are in bijection with permutations \(\sigma\) of the \(a+b\) individually labelled open path components. Each cycle of \(\sigma\) concatenates those paths in their forced orientations; its total vertex length is odd exactly when that cycle contains an odd number of the \(a\) odd-size components. This is the only constraint.

**2. Count the odd components.** First take \(b=0\). Every cycle of the component permutation must have odd length, so the standard exponential formula gives
\[
 C(x)=\sum_{a\ge0}c_a\frac{x^a}{a!}
 =\exp\left(\sum_{j\ge0}\frac{x^{2j+1}}{2j+1}\right)
 =\sqrt{\frac{1+x}{1-x}}.
\]
Coefficient extraction, or the recurrence from \((1-x^2)C'(x)=C(x)\), yields \(c_0=c_1=1\), \(c_{2h}=((2h-1)!!)^2\), and \(c_{2h+1}=(2h+1)!!(2h-1)!!\). In particular, \(c_a>0\) for every \(a\ge1\).

**3. Insert the even components.** Fix a permutation of the \(a\) odd components with every cycle odd. Insert the even components in a fixed order of their labels. Immediately before inserting the \((j+1)\)-st even component, there are exactly \(a+j\) directed gaps between consecutive path components in the cycles. Inserting the even-size component into any gap preserves odd total vertex length in that cycle. Conversely, deleting the even components in reverse label order from any admissible completion recovers a unique odd-cycle permutation of the \(a\) odd components and a unique sequence of insertion gaps: no admissible cycle can consist solely of even-size components. This is a bijection, so the number is
\[
 c_a\,a(a+1)\cdots(a+b-1)
 =c_a\frac{(a+b-1)!}{(a-1)!}.
\]
When \(a=0<b\), every possible component cycle has even vertex length, so no completion exists on \(X\). If there are no paths, the existing odd cycles are already a unique permutation, giving \(N_{0,0}=1\). Summing the insertion formula over \(b\) gives
\[
 \sum_{a,b\ge0}\frac{N_{a,b}}{a!b!}x^a y^b
 =C\!\left(\frac{x}{1-y}\right)
 =\sqrt{\frac{1-y+x}{1-y-x}}.
\]

**4. Sharp one-new-vertex repair.** In the remaining case \(a=0<b\), adjoin a fresh vertex \(z\), an odd path component of size one, and concatenate *all* \(b\) even paths with \(z\) in one directed cycle. Its total length \(1\) plus an even sum is odd. Thus one point suffices, whereas Step 3 proves zero points impossible. In *every* minimal completion, each component cycle must contain an odd number of odd-size components. Since \(z\) is the sole odd-size component, every original path must be in the one cycle containing \(z\). Holding \(z\) as a distinguished starting position, an arbitrary ordering of the \(b\) path components gives one completion, and all arise this way. Therefore precisely \(b!\) minimal completions exist on the given \(X\cup\{z\}\).

## Verification
The standalone Python 3 checker `checker.py` reconstructs the directed component structure independently of the formula, enumerates all injective partial maps on labelled sets of sizes zero through five, and counts all extending odd-order permutations by direct permutation enumeration. It then verifies the one-new-vertex multiplicity for sizes zero through four. It compares the double-factorial closed form against independent cycle enumeration and checks the bivariate counts by a recursive distinguished-cycle decomposition. Reproduce with `python3 checker.py`; the expected terminal marker is `ALL_CHECKS_OK`. Finite checks are not a substitute for the bijective proof.

## Relationship to prior work
Etedadialiabad and Gao, *Extension Properties for Partial Permutations*, arXiv:2610.04870v1, Section 3.5, Lemma 3.12, establish existence of prime-restricted completions for one partial permutation by closing each path after adding sufficiently many vertices. This work addresses **optimal additional ground-set size, complete exact representation multiplicities, and the parity-profile invariant** for the odd-order case; it does not assert new group-extension existence results for two or more generators. The known numbers of permutations with exclusively odd cycles are used as the baseline \(c_a\), consistent with Adin--Hegedűs--Roichman, arXiv:2502.03507v1, Section 1. Claesson--Jelínek--Jelínková--Kitaev, arXiv:1005.2216, treat a different notion of partial permutation as a word with holes and study pattern avoidance.

## Limitations
The theorem covers one partial bijection and odd order, not simultaneous completions of multiple partial bijections, arbitrary prime restrictions, or quotienting completions by relabellings. The all-odd-cycle enumeration \(c_a\) is classical, not independently novel. Equivalence to an unlocated classical prescribed-arcs enumeration remains a literature risk. The computations exhaust only the stated small finite domains. No independent scientific audit has been carried out.

## References
- M. Etedadialiabad and S. Gao, *Extension Properties for Partial Permutations*, arXiv:2610.04870v1 (first posted 2026-10-04), especially Lemma 3.12: https://arxiv.org/html/2610.04870v1 .
- R. M. Adin, P. Hegedűs, and Y. Roichman, *Descent set distribution for permutations with cycles of only odd or only even lengths*, arXiv:2502.03507v1 (2025), Section 1: https://arxiv.org/html/2502.03507v1 .
- A. Claesson, V. Jelínek, E. Jelínková, and S. Kitaev, *Pattern avoidance in partial permutations*, arXiv:1005.2216 (2010): https://arxiv.org/abs/1005.2216 .
