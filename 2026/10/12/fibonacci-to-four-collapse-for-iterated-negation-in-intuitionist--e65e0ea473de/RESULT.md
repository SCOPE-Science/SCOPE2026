# Fibonacci-to-four collapse for iterated negation in intuitionistic non-deterministic truth-tables

## Finding

Consider the three-valued non-deterministic semantics for intuitionistic propositional logic introduced by Leme, Coniglio, and Lopes, with truth values \(\mathbf T,\mathbf U,\mathbf F\). For
\[
\alpha_n=\neg^n p\qquad(n\ge 0),
\]
let the columns be ordered
\[
p,\neg p,\neg^2p,\ldots,\neg^np.
\]

The full initial Nmatrix table, before the paper's support-deletion procedure is applied, has exactly
\[
\boxed{F_{n+3}}
\]
rows, where \(F_0=0\) and \(F_1=1\). For \(n\ge1\), the numbers of initial rows whose last entry is respectively \(\mathbf T,\mathbf U,\mathbf F\) are
\[
\boxed{F_{n+1},\ F_{n+1},\ F_n}.
\]

After the support-deletion procedure stabilizes, the final intuitionistic truth-table has
\[
\boxed{2,\ 3,\ 4,\ 4,\ 4,\ldots}
\]
rows for \(n=0,1,2,3,\ldots\). More precisely, for every \(n\ge2\) its four rows are exactly
\[
\begin{aligned}
A_n&=(\mathbf T,\mathbf F,\mathbf T,\mathbf F,\ldots),\\
B_n&=(\mathbf F,\mathbf U,\mathbf U,\mathbf U,\ldots),\\
C_n&=(\mathbf F,\mathbf U,\mathbf T,\mathbf F,\mathbf T,\ldots),\\
D_n&=(\mathbf F,\mathbf T,\mathbf F,\mathbf T,\mathbf F,\ldots).
\end{aligned}
\]
The deletion process reaches this four-row fixed point in at most two deletion rounds.

Thus this canonical one-variable family exhibits a sharp separation between table generation and table refinement: the initial row count grows as
\[
F_{n+3}\sim \frac{\varphi^{n+3}}{\sqrt5},
\qquad
\varphi=\frac{1+\sqrt5}{2},
\]
while the final table is constant-sized from depth \(2\) onward.

## Assumptions and scope

The statement concerns the specific Nmatrix \(\mathcal M_{IPL}\) and support-deletion procedure defined in the cited paper. "Initial table" means the exhaustive list of partial Nmatrix valuations before unsupported rows are removed. "Final truth-table" means the fixed point obtained by repeatedly enforcing the paper's support condition.

No claim is made about the total implementation cost of finding the fixed point, about arbitrary formulas with implication or binary connectives, or about other non-deterministic semantics for intuitionistic logic.

## Proof

The source restricts atomic valuations to the classical values, so the column \(p\) begins with exactly two rows, one with \(\mathbf T\) and one with \(\mathbf F\). Its negation table is
\[
\mathbf T\mapsto\{\mathbf F\},\qquad
\mathbf U\mapsto\{\mathbf U,\mathbf T\},\qquad
\mathbf F\mapsto\{\mathbf U,\mathbf T\}.
\]

Let \(t_n,u_n,f_n\) be the numbers of initial rows ending in \(\mathbf T,\mathbf U,\mathbf F\) after the column \(\neg^np\). Then
\[
(t_0,u_0,f_0)=(1,0,1)
\]
and the displayed negation table gives
\[
t_{n+1}=u_n+f_n,\qquad
u_{n+1}=u_n+f_n,\qquad
f_{n+1}=t_n.
\]
At \(n=1\) this is \((1,1,1)\). Induction therefore gives, for \(n\ge1\),
\[
(t_n,u_n,f_n)=(F_{n+1},F_{n+1},F_n).
\]
Consequently
\[
t_n+u_n+f_n=2F_{n+1}+F_n=F_{n+3}.
\]

It remains to classify the rows surviving support deletion. In a row \(v\), every occurrence \(v_i=\mathbf U\) must have a supporting row \(w\) with \(w_i=\mathbf F\), while every coordinate at which \(v\) has \(\mathbf T\) must also have \(\mathbf T\) in \(w\).

First apply that condition relative to the full initial table. Suppose a row has already attained \(\mathbf T\) and later contains a first new \(\mathbf U\). Immediately before that \(\mathbf U\) the row has the pattern \(\mathbf T,\mathbf F,\mathbf U\): every \(\mathbf T\) forces the following \(\mathbf F\), and this is the first subsequent branch to \(\mathbf U\). If the \(\mathbf U\) occurs at coordinate \(i\), any support would need \(w_i=\mathbf F\), hence \(w_{i-1}=\mathbf T\). But preservation of the row's \(\mathbf T\) at coordinate \(i-2\) forces \(w_{i-2}=\mathbf T\), which in turn forces \(w_{i-1}=\mathbf F\), a contradiction.

