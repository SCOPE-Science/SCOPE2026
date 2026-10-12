# Metric self-dual completion doubles the full source support hierarchy
## Finding

Let
\[
C\le\mathbb F_2^m
\]
be a binary linear code of dimension \(k\). Apply Ostrovsky's metric self-dual completion with any threshold
\[
H\ge2m.
\]
Thus the source theorem supplies a self-dual code
\[
A\le\mathbb F_2^N
\]
and a linear embedding
\[
\tau:\mathbb F_2^m\hookrightarrow\mathbb F_2^N
\]
with
\[
\operatorname{wt}(\tau(x))=2\operatorname{wt}(x)
\]
for every \(x\), and
\[
\tau(C)=\{a\in A:\operatorname{wt}(a)\le H\}.
\]

For every
\[
1\le r\le k,
\]
the map \(\tau\) induces a bijection between all \(r\)-dimensional subcodes \(U\le C\) and all \(r\)-dimensional subcodes \(D\le A\) whose support size is at most \(H\). Under this bijection,
\[
|\operatorname{Supp}(\tau(U))|
=
2|\operatorname{Supp}(U)|.
\]

Consequently, if
\[
C^{(r)}_s
=
\#\{U\le C:\dim U=r,\ |\operatorname{Supp}(U)|=s\}
\]
and \(A^{(r)}_j\) is defined analogously, then throughout the entire short-support range
\[
j\le H
\]
one has
\[
A^{(r)}_j
=
\begin{cases}
C^{(r)}_{j/2},&j\text{ even},\\
0,&j\text{ odd}.
\end{cases}
\]

In particular, writing \(d_r\) for generalized Hamming weights,
\[
d_r(A)=2d_r(C)
\qquad
(1\le r\le k).
\]
Thus the completion preserves the **full generalized Hamming weight hierarchy of the source code**, not only its minimum distance, with the same factor-of-two scaling.

## Assumptions and scope

Ostrovsky's Main Theorem 1 applies for every integer \(m\ge1\) and every threshold \(H\ge2m\). It constructs a binary self-dual code \(A\), together with a linear embedding \(\tau\), satisfying four clauses. Only two are needed here:

1. exact weight scaling,
\[
\operatorname{wt}(\tau(x))=2\operatorname{wt}(x)
\quad
(x\in\mathbb F_2^m),
\]
2. exact isolation of short codewords,
\[
\tau(C)=\{a\in A:\operatorname{wt}(a)\le H\}.
\]

For an \(r\)-dimensional subcode \(U\), its support is
\[
\operatorname{Supp}(U)
=
\{j:\exists u\in U\text{ with }u_j\ne0\}.
\]
The \(r\)-th generalized Hamming weight is
\[
d_r(C)
=
\min_{\substack{U\le C\\\dim U=r}}
|\operatorname{Supp}(U)|.
\]

The theorem below concerns the first \(k\) generalized weights of \(A\), where \(k=\dim C\). The completion has dimension \(N/2\), so it generally has additional generalized weights beyond this source range; no formula for those later weights is claimed.

## Proof

The key binary identity is that for every \(r\)-dimensional subspace \(U\),
\[
\sum_{u\in U}\operatorname{wt}(u)
=
2^{r-1}|\operatorname{Supp}(U)|.
\]
Indeed, at every active coordinate, evaluation on \(U\) is a nonzero linear functional. Exactly half of the \(2^r\) vectors in \(U\) therefore have a \(1\) in that coordinate. Summing coordinate by coordinate proves the identity.

Now let \(U\le C\) have dimension \(r\). Since \(\tau\) is linear and injective, \(\tau(U)\) also has dimension \(r\). Applying the support-sum identity twice and using exact weight scaling gives
\[
\begin{aligned}
2^{r-1}|\operatorname{Supp}(\tau(U))|
&=\sum_{u\in U}\operatorname{wt}(\tau(u))\\
&=2\sum_{u\in U}\operatorname{wt}(u)\\
&=2^r|\operatorname{Supp}(U)|.
\end{aligned}
\]
Hence
\[
|\operatorname{Supp}(\tau(U))|
=
2|\operatorname{Supp}(U)|.
\]
Because every source support has size at most \(m\), every image support has size at most
\[
2m\le H.
\]
Thus every \(r\)-subcode of \(C\) maps to an \(r\)-subcode of \(A\) in the short-support range.

