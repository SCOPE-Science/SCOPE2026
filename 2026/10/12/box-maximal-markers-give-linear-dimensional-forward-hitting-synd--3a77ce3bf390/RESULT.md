# Box-maximal markers give linear-dimensional forward-hitting syndeticity
## Finding
Let \(n,r\ge 1\). Suppose \(f_1,\ldots,f_n:X\to X\) are commuting bounded-to-one Borel maps on a standard Borel space, and let \(F(X)\) be the free part of the induced \(\mathbb N^n\)-action. Then there is a Borel set \(H\subseteq F(X)\) which is \(r\)-forward-independent and has syndeticity \(2nr\). Explicitly, for every \(x\in F(X)\) there is \(\gamma=(\gamma_1,\ldots,\gamma_n)\in\mathbb N^n\) such that
\[
\sum_{i=1}^n\gamma_i\le 2nr
\]
and
\[
f_1^{\gamma_1}\cdots f_n^{\gamma_n}(x)\in H.
\]
This improves the \(2n^2r\) syndeticity bound in Gao--Hu--Zou, Theorem 3.1, with the same hypotheses.

## Assumptions and scope
A set \(H\subseteq F(X)\) is \(r\)-forward-independent when distinct \(x,y\in H\) cannot satisfy
\[
f_1^{\alpha_1}\cdots f_n^{\alpha_n}(x)
=
f_1^{\beta_1}\cdots f_n^{\beta_n}(y)
\]
for vectors \(\alpha,\beta\in\{0,\ldots,r}\^n\) satisfying \(\alpha_i\beta_i=0\) for every \(i\). The theorem concerns only the free part; no assertion is made on points with nontrivial monoid stabilizer. The maps are assumed bounded-to-one exactly as in the transfer theorem used by Gao--Hu--Zou.

## Proof
First consider a free continuous action of \(\mathbb Z^n\) on a zero-dimensional Polish space. Define the finite-range box graph \(B_r\) by joining distinct points \(x,y\) exactly when
\[
y=\delta\cdot x
\quad\text{for some}\quad
\delta\in([-r,r]\cap\mathbb Z)^n.
\]
This graph has bounded degree. The same Linial maximal-independent-set argument used for graph powers in Gao--Hu--Zou, Lemma 3.5, applies to this finite-range graph: a maximal independent set for \(B_r\) is an \(O(\log^* N)\) local problem on the grid, hence every free continuous \(\mathbb Z^n\)-action admits a clopen maximal \(B_r\)-independent set \(H\).

The set \(H\) is \(r\)-forward-independent. Indeed, if distinct \(x,y\in H\) satisfied a forbidden collision with vectors \(\alpha,\beta\in\{0,\ldots,r}\^n\) and \(\alpha_i\beta_i=0\), freeness of the group action would give
\[
y=(\alpha-\beta)\cdot x
\]
up to the harmless choice of sign convention. Every coordinate of \(\alpha-\beta\) lies in \([-r,r]\), so \(x\) and \(y\) would be adjacent in \(B_r\), contradicting independence.

Now fix \(z\). Put
\[
u=(r,\ldots,r)\cdot z.
\]
Maximality of \(H\) in \(B_r\) gives \(h\in H\) and \(\delta\in([-r,r]\cap\mathbb Z)^n\) with \(h=\delta\cdot u\), allowing \(\delta=0\) when \(u\in H\). Hence
\[
h=(r+\delta_1,\ldots,r+\delta_n)\cdot z.
\]
Every coordinate \(r+\delta_i\) lies in \([0,2r]\), and therefore
\[
\sum_{i=1}^n(r+\delta_i)\le 2nr.
\]
Thus the clopen set is a hitting set with syndeticity \(2nr\).

Finally encode these two requirements as the same kind of finite-window locally checkable labeling problem used in Gao--Hu--Zou, but with forward window \(\{0,\ldots,2r}\^n\) and hitting budget \(2nr\). The preceding construction supplies a continuous labeling for every free continuous \(\mathbb Z^n\)-action. The LOCAL equivalence quoted as Gao--Hu--Zou, Theorem 3.2, transfers this to an \(O(\log^* N)\) algorithm on \(\mathbb N^n\), and their Theorem 3.3 transfers that algorithm to every free bounded-to-one Borel \(\mathbb N^n\)-action. The marker set of that labeling is the required Borel \(H\).

## Verification
The load-bearing change is geometric: forward-independence forbids coordinate displacement in the box \([-r,r]^n\), whereas the published proof enforces the stronger graph-distance condition \(\rho\le nr\). Centering a maximal box-independent net at \((r,\ldots,r)\) makes every coordinate of the resulting forward displacement lie in \([0,2r]\), giving the stated \(\ell^1\) budget \(2nr\).

The proof uses no finite experiment or numerical approximation. The two external transfer inputs are the LOCAL equivalence and Borel transfer stated as Theorems 3.2 and 3.3 in the motivating paper.

## Relationship to prior work
Gao, Hu and Zou prove the same existence theorem with syndeticity \(2n^2r\). Their proof chooses a maximal \(nr\)-independent set in the ordinary Schreier graph, shifts by \((nr,\ldots,nr)\), and bounds each resulting coordinate by \(2nr\). The present proof instead matches the forbidden collision geometry coordinatewise and uses a maximal independent set in the box graph, reducing the shift to \((r,\ldots,r)\).

Shinko, Weilacher and Yu provide the LOCAL-to-Borel framework used in the transfer step and prove hyperfiniteness for bounded-to-one commutative monoid actions. No claim is made here to strengthen their hyperfiniteness theorem.

## Limitations
The constant \(2nr\) is an upper bound; optimality is not claimed. The theorem is only for the free part and retains bounded-to-one hypotheses. The full text of the Shinko--Weilacher--Yu preprint was not independently inspected in this verification; its relevant transfer statements were checked as reproduced verbatim in Gao--Hu--Zou. A targeted search found no published \(2nr\) bound, but that does not constitute an exhaustive novelty proof.

## References
1. Su Gao, Xiangxi Hu, Jie Zou, *Borel graphs generated by commuting functions*, arXiv:2608.15422 (first public 2026-08-15), especially Theorem 3.1, Theorems 3.2--3.3 as quoted there, Lemma 3.5, and Proposition 3.4.
2. Forte Shinko, Felix Weilacher, Jing Yu, *Hyperfiniteness of bounded-to-one actions of commutative monoids*, arXiv:2608.18439 (first public 2026-08-19).
3. Nathan Linial, *Locality in distributed graph algorithms*, SIAM Journal on Scientific Computing 21 (1992), 193--201.
