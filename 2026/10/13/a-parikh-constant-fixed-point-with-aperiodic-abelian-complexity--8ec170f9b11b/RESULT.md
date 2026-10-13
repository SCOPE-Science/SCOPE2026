# A Parikh-constant fixed point with aperiodic abelian complexity
## Finding
Let
\[
\tau(0)=012,\qquad \tau(1)=201,\qquad \tau(2)=120,
\]
and let
\[
\mathbf{x}=\tau^\omega(0).
\]
All three images have Parikh vector
\[
(1,1,1),
\]
so \(\tau\) is Parikh-constant.

The abelian complexity \(\mathsf a_{\mathbf{x}}(n)\) is
\[
\mathsf a_{\mathbf{x}}(n)=
\begin{cases}
7,&3\mid n,\\[2mm]
3,&n=1,\\
3,&n=3^{\,2r+1}+1\text{ for some }r\ge0,\\
3,&n=3^{\,2r+2}-1\text{ for some }r\ge0,\\
6,&\text{otherwise}.
\end{cases}
\]

In particular, \(\mathsf a_{\mathbf{x}}\) is not ultimately periodic. Thus a fixed point of a Parikh-constant morphism need not have ultimately periodic abelian complexity.

## Assumptions and scope
For a finite word \(u\) on \(\{0,1,2\}\), its Parikh vector is
\[
\Psi(u)=(|u|_0,|u|_1,|u|_2).
\]
The abelian complexity \(\mathsf a_{\mathbf{x}}(n)\) is the number of distinct Parikh vectors of length-\(n\) factors of \(\mathbf{x}\).

The morphism is interpreted on the alphabet \(\mathbb Z/3\mathbb Z\). Its \(r\)-th output letter satisfies
\[
\tau(a)[r]\equiv r-a\pmod 3,
\qquad r\in\{0,1,2\}.
\]
Therefore the fixed point obeys the coordinate recurrence
\[
x_{3j+r}\equiv r-x_j\pmod 3.
\]

The claim gives the complete abelian-complexity function for this fixed point. It does not classify all Parikh-constant morphisms.

## Proof
For \(q\ge0\), define the difference set
\[
D_q=\{x_{i+q}-x_i\pmod3:i\ge0\}.
\]
From the coordinate recurrence,
\[
D_{3m}=-D_m,
\]
and, for \(m\ge1\),
\[
D_{3m+1}=(1-D_m)\cup(1-D_{m+1}),
\]
\[
D_{3m+2}=(2-D_m)\cup(2-D_{m+1}).
\]
The initial sets are
\[
D_0=\{0\},\qquad D_1=\{0,1\},\qquad D_2=\{1,2\}.
\]
For \(D_1\), adjacent differences at positions congruent to \(0\) or \(1\) modulo \(3\) equal \(1\), while a difference at position \(3j+2\) equals \(1-(x_{j+1}-x_j)\); induction gives only \(0\) and \(1\), and both occur.

These recurrences give, by induction,
\[
D_{3^k}=
\begin{cases}
\{0,1\},&k\text{ even},\\
\{0,2\},&k\text{ odd},
\end{cases}
\]
\[
D_{2\cdot3^k}=\{1,2\},
\]
and
\[
D_q=\{0,1,2\}
\]
for every other positive \(q\). Indeed, multiplication by \(3\) merely negates the preceding set. For a nonmultiple of \(3\), the two smaller indices \(m,m+1\) cannot both belong to the exceptional family \(\{3^k,2\cdot3^k:k\ge0\}\), except for the initial consecutive pairs \((1,2)\) and \((2,3)\), which are checked directly; hence the relevant union is all of \(\mathbb Z/3\mathbb Z\).

We now count Parikh vectors. Let
\[
U=(1,1,1)
\]
and let \(e_j\) be the unit vector of symbol \(j\), with indices modulo \(3\). Each substitution block has Parikh vector \(U\).

For length \(3q\), a factor beginning at a block boundary has Parikh vector \(qU\). A factor beginning one letter into a block has
\[
qU+e_{-b}-e_{-a},
\]
where \(a=x_i\) and \(b=x_{i+q}\). A factor beginning two letters into a block has
\[
qU+e_{2-a}-e_{2-b}.
\]
For every \(q\ge1\), \(D_q\) contains a nonzero difference. The two non-boundary offsets therefore produce the six nonzero root differences \(e_i-e_j\), while the boundary case gives \(qU\). Hence
\[
\mathsf a_{\mathbf{x}}(3q)=7.
\]

