# Jump-and-symmetry formula for minimum rank in cyclic partial-translation automata

## Finding

**Theorem.** For each integer \(n\ge2\), each integer \(1\le h<n\), and each subset \(A\subseteq\mathbb Z/n\mathbb Z\), define the complete binary deterministic automaton with states \(Q=\mathbb Z/n\mathbb Z\) and letters
\[
a(i)=i+1\pmod n,\qquad
b(i)=\begin{cases}i+h\pmod n,&i\in A,\\i,&i\notin A.\end{cases}
\]
Let its rotational stabilizer be \(H(A)=\{t\in Q:A+t=A\}\), write \(s=|H(A)|\), \(m=n/s\), and define the minimum transformation rank by
\[
r_{\min}(n,h,A)=\min_{w\in\{a,b\}^*}|Qw|.
\]
Then, without any restriction on the active set, its cardinality, or its symmetry,
\[
\boxed{r_{\min}(n,h,A)=s\gcd(m,h).}
\]
In particular this automaton is synchronizing if and only if \(H(A)=\{0\}\) and \(\gcd(n,h)=1\).

## Assumptions and scope

States and sums are taken modulo \(n\); the jump \(h\) is an integer from \(1\) to \(n-1\). Word actions are applied from left to right. The empty and full sets \(A\) are included; then \(s=n\), \(m=1\), and the minimum rank is \(n\). The assertion concerns the smallest possible image cardinality, **not** the length of a shortest word attaining that rank. The word \(a\) is a full cycle. No regularity or interval assumption is placed on \(A\).

## Proof

