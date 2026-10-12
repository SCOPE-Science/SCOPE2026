# Exact quasi-idempotent generating rank of the singular order-preserving transformation semigroup

## Finding

For every integer \(n\ge4\), let \(\mathcal O_n\) be the semigroup of all **singular**, order-preserving full self-maps of the chain \([n]=\{1,\ldots,n\}\), with multiplication given by composition. A quasi-idempotent is a map \(f\) with \(f\ne f^2=f^4\). Let \(\operatorname{qrank}(\mathcal O_n)\) be the least size of a subset of quasi-idempotents that generates \(\mathcal O_n\). Then

\[
\boxed{\operatorname{qrank}(\mathcal O_n)=\left\lfloor\frac{6n}{5}\right\rfloor-\mathbf1_{\{n\equiv1\pmod5\}}.}
\]

In particular, \(\operatorname{qrank}(\mathcal O_9)=10\), contradicting the sharpness conjecture in Remark 1 of Imam--Ibrahim--Garba--Usman--Idris (2023), which predicted \(\lceil3(n-2)/2\rceil=11\) at \(n=9\). One size-ten generating set is \(\{\delta_2,\delta_3,\delta_5,\delta_6,\delta_8,\mu_2,\mu_3,\mu_5,\mu_7,\mu_8\}\), with the generators defined below.

## Assumptions and scope

All maps have domain **and** codomain \([n]\); singular excludes the identity, the only increasing bijection. The result is purely combinatorial, with no field or characteristic assumptions. The generators of image rank \(n-1\) can be indexed by a collapsed adjacent pair \(j,j+1\) (\(1\le j\le n-1\)) and an omitted image value \(k\) (\(1\le k\le n\)); denote the unique such order-preserving map by \(e_{j,k}\). For \(2\le i\le n-1\), set

\[
\delta_i=e_{i,i-1},\qquad \mu_i=e_{i-1,i+1}.
\]

Precisely these \(2(n-2)\) rank-\(n-1\) maps are quasi-idempotent; this fact and the generation of \(\mathcal O_n\) by all rank-\(n-1\) elements are established in the 2023 motivating paper. The arguments here use these known facts and independently analyze which subsets generate.

## Proof

