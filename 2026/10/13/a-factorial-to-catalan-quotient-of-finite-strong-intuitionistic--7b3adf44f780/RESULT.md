# A factorial-to-Catalan quotient of finite strong intuitionistic modal frames with distributive presentation fibers

## Finding

For each integer \(n\geq1\), the strong intuitionistic modal relations on the fixed ordered chain \(C_n=\{0<1<\cdots<n-1\}\) form a finite semigroup of size \((n+1)!\). Their distinct global necessity operators on persistent truth sets form a quotient semigroup isomorphic to the *Catalan monoid* of order-preserving, order-decreasing self-maps of \(\{0,\ldots,n\}\), with exactly \(\frac{1}{n+2}\binom{2n+2}{n+1}\) elements.

The new structural refinement is an **exact classification of every semantic presentation fiber**. A modal operator with threshold profile \(\rho\) has an interval of representing accessibility relations, isomorphic as a poset to a product of explicit integer chains. Its edge-count polynomial is
\[
\boxed{\displaystyle
\sum_{R:\,\rho_R=\rho}q^{|R|}
=q^{\sum_{z\in J(\rho)}\rho(z+1)}
\prod_{z\in P(\rho)}\left(1+q+\cdots+q^{\rho(z+1)}\right),
}
\]
where \(J(\rho)=\{0\le z<n:\rho(z+1)>\rho(z)\}\) is the set of positive record steps and \(P(\rho)=\{0,\ldots,n-1\}\setminus J(\rho)\) is the set of plateau steps. In particular, exactly \(2^n\) semantic operators have a unique representing relation; every other one has more than one. The share of uniquely represented operators tends to zero as \(n\) grows.

## Assumptions and scope

Fix \(n\geq1\), retain the labels and linear order of \(C_n\), and consider **all**, not just the frames satisfying stronger logic-specific axioms, binary relations \(R\subseteq C_n\times C_n\) such that
\[
 xRy\Longrightarrow x\le y,
 \qquad x\le y\ \&\ yRz\Longrightarrow xRz.
\]
These are precisely the strong, prefix-stable frames used as the base frame class in [1]. No seriality, reflexivity, or additional modal axiom is assumed. (Strongness plus prefix-stability does imply transitivity.) Atomic valuations are arbitrary upward-closed subsets of \(C_n\). Modal equivalence of frames means equality of the truth set of **every** intuitionistic modal formula at corresponding worlds under **every** common persistent atomic valuation; equivalent frames need not have identical accessibility relations. Their order and world labels are fixed throughout; there is no quotient by chain isomorphism.

Write \(U_k=\{k,k+1,\ldots,n-1\}\) for \(0\le k\le n\), so \(U_0=C_n\) and \(U_n=\varnothing\). The usual forcing clause is \(x\Vdash\Box A\) if and only if every \(R\)-successor of \(x\) forces \(A\).

## Proof

**1. Every relation is a bounded column-height vector.** Fix the second coordinate \(z\). Prefix-stability says that \(\{x:xRz\}\) is an initial interval of the chain; strongness says it lies in \(\{0,\ldots,z\}\). Thus there is a unique integer \(a_z\), \(0\le a_z\le z+1\), such that \(xRz\) precisely when \(x<a_z\). Conversely every such vector \(a=(a_0,\ldots,a_{n-1})\) defines a valid strong relation. Consequently
\[
 \#\mathcal R_n=\prod_{z=0}^{n-1}(z+2)=(n+1)!,\qquad |R_a|=\sum_{z=0}^{n-1}a_z.
\]
The inclusion order on these relations is the componentwise order on \(\prod_{z=0}^{n-1}\{0,\ldots,z+1\}\), a product of finite chains.

