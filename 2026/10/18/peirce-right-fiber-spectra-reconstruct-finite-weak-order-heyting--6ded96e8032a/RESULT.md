# Peirce-right-fiber spectra reconstruct finite weak-order Heyting frames

## Finding
Let \(P=A_1\oplus\cdots\oplus A_h\) be an ordinal sum of nonempty antichains, \(|A_i|=n_i\geq1\), and let \(H=\operatorname{Up}(P)\) be the finite Heyting algebra of upsets. Write \(a_i=2^{n_i}-1\) and \(N=1+\sum_{i=1}^h a_i=|H|\). For \(U\in H\), the *Peirce-right fiber* is
\[
R(U)=\{V\in H:((U\to V)\to U)=U\}.
\]
Equivalently this is the set of right arguments for which \(((U\to V)\to U)\to U=1\).

The complete fiber-cardinality generating polynomial is
\[
\boxed{\Phi_P(z):=\sum_{U\in H} z^{|R(U)|}=(a_h+1)z^N+\sum_{i=1}^{h-1}a_i z^{1+\sum_{j=1}^{i}a_j}.}
\]
Its exponents are strictly increasing. **The polynomial uniquely determines the entire ordered tuple of level sizes** \((n_1,\ldots,n_h)\) and hence the isomorphism type of \(P\) and \(H\), within the family of finite weak orders.

For comparison, the ordinary two-variable Peirce satisfaction degree is
\[
\boxed{\frac{|\{(U,V)\in H^2:((U\to V)\to U)=U\}|}{N^2}=1-\frac{\sum_{i<j}a_i a_j}{N^2}.}
\]
This scalar is insensitive to the order of the levels, while the full right-fiber polynomial is not. For example, level-size sequences \((2,3)\) and \((3,2)\) both have Peirce degree \(100/121\), whereas their fiber polynomials are respectively \(3z^4+8z^{11}\) and \(7z^8+4z^{11}\).

## Assumptions and scope
The poset \(P\) has at least one level. All levels are finite and nonempty, and \(A_i<A_j\) pointwise for \(i<j\). Every element of \(H\) is an upward-closed subset of \(P\). Heyting implication is defined by
\[
U\to V=\{x\in P:(\uparrow_P x)\cap U\subseteq V\}.
\]
The statement includes the one-level (Boolean) case and singleton levels, without positivity assumptions beyond \(n_i\geq1\). Fiber cardinalities and the polynomial use the ordinary finite set cardinality, not a probability weighting.

## Proof
**Upset normal form.** Put \(T_i=\bigcup_{j=i}^{h}A_j\) and \(T_{h+1}=\varnothing\). Besides \(\varnothing\), every upset has a unique representation \(U=T_{i+1}\cup S\), with \(\varnothing\ne S\subseteq A_i\). Thus there are \(a_i\) nonempty upsets first meeting level \(i\), and \(|H|=N\).

**Implication test.** For arbitrary upsets \(U,V\), we always have \(U\subseteq (U\to V)\to U\). Equality holds precisely when, for every \(x\notin U\), there exists \(y\geq x\) such that \(y\notin U\) and \((\uparrow_P y)\cap U\subseteq V\). This follows directly from the displayed implication definition: a point \(x\notin U\) must fail membership in \((U\to V)\to U\) because of a higher witness \(y\in(U\to V)\setminus U\).

**Exact fibers.** Suppose \(U=T_{i+1}\cup S\), where \(\varnothing\ne S\subsetneq A_i\). For any \(x\in A_i\setminus S\), the only point at or above \(x\) but outside \(U\) is \(x\) itself, and \((\uparrow_P x)\cap U=T_{i+1}\). The implication test therefore forces \(T_{i+1}\subseteq V\). Conversely, if this containment holds, any \(x\notin U\) on a lower level can reach a point of \(A_i\setminus S\), and a point already in that complement can witness itself. Hence
\[
R(U)=\{V\in H:T_{i+1}\subseteq V\}.
\]
If instead \(U=T_i\) is a full tail with \(i>1\), every point just below this tail, in \(A_{i-1}\), has intersection of its upper cone with \(U\) equal to \(T_i\). The same necessary-and-sufficient witness argument gives
\[
R(T_i)=\{V\in H:T_i\subseteq V\}\qquad(2\leq i\leq h).
\]
Finally, \(R(\varnothing)=R(P)=H\) directly by the Heyting identities for \(0\) and \(1\).

**Counting and inversion.** For each \(1\leq i<h\), the fiber \(\{V:T_{i+1}\subseteq V\}\) occurs for precisely \(a_i-1\) partial upsets at level \(i\) and the full tail \(T_{i+1}\): hence multiplicity \(a_i\). Its size is \(1+\sum_{j\leq i}a_j\). The unrestricted fiber \(H\) occurs for \(\varnothing\), \(P\), and the \(a_h-1\) partial upsets at the top level, hence multiplicity \(a_h+1\). This proves the polynomial, including \(h=1\).

As the exponents increase strictly, the ordered nonleading coefficients are exactly \(a_1,\ldots,a_{h-1}\), and the leading coefficient is \(a_h+1\). Recover \(n_i=\log_2(a_i+1)\) for \(i<h\) and \(n_h=\log_2(\text{leading coefficient})\). The recovered tuple classifies weak-order posets, so the polynomial determines the isomorphism type. Summing the cardinalities of all fibers yields the degree formula; equivalently, the \(a_i\) arguments in each nonleading fiber lack exactly \(\sum_{j>i}a_j\) right-hand witnesses, giving \(\sum_{i<j}a_i a_j\) failing ordered pairs.

## Verification
The included `verify.py` enumerates all labelled weak-order level-size compositions of total world counts \(1\) through \(8\), and five additional larger examples. It independently constructs upsets and implication from principal cones, exhaustively verifies every Peirce pair, the explicit fiber sets, polynomial coefficients, inverse level reconstruction, and total failure formula. For all compositions of size at most \(5\), it additionally reconstructs implication by independently enumerating the largest residuated upset. Its successful local run returned `VERIFY_OK families=260 peirce_pairs=328293 direct_residuation_families=31`. The unrestricted theorem relies on the preceding proof, not finite testing.

Run with standard Python 3: `python verify.py`. No third-party dependencies are needed.

## Relationship to prior work
Bumpus and Kocsis introduced the degree-of-satisfiability framework for finite Heyting algebras, treated Peirce's law as a two-variable classical principle, and established that it has no finite satisfiability gap (notably Corollary 3.11 of their preprint). Their paper does not provide the full Peirce right-fiber cardinality polynomial or reconstruction of level sizes for ordinal sums of antichains. The usual finite-poset representation of Heyting algebras and the basic Kripke implication formula are standard inputs, not claimed as new. The contribution here is the fiber structural classification together with its complete rank polynomial and inverse-isomorphism statement.

## Limitations
The inversion concerns the family of finite weak-order frames only; no claim is made that right-fiber polynomials classify general finite posets or infinite Heyting algebras. The degree-of-satisfiability concept, Peirce identity, and bounded-poset algebra representation are established mathematics. Equivalent uncatalogued formulas in earlier order-theoretic or logic literature remain possible; publication priority has not been independently established. Exhaustive finite tests alone do not prove the general identities.

## References
B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first public version 2021-10-21), especially Example 1.8 and Corollary 3.11. https://arxiv.org/abs/2110.11515

B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, *Journal of Symbolic Logic* 90 (2025), 533–551. https://doi.org/10.1017/jsl.2024.2
