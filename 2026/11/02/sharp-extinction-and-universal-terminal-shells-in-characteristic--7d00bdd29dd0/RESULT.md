# Sharp extinction and universal terminal shells in characteristic-divisible rooted-tree dynamics

## Finding

**Theorem (universal terminal extinction shells).** Let \(T\) be a finite, rooted, undirected tree of height \(h\ge1\) and order \(N\). Let \(\mathbb F_q\) be a finite field of characteristic \(p\). Suppose every nonleaf vertex has a number of children divisible by \(p\). For a configuration \(x\in\mathbb F_q^{V(T)}\), use the synchronous nearest-neighbor sum update
\[
(Fx)_v=\sum_{w\sim v}x_w
\]
with arithmetic in \(\mathbb F_q\). Then \(F\) is nilpotent with **exact** index \(2h+1\). Indeed,
\[
\operatorname{rank}(F^{2h-1})=2,\qquad
\operatorname{rank}(F^{2h})=1,\qquad F^{2h+1}=0.
\]
The zero configuration is the only periodic configuration. If \(x\) is chosen uniformly from all \(q^N\) configurations and \(\tau(x)=\min\{t\ge0:F^t x=0\}\), then
\[
\Pr(\tau\le2h-1)=q^{-2},\quad
\Pr(\tau=2h)=q^{-1}-q^{-2},\quad
\Pr(\tau=2h+1)=1-q^{-1}.
\]
In particular, these last two shell probabilities depend **only** on the field size, not on branching or tree shape. At time \(2h\) the entire nonzero output, if any, lies on the deepest level, with equal values at all vertices of that level.

**Sharp branching dichotomy for complete trees.** For integers \(d\ge2\), \(h\ge1\), on the complete rooted \(d\)-ary tree of height \(h\), this neighbor-sum dynamics is globally extinguishing if and only if \(p\mid d\). If \(p\nmid d\), nonzero configurations with nonextinguishing trajectories exist.

## Assumptions and scope

Trees are finite and simple, children are defined by the chosen root, and height means the maximum number of edges from root to a vertex. The divisibility condition applies to the **number of children**, not to total graph degree. Leaves may occur at different depths. A finite field \(\mathbb F_q\) has \(q\) elements and prime characteristic \(p\). This is a synchronous, loopless, linear neighbor-sum update; it is not a majority rule or a chip-firing rule. Nilpotency index means the least positive integer \(t\) such that \(F^t=0\). The theorem does not claim that the divisibility condition is necessary on all irregular trees; necessity is asserted only in the complete \(d\)-ary family.

## Proof