**1. Rank-preserving multiplication and a connectivity criterion.** If \(e_{j,k}\) is followed by \(e_{j',k'}\), the composite has rank \(n-1\) exactly when \(k=j'\) or \(k=j'+1\). In that case its kernel and image are respectively those of the first and second factors, so its pair of indices is \((j,k')\). Thus a selected family generates every rank-\(n-1\) map if and only if, in the directed graph with vertices \(R_j\) and \(L_k\), arcs \(R_j\to L_k\) for selected \(e_{j,k}\), and fixed arcs \(L_k\to R_j\) for \(k\in\{j,j+1\}\), each \(R_j\) reaches every \(L_k\). Because every \(L_k\) has at least one fixed outgoing arc, this is equivalent to strong connectivity of the whole graph. Products cannot increase rank, so lower-rank generators cannot replace any rank-\(n-1\) generator. Conversely, generating the whole top rank stratum generates the full singular semigroup by its known idempotent generation.

**2. Local characterization of generating subsets.** Write \(D\) and \(U\) for the sets of indices of the selected \(\delta\)'s and \(\mu\)'s, and put \(N=n-1\). Compressing each two-step path \(R\to L\to R\) produces a directed graph on \(R_1,\ldots,R_N\). A selected \(\delta_i\) adds arcs from \(R_i\) to \(R_{i-1}\) and, when available, \(R_{i-2}\); a selected \(\mu_i\) adds arcs from \(R_{i-1}\) to \(R_i\) and, when available, \(R_{i+1}\). Strong connectivity is therefore equivalent to the following four families of clauses:

\[
\begin{aligned}
&j\in D\ \lor\ j+1\in U &&(1\le j\le N),\\
&k+1\in D\ \lor\ k-1\in U &&(1\le k\le n),\\
&t\in U\ \lor\ t+1\in U &&(1\le t<N),\\
&t+1\in D\ \lor\ t+2\in D &&(1\le t<N),
\end{aligned}
\]

where membership outside \(\{2,\ldots,N\}\) is false. The first family says that every \(R_j\) has an outgoing arc, the second that every \(L_k\) has a selected incoming arc, and the last two require crossings of every proper prefix cut of the compressed graph in both directions.

For sufficiency, suppose the conditions hold but the compressed graph is not strongly connected. Choose a sink strongly connected component \(S\). Every arc of length two is accompanied by an arc from the same source to the intervening vertex. Hence, if a strongly connected sink component contained vertices on both sides of an omitted intermediate vertex, a path across the omission would force an outgoing arc from \(S\), impossible. Thus \(S\) is an interval \([a,b]\) of vertices. A singleton sink is excluded by the first family. If \(a>1\), the leftward-crossing clause at \(a-1\) forces an arc from \(R_a\) or \(R_{a+1}\), both in \(S\), to the left, a contradiction. If \(a=1\) and \(b<N\), the rightward-crossing clause at \(b\) similarly forces an arc out of \(S\). Therefore the compressed graph is strongly connected, and the second family incorporates every \(L_k\). Necessity follows from outgoing/incoming degree and prefix-cut conditions.

**3. Reduction to a finite maximum-weight word problem.** Let \(x_i\) (respectively \(y_i\)) be 1 when \(\delta_i\) (respectively \(\mu_i\)) is omitted, and 0 when selected. The clauses are equivalent to the boundary conditions

\[
x_2=x_3=x_N=y_2=y_{N-1}=y_N=0
\]

and the local exclusions, whenever all subscripts are in range,

\[
x_ix_{i+1}=0,\qquad y_iy_{i+1}=0,\qquad x_i y_{i+1}=0,\qquad x_i y_{i-2}=0.
\]

The minimum generating-set size is \(2(n-2)\) minus the maximum number of omitted generators under these constraints. Encode the pair \((x_i,y_i)\) by a two-bit integer \(s_i\in\{0,1,2,3\}\), with bit 1 representing \(x_i\) and bit 2 representing \(y_i\). Form the \(16\)-state max-plus transfer matrix \(T\), whose states are \((a,b)\in\{0,1,2,3\}^2\). Its entry from \((a,b)\) to \((b,c)\) equals the number of set bits of \(c\), provided

\[
(c\mathbin{\&}1)(b\mathbin{\&}1)=0,\quad
(c\mathbin{\&}2)(b\mathbin{\&}2)=0,\quad
(c\mathbin{\&}2)(b\mathbin{\&}1)=0,\quad
(c\mathbin{\&}1)(a\mathbin{\&}2)=0;
\]

all other entries are \(-\infty\). Here \(\&\) denotes bitwise AND and tropical multiplication takes the maximum of sums.

For \(n\ge6\), the maximum omitted count is

\[
F_n=\max_{b\in\{0,2\},\ a\in\{0,1\}}
\left(\operatorname{wt}(b)+(T^{n-4})_{(0,b),(a,0)}\right),
\]

where \(\operatorname{wt}\) counts set bits. This encodes the boundary constraints at the first two and last two columns.

**4. Exact finite transfer identity and the formula.** The explicit \(16\times16\) matrix has the entrywise max-plus identity

\[
T^9=T^4+4,
\]

with \(-\infty+4=-\infty\). This is an exact finite integer identity: the included self-contained `checker.py` constructs every entry using the four exclusion tests above, performs max-plus matrix multiplication with integer/negative-infinity values, and asserts all \(256\) equalities. Associativity gives \(T^{h+5}=T^h+4\) for **every integer \(h\ge4\)**, not merely tested powers. Hence \(F_{n+5}=F_n+4\) and the minimum rank increases by 6 for every \(n\ge8\). Exact transfer evaluation gives ranks \(9,10,12,12,14\) for \(n=8,9,10,11,12\), respectively, while the boundary cases \(n=4,5,6,7\) give \(4,6,6,8\). These nine bases and the recurrence yield the displayed closed formula for every \(n\ge4\).

## Verification

Run `python3 checker.py` in a directory containing that file. It checks the finite \(16\times16\) identity with exact integer max-plus arithmetic, compares the formula with the derived transfer expression for \(4\le n\le100\), and checks all subsets of candidate generators against direct rank-\(n-1\) product closure for \(4\le n\le8\). It also verifies the explicit ten-generator construction at \(n=9\). These exhaustive finite tests corroborate the structural semigroup reduction. The finite matrix identity, combined with associative matrix multiplication, is the certificate that establishes the infinite recurrence.

## Relationship to prior work

Imam, Ibrahim, Garba, Usman and Idris (2023), Theorem 2, prove that the \(2(n-2)\) quasi-idempotents of rank \(n-1\) generate \(\mathcal O_n\). Their Theorems 3--4 compute the cases \(n=4,5\) and the upper bound \(\lceil3(n-2)/2\rceil\). Remark 1 suggests this bound is sharp; the exact formula above disproves that suggestion from \(n=9\) onward in many residue classes. The 2024 partial-transformation analogue establishes a different upper bound. The 2026 follow-up on ideals and factorization lengths does not state this minimum-generator formula. Standard earlier results on ordinary and idempotent ranks are used only as background.

## Limitations

The result applies to the **singular full** order-preserving semigroup, not all partial maps or arbitrary full transformations. The formula is exact for \(n\ge4\) but does not classify the total number of distinct minimum generating subsets (although the transfer mechanism can be extended to that enumeration). Novelty assessment is based on the inspected literature and indexed searches; a differently presented earlier equivalent may exist. No independent audit or external formal certification is asserted.

## References

1. A. T. Imam, S. Ibrahim, G. U. Garba, L. Usman, A. Idris, *Quasi-idempotents in finite semigroup of full order-preserving transformations*, Algebra and Discrete Mathematics 35 (2023), 62--72, DOI: 10.12958/adm1846. Full text: https://admjournal.luguniv.edu.ua/index.php/adm/article/download/1846/pdf
2. A. T. Imam, L. Usman, A. Idris, S. Ibrahim, *Product of quasi-idempotents in finite semigroup of partial order-preserving transformations*, International Journal of Mathematical Sciences and Optimization 10 (2024), 53--59, https://www.ajol.info/index.php/ijmso/article/view/265112
3. A. T. Imam, I. A. Bayero, A. Idris, *Quasi-idempotents in finite semigroup of full order-preserving transformations*, Journal of Semigroup Theory and Applications (2026), article 2, DOI: 10.28919/jsta/9723. Full text: https://www.scik.org/index.php/jsta/article/download/9723/4466