**2. The observable threshold profile is the prefix maximum.** Define
\[
 \rho_a(0)=0,\qquad \rho_a(k)=\max_{0\le z<k}a_z\quad(1\le k\le n).
\]
For each \(x\in C_n\) and every \(k\),
\[
 \begin{aligned}
 x\in\Box_{R_a}(U_k)
 &\iff \text{no }z<k\text{ satisfies }xR_a z\\
 &\iff \text{for each }z<k,\ x\ge a_z\\
 &\iff x\ge\rho_a(k).
 \end{aligned}
\]
Hence \(\Box_{R_a}(U_k)=U_{\rho_a(k)}\). Each \(\rho_a\) is nondecreasing and satisfies \(0\le\rho_a(k)\le k\). Conversely, given any nondecreasing map \(\rho:\{0,\ldots,n\}\to\{0,\ldots,n\}\) with \(\rho(k)\le k\), choose
\[
 a_z=\begin{cases}
 \rho(z+1),&\rho(z+1)>\rho(z),\\
 0,&\rho(z+1)=\rho(z).
 \end{cases}
\]
Then \(0\le a_z\le z+1\) and induction on \(k\) gives \(\rho_a=\rho\). Thus every Catalan-monoid element is realized. Its standard ballot-path enumeration is \(C_{n+1}=\frac{1}{n+2}\binom{2n+2}{n+1}\) [2–4].

Because every persistent formula truth set is some \(U_k\), equality of these operators implies, by structural induction, equality of truth sets for every formula under every persistent valuation. If two profiles differ at \(k\), assign an atom \(p\) the truth set \(U_k\); then \(\Box p\) distinguishes the frames. This proves the stated exact modal-equivalence criterion.

**3. The quotient respects relational composition.** Take the convention
\(x(R_a\circ R_b)z\) if and only if some \(y\) satisfies \(xR_a y\) and \(yR_b z\). The height of column \(z\) in the composite is
\[
 c_z=\max_{0\le y<b_z}a_y=\rho_a(b_z)
\]
(the empty maximum is zero). The composite is again strong and prefix-stable, and for every \(k\),
\[
 \rho_c(k)=\max_{z<k}\rho_a(b_z)
 =\rho_a\bigl(\max_{z<k}b_z\bigr)
 =\rho_a(\rho_b(k)).
\]
The middle equality uses monotonicity of \(\rho_a\). Therefore \(a\mapsto\rho_a\) is a surjective semigroup homomorphism, with kernel precisely modal equivalence. **The source need not be a monoid:** the full order relation is a left identity, but usually not a right identity. The quotient is nevertheless the usual Catalan monoid with its identity map.

**4. Every congruence class is an explicit distributive interval.** Fix \(\rho\). At each step \(z\) where \(\rho(z+1)>\rho(z)\), the new prefix maximum forces \(a_z=\rho(z+1)\). At every plateau step where \(\rho(z+1)=\rho(z)\), the previous prefix maximum is already achieved, so the only condition on \(a_z\) is \(0\le a_z\le\rho(z+1)\). All plateau choices are independent. Thus the fiber is exactly
\[
 \mathcal F(\rho)\cong\prod_{z\in P(\rho)}\{0,1,\ldots,\rho(z+1)\}.
\]
The coordinatewise lower and upper bounds on its entries are themselves in the fiber, so it is literally an interval of the ambient product lattice. Its cardinality is \(\prod_{z\in P(\rho)}(\rho(z+1)+1)\); grading by the number of edges \(\sum a_z\) proves the polynomial in the Finding. Every intermediate edge count between its least and greatest values is attained, and there is one relation at each extreme.

**5. Exactly \(2^n\) fibers are singletons.** The product has one element exactly when every plateau has height zero. Since \(\rho\) is nondecreasing, it then consists of a possibly empty initial string of zeros followed by a *strictly* increasing string of positive entries. The positive entries constitute a subset \(\{v_1<\cdots<v_k\}\subseteq\{1,\ldots,n\}\), placed in the last \(k\) positions of \((\rho(1),\ldots,\rho(n))\). Conversely every such subset defines a valid regressive profile because its \(j\)-th smallest member satisfies \(v_j\le n-k+j\). Thus singleton fibers are indexed by the \(2^n\) subsets. Since \(C_{n+1}\sim4^{n+1}/(\sqrt\pi(n+1)^{3/2})\), their proportion \(2^n/C_{n+1}\) tends to zero.

