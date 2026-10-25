# Exact finite-field idempotent census of complete-graph evolution algebras

## Finding

Let \(E_n(\mathbb F_q)\) be the evolution algebra of the loopless complete graph, with \(n\ge3\) and its unnormalised adjacency structure matrix. Let \(N_{n,q}\) be the number of solutions of \(x^2=x\), including \(0\). Write \(p=\operatorname{char}\mathbb F_q\), and let \(\chi_q:\mathbb F_q\to\{-1,0,1\}\) be the quadratic character when \(p\) is odd, extended by \(\chi_q(0)=0\).

**Theorem (complete idempotent census).** For every \(n\ge3\) and prime power \(q\),

1. If \(p\) is odd and \(p\nmid n-1\), then
   \[
   N_{n,q}=2+\frac12\sum_{r=1}^{n-1}\binom nr
   \left(1+\chi_q\bigl(1-4r(n-r)\bigr)-\mathbf1_{p\mid n+1}\right).
   \]
2. If \(p\) is odd and \(p\mid n-1\), then
   \[
   N_{n,q}=1+\frac12\sum_{\substack{1\le r<n\\2r\not\equiv1\pmod p}}\binom nr.
   \]
3. If \(q=2^m\), then
   \[
   N_{n,q}=\begin{cases}
   2^n,&n\text{ even and }m\text{ even},\\
   2^{n-1},&\text{otherwise}.
   \end{cases}
   \]

The proof below also classifies every idempotent vector: it has at most two coordinate values; its labelled support and one quadratic (or linear) equation determine it. This includes singular adjacency matrices, namely the case \(p\mid n-1\), rather than relying on perfection.

## Assumptions and scope

For each \(n\ge3\), fix the natural basis \(e_1,\dots,e_n\) of \(E_n\) by
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=\sum_{j\ne i}e_j.
\]
This is the **unweighted, unnormalised** graph-evolution algebra of the complete *loopless* graph \(K_n\); it is not the randomly normalised graph algebra. Integers inside the finite field are reduced modulo \(p\). An idempotent is an algebra element \(x\) satisfying \(x^2=x\), not an 'idempotent evolution algebra' in the alternative terminology for a perfect algebra. The count is of elements, not algebra-isomorphism classes. The structure matrix is \(J-I\), invertible precisely when \(p\nmid n-1\).

## Proof

**Step 1: the two-coordinate-value reduction.** Let \(x=\sum_i x_i e_i\), and set \(S=\sum_j x_j^2\). Coordinatewise, \(x^2=x\) is equivalent to
\[
 x_i=S-x_i^2\quad(1\le i\le n),\qquad\text{equivalently } x_i^2+x_i=S.
\]
Consequently every coordinate is a root of the same monic polynomial \(T^2+T-S\), so there are at most two distinct values. Two possible values, denoted \(a\) and \(b\), must satisfy \(a+b=-1\), hence \(b=-1-a\). If \(I\subset\{1,\dots,n\}\) is the set of coordinates taking value \(a\), with \(|I|=r\), substitution into the common-square condition yields
\[
 (n-1)a^2+\bigl(2(n-r)-1\bigr)a+(n-r)=0.\tag{1}
\]
Conversely, for every \(I\) of size \(1\le r<n\), every solution \(a\) of (1) gives an idempotent by assigning \(a\) on \(I\) and \(-1-a\) off \(I\). If the values differ, each vector occurs in exactly two such descriptions, after complementing \(I\) and swapping \(a,b\). This is exhaustive by the degree-two argument.

**Step 2: constant vectors.** A constant vector \(x=c\sum_i e_i\) is idempotent if and only if \(c=(n-1)c^2\). There are two constant solutions, \(c=0\) and \(c=(n-1)^{-1}\), when \(p\nmid n-1\); if \(p\mid n-1\), only \(c=0\) remains. When \(p\) is odd, the two roots coincide at \(a=b=-1/2\) precisely when (1) has that root, and direct substitution gives \((n+1)/4=0\). Thus this single coincident root occurs for every proper \(I\) if and only if \(p\mid n+1\). It is the already-counted constant vector \((-1/2)\sum_i e_i\). In characteristic two, the two values \(a\) and \(1+a\) are always distinct.

**Step 3: odd characteristic, nonsingular adjacency.** Suppose \(p\) odd and \(p\nmid n-1\). The discriminant of (1) is exactly
\[
 \bigl(2(n-r)-1\bigr)^2-4(n-1)(n-r)=1-4r(n-r)=:\Delta_r.
\]
The number of solutions of (1) over \(\mathbb F_q\) is \(1+\chi_q(\Delta_r)\). If \(p\mid n+1\), exactly one solution in each such list is the already-counted coincident constant root; remove it. Summing over the \(\binom nr\) subsets, halving for complementary descriptions, and adding the two constants gives formula (1) of the theorem. The subtraction is per subset and is necessary: without it the constant root would be counted repeatedly.

