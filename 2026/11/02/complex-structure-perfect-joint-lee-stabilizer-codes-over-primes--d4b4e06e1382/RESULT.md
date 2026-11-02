# Complex-structure perfect joint-Lee stabilizer codes over primes congruent to three modulo four

## Finding
For each odd prime \(p\equiv3\pmod4\) and even integer \(r\ge2\), apart from \((p,r)=(3,2)\), there is an explicit nondegenerate stabilizer code
\[
\left[\!\left[\frac{p^r-1}{4},\frac{p^r-1}{4}-r,3_{\diamond}\right]\!\right]_p
\]
that corrects all single elementary shifts \(X_i^{\pm1}\) and \(Z_i^{\pm1}\). Its joint-Lee radius-one ball has exactly \(1+4n=p^r\) errors, each with a distinct syndrome, so the code is perfect in that metric. Examples include \([[12,10,3_{\diamond}]]_7\), \([[20,16,3_{\diamond}]]_3\), and \([[30,28,3_{\diamond}]]_{11}\). These parameters concern joint Lee distance, not standard quantum Hamming distance.

## Assumptions and scope
Let \(V=\mathbb F_p^r\), with \(p\) an odd prime congruent to \(3\) modulo \(4\) and \(r\) even. Work with \(p\)-level qudits, Pauli errors \(X^aZ^b\), and joint Lee weight \(\sum_i(\operatorname{Lee}_p(a_i)+\operatorname{Lee}_p(b_i))\), with \(\operatorname{Lee}_p(c)=\min\{c,p-c\}\) for the representative \(0\le c<p\). The elementary errors of joint Lee weight one are exactly \(X_i^{\pm1}\) and \(Z_i^{\pm1}\).

Define the invertible linear map \(J:V\to V\) as the direct sum of \(r/2\) rotations \((x,y)\mapsto(-y,x)\). Hence \(J^2=-I\). Because \(-1\) is not a square in \(\mathbb F_p\), \(J\) has no eigenvectors over \(\mathbb F_p\); for each nonzero \(v\), the four vectors \(v,Jv,-v,-Jv\) are distinct. Fix one representative \(v_i\) from every orbit under \(\langle J\rangle\); there are \(n=(p^r-1)/4\) orbits, indexed by \(1\le i\le n\). Write \(w_i=Jv_i\).

Let the \(r\)-row stabilizer-check matrix \(H=(H_X\mid H_Z)\) have its \(i\)-th \(X\) column equal to \(w_i\) and its \(i\)-th \(Z\) column equal to \(-v_i\). The Pauli commutator is determined by \(H_XH_Z^\mathsf T-H_ZH_X^\mathsf T\). With this convention an elementary \(X_i\) has syndrome \(v_i\), and \(Z_i\) has syndrome \(w_i\), up to an inessential global sign convention.

## Proof
**Four-orbit partition.** The polynomial \(T^2+1\) has no root in \(\mathbb F_p\); therefore no nonzero \(v\) satisfies \(Jv=\pm v\). Since \(J^2=-I\), every nonzero \(J\)-orbit has size exactly four. The \(4n\) vectors \(\{\pm v_i,\pm Jv_i\}\) partition \(V\setminus\{0\}\).

**Commutativity.** Define the alternating matrix
\[
T(v)=v(Jv)^\mathsf T-(Jv)v^\mathsf T.
\]
Direct substitution using \(J^2=-I\) gives \(T(Jv)=T(v)\), so
\[
4\sum_{i=1}^n T(v_i)=\sum_{v\in V}T(v).
\]
For each pair of coordinate indices \(a,b\), the sum \(\sum_{v\in V}v_av_b\) is zero in \(\mathbb F_p\): if \(a\ne b\), a factor \(\sum_{t\in\mathbb F_p}t=0\) occurs; if \(a=b\), the remaining \(r-1\ge1\) free coordinates contribute a factor \(p=0\). Thus \(\sum_v vv^\mathsf T=0\), whence \(\sum_v T(v)=0\). As \(4\) is invertible, \(\sum_i T(v_i)=0\), equivalently
\[
H_XH_Z^\mathsf T-H_ZH_X^\mathsf T=0.
\]
Therefore the \(r\) stabilizer rows commute, with phases chosen in the usual odd-prime Weyl convention. The columns of \(H\) span \(V\), since their signed versions cover every nonzero vector, so \(\operatorname{rank} H=r\). The resulting stabilizer code has \(n-r\) logical qudits.

