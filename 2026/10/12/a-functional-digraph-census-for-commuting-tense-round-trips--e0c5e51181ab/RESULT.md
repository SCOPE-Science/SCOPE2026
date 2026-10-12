# A functional-digraph census for commuting tense round trips

## Finding

Let \(X\) be any nonempty set and \(f:X\to X\) any total function. Interpret future and past possibility on Boolean events \(A\subseteq X\) by
\[
\mathbf F(A)=f^{-1}[A],\qquad \mathbf P(A)=f[A].
\]
Put \(D=f[X]\), \(C=\mathbf F\mathbf P\), and \(I=\mathbf P\mathbf F\). The following conditions are equivalent, without any finiteness or choice assumption:

1. \(C\circ I=I\circ C\) on every subset of \(X\). Equivalently the tense formula \(\mathbf F\mathbf P\mathbf P\mathbf Fp\leftrightarrow\mathbf P\mathbf F\mathbf F\mathbf Pp\) holds for every valuation on the deterministic frame of \(f\).
2. The range is a union of complete fibers: \(f^{-1}[f[D]]=D\).
3. Every two points \(v,w\) with \(f(v)=f(w)\) have the same range-membership status: \(v\in D\) if and only if \(w\in D\).
4. In the directed functional graph (edges \(x\to f(x)\)), all children of each vertex are either all leaves (indegree zero) or all nonleaves (positive indegree).

For \(n\geq1\), let \(a_n\) count these functions on an \(n\)-element labelled set, with the empty-set convention \(a_0=1\). Then the exact exponential generating function is
\[
A(z)=\sum_{n\geq0}a_n\frac{z^n}{n!}=\frac{1}{1-z\exp(u(z))},
\qquad u(z)=z\bigl(\exp(z)+\exp(u(z))-2\bigr),\quad u(0)=0.
\]
This equation specifies a unique formal power series \(u\) with zero constant term. The first coefficients, in order \(n=0,\ldots,10\), are
\[
1,\ 1,\ 2,\ 12,\ 108,\ 1100,\ 13350,\ 194502,\ 3280424,\ 62480952,\ 1328405130.
\]

Let \(\rho\) be the unique positive solution of
\[
1+\rho(\exp(\rho)-2)+\log\rho=0
\]
and put \(B=(1+\rho)\exp(\rho)-2+\rho^{-1}\). Then
\[
a_n\sim\frac{n!\,\rho^{-n}}{\sqrt{2\pi B\rho n}},\qquad
\frac{a_n}{n^n}\sim \frac{1}{\sqrt{B\rho}}\left(\frac{1}{e\rho}\right)^n.
\]
Numerically, \(\rho\approx0.44710445270910068\), \(B\approx2.49956339835460809\), and \(1/(e\rho)\approx0.82280424393535511\). Hence the probability that a uniformly random labelled endofunction has commuting round trips decays exponentially, with this explicit rate.

## Assumptions and scope

The Boolean set operations are performed on the full powerset of \(X\). Future is the unique forward successor operation for the total transition \(f\), while past is the relational converse and may branch. The operations \(C\) and \(I\) are compositions of event transformers; function composition is interpreted right-to-left. For all events,
\[
C(A)=f^{-1}[f[A]],\qquad I(A)=A\cap f[X].
\]
Both are idempotent: \(C^2=C\) and \(I^2=I\). The finite enumerative and asymptotic conclusions apply to labelled finite sets. They do not assert a classification for arbitrary nondeterministic tense relations, or any proof-theoretic completeness result.

## Proof

**Equivalence.** The image–preimage identity for the same total function gives \(I(A)=A\cap D\). The other composite \(C\) sends a set to the union of all \(f\)-fibers meeting it. If \(D\) is a union of such fibers, intersecting with \(D\) before or after this saturation has the same effect:
\[
C(A\cap D)=C(A)\cap D \quad\text{for every }A\subseteq X.
\]
This is \(CI=IC\). Conversely suppose these two operators commute. Substitute \(A=X\setminus D\). Then \(I(A)=\varnothing\), so
\[
\varnothing=C(I(A))=I(C(A))=C(X\setminus D)\cap D.
\]
Thus no fiber meets both \(D\) and its complement, so \(D\) is fiber-saturated. The equivalent pairwise formulation is immediate. A vertex lies in \(D\) exactly when some vertex points to it; this identifies membership in \(D\) with positive indegree and gives the sibling formulation. This reasoning also proves the claim for infinite \(X\), with no selection of representatives.

**Finite decomposition.** A finite functional digraph is a set of connected components, each having one directed cycle with rooted trees feeding into its cycle vertices. Every noncycle vertex is either a leaf or a nonleaf. In a tree rooted at a noncycle nonleaf, all incoming children must have the same leaf/nonleaf status by the established criterion. Let \(u(z)\) be the exponential generating function for these noncycle nonleaf rooted trees. The root contributes \(z\), and its nonempty unordered set of children consists either entirely of leaves (each of weight \(z\)) or entirely of nonleaf rooted trees (each of weight \(u(z)\)). These disjoint choices have generating functions \(\exp(z)-1\) and \(\exp(u)-1\), yielding
\[
u(z)=z\bigl(\exp(z)+\exp(u(z))-2\bigr).
\]

