# Circular-window concept lattices: exact spectra, sharp crossover and modularity classification

## Finding

Let \(n\ge 2\) and \(1\le \ell<n\) be integers. On \(V=\mathbb Z/n\mathbb Z\), let \(W_s=\{s,s+1,\ldots,s+\ell-1\}\) (modulo \(n\)). The formal context \(K_{n,\ell}\) has one object for each \(W_s\), one attribute for each vertex, and incidence given by membership. Write \(r=n-\ell\), and denote its number of formal concepts by \(C(n,\ell)\). Then:

**(A) Exact lattice description.** Under the intent representation, the elements of the concept lattice are precisely the subsets of \(V\) whose complements are empty, all of \(V\), or are disjoint unions of nonempty maximal cyclic consecutive runs each having length at least \(r\). Equivalently the complement is a union of cyclic \(r\)-windows. The standard concept lattice orders intents by reverse inclusion; reversing the order does not change cardinality, height, modularity or distributivity.

**(B) Exact census and spectral law.** For all \(n>r\ge1\),
\[
 C(n,n-r)=2+\sum_{j=1}^{\lfloor n/(r+1)\rfloor}\frac{n}{j}\binom{n-j(r-1)-1}{2j-1}.
\]
Set \(a_0=r+1\), \(a_1=\cdots=a_r=2\), and, for \(n\ge r+1\), define
\[
 a_n=2a_{n-1}-a_{n-2}+a_{n-r-1}.
\]
Then \(C(n,n-r)=a_n\). For fixed \(r\), as \(n\to\infty\),
\[
 C(n,n-r)\sim\lambda_r^n,
 \quad \lambda_r^{\,r-1}(\lambda_r-1)^2=1,
 \quad 1<\lambda_r\le2.
\]
The root \(\lambda_r\) is unique on \((1,\infty)\); \(\lambda_1=2\), and \(\lambda_r\) strictly decreases to \(1\).

**(C) Sharp low-width crossover and inverse uniqueness.** If \(\ell\le\lfloor(n+1)/2\rfloor\), then exactly \(C(n,\ell)=2+n\ell\). If \(\ell>\lfloor(n+1)/2\rfloor\), then \(C(n,\ell)>2+n\ell\). For fixed \(n\), the number \(C(n,\ell)\) is strictly increasing in \(\ell\), so the number of concepts, together with \(n\), uniquely determines the window width. Every maximal chain has at most \(\ell+2\) elements, and there exists one with exactly \(\ell+2\).

**(D) Lattice-theoretic boundary.** The concept lattice is modular exactly when \(\ell=1\) or \(\ell=n-1\). It is distributive exactly when \(\ell=n-1\). At \(\ell=1\) it is the height-two lattice with \(n\) atoms (Boolean when \(n=2\)); at \(\ell=n-1\) it is the Boolean lattice on \(n\) generators.

For example, at \(n=8\) the concept counts for \(\ell=7,6,\ldots,1\) are \(256,90,46,34,26,18,10\), respectively. The result is an exact classification of the intersection-closure complexity and elementary lattice type of this symmetric family, not a claim about arbitrary circular-arc hypergraphs.

## Assumptions and scope

All cyclic windows are indexed by their labeled start vertices; \(1\le\ell<n\) makes the \(n\) window sets distinct. Every concept is counted once as a Galois-closed intent. Cyclic runs are maximal and counted on the circle, not in a chosen linear representation. In the asymptotic statement \(r\) is fixed and \(n\to\infty\); there is no assertion of a uniform asymptotic when \(r\) grows with \(n\). The modularity statement concerns the abstract lattice, not the hypergraphic poset of acyclic orientations of a hypergraph.

## Proof

**Step 1 (Galois closure).** For the membership context, intents are exactly arbitrary intersections of the object attribute sets \(W_s\), including the intersection over the empty family, \(V\). The complement \(B_s=V\setminus W_s\) is an \(r\)-vertex cyclic interval. Taking complements bijects all intents with all unions of the \(B_s\). A nonempty proper union of cyclic \(r\)-windows has each maximal run of included vertices of length at least \(r\): a vertex's originating window lies in that connected component. Conversely, each maximal cyclic run of length \(m\ge r\) is the union of its \(m-r+1\) consecutive \(r\)-windows; taking the union over runs realizes the full set. Empty and full unions are separately permitted. This proves (A).

