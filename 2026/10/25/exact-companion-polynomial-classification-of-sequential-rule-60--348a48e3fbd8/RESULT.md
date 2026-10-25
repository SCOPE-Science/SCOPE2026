# Exact companion-polynomial classification of sequential Rule-60 dynamics on rings

## Finding
For every integer \(n\ge3\) and every permutation \(\pi\) of the sites \(\mathbb Z/n\mathbb Z\), consider one *sweep* of the binary local rule
\[
(U_i x)_i=x_i+x_{i-1}\pmod2,\qquad (U_i x)_j=x_j\quad(j\ne i),
\]
applying each \(U_i\) once, in order \(\pi\). Write \(F_\pi\) for the resulting linear map. Let \(p_\pi(i)\) denote the position of site \(i\) in the update order, and define
\[
a(\pi)=\#\{i\in\mathbb Z/n\mathbb Z:p_\pi(i-1)<p_\pi(i)\}.
\]
Then \(1\le a(\pi)\le n-1\), and the following complete classification holds.

**Companion classification.** Over \(\mathbb F_2\), both the characteristic and minimal polynomials of \(F_\pi\) equal
\[
Q_{n,a}(t)=(t+1)^n+t^a,\qquad a=a(\pi).
\]
Moreover, \(F_\pi\) is similar over \(\mathbb F_2\) to the companion matrix of \(Q_{n,a}\). Exactly \(n-1\) linear similarity classes arise as \(\pi\) varies: every value \(a\in\{1,\ldots,n-1\}\) occurs, and distinct values give different characteristic polynomials.

**Exact orbit census.** The map is bijective, so every state is periodic. For each positive integer \(m\), its number of points of period dividing \(m\) is
\[
P_{n,a}(m)=\#\operatorname{Fix}(F_\pi^m)
=2^{\deg\gcd\bigl(Q_{n,a}(t),t^m+1\bigr)}.
\]
The number of primitive cycles of length exactly \(m\) is
\[
C_{n,a}(m)=\frac1m\sum_{d\mid m}\mu(m/d)
2^{\deg\gcd\bigl(Q_{n,a}(t),t^d+1\bigr)},
\]
where \(\mu\) is the classical Möbius function. The global permutation order is equivalently the least positive \(m\) for which \(Q_{n,a}(t)\) divides \(t^m+1\). In every schedule, the all-zero state is the unique fixed point.

For example, on a six-site ring, distinct update orders realize global permutation orders \(14\), \(15\), and \(21\). This is not a claim that the \(n-1\) linear similarity classes always have different *unlabelled orbit structures*: distinct characteristic polynomials can induce equal cycle counts.

## Assumptions and scope
Sites are labelled cyclically, indices are reduced modulo \(n\), addition takes place in \(\mathbb F_2\), and one iteration means a complete permutation sweep (not one site update). The theorem treats every permutation order, every \(n\ge3\), and every integer \(m\ge1\), without restrictions on polynomial squarefreeness. Conjugacy means invertible **linear** change of coordinates over \(\mathbb F_2\); equality of cycle counts is a weaker equivalence.

## Proof
**1. An implicit linear system for one sweep.** Set \(\epsilon_i=1\) if site \(i-1\) is updated before site \(i\), and \(\epsilon_i=0\) otherwise. For an input \(x\) and output \(y=F_\pi x\), the predecessor used when site \(i\) is updated equals \(y_{i-1}\) when \(\epsilon_i=1\) and equals \(x_{i-1}\) when \(\epsilon_i=0\). Thus
\[
y_i+\epsilon_i y_{i-1}=x_i+(1-\epsilon_i)x_{i-1}
\quad\text{in }\mathbb F_2.
\]
Define \(H=I+\sum_{\epsilon_i=1}E_{i,i-1}\) and \(J=I+\sum_{\epsilon_i=0}E_{i,i-1}\), where \(E_{ij}\) is a matrix unit. Then \(Hy=Jx\). In update-order coordinates, every off-diagonal nonzero of \(H\) points to a previously updated site, so \(H\) is unit triangular and \(\det H=1\). Consequently \(F_\pi=H^{-1}J\).

**2. Characteristic determinant.** For an indeterminate \(t\),
\[
\det(tI-F_\pi)=\det(tH+J).
\]
The matrix \(tH+J\) has diagonal \(t+1\), and its only off-diagonal entries lie on the directed predecessor cycle: the entry in row \(i\), column \(i-1\) is \(t^{\epsilon_i}\). For \(n\ge3\), a nonzero term in its permutation-determinant expansion must select either all diagonal entries or all predecessor-cycle entries: selecting a predecessor entry at any row forces that choice around the entire ring. In characteristic two their contributions add, yielding
\[
\det(tI-F_\pi)=(t+1)^n+t^{\sum_i\epsilon_i}=Q_{n,a}(t).
\]
A strict total order around a circle cannot make all cyclic predecessor comparisons true or all false, so \(1\le a\le n-1\).