For length \(3q+1\), offsets \(0\) and \(2\) give exactly
\[
qU+e_j,\qquad j\in\mathbb Z/3\mathbb Z.
\]
The remaining offset gives
\[
qU+U-e_{-a}-e_{2-b},
\qquad b=x_{i+q}.
\]
This is one of the preceding three vectors unless
\[
b-a\equiv2\pmod3.
\]
When that difference occurs, it contributes three additional vectors. The language is invariant under cyclic translation of the alphabet: since
\[
\tau(a+c)=\tau(a)-c,
\]
one has
\[
\tau^k(a+c)=\tau^k(a)+(-1)^kc,
\]
and every substituted letter block occurs in the primitive fixed point. Thus one occurrence of a difference yields its full three-vector orbit. Therefore, for \(q\ge1\),
\[
\mathsf a_{\mathbf{x}}(3q+1)=
\begin{cases}
6,&2\in D_q,\\
3,&2\notin D_q.
\end{cases}
\]
By the classification of \(D_q\), the value \(2\) is absent exactly when
\[
q=3^{2r}.
\]
Together with \(\mathsf a_{\mathbf{x}}(1)=3\), this gives the stated \(3q+1\) cases.

For length \(3q+2\), offsets \(0\) and \(1\) give exactly
\[
qU+U-e_j,\qquad j\in\mathbb Z/3\mathbb Z.
\]
The remaining offset gives
\[
qU+e_{2-a}+e_{-b},
\qquad b=x_{i+q+1}.
\]
It contributes three new vectors exactly when
\[
b-a\equiv1\pmod3.
\]
Hence
\[
\mathsf a_{\mathbf{x}}(3q+2)=
\begin{cases}
6,&1\in D_{q+1},\\
3,&1\notin D_{q+1}.
\end{cases}
\]
The value \(1\) is absent from \(D_{q+1}\) exactly when
\[
q+1=3^{2r+1},
\]
which is equivalent to
\[
3q+2=3^{2r+2}-1.
\]

This proves the formula.

Finally, the positions where the complexity equals \(3\) include
\[
1,4,8,28,80,244,728,2188,\ldots
\]
and have unbounded gaps, while occurring infinitely often. In an ultimately periodic sequence, any value that occurs infinitely often in the periodic tail has bounded gaps. Therefore \(\mathsf a_{\mathbf{x}}\) is not ultimately periodic.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier reconstructs the fixed point and checks
\[
x_{3j+r}\equiv r-x_j\pmod3
\]
through a prefix of length \(3^{11}\). It independently evaluates the recursive difference sets \(D_q\) through \(q=20000\) and compares them with the closed classification.

For direct factor checks, it computes sliding Parikh vectors on the same fixed-point prefix for every \(1\le n\le250\) and for selected larger lengths around the sparse exceptional positions. It also checks the language-translation symmetry through eight substitution levels.

These finite tests supplement the symbolic difference-set and factor-boundary proof; no infinite conclusion is inferred from finite enumeration.

## Relationship to prior work
Rigo, Stipulanti, and Whiteland prove that the abelian complexity of every fixed point of a Parikh-collinear morphism is automatic. In their concluding remarks they explicitly ask whether the more restrictive Parikh-constant case might always have ultimately periodic abelian complexity.

The morphism used here is Parikh-constant in the strongest literal sense: every image is a permutation of \(012\). Its fixed point itself was previously recorded as OEIS A287451, but the checked sequence entry gives the morphism and fixed point, not its abelian-complexity formula.

Earlier work of Rigo and Salimov develops binomial complexity for fixed points of Parikh-constant morphisms and gives boundedness results, but it does not imply ultimate periodicity of abelian complexity and does not provide the formula above.

Targeted searches for the exact morphism, its OEIS identifier, Parikh-constant aperiodic abelian complexity, and the explicit exceptional lengths did not locate a published covering statement.

## Limitations
The result is a counterexample and a complete formula for one ternary fixed point. It does not characterize which Parikh-constant morphisms have ultimately periodic abelian complexity.

The proof exploits the special affine rule
\[
\tau(a)[r]\equiv r-a\pmod3,
\]
so no corresponding formula for arbitrary permutation-block substitutions is asserted.

An unindexed note or unpublished computation could contain the same example.

## References
1. M. Rigo, M. Stipulanti, and M. A. Whiteland, “Automatic Abelian Complexities of Parikh-Collinear Fixed Points,” arXiv:2405.18032v1, first public version 2024-05-28; Theory of Computing Systems 68 (2024), 1622–1639, DOI 10.1007/s00224-024-10197-5.
2. M. Rigo and P. Salimov, “Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words,” Theoretical Computer Science 601 (2015), 47–57, DOI 10.1016/j.tcs.2015.07.025.
3. OEIS Foundation Inc., OEIS A287451, fixed point of \(0\mapsto012\), \(1\mapsto201\), \(2\mapsto120\).