**Step 2 (mixed-run enumeration).** For a proper nonempty union, write the cyclic binary indicator of the union. With \(j\ge1\) runs of ones, there are also exactly \(j\) runs of zeros. The one-run lengths \(u_i\) satisfy \(u_i\ge r\), and the zero-run lengths \(v_i\) satisfy \(v_i\ge1\), with total sum \(n\). After writing \(u_i=r+u'_i\), \(v_i=1+v'_i\), the nonnegative lengths sum to \(n-j(r+1)\). Stars and bars gives \(\binom{n-j(r-1)-1}{2j-1}\) ordered alternating run-length profiles. Choose the starting vertex of a marked one-run in \(n\) ways. Each resulting cyclic word is counted once for each of its \(j\) one-runs, so division by \(j\) gives the displayed summand. Only \(j\le\lfloor n/(r+1)\rfloor\) is possible. Add the two constant words to prove the exact sum in (B).

**Step 3 (transfer recurrence and asymptotics).** Use states \(0,1,\ldots,r\). State \(0\) represents the end of a one-run; state \(i\), for \(1\le i<r\), represents an unfinished zero-run of length \(i\); state \(r\) represents a zero-run of length at least \(r\). The permitted transitions are \(0\to0,0\to1\); \(i\to i+1\) for \(1\le i<r\); and \(r\to r,r\to0\). Call this adjacency matrix \(A_r\). Accepted length-\(n\) closed walks biject to cyclic strings with each zero-run of length at least \(r\), using the complementary convention to Step 2. The two constant strings correspond to the loops at states \(0\) and \(r\). For \(n>r\), each word determines exactly one closed walk, hence \(C(n,n-r)=\operatorname{tr}(A_r^n)\).

Direct expansion of \(\det(xI-A_r)\) gives \(x^{r-1}(x-1)^2-1\). Its Cayley--Hamilton identity gives \(a_n=2a_{n-1}-a_{n-2}+a_{n-r-1}\) with formal trace initials \(a_0=r+1\), \(a_1=\cdots=a_r=2\); only \(n>r\) is used as a context count. The matrix is nonnegative, irreducible and primitive (it has self-loops), so its unique leading eigenvalue is the positive root \(\lambda_r>1\) and \(\operatorname{tr}(A_r^n)=\lambda_r^n+O(\rho_r^n)\) for some \(\rho_r<\lambda_r\). The defining function is strictly increasing on \((1,\infty)\), giving uniqueness of the root. At the \(r\)-root, the \((r+1)\)-root equation's left side is larger than one, so \(\lambda_{r+1}<\lambda_r\). If the decreasing limit exceeded one, \(\lambda_r^{r-1}(\lambda_r-1)^2\) would diverge, a contradiction. This finishes (B).

**Step 4 (crossover, inverse count and chain height).** When \(\lfloor n/(r+1)\rfloor=1\), Step 2 has only the \(j=1\) term, namely \(n(n-r)=n\ell\). The condition is \(n<2(r+1)\), equivalently \(\ell\le\lfloor(n+1)/2\rfloor\). Beyond it the \(j=2\) term is positive. For fixed \(n\), the family of cyclic binary words whose one-runs have minimum length \(r+1\) is properly contained in the corresponding family with minimum length \(r\), for every \(1\le r<n-1\). A word with a single run of exactly \(r\) ones and at least one zero witnesses strictness. Thus \(C(n,\ell)\) strictly increases with \(\ell\). Every proper closed intent is contained in at least one window and therefore has at most \(\ell\) elements, bounding the length of a strict chain by \(\ell+2\) elements. Conversely every consecutive interval of length at most \(\ell\) is closed: its complement is a single interval of length at least \(r\), hence is a union of \(r\)-windows. The chain formed from the empty set, consecutive intervals of lengths \(1,\ldots,\ell\), and the full set attains the bound. This proves (C).

