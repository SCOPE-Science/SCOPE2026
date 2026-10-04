# Fixed-parity second differences strictly refine Goda's twisted-Alexander asymptotic
## Finding
Fix one parity of the higher-dimensional twisted Alexander sequence in Aso's normalization. Put
\[
a_n=\log|A_{K,n}(1)|
\]
and
\[
q_n=\frac{\pi}{2}\left(a_{n-2}+a_{n+2}-2a_n\right).
\]
If \(q_n\to L\) along that parity, then
\[
\frac{a_n}{n^2}\longrightarrow\frac{L}{4\pi}.
\]
Thus the real-part assertion of Aso's Conjecture 1 implies Goda's asymptotic volume formula with the correct normalization and without an auxiliary growth hypothesis.

The implication is strict as asymptotic sequence information: quadratic growth of \(a_n\) alone does not force convergence of the fixed-parity second differences.

## Assumptions and scope
Aso defines normalized values \(A_{K,n}(1)\) separately in even and odd dimensions and conjectures, for each fixed parity, convergence of
\[
\frac{\pi}{2}\log\left(
\frac{A_{K,n-2}(1)A_{K,n+2}(1)}{A_{K,n}(1)^2}
\right)
\]
to the complex volume modulo \(i\pi^2\mathbb Z\). Taking real parts removes the logarithm-branch ambiguity and gives the real second-difference quantity \(q_n\).

The converse counterexample below is an abstract positive sequence; it is not asserted to arise from a knot.

## Proof
Write the chosen parity as \(n=\varepsilon+2k\) and put \(b_k=a_{\varepsilon+2k}\). Then
\[
b_{k+1}-2b_k+b_{k-1}
=
\frac{2}{\pi}q_{\varepsilon+2k}.
\]
Twice summing this recurrence gives, for every \(k\ge2\),
\[
b_k=b_0+k(b_1-b_0)
+
\frac{2}{\pi}
\sum_{j=1}^{k-1}(k-j)q_{\varepsilon+2j}.
\]

Suppose \(q_{\varepsilon+2j}\to L\). Write \(q_{\varepsilon+2j}=L+e_j\), with \(e_j\to0\). The constant part is
\[
\frac{2L}{\pi}\sum_{j=1}^{k-1}(k-j)
=
\frac{L}{\pi}k(k-1).
\]
For every \(\delta>0\), all sufficiently late \(e_j\) have absolute value below \(\delta\). Their weighted sum is therefore \(O(\delta k^2)\), while the finitely many early terms contribute only \(O(k)\). Hence the total error is \(o(k^2)\), and
\[
b_k=\frac{L}{\pi}k^2+o(k^2).
\]
Since \((\varepsilon+2k)^2=4k^2+O(k)\),
\[
\frac{a_{\varepsilon+2k}}{(\varepsilon+2k)^2}
\longrightarrow
\frac{L}{4\pi}.
\]

For strictness, fix any real \(L\) and define
\[
b_k=\frac{L}{\pi}k^2+(-1)^k k^{3/2},
\qquad
A_{\varepsilon+2k}=\exp(b_k).
\]
Then \(b_k/(\varepsilon+2k)^2\to L/(4\pi)\), but the second difference of the oscillatory term has magnitude asymptotic to \(4k^{3/2}\). Therefore the corresponding \(q_n\) is unbounded and cannot converge.

## Verification
Aso's full current preprint was checked directly. It declares primary MSC \(57K14\), recalls Goda's parity-separated limit
\[
\frac{\log|A_{K,n}(1)|}{n^2}
\longrightarrow
\frac{\operatorname{Vol}(K)}{4\pi},
\]
and states Conjecture 1 using the fixed-parity second difference.

The bundled regression script checks the Green identity on a quadratic sequence and the finite-tail growth of the oscillatory counterexample. It prints:

`VERIFY_OK green_identity_N=160 constant_second_difference=7.25 converse_tail_max=12471.433240`

The finite regression is not used as an infinite proof.

## Relationship to prior work
Aso motivates the second-difference expression by formally inserting the stronger ansatz
\[
A_{K,n}(1)\sim
\exp\left(\frac{n^2}{4\pi}\mathcal V(K)\right)
\]
and then proposes Conjecture 1 from numerical experiments. The preprint recalls Goda's earlier theorem for absolute values but does not state or prove that real-part second-difference convergence alone forces Goda's limit.

The exact Green identity supplies that implication without the formal exponential ansatz and identifies the boundary in the reverse direction: a quadratic-growth limit alone does not control local second differences.

Targeted published-finding corpus and literature searches for an implication, converse, or equivalence between these two fixed-parity asymptotics did not locate an equivalent statement.

## Limitations
The converse counterexample is sequence-theoretic. It shows that Goda's asymptotic theorem alone cannot logically yield Aso's real-part conjecture, but it does not construct a hyperbolic knot whose twisted Alexander sequence has the displayed oscillation.

The result concerns only the real part and does not settle the Chern--Simons phase in Aso's full complex-volume conjecture.

## References
1. A. Aso, *Asymptotic behavior of twisted Alexander invariants for hyperbolic knots with at most six crossings*, arXiv:2609.29124v1, first posted 2026-09-24.
2. H. Goda, *Twisted Alexander invariants and hyperbolic volume*, arXiv:1604.07490v1; Proceedings of the Japan Academy, Series A 93 (2017), 61--66, DOI `10.3792/pjaa.93.61`.