For a vertex on a directed cycle, its predecessor on that cycle has positive indegree and is therefore a nonleaf. Thus every additional child of that cycle vertex must be a nonleaf rooted tree. The weight of a cycle vertex together with its attached branches is \(v(z)=z\exp(u(z))\). A component is a directed labelled cycle of such units, with generating function \(\sum_{k\ge1}v(z)^k/k=-\log(1-v(z))\). A whole functional graph is an unordered set of components, giving \(A(z)=\exp(-\log(1-v(z)))=1/(1-v(z))\). These constructions are reversible and count each labelled endofunction once. The formal power series equations determine all coefficients exactly.

**Asymptotics.** Write \(H(z,u)=u-z(\exp(z)+\exp(u)-2)\). The first positive critical point satisfies \(H=H_u=0\). Since \(H_u=1-z\exp(u)\), one has \(\exp(u)=1/z\), hence \(u=-\log z\) and the displayed equation for \(\rho\). Its left side increases strictly on \((0,1)\), since its derivative is \(B(z)=(1+z)\exp(z)-2+1/z>0\); its limits at zero and one have opposite signs, establishing uniqueness. At the critical point \(u_*=-\log\rho\),
\[
H_z(\rho,u_*)=-B,\qquad H_{uu}(\rho,u_*)=-1.
\]
Consequently the implicit-function square-root expansion has
\[
u(z)=u_*-\sqrt{2B\rho}\sqrt{1-z/\rho}+O(1-z/\rho).
\]
It follows that
\[
1-z\exp(u(z))=\sqrt{2B\rho}\sqrt{1-z/\rho}+O(1-z/\rho).
\]
The coefficients of \(u\) are nonnegative and occur at consecutive exponents \(2\) and \(3\), so the smooth implicit-function schema is aperiodic and the positive real singularity is uniquely dominant. Its standard square-root transfer theorem gives
\[
[z^n]A(z)\sim\frac{\rho^{-n}}{\sqrt{2\pi B\rho n}}.
\]
Multiplying by \(n!\), then using Stirling's formula, proves both stated asymptotics. Neither numerical root-finding nor finite enumeration is used as a substitute for the analytic proof.

## Verification

Run `python3 verify.py` from the directory containing this document. The standalone standard-library checker computes the first eleven coefficients of the formal series using exact rational arithmetic. Independently, it enumerates every labelled function on sets of sizes one through six (a total of 50,069 endofunctions), verifying the fiber/leaf condition and matching exact counts. For every function through size five, it additionally checks the two composite modal event transformers on every Boolean valuation (104,330 function–event pairs in total). Explicit finite witnesses confirm both an allowed nonpermutation and a disallowed constant map. Verification output ends in `VERIFICATION_OK`.

These finite tests do not establish the infinite-set equivalence, the all-orders generating function, or the asymptotic law; those conclusions are supplied by the arguments above.

## Relationship to prior work

The recent article of Figallo, Sarmiento and Pezzini [1] develops tense Boolean algebra semantics and algebraic completeness for a minimal tense calculus. Its definitions of the conjugate tense operators, including Proposition 2.1, supply the motivating setting. The inspected Sections 1–5 establish proof-theoretic/algebraic correspondence rather than classify functional frames where two round trips commute, enumerate those frames, or derive their asymptotic frequency.

The decomposition of functional digraphs into cycle-rooted trees and the labelled exponential formula are classical; they are used, not asserted as new. Marty [2] studies the different problem of counting successor-closed subsets of functional digraphs, a nearby use of the same graph decomposition. The term *saturated* for a union of full fibers and the analytic transfer machinery in [3] are also standard. The claimed added result is the specific equivalence between tense round-trip commutation and this functional-graph constraint, together with its exact labelled census and exponential probability law.

## Limitations

The result applies to total deterministic forward maps, while their past converses may be multivalued. The counts distinguish labels; they are not counts up to graph isomorphism. The exponential formula uses finite graph decomposition, so does not enumerate infinite functional digraphs. There may be an older equivalent formulation of the same restricted mapping class or the coefficient sequence under different terminology; the originality assessment remains qualified by that bibliographic risk. No independent audit has been performed.

## References

[1] M. Figallo, J. Sarmiento and L. Pezzini, *Tense Logic via Truth Degrees: An Algebraic Completeness Result for Kashima’s Calculus*, arXiv:2610.01547v1 (first public 2026-10-01), https://arxiv.org/html/2610.01547v1.

[2] M. Marty, *Counting Successor-Closed Subsets of Functional Digraphs*, arXiv:2608.27145v2 (2026), https://arxiv.org/abs/2608.27145. Its functional-digraph decomposition (Proposition 2.10), successor-closed subset polynomial (Theorem 3.1), and extremal bounds (Theorems 4.1 and 5.1) were inspected; they address a different counting variable and do not imply the present labelled map census.

[3] P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), chapters on labelled structures, smooth implicit-function schemas, and singularity analysis.
