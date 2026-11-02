# Rank-stratified brace and group centralizers in three-block matrix radicals

## Finding

Fix a prime power \(q\) and positive integers \(r,s,t\). Consider the nilpotent associative \(\mathbb F_q\)-algebra \(R_{r,s,t}\) of three-block matrices
\[
A(X,Y,Z)=\begin{pmatrix}0&X&Z\\0&0&Y\\0&0&0\end{pmatrix},
\quad X\in M_{r,s}(\mathbb F_q),\ Y\in M_{s,t}(\mathbb F_q),\ Z\in M_{r,t}(\mathbb F_q).
\]
Its radical-ring brace is \(B=(R,+,\circ)\) with \(A\circ B=A+B+AB\); write \(G=(R,\circ)\). For \(A=A(X,Y,Z)\), let \(a=\operatorname{rank}X\), \(b=\operatorname{rank}Y\). Define the *brace centralizer* by \(\operatorname{Cb}(A)=\{D:AD=DA=0\}\) and the multiplicative centralizer by \(C_G(A)=\{D:A\circ D=D\circ A\}\). The latter equality is equivalent to \(AD=DA\). Then
\[
|\operatorname{Cb}(A)|=q^{rs+st+rt-at-rb},\qquad
|C_G(A)|=q^{rs+st+rt-at-rb+ab},
\]
so the **exact centralizer gap is \(|C_G(A)|/|\operatorname{Cb}(A)|=q^{ab}\)**. The joint rank strata occur with multiplicity \(q^{rt}R_{r,s}(a)R_{s,t}(b)\), where
\[
R_{m,n}(j)={m\brack j}_q\prod_{i=0}^{j-1}(q^n-q^i).
\]

This stratification gives all centralizer-size distributions and two different commuting probabilities. Put \(D=rs+st\), and
\[
P_0=q^{-D}\sum_{a=0}^{\min(r,s)}R_{r,s}(a)q^{st-at}
=q^{-rs}\sum_{a=0}^{\min(r,s)}R_{r,s}(a)q^{-at}.
\]
Then \(P_0\) is the probability that two uniformly independent compatible rectangular matrices have zero product. The two-sided-brace and circle-group commuting probabilities are respectively
\[
\boxed{\operatorname{Pb}(B)=P_0^2},\qquad
\boxed{\operatorname{Pr}(G)=q^{-D}\sum_{a,b}R_{r,s}(a)R_{s,t}(b)q^{-at-rb+ab}}.
\]
All sums over \(a,b\) here run from zero through their corresponding maximal matrix ranks. For every positive \(r,s,t\), \(\operatorname{Pr}(G)>\operatorname{Pb}(B)\).

There is also a *rank-exact commutator fiber law*. For a fixed matrix \(C\in M_{r,t}(\mathbb F_q)\) of rank \(k\), define
\[
F_k(d)=\sum_{j=k}^{\min(r,d)}{r-k\brack j-k}_q
\left(\prod_{i=0}^{j-1}(q^d-q^i)\right)q^{(d-j)t},
\]
with an empty sum interpreted as zero. The number of ordered \((A,B)\in R\times R\) having group commutator \([1+A,1+B]=1+E_C\), where \(E_C=A(0,0,C)\) is the central block matrix, is exactly \(q^{2rt}F_k(2s)\). Here \(1+A\) realizes the circle group in invertible unipotent matrices.

Thus the single-commutator image consists *exactly* of central matrices of rank at most \(2s\). For a central element with block \(C\), the minimum number of group commutators whose product equals it is
\[
\ell_{\mathrm{comm}}(C)=\left\lceil\frac{\operatorname{rank}C}{2s}\right\rceil.
\]
By contrast, the minimum number of ring/brace products \(A*B=AB\) whose **sum** is \(A(0,0,C)\) is
\[
\ell_{\mathrm{prod}}(C)=\left\lceil\frac{\operatorname{rank}C}{s}\right\rceil.
\]
Both lengths are defined to be zero for the zero matrix, and all products/commutators lie in the common central ideal \(R^2\). In particular the group-commutator width of \(G\) is \(\lceil\min(r,t)/(2s)\rceil\), and the additive brace-product width of \(R^2\) is \(\lceil\min(r,t)/s\rceil\).

