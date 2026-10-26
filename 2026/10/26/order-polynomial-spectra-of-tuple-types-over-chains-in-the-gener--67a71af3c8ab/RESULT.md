# Order-polynomial spectra of tuple types over chains in the generic partial order

## Finding
Let \(\mathcal R\) be the countable universal homogeneous strict partial order. Let \(C_n=(a_1<\cdots<a_n)\) be an individually named finite induced chain, with \(n\geq0\). For \(r\geq1\), let \(T_r(n)\) be the number of complete types of ordered, pairwise distinct \(r\)-tuples, all outside \(C_n\), over these parameters. Equivalently, it is the number of labelled finite posets extending the fixed chain \(C_n\) by \(r\) named distinct new elements.

For each strict partial order \(F\) on \([r]\), construct an endpoint poset \(Q_F\) on \(2r\) distinct symbols \(L_i,U_i\) (\(i\in[r]\)) by taking the reflexive transitive closure of:

1. \(L_i\leq U_i\) for every \(i\);
2. \(L_i\leq L_j\) and \(U_i\leq U_j\) whenever \(i<_Fj\);
3. \(L_i\leq U_j\) and \(L_j\leq U_i\) whenever \(i\parallel_F j\).

These rules define a genuine partial order: same-kind arrows follow the acyclic relation \(F\), cross-kind arrows go only from \(L\)-symbols to \(U\)-symbols, and there are no arrows in the opposite direction. Write \(\Omega_Q(m)\) for the number of weakly order-preserving maps from \(Q\) to an \(m\)-element chain. Then, **for every \(n\geq0\) and \(r\geq1\),**
\[
\boxed{T_r(n)=\sum_{F\in\mathsf{Pos}(r)}\Omega_{Q_F}(n+1),}
\]
where \(\mathsf{Pos}(r)\) comprises all *labelled* strict partial orders on \([r]\), not isomorphism classes.

Consequently \(T_r(n)\), for each fixed \(r\), is an integer-valued polynomial in \(n\) of **exact degree \(2r\)**. More precisely,
\[
\boxed{T_r(n)=\sum_{k=1}^{2r}c_{r,k}\binom{n+1}{k}},\qquad
c_{r,k}=\sum_{F\in\mathsf{Pos}(r)}\#\operatorname{SurjIso}(Q_F,[k])>0.
\]
Here \(\operatorname{SurjIso}\) denotes surjective weak order-preserving maps; every coefficient is a positive integer. After these finitely many arity-dependent coefficients are computed, the type count at any chain length requires at most \(2r\) binomial terms.

The first exact polynomials are
\[
\begin{aligned}
T_1(n)&=\frac{(n+1)(n+2)}2,\\
T_2(n)&=\frac{(n+1)(n+2)(2n^2+8n+9)}6,\\
T_3(n)&=\frac{(n+1)(n+2)(n^2+4n+5)(6n^2+29n+38)}{20}.
\end{aligned}
\]
For the two-point count, each orientation \(x<y\) or \(y<x\) occurs
\[\frac{(n+1)(n+2)^2(n+3)}{12}\]
times, while \(x\parallel y\) occurs
\[\frac{(n+1)(n+2)(n^2+3n+3)}6\]
times. Thus the three relation frequencies tend to \(1/4,1/4,1/2\) as \(n\to\infty\). At \(n=0\), \(T_r(0)\) is the number of labelled \(r\)-element posets, as expected.

## Assumptions and scope
The language contains only one binary strict-order relation and equality. All chain elements are named individually; tuple coordinates are ordered and are required to be pairwise distinct and different from all parameters. There is no quotient by permutations of tuple coordinates or chain labels. The homogeneous structure is the Fraïssé limit of **all** finite strict partial orders. The formula does not claim that arbitrary parameter posets have polynomial type counts when their size varies, nor that the polynomial degree is uniform in growing arity. Integer-arithmetic complexity is asserted only for fixed \(r\) after precomputation.

## Proof
**Step 1: Finite types.** Every finite poset extends into \(\mathcal R\), and any isomorphism between finite induced subposets extends to an automorphism. Therefore two ordered tuples over the named chain have the same complete type precisely when their finite induced poset structures are identical. It suffices to count the labelled finite one-block extensions specified above.

**Step 2: Endpoint coordinates.** For a new point \(x_i\), its predecessors among \(C_n\) form an initial segment and its successors form a final segment. Hence there are unique integers \(0\leq\ell_i\leq u_i\leq n\) such that
\[
a_j<x_i\iff j\leq\ell_i,\qquad x_i<a_j\iff j>u_i.\]
Every parameter with \(\ell_i<j\leq u_i\) is incomparable to \(x_i\).

**Step 3: Necessary constraints.** Fix the strict partial order \(F\) induced by the new tuple. If \(x_i<x_j\), transitivity forces \(\ell_i\leq\ell_j\) and \(u_i\leq u_j\). If \(x_i\parallel x_j\), a chain witness \(x_i<a_t<x_j\) would force \(x_i<x_j\), and such a witness exists exactly if \(u_i<\ell_j\). Thus incomparability requires \(\ell_j\leq u_i\) and \(\ell_i\leq u_j\). These are precisely the inequalities defining an isotone map \(Q_F\to\{0,1,\ldots,n\}\), with \(L_i\mapsto\ell_i\), \(U_i\mapsto u_i\).