**Step 5 (modularity).** If \(\ell=n-1\), the complementary windows are singleton sets, so every subset is a union and the lattice is Boolean. If \(\ell=1\), its intents are exactly \(\varnothing\), the \(n\) singleton sets, and \(V\); this lattice is modular and is nondistributive when \(n\ge3\). Now assume \(2\le\ell\le n-2\) and write \(z=W_0\), \(x=W_0\cap W_1=\{1,\ldots,\ell-1\}\), \(y=W_2=\{2,\ldots,\ell+1\}\), choosing representatives \(0,\ldots,n-1\). We have \(x\subsetneq z\), and \(y\cap z\subseteq x\). Hence \(x\vee(y\wedge z)=x\). But \(x\cup y=\{1,\ldots,\ell+1\}\), which has size \(\ell+1\) and cannot be contained in any proper closed intent (every such intent lies in an \(\ell\)-window). Thus \(x\vee y=V\) and \((x\vee y)\wedge z=z\ne x\), contradicting modularity. These operations are in the inclusion order of intents; modularity and distributivity are unchanged by reversing the lattice order. This proves (D).

## Verification

The standalone program `verify_circular_arc_concepts.py` independently enumerates all intersections of windows, enumerates cyclic-run-restricted subsets, computes transfer-matrix traces by state transitions, evaluates the binomial sum and recurrence, checks strict monotonicity, and brute-force checks modularity for small lattices. The reported successful run was:

`VERIFY_OK parameter_pairs=55 independent_bit_patterns=36868 n=2..11 exact_intersections=PASS cyclic_runs=PASS transfer_trace=PASS composition=PASS recurrence=PASS fixed_n_strict_inverse=PASS`

`MODULARITY_OK cases=20 n=3..7 criterion=(arc_length=1 or complement_length=1)`

The finite tests are not a proof for arbitrary parameters; Steps 1--5 supply the general proof. Run with `python verify_circular_arc_concepts.py` using Python 3 and only its standard library.

## Relationship to prior work

Rawson, Myers, Green, Robinson and Joslyn (2023) explain the general equivalence between incidence-context concept lattices and hyperedge intersection complexes, and algorithms on those structures. That general equivalence is used here, not claimed as new. Cattaneo, Chiaselotti, Ciucci and Gentile study a connection between hypergraphs and formal concept analysis, principally including the complete uniform-hypergraph case. Kovačević and Vukobratović (2021) develop extensive enumeration and asymptotic techniques for runlength-limited binary strings, including unequal constraints on zero and one runs. The string-enumeration and transfer-matrix tools themselves are classical. The subject of the present theorem is the resulting explicit *logical closure lattice* for every cyclic uniform sliding-window context: an exact two-parameter concept count, its sharp low-width crossover, inverse width recovery, height and modularity classification, and fixed-defect spectral law together. The available inspected primary texts do not state that complete package for these incidence contexts.

## Limitations

This is an exact result for one natural symmetric family, not for arbitrary circular-arc or interval hypergraphs. Its word-counting subformula and spectral method use established methods; no invention of general RLL theory is claimed. The 2016 submitted full-text version could not be retrieved from the author's repository during the comparison (access denied), and hidden equivalent formulations in general hypergraph, formal-context or coding literature remain an originality risk. The review here is not an independent external audit. An abstract treatment of cyclic-interval *hypergraphic posets* concerns a different poset construction and is not used to claim full-text noncoverage.

## References

1. M. G. Rawson, A. Myers, R. Green, M. Robinson, C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681v1 (first publicly submitted 2023-07-21), https://arxiv.org/abs/2307.11681.
2. M. Kovačević, D. Vukobratović, *Asymptotic Behavior and Typicality Properties of Runlength-Limited Sequences*, arXiv:2105.04617 (first publicly submitted 2021-05-10), https://arxiv.org/abs/2105.04617.
3. G. Cattaneo, G. Chiaselotti, D. Ciucci, T. Gentile, *On the Connection of Hypergraph Theory with Formal Concept Analysis and Rough Set Theory*, Information Sciences 330 (2016), 342--357, https://doi.org/10.1016/j.ins.2015.09.054.
