# Exact generic degree and two-pole structure for sparse rank-two Hankel projections

## Finding

For every integer \(n\ge5\), let \(H_{2,n}\subset\mathbb A^n_{\mathbb C}\) denote the variety of sequences \((a_0,\ldots,a_{n-1})\) whose \(3\times(n-2)\) Hankel matrix has rank at most two. The coordinate projection retaining indices \(\{0,1,3,n-1\}\), equivalently one-based indices \(\{1,2,4,n\}\), is dominant, generically finite, and has **exact generic degree**
\[
\deg\pi_{\{1,2,4,n\}}=n-4+\left\lfloor\frac{n-1}{2}\right\rfloor=\left\lfloor\frac{3(n-3)}2\right\rfloor.
\]

More precisely, over the rational function field \(K=\mathbb C(A,B,C)\) of \(A=a_0\), \(B=a_1\), \(C=a_3\), the last coordinate is a rational function \(R_{n-1}(S)\) of a recurrence parameter \(S\). The map \(\mathbb P^1_S\to\mathbb P^1_{R_{n-1}}\) has precisely two poles: at \(S=\infty\) of order \(n-4\) and at \(S=-B/A\) of order \(\lfloor(n-1)/2\rfloor\).

## Assumptions and scope

The base field is \(\mathbb C\). Generic means over the field of rational functions in the four retained coordinates, not a statement about every numerical fiber. On the dense rank-two open subset where \(a_0a_2-a_1^2\ne0\), the moments satisfy the recurrence \(a_{j+2}=Sa_{j+1}-Pa_j\) with uniquely determined \(S,P\). The genericity conditions used for the pole calculation are \(A\ne0\), \(B\ne0\), and \(\Delta=A^2C-B^3\ne0\), which hold over \(K\). The rank-at-most-two Hankel ideal is prime and its affine variety has dimension four; see the cited primary source.

## Proof

**1. A rational function-field chart.** A rank-two Hankel matrix with \(a_0a_2-a_1^2\ne0\) has its third row a unique linear combination of its first two rows. It follows that the sequence satisfies a unique order-two recurrence. Conversely, any \((A,B,S,P)\in\mathbb A^4\) produces a recurrence sequence. On the dense open where the initial \(2\times2\) determinant is nonzero, these constructions are mutually rational inverses. Thus \(\mathbb C(H_{2,n})=\mathbb C(A,B,S,P)\).

**2. The fixed three observations.** Put \(C=a_3\). The recurrence gives \(C=BS^2-P(AS+B)\). Hence
\[
P=\frac{BS^2-C}{AS+B},\qquad
 a_2=\frac{B^2S+AC}{AS+B}.
\]
In particular \(A,B,C,S\) are algebraically independent and \(\mathbb C(H_{2,n})=K(S)\) where \(K=\mathbb C(A,B,C)\). Define \(R_j(S)=a_j\in K(S)\) for \(j\ge0\), using the displayed formulas and the recurrence. Consequently
\[
\deg\pi_{\{1,2,4,n\}}=[K(S):K(R_{n-1})]=\deg(R_{n-1}:\mathbb P^1\to\mathbb P^1).
\]
The last equality holds for a nonconstant rational function on a projective line.

**3. Pole at infinity.** As \(S\to\infty\), \(P=(B/A)S+O(1)\) and \(a_2=B^2/A+O(S^{-1})\), while \(a_3=C\). Therefore
\[
a_4=Sa_3-Pa_2=\frac{\Delta}{A^2}S+O(1),\quad\Delta=A^2C-B^3\ne0.
\]
Induction on \(j\ge4\) using \(a_{j+2}=Sa_{j+1}-Pa_j\) gives
\[
a_j=\frac{\Delta}{A^2}S^{j-3}+O(S^{j-4}),\qquad j\ge4.
\]
Indeed, if \(a_j\) has leading order \(j-3\) and \(a_{j+1}\) has leading order \(j-2\), then \(Sa_{j+1}\) has order \(j-1\), strictly exceeding the order \(j-2\) of \(Pa_j\). Thus \(R_t\), for \(t=n-1\ge4\), has a pole of order exactly \(t-3=n-4\) at infinity.