Conversely, let \(D\le A\) have dimension \(r\) and
\[
|\operatorname{Supp}(D)|\le H.
\]
Every vector \(d\in D\) then satisfies
\[
\operatorname{wt}(d)
\le
|\operatorname{Supp}(D)|
\le H.
\]
By the short-codeword isolation clause of the source theorem,
\[
d\in\tau(C).
\]
Therefore
\[
D\le\tau(C).
\]
Since \(\tau\) is a linear isomorphism from \(C\) onto \(\tau(C)\), there is a unique \(r\)-dimensional \(U\le C\) with
\[
D=\tau(U).
\]
This proves the claimed bijection, and the already established support-scaling identity proves the short higher-weight-spectrum formula.

Finally fix \(1\le r\le k\). If \(U\le C\) realizes \(d_r(C)\), then
\[
d_r(A)
\le
|\operatorname{Supp}(\tau(U))|
=
2d_r(C)
\le2m\le H.
\]
Hence an \(r\)-subcode of \(A\) realizing \(d_r(A)\) lies in the short-support range and must equal \(\tau(U')\) for some \(r\)-subcode \(U'\le C\). Therefore
\[
d_r(A)
=
2|\operatorname{Supp}(U')|
\ge
2d_r(C).
\]
Together with the upper bound this yields
\[
d_r(A)=2d_r(C).
\]

## Verification

`artifacts/verify.py` independently stress-tests the abstract implication used above.

For every binary linear code of every length
\[
1\le m\le4,
\]
the script constructs a simple auxiliary extension having the two premises used in the proof: a linear duplication embedding that doubles every Hamming weight, and a disjoint high-weight summand whose nonzero words all lie above the cutoff \(H=2m\). This auxiliary extension is not used as a substitute for the source's self-dual construction; it isolates and tests the new support-theoretic deduction from the two source clauses.

For every source code and every admissible subcode dimension, the verifier enumerates all subspaces exactly, computes their support-size histograms, and checks that the complete histogram below the cutoff is obtained by doubling the source support sizes. It also computes every generalized Hamming weight on both sides and checks
\[
d_r(\text{extension})=2d_r(C).
\]

The script separately verifies the identity
\[
\sum_{u\in U}\operatorname{wt}(u)
=
2^{r-1}|\operatorname{Supp}(U)|
\]
for every enumerated binary subspace.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Ostrovsky's Main Theorem 1 proves exact doubling of individual Hamming weights, exact doubling of source-coset distances, and the fact that all codewords of the completed self-dual code of weight at most \(H\) are exactly the embedded source codewords. The paper explicitly derives preservation of minimum distance and uses the construction for hardness results.

The inspected full text does not discuss generalized Hamming weights, higher weights, weight hierarchies, or higher-weight spectra. Those invariants are strictly richer than minimum distance because they minimize the union of supports of entire subcodes rather than the weight of one codeword.

Generalized Hamming weights are classical, beginning with Wei's 1991 work, and higher-weight spectra have also been studied for self-dual and design-derived codes. Those results provide definitions, duality, and code-specific calculations. They do not state that the 2026 metric self-dual completion preserves every source generalized weight, nor do they identify the complete short-support subcode spectrum of that completion.

The new step is to combine the source theorem's **linear weight-doubling embedding** with its **exact low-weight isolation**. The first property doubles the support of every embedded subcode through the binary support-sum identity, while the second rules out any competing short subcode outside the embedded source.

## Limitations

The equality
\[
d_r(A)=2d_r(C)
\]
is asserted only for
\[
1\le r\le\dim C.
\]
The self-dual completion generally has larger dimension, and its later generalized weights can depend on the chosen host construction.

The proof is binary. The support-sum identity has a \(q\)-ary analogue, but the accepted statement is restricted to the exact binary completion in the source theorem.

No claim is made that two completions of the same source code are equivalent. The result identifies their common short-support spectrum forced by the theorem's guarantees.

## References

1. Rafail Ostrovsky, *Metric Self-Dual Completion and Optimal Additive Hardness for Quantum and Graph-State Distance*, arXiv:2609.22669v1, first public 19 September 2026.
2. Victor K.-W. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418, DOI 10.1109/18.133259.
3. Steven T. Dougherty and Reshma Ramadurai, *Higher Weights of Codes from Projective Planes and Biplanes*, Mathematics Journal of Okayama University 49 (2007), 149--161.