**Step 1: Quotient and an equivariant lower bound.** The stabilizer \(H=H(A)\) is a subgroup of the cyclic group \(Q\) of order \(s\), so its orbits are the cosets modulo \(m=n/s\). Because \(A\) is invariant under \(H\), each of \(a\) and \(b\) commutes with every translation \(i\mapsto i+t\) for \(t\in H\). Therefore the image under any word is a union of entire \(H\)-orbits, and each word induces a well-defined map on the quotient \(Q/H\cong\mathbb Z/m\mathbb Z\). The quotient active set \(A'\subseteq\mathbb Z/m\mathbb Z\) consists of the images of \(A\); the induced letters are again \(i\mapsto i+1\) and the partial jump by \(h\) on \(A'\). In particular, for every word \(w\),
\[
|Qw|=s\,| (\mathbb Z/m\mathbb Z)w|.
\]
The set \(A'\) has trivial rotational stabilizer: any nontrivial stabilizing translation on the quotient would lift to an additional stabilizing translation on \(Q\), contradicting the definition of \(H\).

Put \(d=\gcd(m,h)\). On the quotient, letter \(b\) preserves every residue class modulo \(d\), while \(a\) sends each residue class to the next. Hence any word sends the \(d\) distinct initial residue classes bijectively to \(d\) distinct residue classes (as labels); their images cannot intersect. It follows that every word has rank at least \(d\) in the quotient, hence at least \(sd\) upstairs.

**Step 2: Aperiodicity supplies each inverse extension.** The case \(m=1\), or more generally \(d=m\), already has rank \(m\) and requires no construction. Suppose \(d<m\), so \(A'\) is aperiodic and \(h\not\equiv0\pmod m\). For each \(t\in\mathbb Z/m\mathbb Z\), the conjugate word \(a^{-t}ba^t\) induces
\[
b_t(i)=\begin{cases}i+h,&i-t\in A',\\i,&i-t\notin A'.\end{cases}
\]
Here the powers \(a^{-t}\) are represented by nonnegative powers of the cycle \(a\), so \(b_t\) belongs to the original transformation semigroup.

Fix one residue class \(C\) modulo \(d\). Because \(h/d\) and \(m/d\) are coprime, its elements are a single cycle under addition by \(h\), of size \(L=m/d\). Let
\[
I_\ell(u)=\{u,u+h,\ldots,u+(\ell-1)h\},\qquad1\le\ell<L,
\]
be an interval along that cycle, and set \(p=u-h\) and \(v=u+(\ell-1)h\). The separation \(v-p=\ell h\) is nonzero modulo \(m\). Since \(A'\) has no nonzero period, there exists a translation \(t\) such that
\[
p-t\in A'\quad\text{and}\quad v-t\notin A'.
\]
Indeed, if no such \(t\) existed, the equality of the cardinalities of \(A'\) and its translate by \(\ell h\) would force equality of those sets, giving a forbidden period.

For this \(t\), direct inspection of the partial jump shows the **exact inverse-image identity**
\[
b_t^{-1}\bigl(I_\ell(u)\bigr)=I_{\ell+1}(u-h).
\]
The predecessor \(p\) enters because it is active and maps to \(u\); the right endpoint \(v\) stays inside because it is inactive. Every other point of the old interval maps inside, and no point farther to the left can enter. All other residue classes modulo \(d\) are disjoint and cannot contribute to this inverse image.

Beginning with any singleton in \(C\), repeat this identity \(L-1\) times. Reversing the order of the chosen conjugate letters gives a word mapping **all** of \(C\) to a single point. Do this successively for each of the \(d\) residue classes. Every conjugate \(b_t\) preserves each residue class, so subsequent steps cannot unmerge a class already collapsed. The resulting quotient word has an image of exactly \(d\) states. Lifting that word to the original automaton gives rank \(sd\). This attains the lower bound of Step 1 and proves the formula.

**Synchronization criterion.** Rank one means \(s\gcd(m,h)=1\). Both factors are positive integers, so \(s=1\) and then \(m=n\), \(\gcd(n,h)=1\), as claimed.

## Verification

The included standard-library program `verify.py` computes the minimum reachable rank independently by breadth-first search on subsets for all \(n=2,\ldots,10\), all \(1\le h<n\), and every active set. It also constructs the inverse-image words for all patterns through \(n=12\), and deterministic random larger cases, verifying their full original-state images. An observed successful run printed:

```
VERIFY_OK exhaustive_subset_bfs_cases=16388 constructive_witness_cases=83324 certified_inverse_expansions=769634
```

The proof above, rather than exhaustive finite testing, establishes the statement for every \(n\). The checker can be replayed using `python3 verify.py` with no third-party dependencies.

## Relationship to prior work

The minimum-rank problem for deterministic and circular automata is studied by Kari, Ryzhikov, and Varonka, whose Theorem 3 bounds the length of a minimum-rank word in a circular automaton **once its minimum rank is specified**; it does not supply this value for the present partial-jump automata. Volkov studies when primitive automata synchronize, and Rystsov and Szykuła establish synchronizing criteria for several transformation-letter families, including semiconstant letters; neither inspected result gives the arbitrary-active-set, arbitrary-jump minimum-rank formula. The special case \(h=1\) is a separate predecessor of the present rank classification, and the case of singleton \(A\) admits earlier synchronization analyses. The combined dependence on rotational symmetry and the jump gcd is the point of the stated formula.

## Limitations

The theorem determines minimum image cardinality only; it does not determine the shortest length of a minimum-rank word. For \(h\) coprime to \(n\), the formula reduces to the unit-jump symmetry case after relabeling. The substantive new cases are simultaneous nontrivial jump divisibility and arbitrary active-set structure. The literature comparison cannot rule out an unindexed equivalent statement; no independent mathematical audit has been performed.

## References

1. J. Kari, A. Ryzhikov, E. Varonka, *Words of Minimum Rank in Deterministic Finite Automata*, in Developments in Language Theory (2019), DOI:10.1007/978-3-030-24886-4_5. Author manuscript: https://www.utupub.fi/bitstreams/df55c125-3bb6-4f4f-b3ef-3799b3cff98c/download .
2. M. Volkov, *Synchronization of primitive automata*, arXiv:2306.13317v1 (first public 2023-06-23): https://arxiv.org/abs/2306.13317 .
3. I. Rystsov, M. Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302v1 (first public 2023-07-03): https://arxiv.org/abs/2307.01302 .