**Step 4: odd characteristic, singular adjacency.** Suppose \(p\mid n-1\). Then (1) reduces in \(\mathbb F_q\) to
\[
 (1-2r)a+(1-r)=0.
\]
If \(2r\equiv1\pmod p\), its constant term is \(1/2\ne0\), so there are no solutions. Otherwise there is exactly one solution. Also \(p\nmid n+1\) because \(p\) is odd, so no two coordinate values coincide. The sum over proper subsets, halved, together with the unique zero constant, is formula (2) of the theorem. Complementation proves the displayed half-integer expression is an integer.

**Step 5: characteristic two.** Write \(q=2^m\). Equation (1) now reads
\[
 (n-1)a^2+a+(n-r)=0
\]
with integer coefficients reduced modulo two. If \(n\) is odd this is linear and has exactly one root for each proper subset \(I\), while the sole constant idempotent is zero. Thus \(N_{n,q}=1+(2^n-2)/2=2^{n-1}\). If \(n\) is even, constants are zero and the all-ones vector. For even \(r\), (1) is \(a^2+a=0\), with the two roots \(0,1\). For odd \(r\), it is \(a^2+a=1\). The latter equation has two solutions over \(\mathbb F_{2^m}\) exactly when the absolute trace of \(1\) is zero, i.e. when \(m\) is even, and none when \(m\) is odd. For even \(n\), each of the even-cardinality and odd-cardinality subsets has total cardinality \(2^{n-1}\). Excluding the empty and full even subsets, adding the two constant vectors, and dividing the two-valued descriptions by two gives \(2^{n-1}\) for odd \(m\) and \(2^n\) for even \(m\).

All cases are exhaustive and all counts include zero. \(\square\)

## Verification

The standalone program `verify.py` builds the finite fields of orders \(2,3,4,5,7,8,9\) from explicit irreducible polynomials and enumerates every coordinate vector for eighteen dimension/field pairs, rather than reusing the quadratic-support proof for its reference counts. It compares those counts with each applicable closed formula and returns `VERIFY_OK cases= 18`. For example, in characteristic two and dimension four, the counts are \(8,16,8\) over field orders \(2,4,8\), respectively; over fields of orders \(3,9\) the three-dimensional counts are \(2,8\), respectively. These finite checks support the derivation but are not substituted for the general proof.

To reproduce: run `python3 verify.py` with Python 3 standard library; no network or external package is required.

## Relationship to prior work

The graph-evolution construction is classical; Cadavid, Rodiño Montoya and Rodríguez study graph and random-walk evolution algebras (arXiv:1710.10516). Kaygorodov, Martín González and Viruel's survey (arXiv:2610.22248v1, first public 15 October 2026) gives the general idempotent equations, a \(2^n\) scheme-length bound for perfect evolution algebras (Theorem 17), and an exact **average** of one nonzero idempotent for uniform invertible structure matrices (Remark 23). Those results do not determine rational-point counts for the one fixed, highly symmetric adjacency matrix \(J-I\), nor the exceptional singular case. The same survey poses questions on idempotents over arbitrary fields, motivating explicit finite-field examples; the result here is not presented as a solution to its universal question. García-Martínez and Pérez-Rodríguez (arXiv:2512.12418v1, 2025) prove existence statements for complex regular evolution algebras and study an unrelated *subalgebra-completeness* property, not the present finite-field point distribution. The phrase 'idempotent evolution algebra' in Wei and Zou's 2023 classification concerns **perfect** algebras and is not an element-level census.

## Limitations

The theorem counts elements only for the **unnormalised loopless complete-graph** family, not arbitrary graphs, weighted adjacencies, random-walk normalisations, or algebra isomorphism classes. The claims of originality are limited by possible unindexed equivalent enumerations and undiscovered representations of the common-root equation. The finite experiments cover only the fields and dimensions named above; they provide no infinite verification. There has been no independent audit.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026), Sections 1.1, 2.1.4, 2.1.5 and Remark 23. https://arxiv.org/html/2610.22248v1
2. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, arXiv:2512.12418v1 (2025), especially Sections 2, 3.3. https://arxiv.org/pdf/2512.12418
3. P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516 (2017). https://arxiv.org/abs/1710.10516
4. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023). https://arxiv.org/abs/2310.12368