As \(s\to\infty\) with \(r,t,q\) fixed, the two probabilities converge to \(q^{-2rt}\) and \(q^{-rt}\), respectively. Thus the gap survives middle-block stabilization.

## Assumptions and scope

Every assertion holds over **every finite field** \(\mathbb F_q\), with \(r,s,t\ge1\). Group commutators use \([g,h]=ghg^{-1}h^{-1}\), and the brace centralizer of this two-sided radical-ring brace is defined by the simultaneous annihilation conditions \(AD=DA=0\). Additive commutators vanish because the underlying additive group is abelian. The theorem does not concern arbitrary skew braces, arbitrary parabolic radicals with more than three blocks, or non-field coefficient rings.

The algebra has \(R^3=0\) and \(R^2=\{A(0,0,C):C\in M_{r,t}(\mathbb F_q)\}\). Its circle group is isomorphic to \(1+R\); central elements from \(R^2\) multiply by adding central blocks.

## Proof

**Step 1: multiplication and both centralizers.** Direct block multiplication gives
\[
A(X,Y,Z)A(U,V,W)=A(0,0,XV),
\]
and its reversed product is \(A(0,0,UY)\). The brace centralizer consists exactly of \(XV=0\) and \(UY=0\). For fixed \(X\) of rank \(a\), each of the \(t\) columns of \(V\) lies in the \((s-a)\)-dimensional kernel of \(X\); therefore there are \(q^{(s-a)t}\) choices. For fixed \(Y\) of rank \(b\), each \(U\) must vanish on \(\operatorname{im}Y\), giving \(q^{r(s-b)}\) choices. The unrestricted central block \(W\) contributes \(q^{rt}\). This proves the first centralizer formula.

For circle-group commutation, the linear equation is \(XV-UY=0\). The image of the map \((U,V)\mapsto XV-UY\) is the sum of the space of matrices whose columns lie in \(\operatorname{im}X\) (dimension \(at\)) and the space of matrices whose rows lie in the row space of \(Y\) (dimension \(rb\)). Their intersection is the tensor product of those two subspaces, dimension \(ab\). Hence the linear map has rank \(at+rb-ab\), giving the second formula. The exact quotient of centralizer sizes is \(q^{ab}\). The standard finite-field rank count \(R_{m,n}(j)\) is obtained by choosing a rank-\(j\) image subspace and then a surjective linear map onto it, proving the stratum multiplicity.

**Step 2: the probabilities.** The fraction of compatible pairs \((X,V)\in M_{r,s}\times M_{s,t}\) with \(XV=0\) equals \(P_0\) by conditioning on \(\operatorname{rank}X\). For independent uniformly chosen \((X,Y,Z)\) and \((U,V,W)\), the conditions \(XV=0\) and \(UY=0\) involve disjoint sets of random matrix variables and each has probability \(P_0\); hence \(\operatorname{Pb}(B)=P_0^2\). Averaging the group-centralizer probabilities \(q^{-at-rb+ab}\) over the independent rank distributions of \(X,Y\) gives the displayed formula for \(\operatorname{Pr}(G)\). The inequality is strict because \(q^{ab}>1\) for \(a,b>0\), and the locus of pairs with both ranks positive has positive measure.

**Step 3: all commutator fibers.** Since \(R^3=0\), \([1+A,1+B]=1+AB-BA\). The central block is \(XV-UY\), which factors as
\[
[X\ -U]\begin{bmatrix}V\\Y\end{bmatrix}.
\]
The two factors range **independently over all** \(r\times2s\) and \(2s\times t\) matrices. To count factorizations of a fixed rank-\(k\) matrix \(C\) through a \(d\)-dimensional middle space, condition on the rank \(j\) of the first factor. Its image \(W\) must be a \(j\)-space containing \(\operatorname{im}C\); there are \({r-k\brack j-k}_q\) such subspaces. The number of maps onto \(W\) is \(\prod_{i=0}^{j-1}(q^d-q^i)\). For each such map, the \(t\) columns of the second factor have \(q^{d-j}\) independent choices of preimage each, giving \(q^{(d-j)t}\). Summation gives \(F_k(d)\). The two central input blocks contribute \(q^{2rt}\). This also shows that a single commutator attains exactly those central blocks with rank at most \(2s\).

