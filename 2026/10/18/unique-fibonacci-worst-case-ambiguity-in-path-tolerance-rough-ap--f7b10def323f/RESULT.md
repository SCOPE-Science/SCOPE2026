# Unique Fibonacci worst-case ambiguity in path-tolerance rough approximations

## Finding

For each integer \(n\ge 2\), let \(R\) be the reflexive symmetric path tolerance on \([n]\), given by \(iRj\) if and only if \(|i-j|\le 1\). For each \(X\subseteq[n]\), let
\[
 L_R(X)=\{i:R(i)\subseteq X\},\qquad U_R(X)=\{i:R(i)\cap X\ne\varnothing\}.
\]
The approximation map \(\rho_n(X)=(L_R(X),U_R(X))\) loses information: different subsets may yield the same pair. For every possible approximation pair \(Q\), write \(\mu_n(Q)=|\rho_n^{-1}(Q)|\). With Fibonacci numbers \(F_1=F_2=1\), the following exact extremum holds:
\[
 \boxed{\max_Q\mu_n(Q)=2F_{n-1}.}
\]
Moreover the **unique** maximizing pair is \(Q=(\varnothing,[n])\), the completely uncertain rough set. For every individual rough pair, its multiplicity admits the four-state transfer formula stated below; this computes a fiber in time linear in \(n\).

Encode a rough pair by a ternary output word \(y_1\cdots y_n\) with \(y_i=0\) when \(i\notin U_R(X)\), \(y_i=1\) when \(i\in L_R(X)\), and \(y_i=*\) otherwise. Define the state ordering \((00,01,10,11)\), row vectors
\[
 e_0=(1,0,0,0),\quad e_1=(0,0,0,1),\quad e_*=(0,1,1,0),
\]
column vectors \(f_a=e_a^{\mathsf T}\), and transition matrices
\[
 M_0=\begin{pmatrix}1&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},\quad
 M_1=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&1\end{pmatrix},
\]
\[
 M_*=\begin{pmatrix}0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0\end{pmatrix}.
\]
For every \(n\ge2\) and \(y\in\{0,1,*\}^n\), the **exact** number of subsets producing the output \(y\) is
\[
 \boxed{\mu_n(y)=e_{y_1}M_{y_2}\cdots M_{y_{n-1}}f_{y_n}.}
\]
The product is empty when \(n=2\); unattainable outputs give zero. No quotient by path reversal or complementation is taken.

## Assumptions and scope

All vertices, subsets, and approximation pairs are labeled. \(R\) is the **same** reflexive symmetric relation used for both lower and upper approximation, not a graph-orbit equivalence or a mixed equivalence/tolerance approximation. The maximum ranges over distinct output pairs, while the multiplicity counts labeled input subsets. The result applies to every path length \(n\ge2\), including endpoints with two-point neighborhoods.

## Proof

**Transfer identity.** Encode a subset by bits \(x_1,\ldots,x_n\), where \(x_i=1\) if and only if \(i\in X\). The output at an endpoint is \(0\) for a binary pair \(00\), \(1\) for \(11\), and \(*\) for \(01\) or \(10\). At an interior vertex it is \(0\) for the triple \(000\), \(1\) for \(111\), and \(*\) for the other six triples. After reading output \(y_1\), the row vector \(e_{y_1}\) counts possible first two bits. On processing interior position \(i\), a state \((x_{i-1},x_i)\) extends to \((x_i,x_{i+1})\) precisely when the three-bit window gives symbol \(y_i\). These transitions are exactly the three matrices displayed above. Applying the last endpoint condition \(f_{y_n}\) proves the formula, including the empty-matrix-product case \(n=2\).

**Uniform upper bound and rigidity.** For \(k\ge1\), put
\[
 s_k=(F_k,F_{k+1},F_{k+1},F_k).
\]
After processing the first interior position \(2\), the state vector is componentwise at most \(s_1=(1,1,1,1)\), with equality if and only if \(y_1=y_2=*\). Indeed, with a prescribed last two-bit state \((x_2,x_3)\), the first endpoint output \(y_1\) fixes \(x_1\) uniquely, if possible. Directly \(e_*M_*=s_1\); any other choice of the first two output symbols has a strict coordinate deficit.