Let \(e_v\) be the standard basis vector supported at vertex \(v\). Define the two operators \(D,U\) by
\[
D e_v=\sum_{w\text{ a child of }v}e_w,\qquad
U e_v=\begin{cases}e_{\operatorname{parent}(v)},&v\text{ nonroot},\\0,&v\text{ root}.\end{cases}
\]
For undirected adjacency, \(F=D+U\). Since every parent has a number of children that is zero in \(\mathbb F_q\),
\[
UD e_v=(\#\{\text{children of }v\})e_v=0,
\]
so \(UD=0\). The depth bound gives \(D^{h+1}=U^{h+1}=0\). In every word in the noncommutative expansion of \((D+U)^t\), the occurrence of an adjacent \(UD\) kills the word. The only possible surviving words have all \(D\)'s before all \(U\)'s, each occurring once, giving
\[
F^t=\sum_{a+b=t}D^aU^b.
\]
At \(t=2h+1\), every pair \(a+b=2h+1\) has \(a>h\) or \(b>h\). Therefore \(F^{2h+1}=0\).

Write \(v_j=D^j e_r\), where \(r\) is the root. This is the indicator vector of the set of vertices at depth \(j\), and \(v_j\ne0\) for every \(0\le j\le h\). For \(t=2h\) only \((a,b)=(h,h)\) remains, whence \(F^{2h}=D^hU^h\). The map \(U^h\) sends a basis vector at depth \(h\) to \(e_r\), and kills every basis vector at smaller depth. Thus \(F^{2h}\) has the one-dimensional image \(\mathbb F_q v_h\), attained from any vertex at depth \(h\). This proves rank one and exact index.

At \(t=2h-1\), exactly two terms survive:
\[
F^{2h-1}=D^hU^{h-1}+D^{h-1}U^h.
\]
The image is contained in \(\operatorname{span}\{v_h,v_{h-1}\}\). Each input basis vector at depth \(h-1\) is sent to \(v_h\); each input basis vector at depth \(h\) is sent to \(v_{h-1}\). These two output vectors have disjoint nonempty level supports, hence are linearly independent. The rank is exactly two. The formula for the common terminal profile follows from the expression \(F^{2h}=D^hU^h\): its coefficient is the sum of the initial field values over vertices of depth \(h\).

For a linear operator of rank \(r_t\) on an \(N\)-dimensional vector space over \(\mathbb F_q\), precisely \(q^{N-r_t}\) inputs have \(F^t x=0\). Substituting ranks \(2,1,0\) at times \(2h-1,2h,2h+1\) proves the three probabilities by subtraction. A nilpotent map has no nonzero periodic point: if \(F^k x=x\), then sufficiently many repetitions of \(F^k\) send \(x\) both to itself and to zero.

For the dichotomy, if \(p\mid d\), the first assertion applies. Conversely, let \(p\nmid d\). At height one (a star), \(F^2e_r=d e_r\), so no power of \(F\) can vanish. For height at least two, take two of the root's child subtrees and embed any state \(y\) of the complete \(d\)-ary tree of height \(h-1\) as \(y\) on the first subtree and \(-y\) on the second, with zero elsewhere. The root always receives zero, so this is an invariant linear copy of the height-\(h-1\) system. Induction from the height-one star excludes nilpotency for every height. Over a finite field, a nonnilpotent linear map has a trajectory that does not eventually become zero; equivalently it has a nonzero periodic state in its eventual image.

## Verification

A self-contained standard-Python program `verify.py` independently constructs adjacency matrices, computes modular matrix-power ranks, and simulates complete configuration spaces for small trees. It verifies the terminal ranks \((2,1,0)\) for twelve equal- and unequal-depth examples in characteristics two and three, and checks nonextinction in five complete-tree cases with characteristic not dividing the branching factor. Direct exhaustive first-zero times are also checked wherever tractable; run `python3 verify.py`. The included `verify_output.txt` records the successful execution. The proof above, not finite testing, establishes the statements for arbitrary sizes.

## Relationship to prior work

Rojo's 2005 publicly available study of symmetric rooted-tree adjacency spectra treats eigenvalue and determinant questions over the real setting, not finite-field synchronous extinction time or its probability shells. Fritscher and Trevisan's 2016 spectral-decomposition work likewise studies matrix eigenvalue structure. Aledo, Martínez and Valverde's 2015 survey formulates global orbit questions for parallel dynamical systems; it does not supply this tree-specific characteristic-divisibility and sharp terminal-shell law. The present mechanism is the noncommutative factorization \(UD=0\), which works also for asymmetric trees outside balanced Bethe-tree classes. No uniqueness or priority claim beyond the sources inspected is asserted.

## Limitations

Only the final two nontrivial extinction shells and the earlier cumulative mass are given; the theorem does not determine every earlier extinction-time population. The full spectrum and Jordan partition for all these operators are not enumerated. The general-tree condition is sufficient, not claimed necessary. No external independent validation has been performed. The exact comparison to earlier matrix-spectral literature is limited by its different coefficient field and by accessible published material; unindexed equivalent formulations cannot be ruled out.

## References

1. O. Rojo, "On the spectra of certain rooted trees," *Linear Algebra and its Applications* 414 (2006), 218–243, DOI:10.1016/j.laa.2005.09.019. First available online 2005-11-23.
2. O. Rojo and M. Robbiano, "An explicit formula for eigenvalues of Bethe trees and upper bounds on the largest eigenvalue of any tree," *Linear Algebra and its Applications* 427 (2007), 138–150, DOI:10.1016/j.laa.2007.06.024.
3. J. A. Aledo, S. Martínez and J. C. Valverde, "Parallel dynamical systems over graphs and related topics: A survey," *Journal of Applied Mathematics* (2015), 594294, DOI:10.1155/2015/594294. First published 2015-03-24.
4. E. Fritscher and V. Trevisan, "Exploring symmetries to decompose matrices and graphs preserving the spectrum," *SIAM Journal on Matrix Analysis and Applications* 37 (2016), 260–289, DOI:10.1137/15M1013262. First published 2016-03-15.