**Step 4: exact widths.** The rank of a product factoring through an \(s\)-space is at most \(s\), and that of one group commutator is at most \(2s\). Rank subadditivity provides the two lower bounds for sums/products of commutators. Conversely, write a rank-\(k\) matrix as a sum of \(k\) rank-one matrices, partition these into groups of at most \(s\) or \(2s\), and factor each grouped matrix through a space of the required dimension. These are actual brace products or group commutators by the factorization above. Their central blocks add under circle multiplication, proving both exact minima, including zero.

**Step 5: limiting separation.** When \(s\to\infty\) with \(r,t,q\) fixed, random \(X\in M_{r,s}\) has rank \(r\) with probability tending to one; random \(Y\in M_{s,t}\) has rank \(t\) with probability tending to one. On this full-rank event the group and brace centralizer fractions are respectively \(q^{-rt}\) and \(q^{-2rt}\). Both fractions are bounded by one and the complement probability tends to zero, proving the limits.

## Verification

Run the dependency-free prime-field checker with `python3 verify.py`. It constructs the block products directly from entries and exhaustively enumerates all relevant \((X,Y,U,V)\) for the parameter sets \((r,s,t;q)=(1,1,1;2),(1,1,1;3),(1,1,1;5),(2,1,2;2),(2,1,2;3),(1,2,1;2),(2,1,3;2),(3,1,3;2)\). It independently verifies **every** rank-stratum centralizer size, each individual commutator fiber and product fiber, and the two commuting probabilities. For \((3,1,3;2)\), it also enumerates all single products, single commutators and sums of two commutators to verify the sharp width distinction. Successful execution prints `VERIFY_OK`.

For instance, at \((r,s,t;q)=(2,1,2;2)\), the zero-product count among \(16\) compatible pairs is \(7\). The brace-centralizing count among \(256\) quadruples is \(49\), whereas the circle-group commuting count is \(58\). At \((3,1,3;2)\), there are \(50\) distinct one-product central matrices, \(344\) one-commutator central matrices, and all \(512\) central matrices are products of at most two commutators.

The checker uses prime fields only; the symbolic proof establishes every prime-power case. Brute-force checks of bounded configurations do not establish the unrestricted theorem by themselves.

## Relationship to prior work

Mondal and Yadav, *Commuting probability of skew left braces* (first public arXiv posting 2026-03-17), introduce brace commuting probabilities and derive general centralizer bounds and cyclic examples. Mondal, Shumyatsky, Trombetti and Yadav, *Relative commuting probability and BFC-type results for finite skew braces* (first public arXiv posting 2026-09-14), develop their structural significance. The present theorem is an explicit calculation for a natural three-parameter family of two-sided radical-ring braces and distinguishes their brace centralizers from their multiplicative-group centralizers. Neither inspected article states the matrix-rank formulas, the exact multiplicative-to-brace centralizer quotient, or the two sharp widths.

Classical finite-field matrix rank and factorization counting supplies crucial standard ingredients and is **not** claimed to be new. The asserted contribution is the combined centralizer classification, fiber law, and sharp brace-product versus group-commutator width distinction in one infinite family. Ordinary commuting-matrix enumerations (including Fulman--Guralnick) concern different matrix spaces, and the published Kronecker-path-algebra centralizer calculation concerns a different algebra with different fiber behavior; these comparisons alone cannot prove historical uniqueness.

## Limitations

No claim is made that the elementary rank-counting factors are novel, that this class represents all class-two groups or braces, or that every possible earlier equivalent formulation has been excluded. The result does not extend without additional arguments to four-block or longer radicals, to arbitrary finite coefficient rings, or to arbitrary non-two-sided skew braces. Historical-priority risk remains from the literature on generalized Heisenberg groups, algebra groups, and rank-stratified commutator word maps.

## References

1. S. Mondal and M. K. Yadav, *Commuting probability of skew left braces*, arXiv:2603.16771 (first publicly submitted 2026-03-17), https://arxiv.org/abs/2603.16771.
2. S. Mondal, P. Shumyatsky, M. Trombetti, and M. K. Yadav, *Relative commuting probability and BFC-type results for finite skew braces*, arXiv:2609.16269 (first publicly submitted 2026-09-14), https://arxiv.org/abs/2609.16269.
3. J. Fulman and R. Guralnick, *Enumeration of commuting pairs in Lie algebras over finite fields*, arXiv:1611.05499 (2016), https://arxiv.org/abs/1611.05499.