The recurrence \(F_{k+2}=F_{k+1}+F_k\) gives \(s_kM_*=s_{k+1}\). Since the matrices have nonnegative entries, \(v\le s_k\) implies \(vM_a\le s_{k+1}\) for every symbol \(a\). More precisely, if \(a=0\) or \(1\), the two mixed-state output coordinates vanish, whereas those of \(s_{k+1}\) are positive. If \(a=*\) and \(v\ne s_k\), the **sum** of the two mixed-state output coordinates satisfies
\[
 (vM_*)_{01}+(vM_*)_{10}=v_{00}+v_{01}+v_{10}+v_{11}
 < 2F_k+2F_{k+1}=2F_{k+2}.
\]
Thus a deficit in any processed output prefix forces a strict deficit in the final mixed-state sum. After all interior positions, the state vector is bounded by \(s_{n-2}\). When \(y_n=*\), its total accepted weight is at most \(2F_{n-1}\), with equality only if all output symbols are stars. When \(y_n=0\) or \(1\), the corresponding accepted coordinate is at most \(F_{n-2}<2F_{n-1}\). This completes the uniqueness argument for \(n\ge3\). For \(n=2\), the four binary inputs give outputs \(00,**,**,11\), so the unique largest fiber is likewise the all-star output, of size \(2=2F_1\).

**Attainment and an independent count.** A binary input produces the all-star word precisely when its first two bits differ, its last two bits differ, and it has no constant triple at an interior position. Equivalently, every maximal constant run has size \(1\) or \(2\), and the first and last runs have size \(1\). There are two choices of first bit. Removing the first and last singleton runs leaves a composition of \(n-2\) into parts \(1\) and \(2\); the number is \(F_{n-1}\). Therefore \(\mu_n(*\cdots*)=2F_{n-1}\), achieving the uniform bound. In particular the largest fiber grows as \(\Theta(\varphi^n)\), where \(\varphi=(1+\sqrt5)/2\).

## Verification

The self-contained standard-library program `verify.py` exhaustively constructs all \(2^n\) labeled input subsets for each \(2\le n\le14\). It computes the lower and upper approximations directly, groups identical rough outputs, checks the transfer product for every attained output, and confirms the unique maximum \(2F_{n-1}\). Its final line is:

`VERIFY_OK original_subsets 32764 individual_fibers 12309 transition_counts=PASS unique_extremum=PASS`

These finite tests are not used as a proof for arbitrary \(n\); the preceding transfer and comparison argument establishes all quantifiers.

## Relationship to prior work

Järvinen and Radeleczki [1] developed the general rough-set approximation and order framework for tolerances and treated the five-vertex path tolerance as a nonlattice example. Their lattice phenomena are background, not novelty claims here. Järvinen, Kovács, and Radeleczki [2] studied mixed equivalence/tolerance approximations \((X_E,X^T)\), a different two-operator setting. The already known count of *distinct* rough pairs for the path is also different from the **largest multiplicity** of one pair and is not claimed as a new result. This theorem concerns the full fiber-size transfer and the uniquely maximizing rough pair. A mathematically analogous Fibonacci fiber result exists for a different binary transverse-read channel [3]; its odd-length read map and resulting \(F_{m+3}\) extremum do not provide a stated implication for the path-tolerance approximation map, but equivalence through an unstated encoding remains a priority risk.

## Limitations

The theorem is restricted to reflexive closed-neighborhood tolerances of **paths**, with two-valued underlying membership. It does not classify automorphisms or lattice operations, and it does not determine the second-largest fiber. No independent external audit or exhaustive publication-priority certification has been performed. The transverse-read-channel analogy warrants expert follow-up before asserting priority.

## References

[1] J. Järvinen and S. Radeleczki, *Rough sets determined by tolerances*, arXiv:1303.6332 (first public 2013-03-25); International Journal of Approximate Reasoning 55 (2014), 1419–1438.

[2] J. Järvinen, L. Kovács, and S. Radeleczki, *Defining rough sets using tolerances compatible with an equivalence*, arXiv:1811.09609 (first public 2018-11-21); Information Sciences 496 (2019), 264–283.

[3] Published mathematical research record, *Fibonacci worst-case ambiguity of the binary (3,2) transverse-read channel*, record `2026/10/4/SCOPE-fibonacci-worst-case-ambiguity-of-the-binary-3-2-transverse-read--d72c6473df5e` (2026); different observation map and parameters, cited as a conceptual comparison only.