Summing the edge enumerators of all fibers recovers the independent relation count refined by edge number,
\[
 \sum_{\rho}\sum_{R_a:\rho_a=\rho}q^{|R_a|}
 =\prod_{j=1}^n(1+q+\cdots+q^j),
\]
confirming compatibility with the original independent column choices, without claiming this known product to be new.

## Verification

The included portable script `verify.py` constructs every allowed column-height vector for each \(1\le n\le7\) (46,232 labeled relations). It independently evaluates necessity on all \(n+1\) upward-closed truth sets, checks the distinct operator counts \(2,5,14,42,132,429,1430\), singleton-fiber counts \(2,4,8,16,32,64,128\), record invariants, exact fiber sets and cardinalities, full edge-polynomial distributions, and total factorial/graded enumerators. For \(n\le4\) it also independently constructs each compositional relation via an intermediate world and verifies the quotient homomorphism for every ordered pair, including the left-identity/right-identity distinction. Its recorded result is `VERIFY_OK 177137 exact assertions; 46232 accessibility matrices screened; all operators evaluated on every upset through n=7`.

These are exact finite cross-checks; the proof above, not finite enumeration, establishes the assertions for all \(n\ge1\). Independent mathematical audit has not yet been performed.

## Relationship to prior work

Van der Giessen [1, Section 1] gives the strong, prefix-stable modal Kripke semantics and investigates admissibility and proof systems, rather than the numbers or equivalence classes of relational presentations on a fixed chain. The Catalan monoid and its cardinality are classical [2–4]; those properties are explicitly **prior work**, not independently new here. The closely related double Catalan monoid [3] arises from a different relational representation of the 0-Hecke monoid, not from quotienting all strong chain-frame presentations by their induced necessity operator. The more recent faithful upper-triangular Boolean-matrix representations [5] do not, in their inspected indexed description, supply the quotient of this factorial relation semigroup or the interval structure and graded rank polynomials of all its modal fibers. The claimed contribution is their **joint semantic quotient and fiber classification**, not the Catalan enumeration or q-factorial alone. No unindexed/implicit prior derivation can be ruled out.

## Limitations

The ordered finite-chain hypothesis is essential; the argument does not classify strong frames over arbitrary partial orders or additional logic-specific frame classes. It compares pointwise semantics under *common valuations*, not merely validity of formulas after universal quantification over entire frames. Source comparisons used substantial openly indexed text of [1] and published abstracts/descriptions of several algebraic references, not an exhaustive inspection of all relevant full-length semigroup papers; equivalence to an unindexed theorem remains a potential originality risk. The new classification is mathematically proved here and computationally checked in small cases, but has not undergone an independent external audit.

## References

[1] Iris van der Giessen, *Admissible rules for six intuitionistic modal logics*, Annals of Pure and Applied Logic 174 (2023), 103233; first publicly online December 21, 2022. https://doi.org/10.1016/j.apal.2022.103233

[2] O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, International Electronic Journal of Algebra 10 (2011). https://dergipark.org.tr/en/pub/ieja/article/266308

[3] V. Mazorchuk and B. Steinberg, *Double Catalan monoids*, Journal of Algebraic Combinatorics 36 (2012), 333–354. https://doi.org/10.1007/s10801-011-0336-y

[4] Andrew Solomon, *Catalan monoids, monoids of local endomorphisms, and their presentations*, Research Report 95-6, 1995. https://ns.maths.usyd.edu.au/u/ResearchReports/Algebra/Sol/cat-mon-end.html

[5] Y. F. Luo, Z. F. Jin and W. T. Zhang, *Finite Gröbner-Shirshov bases and faithful representations for Catalan monoids*, Communications in Algebra 54 (2026), 185–195; online June 29, 2025. https://doi.org/10.1080/00927872.2025.2522155
