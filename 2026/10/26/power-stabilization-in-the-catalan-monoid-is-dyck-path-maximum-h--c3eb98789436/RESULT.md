# Power stabilization in the Catalan monoid is Dyck-path maximum height

## Finding
For every integer \(n\ge1\), let \(C_n\) consist of all maps \(f:[n]\to[n]\) satisfying \(f(1)\le\cdots\le f(n)\) and \(f(i)\le i\). This is the Catalan transformation monoid, with composition. Define the *power-stabilization depth*
\[
s(f)=\min\{k\ge0:f^{k+1}=f^k\}.
\]
There is a bijection from \(C_n\) to Dyck paths of semilength \(n\) with
\[
\boxed{s(f)=\operatorname{height}(D_f)-1.}
\]
Here height is the largest number of unmatched opening parentheses (equivalently, maximum upward excursion). In particular the complete multiplicity of each possible stabilization depth is the corresponding classical bounded-height Dyck-path difference, not merely the total Catalan cardinality.

For every integer \(k\ge0\), put \(a_{n,k}=|\{f\in C_n:s(f)\le k\}|\) and \(F_k(z)=\sum_{n\ge0} a_{n,k}z^n\), with the unique empty transformation counted at \(n=0\). Then
\[
\boxed{F_0(z)=\frac1{1-z},\qquad F_k(z)=\frac1{1-zF_{k-1}(z)}\quad(k\ge1).}
\]
The number having depth exactly \(k\ge1\) is \([z^n](F_k-F_{k-1})\); at depth zero it is \([z^n]F_0=1\). All values \(0,\ldots,n-1\) occur for \(n\ge1\). The top depth \(n-1\) is attained uniquely by the map \(f(1)=1\), \(f(i)=i-1\) for \(i>1\).

For \(n\ge1\), direct consequences are
\[
\boxed{a_{n,1}=2^{n-1},\qquad a_{n,2}=\operatorname{Fib}_{2n-1},\qquad a_{n,3}=\frac{3^{n-1}+1}{2}.}
\]
Here \(\operatorname{Fib}_0=0\), \(\operatorname{Fib}_1=1\), and \(\operatorname{Fib}_{m+2}=\operatorname{Fib}_{m+1}+\operatorname{Fib}_m\). For each fixed \(k\ge0\), the cumulative frequency has exponential growth \(\Theta_k(\lambda_k^n)\), where
\[
\boxed{\lambda_k=4\cos^2\!\left(\frac{\pi}{k+3}\right).}
\]

## Assumptions and scope
No field, characteristic, or additional structure is required. Composition powers use the convention \(f^0=\operatorname{id}\). Since \(f(i)\le i\), iterates cannot have nontrivial cycles; they eventually fix each point, so \(s(f)\) is well-defined. A plane rooted forest means an ordered list of rooted ordered trees. Its number of vertices is \(n\). Each forest is encoded by its standard depth-first balanced-parenthesis word, with one matching pair per vertex.

## Proof
**1. Canonical fixed-point blocks.** All maps in \(C_n\) fix \(1\). Let their fixed points in increasing order be \(r_1=1<r_2<\cdots<r_t\), and put \(r_{t+1}=n+1\). For each interval \(B_j=[r_j,r_{j+1}-1]\), monotonicity gives \(f(i)\ge f(r_j)=r_j\); order decrease gives \(f(i)\le i\). Therefore \(f(B_j)\subseteq B_j\), and the unique fixed point in \(B_j\) is its left endpoint. For every nonroot \(i\in B_j\), we have \(r_j\le f(i)<i\).

**2. Bijection to plane forests.** Within each block, draw the edge from \(i\) to its parent \(f(i)\), ordered children by their vertex labels. The parent labels \(f(i)\) form a weakly increasing sequence as \(i\) ranges over nonroots. Consequently all children of smaller-labeled vertices precede all children of larger-labeled vertices, so labels within each block occur in *breadth-first* (queue) order. This constructs one plane rooted tree per block, hence an ordered plane forest. Conversely, list the trees of a plane forest in order, assign consecutive integer labels in breadth-first order separately within each tree, and define \(f(i)\) to be the parent label or the label itself when \(i\) is a root. Within any tree, parent labels are weakly increasing and smaller than their children; across successive trees, old parent labels are less than the next root. Thus the resulting map belongs to \(C_n\). These operations are inverse, giving a bijection for every \(n\).

