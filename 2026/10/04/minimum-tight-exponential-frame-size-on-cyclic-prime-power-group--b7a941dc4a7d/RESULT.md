# Minimum tight exponential-frame size on cyclic prime-power groups
## Finding
Let \(p\) be prime, let \(k\ge 1\), put \(G=\mathbb Z/p^k\mathbb Z\), and let \(A\subseteq G\) be nonempty. For every nonzero residue \(d\in G\), define \(v_p(d)\in\{0,\ldots,k-1\}\) to be the largest integer \(v\) such that \(p^v\) divides an integer representative of \(d\). Define
\[
R(A)=\{v_p(a-a'):a,a'\in A,\ a\ne a'\}.
\]
Then the minimum cardinality of a frequency set \(B\subseteq G\) for which the restricted characters
\[
x\longmapsto \exp(2\pi i b x/p^k),\qquad b\in B,
\]
form a tight frame for \(\mathbb C^A\) with counting inner product is exactly
\[
p^{|R(A)|}.
\]

More precisely, set
\[
S(A)=\{k-v:v\in R(A)\}
\]
and let \(P_B(X)=\sum_{b\in B}X^b\). Tightness is equivalent to the simultaneous cyclotomic divisibilities
\[
\Phi_{p^s}(X)\mid P_B(X)\qquad(s\in S(A)).
\]
The minimum is attained by the explicit digit set
\[
B_A=\left\{\sum_{s\in S(A)}c_s p^{s-1}:0\le c_s<p\right\},
\]
which has \(|B_A|=p^{|R(A)|}\) and tight-frame bound \(p^{|R(A)|}\). When \(|A|=1\), the set \(R(A)\) is empty and the formula gives the correct minimum \(1\).

## Assumptions and scope
The ambient group is the cyclic prime-power group \(G=\mathbb Z/p^k\mathbb Z\). Frequencies are distinct residues, so \(B\) is a set rather than a multiset. The Hilbert space \(\mathbb C^A\) uses the counting inner product. Characters are unnormalized; therefore a tight frequency set of cardinality \(|B|\) has frame bound \(|B|\).

The invariant \(R(A)\) records only the distinct \(p\)-adic scales occurring among nonzero differences of points of \(A\). The theorem does not classify every cardinality larger than the minimum, nor does it address non-prime-power cyclic groups or weighted frequency multisets.

## Proof
Let \(\zeta=\exp(2\pi i/p^k)\), and form the evaluation matrix \(F\) indexed by \(A\times B\), with
\[
F_{a,b}=\zeta^{ab}.
\]
The restricted characters indexed by \(B\) form a tight frame exactly when the row Gram matrix is a scalar multiple of the identity. Its diagonal entries are \(|B|\), while for distinct \(a,a'\in A\) the corresponding off-diagonal entry is
\[
\sum_{b\in B}\zeta^{b(a-a')}=P_B(\zeta^{a-a'}).
\]
Thus tightness is equivalent to \(P_B(\zeta^d)=0\) for every nonzero difference \(d=a-a'\).

Fix such a difference and write \(v=v_p(d)\). The root \(\zeta^d\) has exact order \(p^{k-v}\). Its minimal polynomial over \(\mathbb Q\) is therefore \(\Phi_{p^{k-v}}(X)\). Since \(P_B(X)\in\mathbb Z[X]\),
\[
P_B(\zeta^d)=0
\quad\Longleftrightarrow\quad
\Phi_{p^{k-v}}(X)\mid P_B(X).
\]
Taking all difference scales gives the stated equivalence with divisibility by \(\Phi_{p^s}\) for every \(s\in S(A)\).

Distinct cyclotomic polynomials are pairwise coprime and monic, so
\[
\prod_{s\in S(A)}\Phi_{p^s}(X)\mid P_B(X)
\]
in \(\mathbb Z[X]\). Evaluating at \(X=1\), and using \(\Phi_{p^s}(1)=p\), gives
\[
p^{|S(A)|}\mid P_B(1)=|B|.
\]
Since \(|S(A)|=|R(A)|\) and \(B\ne\varnothing\), every tight frequency set satisfies
\[
|B|\ge p^{|R(A)|}.
\]

For the reverse inequality, use the digit set \(B_A\) above. Its mask polynomial is
\[
P_{B_A}(X)
 =\prod_{s\in S(A)}\left(1+X^{p^{s-1}}+\cdots+X^{(p-1)p^{s-1}}\right)
 =\prod_{s\in S(A)}\Phi_{p^s}(X).
\]
The exponents in the product are distinct because they are base-\(p\) numbers with independently chosen digits precisely in the positions \(s-1\), so every coefficient is either \(0\) or \(1\), and the polynomial is exactly the mask of a subset of \(G\). It follows that \(|B_A|=p^{|S(A)|}=p^{|R(A)|}\), and the required divisibilities show that \(B_A\) is tight. This proves both optimality and the explicit construction.

## Verification
The accompanying `verify.py` uses exact integer polynomial arithmetic. It reconstructs the required cyclotomic divisibility criterion, exhausts every nonempty spatial set and every nonempty frequency set for \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/8\mathbb Z\), and \(\mathbb Z/9\mathbb Z\), and verifies that the smallest tight frequency cardinality is always the predicted \(p^{|R(A)|}\). It also checks the explicit construction on selected larger examples in \(\mathbb Z/32\mathbb Z\), \(\mathbb Z/27\mathbb Z\), \(\mathbb Z/25\mathbb Z\), and \(\mathbb Z/49\mathbb Z\).

A replay returned:

`VERIFY_OK exhaustive_A=781 larger_cases=4`

The finite replay is not used as an infinite proof; the general theorem follows from the Gram-matrix and cyclotomic-divisibility argument above.

## Relationship to prior work
Frederick and Mayeli introduce finite frame spectral pairs and develop construction and lifting results for finite exponential frames. Their framework supplies the natural matrix formulation used here, but the inspected preprint does not state a prime-power classification by distinct \(p\)-adic difference scales or the exact minimum \(p^{|R(A)|}\).

Lam and Leung study vanishing sums of roots of unity, providing general structural background for restrictions on their lengths. Malikiosis studies spectral and tiling subsets of cyclic groups and uses cyclotomic divisibility extensively. Those results motivate the cyclotomic step, but the statement proved here concerns oversampled tight exponential frames for an arbitrary subset \(A\), with an exact minimum and a canonical digit-set optimizer; it is not a spectral-set or tiling classification.

## Limitations
The result is specific to cyclic groups of prime-power order. It does not determine the full set of feasible oversampling cardinalities above the minimum, and it does not classify all minimizing frequency sets. The literature comparison did not locate an equivalent theorem, but an obscure equivalent formulation in the broader literature on finite harmonic frames or cyclotomic masks remains a residual originality risk.

## References
1. G. Frederick and A. Mayeli, *Frame spectral pairs and exponential bases*, arXiv:2010.05667; Journal of Fourier Analysis and Applications 27 (2021), DOI 10.1007/s00041-021-09872-9.
2. T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, Journal of Algebra 224 (2000), DOI 10.1006/jabr.1999.8089.
3. R.-D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma 10 (2022), DOI 10.1017/fms.2022.14.