**3. Cyclicity, including repeated polynomial factors.** Let \(R=\mathbb F_2[t]\), let \(B(t)=tH+J\), and consider the \(R\)-module
\[
M=\operatorname{coker}(B(t)^\mathsf T).
\]
Because \(B(t)^\mathsf T=(tI-F_\pi)^\mathsf T H^\mathsf T\), and \(H^\mathsf T\) is invertible over \(R\), this is the standard \(R\)-module \(\mathbb F_2^n\) with \(t\) acting by \(F_\pi^\mathsf T\). The adjugate identity gives \(Q_{n,a}(t)M=0\). Since \(Q_{n,a}(0)=Q_{n,a}(1)=1\), both \(t\) and \(t+1\) are units on \(M\) (Bézout's identity). If \(e_i\) denote the canonical module generators, the row relations of \(B\) are
\[
(t+1)e_i+t^{\epsilon_i}e_{i-1}=0.
\]
Thus \(e_i=t^{\epsilon_i}(t+1)^{-1}e_{i-1}\) in \(M\). Starting from \(e_0\) and proceeding through \(e_1,\ldots,e_{n-1}\), all generators lie in \(Re_0\). Therefore \(M\) is cyclic. A cyclic \(n\)-dimensional \(R\)-module has the form \(R/(D)\) for a monic polynomial \(D\) of degree \(n\); its characteristic polynomial is \(D\). Step 2 gives \(D=Q_{n,a}\). Transposition preserves minimal and characteristic polynomials, hence \(F_\pi\) itself has this companion form. No assumption about simple eigenvalues was made.

**4. Exact periods.** Since \(Q_{n,a}(0)=1\), \(F_\pi\) is invertible and all \(2^n\) configurations lie on cycles. On the cyclic module \(R/(Q_{n,a})\), the dimension of the kernel of multiplication by \(t^m+1\) equals \(\deg\gcd(Q_{n,a},t^m+1)\). Indeed, dividing both polynomials by their gcd reduces the kernel condition to divisibility by the complementary factor of \(Q_{n,a}\). Taking powers of two gives the fixed-point formula. Möbius inversion on divisors of \(m\) counts points of least period \(m\); dividing by \(m\) counts cycles. The map is the identity after \(m\) sweeps exactly when its minimal polynomial divides \(t^m+1\). For \(m=1\), \(Q_{n,a}(1)=1\), so the kernel of \(F_\pi-I\) has dimension zero and the sole fixed state is zero.

**5. Exactly \(n-1\) linear types.** Choose any \(a\) cyclic predecessor edges to satisfy the earlier-than orientation, leaving the other \(n-a\) in the opposite direction. Because both orientations occur, the resulting oriented cycle has no directed circuit; a topological ordering of its vertices realizes exactly that pattern of precedence comparisons. Thus every \(a\in\{1,\ldots,n-1\}\) occurs. For different values, the polynomials \((t+1)^n+t^a\) are different. Conversely, all schedules with a given \(a\) have the same companion form and are therefore linearly similar.

## Verification
The accompanying `verify.py` uses integer bit arithmetic and a separate polynomial-determinant dynamic program over \(\mathbb F_2[t]\). It exhausts all permutation orders for ring sizes \(3\) through \(7\), checks reproducibly chosen additional permutations for sizes \(8\) and \(9\), independently tests fixed-point formulas by binary matrix ranks at ten return times, and tests cyclic vectors and primitive orbit censuses. It reports `VERIFY_OK characteristic_polynomials 6390 fixed_point_checks 59700 cyclic_vectors 5978 orbit_censuses 160`. These are finite corroborations, not substitutes for the all-size proof above.

## Relationship to prior work
Macauley and Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412v1, prove update-order cycle-equivalence criteria and the general cycle-graph upper bound \(n-1\) for their orientation equivalence classes. That upper bound does **not** determine Rule-60 characteristic polynomials or count its fixed points at every iterate; linear similarity also differs from unlabelled cycle equivalence.

Macauley, McCammond and Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238v2, Section 5, explicitly identify Rule-60 local transvections and the group they generate as \(\mathrm{SL}_n(\mathbb F_2)\). Their full-group result does not supply the characteristic and minimal polynomial of every **single permutation sweep**, nor the resulting exact sweep-by-sweep orbit census.

Jae-Gyeom Kim, *Characteristic Matrices of Cellular Automata with Rule 60 and Intermediate Boundary Condition*, DOI 10.14403/jcms.2015.28.4.545, addresses different boundary and update conventions according to its available abstract. Its full text was not available for inspection; that comparison remains a stated priority risk.

## Limitations
The result applies to sequential, one-pass Rule-60 schedules on finite cyclic rings, not arbitrary repeated-site schedules, synchronous Rule 60, or other local rules. It does not assert that the \(n-1\) linear similarity classes are distinct as abstract permutations; reciprocal polynomials can have identical periodic orbit counts. Priority against all potentially inaccessible historical literature has not been independently established. Experimental tests cover finite dimensions and return times, whereas the proof covers every permitted parameter.

## References
1. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412v1 (first posted 2008-02-29), https://arxiv.org/abs/0802.4412.
2. M. Macauley, J. McCammond and H. S. Mortveit, *Dynamics Groups of Asynchronous Cellular Automata*, arXiv:0808.1238v1 (first posted 2008-08-08), https://arxiv.org/abs/0808.1238.
3. J.-G. Kim, *Characteristic Matrices of Cellular Automata with Rule 60 and Intermediate Boundary Condition*, Journal of the Chungcheong Mathematical Society 28 (2015), 545–551, DOI:10.14403/jcms.2015.28.4.545 (abstract consulted; full text not inspected).