**3. Exact power index.** In the constructed forest, applying \(f\) moves each nonroot one edge toward its root and fixes the root. A vertex at distance \(d\) from its root first reaches that root after exactly \(d\) iterations. Hence \(s(f)\) is exactly the largest edge-distance of any vertex to its root. Standard depth-first parentheses for the forest reach nesting depth \(d+1\) at such a vertex; the Dyck maximum height is exactly \(s(f)+1\), proving the statistic-preserving bijection.

**4. Rational generating functions.** A forest of maximal edge-depth at most \(k\) is an arbitrary sequence of rooted plane trees whose root-child forests have maximal edge-depth at most \(k-1\). For \(k=0\), only isolated roots occur, giving \(F_0=(1-z)^{-1}\). For \(k\ge1\), each tree is a root (one vertex, factor \(z\)) carrying a forest counted by \(F_{k-1}\), and an arbitrary sequence of such trees has series \((1-zF_{k-1})^{-1}\). The coefficient differences give the exact distribution.

**5. Closed low-depth families.** The first three nontrivial iterates are
\[
F_1=\frac{1-z}{1-2z},\qquad
F_2=\frac{1-2z}{1-3z+z^2},\qquad
F_3=\frac{1-3z+z^2}{1-4z+3z^2}.
\]
Their positive-degree coefficients are, respectively, \(2^{n-1}\), \(\operatorname{Fib}_{2n-1}\), and \((3^{n-1}+1)/2\). The top-depth statement follows since a rooted forest on \(n\) vertices has depth \(n-1\) only if it is a single directed chain, which yields the unique stated map.

**6. Fixed-depth asymptotics.** Bounded-height Dyck words have a standard transfer matrix: a walk with up/down steps on height states \(0,\ldots,k+1\), beginning and ending at state zero. Let \(A_{k+2}\) be the path-graph adjacency matrix on these \(k+2\) states. The cumulative count is \((A_{k+2}^{2n})_{0,0}\). Its eigenvalues are \(2\cos(j\pi/(k+3))\), for \(1\le j\le k+2\). The positive/negative dominant pair yields exponential rate \(\lambda_k=4\cos^2(\pi/(k+3))\) and a strictly positive leading constant, as claimed.

## Verification
The included standard-library verifier `verify.py` enumerates every nondecreasing regressive map for each \(1\le n\le10\), independently computes its power depth, reconstructs its forest and Dyck path, and tests the height identity, the Catalan totals, all cumulative generating-function coefficients and the displayed closed formulas. For example the exact-depth arrays for \(n=5\) and \(n=8\) are \((1,15,18,7,1)\) and \((1,127,482,484,247,75,13,1)\). Output ends in `VERIFY_OK_CATALAN_POWER_STABILIZATION`. Exhaustive finite verification is corroboration, not proof of all-order statements.

## Relationship to prior work
The Catalan monoid, the fact that its size is a Catalan number, its known idempotent count, and classical enumeration of bounded-height Dyck paths are all prior mathematics. Ganyushkin–Mazorchuk (arXiv:1006.0316, sections 1–4) identify the same monoid through type-\(A\) Hecke–Kiselman quotients and study its representations and idempotents. Grensing–Mazorchuk (arXiv:1211.2597, sections 1–5) study its categorification. Laradji–Umar treat other order-preserving transformation/lattice-path enumerations. The precise claim here is the power-index-preserving *breadth-first forest correspondence*, yielding the entire infinite stabilization-depth distribution and its exponential rates. The inspected primary texts did not explicitly make this joint identification; an equivalent hidden in older Catalan correspondences or semigroup-power literature remains a priority risk.

## Limitations
No claim about arbitrary nonmonotone transformations, partial transformations, or order-increasing conventions without duality is made. The low-depth coefficient sequences and Dyck height enumeration are classical on their own. Exhaustive searches cannot certify historical uniqueness; an older inaccessible Solomon research report could contain a related correspondence. Independent audit has not been performed.

## References
- O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, arXiv:1006.0316 (first arXiv version dated 2010-06-02), especially the Catalan monoid identification in Section 1 and the representation/enumeration sections; https://arxiv.org/html/1006.0316v3.
- A.-L. Grensing and V. Mazorchuk, *Categorification of the Catalan monoid*, arXiv:1211.2597 (first arXiv version dated 2012-11-12); https://arxiv.org/html/1211.2597v2.
- A. Laradji and A. Umar, *Lattice Paths and Order-preserving Partial Transformations*, full-text article available at https://www.researchgate.net/publication/236455871_Lattice_Paths_and_Order-preserving_Partial_Transformations.
- A. Solomon, *Catalan monoids, monoids of local endomorphisms, and their presentations*, Research Report 95-6 (1995), abstract accessible at https://ns.maths.usyd.edu.au/u/ResearchReports/Algebra/Sol/cat-mon-end.html.
