# Nilpotent rank polynomials and a sharp defect-five rigidity threshold for finite-fence partial injections

## Finding

For each \(n\geq1\), let \(S_n\) be the inverse monoid of order-preserving, fence-preserving, parity-preserving partial injections on the chain \([n]=\{1,\ldots,n\}\), with the alternating fence order \(1\prec2\succ3\prec4\succ\cdots\). Let
\[
N_n(z)=\sum_{\substack{\alpha\in S_n\\\alpha\text{ nilpotent}}}z^{\operatorname{rank}(\alpha)}.
\]
The following recurrence computes every coefficient of \(N_n(z)\), for arbitrary \(n\), with a polynomial number of integer arithmetic operations. Set \(F_{i,j}(z)=P_{i,j}(z)=0\) if either index is nonpositive. For positive \(i,j\), put
\[
F_{i,j}(z)=\begin{cases}
z\bigl(1+F_{i-1,j-1}(z)+P_{i-2,j-2}(z)+P_{i-3,j-3}(z)\bigr),&i\equiv j\pmod2,\ i\ne j,\\
0,&\text{otherwise},
\end{cases}
\]
\[
P_{i,j}(z)=F_{i,j}(z)+P_{i-2,j}(z)+P_{i,j-2}(z)-P_{i-2,j-2}(z).
\]
Then
\[
\boxed{N_n(z)=1+\sum_{i=1}^{n}\sum_{j=1}^{n}F_{i,j}(z).}
\]
The term \(1\) represents the empty map. Computing the polynomials through dimension \(n\) takes \(O(n^3)\) integer coefficient operations.

There is also sharp rigidity near full rank. If \(n\geq3\), \(0\leq k\leq4\), and a nilpotent \(\alpha\in S_n\) has positive rank \(n-k\), then it is a restriction of one of the translations \(t\mapsto t+2\), \(t\mapsto t-2\), \(t\mapsto t+4\), \(t\mapsto t-4\), with a single translation on its entire domain. In particular,
\[
[z^n]N_n=[z^{n-1}]N_n=0,
\]
\[
[z^{n-2}]N_n=2\quad(n\geq3),\qquad
[z^{n-3}]N_n=2(n-2)\quad(n\geq4),
\]
\[
\boxed{[z^{n-4}]N_n=(n-2)(n-3)+2\quad(n\geq5).}
\]
The defect bound is optimal: for every \(n\geq7\), a nilpotent element of rank \(n-5\) exists whose displacement is not constant.

For example,
\[
N_7(z)=1+18z+32z^2+22z^3+10z^4+2z^5.
\]

## Assumptions and scope

Order-preserving means strictly increasing on the domain of a partial injection; fence-preserving means an isomorphism between the induced subposets of the fence, and parity-preserving means every point and its image have the same parity. The empty partial injection belongs to \(S_n\); multiplication is composition. Nilpotent means a positive power is the empty partial injection. Rank is the domain cardinality.

For a nonempty partial map, list its graph as
\[
(d_1,m_1),\ldots,(d_r,m_r),\quad d_1<\cdots<d_r,\quad m_1<\cdots<m_r.
\]
The characterization from Sareeto--Koppitz [1, Proposition 1] says that each \(d_t\) and \(m_t\) have the same parity; and consecutive coordinate gaps are simultaneously \(1\), both even and at least \(2\), or both odd and at least \(3\). Conversely these conditions describe exactly \(S_n\). The recurrent symbols \(F_{i,j}(z)\) and \(P_{i,j}(z)\) count nilpotent maps, rather than arbitrary elements.

## Proof

**Nilpotency criterion.** Every partial injection decomposes as directed chains and directed cycles, with isolated points allowed. If it is increasing, any directed cycle must be a fixed point: a cycle of length greater than one has a least vertex whose image is greater, contradicting increasing behavior after following the cycle. Consequently an increasing partial injection is nilpotent exactly when it has no fixed point. Under parity preservation, every pair \((d_t,m_t)\) in a nilpotent graph therefore has \(d_t\ne m_t\) and \(d_t\equiv m_t\pmod2\).

**Rank recurrence.** Define \(F_{i,j}(z)\) to be the generating polynomial of nonempty nilpotent elements whose *last* graph pair is exactly \((i,j)\), weighted by \(z\) per graph pair. This polynomial vanishes for mismatched parity or \(i=j\). In the remaining cases, the sole-pair graph contributes \(z\). Any preceding graph pair must have one of the three disjoint allowed gap configurations: \((1,1)\), both even at least \(2\), or both odd at least \(3\). These contribute respectively \(zF_{i-1,j-1}\), \(zP_{i-2,j-2}\), and \(zP_{i-3,j-3}\), since
\[
P_{i,j}(z)=\sum_{a,b\geq0}F_{i-2a,j-2b}(z)
\]
(with nonpositive-index terms zero). Inclusion--exclusion of the two parity-preserving prefix shifts gives the displayed recurrence for \(P\). Removing the last pair is reversible in all three cases. Every nonempty graph has one last pair, establishing the formula for \(N_n\). There are \(n^2\) states and each polynomial has degree at most \(n\), giving the stated complexity in coefficient operations.