**Step 4: Sufficiency and absence of hidden closure constraints.** Conversely fix \(F\) and integers satisfying the displayed inequalities. Define a binary strict relation on \(C_n\sqcup[r]\) by the given chain order, by \(F\) among new points, and by the declared cuts between new points and parameters. This is irreflexive and asymmetric: \(F\) is a strict poset, the chain is strict, and \(\ell_i\leq u_i\) prevents both \(a_j<x_i\) and \(x_i<a_j\) for the same pair. We check *transitivity* on all triples, without relying on enumeration. Triples wholly within either block are transitive by construction. For two parameters and one new point, the lower parameters form an initial segment and the upper parameters form a final segment with no overlap, so transitivity holds. For two new points and one parameter, there are only three relevant patterns: \(a_j<x_i<x_h\) implies \(j\leq\ell_i\leq\ell_h\), so \(a_j<x_h\); \(x_i<x_h<a_j\) implies \(j>u_h\geq u_i\), so \(x_i<a_j\); and \(x_i<a_j<x_h\) implies \(u_i<j\leq\ell_h\). In the third pattern the inequality \(u_i<\ell_h\) rules out \(i\parallel_F h\) by the cross-cut constraint, and also rules out \(h<_F i\) because then \(\ell_h\leq\ell_i\leq u_i\). Therefore \(i<_F h\), the transitivity conclusion already present. All triple patterns are covered (including the dual orientations), proving that the prescribed relation itself is a strict partial order with no additional comparisons. Thus it is exactly the desired finite induced extension.

The two constructions are mutually inverse. Summing their numbers over every labelled \(F\) gives the first boxed identity.

**Step 5: Polynomiality and its sharp degree.** Every isotone map \(Q_F\to[n+1]\) has a unique image of size \(k\), obtained by choosing \(k\) target labels and a surjective isotone map to the standard \(k\)-chain. Hence
\[\Omega_{Q_F}(n+1)=\sum_{k=1}^{2r}\#\operatorname{SurjIso}(Q_F,[k])\binom{n+1}{k}.\]
For every \(k\in[1,2r]\), take any linear extension of \(Q_F\) and coalesce consecutive entries into \(k\) nonempty blocks to obtain at least one such surjection. In particular, the coefficient of \(\binom{n+1}{2r}\) is positive, proving exact degree \(2r\). The two- and three-point displayed polynomials follow from finite endpoint-poset enumeration; the accompanying standard-library checker reproduces their binomial coefficients and independently tests small finite extensions.

**Step 6: Two-point orientation split.** For \(r=2\), the two comparable labelled posets each yield \((n+1)(n+2)^2(n+3)/12\) isotone maps. The incomparable labelled poset yields \((n+1)(n+2)(n^2+3n+3)/6\). Their sum is \(T_2(n)\). The leading coefficients are respectively \(1/12,1/12,1/6\), whose normalized fractions are \(1/4,1/4,1/2\).

## Verification
Run `python3 verify.py` using a standard Python 3 interpreter. The program independently constructs the finite endpoint posets, counts surjective isotone maps by strict chains of order ideals, and evaluates the binomial-coefficient spectrum for arities \(1\) through \(4\). A separate exhaustive checker assigns all ternary relations among old/new vertices and computes transitive closure directly, with no use of endpoint inequalities; it matches the spectral formula for \(15\) parameter/arity configurations: \(1\leq r\leq3\), with \(0\leq n\leq4\) for arity one, \(0\leq n\leq5\) for arity two, and \(0\leq n\leq3\) for arity three. It also checks the \(18\) orientation counts at arity two. Closed polynomial expressions undergo \(33\) comparisons. The output file `verification_output.txt` records all results, ending in `ALL_TESTS_PASS`. These finite checks do not prove the all-arity result: Steps 1–5 above do.

## Relationship to prior work
The universal homogeneous poset and its extension property are established background (Hubička 2010; Pach–Pinsker–Pluhár–Pongrácz–Szabó 2011). The classical order-polynomial theorem for maps from a fixed finite poset to a chain is due to Stanley; Jochemko (2013) provides related orbital order-polynomial theory. The new content claimed here is the explicit *endpoint poset* \(Q_F\) encoding **all complete tuple types over a varying named chain**, the resulting arity-uniform binomial spectrum, and its sharp \(2r\)-degree conclusion.

Earlier random-poset one-type counting over arbitrary parameters and two-type counting over antichain parameters concern different base configurations. In contrast to chain parameters' polynomial growth, the previously established antichain-parameter two-type sequence grows exponentially. The numerical two-point scalar sequence coincides, after an index shift, with OEIS A071245; that entry already tabulates the quartic polynomial numerically, but does not attribute it to random-poset tuple types or supply the all-arity endpoint construction. The numeric quartic alone is **not** claimed as a newly discovered integer sequence.

## Limitations
An independent mathematical audit and an exhaustive historical priority search have not occurred. Literature indexing may miss an earlier equivalent finite-extension enumeration, particularly in older combinatorial treatments. The public published-finding corpus descriptions of the closest indexed findings were compared, but their linked full text was not accessible in this round; the coverage assessment is accordingly qualified. The program checks finitely many cases; all infinite assertions rest on the mathematical proof. No complexity claim for computing the coefficients as a function of unbounded arity is made.

## References
- J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1 (public 2010-09-03), especially Section 3.1, https://arxiv.org/html/1009.0566v1.
- P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz and C. Szabó, *Reducts of the random partial order*, arXiv:1111.7109v1 (public 2011-11-30), especially Sections 1–3, https://arxiv.org/html/1111.7109v2.
- K. Jochemko, *Order polynomials and Pólya's enumeration theorem*, arXiv:1310.0838 (public 2013-10-02), especially Section 2, https://arxiv.org/abs/1310.0838.
- R. P. Stanley, *A chromatic-like polynomial for ordered sets*, 1970, and *Ordered Structures and Partitions*, Memoirs AMS 119 (1972): foundations of order polynomials.
- OEIS A071245, previously tabulated quartic scalar sequence (index shift only), https://oeis.org/A071245.
