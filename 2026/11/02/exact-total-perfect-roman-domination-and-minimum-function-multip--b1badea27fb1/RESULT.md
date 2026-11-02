# Exact total perfect Roman domination and minimum-function multiplicities on ladder graphs

## Finding

Let \(L_n=P_2\square P_n\) be the two-row ladder with \(n\ge2\) columns. The total perfect Roman domination number is
\[
\gamma_{tR}^{p}(L_n)=2n-2\left\lfloor\frac n3\right\rfloor.
\]
Write \(M_n\) for the number of distinct minimum-weight total perfect Roman dominating functions, with vertices and the three labels distinguished. Then
\[
M_n=\begin{cases}
1,&n=3q,\\
q+1,&n=3q+1,\\
13+\frac92 q(q+3),&n=3q+2.
\end{cases}
\]
where \(q\ge1\) in the first two lines and \(q\ge0\) in the last line. Thus \(M_2=13\), and every ladder with \(3\mid n\) has exactly one minimum function: the two rows both repeat the pattern \(0,2,0\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The vertices are \((r,j)\) for \(r\in\{1,2\}\), \(1\le j\le n\), with the rung edge joining the two vertices in each column and horizontal edges joining consecutive vertices in each row. A total perfect Roman dominating function \(f:V(L_n)\to\{0,1,2\}\) satisfies two conditions: each vertex labeled \(0\) has **exactly one** neighbor labeled \(2\), and every vertex with a positive label has at least one positively labeled neighbor. Its weight is \(\sum_{v\in V(L_n)} f(v)\). No symmetries are quotiented out in \(M_n\).

## Proof

**1. Exact local equivalence.** Represent column \(j\) by a vector \(b_j=(f(1,j),f(2,j))\in\mathcal A=\{0,1,2\}^2\), and write \(\bot=(0,0)\) for a boundary sentinel (not a graph column). For \(a,b,c\in\mathcal A\), define \(\operatorname{ok}(a,b,c)\) as the conjunction over \(r=1,2\) of
\[
 b_r=0\ \Longrightarrow\
 \mathbf1_{a_r=2}+\mathbf1_{b_{3-r}=2}+\mathbf1_{c_r=2}=1,
\]
and
\[
 b_r>0\ \Longrightarrow\ (a_r>0)\lor(b_{3-r}>0)\lor(c_r>0).
\]
These are exactly the two requirements at the vertices of the middle column. The missing horizontal neighbors at either endpoint contribute neither a defender nor positive support, hence the sentinel is valid. A sequence \((b_1,\ldots,b_n)\) is feasible if and only if \(\operatorname{ok}(\bot,b_1,b_2)\), \(\operatorname{ok}(b_{j-1},b_j,b_{j+1})\) for all \(2\le j<n\), and \(\operatorname{ok}(b_{n-1},b_n,\bot)\).

**2. Exact finite-state recurrence.** There are \(9\) column symbols and \(81\) ordered two-column states \((a,b)\). Let \(d_k(a,b)\) be the minimum weight of a \(k\)-column prefix ending in \((a,b)\) in which all but the last column have already been checked. Let \(c_k(a,b)\) be the number of prefixes attaining that minimum, taking \(d_k=\infty\), \(c_k=0\) for impossible states. At \(k=2\),
\[
(d_2(a,b),c_2(a,b))=\begin{cases} (|a|+|b|,1),&\operatorname{ok}(\bot,a,b),\\(\infty,0),&\text{otherwise},\end{cases}
\]
where \(|a|=a_1+a_2\). For every \(k\ge2\),
\[
 d_{k+1}(b,c)=|c|+\min_{a:\operatorname{ok}(a,b,c)}d_k(a,b),
\]
\[
 c_{k+1}(b,c)=\sum_{\substack{a:\operatorname{ok}(a,b,c)\\d_k(a,b)+|c|=d_{k+1}(b,c)}}c_k(a,b).
\]
Finally, take the smallest finite \(d_n(a,b)\) among states satisfying \(\operatorname{ok}(a,b,\bot)\); sum their corresponding counts to obtain \((\gamma_{tR}^{p}(L_n),M_n)\). Each labeling has a unique column word and a unique path through the recurrence, so no function is omitted or counted twice.

**3. Finite identities establishing infinite behavior.** Two **exact integer identities**, for *all* \(81\) states (including unreachable ones), follow by the displayed recurrence:
\[
 d_{r+3}(s)=d_r(s)+4\qquad(r\in\{3,4,5\}),
\tag{1}
\]
where \(\infty+4=\infty\), and
\[
 \sum_{j=0}^{4}(-1)^{4-j}\binom4j\,c_{r+3j}(s)=0
 \qquad(r\in\{3,4,5\}).
\tag{2}
\]
A complete standalone evaluator of both identities is in `verify.py`. The finite calculation enumerates the declared nine symbols, tests the local conditions explicitly, and evaluates at most seventeen columns; it is not a sample from an infinite parameter range.

The min-plus recurrence is homogeneous under adding a constant to all finite state costs. Applying it to (1) yields \(d_{k+3}(s)=d_k(s)+4\) for every \(k\ge3\), so the admissible minimum-predecessor transitions for counts repeat every three steps. For each starting phase \(r\in\{3,4,5\}\), there is therefore a fixed nonnegative integer matrix \(B_r\) taking the count vector at length \(r+3j\) to the one at \(r+3(j+1)\). Equation (2) states exactly that \((B_r-I)^4c_r=0\). Multiplying by \(B_r^j\) proves that the **fourth finite difference** of every state-count sequence, indexed by \(j\), vanishes forever. Every such sequence is therefore a polynomial of degree at most three in \(j\).

For each phase, the set of terminal states attaining the global minimum is fixed, because the finite costs all shift by four. Hence the minimum value shifts by four per three columns, and the sum of terminal counts is itself a polynomial of degree at most three in the number of three-column increments.

**4. Terminal values and interpolation.** Exact recurrence evaluation gives
\[
(\gamma_{tR}^{p}(L_2),M_2)=(4,13),
\]
\[
\begin{array}{c|rrrr}
n&3&6&9&12\\\hline
\gamma_{tR}^{p}(L_n)&4&8&12&16\\
M_n&1&1&1&1
\end{array}
\]
\[
\begin{array}{c|rrrr}
n&4&7&10&13\\\hline
\gamma_{tR}^{p}(L_n)&6&10&14&18\\
M_n&2&3&4&5
\end{array}
\]
\[
\begin{array}{c|rrrr}
n&5&8&11&14\\\hline
\gamma_{tR}^{p}(L_n)&8&12&16&20\\
M_n&31&58&94&139
\end{array}.
\]
For each phase, four values determine its polynomial of degree at most three uniquely. Interpolation gives the three asserted expressions for \(M_n\); the separate boundary case \(n=2\) agrees with the last expression at \(q=0\). The cost shift and starting values similarly give \(2n-2\lfloor n/3\rfloor\) for all \(n\ge2\).

**5. Witnesses and rigidity.** For \(n=3q\), put both row labels equal to the word \((0,2,0)^q\). For \(n=3q+1\), append a final pair of \(1\)-labels to that word; for \(n=3q+2\), append \(0,2\) to it, including the empty initial word when \(n=2\). Every zero is adjacent to exactly one \(2\), and all positive vertices receive support from their rung partner. These functions have the stated weights. In the divisible-by-three case the polynomial count equals one, so its displayed witness is necessarily the unique minimum function.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. It checks all \(81\) states in (1), all \(81\) state counts in (2), and four terminal values for each phase, then checks direct graph-level all-label enumerations for lengths \(2\) through \(6\), separately from the state recurrence. It also verifies explicit witnesses for lengths \(2\) through \(100\). The intended successful output begins with `VERIFY_OK`.

This is a finite exact certificate for the inductive identities, not a claim that testing finitely many graph sizes alone proves the infinite theorem. The induction and polynomial argument above are essential.

## Relationship to prior work

Almulhim introduced and studied total perfect Roman domination, including the exact-one-defender and positive-support conditions, general bounds, hardness, and a tree equality class (2023). The full accessible paper does not present the ladder formula or minimum-function enumeration here. Almulhim, Akwu, and AlSubaiei (2022) studied the **different** perfect Roman parameter on grid products with both path dimensions exceeding five and obtained an upper bound; that bound neither applies directly to the two-row family nor imposes positive support or counts minima. A 2024 paper on perfect Roman and perfect Italian domination of Cartesian products addresses distinct variants and describes complexity and upper bounds in its publicly accessible abstract. The present contribution is an exact minimum and **all** minimum-labeling multiplicities for a natural two-row Cartesian family.

## Limitations

No claim is made about nonminimum-function counts, ladder cycles, wider grids, or uniqueness of publication priority beyond the sources checked. The 2024 related article was assessed from its publicly accessible abstract, not its complete body. Independent mathematical review has not been performed. All stated infinite equalities depend on the correctness of the explicit finite-state definition, the exact finite identities, and the displayed algebraic induction.

## References

1. A. Almulhim, *Total Perfect Roman Domination*, Symmetry **15** (2023), 1676, published 31 August 2023. DOI: 10.3390/sym15091676. Full-text PDF: https://pdfs.semanticscholar.org/df1f/c7e883486c82017aff34cacb2c5955260645.pdf.
2. A. Almulhim, A. D. Akwu, and B. AlSubaiei, *The Perfect Roman Domination Number of the Cartesian Product of Some Graphs*, Journal of Mathematics (2022), article 1957027. DOI: 10.1155/2022/1957027.
3. A. Almulhim, *Perfect Roman and Perfect Italian Domination of Cartesian Product Graphs*, Scientific Journal of King Faisal University, Basic and Applied Sciences **25** (2024), 63–68. DOI: 10.37575/b/sci/240037. Abstract inspected.