**Perfect radius-one decoding and distance lower bound.** The syndromes of \(X_i^{\pm1}\) and \(Z_i^{\pm1}\) are the distinct vectors \(\pm v_i\) and \(\pm w_i\). They exhaust the \(p^r-1\) nonzero syndromes. Together with the identity, they make \(1+4n=p^r\) disjoint syndrome classes; radius-one correction is perfect. Every nonidentity Pauli error of joint-Lee weight at most two decomposes into at most two elementary errors. If such an error had zero syndrome, the two elementary syndromes would have to be opposites, so the elementary errors would cancel as Pauli exponents (up to a global phase). This is impossible for a nonidentity error. Consequently \(d_{\diamond}\ge3\).

**Exact upper bound and exclusion from the stabilizer.** Fix one orbit representative \(v=v_i\) and put \(w=Jv\). The nonzero vector \(-v-w\) is in the radius-one syndrome partition, hence labels an elementary shift on some qudit \(j\). The vectors \(v+w\) and \(\pm v,\pm w\) are distinct because \(v,w\) are linearly independent; thus \(j\ne i\). Multiplying \(X_iZ_i\) by the elementary shift with syndrome \(-v-w\) produces a zero-syndrome Pauli error \(E\) of joint-Lee weight exactly three, supported on two physical qudits.

To show \(E\) is not a stabilizer, consider any nonzero linear combination of stabilizer rows, indexed by \(a\in V\setminus\{0\}\). The corresponding Pauli vector on qudit \(i\) is nonzero whenever at least one of \(a\cdot v_i\) and \(a\cdot Jv_i\) is nonzero. Exactly \((p-1)p^{r-1}\) vectors \(u\in V\) satisfy \(a\cdot u\ne0\). Each orbit can contain at most four such vectors, so every nonidentity stabilizer acts on at least
\[
\left\lceil\frac{(p-1)p^{r-1}}4\right\rceil
\]
physical qudits. This bound exceeds two when \(p\equiv3\pmod4\), \(r\ge2\) is even, and \((p,r)\ne(3,2)\). Thus \(E\) is not in the stabilizer and represents a nontrivial logical operator: \(d_{\diamond}\le3\). Combining both inequalities gives \(d_{\diamond}=3\). The excluded \((3,2)\) parameter has \(n=r=2\) and zero logical qudits, so it is not asserted to have a logical distance.

## Verification
The standalone standard-library program `verify.py` independently forms the orbits, constructs the check matrix, confirms full row rank, evaluates every symplectic commutator, checks all \(p^r-1\) distinct elementary-error syndromes, constructs a weight-three zero-syndrome witness, and exhaustively measures physical supports of all \(p^r-1\) nontrivial stabilizers for \((p,r)=(3,2),(3,4),(3,6),(7,2),(11,2),(19,2)\). Run with `python3 verify.py`; the expected output is stored in `verify_output.txt`, ending with `COMPLEX_STRUCTURE_LEE_VERIFY_OK`. These finite checks corroborate the algebraic proof; they are not an infinite-family certificate.

## Relationship to prior work
Guo, Han, Chakraborty, Jain, Liu, Albert and Lucas (2026) introduced the joint Lee stabilizer metric and gave an isolated \([[6,4,3_{\diamond}]]_5\) perfect example alongside short-length composite-dimension constructions. Their Section 3.1 and Table 2 do not present the even-rank complex-structure orbit construction for odd primes \(p\equiv3\pmod4\). Matsumoto (2021) studies quantum Lee weights and CSS constructions with separately controlled bit/phase components; those results use a different correction criterion and do not imply the claimed non-CSS joint-Lee syndrome partition. Known symplectic equivalences remain a priority-search risk. The result uses standard finite-field and stabilizer linear algebra but supplies an explicit cancellation mechanism specific to this syndrome design.

## Limitations
The family requires prime dimensions \(p\equiv3\pmod4\), even check rank \(r\), and \(n>r\); it makes no assertion for odd \(r\), or other alphabet dimensions. The code corrects single \(X\)- or \(Z\)-shifts in the joint Lee metric, not all single-qudit Pauli errors in the standard quantum Hamming metric. It does not establish efficient encoding, fault tolerance, quantum Hamming distance, or physical-noise performance. Priority against unindexed or differently parametrized earlier symplectic constructions is not independently established.

## References
1. J. Guo, Y. Han, A. Chakraborty, S. P. Jain, T. Liu, V. V. Albert and A. Lucas, *Quantum codes in the Lee metric*, arXiv:2610.04834 (first submitted 2026-10-04), especially Section 3.1 and Table 2. https://arxiv.org/abs/2610.04834
2. R. Matsumoto, *Lee Weight for Nonbinary Quantum Error Correction*, arXiv:2105.12354 (2021), especially Sections 2 and 4. https://arxiv.org/abs/2105.12354
