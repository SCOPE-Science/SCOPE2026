# Exact finite-model census and automorphism universality for two constant-composite projections

## Finding
For each integer \(n\ge1\), the number \(L_n\) of ordered pairs of functions \(f,g:[n]\to[n]\) obeying
\[
f^2=f,\qquad g^2=g,\qquad f\circ g=g\circ f=c_r
\]
for some constant map \(c_r\) is
\[
\boxed{L_n=n\sum_{\substack{a,b,c\ge0\\a+b+c=n-1}}\frac{(n-1)!}{a!b!c!}\bigl((a+1)(b+1)\bigr)^c.}
\]
The initial values at \(n=1,\ldots,8\) are \(1,6,39,300,2785,30798,398097,5912056\). An exact invariant classifies every isomorphism class and determines its full automorphism group. Despite the simple unary identities, **every finite group** occurs as one of those full automorphism groups; replacing the two operators by a single idempotent operator destroys this universality.

## Assumptions and scope
Work with nonempty finite sets in the ordered signature of two unary operations; automorphisms must preserve \(f\) and \(g\) individually. Composition is right-to-left, so \(f\circ g\) sends \(x\) to \(f(g(x))\). The common composite is required to be a constant map, but its value \(r\) is not named by an additional constant symbol: the operations determine it. Counts are for **labeled** carriers, not isomorphism classes; the finite-group assertion concerns abstract full automorphism groups.

Put \(A=\operatorname{Fix}(f)\setminus\{r\}\), \(B=\operatorname{Fix}(g)\setminus\{r\}\), and \(C=X\setminus(A\cup B\cup\{r\})\). For \(u\in A\cup\{r\}\), \(v\in B\cup\{r\}\), define \(m_{uv}=|\{x\in C:f(x)=u,\ g(x)=v\}|\). Write \(H_m\) for the permutations of non-root rows and non-root columns that preserve all entries \(m_{uv}\), keeping root row and column fixed.

## Proof
**1. Canonical decomposition.** Because \(f\circ g\) is the constant map with value \(r\), \(f(r)=f(f(g(x)))=f(g(x))=r\) for any \(x\). Similarly \(g(r)=r\). If \(f(x)=x\), then \(g(x)=g(f(x))=r\) because \(g\circ f=c_r\); hence any fixed point of \(f\) other than \(r\) lies outside \(\operatorname{Fix}(g)\). The dual holds for \(g\). If \(x\in C\), idempotence puts \(f(x)\) among the fixed points of \(f\), and \(g(x)\) among the fixed points of \(g\). Thus the displayed partition and ordered pair of targets are forced by the functions.

Conversely, take disjoint finite \(\{r\},A,B,C\) and any \(\alpha:C\to A\cup\{r\}\), \(\beta:C\to B\cup\{r\}\). Set \(f\) equal to the identity on \(\{r\}\cup A\), to \(r\) on \(B\), and to \(\alpha\) on \(C\). Set \(g\) equal to the identity on \(\{r\}\cup B\), to \(r\) on \(A\), and to \(\beta\) on \(C\). Both are idempotent and both compositions map every element to \(r\). Points of \(C\) are fixed by neither operation because \(\alpha(C)\cap C=\beta(C)\cap C=\varnothing\), so this inverse construction recovers precisely the original decomposition. It also works if some of the three sets are empty.

**2. Exact labeled enumeration.** Choose \(r\) in \(n\) ways. Given nonnegative \(a,b,c\) with \(a+b+c=n-1\), choose ordered disjoint subsets \(A,B,C\) of these sizes in \((n-1)!/(a!b!c!)\) ways. Independently for each of the \(c\) elements choose one of the \((a+1)(b+1)\) pairs of permitted targets. The decomposition is unique, so there is no overcount. Summing proves the exact formula. Its exponential generating function is the locally finite formal series
\[
\sum_{n\ge1}L_n\frac{z^n}{n!}=z\sum_{a,b\ge0}\frac{z^{a+b}}{a!b!}\exp((a+1)(b+1)z).
\]

