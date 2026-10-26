# Exact polynomial-state Littlestone recurrence for two-row order ideals

## Finding

Let \(P_n=[2]\times[n]\), ordered componentwise, for each integer \(n\ge0\). Interpret every order ideal \(I\subseteq P_n\) as its indicator concept \(h_I:P_n\to\{0,1\}\). Write \(\mathcal J_n\) for this finite concept class, including the empty ideal. Define \(\operatorname{Ldim}\) by the largest depth of a complete binary tree shattered by the class (depth zero for a singleton class).

**Theorem.** For every \(n\ge0\), the exact Littlestone dimension of \(\mathcal J_n\) is given by the four-bound recurrence in the proof. Memoization uses \(O(n^4)\) states and \(O(n^5)\) time. The least \(n\) for which \(\operatorname{Ldim}(\mathcal J_n)\ge d\), for \(1\le d\le10\), is, in increasing order,
\[
1,\ 2,\ 3,\ 5,\ 8,\ 12,\ 17,\ 25,\ 36,\ 52.
\]
In contrast, \(\operatorname{VCdim}(\mathcal J_n)=\min\{n,2\}\). In particular, the finite VC dimension is uniformly bounded while the online mistake dimension diverges logarithmically in \(n\).

## Assumptions and scope

The finite chain \([n]\) is \(\{1,\ldots,n\}\), with \([0]=\varnothing\). Ideals are downward-closed subsets in the componentwise order. Every ideal is uniquely represented by an ordered pair of row lengths \((a,b)\) with \(0\le b\le a\le n\): row one contains columns \(1,\ldots,a\), and row two contains columns \(1,\ldots,b\). A query at row one, column \(t\), returns one exactly when \(a\ge t\); a query at row two, column \(t\), returns one exactly when \(b\ge t\). The problem is ordinary deterministic realizable online binary prediction, with adversarial instance selection and feedback.

For integer endpoints \(0\le A\le B\le n\) and \(0\le C\le D\le n\), let \(\mathcal V(A,B,C,D)\) be the subfamily of pairs satisfying \(A\le a\le B\), \(C\le b\le D\), and \(b\le a\). Only nonempty subfamilies are used. Put \(F(A,B,C,D)=\operatorname{Ldim}(\mathcal V(A,B,C,D))\).

## Proof

**Step 1 (four-interval normal form).** Fix any finite sequence of labeled membership observations. Every observation constrains exactly one of \(a,b\) by a lower or upper bound. Their intersection is therefore \(\mathcal V(A,B,C,D)\) for suitable endpoints, subject to \(b\le a\). The constraint \(b\le a\) allows the harmless normalization
\[
 A\gets\max\{A,C\},\qquad D\gets\min\{D,B\}.
\]
Indeed, every feasible pair already obeys those sharpened bounds, and sharpening removes no pair. For a normalized nonempty state, \(A\le B\), \(C\le D\), \(A\ge C\), and \(D\le B\); the pair \((A,C)\) witnesses nonemptiness.

**Step 2 (exact recurrence).** For a normalized state, a nonconstant row-one query has threshold \(t\) with \(A<t\le B\); its zero and one branches are, respectively, \(\mathcal V(A,t-1,C,D)\) and \(\mathcal V(t,B,C,D)\). A nonconstant row-two query similarly has \(C<t\le D\), with branches \(\mathcal V(A,B,C,t-1)\) and \(\mathcal V(A,B,t,D)\). Every displayed branch is nonempty: the first kind is witnessed by \((A,C)\) and \((t,C)\); the second by \((A,C)\) and \((\max\{A,t\},t)\). All other queries are constant on the current state, so they cannot root a shattered tree of positive depth.

If a state contains exactly one pair, its dimension is zero; in normal form this is equivalent to \(A=B\) and \(C=D\). Otherwise the definition of a shattered complete binary tree gives the following exact, terminating recurrence:
\[
\begin{aligned}
F(A,B,C,D)=\max\bigg\{&\max_{A<t\le B}\left[1+\min\{F(A,t-1,C,D),F(t,B,C,D)\}\right],\\
&\max_{C<t\le D}\left[1+\min\{F(A,B,C,t-1),F(A,B,t,D)\}\right]\bigg\}.
\end{aligned}
\]
An empty inner maximum contributes zero, and each recursive argument is normalized before evaluation. Every split strictly reduces the number of feasible pairs on both branches, proving termination and, by induction on this number, equality with Littlestone dimension rather than merely a lower or upper bound.

**Step 3 (complexity).** Each state consists of four integer endpoints from \(\{0,\ldots,n\}\), hence there are at most \((n+1)^4\) normalized states. At most \(2n\) threshold queries are considered per state. Memoized evaluation therefore takes \(O(n^5)\) integer comparisons and \(O(n^4)\) stored states. Initially all \(0\le b\le a\le n\) are possible, so \(\operatorname{Ldim}(\mathcal J_n)=F(0,n,0,n)\). The \(n=0\) case is the singleton empty ideal and has dimension zero.

**Step 4 (sharp finite thresholds).** The exact integer recurrence, evaluated in the supplied standalone program, gives the following adjacent boundary pairs:

| Target depth \(d\) | Last failing \(n\) | Its dimension | First succeeding \(n\) | Its dimension |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | 0 | 1 | 1 |
| 2 | 1 | 1 | 2 | 2 |
| 3 | 2 | 2 | 3 | 3 |
| 4 | 4 | 3 | 5 | 4 |
| 5 | 7 | 4 | 8 | 5 |
| 6 | 11 | 5 | 12 | 6 |
| 7 | 16 | 6 | 17 | 7 |
| 8 | 24 | 7 | 25 | 8 |
| 9 | 35 | 8 | 36 | 9 |
| 10 | 51 | 9 | 52 | 10 |

The class \(\mathcal J_n\) is a restriction of a subfamily of \(\mathcal J_{n+1}\): extend an ideal with no elements in the new last column. Thus \(\operatorname{Ldim}(\mathcal J_n)\) is nondecreasing in \(n\), and the listed adjacent evaluations prove every minimum without requiring scans of intervening sizes. For \(n=52\), an independently checked complete depth-ten shattered tree has \(1024\) consistent root-to-leaf paths (supplied as a standalone certificate).

**Step 5 (VC dimension and growth).** Every set of three queried grid cells includes two in the same row. Their membership indicators are nested threshold predicates, so those two cannot realize all four binary label pairs; consequently no triple is VC-shattered. For \(n\ge2\), the two cells \((1,2)\) and \((2,1)\) are shattered by the four ideals with row lengths \((0,0)\), \((2,0)\), \((1,1)\), and \((2,1)\), giving VC dimension two. For \(n=1\), one query is shattered, while \(n=0\) has none. This proves \(\operatorname{VCdim}(\mathcal J_n)=\min\{n,2\}\).

For growth, put \(m=\lfloor n/2\rfloor\), and restrict to \(m\le a\le n\) and \(0\le b\le m\). The inequality \(b\le a\) is then automatic, leaving two independent finite threshold classes, of sizes \(n-m+1\) and \(m+1\). Concatenating complete mistake trees on their disjoint query rows yields
\[
 \operatorname{Ldim}(\mathcal J_n)\ge \lfloor\log_2(n-m+1)\rfloor+\lfloor\log_2(m+1)\rfloor.
\]
The \((n+1)(n+2)/2\) distinct ideals furnish the upper bound \(\lfloor\log_2((n+1)(n+2)/2)\rfloor\), since a shattered depth-\(d\) tree needs at least \(2^d\) concepts. Hence the dimension grows as \(2\log_2 n+O(1)\). The finite threshold table is stronger than either general cardinality bound.

## Verification

Run `python3 verify.py` and then `python3 check_witness.py` with Python 3 and no additional packages. The program implements the proved normalized four-endpoint recurrence; separately, for each \(0\le n\le16\), it constructs every ideal as an explicit membership bit vector and evaluates the unrestricted hypothesis-subset minimax recurrence. These independent procedures agree on all seventeen sizes. The program checks both sides of each of the ten threshold transitions; these evaluations cover up to \(n=52\), using \(708345\) distinct normalized cached states during this run. It constructs a complete shattered tree for \(n=52\), writes `depth10_n52_witness.json`, and separately replays all \(1024\) paths by checking nonempty sets of actual ideals at every branch. The separate `check_witness.py` reads and validates the existing witness file without recomputing or rewriting it. The supplied `verification_output.txt` records both successful executions. The certificate and the recurrence do not rely on approximate numerical arithmetic.

## Relationship to prior work

Littlestone dimension measures adaptive shattering and online mistake complexity. Malliaris and Moran [1] develop its connection with model-theoretic stability and excellent sets, and Ghazi, Golowich, Kumar and Manurangsi [2] prove generic upper bounds under Boolean aggregation. These frameworks justify considering finite rank profiles but do not, in the inspected definitions and main-result statements, give the exact four-bound rank or the sharp grid thresholds here. The one-dimensional threshold class has only one unknown cut, while the two-row ideal class has two cuts linked by an order inequality; this creates triangular version spaces rather than an unrestricted Cartesian product.

The class is not the class of intervals on a chain. In particular, at \(n=3\) the two-row ideal class has Littlestone dimension three, while the interval-indicator class on a three-point chain has dimension two. Membership queries on a two-row grid test one of the two cut coordinates independently; interval queries on a single chain test their conjunction. Thus an interval-class recurrence does not supply this exact result merely by renaming endpoints.

## Limitations

The recurrence determines every finite dimension, but no explicit closed formula for all sharp depth thresholds is asserted. The displayed threshold census covers only depths one through ten; the logarithmic growth bounds cover all \(n\). The accompanying programs prove the finite integer computations conditional on ordinary execution semantics, not any claim of independent formal proof or full historical novelty. Literature-priority searches may miss equivalent results described as nested thresholds, monotone matrix paths, or online prediction of Young diagrams. No independent mathematical audit has been performed.

## References

[1] M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, first available 2021-08-12, arXiv:2108.05569, https://arxiv.org/abs/2108.05569 .

[2] B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, first available 2020-07-07, arXiv:2007.03668, https://arxiv.org/abs/2007.03668 .