**Defect-four rigidity.** Put \(r=n-k>0\), and write the domain/image pairs as \(d_t=t+a_t\) and \(m_t=t+b_t\). The nondecreasing integer sequences \((a_t)\) and \((b_t)\) have values in \(\{0,\ldots,k\}\), because there are only \(k\) omitted points in each of the domain and image. Let \(\delta_t=b_t-a_t\). Parity and nilpotency force \(\delta_t\in2\mathbb Z\setminus\{0\}\).

Suppose \(\delta_t\ne\delta_{t+1}\). The admissible-gap conditions rule out gap \((1,1)\), so both gaps are at least \(2\), which gives \(a_{t+1}\geq a_t+1\) and \(b_{t+1}\geq b_t+1\). Interchanging domain and image if necessary, assume \(\delta_t>0\). If \(\delta_t\geq4\), then \(b_t\geq4\) and \(b_{t+1}\geq5\). Otherwise \(\delta_t=2\). If \(\delta_{t+1}\geq4\), then \(b_{t+1}=a_{t+1}+\delta_{t+1}\geq5\). If \(\delta_{t+1}\leq-2\), then
\[
a_{t+1}\geq b_{t+1}+2\geq b_t+3\geq5.
\]
All cases imply \(k\geq5\). Thus when \(k\leq4\), the displacement is constant. Its possible values are the nonzero even integers of absolute size at most \(k\), yielding only the indicated translations.

For translation by \(2\), its domain can be any \((n-k)\)-subset of \([n-2]\), giving \(\binom{n-2}{n-k}\) distinct maps; translation by \(-2\) gives the same count. Translation by \(4\) or \(-4\) first becomes possible at \(k=4\), contributing one map each there. Distinct nonempty translations do not overlap. Taking \(k=2,3,4\) proves the three coefficient identities, and taking \(k=0,1\) proves the two vanishing coefficients.

**Sharpness.** For \(n\geq7\), take the graph with domain sequence \((1,3,4,\ldots,n-4)\) and image sequence \((3,7,8,\ldots,n)\). Its two sequences have length \(n-5\) and satisfy the parity and fence-gap criterion: the first gaps are \(2\) and \(4\), followed by simultaneous gaps of \(1\). It has no fixed points, hence is nilpotent. Its first displacement equals \(2\) and every subsequent displacement equals \(4\), so it is not a restriction of a single translation. This realizes exactly defect \(5\), proving optimality of the threshold.

## Verification

The accompanying standalone Python 3 program `checker.py` implements the polynomial recurrence, independently enumerates all increasing parity-preserving fence isomorphisms by directly comparing fence-order relations, and tests nilpotency by traversing partial functional graphs. It compares every rank coefficient for \(1\leq n\leq9\), verifies the sharp high-rank formulas through \(n=20\), and tests the explicit nonuniform defect-five examples for \(7\leq n\leq20\). Invocation: `python3 checker.py`; successful output is `VERIFY_OK`. The proof above, not finite enumeration, establishes the assertions for arbitrary \(n\).

## Relationship to prior work

Sareeto and Koppitz [1] characterize this precise inverse monoid and compute its generating rank; their structural characterization is used as an established premise. Their later work [2] studies maximal subsemigroups of its ideals, while [3] gives a presentation. These are not the rank-refined nilpotent enumeration and defect-five rigidity established here. Laradji and Umar [4] address nilpotent counts in broader order-preserving partial-injection monoids; the fence and parity restrictions are additional simultaneous local graph constraints, and total broad-monoid counts do not directly determine these restricted rank coefficients. The published partial-isometry literature concerns a narrower transformation class and does not cover nonisometric elements of this monoid. Searches for equivalent rank polynomials, nilpotent ideals and translation rigidity did not identify an already stated equivalent theorem, but this does not establish exhaustive bibliographic priority.

## Limitations

The recurrence counts nilpotent elements by rank, not by their exact nilpotency index or conjugacy classes. The operation bound counts arithmetic operations, not bit complexity. The sharp constant-displacement statement covers only positive ranks at defect at most four; no formula for every fixed larger defect is asserted. An inaccessible older article [4] and potentially broader enumerative machinery leave a residual originality risk. No independent audit has been performed.

## References

[1] A. Sareeto and J. Koppitz, *The rank of the semigroup of order-, fence-, and parity-preserving partial injections on a finite set*, arXiv:2208.03202, first posted 2022-08-05, especially Proposition 1.

[2] A. Sareeto and J. Koppitz, *The maximal subsemigroups of the ideals on a monoid of partial injections*, arXiv:2403.06957, 2024-03-11.

[3] A. Sareeto and J. Koppitz, *A presentation for a submonoid of the symmetric inverse monoid*, Ural Mathematical Journal (2023), DOI:10.15826/umj.2023.2.015.

[4] A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving or order-reversing subpermutations*, Journal of Difference Equations and Applications 21 (2015), 269–283, DOI:10.1080/10236198.2015.1005080 (abstract checked; full text not inspected).