**3. Isomorphism and automorphisms.** Any isomorphism must fix the unique composite point \(r\), carry \(A\) to \(A\), \(B\) to \(B\), and \(C\) to \(C\), and carry each fiber \(\{x\in C:(f(x),g(x))=(u,v)\}\) to the fiber for the images of \(u,v\). Thus isomorphism is exactly equality of the matrix \((m_{uv})\) up to row permutations of \(A\) and column permutations of \(B\); the root row and column are fixed. Conversely every such matrix equivalence extends to a structure isomorphism by arbitrary bijections of corresponding fibers. Choosing bijections to index each fiber gives the (noncanonical) semidirect-product decomposition
\[
\operatorname{Aut}(X;f,g)\cong\left(\prod_{u\in A\cup\{r\},\ v\in B\cup\{r\}}S_{m_{uv}}\right)\rtimes H_m.
\]
Here \(S_0\) and \(S_1\) mean the trivial group.

**4. Universal finite automorphism groups.** By the classical Frucht theorem, for any finite group \(G\) there is a finite connected simple cubic graph \(\Gamma=(V,E)\) with \(\operatorname{Aut}(\Gamma)\cong G\). Introduce a distinguished point \(r\), an \(f\)-fixed point \(a_v\) for each graph vertex \(v\), a \(g\)-fixed point \(b_e\) for each graph edge \(e\), and a point \(c_{v,e}\) for each incidence \(v\in e\). Put \(f(c_{v,e})=a_v\) and \(g(c_{v,e})=b_e\) and define all other values according to step 1. Since \(\Gamma\) is simple, each positive incidence fiber has size one; each edge point has exactly the two incident points in its \(g\)-fiber, and no non-incidence fibers exist. Consequently automorphisms of the two-function structure are uniquely the induced graph automorphisms. Its size is \(1+|V|+3|E|\).

For comparison, an idempotent single unary function \(h\) partitions its domain into rooted stars (one at each fixed point). Every nontrivial automorphism of such a structure forces either at least two equal-sized rooted stars, whose exchange is an involution, or at least two leaves on one star, whose transposition is an involution. Thus its automorphism group is either trivial or of even order. In particular it cannot be a cyclic group of order three. This proves the sharp two-versus-one assertion within the idempotent-only signature.

## Verification
A standalone standard-library checker independently enumerates all functions on carriers of sizes \(1\) through \(4\), filters by idempotence and rank-one commuting composite, and compares the resulting counts with the closed formula: \(1,6,39,300\). It also compares automorphism groups of several small incidence-graph constructions with direct permutation enumeration, including a three-vertex path. Run `python checker.py`. The program prints `ALL_CHECKS_OK` on success. The proof above, not the finite computations, establishes the formula for all \(n\) and all finite groups.

## Relationship to prior work
Kuželka (2026), *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting* (arXiv:2608.30580, first public August 31, 2026), studies general first-order model-counting problems with unary functions, including hardness with two functions and automorphism marking. It does not give this restricted constant-composite enumeration or the two-projection realization theorem in the inspected Sections 1, 2, 4, 5 and 8.4. Liao (2026), *A note on ultrahomogeneous unary algebras* (arXiv:2607.02725, first public July 2, 2026), uses a pair of unary maps for homogeneity questions; its inspected Sections 2–3 have different hypotheses and goals. Quinn-Gregson (2026), *Ultrahomogeneity and ω-categoricity of monounary algebras* (arXiv:2603.26616, first public March 27, 2026), classifies homogeneity properties for one map, not these pairs. Frucht's classical graph-automorphism theorem is used explicitly and is **not claimed as new**. General commuting-function counts are already documented, including OEIS A181162, but do not state the extra idempotent and constant-composite restrictions.

## Limitations
The result is for exactly two **ordered** idempotent operations with a **single-point** common composite on **finite nonempty** carriers. No asymptotic estimate, efficient algorithm for counting unlabeled types, or best possible carrier size for realizing a given finite group is asserted. The universal-group construction relies on the established Frucht theorem. A historical classification of finite actions of a four-element semilattice, or an equivalent incidence-structure enumeration under older terminology, could already imply the formula or group conclusion; that priority risk requires independent specialist assessment. The result has undergone an internal self-review only, not an independent audit.

## References
1. O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580 (2026), https://arxiv.org/abs/2608.30580 .
2. C. Liao, *A note on ultrahomogeneous unary algebras*, arXiv:2607.02725 (2026), https://arxiv.org/abs/2607.02725 .
3. T. Quinn-Gregson, *Ultrahomogeneity and omega-categoricity of monounary algebras*, arXiv:2603.26616 (2026), https://arxiv.org/abs/2603.26616 .
4. R. Frucht, *Graphs of degree three with a given abstract group*, Canadian Journal of Mathematics 1 (1949), 365–378.
5. OEIS A181162, *Number of commuting functions*, https://oeis.org/A181162 .