**4. The only finite pole and its order.** All \(a_j\) are polynomials in \(A,B,S,P\) before substitution. The displayed expression for \(P\) shows their only possible finite pole occurs at \(S_0=-B/A\). Since \(BS_0^2-C=-\Delta/A^2\ne0\), \(P\) has a simple pole there. For the leading \(P\)-degree, define \(F_0=0\), \(F_1=1\), \(F_{j+1}=SF_j-PF_{j-1}\). Then \(a_j=BF_j-APF_{j-1}\) for \(j\ge1\), and
\[
F_j=\sum_{h=0}^{\lfloor(j-1)/2\rfloor}(-P)^h\binom{j-1-h}{h}S^{j-1-2h}.
\]
For \(t=2m\ge4\), the coefficient of the top power \(P^m\) in \(a_t\) is \((-1)^mA\), nonzero. For \(t=2m+1\ge5\), it is \((-1)^m(B+mAS)\), which takes the nonzero value \((-1)^m(1-m)B\) at \(S_0\), because \(m\ge2\). Thus no leading-pole cancellation is possible, and the pole order at \(S_0\) is exactly \(m=\lfloor t/2\rfloor\). There are no other finite poles.

**5. Generic degree.** The degree of a nonconstant rational map of projective lines is the sum of its pole orders, so
\[
\deg R_t=(t-3)+\lfloor t/2\rfloor
=n-4+\lfloor(n-1)/2\rfloor
=\lfloor3(n-3)/2\rfloor.
\]
The characteristic-zero map is generically separable; this degree therefore equals the number of geometric points in a generic fiber, counted without multiplicity. This completes the proof.

## Verification

The included standalone exact-arithmetic script `verification/check_degree.py` specializes \((A,B,C)\) to two rational triples satisfying the open conditions. For each \(5\le n\le18\), it constructs the rational recurrence exactly, reduces the numerator and denominator, and verifies the two poles and their orders, as well as the resulting generic degree. This finite computation checks algebraic identities for sample values but does **not** replace the uniform proof above. Execute it with `python verification/check_degree.py` using Python and SymPy; expected output: `VERIFY_OK`.

## Relationship to prior work

Ethan Reed and Manolis C. Tsakiris, *On Hankel Determinantal Matroids* (2026), prove uniformity of the algebraic matroid and bounds for degrees of arbitrary coordinate projections. Their Section 5.2 and Remark 7 report, by Macaulay2, the six finite degrees \(3,4,6,7,9,10\) for \(\{1,2,4,n\}\) at \(n=5,\ldots,10\), and Theorem 5 gives the bound \(2\max\{2,n-4\}\) for this pattern. Their Theorem 6 gives an exact all-\(n\) degree for the **different**, consecutive-index pattern \(\{1,2,3,n\}\). The present formula explains and extends the specific six-entry numerical sequence at every \(n\), and determines the two-pole mechanism underlying it. The previously reported numerical values and the general uniformity/degree-bound results are not claimed as new.

## Limitations

The formula concerns complex rank-at-most-two Hankel varieties and the particular four observations \(\{1,2,4,n\}\). It does not determine higher-rank projection degrees, exceptional or nonreduced fibers, arithmetic in positive characteristic, or degree formulas for arbitrary sparse coordinate sets. The historical originality comparison is based on the inspected motivating primary paper, targeted literature searches, and mathematical-record searches; an equivalent classical Prony-theory presentation not located by those searches remains a possibility. Independent mathematical validation has not been performed.

## References

Reed, E., and Tsakiris, M. C., *On Hankel Determinantal Matroids*, arXiv:2610.27554v1, first public October 20, 2026. https://arxiv.org/html/2610.27554v1 ; see Section 5.2, Remark 7, Theorem 5, and Section 5.3, Theorem 6.