Conversely, if all \(\mathbf U\)'s occur before the first positive-coordinate \(\mathbf T\), every such \(\mathbf U\) has a support in the full table: for a \(\mathbf U\) at coordinate \(i\), choose a valid row that reaches \(\mathbf T\) at \(i-1\), hence \(\mathbf F\) at \(i\), stays \(\mathbf U\) until the required first tail-\(\mathbf T\), and then follows the same forced alternating tail. The all-\(\mathbf U\) row is supported coordinatewise in the same way. Hence the first-round survivors are exactly \(A_n,B_n,D_n\) together with
\[
C_{n,k}=(\mathbf F,\underbrace{\mathbf U,\ldots,\mathbf U}_{k\text{ entries}},
\mathbf T,\mathbf F,\mathbf T,\ldots),
\qquad 1\le k\le n-1.
\]
There are \(n+2\) of them.

Now enforce support inside this smaller family. The row \(A_n\) has \(\mathbf F\) exactly at odd positive coordinates, while \(D_n\) has \(\mathbf F\) exactly at even positive coordinates. The all-\(\mathbf U\) row \(B_n\) has no positive \(\mathbf T\)-requirements, so each of its \(\mathbf U\)'s is supported by one of \(A_n,D_n\). The row \(C_{n,1}=C_n\) has only one \(\mathbf U\), at coordinate \(1\), and \(A_n\) supports it while preserving all later \(\mathbf T\)'s.

For \(k\ge2\), no support exists for at least one of the first two \(\mathbf U\)'s of \(C_{n,k}\). If \(k\) is even, every first-round survivor that preserves the alternating \(\mathbf T\)-tail of \(C_{n,k}\) is either \(D_n\) or some \(C_{n,\ell}\) with even \(\ell\le k\); at coordinate \(1\) these rows have respectively \(\mathbf T\) or \(\mathbf U\), never \(\mathbf F\). Thus the \(\mathbf U\) at coordinate \(1\) is unsupported. If \(k\ge3\) is odd, the possible tail-preserving supporters are \(A_n\) and the \(C_{n,\ell}\) with odd \(\ell\le k\); at coordinate \(2\) they have respectively \(\mathbf T\), \(\mathbf T\) when \(\ell=1\), or \(\mathbf U\) when \(\ell\ge3\), again never \(\mathbf F\). Thus the \(\mathbf U\) at coordinate \(2\) is unsupported. Hence every \(C_{n,k}\) with \(k\ge2\) is deleted in the second round.

Finally \(A_n\) and \(D_n\) contain no \(\mathbf U\)'s, \(B_n\) is supported coordinatewise by \(A_n\) and \(D_n\), and \(C_n\) is supported by \(A_n\). Therefore these four rows form a fixed point, proving the classification.

## Verification

A standalone exact replay independently generates every initial row from the source negation table, applies the support condition literally, and compares the surviving rows with the closed forms above through negation depth \(13\). It also checks the Fibonacci distribution and recurrence through depth \(200\).

Recorded result:

```text
VERIFY_OK 919 exact assertions
```

The finite replay is corroborative; the all-\(n\) statement follows from the recurrence and support classification proved above.

## Relationship to prior work

Leme, Coniglio, and Lopes define the three-valued Nmatrix, restrict atomic variables to \(\mathbf T,\mathbf F\), give the support-deletion algorithm, and derive the general initial-table bound
\[
2^{|sub(\alpha)|}.
\]
They explicitly note that table size depends on the number and shape of subformulas and that even one-variable formulas can be arbitrarily large. Their paper does not state an exact row profile for iterated negation; the full text contains no occurrence of "Fibonacci" or "iterated negation."

For \(\alpha_n\), the generic bound is \(2^{n+1}\). The exact initial count \(F_{n+3}\) therefore replaces the worst-case base \(2\) by the golden-ratio base \(\varphi\), and the support-deletion analysis is stronger still: the final table stabilizes at four rows. Searches under Nmatrix, restricted-Nmatrix, negation-tower, exact-row-count, Fibonacci, and golden-ratio formulations did not locate this specialization in the literature.

## Limitations

The result is specific to pure iterated negation in the Leme--Coniglio--Lopes semantics. It does not imply constant final table size for one-variable formulas involving implication, conjunction, or disjunction.

The four-row theorem measures the size of the stabilized truth-table, not the work required by a particular implementation to generate and delete the initial Fibonacci-many rows. A more efficient implementation could exploit the normal form directly.

The literature search cannot rule out an equivalent observation in unindexed notes or software documentation. Independent audit has not been performed.

## References

1. Renato Leme, Marcelo E. Coniglio, and Bruno Lopes, "A new decision method for Intuitionistic Logic by 3-valued non-deterministic truth-tables (pre-print version)," arXiv:2308.13664, first posted 25 August 2023; related DOI 10.1017/jsl.2025.10174.
